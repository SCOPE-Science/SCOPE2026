# Hahn–Exton zeros determine every singular value of a geometric Rhaly operator

## Finding

Fix \(0<t<1\). On the classical Hardy space \(H^2(\mathbb D)\), with the monomials \(1,z,z^2,\ldots\) orthonormal, define the point-mass Rhaly operator
\[
(W_t f)(z)=\frac{f(tz)}{1-tz},\qquad
f(z)=\sum_{j=0}^{\infty}a_jz^j.
\]
The following entire-function identity holds for every \(\zeta\in\mathbb C\):
\[
\boxed{\det(I-\zeta W_tW_t^*)=
 \sum_{k=0}^{\infty}\frac{(-\zeta)^k t^{k(k-1)}}{\prod_{j=1}^k(1-t^{2j})^2}
 =J_0^{(3)}\!\left(\frac{2\sqrt{\zeta}}t;t^2\right).}
\]
Here the final notation denotes the **order-zero Hahn–Exton (third Jackson) basic Bessel function** in the explicitly normalized series
\[
J_0^{(3)}(x;Q)=\sum_{k=0}^{\infty}
\frac{(-1)^k Q^{k(k+1)/2}(x^2/4)^k}{(Q;Q)_k^2},
\qquad (Q;Q)_k=\prod_{j=1}^k(1-Q^j),\quad (Q;Q)_0=1.
\]
Its argument is interpreted by the even entire series, so no choice of a square-root branch is required. All zeros of the displayed Fredholm determinant are **strictly positive, simple, and infinite in number**. If they are arranged as \(0<\zeta_1(t)<\zeta_2(t)<\cdots\), the complete list of singular values of \(W_t\), including multiplicities, is
\[
\boxed{s_j(W_t)=\zeta_j(t)^{-1/2}\quad(j=1,2,\ldots),
\qquad \|W_t\|=\zeta_1(t)^{-1/2}.}
\]
In particular, this computes every best finite-rank Hilbert-space approximation error, since the optimal error of rank less than \(j\) is \(s_j(W_t)\). One exact spectral sum rule is
\[
\sum_{j=1}^{\infty}s_j(W_t)^2=\frac1{(1-t^2)^2}.
\]

## Assumptions and scope

The parameter \(t\) is real and satisfies \(0<t<1\); the conclusion concerns the **singular values**, not the ordinary eigenvalues, of \(W_t\) on the coefficient-normalized Hardy space \(H^2\). On Taylor coefficients,
\[
(W_ta)_n=t^n\sum_{j=0}^{n}a_j,\qquad n\ge0,
\]
with all indices starting at zero. Thus \(W_t\) is precisely the Rhaly matrix with geometric weights \(\eta_n=t^n\). The parameter endpoint \(t=0\) yields a rank-one limiting operator, whereas \(t=1\) does not define a bounded Rhaly operator on \(H^2\); neither endpoint is included. The determinant is the Fredholm determinant of the positive trace-class operator \(W_tW_t^*\).

## Proof

**1. Trace class and kernel.** Under the coefficient identification \(H^2\cong\ell^2(\mathbb N_0)\), the matrix of \(W_t\) has entries \(t^n\) when \(j\le n\), and zero otherwise. It factors as \(W_t=A_tB_t\), where \(A_t\) is diagonal with entries \(t^{n/2}\) and \(B_t\) has entry \(t^{n/2}\) for \(j\le n\). Both are Hilbert–Schmidt, because
\[
\|A_t\|_{\mathrm{HS}}^2=\sum_{n\ge0}t^n<\infty,
\qquad \|B_t\|_{\mathrm{HS}}^2=\sum_{n\ge0}(n+1)t^n<\infty.
\]
Consequently \(W_t\) is trace class, and its Gram operator \(K_t=W_tW_t^*\) is positive trace class, with explicitly computed kernel
\[
(K_t)_{nm}=t^{n+m}\bigl(\min\{n,m\}+1\bigr),\qquad n,m\ge0.
\]
In particular, \(\operatorname{tr}(K_t)=\sum_{n\ge0}(n+1)t^{2n}=(1-t^2)^{-2}\).

