# Color-permutation characters of complete-graph Hom complexes

## Finding

**Theorem.** For every pair of integers \(2\le m\le n\), consider \(X_{m,n}=\operatorname{Hom}(K_m,K_n)\), with the symmetric group \(S_n\) permuting the \(n\) target colors. Write \(c(g)\) for the number of cycles of \(g\in S_n\), counting fixed points. All reduced rational homology of \(X_{m,n}\) is concentrated in degree \(n-m\), where its character is
\[
\chi_{m,n}(g)=(-1)^m\operatorname{sgn}(g)
\sum_{j=2}^{m}(-1)^j\binom mj(j-1)^{c(g)}.
\]
Equivalently, in the rational representation ring of \(S_n\), with \(F_{n,q}=\mathbb Q[\operatorname{Fun}([n],[q])]\) the permutation module on all functions from an \(n\)-set to a \(q\)-set,
\[
[\widetilde H_{n-m}(X_{m,n};\mathbb Q)]
=(-1)^m[\operatorname{sgn}]\sum_{j=2}^{m}(-1)^j\binom mj[F_{n,j-1}].
\]
This is an equality in the representation ring; the alternating virtual expression does not assert a corresponding direct-sum decomposition over \(\mathbb Z\).

Moreover, for **every** such \(m,n\), the full target-color symmetry quotient is rationally acyclic:
\[
\widetilde H_i(|X_{m,n}|/S_n;\mathbb Q)=0
\qquad\text{for all integers }i.
\]
For the three-source-vertex family \(m=3\), the character simplifies to \(\chi_{3,n}(g)=\operatorname{sgn}(g)(2^{c(g)}-3)\), and for \(n\ge3\) the complete decomposition into irreducible rational Specht modules is
\[
\widetilde H_{n-3}(X_{3,n};\mathbb Q)
\cong\operatorname{sgn}\otimes
\left((n-2)S^{(n)}\oplus
\bigoplus_{j=1}^{\lfloor n/2\rfloor}(n-2j+1)S^{(n-j,j)}\right).
\]
All multiplicities appearing here are positive in their stated ranges.

## Assumptions and scope

The graphs \(K_m\) and \(K_n\) are finite, simple, unlooped complete graphs. An actual cell of \(X_{m,n}\) is an ordered \(m\)-tuple \((A_1,\ldots,A_m)\) of pairwise disjoint, **nonempty** subsets of \([n]\). The cell is the product \(\Delta^{A_1}\times\cdots\times\Delta^{A_m}\), with dimension \(\sum_i(|A_i|-1)\). The face relation reduces one or more blocks to a nonempty subset. The action of \(S_n\) permutes labels in each block, never the \(m\) block positions. In particular, source-position permutations are a different action and are not being analyzed here.

The case \(n=m\), when the complex consists of \(m!\) isolated points, is included: its top reduced homology is in degree zero. Homology and character decompositions are over \(\mathbb Q\); the known nonequivariant wedge-of-spheres fact also implies free integral homology but does not determine its integral \(S_n\)-lattice.

## Proof

**1. Homological concentration.** Babson and Kozlov establish that \(\operatorname{Hom}(K_m,K_n)\) is homotopy equivalent to a wedge of \((n-m)\)-spheres for \(n\ge m\ge2\) [1, Section 4.3, Proposition 4.5]. This is used only as a nonequivariant fact. Hence, with \(d=n-m\), the reduced Lefschetz number of an action \(g\) equals \((-1)^d\) times the trace of \(g\) on \(\widetilde H_d\), including the zero-dimensional case.

**2. Signed fixed-cell trace.** Orient each product cell by increasing order of target labels within every simplex factor and by the fixed order of the \(m\) factors. A cell contributes to the cellular trace of \(g\) precisely if each \(A_i\) is a union of complete cycles of \(g\). If the cell uses exactly \(q\) of the \(c=c(g)\) cycles and hence a total of \(t\) target labels, then its dimension is \(t-m\), while the orientation permutation contributes \((-1)^{t-q}\). Its signed Lefschetz weight is therefore \((-1)^{q-m}\), independent of individual cycle lengths.

Choose the \(q\) used cycles, then distribute them surjectively among the \(m\) labeled nonempty blocks. Writing \(\left\{\begin{smallmatrix}q\\m\end{smallmatrix}\right\}\) for the Stirling number of the second kind, the ordinary Lefschetz number is
\[
L(g)=\sum_{q=m}^{c}(-1)^{q-m}\binom cq
m!\left\{\begin{smallmatrix}q\\m\end{smallmatrix}\right\}.
\]
The standard inclusion-exclusion identity
\[
m!\left\{\begin{smallmatrix}q\\m\end{smallmatrix}\right\}=
\sum_{j=0}^{m}(-1)^{m-j}\binom mj j^q
\]
then gives, using the binomial theorem,
\[
L(g)=\sum_{j=0}^{m}(-1)^j\binom mj(1-j)^c.
\]
Because \(n\ge2\), \(c\ge1\); the \(j=0\) term is \(1\), and the \(j=1\) term vanishes. Consequently
\[
(-1)^{n-m}(L(g)-1)=(-1)^{n-m+c}
\sum_{j=2}^{m}(-1)^j\binom mj(j-1)^c.
\]
Finally, \(\operatorname{sgn}(g)=(-1)^{n-c}\), so \((-1)^{n-m+c}=(-1)^m\operatorname{sgn}(g)\). This proves the character formula and its virtual permutation-module formulation: \(\operatorname{tr}(g|F_{n,q})=q^{c(g)}\), since a fixed function must be constant on each cycle.

