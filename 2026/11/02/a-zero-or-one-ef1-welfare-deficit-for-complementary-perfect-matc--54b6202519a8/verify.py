"""Exact finite corroboration for two disjoint perfect-matching complement valuations.
This is a test program, not a substitute for the all-size combinatorial proof.
"""
import itertools

def matchings(t):
    if not t:
        yield ()
        return
    a=t[0]
    for j in range(1,len(t)):
        b=t[j]
        for rest in matchings(t[1:j]+t[j+1:]):
            yield ((a,b),)+rest

def cycle_weights(A,B,n):
    partners=[]
    for M in (A,B):
        p=list(range(n))
        for a,b in M:p[a]=b;p[b]=a
        partners.append(p)
    seen=set();ww=[]
    for i in range(n):
        if i in seen:continue
        stack=[i]; comp=set()
        while stack:
            u=stack.pop()
            if u in comp:continue
            comp.add(u);stack.extend([partners[0][u],partners[1][u]])
        seen|=comp
        assert len(comp)%2==0
        ww.append(len(comp)//2)
    return ww

def check_size(n):
    A=tuple((i,i+1) for i in range(0,n,2))
    N=n//2
    instances=allocations=ef1_winners=0
    for B in matchings(list(range(n))):
        weights=cycle_weights(A,B,n)
        possible={0}
        for w in weights:possible|={s+w for s in possible}
        predicted=N if any(abs(2*s-N)<=1 for s in possible) else N-1
        actual=-1
        for mask in range(1<<n):
            a=sum(((mask>>i)&1)*((mask>>j)&1) for i,j in A)
            wa=sum((1-((mask>>i)&1))*(1-((mask>>j)&1)) for i,j in A)
            b=sum((1-((mask>>i)&1))*(1-((mask>>j)&1)) for i,j in B)
            wb=sum(((mask>>i)&1)*((mask>>j)&1) for i,j in B)
            allocations+=1
            if a>=wa-1 and b>=wb-1:
                actual=max(actual,a+b)
                ef1_winners+=1
        assert actual==predicted, (n,A,B,weights,predicted,actual)
        instances+=1
    print('n_items',n,'instances',instances,'allocations_checked',allocations,'EF1_allocations',ef1_winners)

if __name__=='__main__':
    for n in (2,4,6,8,10):check_size(n)
    print('VERIFY_OK')
