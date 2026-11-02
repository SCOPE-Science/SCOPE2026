#!/usr/bin/env python3
"""Finite-field arithmetic checks for commuting retractions of free class-two Lie algebras.

No dependencies other than the Python standard library. The direct enumerator uses
full linear matrices for all homomorphisms, rather than the weight-space proof.
"""
from itertools import product
from math import factorial, comb


def gl(n,q):
    return 1 if n==0 else __import__('math').prod(q**n-q**i for i in range(n))


def prediction(n,q,k):
    d=comb(n,2)
    total=0
    colors=2**k
    def recurse(dim,i,assigned):
        nonlocal total
        if i==colors-1:
            choices=assigned+[dim]
        else:
            for a in range(dim+1):
                recurse(dim-a,i+1,assigned+[a])
            return
        # W weight at each color is pairwise bitwise-AND of V colors.
        w=[comb(choices[s],2) for s in range(colors)]
        for s in range(colors):
            for t in range(s+1,colors):
                w[s&t] += choices[s]*choices[t]
        exponent=n*d-sum(choices[s]*w[s] for s in range(colors))
        assert exponent>=0, (n,q,k,choices,exponent)
        orbit=gl(n,q)
        denominator=__import__('math').prod(gl(a,q) for a in choices)
        assert orbit%denominator==0
        total+=(orbit//denominator)*q**exponent
    recurse(n,0,[])
    return total


def wedge(columns,n,q):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    out=[]
    for (i,j) in pairs:
        out.append(tuple((columns[i][a]*columns[j][b]-columns[i][b]*columns[j][a])%q for a,b in pairs))
    return out


def linear_action(columns,vec,q):
    length=len(vec)
    return tuple(sum(vec[j]*columns[j][i] for j in range(length))%q for i in range(length))


def enumerate_idempotents(n,q):
    d=comb(n,2); length=n+d
    vectors=list(product(range(q),repeat=n))
    for A in product(vectors,repeat=n):
        if any(linear_action(A,A[i],q)!=A[i] for i in range(n)):
            continue
        D=wedge(A,n,q)
        for bflat in product(range(q),repeat=n*d):
            B=[tuple(bflat[d*i:d*(i+1)]) for i in range(n)]
            cols=tuple(tuple(A[i])+tuple(B[i]) for i in range(n))+tuple((0,)*n+tuple(D[j]) for j in range(d))
            if all(linear_action(cols,cols[i],q)==cols[i] for i in range(length)):
                yield cols


def action_table(columns,q):
    length=len(columns)
    vecs=list(product(range(q),repeat=length))
    lookup={vec:i for i,vec in enumerate(vecs)}
    cols_indices=[lookup[c] for c in columns]
    return cols_indices,tuple(lookup[linear_action(columns,v,q)] for v in vecs)


def graph_counts(n,q,triangles=False):
    cols=list(enumerate_idempotents(n,q))
    N=len(cols)
    table=[action_table(c,q) for c in cols]
    adj=[0]*N
    for i in range(N):
        ci,ai=table[i]
        for j in range(i+1,N):
            cj,aj=table[j]
            if all(ai[cj[t]]==aj[ci[t]] for t in range(n+comb(n,2))):
                adj[i]|=1<<j; adj[j]|=1<<i
    E=sum(x.bit_count() for x in adj)//2
    T2=N+2*E
    out={'n':n,'q':q,'idempotents':N,'commuting_ordered_pairs':T2,'edges':E}
    assert N==prediction(n,q,1),(out,prediction(n,q,1))
    assert T2==prediction(n,q,2),(out,prediction(n,q,2))
    if n==2:
        # Independent maximal-clique enumeration from the entire graph.
        count=0
        sizes=set()
        def bk(R,P,X):
            nonlocal count
            if not P and not X:
                count+=1
                sizes.add(R.bit_count())
                return
            U=P|X
            pivot=max((i for i in range(N) if U>>i&1),key=lambda i:(P&adj[i]).bit_count(),default=-1)
            candidates=P & ~(adj[pivot] if pivot>=0 else 0)
            while candidates:
                bit=candidates&-candidates; v=bit.bit_length()-1
                bk(R|bit,P&adj[v],X&adj[v])
                P-=bit;X|=bit;candidates-=bit
        bk(0,(1<<N)-1,0)
        predicted=q**(n*comb(n,2))*gl(n,q)//(factorial(n)*(q-1)**n)
        assert count==predicted and sizes=={2**n},(count,sizes,predicted)
        out.update(maximal_cliques=count,maximal_clique_sizes=sorted(sizes))
    if triangles:
        triangles_count=0
        for i in range(N):
            greater_i=adj[i]&~((1<<(i+1))-1)
            while greater_i:
                lsb=greater_i&-greater_i
                j=lsb.bit_length()-1
                triangles_count += (adj[i]&adj[j]&~((1<<(j+1))-1)).bit_count()
                greater_i-=lsb
        T3=N+6*E+6*triangles_count
        assert T3==prediction(n,q,3),(out,T3,prediction(n,q,3))
        out.update(triangles=triangles_count,commuting_ordered_triples=T3)
    return out


def main():
    # Independent direct algebra maps, all tuples up to arity three.
    for n,q in [(2,2),(2,3),(3,2)]:
        out=graph_counts(n,q,triangles=True)
        print(out)
    for n in range(1,7):
        for k in (0,1,2,3):
            assert prediction(n,2,k)>=1
    print('VERIFY_OK')

if __name__=='__main__':main()
