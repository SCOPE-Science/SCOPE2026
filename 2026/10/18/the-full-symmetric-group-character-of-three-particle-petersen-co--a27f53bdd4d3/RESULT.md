# The full symmetric-group character of three-particle Petersen configuration homology

## Finding
Let \(P=KG(5,2)\) be the Petersen graph, with vertices the ten two-element subsets of \(\{1,2,3,4,5\}\) and edges joining disjoint subsets. Let \(B_3(P)\) be the unordered configuration space of three distinct points in its geometric realization, with the natural action of \(S_5=\operatorname{Aut}(P)\). As rational \(S_5\)-representations,
\[
H_2(B_3(P);\mathbb Q)\cong
S^{(3,2)}\oplus S^{(3,1,1)}\oplus2S^{(2,2,1)}\oplus S^{(2,1,1,1)}.
\]
Here \(S^\lambda\) is the rational Specht representation indexed by the partition \(\lambda\) of five. In particular, this rational homology has dimension \(25\) and its \(S_5\)-fixed subspace is zero. On the conjugacy classes ordered by cycle type \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), its character is
\[
(25,-3,1,-2,0,1,0).
\]

## Assumptions and scope
The graph is the ordinary simple Petersen graph, not its subdivision as a new topological space, and configurations are **unordered** and collision-free in the underlying one-dimensional CW complex, not tuples of distinct graph vertices. Homology is singular homology over \(\mathbb Q\); the coefficient field has characteristic zero. Group elements act by relabeling the five defining symbols. The claim is a finite, exact representation classification for three particles and one graph. No integral splitting is asserted.

## Proof
**1. A functorial finite complex.** Use the reduced Świątkowski complex of the graph [2], which computes graph-configuration homology naturally under graph automorphisms (Comparison Theorem 4.5 and Proposition 4.9). There are ten trivalent graph vertices and fifteen edges. Fix a reference incident edge \(b(v)\) at each vertex. At vertex \(v\) take the empty symbol in homological degree zero and two basis differences \(h_{v,e}-h_{v,b(v)}\) in homological degree one, one for each nonreference incident edge \(e\). Polynomial variables indexed by the fifteen edges carry degree zero and particle weight one; a half-edge difference carries degree one and particle weight one. The differential is
\[
\partial(h_{v,e}-h_{v,b(v)})=e-b(v),
\]
with the standard alternating Koszul signs on products of distinct local degree-one symbols. At total particle weight three, the chain groups in degrees \(0,1,2,3\) have dimensions
\[
(680,2400,2700,960),
\]
as follows by choosing \(k\) of the ten graph vertices, choosing one of two differences at each, then a degree-\(3-k\) multiset of fifteen edges.

**2. Exact rational ranks without modular extrapolation.** Sparse elimination over both \(\mathbb F_3\) and \(\mathbb F_5\) gives ranks \((679,1715,960)\) for the three consecutive boundary maps. These computations, using the explicit integer differential, provide lower bounds on rational ranks; they are not taken alone to prove equality. The first boundary has rank at most \(679\), because its image lies in the augmentation kernel of the \(680\)-dimensional degree-zero group. The third map has rank at most its entire \(960\)-dimensional domain. Therefore both bounds are attained. For the middle map, consider the natural Abel–Jacobi total-motion map from \(B_3(P)\) to the graph Jacobian, inducing \(H_1(B_3(P);\mathbb Q)\to H_1(P;\mathbb Q)\). Every one of the twelve simple five-cycles can be traversed by one moving particle while the other two are parked at distinct graph vertices outside the cycle. Their twelve oriented edge-cycle vectors have exact rank six, and \(\dim H_1(P;\mathbb Q)=15-10+1=6\). Hence the induced map is surjective and \(\dim H_1(B_3(P);\mathbb Q)\ge6\). The rational middle boundary consequently has rank at most \(2400-679-6=1715\), matching its modular lower bound. Thus the exact rational Betti numbers are \((1,6,25,0)\). The dimension-six first homology maps equivariantly isomorphically to graph first homology.

