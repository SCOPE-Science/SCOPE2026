# Separated sphere dimensions and integral petal symmetries of clique-free windmills

## Finding

For integers \(m\ge3\), \(t\ge3\), and \(s_i\ge t\) for \(1\le i\le m\), form a *clique windmill* \(W=W(s_1,\dots,s_m)\) by gluing \(m\) complete graphs \(K_{s_i}\) along one common vertex \(c\), with no further identifications or cross-petal edges. Write \(X=\operatorname{CF}_t(W)\) for the simplicial complex of vertex subsets containing no clique of size \(t\).

Define \(b_i=\binom{s_i-2}{t-2}\) and \(a_i=\binom{s_i-2}{t-1}\), interpreting out-of-range binomial coefficients as zero. Then
\[
|X|\simeq\left(\bigvee^{\prod_{i=1}^{m} b_i} S^{m(t-2)}\right)\vee
\left(\bigvee^{\prod_{i=1}^{m} a_i} S^{m(t-1)-1}\right).
\]
A wedge with zero summands denotes a point. Consequently the only possible nonzero reduced integral homology groups occur in the two displayed degrees, with respective free ranks \(\prod_i b_i\) and \(\prod_i a_i\). All integral homology is torsion-free.

Let \(P_i\) denote the \(s_i-1\) private vertices in petal \(i\), and put \(U_i=\ker(\mathbb Z^{P_i}\xrightarrow{\sum}\mathbb Z)\). The full coordinatewise permutation subgroup \(\prod_i S_{P_i}\) acts on the reduced integral homology by the canonical modules
\[
\widetilde H_{m(t-2)}(X;\mathbb Z)\cong\bigotimes_{i=1}^{m}\bigwedge^{t-2} U_i,
\quad
\widetilde H_{m(t-1)-1}(X;\mathbb Z)\cong\bigotimes_{i=1}^{m}\bigwedge^{t-1} U_i.
\]
For equal petal sizes, \(s_1=\cdots=s_m=s\), this gives the *actual integral* \(S_{s-1}\wr S_m\)-action: internal permutations act on the appropriate exterior powers, and interchanging two petals introduces \((-1)^{t-2}\) in the lower degree and \((-1)^{t-1}\) in the higher degree. The homotopy equivalence above is not asserted equivariant.

For example, three glued four-cliques at threshold three give \(\bigvee^8 S^3\vee S^5\); three glued five-cliques at threshold four give \(\bigvee^{27}S^6\vee S^8\). In the equal-size case, the gap between the two sphere dimensions is \(m-1\), and hence can be arbitrarily large.

## Assumptions and scope

The parameter \(t\) means *forbidden clique size*, not a bound on the independence number. All graphs are finite simple graphs, and all homology is reduced simplicial homology over \(\mathbb Z\). The result allows unequal clique sizes and all boundary values \(s_i=t\). The permutation-action conclusion is integral and concerns homology, not an equivariant homotopy decomposition.

## Proof

**1. An exact deletion-and-link decomposition.** Every clique of size at least three in \(W\) lies in one complete petal: two private vertices from different petals are nonadjacent. Set \(N_i=s_i-1\) and, for \(1\le r\le N_i\), write \(L_i(r)\) for the simplicial complex of subsets of \(P_i\) of size at most \(r\) (the \((r-1)\)-skeleton of the simplex). A face avoiding the apex is permitted precisely when its intersection with each private petal has size at most \(t-1\); a face containing the apex is permitted precisely when every such intersection has size at most \(t-2\). Thus with
\[
A=*_{i=1}^{m}L_i(t-1), \qquad B=*_{i=1}^{m}L_i(t-2),
\]
there is an equality of simplicial complexes \(X=A\cup(c*B)\) with intersection \(B\). Geometric realization identifies \(X\) with the mapping cone of \(B\hookrightarrow A\).

**2. Topology of the simplex skeleta.** For a set \(P\) of \(N\) vertices and \(1\le r\le N\), the complex \(L(r)\) of subsets with size at most \(r\) is homotopy equivalent to \(\bigvee^{\binom{N-1}{r}}S^{r-1}\) (zero spheres when \(r=N\)). This follows by the standard deletion-of-a-vertex induction, or by explicit simplicial collapses to a wedge of boundaries of \(r\)-simplices. In particular, \(L(r)\) is \((r-2)\)-connected when noncontractible and has no nonzero reduced integral homology outside degree \(r-1\). There is a canonical integral homology identification
\[
\widetilde H_{r-1}(L(r);\mathbb Z)=\ker(\partial:\bigwedge^r\mathbb Z^P\to\bigwedge^{r-1}\mathbb Z^P)\cong\bigwedge^r U_P,
\quad U_P=\ker(\mathbb Z^P\xrightarrow{\sum}\mathbb Z).
\]
Indeed the augmented simplicial boundary on exterior chains is contraction by the summation covector. Choose a vector whose coordinate sum is one to split \(\mathbb Z^P\cong U_P\oplus\mathbb Z\). Contraction is zero on \(\bigwedge U_P\) and is an isomorphism from the complementary summand, proving the kernel identity *integrally* and equivariantly under \(S_P\).

