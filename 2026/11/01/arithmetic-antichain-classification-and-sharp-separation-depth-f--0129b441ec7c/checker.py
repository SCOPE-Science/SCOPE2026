from itertools import product

def sig(f,root):
    seen={};seq=[];w=root
    while w not in seen:
        seen[w]=len(seq);seq.append(w);w=f[w]
    return seen[w],len(seq)-seen[w]

def behaviors(f,L,alpha):
    n=len(f);result=set()
    for col in product(range(alpha),repeat=n):
        for root in range(n):
            w=root;word=[]
            for _ in range(L):
                word.append(col[w]);w=f[w]
            result.add(tuple(word))
    return result

N=4;frames=[]
for n in range(1,N+1):
    for f in product(range(n), repeat=n):
        types={sig(f,w) for w in range(n)}
        # maximal under preorder
        maximal=tuple(sorted((t,p) for (t,p) in types if not any((t,p)!=(T,P) and t<=T and P%p==0 for (T,P) in types)))
        frames.append((f,maximal))
print('frames',len(frames),'unique theories',len(set(x[1] for x in frames)))
# exhaustive frame-pair test for same n <=3, using alpha=3 and L=2*N+2
for n in range(1,N+1):
    grp=[(f,ms) for f,ms in frames if len(f)==n]
    reps={f:behaviors(f,2*n+2,n) for f,ms in grp}
    for f,Af in grp:
        for g,Ag in grp:
            predicted=all(any(t<=T and P%p==0 for T,P in Af) for t,p in Ag)
            observed=reps[g]<=reps[f]
            if predicted!=observed:
                raise ValueError(('MISMATCH',n,f,Af,g,Ag,predicted,observed))
    print('checked n',n,'ordered pairs',len(grp)**2)
# independent all elementary signature pair test (alpha=max total node count)
signatures=[(t,p) for t in range(4) for p in range(1,5-t)]
for t,p in signatures:
    seq=list(range(t+p));seq[-1]=seq[-1]
    f=list(range(1,t+p))+[t]
    B=behaviors(f,10,4)
    for T,P in signatures:
        g=list(range(1,T+P))+[T]
        A=behaviors(g,10,4)
        pred=(t<=T and P%p==0)
        if (B<=A)!=pred:raise ValueError(('SIG',t,p,T,P))
print('ALL_CHECKS_OK')
