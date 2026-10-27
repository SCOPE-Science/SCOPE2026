# Exact Krylov rank of fractional-power corrections under a positive rank-one matrix update

## Finding
Let \(A\) be any real symmetric positive-definite matrix, \(u\ne0\), \(\tau>0\), and \(B=A+\tau uu^{\mathsf T}\). For every \(0<s<1\), define the positive- and negative-power corrections
\[
D_s^+=B^s-A^s,\qquad D_s^-=A^{-s}-B^{-s}.
\]
Both corrections are positive semidefinite and have **exactly** the same range and kernel:
\[
\operatorname{ran}D_s^+=\operatorname{ran}D_s^-=\mathcal K(A,u),\qquad
\ker D_s^+=\ker D_s^-=\mathcal K(A,u)^\perp,
\]
where \(\mathcal K(A,u)=\operatorname{span}\{u,Au,\ldots,A^{n-1}u\}\). Consequently their common exact algebraic rank is the number of distinct eigenvalues \(\lambda\) of \(A\) for which \(P_\lambda u\ne0\), with \(P_\lambda\) the orthogonal spectral projector. This classification is independent of \(s\in(0,1)\) and of spike strength \(\tau>0\).

In particular, when \(A\) has simple spectrum and \(u\) has nonzero projection along each eigenvector, both corrections are strictly positive definite, so a **rank-one perturbation generically creates full-rank fractional-power corrections**. The square-root and inverse-square-root cases follow at \(s=1/2\). If \(A=\alpha I\), both corrections instead have rank one. At the exponent endpoint \(s=1\), the positive-power correction is \(\tau uu^{\mathsf T}\), while the inverse-power correction has rank one by Sherman–Morrison; thus for two or more active eigenvalues the exact rank changes at this endpoint.

## Assumptions and scope
The dimension is any finite integer \(n\ge1\). The matrix \(A\) is **strictly** positive definite and real symmetric; \(u\) is real and nonzero; the update is positive with \(\tau>0\); and \(s\) is any real number strictly between zero and one. Powers are principal spectral powers. No spectral simplicity is required. No conclusion is asserted for nonnormal matrices, indefinite updates, or zero eigenvalues of the base matrix.

## Proof
For \(t>0\), write \(R_t=(A+tI)^{-1}\). The rank-one resolvent identity is
\[
(A+tI)^{-1}-(B+tI)^{-1}
=\frac{\tau R_tuu^{\mathsf T}R_t}{1+\tau u^{\mathsf T}R_tu}.
\]
The denominator is strictly positive. The elementary Stieltjes representations of scalar fractional powers, extended by spectral calculus, are
\[
X^s=\frac{\sin(\pi s)}\pi\int_0^\infty t^{s-1}X(X+tI)^{-1}\,dt,
\qquad
X^{-s}=\frac{\sin(\pi s)}\pi\int_0^\infty t^{-s}(X+tI)^{-1}\,dt.
\]
Using \(X(X+tI)^{-1}=I-t(X+tI)^{-1}\) and the resolvent identity gives **both** positive Gram-integral expressions
\[
D_s^+=\frac{\tau\sin(\pi s)}\pi\int_0^\infty
\frac{t^sR_tuu^{\mathsf T}R_t}{1+\tau u^{\mathsf T}R_tu}\,dt,
\]
\[
D_s^-=\frac{\tau\sin(\pi s)}\pi\int_0^\infty
\frac{t^{-s}R_tuu^{\mathsf T}R_t}{1+\tau u^{\mathsf T}R_tu}\,dt.
\]
The integrands are symmetric positive semidefinite and locally continuous. They are integrable at zero because \(A\succ0\), and at infinity because \(R_t=O(t^{-1})\), hence the weights produce \(O(t^{s-2})\) and \(O(t^{-s-2})\), respectively. Their scalar quadratic forms are nonnegative and vanish exactly when \(x^{\mathsf T}R_tu=0\) for every \(t>0\), as each scalar weight is strictly positive on \((0,\infty)\).

Write the spectral decomposition \(A=\sum_{\lambda\in\Lambda}\lambda P_\lambda\) over its **distinct** eigenvalues. Then
\[
x^{\mathsf T}R_tu=\sum_{\lambda\in\Lambda}
\frac{x^{\mathsf T}P_\lambda u}{t+\lambda}.
\]
The rational functions \((t+\lambda)^{-1}\) for distinct \(\lambda\) are linearly independent: multiply a vanishing sum by \(\prod_{\lambda\in\Lambda}(t+\lambda)\), then evaluate the resulting polynomial identity at each distinct negative pole \(-\lambda\). Therefore, the quadratic form vanishes precisely when \(x\perp P_\lambda u\) for every \(\lambda\). Since the matrices are positive semidefinite, zero quadratic form is equivalent to membership of the kernel.

