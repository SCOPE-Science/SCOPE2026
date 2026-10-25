# A wedge of twenty-six four-spheres from the 27 lines on a cubic surface

## Finding

**Theorem.** Let \(X\) be any nonsingular cubic surface over \(\mathbb C\). Let \(K(X)\) be the finite simplicial complex with one vertex for each of the 27 lines contained in \(X\), and a simplex for every collection of pairwise disjoint lines (including the empty simplex). Then

\[
K(X)\simeq \bigvee^{26}S^4.
\]

In particular, \(\widetilde H_i(K(X);\mathbb Z)\) is \(\mathbb Z^{26}\) for \(i=4\) and zero for all \(i\ne4\), and the complex has no integral homology torsion. This is a homotopy classification, not merely a Betti-number calculation.

## Assumptions and scope

Every smooth complex cubic surface is isomorphic to the blow-up of \(\mathbb P^2\) at six points in general position. With \(H\) denoting the plane pullback and \(E_0,\ldots,E_5\) the six exceptional divisors, its 27 line classes are

\[
E_i,\qquad L_{ij}=H-E_i-E_j\ (0\le i<j\le5),\qquad Q_i=2H-\sum_{k\ne i}E_k.
\]

The intersection form has \(H^2=1\), \(E_i^2=-1\), \(H\cdot E_i=0\) and \(E_i\cdot E_j=0\) for distinct indices. Two distinct lines are disjoint exactly when their intersection number vanishes. Hence this definition of \(K(X)\) depends only on the classical intersection configuration, not on the particular cubic chosen. Its one-skeleton is the Schläfli graph on 27 lines with edges joining disjoint pairs, equivalently the complement of the point-collinearity graph of the generalized quadrangle \(\mathrm{GQ}(2,4)\).

## Proof

**1. Exact finite model.** Index the vertices in the order \(E_0,\ldots,E_5\), followed by \(L_{01},L_{02},\ldots,L_{45}\) in lexicographic pair order, followed by \(Q_0,\ldots,Q_5\). The intersection form above gives these complete meeting rules for distinct line classes: an \(E_i\) meets \(L_{jk}\) precisely when \(i\in\{j,k\}\), and meets \(Q_j\) precisely when \(i\ne j\); two distinct \(L\)-classes meet precisely when their index pairs are disjoint; an \(L_{ij}\) meets \(Q_k\) precisely when \(k\in\{i,j\}\). Distinct \(E\)-classes never meet one another, and distinct \(Q\)-classes never meet one another. Adjacency in the Schläfli graph is the complement of this meeting relation on distinct vertices. The provided exact verifier reconstructs this graph independently from these rules and checks its strongly regular parameters \((27,16,10,8)\).

**2. Enumerate every simplex.** Start with the 27 singleton faces and recursively append a larger vertex adjacent to all vertices of an existing clique. This creates every nonempty clique exactly once, as each clique has a unique increasing listing. The resulting counts in dimensions zero through five are

\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(27,216,720,1080,648,72).
\]

Thus there are exactly 2,763 nonempty simplices and 10,584 codimension-one face incidences. The ordinary Euler characteristic is \(27\), compatible with reduced Euler characteristic \(26\). In addition to the 72 six-line cliques, there are 216 inclusion-maximal five-line cliques, so the complex is not pure.

**3. Construct a complete acyclic matching.** Initially declare every nonempty face unpaired. For each vertex index \(v=0,1,\ldots,26\), visit the remaining faces \(\sigma\) not containing \(v\) in increasing order of \((\lvert\sigma\rvert,\sigma)\). If both \(\sigma\) and \(\sigma\cup\{v\}\) remain unpaired, pair them and remove them from the pool. The second face must be a simplex; otherwise skip the first. The exact verifier performs this rule without heuristic choices or unverified pruning. It produces precisely 1,368 disjoint codimension-one pairs and 27 unpaired critical cells, consisting of one vertex \(E_0\) and 26 four-simplices. The 27 critical cells are explicitly listed in the verifier output as indexed vertex sets.

**4. Certify acyclicity.** Form the entire directed Hasse diagram on the 2,763 nonempty faces, orienting each unmatched face incidence from higher to lower dimension and reversing each matched incidence. The verifier enumerates every one of its 10,584 incidences, constructs their directions, and performs a complete topological sort. It visits all 2,763 vertices of this directed graph; therefore no directed cycle exists. This is the standard finite acyclicity criterion for a discrete-Morse matching. There are no unmatched or unexamined face incidences.

**5. Deduce the homotopy equivalence.** Forman's acyclic matching theorem gives a CW model for \(K(X)\) with exactly one zero-cell and 26 four-cells and no other cells. Because the three-skeleton is a point, each four-cell is attached along the constant map from its boundary three-sphere. The CW model is precisely a wedge of 26 four-spheres. The construction is independent of the chosen cubic once the intersection configuration is fixed. This concludes the proof.

## Verification

The self-contained Python 3 file `verify.py` uses only the standard library and integer/set operations. Run `python3 verify.py` without optimization; the complete asserted finite checks must succeed and print `VERIFY_OK`. Its exact output from this package is saved as `verify_output.txt`. The verifier does not infer an infinite theorem from a sample: the problem has precisely 27 vertices and all possible simplices and Hasse incidences are checked exhaustively. The geometric reduction to this finite graph is separately justified by the classical intersection classes above. The independent mod-two simplicial boundary ranks are \(26,190,530,550,72\), and the reported Euler characteristic supplies another elementary consistency check; neither substitutes for acyclicity.

## Relationship to prior work

Dolgachev and Kapranov (first publicly available April 13, 1993), §0.1, explicitly describe all 27 lines using the six exceptional curves, 15 pair-transforms, and six conic-transforms and discuss the 36 double-sixes. That paper is used for the classical geometry, not as a new result. The public Schläfli graph reference identifies the skew-line graph with the complement of the point graph of \(\mathrm{GQ}(2,4)\) and gives the same strongly regular parameters.

Cioabă and Mim, Proposition 7.7(2b) (2026), study **the same clique complex of the same Schläfli graph** and prove the vanishing of its first homology over every field. This is compatible with, but substantially weaker than, the complete integral homotopy type proved here: vanishing in degree one does not determine degree-four homology, higher attaching maps, or torsion. The 27-line open-neighborhood complex in a separately indexed result is a different simplicial construction on the complementary collinearity graph and therefore does not imply this finding. General clique-complex homotopy papers checked likewise lack the required input graph or a theorem implying this exact homotopy type.

## Limitations

The theorem concerns pairwise disjoint lines on smooth **complex** cubic surfaces and does not assert an analogous result for singular cubics, arithmetic real-line subsets, or different degree del Pezzo surfaces. The result determines the ordinary homotopy type, not the action of the full Weyl symmetry group on homology. Although several source searches and highly relevant full-text sections were inspected, unindexed earlier equivalent calculations cannot be categorically excluded. This mathematical proof has not received independent external validation.

## References

1. I. Dolgachev and M. Kapranov, *Schur quadrics, cubic surfaces and rank 2 vector bundles over the projective plane*, arXiv:alg-geom/9304005v1 (April 13, 1993), §0.1, https://arxiv.org/pdf/alg-geom/9304005.
2. S. M. Cioabă and N. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328 (2026), §7, Proposition 7.7, https://arxiv.org/pdf/2606.27328.
3. A. E. Brouwer et al., *Schläfli graph* (online finite-graph reference), https://jaanos.github.io/tables/graphs/Schlaefli.html.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145; the acyclic matching theorem.
