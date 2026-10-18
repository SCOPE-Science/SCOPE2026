# Sharp four-round refinement from an affine frame in ternary point–hyperplane incidence graphs

## Finding

For every integer \(d\ge3\), form the bipartite point–hyperplane incidence graph \(G_d\) of \(\operatorname{AG}(d,3)\). Its point vertices are \(\mathbb F_3^d\), and its other vertices are the affine hyperplanes \(H_{a,b}=\{x\in\mathbb F_3^d:a\cdot x=b\}\), where \(a\ne0\) and \((a,b)\) is identified with \((2a,2b)\). Adjacency is incidence. Initially give the point and hyperplane sides different colours and give the \(d+1\) points of an arbitrary affine basis distinct individual colours.

With the synchronous refinement convention that the given colouring is round zero, **the first completely discrete colouring is round four**, for every \(d\ge3\). Moreover, **\(d+1\) is the minimum number of individually coloured point vertices** that can make this graph discrete; an affine basis attains the minimum. The same four-round result also holds for \(d=2\), but the theorem's new higher-dimensional scope is \(d\ge3\).

A structural component is a sparse, explicitly recovered separating family: by round two, the \(1+2d+\binom d2\) points
\[
P=\{0\}\cup\{e_i,2e_i:1\le i\le d\}\cup\{2e_i+2e_j:1\le i<j\le d\}
\]
all have singleton colours, and their incidence signatures separate all \(3(3^d-1)/2\) hyperplanes. Every affine basis works, by affine coordinate change.

## Assumptions and scope

A hyperplane is a codimension-one affine subspace of \(\mathbb F_3^d\); the graph is simple, undirected, and bipartite. An affine basis is a set of \(d+1\) affinely independent points. All unmarked points share one initial colour, all hyperplanes share a different initial colour, and each marked point has its own initial singleton colour. Refinement is ordinary one-dimensional counting colour refinement:
\[
 c_{t+1}(v)=\big(c_t(v),\,\operatorname{multiset}_{w\sim v} c_t(w)\big),
\]
where the displayed multiset notation means the multiset of neighbours' colours; equality of these pairs defines the next colour partition. No assumption is made about any identification problem against arbitrary graphs, nor about higher prime powers.

For proof, carry an arbitrary affine basis to \(\{0,e_1,\ldots,e_d\}\). When \(b\ne0\), write a hyperplane uniquely as \(H_{a,1}\) with \(a\ne0\). When \(b=0\), its normal \(a\ne0\) is defined up to multiplication by \(2=-1\).

## Proof

**1. The first round reveals coordinate-zero hyperplanes.** A hyperplane's round-one colour records exactly which individually marked points it contains. For each \(i\), the hyperplane \(D_i=\{x:x_i=0\}\) contains \(0\) and all \(e_j\) with \(j\ne i\), but not \(e_i\). It is the *unique* hyperplane with this particular marked-point incidence pattern: a hyperplane through \(0\) and all \(e_j\), \(j\ne i\), has normal supported only on coordinate \(i\). Thus every \(D_i\) has a singleton colour at round one.

**2. Round two recovers a small separating family of points.** A point's round-two colour determines the complete set \(\{i:x_i=0\}\), since it records incidence or nonincidence with each singleton \(D_i\). Therefore it distinguishes every support \(\{i:x_i\ne0\}\). For support \(\{i\}\), the two candidates are \(e_i\) (already uniquely marked) and \(2e_i\), so \(2e_i\) becomes singleton at round two.

For distinct indices \(i,j\), consider the round-one hyperplane colour consisting precisely of hyperplanes containing the marks \(e_i,e_j\) but not \(0\) or any other marked \(e_k\). Written with right-hand side \(1\), these are exactly
\[
 H_{a,1}\quad\text{with}\quad a_i=a_j=1,\quad a_k\in\{0,2\}\ (k\notin\{i,j\}).
\]
There are \(2^{d-2}\) of them. Among points of support exactly \(\{i,j\}\), the point \(2e_i+2e_j\) lies on *all* of them because \(2+2=1\) in \(\mathbb F_3\). The other three points \(e_i+e_j\), \(e_i+2e_j\), and \(2e_i+e_j\) lie on *none* because their coordinate sums are \(2\) or \(0\). Thus \(2e_i+2e_j\) is uniquely coloured at round two. Hence all points in \(P\) are singleton by round two.

**3. The incidence pattern on \(P\) identifies every hyperplane.** For \(H_{a,1}\), nonincidence of \(0\) distinguishes it from any homogeneous hyperplane. For each \(i\), its membership pattern on \(e_i,2e_i\) determines \(a_i\): \(e_i\) belongs precisely when \(a_i=1\), \(2e_i\) belongs precisely when \(a_i=2\), and neither belongs when \(a_i=0\). Therefore its entire normal \(a\), and thus the hyperplane, are recovered.

