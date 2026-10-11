# Exact first-order non-sphericity of Haddad's Barker--Larman branch

## Finding

Let
\[
\lambda_0=4\sqrt3\pi
\]
and fix an integer \(N\ge1\). For the finite-order body \(K_{\lambda,N}\subset\mathbb R^4\) constructed by Haddad near \(\lambda_0\), the radial function satisfies, uniformly for \(t\in[0,2\pi]\),
\[
\boxed{
\rho_{\lambda,N}(t)
=
2-\frac{\sqrt3}{24\pi}\bigl(1+4\cos(2t)\bigr)(\lambda-\lambda_0)
+
O_N\!\bigl((\lambda-\lambda_0)^2\bigr).
}
\]

Writing \(\delta=\lambda-\lambda_0\), for \(\delta\downarrow0\) this gives
\[
R(K_{\lambda,N})
=
2+\frac{\sqrt3}{8\pi}\delta+O_N(\delta^2),
\]
and
\[
r(K_{\lambda,N})
=
2-\frac{5\sqrt3}{24\pi}\delta+O_N(\delta^2).
\]
For \(\delta\uparrow0\), the two linear magnitudes interchange:
\[
R(K_{\lambda,N})
=
2+\frac{5\sqrt3}{24\pi}|\delta|+O_N(\delta^2),
\]
and
\[
r(K_{\lambda,N})
=
2-\frac{\sqrt3}{8\pi}|\delta|+O_N(\delta^2).
\]

Hence, from either side,
\[
\boxed{
R(K_{\lambda,N})-r(K_{\lambda,N})
=
\frac{\sqrt3}{3\pi}|\lambda-\lambda_0|
+
O_N\!\bigl((\lambda-\lambda_0)^2\bigr).
}
\]
Equivalently,
\[
\boxed{
\lim_{\lambda\to\lambda_0,\ \lambda\ne\lambda_0}
\frac{R(K_{\lambda,N})-r(K_{\lambda,N})}{|\lambda-\lambda_0|}
=
\frac{\sqrt3}{3\pi}.
}
\]

The coefficient
\[
\frac{\sqrt3}{3\pi}=0.1837762984739307\ldots
\]
is independent of \(N\). Thus every finite truncation of the nontrivial branch leaves the radius-\(2\) ball with the same first-order radial anisotropy.

## Assumptions and scope

The bodies are precisely the smooth convex bodies of revolution \(K_{\lambda,N}\) supplied by the finite partial sums in arXiv:2609.10257v1, for \(\lambda\) in a sufficiently small neighborhood of \(\lambda_0\). The statement is local in \(\lambda\) and is made separately for each fixed \(N\ge1\).

The result concerns the outradius and inradius measured from the origin, as in the source. It does not prove convergence of the formal power series as \(N\to\infty\), does not produce an exact Barker--Larman counterexample, and does not claim that the displayed first-order directions remain the exact maximizing and minimizing directions away from the bifurcation point.

## Proof

Haddad parametrizes the meridian curve by
\[
\gamma_{\lambda,N}(t)
=
\frac{1}{\cos(t-h_{\lambda,N}(t))}
(\cos t,\sin t),
\]
so its radial function is
\[
\rho_{\lambda,N}(t)
=
\sec(t-h_{\lambda,N}(t)).
\]

The finite nontrivial branch is
\[
h_{\lambda,N}(t)
=
t-\frac{\pi}{3}
+
\sum_{n=1}^N
\frac{(\lambda-\lambda_0)^n}{n!}\phi_n(t).
\]
The source computes the first bifurcation coefficient exactly:
\[
\phi_1(t)
=
-\frac{1}{48\pi}
+
\frac{1}{24\pi}\bigl(1+2\cos(2t)\bigr)
=
\frac{1+4\cos(2t)}{48\pi}.
\]
Therefore, for fixed \(N\),
\[
t-h_{\lambda,N}(t)
=
\frac{\pi}{3}
-
\delta\phi_1(t)
+
O_N(\delta^2),
\qquad
\delta=\lambda-\lambda_0,
\]
uniformly in \(t\). Since
\[
\frac{d}{dx}\sec x\bigg|_{x=\pi/3}
=
2\sqrt3,
\]
Taylor expansion gives
\[
\rho_{\lambda,N}(t)
=
2-2\sqrt3\,\delta\,\phi_1(t)+O_N(\delta^2),
\]
which is the claimed radial expansion.

