"""Exact, dependency-free verifier of the binary two-list/two-deletion certificate.
Run: python verify.py CERTIFICATE.json
The arithmetic uses fractions and integer bitsets only; no optimizer or network.
"""
import json,sys
from itertools import combinations
from fractions import Fraction
from collections import Counter

def parents(n):
    out=[]
    for x in range(1<<n):
        bits=f'{x:0{n}b}'
        ys=set()
        for p,q in combinations(range(n),2):
            ys.add(int(''.join(bits[j] for j in range(n) if j!=p and j!=q) or '0',2))
        out.append(ys)
    return out

def dual_upper(n, P, y, caps=None, eligible=None, fixed_count=0):
    if caps is None: caps=[2]*(1<<(n-2))
    if eligible is None: eligible=range(1<<n)
    weights=[Fraction(0)]*(1<<(n-2));seen=set()
    for j,num,den in y:
        assert 0<=j<len(weights) and j not in seen and den>0 and num>0
        weights[j]=Fraction(num,den);seen.add(j)
    upper=Fraction(fixed_count)+sum((caps[j]*weights[j] for j in range(len(weights))),Fraction(0))
    for i in eligible:
        cost=sum((weights[j] for j in P[i]),Fraction(0))
        upper+=max(Fraction(0),Fraction(1)-cost)
    return upper

def valid_code(P, idx):
    assert len(idx)==len(set(idx))
    counts=Counter(j for i in idx for j in P[i])
    assert not any(v>2 for v in counts.values())

def verify_tree(P, tree, goal):
    n=8;N=1<<n;K=1<<(n-2)
    masks=[sum(1<<i for i in range(N) if j in P[i]) for j in range(K)]
    stats=Counter();max_depth=0;max_bound=Fraction(0)
    def recur(node,one,zero,depth):
        nonlocal max_depth,max_bound
        max_depth=max(max_depth,depth); stats['nodes']+=1
        cap=[2-sum((one>>i)&1 for i in range(N) if j in P[i]) for j in range(K)]
        if min(cap)<0:
            assert node==['infeasible'];stats['infeasible']+=1;return
        for j,c in enumerate(cap):
            if c==0:zero|=masks[j]&~one
        if one&zero:
            assert node==['infeasible'];stats['infeasible']+=1;return
        free=[i for i in range(N) if not ((one|zero)>>i)&1]
        if one.bit_count()+len(free)<goal:
            assert node==['cardinality'];stats['cardinality']+=1;return
        tag=node[0]
        if tag=='dual':
            assert len(node)==2
            bound=dual_upper(n,P,node[1],caps=cap,eligible=free,fixed_count=one.bit_count())
            assert bound<goal,(bound,one,zero)
            max_bound=max(max_bound,bound)
            stats['dual']+=1
        else:
            assert tag=='branch' and len(node)==4
            i=node[1];assert type(i) is int and 0<=i<N and not ((one|zero)>>i)&1
            recur(node[2],one|(1<<i),zero,depth+1)
            recur(node[3],one,zero|(1<<i),depth+1)
            stats['branch']+=1
    recur(tree,0,0,0)
    return stats,max_depth,max_bound

def main(filename):
    with open(filename,'rb') as f: cert=json.loads(f.read().decode('utf8'))
    assert cert['schema']=='binary-two-list-two-deletion-branch-proof-v1'
    assert (cert['k'],cert['t'])==(2,2)
    expected={2:2,3:3,4:4,5:4,6:7,7:11}
    for item in cert['earlier']:
        n=item['n']; assert n in expected
        P=parents(n);w=item['witness']; assert len(w)==expected[n]
        assert all(0<=v<(1<<n) for v in w);valid_code(P,w)
        upper=dual_upper(n,P,item['dual_y'])
        assert upper<expected[n]+1
        print(f'EARLIER n={n} integer_opt={len(w)} LP_dual_upper={upper}')
    assert {i['n'] for i in cert['earlier']}==set(expected)
    P=parents(8);record=cert['n8'];w=record['integer_witness']
    assert len(w)==15 and all(0<=v<256 for v in w);valid_code(P,w)
    frac=[Fraction(0)]*256;seen=set()
    for i,num,den in record['fractional_x']:
        assert i not in seen and 0<=i<256 and den>0 and num>0
        seen.add(i);frac[i]=Fraction(num,den)
    assert all(Fraction(0)<=v<=Fraction(1) for v in frac)
    for j in range(64):
        assert sum((frac[i] for i in range(256) if j in P[i]),Fraction(0))<=2
    lp_lower=sum(frac,Fraction(0))
    lp_upper=dual_upper(8,P,record['root_dual_y'])
    assert lp_lower==lp_upper and lp_lower>16
    assert record['target_infeasible']==16
    stats,depth,mx=verify_tree(P,record['tree'],16)
    assert stats['branch']+stats['dual']+stats['cardinality']+stats['infeasible']==stats['nodes']
    print(f'N8_INTEGER_OPTIMUM=15 N8_LP_OPTIMUM={lp_lower}')
    print('CERTIFIED_SEARCH',dict(stats),'depth',depth,'largest_dual_leaf_bound',mx)
    print('EXACT_TWO_LIST_TWO_DELETION_CERTIFICATE_OK')
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'CERTIFICATE.json')
