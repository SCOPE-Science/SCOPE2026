# One is the sharp spectral-width positivity frontier for two-step Lanczos exponential propagation

## Finding
Let
\[
A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),
\qquad
0<\mu\le\lambda_i\le L,
\]
and let \(b\ge0\) be nonzero. Consider the standard exact-arithmetic two-step Lanczos approximation
\[
y_2(t)
=
\|b\|_2V_2e^{-tT_2}e_1,
\qquad
T_2=V_2^{\mathsf T}AV_2,
\]
to
\[
e^{-tA}b.
\]

Then
\[
\boxed{
y_2(t)\ge0
\text{ for every admissible }A,b,n
\quad\Longleftrightarrow\quad
t(L-\mu)\le1.
}
\]

The exact exponential is strictly positive on every positive component of \(b\), so the threshold concerns a genuine sign defect of the Krylov approximation rather than of the underlying evolution.

Moreover, dimension three is minimal for failure. If \(n\le2\), or more generally if \(b\) has support on at most two distinct eigenvalues, the two-step Lanczos approximation is exact. If
\[
t(L-\mu)>1,
\]
then a three-dimensional diagonal SPD example with a strictly positive starting vector has a negative Lanczos component.

For example,
\[
A=\operatorname{diag}\!\left(1,\frac65,3\right),
\qquad
b=\left(1,1,\frac1{100}\right)^{\mathsf T},
\qquad
t=1
\]
has
\[
t(L-\mu)=2.
\]
Two Lanczos steps give
\[
y_2(t)
\approx
(0.36733725,\ 0.30175770,\ -0.00288458)^{\mathsf T},
\]
whereas
\[
e^{-tA}b
=
\left(e^{-1},e^{-6/5},\frac{e^{-3}}{100}\right)^{\mathsf T}
\]
is strictly positive.

## Assumptions and scope
The matrix is real diagonal SPD and the starting vector is componentwise nonnegative. The approximation is the standard polynomial Lanczos projection in exact arithmetic,
\[
\|b\|_2V_2e^{-tT_2}e_1.
\]

The theorem is a universal statement over all finite dimensions and all diagonal spectra contained in the fixed interval \([\mu,L]\). The quantity
\[
t(L-\mu)
\]
is invariant under adding a scalar multiple of the identity after factoring out the corresponding positive exponential factor.

The result concerns two Lanczos steps only. It does not classify higher Krylov dimensions, nonsymmetric Arnoldi approximations, rational Krylov methods, restarted variants, finite-precision loss of orthogonality, or non-diagonal matrices whose exact exponential may have a different sign structure.

## Proof
If the Lanczos process breaks down before producing two basis vectors, then \(b\) lies in a one-dimensional invariant subspace and the approximation is exact. Assume no breakdown.

Because
\[
\mathcal K_2(A,b)=\operatorname{span}\{b,Ab\},
\]
there is a unique linear polynomial
\[
p(\lambda)=c_0+c_1\lambda
\]
such that
\[
y_2(t)=p(A)b.
\]
Let
\[
\theta_1<\theta_2
\]
be the two eigenvalues of the symmetric projected matrix \(T_2\). Functional calculus on \(T_2\) shows that \(p\) is precisely the linear interpolant of
\[
f(\lambda)=e^{-t\lambda}
\]
at the Ritz values:
\[
p(\theta_j)=e^{-t\theta_j},
\qquad j=1,2.
\]
Since \(T_2\) is a compression of \(A\),
\[
\mu\le\theta_1<\theta_2\le L.
\]

The interpolation slope is negative. Hence \(p(\lambda)>0\) for every \(\lambda\le\theta_2\). For \(\lambda\ge\theta_2\), the mean-value theorem gives a point
\[
\xi\in(\theta_1,\theta_2)
\]
such that
\[
\frac{e^{-t\theta_2}-e^{-t\theta_1}}
{\theta_2-\theta_1}
=
-t e^{-t\xi}.
\]
Therefore
\[
p(\lambda)
=
e^{-t\theta_1}
-t e^{-t\xi}(\lambda-\theta_1).
\]
Because
\[
e^{-t\xi}\le e^{-t\theta_1},
\]
one obtains
\[
p(\lambda)
\ge
e^{-t\theta_1}
\left[
1-t(\lambda-\theta_1)
\right].
\]
If
\[
t(L-\mu)\le1,
\]
then for every \(\lambda\in[\mu,L]\),
\[
t(\lambda-\theta_1)
\le
t(L-\mu)
\le1,
\]
and hence
\[
p(\lambda)\ge0.
\]
Since \(b\ge0\), this proves
\[
p(A)b\ge0.
\]

To prove sharpness, suppose
\[
\tau=t(L-\mu)>1.
\]
Choose
\[
0<r<1
\]
and define
\[
A_r
=
\operatorname{diag}
\left(
\mu,\,
\mu+r(L-\mu),\,
L
\right).
\]
For
\[
b_0=(1,1,0)^{\mathsf T},
\]
the active spectrum has exactly two points, so the two Ritz values are
\[
\mu
\quad\text{and}\quad
\mu+r(L-\mu).
\]
The corresponding interpolation line, evaluated at \(L\), is
\[
p_0(L)
=
e^{-t\mu}
\left[
1-\frac{1-e^{-\tau r}}{r}
\right].
\]
As
\[
r\downarrow0,
\]
the bracket converges to
\[
1-\tau<0.
\]
Thus \(p_0(L)<0\) for every sufficiently small positive \(r\).

