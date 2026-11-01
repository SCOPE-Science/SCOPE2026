# Two-tier sphere wedges and integral symmetry of clique-free windmills

## Finding

Fix integers \(t\ge3\) and \(r\ge2\), and positive integers \(a_1,\ldots,a_r\). Form the *clique windmill* \(W(a_1,\ldots,a_r)\) with one common apex \(v\), disjoint private sets \(B_i\) of cardinality \(a_i\), all edges within \(\{v\}\cup B_i\), and no edges between distinct private sets. Let \(X=\mathsf{CF}_t(W)\) be the simplicial complex of vertex subsets containing no complete graph on \(t\) vertices.

If some \(a_i\le t-2\), then \(X\) is a cone. Otherwise set
\[
P=\prod_{i=1}^r\binom{a_i-1}{t-2},\qquad
Q=\prod_{i=1}^r\binom{a_i-1}{t-1},
\]
with the usual zero convention for binomial coefficients. Then the complete ordinary homotopy type is
\[
\boxed{X\simeq\bigvee^{P}S^{r(t-2)}\ \vee\ \bigvee^{Q}S^{r(t-1)-1}.}
\]
The two indicated dimensions are distinct because \(r\ge2\); an empty wedge contributes a point.

There is also a complete, natural **integral automorphism-module classification**. Let
\[
A_i=\ker\!\left(\varepsilon_i:\mathbb Z[B_i]\longrightarrow\mathbb Z\right),\quad
\varepsilon_i\!\left(\sum_{b\in B_i}n_b b\right)=\sum_{b\in B_i}n_b.
\]
Then the only possibly nonzero reduced integral homology groups are
\[
\boxed{\begin{aligned}
\widetilde H_{r(t-2)}(X;\mathbb Z)&\cong\bigotimes_{i=1}^r\bigwedge^{t-2}A_i,\\
\widetilde H_{r(t-1)-1}(X;\mathbb Z)&\cong\bigotimes_{i=1}^r\bigwedge^{t-1}A_i.
\end{aligned}}
\]
These identifications are natural after ordering the branches, with the **graded permutation action**: an automorphism transporting branch \(i\) to branch \(\sigma(i)\) transports the corresponding exterior-power factor, and reordering two such factors produces sign \((-1)^k\) in the module with exterior exponent \(k\). Thus the low-degree module uses \(k=t-2\), while the high-degree module uses \(k=t-1\). In particular the two degrees generally have opposite block-swap signs.

For an explicit full character formula, fix any apex-preserving automorphism \(g\), let \(\sigma\) be its branch permutation, and let \(C\) range over cycles of \(\sigma\). Choose any branch \(i_C\) in \(C\). For either \(k=t-2\) or \(k=t-1\), the trace in the corresponding degree equals
\[
\boxed{\operatorname{tr}_k(g)=\prod_C(-1)^{k(|C|-1)}
\operatorname{tr}\!\left(\bigwedge^k(g^{|C|}|_{A_{i_C}})\right).}
\]
If the return permutation on \(B_{i_C}\) has cycle lengths \(\ell_1,\ldots,\ell_s\), its local trace is the coefficient of \(z^k\) in
\[
\frac{\prod_{j=1}^s\bigl(1-(-z)^{\ell_j}\bigr)}{1+z}.
\]
Since the apex has degree \(\sum_i a_i\), strictly exceeding each private vertex degree \(a_i\), every graph automorphism fixes \(v\). Thus these descriptions cover the full automorphism group, including permutations of equally sized blocks.

For illustration, \(W(3,3)\) at \(t=3\) gives \(X\simeq\bigvee^4S^2\vee S^3\). Exchanging the two private triples has trace \(-2\) on the integral degree-two lattice and trace \(+1\) on degree three.

## Assumptions and scope

The graph is finite, simple, and specified completely by the common-apex clique-block construction above. The parameter \(t\) is the size of a forbidden clique, not the number of vertices allowed in a connected induced component. All homology is reduced singular or simplicial homology with integral coefficients. The homotopy splitting need not be equivariant; the separate homology-module isomorphisms and character formula are equivariant. No claim about orbit-space integral homology follows automatically.

## Proof

**Step 1: exact deletion and link.** Write \(K(a,k)=\{F\subseteq[a]:|F|\le k\}\). Because distinct private blocks have no interblock edges, the simplicial deletion of the apex and its link in \(X\) are exactly
\[
D=X\setminus\{v\}=*_{i=1}^r K(a_i,t-1),\qquad
L=\operatorname{lk}_X(v)=*_{i=1}^r K(a_i,t-2).
\]
The entire complex is the pushout \(X=D\cup_L (v*L)\), with \(v*L\) a cone. If some \(a_i\le t-2\), any vertex of \(B_i\) belongs to no forbidden \(t\)-clique, and so is a cone vertex of \(X\). We henceforth assume \(a_i\ge t-1\) for all \(i\).

**Step 2: simplex-skeleton homology and connectivity.** For \(1\le k\le a\), the complex \(K(a,k)\) is the \((k-1)\)-skeleton of an \((a-1)\)-simplex. It is \((k-2)\)-connected, and is homotopy equivalent to \(\bigvee^{\binom{a-1}{k}} S^{k-1}\), with zero summands when \(a=k\). For completeness: it contains the whole \((k-1)\)-skeleton, hence is \((k-2)\)-connected, and its reduced Euler characteristic and lack of cells above dimension \(k-1\) yield the indicated top Betti number; a \((k-2)\)-connected \((k-1)\)-dimensional CW complex is a wedge of \((k-1)\)-spheres (for \(k=1\), a finite discrete space gives the corresponding wedge of zero-spheres). This also follows by the standard matching on faces using a distinguished simplex vertex.

