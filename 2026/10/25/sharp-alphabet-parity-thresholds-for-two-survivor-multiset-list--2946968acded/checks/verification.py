"""Direct multiset incidence checks for a two-survivor list code."""
from itertools import combinations,product
from math import comb,ceil
from collections import Counter

def cycles_odd(q):
    assert q%2==1
    m=(q-1)//2
    out=[]
    for s in range(m):
        seq=[q-1,s]
        for i in range(1,m):seq.extend([(s-i)%(q-1),(s+i)%(q-1)])
        seq.append((s-m)%(q-1))
        out.append([tuple(sorted((a,b))) for a,b in zip(seq,seq[1:]+seq[:1])])
    all_edges=[e for c in out for e in c]
    assert len(set(all_edges))==comb(q,2) and len(all_edges)==comb(q,2)
    return out

def matchings_even(q):
    assert q%2==0
    out=[]
    for s in range(q-1):
        edges=[tuple(sorted((q-1,s)))]
        for i in range(1,q//2):
            edges.append(tuple(sorted(((s-i)%(q-1),(s+i)%(q-1)))))
        out.append(edges)
    all_edges=[e for c in out for e in c]
    assert len(set(all_edges))==comb(q,2) and len(all_edges)==comb(q,2)
    return out

def regular_multiplicities(q,r):
    out=Counter()
    if q%2==0:
        factors=matchings_even(q)
        for i in range(r):out.update(factors[i%len(factors)])
    else:
        cycles=cycles_odd(q)
        for i in range(r//2):out.update(cycles[i%len(cycles)])
        if r%2:
            unused=cycles[(r//2)%len(cycles)]
            # Select a matching in unused cycle after removing vertex q-1.
            # Walecki cycles order [q-1, ...]; read its remaining consecutive edges.
            seq=[q-1];adj={a:[] for a in range(q)}
            for a,b in unused:adj[a].append(b);adj[b].append(a)
            current=q-1;prev=None
            for j in range(q-1):
                nxt=next(v for v in adj[current] if v!=prev)
                seq.append(nxt);prev,current=current,nxt
            out.update(tuple(sorted((seq[j],seq[j+1]))) for j in range(1,q-1,2))
    deg=[0]*q
    for (a,b),m in out.items():deg[a]+=m;deg[b]+=m
    assert sum(out.values())==q*r//2
    assert sorted(deg)==([r]*q if q*r%2==0 else [r-1]+[r]*(q-1))
    return out

def build(q,n,L):
    k=2**(q-3);K=4*k;E=(q+2)*k;L0=(q+3)*k
    assert n>=max(q+1,3+k)
    assert (L>=L0 and n>=3+ceil((L-K)/(q-1))) or (q%2 and L==L0-1)
    words=[]
    # one-heavy words, coordinates outside i are 0 or 1
    for i in range(q):
        others=[j for j in range(q) if j!=i]
        for bits in product([0,1],repeat=q-1):
            v=[0]*q
            for j,b in zip(others,bits):v[j]=b
            v[i]=n-sum(bits)
            assert v[i]>=2
            if q%2 and L==L0-1 and all(bits) and i==0:continue
            words.append(tuple(v))
    if q%2 and L==L0-1:
        mult=Counter({edge:k for edge in combinations(range(q),2)})
        for a,b in zip(range(1,q,2),range(2,q,2)):
            mult[a,b]-=1
    else:
        mult=regular_multiplicities(q,L-K)
    for (a,b),count in sorted(mult.items()):
        assert count<=n-3
        for h in range(2,2+count):
            v=[0]*q;v[a]=h;v[b]=n-h
            assert v[a]>=2 and v[b]>=2
            words.append(tuple(v))
    assert len(words)==len(set(words))
    cap=Counter()
    for word in words:
        for i in range(q):
            if word[i]>=2:cap[(i,i)]+=1
            for j in range(i+1,q):
                if word[i]>=1 and word[j]>=1:cap[(i,j)]+=1
    assert cap and max(cap.values())<=L
    upper=(q*L)//2+q*2**(q-2)
    assert len(words)==upper,(q,n,L,len(words),upper)
    return {'q':q,'n':n,'L':L,'size':len(words),'cap_min':min(cap.values()),'cap_max':max(cap.values()),'edge_max':max(cap[e] for e in cap if e[0]!=e[1]),'loop_min':min(cap[(i,i)] for i in range(q))}

if __name__=='__main__':
    for q in range(4,9):
        k=2**(q-3);L0=(q+3)*k
        n=max(q+1,3+k)
        print(build(q,n,L0-(q%2)))
        print(build(q,n,L0))
        extra=3
        r=L0+extra-4*k
        n2=max(n,3+ceil(r/(q-1)))
        print(build(q,n2,L0+extra))
