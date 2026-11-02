# Exact magnetic-field staircases for clique-fiber hypercube antiferromagnets

## Finding

For each integer \(d\ge3\) let \(L=2^d\) and \(N=dL\). Define a graph \(R_d\) on vertices \((i,s)\) where \(0\le i<d\) and \(s\in\mathbb F_2^d\). There is an edge between each pair of distinct vertices with the same word \(s\), and an edge between \((i,s)\) and \((i,s\oplus e_j)\) for every \(j\ne i\). All edges carry the same positive antiferromagnetic exchange \(J\).

For \(r\) positive spins with \(0\le r\le N/2\), put \(q=\lfloor r/L\rfloor\). The exact largest number of cut edges is

\[ B_d(r)=2(d-1-q)r+Lq(q+1). \]

For arbitrary total magnetization \(M\in\{-N,-N+2,\ldots,N\}\), set \(r=(N-|M|)/2\). The exact minimum exchange energy is

\[ E_{\mathrm{ex},\min}(M)=J\bigl[N(d-1)-2B_d(r)\bigr]. \]

Every positive-field transition occurs, and only occurs, at

\[ h_q=2J(d-1-q),\qquad 0\le q\le\lfloor(d-1)/2\rfloor. \]

The strictly stable positive-field sectors are \(r=0,L,\ldots,\lfloor d/2\rfloor L\), together with the zero-magnetization sector \(r=N/2\) for odd \(d\). On \(h=h_q\), all integer \(r\) in \([qL,(q+1)L]\cap[0,N/2]\) coexist. Thus the number of positive-field transitions is \(\lfloor(d+1)/2\rfloor\), and the number of strict plateaux is one greater. These are *sector* claims; general-dimensional ground-state multiplicities are not asserted.

At \(d=3\), \(R_3\) is the 24-site rhombicuboctahedral graph with 48 edges, eight triangular faces and eighteen square faces. The exact sector census gives 18 zero-field ground states, 234 ground states on the strict \(M=8\) plateau, 1392 coexisting states at \(h=2J\), and 13875 at \(h=4J\). The five positive-field regimes are \(0\le h<2J\) with \(M=0\); \(h=2J\) with \(M=0,2,4,6,8\); \(2J<h<4J\) with \(M=8\); \(h=4J\) with \(M=8,10,\ldots,24\); and \(h>4J\) with \(M=24\). At negative fields, globally invert all spins.

## Assumptions and scope

Spins \(\sigma_v\in\{-1,+1\}\) are attached to the labelled vertices of \(R_d\). The classical Hamiltonian is

\[ H(\sigma;h)=J\sum_{\{u,v\}\in E(R_d)}\sigma_u\sigma_v-h\sum_{v\in V(R_d)}\sigma_v,\qquad J>0,\ h\in\mathbb R. \]

There are \(N=d2^d\) sites and \(N(d-1)\) edges. The word-fibres, indexed by \(s\), are disjoint cliques \(K_d\). Each site has \(d-1\) neighbours in its fibre and \(d-1\) within its layer at Hamming distance one along coordinates other than \(i\). The graph is connected and is frustrated because it contains triangles. The statement is for every integer dimension, coupling and admissible magnetization specified above. A positive field favors positive spins.

## Proof

**Cut reduction.** Let \(S\subseteq V(R_d)\) consist of the \(r\) positive-spin sites, \(r\le N/2\). If \(e(S)\) counts edges internal to \(S\), regularity yields the exact cut identity

\[ |\partial S|=2(d-1)r-2e(S). \]

Let \(a_s=|\{i:(i,s)\in S\}|\), so \(0\le a_s\le d\) and \(\sum_s a_s=r\). The clique edges alone give

\[ e(S)\ge\sum_{s\in\mathbb F_2^d}\binom{a_s}{2}. \]

The exchange argument \(\binom{u}{2}+\binom{v}{2}>\binom{u-1}{2}+\binom{v+1}{2}\) whenever \(u\ge v+2\) forces the minimum of this sum, at fixed \(r\), to occur when all occupancy numbers differ by at most one. Writing \(r=qL+t\), \(0\le t<L\), gives the sharp lower bound

\[ e(S)\ge (L-t)\binom q2+t\binom{q+1}{2}=L\binom q2+qt. \]

Substitution gives the claimed upper bound \(2(d-1-q)r+Lq(q+1)\) for the cut.

**Simultaneous equality for every sector.** Denote the binary parity by \(P(s)=\sum_j s_j\pmod 2\). Choose a binary assignment \(c_i\in\{0,1\}\) whose two class sizes differ by at most one. Starting with

\[ S_* =\{(i,s):P(s)=c_i\}, \]