At the integral chain level, the reduced chain group in degree \(k-1\) is \(\bigwedge^k\mathbb Z^{[a]}\); its boundary is contraction against the augmentation covector. Splitting off one basis vector of augmentation one proves
\[
\widetilde H_{k-1}(K(a,k);\mathbb Z)
\cong\ker\!\left(\iota_\varepsilon:\bigwedge^k\mathbb Z^{[a]}\to\bigwedge^{k-1}\mathbb Z^{[a]}\right)
\cong\bigwedge^k\ker\varepsilon.
\]
This isomorphism is canonical under all permutations of the \(a\) vertices.

**Step 3: the attaching map is null.** Standard join connectivity and homology imply that \(L\) is homotopy equivalent to a wedge of \(P\) spheres in dimension \(r(t-2)-1\). Likewise \(D\) is homotopy equivalent to a wedge of \(Q\) spheres in dimension \(r(t-1)-1\), or is contractible when \(Q=0\). In the noncontractible case \(D\) is \((r(t-1)-2)\)-connected, while \(\dim L=r(t-2)-1\). Since \(r\ge2\), the domain dimension is strictly below the stated connectivity. Thus every map \(L\to D\), including the simplicial inclusion, is nullhomotopic by cellular obstruction theory. In the contractible case it is likewise nullhomotopic. The homotopy cofiber of a null map splits as \(D\vee\Sigma L\). This proves the two-tier sphere-wedge assertion, without assuming shellability.

**Step 4: natural integral action.** The split homotopy equivalence need not be natural. Instead use the deletion–link long exact sequence and the degree gap. Because the only reduced homology of \(D\) and \(L\) occurs in degrees \(r(t-1)-1\) and \(r(t-2)-1\), respectively, the inclusion \(D\hookrightarrow X\) identifies the high homology integrally and the connecting homomorphism identifies the low homology integrally with the reduced homology of \(L\). Both maps commute with any automorphism fixing \(v\). Integral join Künneth has no Tor terms here, because all relevant groups are free.

A transposition of two simplicial join factors with reduced homology in degree \(k-1\) switches chains of lengths \(k\) and \(k\), producing the Koszul sign \((-1)^{k^2}=(-1)^k\). Combined with the canonical simplex-skeleton exterior-power identification in Step 2, this proves the stated action on both integral lattices. Every block permutation is a product of transpositions. The trace formula follows by contracting the cyclic tensor permutation around each block orbit: an orbit of length \(\ell\) contributes \((-1)^{k(\ell-1)}\) times the trace of the return map. Lastly, the permutation-module identity \(\mathbb Z[B_i]\cong A_i\oplus\mathbb Z\) over \(\mathbb Q\) yields the generating function for exterior characters, proving the displayed local coefficient formula.

## Verification

The included standalone Python 3 checker `check_windmill.py` enumerates the actual simplices using the definition above, computes complete reduced homology over \(\mathbb F_2\) by sparse binary boundary reduction, independently evaluates signed simplicial Lefschetz numbers, and compares these with the two lattice-character formulas. Running `python3 check_windmill.py` produced twelve complete finite chain calculations, 92 selected signed character checks, and an additional 1,416 exhaustive small-group character checks, all passing. These finite checks are corroboration; the proof establishes the unbounded integral statements.

## Relationship to prior work

Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1 (publicly submitted 2026-02-10), prove in Corollary 3.4 that clique-free complexes of all block graphs are shellable and in Section 4 develop clique attachment results. This covers the shellability of windmills but does not state the exact two-tier homotopy type or the integral action of block and within-block automorphisms. General shellability alone does not specify the full integral symmetry lattice. Earlier work of Khosh-Ahang and Moradi and of Moradi concerns algebraic properties of clique ideals; their inspected abstracts and introductory portions do not imply these specific topological and equivariant statements. The decomposition here is derived directly from the explicit deletion and link; it is not a restatement of the published shellability theorem.

## Limitations

This result applies to graphs whose clique blocks meet at exactly one common apex, not to arbitrary block graphs or arbitrary clique hypergraphs. The ordinary wedge decomposition is not asserted to be equivariant. The complete integral automorphism action is established on homology only, not on a chosen wedge decomposition; no classification of geometric fixed-point spaces or quotient torsion is asserted. The computational checks are finite and mod-two for homology; the integral theorem depends on the explicit chain and cofibration proof. Equivalent unpublished, unindexed, or differently formulated prior work remains possible. No independent mathematical validation has been performed.

## References

1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, 2026-02-10. https://arxiv.org/html/2602.09623v1 ; https://arxiv.org/abs/2602.09623.
2. F. Khosh-Ahang and S. Moradi, *Some algebraic properties of t-clique ideals*, Communications in Algebra 47 (2019), 2870–2882, DOI:10.1080/00927872.2018.1541462.
3. S. Moradi, *t-clique ideal and t-independence ideal of a graph*, Communications in Algebra 46 (2018), 3377–3387, DOI:10.1080/00927872.2017.1412445.
