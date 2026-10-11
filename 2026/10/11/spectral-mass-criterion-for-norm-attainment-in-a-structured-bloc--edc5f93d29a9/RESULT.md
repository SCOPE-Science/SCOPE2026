# Spectral-mass criterion for norm attainment in a structured block operator matrix

## Finding
Let \(H,K\) be complex Hilbert spaces, let \(A\in\mathbb B(K,H)\), let \(a,b,c\in\mathbb C\), and let \(\varphi:[0,\infty)\to\mathbb R\) be continuous with \(\varphi(t)\ge \varphi(0)\ge0\). Define
\[
T=\begin{pmatrix}aI_H&A\\ cA^*&b\varphi(|A|)\end{pmatrix},
\qquad
M_t=\begin{pmatrix}a&t\\ ct&b\varphi(t)\end{pmatrix}.
\]
Set \(B=|A^*|\), \(L=\|T\|\), and
\[
\Omega=\{t\in\sigma(B):\|M_t\|=L\}.
\]
If \(E_B\) denotes the spectral measure of \(B\), then
\[
T\text{ attains its norm}\quad\Longleftrightarrow\quad E_B(\Omega)\ne0.
\]
This removes the singleton-maximizer hypothesis from the point-spectrum criterion in the focal source. When \(\Omega=\{t_0\}\), the condition becomes \(E_B(\{t_0\})\ne0\), equivalently \(t_0\in\sigma_p(B)\).

There is also a non-atomic regime that the singleton criterion cannot see. Let \(H=K=L^2([0,1])\), let \(A\) be multiplication by the independent variable, fix \(r\in(0,1)\), and take \(a=c=0\) and \(b=1\). Define
\[
\varphi(t)=
\begin{cases}
\dfrac{\sqrt{1-r^2}}{r}t,&0\le t\le r,\\
\sqrt{1-t^2},&r\le t\le1,\\
0,&t\ge1.
\end{cases}
\]
Then \(\varphi\) is continuous, nonnegative, and \(\varphi(0)=0\). The operator \(A\) has norm \(1\) but no norming vector. Nevertheless \(\|M_t\|=1\) for every \(t\in[r,1]\), so \(\Omega=[r,1]\) and \(E_A(\Omega)\ne0\). Hence the associated block operator \(T\) attains its norm.

## Assumptions and scope
The result concerns exactly the block family above and ordinary norm attainment on complex Hilbert spaces. No strict monotonicity of \(t\mapsto\|M_t\|\) is assumed. The focal source proves that \(\|T\|=\max_{t\in\sigma(B)}\|M_t\|\) and that norm attainment of \(T\) is equivalent to norm attainment of the corresponding block functional calculus in \(B=|A^*|\); those facts are used here. The conclusion is not a statement about absolute norm attainment on every subspace.

## Proof
By the polar-decomposition reduction in arXiv:2605.25283v1, norm attainment of \(T\) is equivalent to norm attainment of
\[
\widetilde T=
\begin{pmatrix}
aI_H&B\\
cB&b\varphi(B)
\end{pmatrix}
\quad\text{on }H\oplus H,
\]
and
\[
L=\|\widetilde T\|=\max_{t\in\sigma(B)}\|M_t\|.
\]
Apply the spectral theorem to \(B\). In a direct-integral representation, \(B\) acts as multiplication by the scalar parameter \(t\), and \(\widetilde T\) acts fibrewise as \(M_t\) on the two-dimensional coefficient factor. Thus, for every vector field \(\xi(t)\),
\[
\|\widetilde T\xi\|^2
=\int \|M_t\xi(t)\|^2\,d\mu(t)
\le \int \|M_t\|^2\|\xi(t)\|^2\,d\mu(t)
\le L^2\|\xi\|^2.
\]

If \(E_B(\Omega)=0\), then every nonzero vector field has positive mass outside \(\Omega\). On that set \(L^2-\|M_t\|^2>0\). Therefore equality in the preceding estimate is impossible for a unit vector, and \(\widetilde T\) does not attain its norm.

Conversely, assume \(E_B(\Omega)\ne0\). On \(\Omega\), the positive matrix \(M_t^*M_t\) has top eigenvalue \(L^2\). Its top spectral projection is a Borel matrix-valued function of \(t\); on a nonzero spectral subspace carried by \(\Omega\), choose a nonzero measurable vector field in that top eigenspace and normalize it in the direct integral. For the resulting unit vector \(\xi\),
\[
\|M_t\xi(t)\|=L\|\xi(t)\|
\quad\text{for almost every }t
\]
on its support. Hence \(\|\widetilde T\xi\|=L\), so \(\widetilde T\), and therefore \(T\), attains its norm.

For the explicit example, \(A\) is multiplication by \(t\) on \(L^2([0,1])\), so \(\sigma(A)=[0,1]\) and \(1\) is not an eigenvalue; hence \(A\) does not attain its norm. Since \(a=c=0\) and \(b=1\),
\[
M_t=\begin{pmatrix}0&t\\0&\varphi(t)\end{pmatrix},
\qquad
\|M_t\|=\sqrt{t^2+\varphi(t)^2}.
\]
For \(0\le t\le r\), this norm equals \(t/r\le1\); for \(r\le t\le1\), it equals \(1\). Thus \(L=1\) and \(\Omega=[r,1]\). The spectral projection \(E_A([r,1])\) is multiplication by the indicator of \([r,1]\), so it is nonzero. The criterion therefore gives norm attainment of \(T\).

## Verification
The proof was checked at the level of the spectral-theorem representation and the equality case in the fibrewise norm estimate. The zero set of
\[
\det\!\bigl(L^2I_2-M_t^*M_t\bigr)
\]
is exactly \(\Omega\), because \(L^2\) dominates every eigenvalue of \(M_t^*M_t\). Hence the criterion is consistent with the determinant argument used in the focal source for singleton \(\Omega\). The explicit example was checked symbolically from the displayed piecewise formula for \(\varphi\); no finite experiment is used as proof.

## Relationship to prior work
Wu, Ling, and Xu prove the norm formula \(\|T\|=\max_{t\in\sigma(|A^*|)}\|M_t\|\), show sufficiency when a maximizing \(t_0\) is an eigenvalue of \(|A^*|\), and prove necessity under the additional hypothesis that the maximizing set \(\Omega\) is a singleton. Their main theorem then uses strict monotonicity to force \(\Omega=\{\|A\|\}\). The present criterion replaces the singleton/point-spectrum condition by the exact spectral-mass condition \(E_{|A^*|}(\Omega)\ne0\), covering atomic and non-atomic maximizer sets uniformly.

Nag and Golla study absolute norm attainment for positive \(2\times2\) block operator matrices, a stronger property requiring norm attainment on every nonzero closed subspace. That setting does not provide the spectral-mass characterization for the present structured family.

## Limitations
The criterion relies on the special commutative functional-calculus structure in \(|A^*|\). It does not claim a corresponding criterion for arbitrary noncommuting block operator matrices. The measurable top-eigenspace selection is finite-dimensional in the coefficient fibre; extending the statement to infinite matrix fibres would require additional measurable-field hypotheses. Literature searches did not reveal an equivalent published statement, but an older formulation in the language of decomposable operators could still exist.

## References
1. K. Wu, J. Ling, and Q. Xu, *Norm attainment of a class of block operator matrices*, arXiv:2605.25283v1, 2026.
2. P. Nag and R. Golla, *On Absolutely norm (minimum) attaining \(2\times2\) block operator matrix*, arXiv:2507.11148v1, 2025.
3. R. V. Kadison and J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Vol. I*, American Mathematical Society, 1997.
