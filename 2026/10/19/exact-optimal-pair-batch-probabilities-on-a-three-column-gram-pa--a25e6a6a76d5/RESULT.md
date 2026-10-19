# Exact optimal pair-batch probabilities on a three-column Gram path

## Finding

**Theorem (a complete, scale-invariant three-column design).** Let \(A\in\mathbb R^{m\times3}\), \(m\ge3\), have full column rank and columns \(a_1,a_2,a_3\). Assume \(a_1^{\mathsf T}a_3=0\), and define the *magnitudes* of adjacent normalized correlations by
\[
u=\frac{|a_1^{\mathsf T}a_2|}{\|a_1\|_2\|a_2\|_2},\qquad
v=\frac{|a_2^{\mathsf T}a_3|}{\|a_2\|_2\|a_3\|_2}.
\]
Assume \(u>0\), \(v>0\), and \(u^2+v^2<1\). For any \(b\in\mathbb R^m\), write \(x_*\) for the unique least-squares minimizer of \(\|Ax-b\|_2^2\). At each iteration choose independently a two-element coordinate set \(B\in\{\{2,3\},\{1,3\},\{1,2\}\}\) with probabilities \(p_1,p_2,p_3\), respectively, and minimize the least-squares objective exactly over those coordinates.

Set \(\Delta=1-u^2-v^2\), \(a=\sqrt{1-v^2}\), \(c=\sqrt{1-u^2}\), and
\[
Z=3-u^2-v^2-2ua-2vc.
\]
Among **all fixed probability distributions on the three unordered two-coordinate batches**, the unique one minimizing the worst-case conditional *one-step expected squared prediction error ratio* is
\[
\boxed{
(p_1^*,p_2^*,p_3^*)
=\frac1Z\bigl(a(a-u),\ 1-ua-vc,\ c(c-v)\bigr).
}
\]
All three probabilities are strictly positive. Its exact, attained optimal contraction factor is
\[
\boxed{
\min_{\substack{p_i\ge0\\\sum_i p_i=1}}
\sup_{x\ne x_*}
\frac{\mathbb E_p\|A(x^+-x_*)\|_2^2}{\|A(x-x_*)\|_2^2}
=\frac{\Delta}{Z}.
}
\]
The expectation is over the next independently drawn batch, conditional on the current iterate. The assertion also applies to inconsistent least-squares problems because the objective excess equals the squared prediction error. If the law is used independently at every step, it follows that
\[
\mathbb E\|A(x^{(k)}-x_*)\|_2^2
\le\left(\frac{\Delta}{Z}\right)^k
\|A(x^{(0)}-x_*)\|_2^2.
\]
This last inequality need not be an equality for \(k>1\); the proved minimax exactness is **one-step**.

For example, \(u=v=3/5\) gives
\[
(p_1^*,p_2^*,p_3^*)=(4/9,1/9,4/9),\qquad
\lambda_* = 7/9.
\]
Uniform pair sampling instead has worst-case expected one-step factor
\[
\lambda_{\rm unif}=\frac{41+3\sqrt{137}}{96}>\frac79.
\]
The two central-containing pairs receive more probability than the nonadjacent pair; this difference is dictated by the Gram coupling rather than column lengths.

## Assumptions and scope

The two-coordinate update is exact block minimization, i.e.
\[
x^+=x+E_B(A_B^{\mathsf T}A_B)^{-1}A_B^{\mathsf T}(b-Ax),
\]
where \(A_B=AE_B\) and \(E_B\) selects the coordinates in \(B\). There is no damping, stale state, changing or iterate-adaptive sampling, approximate block solve, or restriction on the right-hand side. The columns need not have equal norms; positive rescaling and sign reversals leave each block column space unchanged. After these transformations, the normalized Gram matrix is
\[
G=\begin{pmatrix}1&u&0\\u&1&v\\0&v&1\end{pmatrix},
\]
which is positive definite precisely under the stated inequalities. Endpoints with a zero adjacent correlation are excluded from the uniqueness statement.

## Proof

**1. Complement normals and the sharp one-step objective.** Normalize and sign-adjust the three columns, which does not change any two-column span. Let \(\widehat A\) denote the normalized matrix. For each \(i\in\{1,2,3\}\), let \(V_i\) be the unit vector in \(\operatorname{col}(\widehat A)\) perpendicular to the two columns with indices other than \(i\), with sign selected by the formula
\[
V_i=\frac{\widehat A G^{-1}e_i}{d_i},\qquad
 d_i=\sqrt{(G^{-1})_{ii}}.
\]
Writing \(V=[V_1,V_2,V_3]\), the three normals form a basis of \(\operatorname{col}(A)\) and have Gram matrix
\[
H=V^{\mathsf T}V=D^{-1}G^{-1}D^{-1},\qquad
K=H^{-1}=DGD,
\]
with \(D=\operatorname{diag}(d_1,d_2,d_3)\). For the batch missing coordinate \(i\), its orthogonal residual projector on \(\operatorname{col}(A)\) is \(V_iV_i^{\mathsf T}\). Consequently, for \(y=A(x-x_*)\in\operatorname{col}(A)\),
\[
\mathbb E_p\|A(x^+-x_*)\|_2^2=y^{\mathsf T}C(p)y,
\qquad C(p)=\sum_{i=1}^3p_iV_iV_i^{\mathsf T}.
\]
Thus the worst-case ratio is \(\lambda_{\max}(C(p)|_{\operatorname{col}(A)})\), and the supremum is attained by a nonzero eigenvector.

