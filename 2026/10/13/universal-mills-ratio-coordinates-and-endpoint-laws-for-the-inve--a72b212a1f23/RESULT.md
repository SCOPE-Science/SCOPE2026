# Universal Mills-ratio coordinates and endpoint laws for the inverse-Gaussian Chvátal minimum
## Finding
For \(\kappa>1\), let
\[
m(\kappa)=\inf_{\mu,\lambda>0}\Pr\{X_{\mu,\lambda}\le \kappa\,\mathbb E X_{\mu,\lambda}\},
\qquad X_{\mu,\lambda}\sim\operatorname{IG}(\mu,\lambda),
\]
and let \(x_0(\kappa)=\sqrt{\lambda/\mu}\) at the unique minimizer supplied by Hu--Lu--Zhou--Zhou. Put
\[
\rho=\frac{\kappa-1}{\kappa+1},\qquad
M(z)=\frac{1-\Phi(z)}{\varphi(z)}.
\]
There is a unique \(z_\kappa>0\) satisfying
\[
z_\kappa M(z_\kappa)=\frac{1}{1+\rho}=\frac{\kappa+1}{2\kappa},
\]
and the optimizer and minimum have the exact universal representation
\[
x_0(\kappa)=\frac{\sqrt{\kappa}}{\kappa+1}\,z_\kappa,\qquad
m(\kappa)=\Phi(\rho z_\kappa)+\frac{\varphi(\rho z_\kappa)}{(1+\rho)z_\kappa}.
\]
Moreover
\[
\frac{d}{d\rho}m(\kappa(\rho))
=\frac{z_\kappa\varphi(\rho z_\kappa)}{1+\rho}>0.
\]
Thus the phase transition at \(\kappa=1\) has the sharp endpoint laws
\[
z_\kappa=\sqrt{\frac{2}{\kappa-1}}\bigl(1+O(\kappa-1)\bigr),\quad
x_0(\kappa)=\frac{1}{\sqrt{2(\kappa-1)}}\bigl(1+O(\kappa-1)\bigr),
\]
\[
m(\kappa)=\frac12+\sqrt{\frac{\kappa-1}{\pi}}
+O\!\left((\kappa-1)^{3/2}\right)
\qquad(\kappa\downarrow1).
\]
At the opposite endpoint, if \(z_*>0\) is the unique solution of \(z_*M(z_*)=1/2\), then
\[
z_*=0.6120031809624807\ldots,\qquad
z_*\varphi(z_*)=0.2024564901880246\ldots,
\]
and
\[
x_0(\kappa)=\frac{z_*}{\sqrt{\kappa}}+O(\kappa^{-3/2}),\qquad
m(\kappa)=1-\frac{z_*\varphi(z_*)}{\kappa}+O(\kappa^{-2})
\qquad(\kappa\to\infty).
\]

## Assumptions and scope
The inverse-Gaussian distribution is parameterized by mean \(\mu>0\) and shape \(\lambda>0\), with density
\[
f_{\mu,\lambda}(y)=\sqrt{\frac{\lambda}{2\pi y^3}}
\exp\!\left(-\frac{\lambda(y-\mu)^2}{2\mu^2y}\right),\qquad y>0.
\]
The statement concerns the sharp minimum, over all \(\mu,\lambda>0\), of the threshold probability at a fixed multiplier \(\kappa>1\). The scale reduction uses \(x=\sqrt{\lambda/\mu}\). The endpoint estimates are asymptotic only as \(\kappa\downarrow1\) or \(\kappa\to\infty\).

## Proof
Hu--Lu--Zhou--Zhou give
\[
g_\kappa(x)=
\Phi\!\left(\frac{\kappa-1}{\sqrt\kappa}x\right)
+e^{2x^2}\Phi\!\left(-\frac{\kappa+1}{\sqrt\kappa}x\right)
\]
and prove that, for \(\kappa>1\), its minimum occurs at the unique positive zero of
\[
h_\kappa(x)=2\int_{(\kappa+1)x/\sqrt\kappa}^\infty e^{-t^2/2}\,dt
-\frac{1}{\sqrt\kappa\,x}
e^{-(\kappa+1)^2x^2/(2\kappa)}.
\]
Set
\[
z=\frac{\kappa+1}{\sqrt\kappa}x,\qquad
\rho=\frac{\kappa-1}{\kappa+1}.
\]
Writing \(\overline\Phi(z)=1-\Phi(z)=\varphi(z)M(z)\), the equation \(h_\kappa(x)=0\) becomes exactly
\[
zM(z)=\frac{\kappa+1}{2\kappa}=\frac1{1+\rho}.
\]
The integral representation
\[
M(z)=\int_0^\infty e^{-zu-u^2/2}\,du
\]
gives
\[
zM(z)=1-\int_0^\infty u\,e^{-zu-u^2/2}\,du.
\]
Hence
\[
\frac d{dz}\bigl(zM(z)\bigr)
=\int_0^\infty u^2e^{-zu-u^2/2}\,du>0.
\]
Thus \(zM(z)\) increases continuously from \(0\) to \(1\), proving existence and uniqueness of \(z_\kappa\).

