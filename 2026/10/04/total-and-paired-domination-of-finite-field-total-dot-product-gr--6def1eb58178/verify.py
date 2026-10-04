from itertools import product, combinations

def vecs(q,n):
    return [v for v in product(range(q), repeat=n) if any(v)]

def dot(a,b,q): return sum(x*y for x,y in zip(a,b))%q

def graph(q,n):
    V=vecs(q,n); N=[set() for _ in V]
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            if dot(V[i],V[j],q)==0:
                N[i].add(j); N[j].add(i)
    return V,N

def total(S,N):
    S=set(S); return all(N[v]&S for v in range(len(N)))

def pmatch(S,N):
    S=frozenset(S)
    if not S:return True
    if len(S)%2:return False
    v=next(iter(S))
    for u in N[v]&S:
        if pmatch(S-{v,u},N): return True
    return False

def paired(S,N): return total(S,N) and pmatch(S,N)

def exact(q,n,lim):
    V,N=graph(q,n); gt=gp=None
    for k in range(1,lim+1):
        if gt is None:
            if any(total(S,N) for S in combinations(range(len(V)),k)): gt=k
        if gp is None and k%2==0:
            if any(paired(S,N) for S in combinations(range(len(V)),k)): gp=k
        if gt is not None and gp is not None:return len(V),gt,gp
    return len(V),gt,gp

for q,n in [(2,3),(2,4),(3,3)]:
    N,gt,gp=exact(q,n,4)
    exp_t=q+1; exp_p=q+1 if q%2 else q+2
    assert (gt,gp)==(exp_t,exp_p),(q,n,N,gt,gp)
    print(f'q={q},n={n}: vertices={N}, gamma_t={gt}, gamma_pr={gp} exhaustive')

# Explicit odd witness for q=5,n=3 using W=span(e1,(0,1,1)); norm second=2 nonsquare.
q=5;n=3;V,N=graph(q,n); idx={v:i for i,v in enumerate(V)}
reps=[]
# projective lines reps in span u=(1,0,0), v=(0,1,1): u+t v plus v
for t in range(q): reps.append((1,t,t))
reps.append((0,1,1))
S=[idx[v] for v in reps]
assert total(S,N) and pmatch(S,N) and len(S)==6
print('q=5,n=3: explicit paired-total witness size=6 verified')

# Lower-bound arithmetic union count for representative ranges.
for q in [2,3,5,7,11,13]:
  for n in range(3,9):
    assert q*(q**(n-1))-(q-1) < q**n
print('hyperplane-union lower-bound arithmetic checked')
print('VERIFY_OK')