Finally, by Lagrange interpolation on the finite distinct spectrum, the span of the vectors \(P_\lambda u\) equals \(\operatorname{span}\{u,Au,\ldots,A^{n-1}u\}\). The nonzero \(P_\lambda u\) are mutually orthogonal, so their count is the exact dimension of this span. Both correction kernels equal its orthogonal complement; for symmetric matrices, the corresponding ranges equal the span itself. This completes the classification.

For the integer boundary \(s=1\), \(B-A=\tau uu^{\mathsf T}\); also
\[
A^{-1}-B^{-1}=\frac{\tau A^{-1}uu^{\mathsf T}A^{-1}}
{1+\tau u^{\mathsf T}A^{-1}u},
\]
which has rank one. No claim of uniform nonzero singular-value lower bounds is made as \(s\) tends to an endpoint.

## Verification
A fully exact two-dimensional witness is
\[
A=\begin{pmatrix}1&0\\0&4\end{pmatrix},\quad
u=\begin{pmatrix}1\\1\end{pmatrix},\quad
B=\begin{pmatrix}2&1\\1&5\end{pmatrix}.
\]
Because \(\det B=9\) and \(\operatorname{tr}B=7\), its principal square root is \(B^{1/2}=(B+3I)/\sqrt{13}\). Thus
\[
D_{1/2}^+=
\begin{pmatrix}5/\sqrt{13}-1&1/\sqrt{13}\\1/\sqrt{13}&8/\sqrt{13}-2\end{pmatrix},
\quad
\operatorname{tr}D_{1/2}^+=\sqrt{13}-3>0,
\]
\[
\det D_{1/2}^+=5-\frac{18}{\sqrt{13}}>0,
\]
where the last strict inequality is equivalent to \(325>324\). Hence the rank-one spike creates a strictly positive-definite rank-two square-root correction; this symbolic example is independently checkable without floating-point arithmetic.

The standalone `check.py` reproduces that exact symbolic witness and reports 279 finite assertions in total on representative diagonal systems with repeated/inactive eigenvalues, on both fractional signs, and on direct resolvent-integral quadrature. Execute `python check.py` with `numpy`, `sympy`, and `scipy` installed. The finite experiments are checks of implementation and normalization only, **not** the proof of the arbitrary-dimensional theorem.

## Relationship to prior work
Shmueli, Drineas and Avron [1], first publicly posted on 2022-01-31, establish rapid eigenvalue decay and efficient **approximately low-rank** corrections for matrix square roots and inverse square roots. They explicitly note that exact corrections tend to be full rank; the present exact active-spectrum rank and common-kernel classification quantifies this distinction for positive rank-one updates and all fractional powers. Their low-rank numerical error bounds are neither contradicted nor re-proved here.

Beckermann, Kressner and Schweitzer [2] give polynomial Krylov approximations of general low-rank matrix-function updates. Beckermann, Cortinovis, Kressner and Schweitzer [3] give rational Krylov approximations, including square roots and inverse square roots, and bound approximation errors. These approaches supply relevant Krylov and integral ingredients but the inspected results do not state the sharp exact algebraic rank or simultaneous range/kernel identity. Bernstein and Van Loan's rational-function rank bounds, described in [2,3], do not directly classify noninteger fractional powers. The established scaled-identity special case [1, §1.1] corresponds to a single active eigenvalue in the present theorem.

## Limitations
Exact algebraic full rank does **not** imply slow numerical low-rank approximability; most singular values may be tiny, as existing decay results show. No universal condition-number, spectral-tail or error bound is established. The theorem concerns positive rank-one updates of finite-dimensional symmetric positive-definite matrices, not signed or indefinite perturbations. Although no equivalent exact-rank theorem was located in the inspected primary sources and indexed mathematical records, earlier operator-monotone/Loewner or control-Gramian literature may contain a stronger equivalent statement. Independent scientific audit has not been performed.

## References
[1] S. Shmueli, P. Drineas and H. Avron, *Low-Rank Updates of Matrix Square Roots*, arXiv:2201.13156 (first posted 2022-01-31), https://arxiv.org/abs/2201.13156 ; *Numerical Linear Algebra with Applications* (2024), DOI:10.1002/nla.2528.

[2] B. Beckermann, D. Kressner and M. Schweitzer, *Low-rank updates of matrix functions*, arXiv:1707.03045 (2017), https://arxiv.org/abs/1707.03045 ; DOI:10.1137/17M1140108.

[3] B. Beckermann, A. Cortinovis, D. Kressner and M. Schweitzer, *Low-rank updates of matrix functions II: Rational Krylov methods*, arXiv:2008.11501 (2020), https://arxiv.org/abs/2008.11501 ; DOI:10.1137/20M1362553.
