# Weighted chordless cycles detect the first even homology of type-A parabolic homotopy colimits

## Finding
For an arbitrary labeled graph \(H\) on \(S=\{1,\ldots,r\}\), \(r\geq1\), write \(K=\mathrm{Cl}(H)\) for its clique complex and
\[
X_H=\operatorname{hocolim}_{I\in K}SU(r+1)/G_I,
\]
where \(G_I\) is the standard compact parabolic subgroup indexed by \(I\).
For \(D\subseteq S\), split \(D\) into maximal consecutive runs of lengths \(a_1,\ldots,a_s\), and define
\[
\lambda(D)=\sum_{i=1}^{s}\binom{a_i+1}{2},\qquad \lambda(\varnothing)=0.
\]
Let \(\mathcal C(H)\) be the collection of vertex sets of induced cycles of length at least four. Then the following are equivalent:

1. \(H\) is chordal, meaning \(\mathcal C(H)=\varnothing\).
2. \(H_{2k}(X_H;\mathbb Z)=0\) for every integer \(k\geq1\).

In the chordal case, all integral homology of \(X_H\) is free, and all its positive-degree homology occurs in odd degrees. More explicitly, for the permutation group \(S_{r+1}\), the odd-degree Poincaré polynomial is
\[
P_{X_H}(t)=1+\sum_{w\in S_{r+1},\ D=\mathrm{Des}(w)\ne\varnothing}(c(H[D])-1)t^{2\operatorname{inv}(w)+1},
\]
where \(c(H[D])\) is the number of connected components of the induced graph. Each summand has a nonnegative coefficient; terms with connected \(H[D]\) vanish.

If \(H\) is not chordal, put
\[
m(H)=\min_{C\in\mathcal C(H)}\lambda(C),\qquad
b(H)=|\{C\in\mathcal C(H):\lambda(C)=m(H)\}|.
\]
Then the first nonzero **positive even** integral homology is exactly
\[
\boxed{H_{2m(H)+2}(X_H;\mathbb Z)\cong\mathbb Z^{b(H)}}.
\]
All lower positive even homology groups vanish; \(b(H)\) is an integer at least one. In particular, the onset degree and its exact rank can be read from a weighted optimization over **induced chordless cycles**, without evaluating the full homology of any clique complex or enumerating all permutations.

## Assumptions and scope
The vertex labeling \(1,\ldots,r\) is part of the datum: unlike unweighted chordality, the statistic \(\lambda\) depends on the Coxeter order of the simple reflections of \(SU(r+1)\). Graphs may be disconnected. The graph is simple; the clique complex contains all singletons. Homology uses integral coefficients, and the augmented reduced homology convention is \(\widetilde H_{-1}(\{\varnothing\};\mathbb Z)=\mathbb Z\). The Weyl group is \(S_{r+1}\), with the right descent set \(\mathrm{Des}(w)=\{i:w(i)>w(i+1)\}\) and Coxeter length \(\operatorname{inv}(w)\), the inversion number.

## Proof
**1. Established integral decomposition.** Zhang's Theorem 1.1 and Theorem 5.4 [1] identify, for every \(n\geq0\),
\[
H_n(X_H;\mathbb Z)\cong\bigoplus_{w\in S_{r+1}}
\widetilde H_{n-2\operatorname{inv}(w)-1}\!\left(\mathrm{Cl}(H[\mathrm{Des}(w)]);\mathbb Z\right).
\]
This decomposition is an input from [1], not reproved here. For \(\mathrm{Des}(w)=\varnothing\), the unique permutation is the identity; its augmented summand contributes only \(H_0=\mathbb Z\). All other possible positive even-degree contributions correspond to **odd** reduced homology degrees \(j=1,3,5,\ldots\) of an induced clique complex, with target degree \(2\operatorname{inv}(w)+j+1\).

**2. Exact cost and uniqueness for any descent set.** Let \(D\subseteq S\) have maximal consecutive runs of lengths \(a_1,\ldots,a_s\). In any permutation having every descent in a run of length \(a_i\), the corresponding consecutive block of \(a_i+1\) entries is strictly decreasing and therefore forces at least \(\binom{a_i+1}{2}\) inversions. These blocks are disjoint. Hence \(\operatorname{inv}(w)\geq\lambda(D)\) whenever \(\mathrm{Des}(w)=D\). To attain equality, partition the positions into those blocks and singleton positions; place the smallest available values consecutively within the first block, the next consecutive values within the second block, etc., and reverse the order *inside* each nonsingleton block. Every descent is in \(D\); there is no inversion between blocks; equality is attained. Any equality permutation can have no between-block inversion. All values in each earlier block must therefore be smaller than all values in later blocks; the within-block decreasing condition then uniquely determines the permutation. Thus **exactly one** permutation has \(\mathrm{Des}(w)=D\) and \(\operatorname{inv}(w)=\lambda(D)\). Moreover, \(\lambda(E)>\lambda(D)\) whenever \(D\subsetneq E\), because adding a descent imposes at least one new inversion.