**2. A distribution-independent dual witness.** Put \(s=(1,-1,1)^{\mathsf T}\), \(\tau=s^{\mathsf T}Ks\), and
\[
 w=\frac{VKs}{\sqrt\tau}.
\]
Since \(V^{\mathsf T}w=s/\sqrt\tau\) and \(\|w\|_2=1\), every admissible distribution satisfies
\[
\lambda_{\max}(C(p))\ge w^{\mathsf T}C(p)w
=\sum_{i=1}^3p_i\frac{s_i^2}{\tau}=\frac1\tau.
\]
A direct inversion of \(G\) yields
\[
(d_1,d_2,d_3)=\frac1{\sqrt\Delta}(a,1,c),\quad
s_i(Ks)_i=\frac1\Delta\bigl(a(a-u),\ 1-ua-vc,\ c(c-v)\bigr)_i.
\]
Therefore \(\tau=Z/\Delta\). Positivity is strict: \(a>u\) and \(c>v\) follow from \(\Delta>0\), while Cauchy–Schwarz gives
\[
ua+vc\le\sqrt{(u^2+v^2)(2-u^2-v^2)}<1.
\]
Hence \(p_i^*=s_i(Ks)_i/\tau\) is a probability vector, and the lower bound is \(1/\tau=\Delta/Z\).

**3. Attainment and uniqueness.** Since \(VKV^{\mathsf T}\) is the orthogonal projector onto \(\operatorname{col}(A)\), the difference between the candidate bound and its mean residual operator is
\[
\frac1\tau P_{\operatorname{col}(A)}-C(p^*)
=\frac1\tau V\Bigl[K-\operatorname{diag}\bigl(s_i(Ks)_i\bigr)\Bigr]V^{\mathsf T}.
\]
Let \(h_{12}=ud_1d_2>0\) and \(h_{23}=vd_2d_3>0\). The bracket is exactly
\[
h_{12}(e_1+e_2)(e_1+e_2)^{\mathsf T}
+h_{23}(e_2+e_3)(e_2+e_3)^{\mathsf T}\succeq0.
\]
It follows that \(\lambda_{\max}(C(p^*))\le1/\tau\), proving equality with the witness bound. Moreover the bracket has rank two, so \(w\) is the unique top eigendirection on \(\operatorname{col}(A)\). If another probability vector \(p\) attained the same optimal factor, equality in its Rayleigh quotient at \(w\) would force \(C(p)w=\tau^{-1}w\). Since \(V\) has independent columns, this implies \(p_is_i=\tau^{-1}(Ks)_i\), and hence \(p=p^*\). This proves uniqueness, including among asymmetric probability laws.

**4. Uniform comparison and repeated steps.** When \(u=v=3/5\), the normal Gram is
\[
H=\begin{pmatrix}1&-3/4&9/16\\-3/4&1&-3/4\\9/16&-3/4&1\end{pmatrix}.
\]
For the optimal law the residual operator has eigenvalues \(7/9,7/36,1/36\). For uniform sampling its largest eigenvalue equals \((41+3\sqrt{137})/96\). Conditional one-step contraction iterated and averaged proves the stated \(k\)-step upper bound, without asserting an exact multi-step rate.

## Verification

The standalone `verify.py` recomputes the rational benchmark symbolically, constructs independent-column least-squares block projectors directly, and checks the optimal law against independently sampled distributions over the **entire** probability simplex for 350 random positive-definite Gram paths. It also scans a simplex grid at the rational benchmark. The program passed 43,801 numerical checks plus the exact eigenvalue identity; see `VERIFICATION.md`. The proof above, not the finite checks, establishes the theorem for all admissible real parameters.

## Relationship to prior work

Xie and Yang (2026, arXiv:2610.04685v1, publicly posted 2026-10-03) formulate coordinate-level joint batch distributions for randomized block coordinate descent and derive convergence bounds, motivating the search for distributions adapted to correlated columns. Gower and Richtárik (2015) develop the general sketch-and-project viewpoint and spectral convergence estimates. Kovalev, Gorbunov, Gasanov, and Richtárik (2018) discuss optimized probabilities and limitations of conventional coordinate sampling. Rodomanov and Kropotov (2019/2020) study volume-based coordinate-subset sampling. These broad formulations contain the operators and optimization criteria needed to *pose* this problem; the claim here is the explicitly solved, asymmetric, three-column path design with a sharp scalar value, strict positivity and uniqueness, not a new generic spectral principle. The complete motivating preprint and some older full texts were not retrievable at review time, so undetected stronger coverage remains a bibliographic risk.

## Limitations

Only the two-coordinate fixed-distribution, one-step minimax squared prediction-error criterion is optimized. No optimality for long-run asymptotic exponents, expected iteration counts, or unequal computational costs is claimed. The proof assumes exact least-squares block minimization, full column rank, one zero nonadjacent Gram correlation, nonzero adjacent correlations, and positive definiteness. Allowing more coordinates per batch, adaptive selection, approximate solvers or floating-point effects is outside scope. Full-document comparison with every plausible source was not possible; novelty is assessed against accessible research and recorded overlap searches, not certified by unsuccessful queries.

## References

1. Dong-Yue Xie and Xi Yang, *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems*, arXiv:2610.04685v1, first posted 2026-10-03. https://arxiv.org/abs/2610.04685
2. Robert M. Gower and Peter Richtárik, *Randomized Iterative Methods for Linear Systems*, SIAM Journal on Matrix Analysis and Applications 36 (2015), 1660–1690, DOI:10.1137/15M1025487. https://doi.org/10.1137/15M1025487
3. Dmitry Kovalev, Eduard Gorbunov, Elnur Gasanov, and Peter Richtárik, *Stochastic Spectral and Conjugate Descent Methods*, arXiv:1802.03703 (2018). https://arxiv.org/abs/1802.03703
4. Anton Rodomanov and Dmitry Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, arXiv:1904.04587 (2019), SIAM Journal on Optimization (2020). https://arxiv.org/abs/1904.04587
