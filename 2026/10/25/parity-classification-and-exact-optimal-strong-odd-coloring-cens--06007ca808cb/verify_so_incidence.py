"""Exact independently formulated vertex-coloring checks for small incidence graphs.
This code is scientific/reproducibility-only; no external services required.
"""
from itertools import product
from collections import Counter

def strong_odd(color, N):
    for v,nbs in enumerate(N):
        if any(color[v]==color[w] for w in nbs):return False
        if any(c%2==0 for c in Counter(color[w] for w in nbs).values()):return False
    return True

def graph(p,q):
    N=[[] for _ in range(p+q+p*q)]
    for i in range(p):
        for j in range(q):
            w=p+q+i*q+j
            a=i;b=p+j
            for v in (a,b): N[v].append(w); N[w].append(v)
    return N

def count(p,q,k):
    N=graph(p,q); count=0; mono=0
    for orig in product(range(k),repeat=p+q):
        choices=[]
        for i in range(p):
            for j in range(q):
                if orig[i]==orig[p+j]:break
                choices.append([c for c in range(k) if c!=orig[i] and c!=orig[p+j]])
            else:continue
            break
        else:
            for subdiv in product(*choices):
                cs=orig+subdiv
                if strong_odd(cs,N):
                    count+=1
                    if len(set(orig[:p]))==len(set(orig[p:]))==1:mono+=1
    return count,mono

def predicted_three(p,q):
    if p%2 and q%2:return 6
    if p%2==0 and q%2==1:return 3*(1<<(p-1))
    if p%2==1 and q%2==0:return 3*(1<<(q-1))
    return 0

def witness(p,q):
    # Three-color constructions if at least one side is odd.
    K=[None]*(p+q+p*q)
    if p%2 and q%2:
        K[:p]=[0]*p;K[p:p+q]=[1]*q
    elif p%2==0 and q%2:
        K[:p]=[0]+[1]*(p-1);K[p:p+q]=[2]*q
    elif p%2 and q%2==0:
        K[:p]=[2]*p;K[p:p+q]=[0]+[1]*(q-1)
    else:
        # Two original colors and a parity-odd edge checkerboard.
        K[:p]=[0]*p;K[p:p+q]=[1]*q
        for i in range(p):
            for j in range(q):
                K[p+q+i*q+j]=2 if ((i==0)!=(j==0)) else 3
        assert strong_odd(K,graph(p,q))
        return K
    for i in range(p):
        for j in range(q):
            K[p+q+i*q+j]=({0,1,2}-{K[i],K[p+j]}).pop()
    assert strong_odd(K,graph(p,q))
    return K

def main():
    for p,q in [(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4),(4,3)]:
        s3,_=count(p,q,3)
        assert s3==predicted_three(p,q),(p,q,s3,predicted_three(p,q))
        c=witness(p,q)
        assert len(set(c))==(4 if p%2==q%2==0 else 3)
        print('CHECK',p,q,'three_colourings',s3,'minimum',len(set(c)))
    for p,q in [(1,1),(2,2),(2,4)]:
        n,mono=count(p,q,4)
        if p%2==q%2==0: assert mono==12*2**((p-1)*(q-1))
        print('FOUR_COLOURS',p,q,'total',n,'monochromatic_original',mono)
    print('VERIFICATION_OK')
if __name__=='__main__':main()