For \(H_{a,0}\), membership of \(e_i\) determines exactly which \(a_i\) are zero. For two nonzero coordinates \(a_i,a_j\), membership of \(2e_i+2e_j\) is equivalent to \(a_i+a_j=0\), thus detecting whether the two nonzero signs are opposite. All pairwise opposite/same information determines the sign vector of the nonzero entries up to simultaneous negation, which is exactly the scalar ambiguity in defining \(H_{a,0}\). The case of only one nonzero coefficient is immediate. Thus every two distinct hyperplanes have different incidence subsets of \(P\), and each hyperplane becomes singleton in round three.

**4. Round four is completely discrete.** Distinct points \(x\ne y\) are separated by some affine hyperplane: choose nonzero \(a\) with \(a\cdot(x-y)\ne0\), then \(H_{a,a\cdot x}\) contains \(x\) but not \(y\). Since all hyperplanes have singleton round-three colours, the round-four point colours are all distinct. Thus the entire graph is discrete by round four.

**5. Four rounds are necessary.** Because the graph is bipartite and all hyperplanes initially have one colour, point colours do not split in round one. Because the point partition does not split in round one, the hyperplane partition does not split further in round two. Consider three unmarked points
\[
 u=e_1+e_2,\qquad v=e_1+2e_2,\qquad w=2e_1+e_2.
\]
They have the same round-two point colour. To see this explicitly, split the round-one hyperplane colours into two types. A homogeneous hyperplane containing \(0\) has a prescribed set of zero coordinates in its normal, and its remaining normal entries vary over \(\{1,2\}\) modulo common negation. Its incidence count with any of \(u,v,w\) depends only on the common support \(\{1,2\}\): if neither coordinate of the normal is nonzero, all choices contribute; if just one is nonzero, none contribute; if both are nonzero, precisely two sign choices before the common-negation quotient contribute. For a hyperplane not containing \(0\), normalize the equation to \(a\cdot x=1\); its round-one colour specifies the set \(T=\{i:a_i=1\}\), with all remaining coefficients in \(\{0,2\}\). For the coordinates \(1,2\), the number of coefficient choices that make \(a\cdot x=1\) is \(1\) if \(|T\cap\{1,2\}|=0\) or \(1\), and \(0\) if that intersection has size \(2\), identically for \(u,v,w\). Coefficients outside the two-coordinate support contribute the same multiplicity. The excluded zero normal never satisfies \(a\cdot x=1\). This proves the claimed round-two collision.

As hyperplane colours have the same partition at rounds one and two, point colours likewise have the same partition at rounds two and three. Thus \(u,v,w\) are still indistinguishable at round three: the graph is not discrete before round four.

**6. The point-marking minimum is \(d+1\).** Any set of at most \(d\) marked point vertices has proper affine span \(W\subsetneq\mathbb F_3^d\). Choosing one point as origin when the set is nonempty, there is a nonidentity invertible linear transformation acting as the identity on the direction space of \(W\) and multiplication by \(2\) on a nonzero complement; conjugating by translation fixes every marked point. For the empty set, any nontrivial translation suffices. Such an affine transformation permutes points and affine hyperplanes while preserving incidence. It moves at least one vertex but fixes all marked points, so colour refinement cannot become discrete. An affine basis has \(d+1\) points and succeeds by the preceding steps; minimality follows.

## Verification

Two self-contained Python programs accompany this result. `check_refinement.py` constructs the exact point–hyperplane graphs from finite-field coordinates, runs full synchronous counting refinement, and verifies the first discrete round is four in dimensions \(2,3,4,5,6\); dimension two is a consistency control outside the claimed higher-dimensional scope. It checks the intermediate point/hyperplane class counts, the round-three collision, and the first-round hyperplane subset count. `check_witnesses.py` independently enumerates the incidence signatures on \(P\) for all hyperplanes in dimensions \(2\) through \(9\), verifying pairwise injectivity, and checks the local second-round collision counting identities without implementing refinement. Their unmodified recorded outputs are included. These finite tests are not used as a substitute for the general proof.

## Relationship to prior work

The general notions of colour refinement, discreteness and individualization are standard; see Arvind–Köbler–Rattan–Verbitsky (2015) and Arvind–Fuhlbrück–Köbler–Kuhnert–Rattan (2016). The latter studies the parameterized computational complexity of minimum individualization, not the sharp value or round complexity of the specific incidence graph here. Prior two-dimensional affine-plane analyses concern point–line incidence and do not imply the higher-dimensional point–hyperplane four-round bound: for \(d\ge3\), lines and hyperplanes are different objects, and this proof uses a new explicitly recovered signed-pair witness family.

The theorem is a proposed specialization with independent priority review still needed. An exact equivalent could conceivably be obtainable from a specialized affine-geometry coherent-configuration calculation not located in the sources examined.

## Limitations

The claim is about \(\mathbb F_3\) and point individualizations of the specified bipartite incidence graph. It does not give the stable partition for arbitrary nonbasis mark sets, prove a bound over all prime fields, or assert graph identification against other structures. The finite verification ranges are stated explicitly. Publication-priority comparisons are not exhaustive.

## References

1. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first public version 2015-02-04), https://arxiv.org/abs/1502.01255 .
2. V. Arvind, F. Fuhlbrück, J. Köbler, S. Kuhnert, and G. Rattan, *The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, arXiv:1606.04383 (first public version 2016-06-14), https://arxiv.org/abs/1606.04383 .