we have \(|S_*|=N/2\), since exactly half the words have each parity. Within any layer \(i\), each allowed non-clique edge flips precisely one bit of \(s\), hence flips parity. Therefore *no* non-clique edge has both endpoints in \(S_*\). Each word fibre contains either \(\lfloor d/2\rfloor\) or \(\lceil d/2\rceil\) selected vertices. Repeatedly delete a selected vertex from a currently most-populated fibre. At every cardinality \(r\), all fibre occupancies still differ by at most one, and no non-clique edges are internal because the selected set remains a subset of \(S_*\). Thus both inequalities above are equalities at every cardinality. Global spin inversion handles \(r>N/2\). This completes the all-sector formula without invoking enumeration.

**Field thresholds.** For \(qL\le r\le(q+1)L\), \(B_d(r)\) has slope \(2(d-1-q)\). For the positive-magnetization branch \(M=N-2r\), the total minimized energy is

\[ F_h(r)=J\{N(d-1)-2B_d(r)\}-h(N-2r). \]

Its slope in that range is \(2h-4J(d-1-q)\). The slopes increase as \(r\) crosses integer multiples of \(L\). Hence the minimizer moves between the interval endpoints only at the stated \(h_q\), and at equality every integer \(r\) in that interval is a minimizer. When \(d\) is odd, the largest segment is truncated by \(r\le N/2\). When \(h\ge0\), the spin-reversed negative-magnetization sector cannot improve on its positive counterpart, and at \(h=0\) the optimum is the zero-magnetization sector. Strict plateaux and their counts follow as stated.

**The three-dimensional polyhedron.** Set \(i\in\{0,1,2\}\) and \(s\in\{0,1\}^3\). Associate to \((i,s)\) the point in \(\mathbb R^3\) with coordinate \(i\) equal to \((-1)^{s_i}(1+\sqrt2)\) and the other two coordinates \((-1)^{s_j}\). Among the 24 distinct points, precisely the defined graph pairs are at Euclidean distance two. They form the standard rhombicuboctahedral vertex set. An exhaustive labelled-state enumeration independently counts the sector maximizers as shown in the verification section; summing the appropriate counts gives the four phase counts above.

## Verification

Run `python3 verify.py` to construct all graphs for \(3\le d\le8\), verify regularity and edge counts, construct matching equality witnesses independently in every sector up to half filling, check the cut directly for \(d=3,4\), and compare the exact three-dimensional geometry. It completes 1794 witness sectors (13+33+81+193+449+1025).

Compile the independent exhaustive verifier as `c++ -O3 -std=c++17 census_independent.cpp -o census` and run `./census`. It traverses all \(2^{24}=16777216\) configurations twice using two distinct recurrences (Gray flips and induced-edge dynamic programming). Both produce the full best-cut and multiplicity vectors for sectors \(0\le k\le24\), and each best cut agrees with the theorem. The half-sector multiplicities, by \(k=0,\ldots,12\), are \(1,24,228,1104,2940,4368,3536,1440,234,552,444,144,18\); remaining sectors reflect global spin inversion. The particular critical-field sums are \(234+552+444+144+18=1392\) and \(1+24+228+1104+2940+4368+3536+1440+234=13875\). No finite check is used as an infinite-dimensional proof.

## Relationship to prior work

Schmidt, Richter and Schnack (2005) investigate quantum and classical Heisenberg antiferromagnets on the cuboctahedron and icosidodecahedron, reporting field-related magnetization effects for these different graphs and spin degrees of freedom. Rousochatzakis, Läuchli and Mila (2007) investigate those same polyhedral kagomé analogues and their Ising limits and local-state manifolds, including a one-third plateau. Their analysis concerns different graphs and does not supply the all-dimensional fibre-clique cut formula, even after passing to an Ising limit.

The max-cut reduction and convex occupancy inequality are standard methods; they are not presented as original. The evaluated contribution is their sharp simultaneous equality on the physically motivated rhombicuboctahedral coordinate-clique family for *all* magnetizations and dimensions, with complete field thresholds and a separate complete finite labelled-state census at the 24-site instance. The broader class of clique-augmented bipartite graphs is not classified. Similar graph names, sector thresholds or magnetization fractions do not by themselves establish mathematical independence, and historical priority remains provisional.

## Limitations

The result applies only to the specified pure, unweighted finite graphs and their uniform-coupling, classical, zero-temperature nearest-neighbour Ising Hamiltonians. It does not determine positive-temperature thermodynamics, Heisenberg quantum spectra, general inhomogeneous couplings, or universal counts of equal-energy configurations for arbitrary \(d\). Ground-state multiplicities outside \(d=3\) are not claimed. The literature comparison cannot exclude an unlocated theorem for a broader graph family that implies this formula. Independent scientific assessment has not been performed.

## References

- R. Schmidt, J. Richter, J. Schnack, *Frustration effects in magnetic molecules*, arXiv:cond-mat/0501376, first made public 2005-01-17. https://arxiv.org/abs/cond-mat/0501376
- I. Rousochatzakis, A. M. Läuchli, F. Mila, *Highly Frustrated Magnetic Clusters: The kagomé on a sphere*, arXiv:0711.3231, first made public 2007-11-20. https://arxiv.org/abs/0711.3231