Set
\[
g(t)
=
-\frac{\sqrt3}{24\pi}\bigl(1+4\cos(2t)\bigr).
\]
Then
\[
\max_t g(t)=\frac{\sqrt3}{8\pi},
\qquad
\min_t g(t)=-\frac{5\sqrt3}{24\pi}.
\]
The remainder in
\[
\rho_{\lambda,N}(t)=2+\delta g(t)+O_N(\delta^2)
\]
is uniform on the compact parameter circle. Consequently, for \(\delta>0\),
\[
\max_t\rho_{\lambda,N}(t)
=
2+\delta\max_tg(t)+O_N(\delta^2)
\]
and
\[
\min_t\rho_{\lambda,N}(t)
=
2+\delta\min_tg(t)+O_N(\delta^2).
\]
For \(\delta<0\), the roles of \(\max g\) and \(\min g\) are exchanged.

Rotating the meridian around the symmetry axis introduces no new radial values. Thus these extrema are exactly the outradius and inradius of \(K_{\lambda,N}\). Subtracting the two expansions yields
\[
\max g-\min g
=
\frac{\sqrt3}{8\pi}
+
\frac{5\sqrt3}{24\pi}
=
\frac{\sqrt3}{3\pi},
\]
which proves the two-sided asymptotic.

## Verification

The proof uses only the explicit first coefficient of the source's finite partial sum and a uniform Taylor expansion of \(\sec\) near \(\pi/3\).

The bundled checker symbolically differentiates the exact radial expression at \(\lambda=\lambda_0\), verifies
\[
\partial_\lambda\rho_{\lambda,N}(t)\big|_{\lambda=\lambda_0}
=
-\frac{\sqrt3}{24\pi}\bigl(1+4\cos(2t)\bigr),
\]
and checks the maximum, minimum, and oscillation coefficients exactly. It also confirms the displayed decimal value.

The checker does not infer an infinite-series statement from finite computation. The theorem is for every fixed finite \(N\), and the uniform \(O_N(\delta^2)\) remainder follows analytically because \(h_{\lambda,N}\) is a finite trigonometric-polynomial expansion and \(\sec\) is smooth in a fixed neighborhood of \(\pi/3\).

## Relationship to prior work

Haddad proves that the same families satisfy a universal lower bound
\[
R(K_{\lambda,N})-r(K_{\lambda,N})
\ge c|\lambda-\lambda_0|
\]
for a positive unspecified constant \(c\). The proof uses only the two test directions \(t=0\) and \(t=\pi/2\) and a first Taylor estimate. The source does not state the exact asymptotic coefficient, the complete first-order radial profile, or the one-sided expansions of \(R\) and \(r\).

The earlier Haddad--Ryabogin rigidity theorem treats exact constant tangent-hyperplane section area for an arithmetic set of section areas. The focal source explains that its arithmetic argument breaks down at the rational bifurcation value corresponding to \(\lambda_0\). That positive theorem therefore does not imply the present local asymptotic on the approximate branch.

Targeted searches for the source identifier together with “outradius”, “inradius”, “first order”, the coefficient \(\sqrt3/(3\pi)\), and the crossing value \(\lambda_0\) found no equivalent statement. The closest published records returned by semantic search concern other radius-ratio or convex-body stability problems and do not imply this bifurcation coefficient.

## Limitations

The asymptotic is local at \(\lambda_0\) and is proved separately for each fixed finite \(N\). The implicit constant in \(O_N(\delta^2)\) may depend on \(N\).

No convergence in \(N\) is asserted. The result does not settle the Barker--Larman problem, does not improve the source's section-error order, and does not establish a second-order non-sphericity coefficient.

The originality assessment is based on the focal full text, the earlier exact-rigidity paper, the foundational Barker--Larman problem record, and targeted exact-constant searches. An equivalent observation under different perturbative terminology remains a residual bibliographic risk.

## References

1. J. Haddad, *An approximate counterexample to the Barker--Larman problem in dimension 4*, arXiv:2609.10257v1, first public 9 September 2026.
2. J. Haddad and D. Ryabogin, *On convex bodies with constant non-central sections*, arXiv:2605.00299v1, first public 1 May 2026.
3. J. A. Barker and D. G. Larman, *Determination of convex bodies by certain sets of sectional volumes*, Discrete Mathematics 241 (2001), 79--96, DOI:10.1016/S0012-365X(01)00111-X.
