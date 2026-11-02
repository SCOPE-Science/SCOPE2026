"""Independent exact recursive finite-rank evaluation using immutable nested type sets."""
import sys

def structure(n):
    elems=[None]+[(i,j) for i in range(n) for j in range(i+1,n)]
    ix={v:k for k,v in enumerate(elems)}
    def mul(x,y):
        if x is None or y is None or x[1]!=y[0]: return None
        return (x[0],y[1])
    product=tuple(tuple(ix[mul(x,y)] for y in elems) for x in elems)
    return len(elems),product

def atomic(x,y,z,prod):
    w=(0,x,y,z)
    # Disjoint equality information + complete relational multiplication table of pointed symbols
    equality=tuple(w[i]==w[j] for i in range(4) for j in range(i))
    mult=tuple(prod[w[i]][w[j]]==w[k] for i in range(4) for j in range(4) for k in range(4))
    return equality,mult

def root_type(n):
    N,prod=structure(n)
    # Do not use a global type numbering. Equality of the immutable types is structural.
    by_pair={(x,y):frozenset(atomic(x,y,z,prod) for z in range(N))
             for x in range(N) for y in range(N)}
    by_point={x:frozenset(by_pair[(x,y)] for y in range(N)) for x in range(N)}
    return frozenset(by_point.values())
if __name__=='__main__':
    upto=int(sys.argv[1]) if len(sys.argv)>1 else 12
    reps=[]
    for n in range(1,upto+1):
        t=root_type(n)
        k=next((i+1 for i,u in enumerate(reps) if u==t),None)
        if k is None:reps.append(t);k=len(reps)
        print(f'n={n} class={k} distinct_single_types={len(t)}',flush=True)
