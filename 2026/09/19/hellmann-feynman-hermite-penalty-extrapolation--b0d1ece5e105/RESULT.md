# Hermite–Hellmann–Feynman extrapolation for constrained eigenvalue penalties

## Result

Let \(H\in\mathbb S^n\), let \(A\in\mathbb R^{m\times n}\) have full row rank, and let \(Z\) have orthonormal columns spanning \(\ker A\). Write
\[
\lambda_* = \lambda_{\min}(Z^T H Z).
\]
Assume that \(\lambda_*\) is simple. For
\[
f(\rho)=\lambda_{\min}(H+\rho A^T A),\qquad \rho>0,
\]
consider the non-finitely-exact case in which the constrained minimizing direction is coupled to the constraint range. Then the large-penalty eigenvalue branch is analytic in \(t=1/\rho\): there is an analytic function \(F\) near \(t=0\) such that
\[
F(t)=f(1/t),\qquad F(0)=\lambda_*.
\]
Consequently \(F\) has a full inverse-penalty expansion.

If \(x_\rho\) is the normalized eigenvector associated with \(f(\rho)\), Hellmann–Feynman gives
\[
f'(\rho)=x_\rho^T A^T A x_\rho=\|Ax_\rho\|_2^2,
\]
and therefore
\[
F'(1/\rho)=-\rho^2 f'(\rho).
\]
For any fixed distinct positive scales \(s_1,\ldots,s_q\), let \(P_{2q-1}\) be the Hermite interpolating polynomial of degree at most \(2q-1\) satisfying
\[
P_{2q-1}(t_j)=F(t_j),\qquad
P'_{2q-1}(t_j)=F'(t_j),
\qquad
 t_j=(s_j\rho)^{-1}.
\]
Then the infinity extrapolant
\[
\widehat\lambda_q(\rho):=P_{2q-1}(0)
\]
satisfies
\[
\boxed{\widehat\lambda_q(\rho)=\lambda_*+O(\rho^{-2q}).}
\]
Thus \(q\) penalized eigenpairs, using the already available Hellmann–Feynman constraint norms in addition to the eigenvalues, cancel the first \(2q-1\) inverse powers. This doubles the generic inverse-power order obtainable from \(q\) value samples alone.

For two penalty levels \(\rho\) and \(2\rho\), the degree-three Hermite formula simplifies to
\[
\boxed{
\widehat\lambda_2(\rho)
=5f(\rho)-4f(2\rho)
 +\rho f'(\rho)+8\rho f'(2\rho)
=\lambda_*+O(\rho^{-4}).
}
\]
In contrast, the two-level value-only Richardson formula already noted in the motivating source is
\[
2f(2\rho)-f(\rho)=\lambda_*+O(\rho^{-2}).
\]
The new fourth-order formula uses the same two penalized eigenpair solves; it additionally evaluates \(\|Ax_\rho\|_2^2\) and \(\|Ax_{2\rho}\|_2^2\).

## Block form and second-order coefficient

Choose orthonormal \(U,Z\) spanning \(\mathcal R(A^T)\) and \(\ker A\), and define
\[
B=U^T H U,\qquad E=U^T H Z,\qquad D=Z^T H Z,
\]
\[
C=(AU)^T(AU)\succ0,
\qquad
G=E^T C^{-1}E.
\]
Let \(w\) be the unit eigenvector of \(D\) for the simple eigenvalue \(\lambda_*\). The Schur complement equation is
\[
\det\!\left(
D-\lambda I-E^T(B+\rho C-\lambda I)^{-1}E
\right)=0.
\]
With \(t=1/\rho\),
\[
(B+\rho C-\lambda I)^{-1}
=tC^{-1}-t^2C^{-1}(B-\lambda I)C^{-1}+O(t^3).
\]
Hence the effective constrained matrix is
\[
D-tG+t^2J+O(t^3),
\qquad
J=E^T C^{-1}(B-\lambda_*I)C^{-1}E.
\]
The simple-root implicit-function theorem yields analyticity of \(F\). Standard simple-eigenvalue perturbation then gives
\[
F(t)=\lambda_*-ct+dt^2+O(t^3),
\qquad c=w^TGw>0,
\]
where, for an orthonormal eigenbasis \(\{w,w_j\}\) of \(D\),
\[
\boxed{
d=w^TJw-
\sum_{j:\lambda_j\ne\lambda_*}
\frac{|w_j^TGw|^2}{\lambda_j-\lambda_*}.
}
\]
The first-order coefficient \(c\) is part of the motivating source's penalty-path theory. The displayed closed form for \(d\), together with the analytic inverse-penalty branch, supplies the input needed for systematic higher-order extrapolation.

