"""Standalone finite verification of explicit involution-avoiding span-two cycles."""
from collections import Counter, defaultdict
from itertools import product


def selected_edges(t: int, f: int):
    if t < 1 or f < 0:
        raise ValueError('t must be positive and f nonnegative')
    a = lambda i: 2*i
    b = lambda i: 2*i+1
    edges = [(a(i),a(i)) for i in range(t)]
    for i in range(t):
        if t % 2 == 0 or i > 0:
            edges.append((a(i),b(i)))
    matched = {(i,i+1) for i in range(t % 2, t-1, 2)}
    for i in range(t):
        for j in range(i+1,t):
            if (i,j) in matched:
                edges.extend([(a(i),a(j)), (b(i),a(j)), (a(j),a(i)), (b(j),a(i))])
            elif t % 2 and (i,j)==(0,1):
                edges.extend([(a(i),a(j)),(b(i),a(j)),(a(j),a(i)),(a(j),b(i))])
            else:
                edges.extend([(a(i),a(j)),(a(i),b(j)),(a(j),a(i)),(b(j),a(i))])
    if f:
        if t % 2:
            edges.append((a(0),b(0)))
        for j in range(f):
            z=2*t+j
            for i in range(t):
                if t % 2 and j==0 and i==0:
                    edges.extend([(z,a(i)),(b(i),z)])
                else:
                    edges.extend([(z,a(i)),(a(i),z)])
    return edges


def permute(x,t):
    return x^1 if x < 2*t else x


def examine(t,f):
    edges=selected_edges(t,f)
    Q=2*t+f
    image=lambda e:(permute(e[0],t),permute(e[1],t))
    assert len(edges)==len(set(edges)),('duplicate',t,f)
    assert set(edges).isdisjoint({image(e) for e in edges}),('negative pair',t,f)
    E=set(edges)
    for x,y in E:
        assert x<Q and y<Q
    target=((Q*Q-f*f)//2)-(t%2 if f==0 else 0)
    assert len(E)==target,(t,f,len(E),target)
    out=Counter(x for x,_ in E)
    inc=Counter(y for _,y in E)
    assert out==inc,(t,f,out,inc)
    active={x for xy in E for x in xy}
    root=min(active)
    discovered={root}
    while True:
        new=discovered|{v for u,v in E if u in discovered}
        if new==discovered:break
        discovered=new
    assert discovered==active,(t,f,'not connected',active-discovered)
    if not(t==1 and f==0):
        assert len(active)==Q,(t,f,active)
    # Reconstruct an Euler circuit and independently compare all cyclic windows.
    adj=defaultdict(list)
    for u,v in sorted(E):
        adj[u].append(v)
    stack=[root]
    walk=[]
    while stack:
        if adj[stack[-1]]:
            stack.append(adj[stack[-1]].pop())
        else:
            walk.append(stack.pop())
    walk.reverse()
    assert len(walk)==len(E)+1 and walk[0]==walk[-1]
    word=walk[:-1]
    assert len({(word[j],word[(j+1)%len(word)]) for j in range(len(word))})==len(word)
    assert {(word[j],word[(j+1)%len(word)]) for j in range(len(word))}==E
    covered={frozenset((e,image(e))) for e in E}
    missed=[(u,v) for u in range(Q) for v in range(Q) if image((u,v))!=(u,v) and frozenset(((u,v),image((u,v)))) not in covered]
    assert len(missed)//2==(t%2 if f==0 else 0)
    return len(E),len(active),len(missed)//2

if __name__ == '__main__':
    for t in range(1,16):
        for f in range(0,9):
            print('t=%02d f=%d length=%d active=%d missing_pairs=%d' % ((t,f)+examine(t,f)))
    print('VERIFIED 135 general parameter pairs')
    # Independent exhaustive search for the two-symbol case: cyclic 2-window words.
    for f,t in [(0,1),(1,1),(0,2),(2,1)]:
        Q=2*t+f
        K=selected_edges(t,f)
        bound=len(K)
        seen=[]
        for length in range(1,bound+1):
            found=False
            for word in product(range(Q),repeat=length):
                edges={(word[i],word[(i+1)%length]) for i in range(length)}
                if len(edges)!=length:continue
                if not edges.isdisjoint({(permute(u,t),permute(v,t)) for u,v in edges}):continue
                found=True;break
            if found:seen.append(length)
        assert seen and max(seen)==bound, (t,f,seen,bound)
        print('EXHAUSTIVE t=%d f=%d attainable=%s optimum=%d'% (t,f,seen,bound))
