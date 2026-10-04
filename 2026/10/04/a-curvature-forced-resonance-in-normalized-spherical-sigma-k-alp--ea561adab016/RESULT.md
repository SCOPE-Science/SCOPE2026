# A curvature-forced resonance in normalized spherical \(\sigma_k^\alpha\)-flow
## Finding
Let \(1\le k\le n\), \(\alpha>0\), and \(\beta>1+k\alpha\). For the centered geodesic-sphere solution of \(\partial_tX=-\rho^\beta\sigma_k^\alpha\nu\) in the unit sphere, put \(a=\beta-k\alpha-1\), \(\gamma_0=\binom{n}{k}^\alpha\), \(\lambda(t)=(1+a\gamma_0t)^{1/a}\), \(y(t)=\lambda(t)\rho(t)\), and \(B=k\alpha/3\). Then \(y(t)\to1\), and the first correction has a sharp resonance at \(a=2\): if \(a>2\), then \(\lambda^2(y-1)\to B/(a-2)\); if \(a=2\), then \(\lambda^2(y-1)/\log\lambda\to B\); if \(0<a<2\), then \(\lambda^a(y-1)\to C(\rho_0)\), where \(C(\rho_0)=-a^{-1}[\rho_0^{-a}-1+a\int_0^{\rho_0}((r\cot r)^{k\alpha}-1)/(r^{a+1}(r\cot r)^{k\alpha})\,dr]\). Thus ambient spherical curvature imposes a universal \(\lambda^{-2}\) correction above the threshold and a logarithmic resonance at the threshold.

Equivalently, in the normalized time \(\tau\) for which \(\lambda=e^{\gamma_0\tau}\), the curvature-forced correction is of order \(e^{-2\gamma_0\tau}\) when \(a>2\), of order \(\tau e^{-2\gamma_0\tau}\) when \(a=2\), and of order \(e^{-a\gamma_0\tau}\) when \(0<a<2\), with the last coefficient depending explicitly on the initial radius.

## Assumptions and scope
Work in the unit round sphere \(\mathbb S^{n+1}\). Fix \(1\le k\le n\), \(\alpha>0\), and \(\beta>1+k\alpha\). The flow speed is \(\rho^\beta\sigma_k^\alpha\), where \(\rho\in(0,\pi/2)\) is geodesic distance from the fixed center and \(\sigma_k\) is the unnormalized \(k\)-th elementary symmetric polynomial of the principal curvatures. The initial hypersurface is a centered geodesic sphere of radius \(\rho_0\in(0,\pi/2)\).

Set
\[
a=\beta-k\alpha-1>0,\qquad
\gamma_0=\binom{n}{k}^{\alpha},\qquad
\lambda(t)=(1+a\gamma_0t)^{1/a},\qquad
y(t)=\lambda(t)\rho(t).
\]
The statement concerns this invariant round subfamily. It does not assert the same second-order coefficient for arbitrary nonspherical solutions.