**2. Every principal minor.** Choose arbitrary indices \(0\le n_1<\cdots<n_k\). Define the positive integer gaps \(d_1=n_1+1\) and \(d_i=n_i-n_{i-1}\) for \(2\le i\le k\). The matrix with entries \(\min(n_i,n_j)+1\) factors as the unit lower-triangular all-ones matrix times \(\operatorname{diag}(d_1,\ldots,d_k)\) times its transpose. Therefore its determinant is exactly \(\prod_{i=1}^kd_i\). Restoring the two diagonal geometric factors gives
\[
\det\big[(K_t)_{n_i n_j}\big]_{i,j=1}^k
=t^{2\sum_{i=1}^k n_i}\prod_{i=1}^k d_i.
\]
The parametrization by positive gaps is a bijection between strictly increasing index tuples and \(d_i\ge1\). Since \(n_i=d_1+\cdots+d_i-1\),
\[
\sum_{i=1}^k n_i=\sum_{i=1}^k(k-i+1)d_i-k.
\]
Summing the nonnegative principal minors of order \(k\), and using the elementary absolutely convergent identity \(\sum_{d=1}^{\infty}d r^d=r/(1-r)^2\) for \(0<r<1\), yields
\[
\begin{aligned}
e_k(K_t)
&=t^{-2k}\prod_{j=1}^k \left(\sum_{d=1}^{\infty}d\,t^{2jd}\right)\\
&=t^{-2k}\prod_{j=1}^k\frac{t^{2j}}{(1-t^{2j})^2}
=\frac{t^{k(k-1)}}{\prod_{j=1}^k(1-t^{2j})^2}.
\end{aligned}
\]
The coefficient identity is valid for every integer \(k\ge1\); \(e_0=1\). Since \(K_t\) is trace class, its finite principal sections converge in trace norm, and the Fredholm determinant is the entire generating series \(\det(I-\zeta K_t)=\sum_{k\ge0}(-\zeta)^k e_k(K_t)\). This is the first boxed formula. Substitution \(Q=t^2\), \(x=2\sqrt\zeta/t\) into the stated Hahn–Exton definition proves the special-function identity without relying on a normalization convention external to the statement.

**3. Positive and simple spectrum.** The adjoint acts by \((W_t^*y)_j=\sum_{n\ge j}t^n y_n\). If \(W_t^*y=0\), subtract its values at \(j\) and \(j+1\) to obtain \(t^j y_j=0\). Thus \(W_t^*\) is injective and \(K_t\) has trivial kernel. Its positive compact spectral decomposition therefore has infinitely many strictly positive eigenvalues tending to zero.

To establish multiplicity one without invoking special-function zero theorems, suppose \(K_t x=\lambda x\) for \(\lambda>0\) and \(x\ne0\). Set
\[
u_n=t^nx_n,\quad v_n=\sum_{m\ge0}(\min\{n,m\}+1)u_m,\quad v_{-1}=0.
\]
The sums converge absolutely by Cauchy–Schwarz and geometric decay. The eigenvalue equation gives \(u_n=t^{2n}v_n/\lambda\). Taking successive discrete differences of \(v_n\) gives
\[
v_{n+1}-2v_n+v_{n-1}=-u_n,
\qquad v_{n+1}=\left(2-\frac{t^{2n}}\lambda\right)v_n-v_{n-1}\quad(n\ge0).
\]
The recurrence and \(v_{-1}=0\) determine \(v_n\), and hence \(x_n\), uniquely up to the single initial scalar \(v_0\); a zero initial scalar produces the zero vector. Every positive eigenspace is consequently one-dimensional. Self-adjointness rules out generalized eigenspaces, proving simple positive eigenvalues. The Fredholm product \(\prod_{j\ge1}(1-\zeta\lambda_j)\) then shows that its zeros are exactly the positive, simple numbers \(\zeta_j=\lambda_j^{-1}\), and \(s_j(W_t)=\sqrt{\lambda_j}\).

