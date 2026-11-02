# Six optimal one-zero-deletion codes in the weight-four length-nine layer

## Finding

Let \(\mathcal W\) be the \(\binom94=126\) binary words of length \(9\) with exactly four ones. A code \(C\subseteq\mathcal W\) is *one-zero-deletion correcting* when deleting a single zero from a codeword always leaves a result that uniquely determines its source codeword. Deletions of a one are not part of this channel. Then the maximum code size is \(26\), and **there are exactly six labeled optimal codebooks**.

They form one orbit under permutations of the five zero-run lengths. Explicitly, encode each word uniquely as
\[
0^{x_0}1\,0^{x_1}1\,0^{x_2}1\,0^{x_3}1\,0^{x_4},
\qquad x_i\geq0,\quad\sum_{i=0}^{4}x_i=5.
\]
One optimal code is the checksum fiber
\[
C_*=\left\{(x_0,\ldots,x_4):\sum_{i=0}^{4}i x_i\equiv0\pmod5\right\}.
\]
Every optimum is a coordinate-permuted copy of \(C_*\), and precisely six distinct copies occur. The stabilizer has order \(20\), so the six optima are naturally indexed by cyclic subgroups of order five in the permutation group on five zero-run positions.

## Assumptions and scope

The five zero-run positions are labeled, including the prefix and suffix. Words are linear, not circular. The alphabet is binary and codewords have exactly four ones and five zeros. Exactly one zero is deleted. The conclusion concerns distinct codebooks as literal subsets of the \(126\)-word layer; codebooks equivalent under permutation of zero-run coordinates are still counted separately. No result about general single-deletion correction is claimed.

## Proof

**Reduction to a unit-transfer graph.** Let \(V=\{x\in\mathbb Z_{\geq0}^{5}:\sum_i x_i=5\}\). Deleting a zero from a word reduces exactly one positive run coordinate by one. Two distinct source vectors \(x,y\) share an output precisely when \(x-e_i=y-e_j\) for some \(i\ne j\), equivalently when \(x-y=e_i-e_j\). Therefore correcting codebooks are exactly independent sets of the graph \(G\) on \(V\) whose edges connect unit transfers; equivalently, the Manhattan distance on the endpoints is \(2\).

**Six explicit codebooks.** A unit transfer \(x\mapsto x+e_i-e_j\) changes \(\sum_{t=0}^4 t x_t\pmod5\) by \(i-j\not\equiv0\pmod5\). Hence every checksum fiber is independent. Exact enumeration of the \(126\) profiles verifies \(|C_*|=26\); alternatively, the fifth-root-of-unity filter gives the same size. Every coordinate permutation preserves adjacency and sends \(C_*\) to another independent set of size \(26\). Among the \(120\) coordinate permutations, precisely \(20\) fix the fiber: the affine permutations \(i\mapsto ai+b\pmod5\), where \(a\in\{1,2,3,4\}\) and \(b\in\{0,1,2,3,4\}\). They yield six distinct candidate codebooks. Their distinctness and the stabilizer calculation are also checked by exhaustive enumeration of all \(120\) permutations.

**Exhaustive optimality and classification certificate.** The accompanying `cert_six_maxima.json` gives two finite branch certificates, checked in exact rational arithmetic by the standalone `verify.py`. Every graph vertex and every clique is generated directly from the defining coordinate constraints; no opaque precomputed adjacency table is trusted. The cliques are the sets of degree-five profiles obtained by adding one unit to a fixed degree-four profile, or subtracting one positive unit from a fixed degree-six profile. The verifier checks pairwise adjacency within every asserted clique.

At any branch node, a particular still-available vertex \(v\) is excluded or included. Inclusion removes the closed neighborhood of \(v\), so the two branches partition all possible independent sets consistently with the already selected vertices. At a pruned leaf, the certificate supplies nonnegative rational weights \(\lambda_K\) on these cliques satisfying
\[
\sum_{K\ni x}\lambda_K\geq1\quad\text{for every still-available vertex }x.
\]
An independent subset can meet each clique in at most one vertex, hence can have at most \(\sum_K\lambda_K\) vertices. If \(s\) vertices are already selected, the rational bound is \(s+\sum_K\lambda_K\).

The first branch tree has four pruned leaves and verifies \(s+\sum_K\lambda_K<27\) at each, proving \(\alpha(G)\leq26\). The second branch tree has \(379\) pruned leaves, each with \(s+\sum_K\lambda_K<26\), and six terminal independent sets of size \(26\). Its branches are exhaustive, so **every** independent set of cardinality \(26\) is one of these six. The verifier compares the resulting six sets, as literal vertex-index sets, against all coordinate-permuted checksum fibers, completing the classification. All finite inequalities are checked with integer arithmetic and exact fractions; the numerical optimizer used to find the certificate is not relied on as an oracle.

## Verification

Run `python3 verify.py cert_six_maxima.json` with the two supplied files in one directory. This uses only the Python 3 standard library and rebuilds all \(126\) vertices, the unit-transfer neighborhoods, and the available cliques. It checks both exhaustive branch trees, the rational inequalities at every pruned leaf, the six resulting independent sets, and their equality with the checksum-fiber orbit. The observed success line is `VERIFY_OK vertices=126 max_size=26 optimum_sets=6 symmetry_orbits=1 upper_certificate_leaves=4 enumeration_certificate_leaves=379`.

## Relationship to prior work

The unit-transfer graph on degree-\(d\) monomials and its spreading number are classical; Babcock and Van Tuyl (2011) study related bounds. Machacek (2020) explicitly investigates **uniqueness and counts** of maximum independent sets for these graphs, proving uniqueness in certain low-dimensional congruence families and listing initial instances. Zabokritskiy (2026) subsequently establishes the **optimal cardinality** for five-variable unit-transfer graphs in every degree, including the already-known optimum \(26\) here. Thus neither the graph, the optimum size, nor the existence of a checksum construction is claimed new. The result claimed here is the **complete six-codebook classification at degree five**, including its single symmetry orbit and affine stabilizer, supported by an exact stand-alone enumeration certificate. No equivalent classification was identified among the inspected materials; the unavailable complete text of the 2026 paper is a residual overlap risk.

## Limitations

The result is restricted to one zero deletion on length-nine weight-four words. The graph search is finite and is not an infinite-parameter theorem. The rational branch certificates prove exactly this finite instance, and do not establish a generic characterization at other lengths, weights or deletion channels. The earlier exact optimum \(26\) is not independently claimed as a novel numerical invariant. An independent literature review and scientific audit have not been performed.

## References

1. J. Machacek, *Unique maximum independent sets in graphs on monomials of a fixed degree*, arXiv:2010.11112, initially submitted 2020-10-21, https://arxiv.org/abs/2010.11112.
2. B. Babcock and A. Van Tuyl, *Revisiting the spreading and covering numbers*, arXiv:1103.3309, 2011, https://arxiv.org/abs/1103.3309.
3. A. L. Zabokritskiy, *Independent Sets in Multiset Profile Graphs via Weighted Local Covers*, arXiv:2607.13733, initially submitted 2026-07-15, https://arxiv.org/abs/2607.13733.
