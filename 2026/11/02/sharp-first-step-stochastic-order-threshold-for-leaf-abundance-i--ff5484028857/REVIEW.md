# Independent mathematical audit

## correctness

PASS

For fixed k>=2 roots and m>=2 nonroots (n=k+m), Pitman forest-volume polynomial equals occupancy from m-1 uniform [n] labels plus one extra uniform root label. Conditioning B=r root edges gives independent root singleton occupancy U_{k,r} and nonroot empty-box occupancy V_{m,m-r}; undirected leaves include root singleton children but not isolated roots. Derive E(L|B=r)=m(1-1/m)^(m-r)+r(1-1/k)^(r-1), strictly increases by a quantified bound. For B=1 vs B=2, couple nonroot Z=V_{m,m-2}, extra nonroot throw J with P(J=1|Z=z)=z/m, root contribution W=0 with probability 1/k else 2. L1=Z+1-J <= Z+W=L2 when m<=2k (z>=2). When m>2k, exact P(L1=2)=m!/m^(m-1) < P(L2=2)=m!/(2k m^(m-2)), while mean increases, forcing incomparability. Also for 2<=k<=m-2, B=k permits L=n-1 with positive mass, whereas B=k+1 forbids it. Independent rational occupancy computations checked all first-step cutoffs, mean monotonicity, and stated saturation for k<=8,m<=12; actual original source verify.py performs independent parent-function enumerations n<=8. These finite checks do not replace Pitman polynomial identity.

## originality

PASS

Best-of-knowledge PASS: conditional occupancy representation is prior (Pitman), but sharp comparison in first-order stochastic order across r=1/2 with explicit m=2k boundary and a second high-leaf obstruction are not in inspected original forest identities.

## value

PASS

Natural probabilistic comparison of leaf abundance conditional on root adjacency in a fixed-root Cayley forest. The surprising incomparability despite strict increase in expected leaves has a sharp first failure boundary and exposes distributional order beyond means.

The dated certificate retains the supplied scientific assessment, sources and limitations.
