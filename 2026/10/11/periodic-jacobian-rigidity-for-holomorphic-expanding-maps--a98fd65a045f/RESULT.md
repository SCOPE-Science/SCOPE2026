# Periodic Jacobian rigidity for holomorphic expanding maps
## Finding
Let \(f:X\to X\) be a holomorphic expanding map on a compact connected complex manifold, and let \(d=\deg(f)\). Then there exists a smooth positive volume form \(m\), normalized to total mass one, such that \(f^*m=d\,m\) pointwise. Equivalently, for every smooth positive volume form \(m_0\) there is a smooth real function \(u\) satisfying \[\log J_{m_0}f-\log d=u-u\circ f.\] Consequently, every periodic point \(p\) with \(f^n(p)=p\) satisfies \[\det_{\mathbb R}(D_pf^n)=d^n,\qquad |\det_{\mathbb C}(D_pf^n)|^2=d^n,\] and every ergodic \(f\)-invariant probability measure has total real Lyapunov exponent, counted with multiplicity, equal to \(\log d\). Thus a smooth expanding covering with even one periodic orbit violating the determinant law cannot be holomorphic expanding for any compatible complex structure.

## Assumptions and scope
The manifold \(X\) is compact, connected, and complex, and \(f\) is holomorphic and expanding in the sense used by Zhang: there is a Riemannian metric and \(\lambda>1\) for which \(\|D_xf(v)\|\ge \lambda\|v\|\) for all tangent vectors. Such a map is a finite covering, and \(d=\deg(f)\) denotes its positive topological degree.

The determinant statements concern the real derivative on the oriented real tangent bundle; because \(f\) is holomorphic, \(\det_{\mathbb R}D_pf^n=|\det_{\mathbb C}D_pf^n|^2>0\). The Lyapunov statement is only about the sum of the real Lyapunov exponents with multiplicity. It does not assert that the individual exponents are independent of the invariant measure.

## Proof
Zhang proves that \(f\) is biholomorphically conjugate to a holomorphic affine expanding endomorphism \(\alpha:N\to N\) of a complex infra-nilmanifold \(N=\Pi\backslash G\). After the affine normalization in the source, \(\alpha\) is induced by an expanding Lie-group automorphism \(A:G\to G\), and the complex structure on \(G\) is left invariant while every element of \(\Pi\) acts biholomorphically.

Choose a positive left-invariant real top-degree form \(\eta\) on \(G\). Write \(\Gamma=\Pi\cap G\). The holonomy group \(\Pi/\Gamma\) is finite. The linear part of each deck transformation is complex linear and has finite order in the holonomy group, hence its real determinant is positive and has finite multiplicative order; therefore that determinant is \(1\). Left translations also preserve \(\eta\). Thus \(\eta\) is \(\Pi\)-invariant and descends to a smooth positive volume form \(m_N\) on \(N\).

Since the vector space of top-degree left-invariant forms is one dimensional, \(A^*\eta=c\eta\) for the positive constant \(c=\det_{\mathbb R}(D_eA)\). Hence \(\alpha^*m_N=c\,m_N\). Integrating over \(N\) and using that \(\alpha\) is an orientation-preserving covering of degree \(d\) gives
\[
 c\int_Nm_N=\int_N\alpha^*m_N=d\int_Nm_N,
\]
so \(c=d\). If \(h:X\to N\) is Zhang's biholomorphic conjugacy, then the normalized pullback \(m=h^*m_N\) satisfies \(f^*m=d\,m\).

Now let \(m_0\) be any smooth positive volume form and write \(m=e^u m_0\) after absorbing a constant into \(u\). By the definition of the Jacobian relative to \(m_0\),
\[
 f^*m=e^{u\circ f}J_{m_0}f\,m_0=d e^u m_0,
\]
and therefore
\[
 \log J_{m_0}f-\log d=u-u\circ f.
\]
If \(f^n(p)=p\), summing this identity around the orbit telescopes and yields \(\log J_{m_0}(f^n)(p)=n\log d\). At a periodic point source and target tangent spaces coincide, so this Jacobian is exactly \(\det_{\mathbb R}(D_pf^n)\), independently of the auxiliary volume form. Holomorphicity gives the complex-determinant formulation.

Finally, for any ergodic invariant probability \(\mu\), Oseledets' theorem applied to the smooth local diffeomorphism gives
\[
 \sum_j\lambda_j(\mu)=\int_X\log J_mf\,d\mu=\log d,
\]
where the real Lyapunov exponents are counted with multiplicity. No limiting experiment is used: the equality follows from the pointwise identity \(J_mf=d\).

## Verification
The critical steps were checked directly against the structural conclusion and proof of Zhang's Theorem A: the conjugacy is biholomorphic, the normalized affine model is induced by an expanding Lie-group automorphism, the complex structure on \(G\) is left invariant, and the full deck group acts biholomorphically. The determinant calculation then uses only finite holonomy, one-dimensionality of top exterior powers, the covering-degree change-of-variables identity, and telescoping of a smooth coboundary.

Boundary checks were also made. The argument needs compactness and connectedness as in the source. It uses the real topological degree, which is positive for a holomorphic covering. It proves only a total Lyapunov-sum law, not equality of individual exponents. The infra-nilmanifold holonomy may change individual return spectra, so no stronger periodic-spectrum statement is inferred.

## Relationship to prior work
Zhang's 2026 theorem supplies the biholomorphic affine classification but does not state a smooth constant-Jacobian volume, the smooth Jacobian cohomology equation, the exact periodic determinant identity, or the universal Lyapunov-sum consequence. The source itself emphasizes that periodic derivative data obstruct smooth conjugacy for general expanding maps; the determinant identity above isolates a scalar part of that periodic data that holomorphic expansion forces to be completely rigid.

The classical Shub--Franks--Gromov classification gives only a topological conjugacy for general expanding maps, so it cannot transfer this differentiable periodic-data identity. Spatzier--Yang obtain smooth affine classification in a genuinely higher-rank commuting setting, not for an arbitrary single holomorphic expanding map. Bowen's entropy work calculates entropy for affine maps on Lie groups and homogeneous spaces but does not state the present Jacobian-coboundary or periodic determinant criterion for holomorphic expanding maps.

## Limitations
The claim does not classify individual Lyapunov exponents, periodic eigenvalues, invariant measures, or entropy-maximizing measures. It also does not assert a converse: satisfying \(\det_{\mathbb R}(D_pf^n)=d^n\) on every periodic orbit is only a necessary condition for holomorphic realizability, not a sufficient one. An equivalent formulation could exist in unindexed literature on Jacobian Livšic rigidity for expanding maps; targeted searches did not locate one, so that remains the principal originality risk.

## References
1. J. Zhang, *Holomorphic expanding maps*, arXiv:2610.01525v1, first submitted 2026-10-01.
2. M. Shub, *Endomorphisms of compact differentiable manifolds*, American Journal of Mathematics 91 (1969), 175--199.
3. J. Franks, *Anosov diffeomorphisms*, Proceedings of Symposia in Pure Mathematics 14 (1970), 61--93.
4. M. Gromov, *Groups of polynomial growth and expanding maps*, Publications Mathématiques de l'IHÉS 53 (1981), 53--78.
5. R. Spatzier and L. Yang, *Exponential mixing and smooth classification of commuting expanding maps*, Journal of Modern Dynamics 11 (2017), 263--312, DOI:10.3934/jmd.2017012.
6. R. Bowen, *Entropy for group endomorphisms and homogeneous spaces*, Transactions of the American Mathematical Society 153 (1971), 401--414, DOI:10.1090/S0002-9947-1971-0274707-X.
