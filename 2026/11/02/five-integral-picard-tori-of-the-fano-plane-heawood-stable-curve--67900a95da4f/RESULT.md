# Five integral Picard tori of the Fano-plane Heawood stable curve

## Finding
Let \(k=\mathbb F_q\) be any finite field. Form the split stable graph curve \(C_H\) by attaching a projective line to each of the fourteen point/line vertices of the Fano-plane incidence (Heawood) graph \(H\), and gluing the three distinct markings \(0,1,\infty\) on each component according to the twenty-one incidences. The natural group \(G=\operatorname{GL}_3(\mathbb F_2)\), of order \(168\), acts on this curve. For any \(g\in G\), let \(C_g/k\) be its finite-field twist whose geometric Frobenius acts by \(g\) on the dual graph. Then \(C_g\) is a geometrically connected stable nodal curve of arithmetic genus \(8\), and the identity component \(J_g=\operatorname{Pic}^0_{C_g/k}\) has exactly the five isomorphism types below.

Define \(R_d=\operatorname{Res}_{\mathbb F_{q^d}/\mathbb F_q}\mathbb G_m\) and \(N_3=\ker(R_3\xrightarrow{\operatorname{Norm}}\mathbb G_m)\). Write \(C_m\) for a cyclic group of order \(m\). Each row describes an isomorphism of algebraic groups, not only an isogeny.

