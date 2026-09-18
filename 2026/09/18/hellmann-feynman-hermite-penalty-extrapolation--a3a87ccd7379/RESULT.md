# Hellmann–Feynman Hermite extrapolation for projected-Hessian penalty paths

## Result

Let \(H\in\mathbb S^n\), let \(A\in\mathbb R^{m\times n}\) have full row rank with \(m<n\), and let \(Z\) have orthonormal columns spanning \(\mathcal N(A)\). Define
\[
\lambda_*:=\lambda_{\min}(Z^THZ),\qquad
f(\rho):=\lambda_{\min}(H+\rho A^TA).
\]
Wang and Xia (2026) proved \(f(\rho)\uparrow\lambda_*\), characterized finite exact recovery, and in the nonattainable case obtained
\[
f(\rho)=\lambda_*-\frac{c}{\rho}+O(\rho^{-2})
\]
with an explicit \(c>0\). They also noted the value-only extrapolation
\[
2f(2\rho)-f(\rho)=\lambda_*+O(\rho^{-2}).
\]

Assume here that \(\lambda_*\) is simple. Then the large-penalty branch is in fact real analytic in \(t=1/\rho\) near \(t=0\). Consequently
\[
f(\rho)=\lambda_*+\sum_{j\ge1} a_j\rho^{-j}
\]
for all sufficiently large \(\rho\), with a convergent local power series. The first two coefficients are explicit. Choose an orthogonal matrix \(Q=[U,Z]\), where the columns of \(U\) span \(\mathcal R(A^T)\), and set
\[
B=U^THU,\quad E=U^THZ,\quad D=Z^THZ,\quad C=U^TA^TAU\succ0.
\]
Let \(v\) be the unit eigenvector of \(D\) for \(\lambda_*\), and let
\[
S=(D-\lambda_*I)^\dagger,\qquad
G=E^TC^{-1}E,
\]
\[
J=E^TC^{-1}(B-\lambda_*I)C^{-1}E.
\]
Then
\[
\boxed{
 f(\rho)=\lambda_* - \frac{c}{\rho}+\frac{b}{\rho^2}+O(\rho^{-3})
}
\]
with
\[
\boxed{c=v^TGv},\qquad
\boxed{b=v^T(J-GSG)v}.
\]
The formula for \(c\) agrees with the leading coefficient of Wang and Xia.

The analyticity also turns the Hellmann–Feynman derivative into a higher-order extrapolation primitive. For sufficiently large \(\rho\), the minimum eigenvalue is simple; for its normalized eigenvector \(x_\rho\),
\[
f'(\rho)=x_\rho^TA^TAx_\rho=\|Ax_\rho\|^2.
\]
For any fixed \(q>1\), values and derivatives at only two penalty levels give
\[
\boxed{
\begin{aligned}
\mathcal H_q(\rho)
={}&\frac{3q-1}{(q-1)^3}f(\rho)
+\frac{\rho}{(q-1)^2}f'(\rho)\\
&+\frac{q^2(q-3)}{(q-1)^3}f(q\rho)
+\frac{q^3\rho}{(q-1)^2}f'(q\rho),
\end{aligned}}
\]
and
\[
\boxed{\mathcal H_q(\rho)=\lambda_*+O(\rho^{-4}).}
\]
In particular, for \(q=2\),
\[
\boxed{
5f(\rho)+\rho f'(\rho)-4f(2\rho)+8\rho f'(2\rho)
=\lambda_*+O(\rho^{-4}).
}
\]
Thus the same two penalty levels used by the source's value-only second-order extrapolation support a fourth-order estimate when the Hellmann–Feynman derivative is retained.

