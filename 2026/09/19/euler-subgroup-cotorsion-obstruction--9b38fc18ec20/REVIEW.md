# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was checked separately in the three boundary regimes \(B=\mathbb Z\), \(B=d\mathbb Z\) with \(d\geq2\), and \(B=\{0\}\).

Extension closure and weak idempotent completeness follow directly from additivity of Euler characteristic. Shifts preserve \(\mathcal A_B\), and contractible complexes have Euler characteristic zero, so the standard cone sequences stay inside the category and give the Frobenius structure.

The Ext calculation is the usual degreewise-split calculation
\[
\operatorname{Ext}^1(X,Y)\cong\bigoplus_n\operatorname{Hom}_k(H^n(X),H^{n+1}(Y)).
\]
For the reverse ideal orthogonality, the test objects \(S^r(k^d)\) work for \(B=d\mathbb Z\), \(d\geq1\), while \(S^r(k)\oplus S^{r+1}(k)\) works for \(B=\{0\}\). These detect every forbidden nonzero cohomology map.

The object-ideal factorizations were checked with the same two cases: \(L^{\oplus d}\) and \(W^{\oplus d}\) for positive \(d\), and \(L\oplus L[1]\) and \(W\oplus W[-1]\) in the zero-Euler case. The added summands have the required cohomological support and correct Euler characteristic.

For completeness of the ideal pair, the kernel and cokernel calculations in the displayed cone constructions were checked explicitly. For \(d\geq1\),
\[
\chi(E_A)=\chi(A)-d\chi(U),\qquad
\chi(D_A)=\chi(A)-d\chi(V),
\]
so the middle terms stay in \(\mathcal A_{d\mathbb Z}\). For \(B=\{0\}\), the paired shifts \(U[-1]\oplus U[-2]\) and \(V[1]\oplus V[2]\) have Euler characteristic zero, and the corresponding middle terms have the same Euler characteristic as \(A\).

The object-level criterion follows from the long exact cohomology sequence: any special \(\mathcal F_B\)-object precover has cohomology exactly \(H^{\leq0}(A)\), and dually any special \(\mathcal C_B\)-object preenvelope has cohomology exactly \(H^{\geq2}(A)\). The converse uses the undoubled cone sequences once the relevant truncation Euler characteristic lies in \(B\).

The sharp boundary is then immediate. A proper subgroup \(B<\mathbb Z\) does not contain \(1\), whereas
\[
S^0(k)\oplus S^1(k),\qquad S^1(k)\oplus S^2(k)
\]
have total Euler characteristic zero but the relevant truncation has Euler characteristic \(1\). For \(B=\mathbb Z\), no restriction remains and both special object approximations exist.

The idempotent-completion statement is checked by \(X\mid X^{\oplus d}\) for \(d\geq2\) and \(X\mid X\oplus X[1]\) for \(B=\{0\}\).

## Originality

PASS, to the best of our knowledge.

The current full text of Ren--Wang, arXiv:2609.18681v1, was inspected. It treats the even-total-cohomology category, equivalently the Euler subgroup \(2\mathbb Z\), and its exact specialness criterion is stated in parity form. It does not state the arbitrary-subgroup family, the zero-Euler case, or the equivalence
\[
(\mathcal F_B,\mathcal C_B)\text{ complete}\iff B=\mathbb Z.
\]

Directed searches for ideal cotorsion pairs combined with Euler-characteristic subgroup or congruence restrictions did not locate the displayed theorem. The earlier Wang--Wang--Zhu counterexample, arXiv:2609.14382v1, is structurally different and is intrinsically not weakly idempotent complete. The original ideal-approximation framework of Fu--Guil Asensio--Herzog--Torrecillas is treated as prior art.

A residual originality risk remains because the proof is a conceptual extension of the newly posted parity example, and similar Grothendieck-group restriction constructions may occur in older exact-category literature under different terminology. No claim of exhaustive literature coverage is made.

## Value

PASS.

The result shows that the recent parity obstruction is one point in a complete one-parameter lattice of Euler restrictions. It identifies the sharp boundary for object completeness, gives exact object-by-object specialness criteria, and includes the zero-Euler category, which is not a positive-modulus congruence case.

The theorem also explains why simply replacing “even total cohomology dimension” by divisibility by \(d>2\) is not the right generalization: total cohomology dimension is not extension-additive, whereas Euler characteristic is. Thus the extension isolates the invariant responsible for the exact-category construction rather than merely changing the numerical modulus.

## Limitations

The result concerns bounded complexes of finite-dimensional vector spaces with the degreewise split exact structure. It does not classify completeness-descent failures in arbitrary Frobenius exact categories. The \(B=2\mathbb Z\) case and the underlying extension calculations are prior work. Originality is to the best of our knowledge and is not independent validation.