| Order of \(g\) | Number of elements | \(J_g\) over \(k\) | Abstract group \(J_g(k)\) | \(\#C_g(k)\) |
| --- | ---: | --- | --- | --- |
| \(1\) | \(1\) | \(\mathbb G_m^8\) | \(C_{q-1}^{8}\) | \(14q-7\) |
| \(2\) | \(21\) | \(R_2^4\) | \(C_{q^2-1}^{4}\) | \(6q+1\) |
| \(3\) | \(56\) | \(R_3^2\times N_3\) | \(C_{q^3-1}^{2}\times C_{q^2+q+1}\) | \(2q+2\) |
| \(4\) | \(42\) | \(R_4^2\) | \(C_{q^4-1}^{2}\) | \(2q+1\) |
| \(7\) | \(48\) | \(\mathbb G_m\times R_7\) | \(C_{q-1}\times C_{q^7-1}\) | \(0\) |

There are six conjugacy classes in \(G\): the order-seven elements form two size-twenty-four classes with the same arithmetic Picard torus. In particular the twist is point-free **if and only if** the Frobenius element has order seven, for every finite field \(k\), including characteristics \(2\), \(3\), and \(7\).

The full rational zeta function is also determined. Let \(v_d(g)\) and \(e_d(g)\) count \(g\)-orbits of length \(d\) on the fourteen vertices and twenty-one edges of \(H\). Then
\[
Z(C_g/k,T)=\prod_{d\ge1}
\frac{(1-T^d)^{e_d(g)-v_d(g)}}{(1-q^dT^d)^{v_d(g)}}.
\]
The complete orbit data, with all unlisted entries zero, are:

| Order | Nonzero \(v_d\) | Nonzero \(e_d\) |
| --- | --- | --- |
| \(1\) | \(v_1=14\) | \(e_1=21\) |
| \(2\) | \(v_1=6,\ v_2=4\) | \(e_1=5,\ e_2=8\) |
| \(3\) | \(v_1=2,\ v_3=4\) | \(e_3=7\) |
| \(4\) | \(v_1=2,\ v_2=2,\ v_4=2\) | \(e_1=1,\ e_2=2,\ e_4=4\) |
| \(7\) | \(v_7=2\) | \(e_7=3\) |

## Assumptions and scope
The Fano plane is the projective plane \(\mathbb P^2(\mathbb F_2)\), described by seven nonzero vectors and seven nonzero covectors in \(\mathbb F_2^3\). A point \(x\) is incident with a covector \(a\) when \(a\cdot x=0\). The Heawood graph is its bipartite incidence graph; it has fourteen vertices, twenty-one edges, and valency three. Components of \(C_H\) meet only in the indicated ordinary nodes, with no triple intersections. The three branch markings on every component are chosen as \(0\), \(1\), and \(\infty\). No projective embedding of this abstract stable curve is required.

Any graph automorphism induces a unique isomorphism among its rational components matching the three marked points. Uniqueness of a projective-line map determined by three ordered distinct points makes these maps an honest group action of \(G\) defined over the prime field. Standard finite Galois descent applied to the cyclic cocycle \(\operatorname{Frob}_q\mapsto g\) gives \(C_g\) over every \(\mathbb F_q\). Neither the characteristic nor a coprimality hypothesis restricts the construction. The graph automorphism group includes additional dualities exchanging the two bipartition classes, but the theorem classifies precisely the twists from its specified subgroup \(G\), not those extra dualities.

## Proof
First, each of fourteen normalized components is geometrically \(\mathbb P^1\), and the twenty-one graph edges are ordinary nodes. Connectedness follows from that of the Fano incidence graph. Thus \(p_a(C_g)=21-14+1=8\); each component meets the rest in three points, making the curve stable.

For any geometrically connected nodal curve \(C\) with normalization \(\widetilde C\), the normalization sequence for units yields the torus exact sequence
\[
1\longrightarrow \mathbb G_m\longrightarrow
\prod_{v\in V}\mathbb G_m\longrightarrow
\prod_{e\in E}\mathbb G_m\longrightarrow
\operatorname{Pic}^0_C\longrightarrow
\prod_v \operatorname{Pic}^0_{\widetilde C_v}\longrightarrow0.
\]
The final term vanishes for this graph curve because every component has genus zero. Hence the Galois character lattice of \(J_g\) is canonically the integral cycle lattice \(H_1(H,\mathbb Z)\), with \(g\) acting on the graph, rather than merely its rationalization.

Enumerate all \(168\) invertible \(3\)-by-\(3\) binary matrices and their induced actions on points and covectors (the latter by inverse transpose). Direct conjugation produces class sizes \(1,21,56,42,24,24\), with orders \(1,2,3,4,7,7\). Fix a lexicographically selected spanning tree \(\mathcal T\) of the Heawood graph. The eight edges outside \(\mathcal T\) give an integral fundamental-cycle basis of \(H_1(H,\mathbb Z)\). Applying representative matrices gives exact integral \(8\)-by-\(8\) Frobenius matrices \(U\).

The companion file `verify_heawood.py` constructs this basis from the graph, checks its boundaries and all \(168\) induced actions, then checks **explicit unimodular** basis changes \(A\) satisfying \(UA=AW\), with \(\det A\in\{1,-1\}\). The normal forms \(W\) are respectively four regular two-cycles, two regular three-cycles plus the cyclotomic two-dimensional block \(\bigl(\begin{smallmatrix}0&-1\\1&-1\end{smallmatrix}\bigr)\), two regular four-cycles, and one fixed rank-one summand plus a regular seven-cycle. In particular, as integral cyclic modules,
\[
H_1(H,\mathbb Z)\cong
\begin{cases}
\mathbb Z^8,&\operatorname{ord}(g)=1,\\
\mathbb Z[C_2]^4,&\operatorname{ord}(g)=2,\\
\mathbb Z[C_3]^2\oplus\mathbb Z[\zeta_3],&\operatorname{ord}(g)=3,\\
\mathbb Z[C_4]^2,&\operatorname{ord}(g)=4,\\
\mathbb Z\oplus\mathbb Z[C_7],&\operatorname{ord}(g)=7.
\end{cases}
\]
The second order-seven conjugacy class is covered because its elements are conjugates of nonidentity powers of a chosen order-seven element; such powers merely permute the regular-orbit basis. The verifier also checks this exhaustion directly. An integral permutation module \(\mathbb Z[C_d]\) is the character lattice of \(R_d\), and \(\mathbb Z[\zeta_3]\) is the character lattice of \(N_3\). This proves the five torus isomorphisms, and taking finite-field points gives the listed cyclic groups.

For the zeta functions, normalize each component and subtract the normalization preimages of each node, then restore the nodes. A vertex orbit of length \(d\) contributes \(1/((1-T^d)(1-q^dT^d))\). An edge orbit of length \(d\) contributes a node factor \((1-T^d)^{-1}\) and two branch factors \((1-T^d)^2\). The graph action preserves the point/line bipartition, so no edge reverses its two branches. Multiplication gives the displayed zeta formula and the orbit table.

In particular, for \(\mathbb F_q\)-points the component-normalization formula simplifies to
\[
\#C_g(\mathbb F_q)=v_1(g)(q+1)-e_1(g).
\]
The displayed orbit table yields the five polynomials, and exactly the order-seven case is zero for every \(q\ge2\). All five regimes are realized as arithmetic twists for every finite field.

## Verification
Run `python3 verify_heawood.py` with Python \(3.8\) or newer; it uses no third-party packages. The program enumerates all \(168\) binary invertible matrices, checks the point/line incidence action, constructs the integer cycle lattice and its eight-dimensional matrices, determines the six conjugacy classes, checks every vertex/edge orbit profile, verifies the four claimed unimodular conjugations via fraction-free integer determinants, and checks that the second order-seven class is covered by powers. Its complete recorded output is `verify_output.txt`, ending in `VERIFY_OK`. The computation is an exhaustive finite-group certificate; the graph-curve descent, normalization, torus identification, and zeta formula are proved algebraically above rather than inferred from sample fields.

## Relationship to prior work
Burnham, Rosen, Sidman, and Vermeire's paper (first posted January 24, 2012) develops graph curves as unions of projective lines corresponding to subtrivalent graphs and studies their projective equations and syzygies. Casalaina-Martin, Kass, and Viviani's paper (first posted July 21, 2011) develops nodal-curve dual-graph techniques in compactified Jacobian geometry. The abstract graph-curve construction and normalization formalism are prior foundations, not asserted new here. The evaluated contribution is the five **integral** arithmetic Picard-torus types for the Fano-plane graph curve, including the cyclotomic norm-one factor, all six group conjugacy types, their complete curve zeta functions, and the exact order-seven point-free criterion. Searches of relevant mathematical records and primary sources did not locate an already evaluated statement with this scope; this is not a proof of historical priority.

## Limitations
The graph curve is a particular stable reducible curve of genus eight, not a smooth genus-eight curve. Its Jacobian is toric, not an abelian variety, and the stated Picard group is its connected identity component. Its underlying abstract curve is constructed by nodal gluing; no embedding in projective space over small characteristics is claimed. The theorem applies to \(\operatorname{GL}_3(\mathbb F_2)\)-twists and not twists by the full order-\(336\) graph automorphism group, which also has point/line dualities. The exhaustive matrix certificate checks finite integral identities; it does not independently audit the general algebraic geometry or establish exclusivity relative to all historical literature.

## References
1. S. Casalaina-Martin, J. L. Kass, F. Viviani, *The Local Structure of Compactified Jacobians*, arXiv:1107.4166v1, first publicly submitted 2011-07-21, https://arxiv.org/abs/1107.4166.
2. G. Burnham, Z. Rosen, J. Sidman, P. Vermeire, *Line arrangements modeling curves of high degree: equations, syzygies and secants*, arXiv:1201.5010v1, first publicly submitted 2012-01-24, https://arxiv.org/abs/1201.5010 (relevant graph-curve definitions in the full-text introduction and Section 3).
