# Every finite field admits a two-dimensional idempotent-free perfect evolution algebra
## Finding
Let \(K=\mathbb F_q\) be any finite field. There exists \(d\in K\) such that the two-dimensional evolution algebra \(E_d\) with natural basis \(e_1,e_2\) and multiplication
\[
e_1e_2=0,\qquad e_1^2=e_2,\qquad e_2^2=e_1+d e_2
\]
is perfect, hence non-solvable, and has no non-zero idempotent. More precisely, every parameter
\[
d\notin\{b^{-1}-b^2:b\in K^\times\}
\]
has these properties. Therefore the least positive dimension of an idempotent-free non-solvable evolution algebra over every finite field is exactly \(2\).

## Assumptions and scope
An evolution algebra over a field \(K\) is a commutative algebra admitting a natural basis \(e_1,e_2\) with \(e_1e_2=0\). The derived series is \(A^{(1)}=A\) and \(A^{(m+1)}=A^{(m)}A^{(m)}\). An algebra is solvable when some derived term is zero. Here \(K\) is any finite field, including characteristic \(2\). The result is an existence theorem and a sharp minimum-dimension statement; it does not classify all idempotent-free two-dimensional evolution algebras.

## Proof
Fix \(d\in K\) and define \(E_d\) by the displayed multiplication. Relative to the natural basis, its structure matrix is
\[
M_d=\begin{pmatrix}0&1\\1&d\end{pmatrix},
\]
whose determinant is \(-1\), which is non-zero over every field. Hence \(e_1^2\) and \(e_2^2\) span \(E_d\), so \(E_d^2=E_d\). Therefore every term of the derived series equals \(E_d\), and \(E_d\) is non-solvable.

Now write \(x=a e_1+b e_2\). Since mixed products vanish,
\[
x^2=b^2e_1+(a^2+d b^2)e_2.
\]
Thus \(x^2=x\) is equivalent to
\[
a=b^2,\qquad b=a^2+d b^2.
\]
If \(b=0\), then \(a=0\). If \(b\ne0\), substituting \(a=b^2\) gives
\[
b=b^4+d b^2,
\]
and division by \(b\) gives
\[
d=b^{-1}-b^2.
\]
Consequently the non-zero idempotents of \(E_d\) are in bijection with the non-zero \(b\in K\) satisfying this last equation.

Define \(g:K^\times\to K\) by \(g(b)=b^{-1}-b^2\). Its domain has \(q-1\) elements while its codomain has \(q\) elements, so \(g\) is not surjective. Choose \(d\in K\setminus g(K^\times)\). Then \(E_d\) has no non-zero idempotent, while the first paragraph shows that it is perfect and non-solvable.

It remains to prove minimality. Every one-dimensional algebra has a basis element \(e\) with \(e^2=\lambda e\). If \(\lambda=0\), the algebra is solvable. If \(\lambda\ne0\), then \(\lambda^{-1}e\) is a non-zero idempotent. Hence no one-dimensional idempotent-free non-solvable algebra exists, and the minimum positive dimension is \(2\).

## Verification
The proof is symbolic and uses only field arithmetic and the pigeonhole principle. Two boundary checks illustrate that no characteristic restriction is hidden. Over \(\mathbb F_2\), the image of \(g\) is \(\{0\}\), so \(d=1\) works. Over \(\mathbb F_3\), the image is \(\{0,1\}\), so \(d=2\) works. These finite checks are illustrative only; the arbitrary finite-field statement follows from \(|K^\times|=q-1<q=|K|\).

## Relationship to prior work
García-Martínez and Pérez-Rodríguez proved that every complex regular evolution algebra has a non-zero idempotent and formulated the complex solvability/idempotent conjecture. Hu and Wen disproved that conjecture in dimension \(3\) over \(\mathbb C\), and their Remark 2 records a two-dimensional idempotent-free non-solvable example over \(\mathbb F_3\). The present result turns that isolated finite-field observation into a uniform theorem for every finite field, including characteristic \(2\), and determines the minimum dimension in every finite-field case.

The classification of two-dimensional perfect evolution algebras over domains by Cabrera Casado, Martín Barquero, and Martín González includes the ambient family containing \(E_d\), but the checked classification does not analyze which finite-field parameters eliminate all non-zero idempotents. González Nevado's field-dependent idempotent framework gives the \(\mathbb F_3\) example and also an example over \(\mathbb Q\), while asking for field-level conditions; the cardinality argument above supplies a uniform finite-field answer in dimension \(2\).

## Limitations
The theorem proves existence, not the number of admissible parameters \(d\), the number of isomorphism classes, or a classification of all two-dimensional idempotent-free evolution algebras. The finite-field hypothesis is essential to the counting step; no assertion is made for arbitrary infinite fields. The result does not classify higher-dimensional counterexamples.

## References
1. X.-Y. Hu and R. Wen, *Idempotent-Free Non-Solvable Evolution Algebras over C*, Preprints 2026, 202609.0078; arXiv:2609.25023.
2. X. García-Martínez and A. Pérez-Rodríguez, *A note on complete evolution algebras*, Archiv der Mathematik 126 (2026), 597–604; arXiv:2512.12418.
3. Y. Cabrera Casado, D. Martín Barquero, and C. Martín González, *Two-dimensional perfect evolution algebras over domains*, Journal of Algebraic Combinatorics 58 (2023), 569–587, DOI 10.1007/s10801-022-01196-1.
4. A. González Nevado, *Order Structures around Evolution Algebras*, arXiv:2505.01444.
