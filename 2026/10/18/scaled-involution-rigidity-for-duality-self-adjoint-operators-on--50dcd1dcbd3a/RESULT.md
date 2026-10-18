# Scaled-involution rigidity for duality-self-adjoint operators on \(\ell_p\)

## Finding

Let \(I\) be any index set with at least two elements, let \(\mathbb K\) be \(\mathbb R\) or \(\mathbb C\), and fix \(1<p<\infty\), \(p\ne2\). Equip \(X=\ell_p(I;\mathbb K)\) with its usual norm and normalized duality map \(J_p\). For every bounded \(\mathbb K\)-linear operator \(T:X\to X\), the identity
\[
T'J_p(x)=J_p(Tx)\qquad\text{for every }x\in X
\]
(where \(T'\) is the Banach transpose) holds **if and only if** either \(T=0\), or there exist a real \(c>0\), an involution \(\pi:I\to I\), and unimodular scalars \(\omega_j\in\mathbb K\) satisfying
\[
\pi^2=\operatorname{id},\qquad
\omega_{\pi(j)}=\overline{\omega_j},\qquad
Te_j=c\omega_j e_{\pi(j)}\quad(j\in I).
\]
In the real case, unimodular means \(\omega_j\in\{-1,1\}\). In the nonzero case, \(T/c\) is a surjective isometric involution and
\[
T^2=c^2I,\qquad\|T\|=c,\qquad\sigma(T)\subseteq\{-c,c\}.
\]
Consequently, **the zero operator is the only compact duality-self-adjoint operator on infinite-dimensional \(\ell_p(I)\) when \(p\ne2\)**. The statement has no analogue at \(p=2\): arbitrary bounded Hilbert-space self-adjoint operators then satisfy the displayed duality identity.

## Assumptions and scope

For \(q=p/(p-1)\), identify \(X^*\) with \(\ell_q(I;\mathbb K)\) through linear functionals \(a(y)=\sum_{i\in I}a_i y_i\). For \(x\ne0\), set
\[
(J_p x)_i=\|x\|_p^{\,2-p}|x_i|^{p-2}\overline{x_i},
\qquad J_p(0)=0,
\]
with a zero coordinate interpreted as zero. This normalization ensures \(\|J_p x\|_q=\|x\|_p\), \((J_p x)(x)=\|x\|_p^2\), and \(J_p(\alpha x)=\overline\alpha J_p(x)\) for complex \(\alpha\). The transpose is defined by \((T'a)(x)=a(Tx)\), not by a Hilbert-space conjugate transpose. All identities are asserted for every vector, not just basis vectors, and \(I\) may be infinite or uncountable.

## Proof

**1. The two-coordinate identity.** Let \(e_j\) be the canonical unit vectors and write \(v=Te_j\), \(w=Te_k\) for distinct \(j,k\in I\). At a unit vector, \(J_p(e_j)=e_j^*\), so the defining operator identity gives
\[
T'J_p(e_j)=J_p(v),\qquad T'J_p(e_k)=J_p(w).
\]
Applying the same identity to \(e_j+t e_k\), with real \(t>0\), yields the **exact functional identity**
\[
J_p(v+tw)=(1+t^p)^{(2-p)/p}
   \bigl(J_p(v)+t^{p-1}J_p(w)\bigr).\tag{1}
\]
We show that distinct columns have disjoint coordinate supports.

**2. Disjointness below the Hilbert exponent.** Suppose \(1<p<2\), \(v\ne0\), and \(v_i\ne0\). The \(i\)-th coordinate of the left side of (1) differs from \((J_pv)_i\) by \(O(t)\): the scalar map \(z\mapsto|z|^{p-2}\overline z\) is continuously differentiable away from zero, and the norm factor is locally Lipschitz away from zero. The right side differs by
\[
t^{p-1}(J_pw)_i+O(t^p)+O(t^{2p-1}).
\]
Because \(p-1<1\), division by \(t^{p-1}\) and passage to zero give \((J_pw)_i=0\), equivalently \(w_i=0\). Thus \(\operatorname{supp}(v)\cap\operatorname{supp}(w)=\varnothing\).

**3. Disjointness above the Hilbert exponent.** Let \(p>2\) and \(v\ne0\). Equation (1) implies
\[
J_p(v+tw)-J_p(v)=o(t)\quad\text{in }X^*.
\]
The function \(F(z)=\tfrac12\|z\|_p^2\) is twice differentiable in real directions at every nonzero \(z\in X\); its first real derivative is \(\operatorname{Re}(J_pz)(\cdot)\). Therefore \(F''(v)[w,w]=0\). To identify its null directions, write \(r=\|v\|_p\); for nonzero \(v_i\), set \(b_i=\operatorname{Re}(\overline{v_i}w_i)/|v_i|\), and set \(b_i=0\) for \(v_i=0\). Introduce the convergent sums
\[
B=\sum_i|v_i|^{p-2}|w_i|^2,\quad
C=\sum_i|v_i|^{p-2}b_i^2,\quad
A=\sum_i|v_i|^{p-1}b_i.
\]
Differentiating \(F=\tfrac12(\sum_i|z_i|^p)^{2/p}\) twice along the real line \(v+tw\) gives
\[
F''(v)[w,w]=r^{2-p}\left[B+(p-2)
\left(C-\frac{A^2}{r^p}\right)\right].\tag{2}
\]
Weighted Cauchy--Schwarz gives \(A^2\le r^p C\), hence (2) is at least \(r^{2-p}B\). Since it is zero, \(B=0\), so \(w_i=0\) wherever \(v_i\ne0\). The formula and differentiations are valid in arbitrary \(\ell_p(I)\): all vectors have countable support, and the relevant sums converge by Hölder's inequality; for \(p>2\), the squared norm is twice Fréchet differentiable away from zero. The same disjointness conclusion follows.

**4. Exact matrix support.** For every \(j\), the identity at \(e_j\) says that row \(j\) of the matrix of \(T\) is the coordinate vector \(J_p(Te_j)\). Hence row \(j\) and column \(j\) have precisely the same support. Pairwise disjoint columns mean that each row contains at most one nonzero entry, so this row--column support equality forces each column to contain at most one nonzero entry.

If \(Te_j=0\) for some \(j\) and \(Te_k\ne0\) for another \(k\), the identity at \(e_k+t e_j\) reduces to
\[
J_p(Te_k)=(1+t^p)^{(2-p)/p}J_p(Te_k),
\]
which is impossible for \(t>0\) because \(p\ne2\). Thus a nonzero \(T\) has exactly one nonzero entry in every column, and therefore exactly one in every row. Write \(Te_j=a_j e_{\pi(j)}\). Row--column support symmetry implies \(\pi^2(j)=j\), and the coefficient comparison at \(e_j\) gives
\[
a_{\pi(j)}=\overline{a_j}.\tag{3}
\]

**5. Uniform modulus.** For any distinct indices \(j,k\), compare the coefficient of \(e_{\pi(j)}^*\) in (1), using the now disjoint monomial supports. After cancelling \(\overline{a_j}\ne0\), one obtains
\[
\bigl(|a_j|^p+t^p|a_k|^p\bigr)^{(2-p)/p}|a_j|^{p-2}
=(1+t^p)^{(2-p)/p}.
\]
Since \(p\ne2\), raising to \(p/(2-p)\) gives \(|a_k|^p=|a_j|^p\). Thus all weights have a common modulus \(c>0\). Writing \(a_j=c\omega_j\) gives precisely the stated classification.

**6. Converse and consequences.** Every indicated weighted permutation \(U=T/c\) is a surjective linear isometry, has \(U^2=I\) by (3), and satisfies \(J_p(Ux)=(U^{-1})'J_p(x)=U'J_p(x)\); multiplying by positive real \(c\) establishes the required identity for \(T\). The zero operator works as well. The equality \(T^2=c^2I\) yields its inverse and spectral inclusion. If \(I\) is infinite, a compact operator cannot satisfy \(T^2=c^2I\) with \(c>0\), because then \(I\) would be compact. At \(p=2\), the duality map is conjugate-linear Riesz identification, and the condition becomes usual Hilbert-space self-adjointness; for example, non-scalar real diagonal operators satisfy it.

## Verification

The proof supplies an exact, infinite-dimensional argument. The two essential nonstandard steps are the support separation from (1), with the Hessian lower bound (2) for \(p>2\), and the row--column symmetry forced by evaluation at basis vectors. Both are stated with their normalizations and quantifiers above. The standalone finite diagnostics in `checker.py` use only the Python standard library and verify 480 randomly generated scaled involutions, including complex phases, alongside 960 exclusions of projections or unequal diagonal scalings for six non-Hilbert exponents. Numerical diagnostics are not substituted for the analytic proof.

## Relationship to prior work

Shameem and Deepesh (arXiv:2608.06873v1, publicly posted 7 August 2026) study spectral representations of compact operators that obey exactly the duality-self-adjoint identity on smooth Banach spaces. Their theorem is general in the underlying space but does not give the present full classification on \(\ell_p\), including noncompact operators; the present compact-vanishing conclusion is specific to non-Hilbert sequence geometry. García-Pacheco (2023) defines general adjoints through duality maps and establishes their fundamental norm and unitary properties; those do not assert the above necessity of scaled involutive isometry for all nonzero \(\ell_p\) solutions. The published result *Contractive spectral tails for compact duality-self-adjoint operators* treats spectral projections of compact operators under the same abstract condition, but neither its statement nor its proof supplies this \(\ell_p\) classification. García-Pacheco's earlier 2020 article defines the underlying self-adjointness notion and reports non-Hilbert examples; only abstract/metadata were accessible for that article, so an earlier equivalent special result cannot be excluded categorically.

## Limitations

This theorem is about the normalized duality map and the **full functional identity for every vector**, not weaker numerical-range or Lumer-Hermitian conditions. It does not classify general \(L_p\) spaces, arbitrary smooth Banach spaces, endpoints \(p=1,\infty\), or \(p=2\). It proves no originality priority beyond the actual literature comparisons: the inaccessible full text of the 2020 precursor and any unnoticed equivalent formulation remain priority risks.

## References

1. M. Shameem and D. K. P., *Spectral theorem for compact self-adjoint operators on smooth Banach spaces*, arXiv:2608.06873v1 (7 August 2026), https://arxiv.org/html/2608.06873.
2. F. J. García-Pacheco, *The adjoint of an operator on a Banach space*, Collectanea Mathematica 75 (2024), 823--840; online 21 August 2023, https://doi.org/10.1007/s13348-023-00414-8.
3. F. J. García-Pacheco, *Selfadjoint operators on real or complex Banach spaces*, Nonlinear Analysis 192 (2020), 111696, https://doi.org/10.1016/j.na.2019.111696 (full text not accessible in this review).
4. *Contractive spectral tails for compact duality-self-adjoint operators*, published research record dated 18 September 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-spectral-gap-contractions-duality-self-adjoint--db9d68568bf9.
