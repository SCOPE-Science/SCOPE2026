# Sixteen four-round theories of Hamming graphs

## Finding

Let \(H(d,a)\), for integers \(d\ge1\) and \(a\ge2\), be the simple graph with vertex set \(\{0,\ldots,a-1\}^d\); distinct words are adjacent exactly when they differ in one coordinate. All first-order statements below use only equality and graph adjacency, without a distance predicate, named coordinates, or counting quantifiers. Write \(G\equiv_4 G'\) for agreement on every sentence of quantifier rank at most four. Define \(\alpha(a)=\min\{a,4\}\), and let \(\tau(a)=6\) when \(a=2\), and \(\tau(a)=5\) when \(a\ge3\). Then

\[
H(d,a)\equiv_4 H(e,b)\quad\Longleftrightarrow\quad
\alpha(a)=\alpha(b)\ \text{ and }\quad
\min\{d,\tau(a)\}=\min\{e,\tau(b)\}.
\]

There are exactly sixteen theories: six in the binary-alphabet regime, five in the ternary regime, and five with alphabet size at least four. Their least-parameter representatives are \(H(1,2),\ldots,H(6,2)\), \(H(1,3),\ldots,H(5,3)\), and \(H(1,4),\ldots,H(5,4)\). Thus every graph in the family has a rank-four-equivalent representative with at most \(4^5=1024\) vertices, and this is sharp among representatives in the family. The binary restriction was previously classified; the new content is the nonbinary classification and its joint comparison with the binary regime.

## Assumptions and scope

The graph vertices are full words, not only words of a fixed weight or a linear code. Adjacency is *exactly one* differing coordinate. Each quantifier ranges over vertices, including previously selected vertices. Equality is available, but graph distance greater than one is not a primitive relation. The claim is restricted to quantifier rank four and the family of uniform-alphabet Hamming graphs. It does not give a classification of all Cartesian products with unequal coordinate alphabets at this rank, or a formula for arbitrary quantifier ranks.

## Proof

**1. Exact game invariant.** For an ordered \(t\)-tuple of vertices, each coordinate records the partition of \(\{1,\ldots,t\}\) induced by equality of the \(t\) symbols at that coordinate. Independent symbol permutations in each coordinate, together with coordinate permutations, show that the histogram of these partitions completely determines the tuple's automorphism orbit. A new tuple element refines each partition by joining one of its old blocks or forming a fresh singleton, the latter option being available precisely when the alphabet has an unused symbol. The resulting refinements are independent from coordinate to coordinate. Therefore, enumeration of these histograms and refinements is an exhaustive orbit enumeration, not sampling.

**2. Recursive four-round types.** For any ordered triple \((x,y,z)\), its type with one move left is the atomic diagram of that triple together with the *set* of atomic diagrams of quadruples \((x,y,z,w)\) attained by all choices of \(w\). With two moves left, the type of a pair \((x,y)\) is its atomic diagram and the set of one-move-left types attained by \((x,y,z)\). By vertex transitivity, the empty-tuple rank-four theory is determined by the set of pair types attained from one fixed first vertex. Induction on the remaining moves proves these statements directly from the Ehrenfeucht–Fraïssé game; multiplicities of attainable extensions play no role.

For the last move, atomic relations depend only on Hamming distances truncated at two: zero is equality, one is adjacency, and at least two is nonadjacency. The five ordered-triple coordinate patterns are \((0,0,0)\), \((0,0,1)\), \((0,1,0)\), \((0,1,1)\), and \((0,1,2)\). The last is unavailable over a binary alphabet. In each coordinate, each possible new symbol contributes a vector in \(\{0,1\}^3\) to the distances from the three old words. Capped addition on \(\{0,1,2\}^3\) produces an explicit twenty-seven-state transition system. Starting at \((0,0,0)\), applying the transitions for every coordinate, and recording all reachable states gives *exactly* the fourth-word atomic diagrams. The file `artifacts/verify_hamming_symbolic.py` implements this finite algorithm, with no approximate arithmetic.

**3. Infinite-dimension saturation certificate.** Denote by \(T_{a,p}\) the union-preserving transition operator on subsets of the twenty-seven capped-distance states for alphabet regime \(a\in\{2,3,4\}\) and triple-coordinate pattern \(p\). Direct exhaustive checking of every one of the twenty-seven singleton input states establishes

\[
T_{a,p}^{C_{a,p}}=T_{a,p}^{C_{a,p}+1},
\]

with caps, in the pattern order above,

\[
(C_{2,p})=(2,4,4,4,\mathrm{n/a}),\qquad
(C_{3,p})=(C_{4,p})=(2,3,3,3,3).
\]

The dash denotes an unavailable pattern. Union preservation and the identity show that the one-move-left type of a triple depends only on the coordinate-pattern counts truncated at these caps. Pairwise atomic relations are preserved as every relevant cap is at least two. The certificate explicitly tests the identities for *all* starting states, so this saturation step does not extrapolate a sequence of observed finite cases.

Fix a pair of words at Hamming distance \(j\). Among their \(d-j\) equal-symbol coordinates, adjoining a third word divides the coordinates into two bins, with caps \(2,4\) in the binary regime and \(2,3\) otherwise. Among their \(j\) distinct-symbol coordinates, adjoining a third word gives two bins of cap four in the binary regime, or three bins of cap three otherwise. A basic capped-composition lemma says that, for bin caps \(c_1,\ldots,c_r\), the set of all truncated bin-count vectors arising from a total of \(n\) items depends only on \(\min\{n,\sum c_i\}\): below the sum the total is exact; at or above it, excess items may be put in any saturated bin. Hence the full pair type depends only on

\[
(\min\{d-j,A\},\min\{j,B\}),
\]

where \((A,B)=(6,8)\) for binary alphabets and \((A,B)=(5,9)\) otherwise. Both pairs sum to fourteen. For every \(d\ge14\), the *set* of such capped profiles over \(0\le j\le d\) is independent of \(d\): it contains all profiles with the first coordinate below \(A\) and the second saturated, all with the second below \(B\) and first saturated, and the doubly saturated profile. It follows that the rank-four theory has stabilized by dimension fourteen. Finally, at most four vertices are selected, so all alphabet sizes at least four permit exactly the same coordinate refinements; replacing any such alphabet by four symbols preserves the entire game.

**4. Finite exact boundary and distinctness.** The same orbit recursion evaluates every dimension from one through fourteen in each of the three alphabet regimes. It yields the following complete partitions:

\[
\begin{array}{c|l}
\text{Alphabet regime}&\text{Dimension classes}\\\hline
2&\{1\},\{2\},\{3\},\{4\},\{5\},\{6,7,\ldots\}\\
3&\{1\},\{2\},\{3\},\{4\},\{5,6,\ldots\}\\
\ge4&\{1\},\{2\},\{3\},\{4\},\{5,6,\ldots\}
\end{array}
\]

The sixteen resulting recursive types are pairwise distinct, including across alphabet regimes. All extension possibilities are enumerated as finite integer compositions; the code contains assertions for both equalities within each stated class and inequalities between distinct classes. An independent verifier constructs the actual graph vertices and checks all third/fourth selections for the stated smaller boundary cases, agreeing exactly with the symbolic pair types. Coupled with Step 3, the finite boundary establishes the theorem for every dimension. The final class has least representative \(H(5,4)\), with \(1024\) vertices, proving sharpness of the family-restricted bound.

## Verification

From the directory containing `artifacts`, run `python3 artifacts/verify_hamming_symbolic.py` and `python3 artifacts/verify_hamming_direct.py`. The former checks all twenty-seven input states for every saturation identity, exhausts all sixteen rank-four types through dimension fourteen, and proves the threshold-profile simplification. The latter enumerates actual vertices and selections, separately confirming all pair types for binary dimensions one through five, ternary dimensions one through four, and four-symbol dimensions one through three. Recorded standard outputs are `artifacts/symbolic_output.txt` and `artifacts/direct_output.txt`. Both checks finish with `VERIFY_OK` or `DIRECT_VERIFY_OK` respectively. Finite enumeration is used only for the finite boundary; the infinite tail is proved by the symbolic saturation identity and capped-composition lemma.

## Relationship to prior work

Klavžar and Peterin (2005) define Hamming graphs as Cartesian products of complete graphs and characterize graph, induced-subgraph, and isometric-subgraph embeddings using edge labelings. Their theorems concern recognition and embeddings, not quantifier-rank-four equivalence of members of the family. Pikhurko and Verbitsky (2010; revised 2013) develop Ehrenfeucht–Fraïssé games and logical graph complexity in general; their inspected survey does not supply the alphabet/dimension partition above. A previously recorded rank-three result classifies Cartesian complete-graph products, and a previously recorded rank-four result already covers binary hypercubes. Those results are acknowledged as earlier coverage, rather than represented as new components. The present additional statements classify all nonbinary uniform-alphabet Hamming graphs at rank four, establish their dimension-five transition, and compare the three alphabet regimes in a single exact theorem. Dedicated published-literature and research-index searches returned no equivalent or logically stronger covering claim, subject to the limitations below.

## Limitations

This is a self-review, not independent audit or external certification. The novelty assessment has a residual risk of equivalent results in unindexed or inaccessible sources, or an implicit earlier consequence of broader graph-product methods. The proof's executable finite certificate is readable but should be independently checked before any external claim of validation. The conclusion does not concern logics with counting, named coordinates, an explicit distance relation, or arbitrary unequal-alphabet products.

## References

1. S. Klavžar and I. Peterin, “Characterizing subgraphs of Hamming graphs,” *Journal of Graph Theory* **49** (2005), 302–312, DOI: 10.1002/jgt.20084. Authors' lawful copy: https://users.fmf.uni-lj.si/klavzar/preprints/20084-scan.pdf . First online publication: 2005-04-08.
2. O. Pikhurko and O. Verbitsky, “Logical complexity of graphs: a survey,” arXiv:1003.4865, first public 2010-03-25, revised 2013-04-29. https://arxiv.org/pdf/1003.4865 .