**3. Full equivariant character.** For \(g\in S_5\), let \(g_E\) and \(g_V\) be the induced edge and vertex permutations. Write \(c\) for an orbit of \(g_E\), \(d\) for an orbit of \(g_V\), and put \(\tau_d\) equal to the number of incident edges fixed by \(g_E^{|d|}\) at a representative vertex of \(d\), minus one. The signed Euler supertrace of the weight-three reduced chain complex is the coefficient of \(t^3\) in
\[
\prod_{c\in E/\langle g\rangle}\frac1{1-t^{|c|}}
\prod_{d\in V/\langle g\rangle}(1-\tau_dt^{|d|}).
\]
The first factors come from edge-monomial permutations. The second are the supertrace factors of the two-dimensional local half-edge-difference representations; the sign of permuting odd-degree factors is included. Let \(L(g)\) denote this coefficient. The natural equivariant isomorphism in step 2 gives
\[
\operatorname{tr}(g\mid H_1(B_3(P);\mathbb Q))
=\operatorname{tr}(g\mid C_1(P;\mathbb Q))
-\operatorname{tr}(g\mid C_0(P;\mathbb Q))+1.
\]
Only degrees zero, one, and two contribute to homology, so \(\chi_2(g)=L(g)-1+\chi_1(g)\). For the seven cycle types in the order stated above, the triples \((L(g),\chi_1(g),\chi_2(g))\) are
\[
(20,6,25),\ (-2,0,-3),\ (4,-2,1),\ (-1,0,-2),\ (1,0,0),\ (2,0,1),\ (0,1,0).
\]
A separate direct signed action on **every basis chain** confirms the coefficient formula for all \(120\) automorphisms. Murnaghan–Nakayama character calculations and the exact inner products \(\langle\chi_2,\chi^\lambda\rangle=(1/120)\sum_g\chi_2(g)\chi^\lambda(g)\) give the four multiplicities \(1,1,2,1\) as claimed, with zero multiplicities for the other three irreducibles. In particular the trivial representation does not occur.

## Verification
The accompanying `verify_petersen3.py` and `petersen3.py` use only Python's standard library. Run `python verify_petersen3.py` with both files in the same directory. The verifier reconstructs the ten vertices and fifteen edges, checks the full differential and \(\partial^2=0\), computes exact ranks over the fields with three and five elements, enumerates twelve pentagons and their rank-six rational span, checks the independently expanded signed chain supertrace for all \(120\) permutations, and confirms exact irreducible character inner products. Successful execution prints `VERIFY_OK`. The rational rank argument is the independent theoretical upper-bound step in the preceding proof, not a consequence of merely passing modular tests.

## Relationship to prior work
Ko and Park [1] establish general first-homology methods for graph braid groups, but do not identify the present second-homology representation. An, Drummond-Cole and Knudsen [2] supply the natural Świątkowski comparison and reduced-chain techniques used as premises; the particular \(120\)-element character calculation is additional. Maciążek and Sawicki [3], Section 5, give general product-cycle information and tables for other graph/particle combinations: Table 1 concerns \(K_4\), \(K_{3,3}\), \(K_5\), and Table 2 concerns higher-order Petersen-family examples, not this three-particle Petersen \(S_5\)-module. A separate existing calculation concerns two particles on the Petersen graph, which cannot determine the different three-particle degree-two character. The natural graph first-homology module and ordinary rational Betti numbers do not alone fix a \(25\)-dimensional representation.

## Limitations
This establishes an abstract isomorphism of rational \(S_5\)-modules, not a canonical geometric decomposition or an integral Specht-module decomposition; integral torsion is not determined. The computation is specific to exactly three unordered particles on the Petersen graph. Related specialized representation calculations that are unindexed or inaccessible cannot be excluded solely through literature searching. No claim about higher particle numbers or other graphs is made.

## References
[1] K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648v1 (first posted 13 January 2011), especially first-homology methods.

[2] B. H. An, G. C. Drummond-Cole and B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351 (first posted 8 August 2017), Theorem 4.5 and Proposition 4.9.

[3] T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, arXiv:1806.02846 (first posted 7 June 2018), Section 5 and Tables 1–2; *Communications in Mathematical Physics* 371 (2019), 921–973.
