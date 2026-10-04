#!/usr/bin/env python3
from itertools import product


def forward_children(x):
    n=len(x)
    out=set()
    for i in range(n):
        for t in range(i+1,n+1):
            out.add(x[:t]+(x[i],)+x[t:])
    return out


def inverse_parents(y):
    out=set()
    for j in range(1,len(y)):
        if y[j] in y[:j]:
            out.add(y[:j]+y[j+1:])
    return out


def runs(y):
    rs=[]
    i=0
    while i<len(y):
        j=i+1
        while j<len(y) and y[j]==y[i]:
            j+=1
        rs.append((y[i],j-i))
        i=j
    return rs


def run_formula(y):
    rs=runs(y)
    first={}
    for a,L in rs:
        if a not in first:
            first[a]=L
    s=sum(1 for L in first.values() if L==1)
    return len(rs)-s


def edge_formula(q,n):
    return q**n*((q-1)*n-q*(q-2))+q*(q-2)*(q-1)**n


def equality_shape(y):
    rs=runs(y)
    if len(set(y))!=2 or len(rs)<2:
        return False
    return rs[0][1] in (1,2) and rs[1][1] in (1,2) and all(L==1 for _,L in rs[2:])


def direct_check(q,n):
    alphabet=tuple(range(q))
    N=n+1
    parent_to_children={x:forward_children(x) for x in product(alphabet, repeat=n)}
    inverse={y:set() for y in product(alphabet, repeat=N)}
    edge_pairs=set()
    for x,cs in parent_to_children.items():
        for y in cs:
            inverse[y].add(x)
            edge_pairs.add((x,y))
    maxdeg=0
    maxwords=[]
    for y,ps in inverse.items():
        ip=inverse_parents(y)
        assert ps==ip, (q,n,y,ps,ip)
        assert len(ps)==run_formula(y), (q,n,y,len(ps),run_formula(y))
        if len(ps)>maxdeg:
            maxdeg=len(ps); maxwords=[y]
        elif len(ps)==maxdeg:
            maxwords.append(y)
    theorem_max=1 if n==1 else n-1
    assert maxdeg==theorem_max, (q,n,maxdeg,theorem_max)
    assert len(edge_pairs)==edge_formula(q,n), (q,n,len(edge_pairs),edge_formula(q,n))
    if n>=3:
        for y in inverse:
            assert (len(inverse[y])==theorem_max)==equality_shape(y), (q,n,y,len(inverse[y]),runs(y))
    return len(inverse), len(edge_pairs)


def witness_check():
    count=0
    for q in range(2,9):
        for n in range(2,51):
            y=tuple(i%2 for i in range(n+1))
            assert run_formula(y)==n-1
            ef=edge_formula(q,n)
            assert isinstance(ef,int) and ef>0
            count+=1
    return count


def main():
    cases=0; received=0; edges=0
    for q in range(2,5):
        for n in range(1,6):
            w,e=direct_check(q,n)
            cases+=1; received+=w; edges+=e
    witnesses=witness_check()
    print(f"VERIFY_OK exhaustive_cases={cases} received_words={received} distinct_edges={edges} witness_grid={witnesses} q<=8_n<=50")


if __name__=='__main__':
    main()