**3. Vanishing for the symmetry quotient.** In every term \(F_{n,q}\) above, \(1\le q\le m-1<n\). Every function \([n]\to[q]\) repeats some value, so its stabilizer contains a transposition. By Frobenius reciprocity the sign representation has multiplicity zero in each \(F_{n,q}\). The representation-ring formula implies that the multiplicity of the trivial representation in \(\widetilde H_d(X_{m,n};\mathbb Q)\) vanishes. Equivariantly subdividing the finite polytopal complex and applying the rational averaging/transfer argument identifies \(H_i(|X_{m,n}|/S_n;\mathbb Q)\) with the \(S_n\)-invariants of \(H_i(X_{m,n};\mathbb Q)\). Thus all reduced rational homology of the quotient vanishes, including in degree zero.

**4. Three-block Specht refinement.** For \(m=3\), the character is \(\operatorname{sgn}(g)(2^{c(g)}-3)\). The function permutation module \(F_{n,2}\) is the rational permutation module on all subsets of \([n]\), and its homogeneous cardinality components are the \(k\)-subset modules. By Young's rule, the latter decomposes as \(\bigoplus_{j=0}^{\min(k,n-k)}S^{(n-j,j)}\). For fixed \(j\), the number of cardinalities containing it is \(n-2j+1\). Removing three copies of the trivial module leaves the coefficient \(n-2\) on \(S^{(n)}\); tensoring with the sign representation yields the claimed decomposition. Since rational representations of finite groups are semisimple, equality of characters gives actual rational module isomorphism.

## Verification

Three self-contained Python scripts accompany this statement. Run them from the enclosing directory as `python3 artifacts/check_cells.py`, `python3 artifacts/verify_chain.py`, and `python3 artifacts/verify_action.py`; they use only the Python standard library. The first enumerates all Hom cells and signed fixed-cell traces over each target permutation in eight small cases, including \(n=m\). The second independently builds the augmented cellular boundary and computes ranks over a large prime field for ten finite cases. The third calculates integral fundamental cycles in the one-dimensional complex \(X_{3,4}\) and checks the induced rational-character traces for all 24 color permutations directly on the homology cycles. All three produce explicit terminal success markers and halt on discrepancies. They are consistency checks; the infinite-range proof is the counting argument above together with [1].

## Relationship to prior work

Babson and Kozlov [1] prove the general nonequivariant wedge-of-spheres result and provide Betti-number formulas. Both are prior coverage and **not** claimed as new here. The new statement determines the natural target-color \(S_n\)-character, its virtual function-module description, the exact reduced rational acyclicity of its full target-color quotient, and the explicit Specht decomposition for three source vertices. In [1], the prominent involution on \(K_m\) interchanges source positions; this differs from the action analyzed here. Thansri [2] establishes equivariant comparison theorems for the symmetry of source factors in hypergraph Hom and box complexes, rather than the target-color character. Dochtermann [3] studies the graph-homotopy and Hom-complex functorial framework rather than this representation. Babson and Kozlov [4] examine Boolean-algebra and deleted-join diagrams with other symmetric actions. No stronger published formula was identified from these inspected sources and targeted searches, but equivalence in unindexed literature remains possible.

## Limitations

This is a rational equivariant homology statement, not an integral group-ring lattice theorem or an equivariant homotopy equivalence. Rational acyclicity of the quotient **does not** imply its contractibility or integral acyclicity. The proof relies explicitly on the previously published nonequivariant homotopy classification [1]. The finite checks do not independently certify the theorem for unbounded parameters. A prior equivalent equivariant character computation may exist outside the inspected literature; publication priority is not certified.

## References

[1] E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056, first submitted 5 October 2003, especially Section 4.3 and Propositions 4.5–4.6; published in *Israel Journal of Mathematics* 152 (2006), 285–312.

[2] T. Thansri, *Simple \(\Sigma_r\)-homotopy types of Hom complexes and box complexes assigned to \(r\)-graphs*, *Kyushu Journal of Mathematics* 66 (2012), 493–508, doi:10.2206/kyushujm.66.493.

[3] A. Dochtermann, *Hom complexes and homotopy theory in the category of graphs*, arXiv:math/0605275.

[4] E. Babson and D. N. Kozlov, *Diagrams of classifying spaces and \(k\)-fold Boolean algebras*, arXiv:math/9704227.