Because
\[
x^2=\frac{1-\rho^2}{4}z^2,
\]
the second term of \(g_\kappa\) satisfies
\[
e^{2x^2}\overline\Phi(z)=\varphi(\rho z)M(z).
\]
At the root, \(M(z_\kappa)=1/((1+\rho)z_\kappa)\), giving the exact formula for \(m(\kappa)\).

Since \(F(z)=zM(z)\) has \(F'(z_\kappa)>0\), the implicit function theorem applies. Differentiating
\[
m(\rho)=\Phi(\rho z_\kappa)+\varphi(\rho z_\kappa)M(z_\kappa)
\]
and using \(M'(z)=zM(z)-1\) and \(z_\kappa M(z_\kappa)=1/(1+\rho)\), the terms involving \(dz_\kappa/d\rho\) cancel and give
\[
m'(\rho)=\frac{z_\kappa\varphi(\rho z_\kappa)}{1+\rho}>0.
\]

For the critical endpoint,
\[
1-F(z)=\int_0^\infty u\,e^{-zu-u^2/2}\,du
=z^{-2}-3z^{-4}+O(z^{-6}).
\]
Combining this with \(1-(1+\rho)^{-1}=\rho/(1+\rho)\) yields \(z_\kappa=\rho^{-1/2}(1+O(\rho))\). Since \(\rho=(\kappa-1)/2+O((\kappa-1)^2)\), the formulas for \(z_\kappa\) and \(x_0(\kappa)\) follow. Substitution in the exact minimum gives
\[
m(\kappa)=\frac12+2\varphi(0)\sqrt\rho+O(\rho^{3/2})
=\frac12+\sqrt{\frac{\kappa-1}{\pi}}+O((\kappa-1)^{3/2}).
\]

For \(\kappa\to\infty\), \(\rho\to1\) and \(z_\kappa\to z_*\), where \(z_*M(z_*)=1/2\). Smooth implicit dependence gives \(z_\kappa=z_*+O(\kappa^{-1})\), hence \(x_0(\kappa)=z_*/\sqrt\kappa+O(\kappa^{-3/2})\). The exact derivative satisfies \(m'(\rho)\to z_*\varphi(z_*)/2\), while \(1-\rho=2/(\kappa+1)\), giving
\[
m(\kappa)=1-\frac{z_*\varphi(z_*)}{\kappa}+O(\kappa^{-2}).
\]

## Verification
The analytic proof uses no finite enumeration. The standalone checker `VERIFY.py` independently evaluates the Mills-ratio root, compares the transformed and original inverse-Gaussian formulas at representative parameter values, checks local minimality numerically, and verifies the two endpoint normalizations. Its numerical checks are regression tests only.

## Relationship to prior work
Hu--Lu--Zhou--Zhou prove the exact inverse-Gaussian reduction, uniqueness of the minimizer for \(\kappa>1\), and identify \(\kappa=1\) as a phase-transition point. Their theorem leaves the optimizer as the zero of \(h_\kappa\). The present result converts that zero condition to the universal Gaussian Mills-ratio coordinate \(zM(z)\), derives an exact parametric formula for the minimum, and quantifies both endpoints.

## Limitations
The result refines the inverse-Gaussian branch only. It does not claim analogous endpoint laws for the paper's log-normal, Gumbel, or logistic families. The literature search did not locate an earlier statement of the Mills-ratio parametrization or the two endpoint laws, but an equivalent elementary reformulation could exist in older inverse-Gaussian or first-passage literature under different notation.

## References
1. Z.-C. Hu, P. Lu, Q.-Q. Zhou, X.-W. Zhou, *The infimum values of the probability functions for some infinitely divisible distributions motivated by Chvátal's theorem*, arXiv:2308.07678, first public version 2023-08-15; current public version v2, Theorem 2.1 and Remark 2.2.
