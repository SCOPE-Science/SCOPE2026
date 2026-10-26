"""Exact finite checks for epidemic-source thresholds on broom contact trees."""
from fractions import Fraction as Q
from collections import deque
import json
from itertools import product


def value(m,L,j,p):
    return sum((p**abs(i-j) for i in range(L+1)),Q(0)) + m*p**(j+1)


def leaf(m,L,p):
    return 1+p+sum((p**(i+1) for i in range(1,L+1)),Q(0)) + (m-1)*p*p


def all_nodes(m,L,p):
    return [value(m,L,j,p) for j in range(L+1)] + [leaf(m,L,p)]*m


def brute(m,L,p):
    # label path 0..L, hub leaves L+1..L+m
    eds=[(i,i+1) for i in range(L)]+[(0,L+i+1) for i in range(m)]
    out=[Q(0)]*(L+1+m)
    E=len(eds)
    for mask in range(1<<E):
        prob=p**mask.bit_count()*(1-p)**(E-mask.bit_count())
        adj=[[] for i in range(L+1+m)]
        for ei,(u,v) in enumerate(eds):
            if (mask>>ei)&1: adj[u].append(v); adj[v].append(u)
        for s in range(len(adj)):
            seen={s};queue=deque([s])
            while queue:
                for nxt in adj[queue.popleft()]:
                    if nxt not in seen: seen.add(nxt);queue.append(nxt)
            out[s]+=prob*len(seen)
    return out


def sign(x): return (x>0)-(x<0)


def pred(m,L,p):
    R=max(0,(L-m)//2)
    j=0
    for i in range(R):
        k=L-2*i-1
        Sk=sum((p**q for q in range(k)),Q(0))
        if Sk>m:j=i+1
        elif Sk==m:return [i,i+1]
    return [j]


def run():
    checks={'tested_parameter_sets':0,'edge_state_enumerations':0,'source_values_checked':0,'adjacent_sign_tests':0,'argmax_tests':0,'threshold_bracket_checks':0}
    for m in range(2,5):
        for L in range(1,7):
            for p in [Q(1,7),Q(2,5),Q(1,2),Q(4,5),Q(9,10)]:
                observed=brute(m,L,p);formula=all_nodes(m,L,p)
                assert observed==formula,(m,L,p,observed,formula)
                checks['tested_parameter_sets']+=1
                checks['edge_state_enumerations']+=1<<(m+L)
                checks['source_values_checked']+=len(observed)
                winning=[i for i,x in enumerate(formula) if x==max(formula)]
                assert winning==pred(m,L,p),(m,L,p,winning,pred(m,L,p))
                checks['argmax_tests']+=1
                for j in range(L):
                    d=formula[j+1]-formula[j]
                    k=L-2*j-1
                    e=p**(j+1)*(1-p**k - m*(1-p))
                    assert d==e
                    checks['adjacent_sign_tests']+=1
    # all root intervals must be nonempty, found by rational-grid bisection
    for m in range(2,8):
        for L in range(m+2,m+27):
            R=(L-m)//2
            thresholds=[]
            for j in range(R):
                k=L-2*j-1
                lo=Q(0);hi=Q(1)
                for _ in range(50):
                    mid=(lo+hi)/2
                    S=sum((mid**i for i in range(k)),Q(0))
                    if S>m:hi=mid
                    else:lo=mid
                thresholds.append((lo,hi))
                checks['threshold_bracket_checks']+=1
            for j in range(R-1):
                assert thresholds[j][1]<thresholds[j+1][0]
    return checks

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,separators=(',',':')))
