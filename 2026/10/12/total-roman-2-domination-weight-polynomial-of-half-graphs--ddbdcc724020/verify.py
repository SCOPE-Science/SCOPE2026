#!/usr/bin/env python3
"""Exact checks for total Roman {2}-domination of bipartite half graphs.

Only standard-library integer arithmetic is used. Invocation: python3 verify.py
"""
from itertools import product
from math import comb


def add(a,b):
    r=[0]*max(len(a),len(b))
    for i,v in enumerate(a):r[i]+=v
    for i,v in enumerate(b):r[i]+=v
    return r


def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        if u:
            for j,v in enumerate(b):r[i+j]+=u*v
    return r


def power(a,k):
    r=[1]
    for _ in range(k):r=mul(r,a)
    return r


def scale(a,k):return [k*v for v in a]


def shift(a,k):return [0]*k+a


def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def formula(n):
    assert n>=2
    z2=[0,0,1]
    alpha=[1,2,3,2,1]
    beta=[0,1,1]
    part1=shift(power(alpha,n-1),4)
    part2=power(beta,n-1)
    for r in range(1,n):
        part2=add(part2,mul(power(alpha,r-1),power(beta,n-r+1)))
    part2=shift(scale(part2,2),3)
    part3=scale(power(beta,n),n-1)
    for d in range(0,n-2):
        part3=add(part3,scale(mul(power(alpha,d),power(beta,n+1-d)),n-2-d))
    part3=shift(part3,2)
    return trim(add(add(part1,part2),part3))


def graph_adjacency(n):
    return [[n+j for j in range(i,n)] for i in range(n)] + [list(range(j+1)) for j in range(n)]


def directly_legal(labels,adj):
    # Uses the vertex-neighborhood definition, not endpoint shortcuts.
    for v,neighbors in enumerate(adj):
        if labels[v]==0:
            if sum(labels[u] for u in neighbors)<2:return False
        elif not any(labels[u]>0 for u in neighbors):return False
    return True


def brute_polynomial(n):
    adj=graph_adjacency(n)
    values=[0]*(4*n+1)
    count=0
    for labels in product((0,1,2), repeat=2*n):
        count+=1
        if directly_legal(labels,adj):values[sum(labels)]+=1
    return trim(values),count


def transfer_polynomial(n):
    # Prefix A total and suffix B total, capped at two; a nine-state boundary check.
    states=tuple(product(range(3),repeat=2))
    trans={}
    for p,q in states:
        opts=[]
        for pp,qq in states:
            for a,b in product(range(3),repeat=2):
                if min(2,p+a)!=pp or min(2,b+qq)!=q:continue
                if a==0 and q!=2 or a>0 and q==0:continue
                if b==0 and pp!=2 or b>0 and pp==0:continue
                opts.append((pp,qq,a+b))
        trans[p,q]=opts
    d={(0,q,w):1 for q in range(3) for w in [0]}
    for _ in range(n):
        next_d={}
        for (p,q,w),c in d.items():
            for pp,qq,wt in trans[p,q]:
                key=(pp,qq,w+wt)
                next_d[key]=next_d.get(key,0)+c
        d=next_d
    values=[0]*(4*n+1)
    for (p,q,w),c in d.items():
        if q==0:values[w]+=c
    return trim(values)


def main():
    total_candidates=0
    for n in range(2,8):
        brute,checked=brute_polynomial(n)
        expected=formula(n)
        dp=transfer_polynomial(n)
        assert brute==expected==dp,(n,brute,expected,dp)
        total_candidates+=checked
        print('exhaustive',n,'assignments',checked,'TR2DF',sum(brute),'min_weight',next(i for i,x in enumerate(brute) if x),'min_count',next(x for x in brute if x),'PASS')
    for n in range(8,19):
        left=formula(n)
        right=transfer_polynomial(n)
        assert left==right,('matrix-coefficients',n)
        assert left[4]==1,(n,'minimum')
        # The derived total-count identity holds for every n >= 2.
        expected=(121*9**n+(189*n-72)*2**n)//441
        assert (121*9**n+(189*n-72)*2**n)%441==0
        assert sum(left)==expected,(n,'total')
        print('transfer-versus-formula',n,'coefficients',len(left),'total',expected,'PASS')
    for n in range(2,8):
        expected=(121*9**n+(189*n-72)*2**n)//441
        assert sum(formula(n))==expected
    print('TOTAL exhaustive assignments',total_candidates)
    print('FINAL PASS: all independent brute-force, transfer, finite-sum and total-count checks')

if __name__=='__main__':main()
