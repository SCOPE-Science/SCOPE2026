"""Exact verification: {2,3,5} cap H_D = < -1,4,a1,a2,a3 > in Q*/Q*4, for
Z_694 normalized as x0^4 + a1 x1^4 + a2 x2^4 + a3 x3^4 = 0 with
a1=7/2, a2=4, a3=-17/2. Only primes {2,7,17}, sign, and targets {3,5} tracked;
all generators supported there, so the check is exact. Result: 2,3,5 not in H_D."""
from itertools import product
# vector coords: (sign, e2, e7, e17, e3, e5) mod 4 (e3,e5 always 0 on generators)
gens = {
 '-1': (1,0,0,0,0,0),
 '4':  (0,2,0,0,0,0),
 'a1=7/2':  (0,3,1,0,0,0),
 'a2=4':    (0,2,0,0,0,0),
 'a3=-17/2':(1,3,0,1,0,0),
}
G = list(gens.values())
H = set()
for c in product(range(4), repeat=len(G)):
    H.add(tuple(sum(c[i]*G[i][j] for i in range(len(G))) % 4 for j in range(6)))
print("|H_D projected| =", len(H))
for name, v in [('2',(0,1,0,0,0,0)), ('3',(0,0,0,0,1,0)), ('5',(0,0,0,0,0,1))]:
    assert v not in H, name
    print(f"{name} not in H_D: OK")
print("HD_CHECK_OK  =>  ISZ Cor 3.3 applies: Br(Z_694) = Br1(Z_694)")