## Proof
A centered geodesic sphere of radius \(\rho\) has all principal curvatures equal to \(\cot\rho\). Hence
\[
\sigma_k=\binom{n}{k}(\cot\rho)^k
\]
and its radius satisfies the exact scalar equation
\[
\rho'=-\gamma_0\rho^{\beta}(\cot\rho)^{k\alpha}
      =-\gamma_0\rho^{a+1}A(\rho),
\qquad
A(r)=(r\cot r)^{k\alpha}.
\]
Because \(0<r\cot r<1\) on \((0,\pi/2)\), the radius is strictly decreasing. A positive limiting radius would make \(\rho'\) bounded away from zero, so \(\rho(t)\to0\).

The Taylor expansion at the origin is
\[
r\cot r=1-\frac{r^2}{3}-\frac{r^4}{45}+O(r^6),
\qquad
A(r)=1-Br^2+O(r^4),
\qquad B=\frac{k\alpha}{3}.
\]
Introduce
\[
x(t)=\rho(t)^{-a},\qquad L(t)=1+a\gamma_0t=\lambda(t)^a,
\qquad E(t)=x(t)-L(t).
\]
Then
\[
x'=a\gamma_0A(\rho),\qquad
E'=a\gamma_0(A(\rho)-1).
\]
Since \(A(\rho)\to1\), one has \(x/L\to1\), and therefore \(y=\lambda\rho=(x/L)^{-1/a}\to1\). Moreover,
\[
\rho^2=L^{-2/a}(1+o(1)),
\qquad
\frac{dE}{dL}=A(\rho)-1=-B L^{-2/a}(1+o(1)).
\]

If \(a>2\), integration gives
\[
E=-\frac{aB}{a-2}L^{1-2/a}(1+o(1)).
\]
Using \((1+z)^{-1/a}=1-z/a+o(z)\) with \(z=E/L\),
\[
y-1=\frac{B}{a-2}L^{-2/a}(1+o(1))
     =\frac{B}{a-2}\lambda^{-2}(1+o(1)).
\]

If \(a=2\), then
\[
E=-B\log L+o(\log L),
\]
so, because \(\log L=2\log\lambda\),
\[
y-1=B\frac{\log\lambda}{\lambda^2}(1+o(1)).
\]

If \(0<a<2\), the integral of \(L^{-2/a}\) at infinity converges, so \(E(t)\) has a finite limit. Changing variables from time to radius in the exact equation gives
\[
E_\infty
=\rho_0^{-a}-1
+a\int_0^{\rho_0}
\frac{A(r)-1}{r^{a+1}A(r)}\,dr.
\]
The integrand is \(-Br^{1-a}+O(r^{3-a})\), hence the integral converges precisely in this regime. Expanding \(y=(1+E/L)^{-1/a}\) yields
\[
\lambda^a(y-1)\longrightarrow -\frac{E_\infty}{a}=C(\rho_0),
\]
which is the stated formula.

## Verification
The exact round-sphere reduction uses the standard principal-curvature identity \(\kappa_i=\cot\rho\) for a geodesic sphere in the unit sphere. The packaged checker verifies symbolically the expansion of \((r\cot r)^{k\alpha}\), checks the algebra converting the three asymptotic forms of \(E\) into the displayed limits for \(y\), and numerically integrates representative scalar ODEs on both sides of the resonance. These finite computations are consistency checks only; the three limits above follow from the analytic comparison and integration argument.

## Relationship to prior work
Sheng, Sheng, and Yang prove convergence of the normalized supercritical spherical flow and, in their normalized evolution, retain the ambient-curvature contribution only as an \(O(\lambda^{-2})\) term. Their theorem therefore establishes convergence but does not identify the sharp round-sphere second-order coefficient, the threshold \(a=2\), or the logarithmic resonance. The companion hyperbolic-space work studies a related non-homogeneous curvature flow in a different ambient geometry and does not imply these spherical asymptotics.

The round family is not an arbitrary special case: it is an invariant family that calibrates any uniform convergence-rate statement for the full flow. In particular, when \(a>2\), the positive limit \(B/(a-2)\) rules out a uniform \(o(\lambda^{-2})\) rate even on centered spheres, while at \(a=2\) the factor \(\log\lambda\) rules out a pure \(O(\lambda^{-2})\) bound for this family.

## Limitations
The result treats centered geodesic spheres and does not determine second-order asymptotics of nonspherical modes. The subcritical coefficient \(C(\rho_0)\) can depend on the initial radius and may vanish for exceptional data; no nonvanishing claim is made there. The ambient sphere has sectional curvature one; rescaling the ambient curvature changes the curvature-correction coefficient.

## References
1. H. Sheng, W. Sheng, J. Yang, *Non-homogeneous curvature flows in a hemisphere*, arXiv:2609.31023v1, first public 2026-09-25.
2. H. Sheng, W. Sheng, J. Yang, *Non-homogeneous curvature flows in hyperbolic space*, arXiv:2609.29199v1, first public 2026-09-24.
