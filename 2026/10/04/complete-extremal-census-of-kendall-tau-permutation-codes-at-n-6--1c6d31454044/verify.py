from itertools import permutations
P=list(permutations(range(6)))
INDEX={p:i for i,p in enumerate(P)}
def kendall(p,q):
    pos=[0]*6
    for i,x in enumerate(p): pos[x]=i
    seq=[pos[x] for x in q]
    return sum(seq[i]>seq[j] for i in range(6) for j in range(i+1,6))
adj=[set() for _ in P]
for i in range(720):
    for j in range(i+1,720):
        if kendall(P[i],P[j])>=10:
            adj[i].add(j); adj[j].add(i)
assert sum(map(len,adj))//2==60840
assert set(map(len,adj))=={169}
cliques4=[]; cliques5=0
for a in range(720):
    n1={x for x in adj[a] if x>a}
    for b in sorted(n1):
        n2={x for x in n1.intersection(adj[b]) if x>b}
        for c in sorted(n2):
            n3={x for x in n2.intersection(adj[c]) if x>c}
            for d in sorted(n3):
                cliques4.append((a,b,c,d))
                cliques5 += sum(1 for e in n3.intersection(adj[d]) if e>d)
assert len(cliques4)==3960 and cliques5==0
for code in cliques4:
    assert sorted(kendall(P[code[i]],P[code[j]]) for i in range(4) for j in range(i+1,4))==[10]*6
def compose(a,b): return tuple(a[b[i]] for i in range(6))
w0=(5,4,3,2,1,0)
def diagram_reverse(p): return compose(w0,compose(p,w0))
def relabel_code(code,g): return frozenset(INDEX[compose(g,P[i])] for i in code)
def reverse_conjugate_code(code): return frozenset(INDEX[diagram_reverse(P[i])] for i in code)
maxima={frozenset(c) for c in cliques4}; unseen=set(maxima); orbits=[]
while unseen:
    code=next(iter(unseen)); orbit=set()
    for g in P:
        image=relabel_code(code,g)
        orbit.add(image); orbit.add(reverse_conjugate_code(image))
    assert orbit<=maxima
    orbits.append(orbit); unseen-=orbit
sizes=sorted(map(len,orbits))
assert sizes==[360,720,1440,1440] and sum(sizes)==3960
expected={
((0,1,2,3,4,5),(0,5,4,3,2,1),(2,5,3,1,4,0),(4,1,3,5,2,0)),
((0,1,2,3,4,5),(0,5,4,3,2,1),(1,5,3,4,2,0),(2,4,3,5,1,0)),
((0,1,2,3,4,5),(0,5,4,3,2,1),(1,4,5,3,2,0),(2,3,5,4,1,0)),
((0,1,2,3,4,5),(0,5,4,3,2,1),(2,4,5,1,3,0),(3,1,5,4,2,0))}
actual=set()
for orbit in orbits:
    actual.add(min(tuple(sorted(P[i] for i in code)) for code in orbit))
assert actual==expected
print('VERIFY_OK maximum=4 labeled_maxima=3960 equidistant=3960 natural_orbits=4 orbit_sizes=360,720,1440,1440 edges=60840 degree=169')