**3. Chordality.** If \(H\) is chordal, every induced subgraph \(H[D]\) is chordal. The clique complex of each connected chordal graph is acyclic in positive degrees over \(\mathbb Z\), by [2, Theorem 4.4]; the componentwise statement gives only reduced degree-zero homology, isomorphic to \(\mathbb Z^{c(H[D])-1}\) for nonempty \(D\). The decomposition in Step 1 therefore has no positive even-degree summands, and no torsion; summing degree-zero contributions gives the stated odd-degree polynomial.

**4. Detection of nonchordality.** If \(H\) is not chordal, choose any induced chordless cycle \(C\) of length at least four. Its induced clique complex is the circle \(S^1\), so \(\widetilde H_1(\mathrm{Cl}(H[C]);\mathbb Z)=\mathbb Z\). By Step 2 there is a permutation with exact descent set \(C\) and inversion number \(\lambda(C)\). By Step 1 this forces a \(\mathbb Z\) direct summand in degree \(2\lambda(C)+2\). Consequently positive even homology does not vanish.

**5. First degree and multiplicity.** Every nonzero positive even-degree summand in Step 1 comes from odd \(j\geq1\) and some descent set \(D\) with \(\widetilde H_j(\mathrm{Cl}(H[D]);\mathbb Z)\ne0\). Such a graph \(H[D]\) cannot be chordal, by Step 3. It contains a chordless induced cycle \(C\subseteq D\). Hence the homological degree satisfies
\[
n=2\operatorname{inv}(w)+j+1\ \geq\ 2\lambda(D)+2\ \geq\ 2\lambda(C)+2\ \geq\ 2m(H)+2.
\]
If equality holds, then \(j=1\), \(\operatorname{inv}(w)=\lambda(D)\), and \(\lambda(D)=\lambda(C)=m(H)\). Strict monotonicity in Step 2 gives \(D=C\). The induced clique complex is then one circle, and Step 2 gives exactly one minimizing permutation for each distinct minimizing cycle vertex set. Hence all summands at the first even degree are free of rank one and their number is exactly \(b(H)\). There can be no torsion at that degree.

**6. Label sensitivity.** For \(r=7\), consider two graph labelings, each consisting of one induced four-cycle and three isolated vertices. If the four-cycle is on \(\{1,2,3,4\}\), its weight is \(10\) and the first even homology lies in degree \(22\), with rank \(1\). If it is on \(\{1,3,5,7\}\), its weight is \(4\) and the first even homology lies in degree \(10\), also with rank \(1\). Thus the grading detects the placement of isomorphic indexing graphs within the Coxeter diagram.

## Verification
A standalone exact Python checker in `verify.py` enumerates all permutations on up to eight letters and their inversion numbers and descent masks. It independently enumerates clique faces of induced subgraphs and computes reduced \(\mathbb F_2\)-Betti numbers by exact binary row reduction. For each tested graph, it applies the degree shifts in the established descent–Hochster formula, independently enumerates all induced chordless cycle vertex sets, and compares the first even-degree rank with the minimum-cost prediction. It verifies minimum inversion costs for every descent set on \(2\leq r\leq7\), four labeled four-cycle examples, and 15 graphs on four to six vertices (including chordal and nonchordal cases). The output ends in `VERIFY_OK` and `INDEPENDENT_CYCLE_MINIMUM_AND_RANK_VERIFIED`. These checks are finite and are not the proof for unbounded \(r\); Steps 1–5 supply that proof.

## Relationship to prior work
Zhang [1] proves the integral descent–Hochster decomposition for **arbitrary** indexing complexes, a result strictly more general as a homology formula than the present flag-indexing setting. This is an essential input. The new contribution is the sharp combinatorial characterization of the first positive even degree **and its rank** via a constrained inversion minimization over induced cycles, and the resulting chordality criterion, neither explicitly stated in the inspected full text of [1]. Parks [2] establishes vanishing of positive clique-complex homology for connected chordal graphs, but does not address parabolic homotopy colimits, Coxeter descent costs, earliest degrees, or the label-sensitive onset rank. The proof openly uses both inputs. Equivalent previously unindexed formulations cannot be excluded by literature searching alone.

## Limitations
The result applies to \(SU(r+1)\) with its specified simple-reflection ordering and flag complexes obtained as clique complexes of simple graphs. It does not classify the *higher* even-dimensional homology groups, nor exclude torsion there for nonchordal graphs. It does not classify the homotopy type, ring structure, or equivariant representations of \(X_H\). The verification covers finite examples only. Originality is assessed relative to inspected available literature; independent scientific review has not been performed.

## References
[1] Yifan Zhang, *Parabolic Homotopy Colimits and Coxeter Descents*, arXiv:2609.01882v1 (first posted 2026-09-01), revised v2 2026-09-24, Theorems 1.1 and 5.4; https://arxiv.org/pdf/2609.01882.

[2] Allen D. Parks, *Clique Complex Homology: A Combinatorial Invariant for Chordal Graphs*, International Journal of Sciences 2 (July 2013), Theorem 4.4; https://www.ijsciences.com/pub/pdf/V2-201307-04.pdf.