The one-level Hellmann–Feynman correction
\[
f(\rho)+\rho f'(\rho)=\lambda_*-d\rho^{-2}+O(\rho^{-3})
\]
is therefore second order. The motivating source already uses this type of Hellmann–Feynman correction at second order; it is not claimed here as a new contribution.

## Proof of the order-doubling statement

Because \(F\) is analytic near zero, Hermite interpolation applies on the shrinking nodes \(t_j=(s_j\rho)^{-1}\). Its remainder at zero is
\[
F(0)-P_{2q-1}(0)
=
\frac{F^{(2q)}(\xi)}{(2q)!}
\prod_{j=1}^q (0-t_j)^2
\]
for some \(\xi\) between zero and the largest node. The derivative is uniformly bounded for sufficiently large \(\rho\), while
\[
\prod_{j=1}^q t_j^2
=\rho^{-2q}\prod_{j=1}^q s_j^{-2}.
\]
This proves \(P_{2q-1}(0)=\lambda_*+O(\rho^{-2q})\).

The method is also uniquely maximally polynomial-exact among coefficient-blind linear extrapolators using these same \(q\) values and \(q\) first derivatives. Exact cancellation of the monomials \(1,t,\ldots,t^{2q-1}\) gives a nonsingular confluent Vandermonde system, hence the Hermite weights are unique. A general additional cancellation at degree \(2q\) cannot be imposed with the same \(2q\) scalar data without exploiting extra structure. This is a statement about linear extrapolation of arbitrary analytic inverse-power expansions, not a lower bound for all possible nonlinear estimators.

## Concrete two-level example

For the block data
\[
C=\operatorname{diag}(2,0.7),\quad
B=\begin{pmatrix}1.2&0.3\\0.3&-0.4\end{pmatrix},
\]
\[
E=\begin{pmatrix}0.8&-0.2&0.5\\0.4&0.6&-0.3\end{pmatrix},
\qquad
D=\operatorname{diag}(0.5,1.7,3),
\]
with \(H=\begin{psmallmatrix}B&E\\E^T&D\end{psmallmatrix}\) and
\(A=[\operatorname{diag}(\sqrt2,\sqrt{0.7})\ \ 0]\), one has
\[
\lambda_*=0.5,
\qquad
c=0.5485714285714287,
\qquad
d=-0.1026394557823130.
\]
The verification artifact gives the following errors:

| \(\rho\) | raw \(f(\rho)-\lambda_*\) | value-only two-level | two-level Hermite-HF | \(\rho^4\) times Hermite-HF error |
|---:|---:|---:|---:|---:|
| 10 | \(-5.6133\times10^{-2}\) | \(7.0413\times10^{-4}\) | \(8.2296\times10^{-6}\) | \(8.2296\times10^{-2}\) |
| 20 | \(-2.7714\times10^{-2}\) | \(1.5035\times10^{-4}\) | \(5.1969\times10^{-7}\) | \(8.3150\times10^{-2}\) |
| 40 | \(-1.3782\times10^{-2}\) | \(3.4719\times10^{-5}\) | \(3.2057\times10^{-8}\) | \(8.2066\times10^{-2}\) |
| 80 | \(-6.8736\times10^{-3}\) | \(8.3423\times10^{-6}\) | \(1.9839\times10^{-9}\) | \(8.1260\times10^{-2}\) |