## Verification

The standalone file `check_spectral_coefficients.py` uses only Python's standard library and exact rational arithmetic. It checks, for rational \(t=1/2\) and \(t=2/3\), that numerous independently evaluated small principal Gram determinants agree with the positive-gap formula, and that their finite-section elementary symmetric sums are below the infinite closed forms. It is a finite consistency check, **not** an infinite proof or certified numerical root table. The infinite statement is proved by the analytic trace-class and principal-minor arguments above.

To reproduce the finite check, run `python check_spectral_coefficients.py` in the directory containing that file. This executes without network access or third-party packages. The coefficient identity can also be independently reproduced symbolically by summing the geometric first moment \(\sum_{d\ge1}d r^d=r/(1-r)^2\) for the \(k\) independent gaps.

## Relationship to prior work

Galanopoulos and Girela (arXiv:2511.09201; first submitted 2025-11-12, primary MSC 30H10) study boundedness and compactness of general Rhaly operators on spaces of analytic functions; they do not evaluate singular spectra. Gallardo-Gutiérrez and Partington (arXiv:2408.03182; published 2025) expressly identify this same point-mass weighted composition map and give its **ordinary spectrum** \(\{0\}\cup\{t^n:n\ge0\}\). These eigenvalues do not determine the singular values because the operator is nonnormal. Bellavita, Dellepiane and Stylogiannis (arXiv:2503.21930, 2025) characterize membership in the Schatten ideals for Rhaly matrices, but their results do not furnish the complete singular-value sequence of this geometric family. Their 2026 work on weighted Hardy spaces and factorable matrices addresses weighted boundedness and Schatten criteria; a complete direct comparison with all portions of its manuscript remains a source-access risk. Classical Hahn–Exton literature studies the basic-Bessel function's zeros in other contexts, not the point-mass Rhaly singular-value identification. In contrast, the theorem here identifies the exact Fredholm characteristic function and hence every optimal finite-rank approximation number of the named operator.

## Limitations

The result is exact but implicit: a generic Hahn–Exton zero is not claimed to have an elementary expression, and no uniform numerical zero-isolation or precise large-index zero asymptotic is supplied. It treats geometric weights \(\eta_n=t^n\) on standard \(H^2\), not arbitrary moment sequences, arbitrary weighted Hardy norms, or \(H^p\) with \(p\ne2\). The cited singular-value relationship may conceivably have an unindexed equivalent formulation in the older literature on Jacobi matrices or basic Bessel functions. The identity establishes mathematical correctness independently of numerical checks; independent external validation has not been performed.

## References

1. P. Galanopoulos and D. Girela, *Rhaly operators acting on Hardy, Bergman, and Dirichlet spaces*, arXiv:2511.09201 (version 1, 2025-11-12); DOI: 10.1007/s12220-026-02361-9. https://arxiv.org/abs/2511.09201
2. E. A. Gallardo-Gutiérrez and J. R. Partington, *Rhaly operators: more on generalized Cesàro operators*, arXiv:2408.03182; DOI: 10.1007/s10231-025-01560-5. https://link.springer.com/article/10.1007/s10231-025-01560-5
3. C. Bellavita, E. Dellepiane and G. Stylogiannis, *Schatten class for Rhaly matrices and spaces of analytic functions*, arXiv:2503.21930 (2025), subsequently *Boundedness, compactness and Schatten class for Rhaly matrices*, DOI: 10.1112/jlms.70304. https://arxiv.org/abs/2503.21930
4. C. Bellavita, E. Dellepiane and G. Stylogiannis, *Rhaly operators on weighted Hardy spaces and factorable matrices*, arXiv:2606.15875 (2026). https://arxiv.org/abs/2606.15875
5. J. L. Cardoso, *On basic Fourier–Bessel expansions*, SIGMA 14 (2018), 035, DOI: 10.3842/SIGMA.2018.035. https://sigma-journal.com/2018/035/