**3. Two joins.** The join of the above skeletons gives
\[
A\simeq\bigvee^{\prod_i\binom{N_i-1}{t-1}} S^{d_A},\qquad
B\simeq\bigvee^{\prod_i\binom{N_i-1}{t-2}} S^{d_B},
\]
where \(d_A=m(t-1)-1\) and \(d_B=m(t-2)-1\). If an \(A\)-factor is a full simplex, then \(A\) is contractible and the first wedge has rank zero; otherwise \(A\) is \((d_A-1)\)-connected. All \(B\)-factors are proper skeleta and \(B\) has geometric dimension \(d_B\).

**4. The attachment is null.** Since \(d_B<d_A\) for every \(m\ge3\), and \(A\) is either contractible or a wedge of \(d_A\)-spheres, every map \(B\to A\) is nullhomotopic by cellular approximation. The cofiber of the inclusion therefore has homotopy type \(A\vee\Sigma B\). Substituting the ranks and dimensions above gives the two sphere families, including the full-simplex boundary cases. This proves an unrestricted integral homotopy classification; finite examples are not extrapolated.

**5. Natural integral symmetry.** The two homology degrees \(d_B+1=m(t-2)\) and \(d_A=m(t-1)-1\) are distinct. The cofiber long exact sequence identifies the lower homology canonically, up to the usual suspension orientation convention, with \(\widetilde H_{d_B}(B;\mathbb Z)\), and the higher homology with \(\widetilde H_{d_A}(A;\mathbb Z)\). The join-chain Künneth isomorphism and step 2 identify these with the displayed tensor products of exterior powers of augmentation lattices. No noncanonical integral splitting is used. Interchanging two equal-size petal factors of the join induces the Koszul sign \((-1)^{r^2}=(-1)^r\) on \(\bigotimes_i\bigwedge^r U_i\). For \(r=t-2\) or \(r=t-1\), this proves the claimed wreath-product actions.

As an explicit character check, for a permutation \(g\) of \(N=s-1\) private vertices, the trace on \(\bigwedge^r U_N\) is the coefficient of \(z^r\) in
\[
\frac{\prod_{\ell\in\operatorname{cyc}(g)}(1-(-z)^\ell)}{1+z}.
\]
For an element of \(S_{s-1}\wr S_m\), each cycle of \(q\) permuted petals contributes the trace of its ordered internal permutation product in this exterior-power character times \((-1)^{r(q-1)}\). The product over cycles is the character in the corresponding homology degree. This also follows from the integral tensor action and gives exact integer character values.

## Verification

The accompanying standalone script `check_clique_bouquet.py` uses only the Python standard library. It enumerates the actual clique-free faces, computes reduced boundary ranks over \(\mathbb F_2\), independently reconstructs signed simplicial Lefschetz numbers, and compares these with both sphere-rank predictions and wreath-product exterior-power characters. In its recorded execution it passed eight parameter checks (including unequal-size petals and the three-petal two-degree examples) and 360 exact signed-character checks. Five checks with two petals independently stress-test the face-generation boundary but are not part of the stated parameter range. These finite checks are corroboration, not proofs of the infinite family or of torsion-freeness; those follow from steps 1–5.

Run `python3 check_clique_bouquet.py` in a directory containing the script. The script is self-contained and requires no network access or external files.

## Relationship to prior work

Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs* (2026), arXiv:2602.09623v1, Theorem 3.3 and Corollary 3.4, prove that the clique-free complexes of block graphs are shellable. Every windmill here is a block graph. That shellability theorem does not specify its integral homotopy type, its two nonzero possible degrees, or its integral petal-permutation representation. Its clique-attachment results likewise address shellability rather than these graded topological invariants. Moradi's earlier work on clique ideals and the work of Khosh-Ahang and Moradi study algebraic properties for other graph families, without an identified equivalent multi-petal integral homotopy representation theorem. The classical simplicial-skeleton and join lemmas are standard background and not novel claims.

A previously investigated special case of *two* overlapping cliques with intersection of size at least two has explicit homology formulas; it does not contain the present multi-petal, single-vertex-gluing homotopy and wreath-symmetry statement. No general claim of classifying all block graphs is made.

## Limitations

The formula only concerns windmills made from complete petals sharing one apex, with at least three petals and clique threshold at least three. It does not classify arbitrary block-graph clique-free complexes, intersections along larger cliques, or equivariant homotopy types. The integral homology representation is established but a simultaneous group-equivariant wedge decomposition is not asserted. Relevant implicit or unindexed prior-work implications cannot be completely excluded. Independent mathematical review has not been performed.

## References

1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, first posted 2026-02-10, especially Theorem 3.3, Corollary 3.4, and §4. Full text: https://arxiv.org/html/2602.09623v1.
2. S. Moradi, *\(t\)-clique ideal and \(t\)-independence ideal of a graph*, arXiv:1712.00583, first posted 2017-12-02, https://arxiv.org/abs/1712.00583.
3. F. Khosh-Ahang and S. Moradi, *Some algebraic properties of \(t\)-clique ideals*, *Communications in Algebra* 47 (2019), DOI:10.1080/00927872.2018.1541462.