More generally, if \(p\) fixed geometric penalty levels \(\rho,q\rho,\ldots,q^{p-1}\rho\) are used, ordinary Richardson extrapolation applied to the analytic \(1/\rho\) expansion gives \(O(\rho^{-p})\). Hermite interpolation using both \(f\) and \(f'\) at those same \(p\) levels gives
\[
\boxed{\lambda_*+O(\rho^{-2p}).}
\]
This order doubling is an asymptotic statement for fixed \(p\) and \(q\); it does not assert that extrapolation is numerically preferable once inner eigensolver error and floating-point cancellation dominate.

## Proof

In the orthogonal basis \(Q=[U,Z]\),
\[
Q^T(H+\rho A^TA)Q=
\begin{bmatrix}
B+\rho C&E\\
E^T&D
\end{bmatrix}.
\]
Put \(t=1/\rho\). For bounded \(\lambda\), the Schur complement of the upper-left block is
\[
\mathcal S(t,\lambda)
=D-\lambda I-tE^T[C+t(B-\lambda I)]^{-1}E.
\]
Because \(C\succ0\), this matrix-valued function is analytic in \((t,\lambda)\) near \((0,\lambda_*)\). Since \(\lambda_*\) is a simple eigenvalue of \(D\), the corresponding zero of \(\det\mathcal S(0,\lambda)\) is simple. The analytic implicit-function theorem therefore gives a unique real-analytic branch \(\lambda(t)\) with \(\lambda(0)=\lambda_*\). The other finite eigenvalue branches converge to the other eigenvalues of \(D\), while the remaining \(m\) eigenvalues diverge to \(+\infty\); hence, for positive sufficiently small \(t\), \(\lambda(t)=f(1/t)\).

Expanding the inverse,
\[
[C+t(B-\lambda I)]^{-1}
=C^{-1}-tC^{-1}(B-\lambda_*I)C^{-1}+O(t^2),
\]
gives the effective symmetric eigenproblem
\[
D-tG+t^2J+O(t^3).
\]
For a simple eigenvalue, second-order symmetric perturbation theory yields
\[
\lambda(t)=\lambda_*-t\,v^TGv
+t^2\bigl[v^TJv-v^TGSGv\bigr]+O(t^3),
\]
which proves the coefficient formulas.

For the extrapolation statement define \(g(t)=f(1/t)\). Analyticity gives a Taylor series for \(g\) at zero, and Hellmann–Feynman gives
\[
g'(t)=-t^{-2}f'(1/t).
\]
The displayed two-level formula is exactly the value at zero of the cubic Hermite interpolant through \(t\) and \(t/q\), after this derivative conversion. Its interpolation remainder is \(O(t^4)=O(\rho^{-4})\). With \(p\) geometric nodes, degree-\((2p-1)\) Hermite interpolation has remainder proportional to the squared nodal product and therefore gives \(O(t^{2p})=O(\rho^{-2p})\). Value-only interpolation similarly gives \(O(t^p)\).

## Exact low-dimensional witness

Take
\[
H=\begin{bmatrix}3&1\\1&1\end{bmatrix},\qquad A=\begin{bmatrix}1&0\end{bmatrix}.
\]
Then \(\lambda_*=1\) and
\[
f(\rho)=\frac{\rho+4-\sqrt{(\rho+2)^2+4}}2
=1-\rho^{-1}+2\rho^{-2}-3\rho^{-3}+2\rho^{-4}+O(\rho^{-5}).
\]
Therefore the source two-level extrapolation satisfies
\[
1-[2f(2\rho)-f(\rho)]=\rho^{-2}+O(\rho^{-3}),
\]
whereas the two-level Hellmann–Feynman Hermite estimator satisfies
\[
1-\mathcal H_2(\rho)=\frac{1}{2}\rho^{-4}+O(\rho^{-5}).
\]
The verification artifact checks these limits and independently checks the second-coefficient formula on a reproducible random symmetric instance.

## Scientific scope and limitations

The higher-order expansion requires a simple constrained target eigenvalue. Multiple target eigenvalues can split under the effective perturbation and require degenerate perturbation theory; no all-order scalar formula is asserted there. The conclusions are asymptotic as \(\rho\to\infty\). Extrapolation weights can amplify inner eigensolver errors and floating-point noise, especially when \(q\) is close to one or \(p\) is large. No finite-precision stability theorem or optimal choice of penalty levels is proved. The result concerns homogeneous linear constraints and the quadratic penalty path above; it does not replace projected certification of eigenvectors.

## Relation to prior work and originality boundary

Wang and Xia (2026) establish the exact penalty duality, finite-attainment dichotomy, first-order \(1/\rho\) expansion, leading coefficient, a value-only two-level \(O(\rho^{-2})\) extrapolation, and Hellmann–Feynman sensitivity. The contribution here is the simple-eigenvalue analytic continuation in \(1/\rho\), the explicit second coefficient, and the derivative-enhanced Hermite extrapolation that reaches \(O(\rho^{-2p})\) from \(p\) penalty levels, including the explicit two-level fourth-order formula.

Richardson extrapolation and Hermite interpolation themselves are classical and are not claimed as new. Bach (2021) studies Richardson extrapolation for regularization paths and other data-science problems; this provides important general precedent for extrapolating a regularization parameter. Zhou, Bai, and Li (2021) study linearly constrained Rayleigh quotient optimization through different reformulations and Krylov methods. Searches using the source paper, constrained-eigenvalue penalty paths, inverse-penalty expansions, Hellmann–Feynman derivatives, Richardson extrapolation, and Hermite extrapolation found no prior statement of the coefficient \(b\) or the derivative-enhanced \(O(\rho^{-2p})\) formulas for this projected-Hessian penalty path. Originality is therefore claimed only to the best of our knowledge.

## References

1. M. Wang and Y. Xia, *The Projected Hessian Quantification Theorem: Exact Duality For Constrained Eigenvalues*, arXiv:2609.18538, 2026. https://arxiv.org/abs/2609.18538
2. F. Bach, *On the Effectiveness of Richardson Extrapolation in Data Science*, SIAM Journal on Mathematics of Data Science 3(4), 1251–1277, 2021. https://doi.org/10.1137/21M1397349
3. Y. Zhou, Z. Bai, and R.-C. Li, *Linear Constrained Rayleigh Quotient Optimization: Theory and Algorithms*, CSIAM Transactions on Applied Mathematics 2(2), 195–262, 2021. https://doi.org/10.4208/csiam-am.2021.nla.01
4. D. C. Joyce, *Survey of Extrapolation Processes in Numerical Analysis*, SIAM Review 13(4), 435–490, 1971. https://doi.org/10.1137/1013092