Now perturb the starting vector to
\[
b_\varepsilon=(1,1,\varepsilon)^{\mathsf T}.
\]
At \(\varepsilon=0\), the two-step Lanczos process on the first two active modes has no first-step breakdown because the two eigenvalues are distinct. Its recurrence coefficients, the two eigenvalues of \(T_2\), and therefore the linear interpolation polynomial depend continuously on \(\varepsilon\). Hence
\[
p_\varepsilon(L)<0
\]
for all sufficiently small \(\varepsilon>0\). The third component is then
\[
\varepsilon p_\varepsilon(L)<0.
\]
This proves failure whenever
\[
t(L-\mu)>1.
\]

Finally, if the ambient dimension is at most two, the degree of the minimal polynomial of \(b\) with respect to \(A\) is at most two. Two Lanczos steps are therefore exact. Hence dimension three is minimal for sign loss.

## Verification
The embedded `verify.py` independently reconstructs the standard two-step Lanczos recurrence for the explicit witness
\[
A=\operatorname{diag}\!\left(1,\frac65,3\right),
\qquad
b=\left(1,1,\frac1{100}\right)^{\mathsf T},
\qquad
t=1.
\]
It evaluates the exponential of the resulting symmetric \(2\times2\) projected matrix using the closed hyperbolic-function formula and high-precision decimal arithmetic.

The checker verifies that the third component is below
\[
-0.0028
\]
while the exact third component is positive. It also checks the limiting sharpness function
\[
1-\frac{1-e^{-\tau r}}{r}
\]
for \(\tau=2\) and a small positive \(r\).

The universal threshold is proved analytically above; finite computations are not used as an exhaustive argument.

## Relationship to prior work
Gallopoulos and Saad developed Krylov approximation of parabolic evolution operators by projecting the matrix exponential to a low-dimensional Arnoldi or Lanczos space. Their 1990 report states the central approximation
\[
e^{-tA}v
\approx
\|v\|_2V_me^{-tH_m}e_1
\]
and notes exactness once the Krylov dimension reaches the degree of the relevant minimal polynomial. The report is explicitly motivated by parabolic equations and carries primary subject classifications including 65M20 and 65F10.

Saad's 1992 analysis develops the polynomial-approximation viewpoint further and identifies Krylov matrix-exponential approximations with interpolation of the exponential on associated Ritz values. Later Lanczos analyses focus on convergence and error bounds for
\[
e^{-tA}v
\]
on positive semidefinite matrices.

The present statement concerns a different property: componentwise positivity of the projected approximation. Targeted searches using Lanczos, Arnoldi, matrix exponential, positivity preserving, nonnegative, diagonal SPD, two-step, Ritz interpolation, and parabolic evolution terminology did not locate the sharp threshold
\[
t(L-\mu)=1
\]
or the minimal-dimension-three sign-loss mechanism.

A retrieved result on positivity-preserving Krylov methods for differential Riccati equations concerns preservation of matrix positive semidefiniteness under a different projected nonlinear flow. It does not imply componentwise positivity of a polynomial Lanczos approximation to an exponential action.

## Limitations
The matrix in the theorem is diagonal. This is intentional: the exact solution is then visibly componentwise positive, and any negative component is attributable to the Krylov polynomial itself. The result does not claim a general positivity criterion for Stieltjes matrices or Metzler generators.

The result is exact-arithmetic. Finite-precision Lanczos may lose orthogonality and can exhibit additional behavior.

Only the two-step approximation is classified. Higher Krylov dimensions use higher-degree interpolation polynomials and require different sign arguments.

The originality search cannot exclude differently phrased older results in polynomial approximation or parabolic time-stepping literature. The closest inspected sources concentrate on error, stability, and convergence rather than componentwise cone invariance.

## References
1. E. Gallopoulos and Y. Saad, “Efficient Solution of Parabolic Equations by Krylov Approximation Methods,” RIACS Technical Report 90.14, NASA Ames Research Center, March 1990; later SIAM Journal on Scientific and Statistical Computing 13 (1992), 1236–1264.
2. Y. Saad, “Analysis of Some Krylov Subspace Approximations to the Matrix Exponential Operator,” SIAM Journal on Numerical Analysis 29 (1992), 209–228. DOI 10.1137/0729014.
3. J. van den Eshof and M. Hochbruck, “Preconditioning Lanczos Approximations to the Matrix Exponential,” SIAM Journal on Scientific Computing 27 (2006), 1438–1457. DOI 10.1137/040605461.
4. Q. Ye, “Error Bounds for the Lanczos Methods for Approximating Matrix Exponentials,” SIAM Journal on Numerical Analysis 51 (2013), 68–87. DOI 10.1137/11085935X.
