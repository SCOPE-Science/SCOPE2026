# A two-dimensional phase law for determinant comparisons of \(|AB|\) and \(|BA|\)

Let \(A\in M_2(\mathbb C)\) be positive definite and let \(B\in M_2(\mathbb C)\) be invertible Hermitian. For real \(k,p\), set
\[
\Delta_{k,p}(A,B)
=
\det\!\bigl(A^k+|AB|^p\bigr)
-
\det\!\bigl(A^k+|BA|^p\bigr).
\]

## Theorem

For all real \(k,p\),
\[
\operatorname{sgn}\Delta_{k,p}(A,B)=\operatorname{sgn}(kp)
\]
whenever \(kp\neq0\) and \(AB\ne BA\). If \(kp=0\) or \(AB=BA\), then \(\Delta_{k,p}(A,B)=0\).

Thus, in order two, the comparison is completely determined by the signs of the two exponents:
\[
kp>0 \Longrightarrow
\det(A^k+|AB|^p)\ge \det(A^k+|BA|^p),
\]
whereas
\[
kp<0 \Longrightarrow
\det(A^k+|AB|^p)\le \det(A^k+|BA|^p).
\]
The inequalities are strict exactly when \(kp\ne0\) and \(A,B\) do not commute.

For \(k,p>0\), the conclusion extends by continuity to positive-semidefinite \(A\) and arbitrary Hermitian \(B\). In particular, the nonnegative-exponent conjecture formulated in Ghabries's 2022 thesis holds for all \(2\times2\) matrices in the stated Hermitian setting. For \(k\ge0\), \(p\le0\), the invertible case gives the proposed reverse inequality in order two.

## Exact gap formula

By unitary conjugation write
\[
A=\begin{pmatrix}a&0\\0&b\end{pmatrix},
\qquad a,b>0,
\qquad
B=\begin{pmatrix}r&z\\\overline z&s\end{pmatrix},
\]
with \(r,s\in\mathbb R\). Put
\[
X=|AB|^2=BA^2B,\qquad
Y=|BA|^2=AB^2A.
\]
Because \(BA=(AB)^*\), the positive matrices \(X\) and \(Y\) have the same two eigenvalues
\(\lambda_1\ge\lambda_2>0\).

If \(\lambda_1\ne\lambda_2\), define
\[
\alpha_p=
\frac{\lambda_1^{p/2}-\lambda_2^{p/2}}{\lambda_1-\lambda_2}.
\]
Then
\[
\boxed{
\Delta_{k,p}(A,B)
=
\alpha_p |z|^2(b^2-a^2)(b^k-a^k).
}
\]
When \(\lambda_1=\lambda_2\), both \(X\) and \(Y\) are the same scalar matrix, so the gap is zero. The displayed formula may equivalently be continued to that case using the corresponding divided-derivative value.

Since \(\operatorname{sgn}\alpha_p=\operatorname{sgn}p\) for \(p\ne0\), while
\[
\operatorname{sgn}\bigl((b^2-a^2)(b^k-a^k)\bigr)=\operatorname{sgn}k
\]
when \(a\ne b\), the phase law follows.

## Proof

The two positive matrices \(X\) and \(Y\) have the same spectrum. In dimension two, functional calculus on a two-point spectrum is affine: for any real \(p\),
\[
X^{p/2}-Y^{p/2}=\alpha_p(X-Y)
\]
when the spectrum is nondegenerate; the degenerate case is immediate.

A direct multiplication gives
\[
(X-Y)_{11}=(b^2-a^2)|z|^2,\qquad
(X-Y)_{22}=(a^2-b^2)|z|^2.
\]
Moreover \(\det X^{p/2}=\det Y^{p/2}\). For any two \(2\times2\) matrices \(C,D\) with the same determinant and for
\(P=\operatorname{diag}(a^k,b^k)\),
\[
\det(P+C)-\det(P+D)
=
b^k(C_{11}-D_{11})+a^k(C_{22}-D_{22}).
\]
Taking \(C=X^{p/2}\), \(D=Y^{p/2}\) yields the exact gap formula.

If \(p\ne0\), the divided difference \(\alpha_p\) is nonzero. If also \(k\ne0\), the remaining factor vanishes exactly when \(a=b\) or \(z=0\), which is exactly the condition \(AB=BA\) in this diagonal representation. This proves the strictness statement.

For \(k,p>0\), singular \(A\) or \(B\) are obtained from positive-definite/invertible approximants; matrix positive powers and determinants are continuous in this regime.

## Relation to prior literature

Lin introduced determinant comparisons involving \(A^2+|AB|^p\) and \(A^2+|BA|^p\). Ghabries, Abbas and Mourad proved the \(k=2\), \(p\ge0\) comparison in the Hermitian setting. Ghabries's 2022 thesis then formulated the broader problem
\[
\det(A^k+|AB|^p)\ge\det(A^k+|BA|^p),\qquad k,p\ge0,
\]
and also a reverse inequality for nonpositive \(p\) under invertibility assumptions. The thesis records only partial parameter ranges for these broader formulations. A 2026 preprint by Ghabries extends the \(k=2\)-type determinant comparison from Hermitian to normal matrices, but its stated theorem does not replace \(A^2\) by arbitrary \(A^k\).

The result here is therefore claimed only **to the best of our knowledge** as a complete order-two phase law for arbitrary real exponents, simultaneously giving the order-two cases of the positive- and negative-\(p\) formulations.

## Limitations

The argument is genuinely two-dimensional: it uses that a function of a positive matrix with at most two spectral values is affine in that matrix, and it uses the degree-two determinant identity. No claim is made that the same sign law holds in dimensions \(n\ge3\), nor that this resolves the full conjectures.

The literature search covered the original Lin paper, the 2020 and 2021 determinant-inequality papers by Ghabries and collaborators, the 2022 thesis where the broader conjectures are stated, and the 2026 normal-matrix extension. Older or differently phrased low-dimensional matrix-inequality literature could still contain an equivalent \(2\times2\) observation.

## References

1. M. Lin, *On a determinantal inequality arising from diffusion tensor imaging*, Communications in Contemporary Mathematics 19 (2017), 1650044. DOI: 10.1142/S0219199716500449.
2. M. M. Ghabries, H. Abbas, B. Mourad, *On some open questions concerning determinantal inequalities*, Linear Algebra and its Applications 596 (2020), 169–183. DOI: 10.1016/j.laa.2020.03.009.
3. H. Abbas, M. M. Ghabries, B. Mourad, *New determinantal inequalities concerning Hermitian and positive semi-definite matrices*, Operators and Matrices 15 (2021), 105–116. DOI: 10.7153/oam-2021-15-07.
4. M. M. Ghabries, *Contributions to Matrix Inequalities and Some Applications*, doctoral thesis, Université d'Angers / Lebanese University, 2022, especially Chapter 2 and the open-problems summary. HAL: tel-03936351.
5. M. M. Ghabries, *A log-majorization inequality for normal matrices with applications to determinantal inequalities and geometric means*, arXiv:2607.21163 (2026).