The nonzero limiting scaled error demonstrates that fourth order is genuinely attained by an ordinary constrained-eigenvalue penalty path, rather than the formula being accidentally higher order on all such paths.

If the surviving leading coefficients are nonzero, the penalty magnitude required for a scalar eigenvalue error \(\epsilon\) changes from \(\Theta(\epsilon^{-1})\) for the raw path to \(\Theta(\epsilon^{-1/2})\) for the two-level value-only extrapolant and \(\Theta(\epsilon^{-1/4})\) for the two-level Hermite-HF extrapolant. This is a statement about penalty scale, not an eigensolver computational-complexity bound.

## Reproducibility

`artifacts/verify_hermite_penalty.py` constructs the displayed symmetric example, evaluates penalized eigenpairs with NumPy, evaluates the Hellmann–Feynman derivatives, checks the explicit two-level formula against a general confluent Hermite solve, and prints the convergence table. `artifacts/verification_output.txt` is its recorded output.

## Limitations

The theorem assumes a simple constrained eigenvalue and the non-finitely-exact asymptotic regime. Multiple constrained eigenvalues require a cluster-valued perturbation analysis and are not covered here. The formula assumes sufficiently accurate penalized eigenpairs; extrapolation can amplify eigenvalue and derivative errors, and it is not a certified upper or lower bound. No new conditioning theorem or eigensolver complexity theorem is claimed. The maximum constrained eigenvalue has an analogous sign-transformed formulation but is not developed separately.

The order-doubling claim is restricted to coefficient-blind linear extrapolation based on the displayed value and first-derivative data. Hermite interpolation and Richardson extrapolation are classical tools. The novelty claim is only their higher-order Hellmann–Feynman use on the newly quantified constrained-eigenvalue penalty path, together with the analytic branch and explicit coefficient calculation stated above.

## Relation to prior literature

The motivating paper by Meiling Wang and Yong Xia, *The Projected Hessian Quantification Theorem: Exact Duality For Constrained Eigenvalues* (arXiv:2609.18538), establishes the exact penalty representation, characterizes finite exact recovery, gives the first-order nonexact asymptotic coefficient, uses the Hellmann–Feynman sensitivity relation, and records second-order value-only and one-level sensitivity corrections. Those results are prior and are not claimed here.

Earlier constrained-eigenvalue literature includes S. Ilanko and F. W. Williams, *Wittrick–Williams algorithm proof of bracketing and convergence theorems for eigenvalues of constrained structures with positive and negative penalty parameters*, International Journal for Numerical Methods in Engineering 75 (2008), 83–102, DOI 10.1002/nme.2247, which establishes penalty bracketing and convergence in structural eigenproblems; and Y. Zhou, Z. Bai, R.-C. Li, *Linear Constrained Rayleigh Quotient Optimization: Theory and Algorithms*, CSIAM Transactions on Applied Mathematics 2 (2021), 195–262, DOI 10.4208/csiam-am.2021.nla.01, which studies constrained Rayleigh quotient formulations and Krylov algorithms.

Searches for equivalent formulations combining constrained eigenvalue penalty paths with Hellmann–Feynman, derivative-assisted Richardson/Hermite extrapolation, confluent Richardson extrapolation, and inverse-penalty acceleration did not reveal the present order-doubling result. Originality is therefore claimed only to the best of our knowledge.

### References

1. M. Wang and Y. Xia, *The Projected Hessian Quantification Theorem: Exact Duality For Constrained Eigenvalues*, arXiv:2609.18538, 2026. https://arxiv.org/abs/2609.18538
2. S. Ilanko and F. W. Williams, *Wittrick–Williams algorithm proof of bracketing and convergence theorems for eigenvalues of constrained structures with positive and negative penalty parameters*, Int. J. Numer. Meth. Engng. 75 (2008), 83–102. https://doi.org/10.1002/nme.2247
3. Y. Zhou, Z. Bai and R.-C. Li, *Linear Constrained Rayleigh Quotient Optimization: Theory and Algorithms*, CSIAM Trans. Appl. Math. 2 (2021), 195–262. https://doi.org/10.4208/csiam-am.2021.nla.01
