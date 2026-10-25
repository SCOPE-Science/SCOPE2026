# Next-order large-\(p\) capacity asymptotics for model manifolds

## Finding

Let \(M^m\) be a complete rotationally symmetric Riemannian manifold with pole \(o\), and write
\[
S(r)=\operatorname{Area}(\partial B(o,r)).
\]
Suppose that, as \(r\to\infty\),
\[
S(r)=C r^k e^{hr}\bigl(1+O(r^{-1})\bigr),
\qquad C>0,\quad h>0,\quad k\geq0.
\]
For every fixed radius \(R>0\), define
\[
Q_p(R)=(p-1)h^{\frac{m-1}{p-1}-1}
\operatorname{Cap}_p(B(o,R))^{\frac{1}{p-1}},
\]
where \(\operatorname{Cap}_p\) is the \(p\)-capacity of a compact ball in the complete manifold. Then
\[
\boxed{
Q_p(R)=1+
\frac{k\log(p-1)+\log\!\left(C h^{m-1-k}\right)+hR-k\gamma_{\mathrm E}}
{p-1}
+o(p^{-1})
}
\qquad (p\to\infty),
\]
where \(\gamma_{\mathrm E}\) is Euler's constant. The factor \(C h^{m-1-k}\) is dimensionless and invariant under a constant rescaling of the metric. Thus the next coefficient after the universal logarithmic term records the asymptotic sphere-area amplitude and the fixed ball radius.

## Assumptions and scope

The manifold is complete and rotationally symmetric about \(o\), so the capacity of a centered ball is given by the radial \(p\)-harmonic potential. The sphere-area hypothesis is a relative asymptotic expansion with an \(O(r^{-1})\) error, not merely a two-sided comparability \(S(r)\asymp r^k e^{hr}\). The parameters \(m,C,h,k\) are fixed, and \(R\) does not depend on \(p\). The conclusion does not assert the existence of this sphere-area expansion for every model manifold, nor does it cover non-radial manifolds whose ball capacities are not represented by the radial integral.

## Proof

Put \(\varepsilon=(p-1)^{-1}\) and
\[
I_\varepsilon(R)=\int_R^\infty S(t)^{-\varepsilon}\,dt.
\]
The radial \(p\)-harmonic potential outside \(B(o,R)\) has derivative
\[
u'(t)=-\frac{S(t)^{-\varepsilon}}{I_\varepsilon(R)}.
\]
Its energy is \(I_\varepsilon(R)^{1-p}\), hence
\[
\operatorname{Cap}_p(B(o,R))^{\varepsilon}=I_\varepsilon(R)^{-1}.
\]
For the model integrand \(C^{-\varepsilon}t^{-k\varepsilon}e^{-h\varepsilon t}\), substitution \(z=h\varepsilon t\) gives
\[
I_\varepsilon^{\mathrm{mod}}(R)
=C^{-\varepsilon}(h\varepsilon)^{k\varepsilon-1}
\Gamma(1-k\varepsilon,h\varepsilon R),
\]
where \(\Gamma(s,z)=\int_z^\infty t^{s-1}e^{-t}\,dt\) is the upper incomplete gamma function. The relative error \(O(t^{-1})\) in \(S(t)\) changes \(h\varepsilon I_\varepsilon(R)\) by \(O(\varepsilon^2\log(1/\varepsilon))=o(\varepsilon)\): on bounded intervals the difference of the two \(-\varepsilon\)-powers is \(O(\varepsilon)\), and on the tail its integral is bounded by a constant times \(\varepsilon\int_T^\infty t^{-1}e^{-h\varepsilon t}dt\). Thus this error is below the coefficient being computed.

As \(\varepsilon\downarrow0\), the standard expansion of the gamma function at \(1\), together with \(h\varepsilon R\to0\), yields
\[
\Gamma(1-k\varepsilon,h\varepsilon R)
=1+k\gamma_{\mathrm E}\varepsilon-hR\varepsilon+o(\varepsilon).
\]
Consequently,
\[
Q_p(R)=
\frac{C^\varepsilon h^{(m-1-k)\varepsilon}\varepsilon^{-k\varepsilon}}
{\Gamma(1-k\varepsilon,h\varepsilon R)}
\bigl(1+o(\varepsilon)\bigr).
\]
Taking logarithms and using
\[
\varepsilon^2\log^2(1/\varepsilon)=o(\varepsilon)
\]
in the exponentiation step gives
\[
\log Q_p(R)=
\varepsilon\left[
k\log(1/\varepsilon)+\log(C h^{m-1-k})+hR-k\gamma_{\mathrm E}
\right]+o(\varepsilon).
\]
Since \(\varepsilon=(p-1)^{-1}\) and \(\log(1/\varepsilon)=\log(p-1)\), exponentiating proves the stated expansion. No finite computation is used as proof.

## Verification

The radial capacity identity is stated in the primary literature on large-\(p\) asymptotic geometric quantities and is also given for hyperbolic annuli in the hyperbolic-capacity literature. The proof above derives the next coefficient from that identity under the stronger relative sphere-area expansion. As a normalization check, in curvature-\(-1\) hyperbolic space of dimension \(m\),
\[
S(r)=\omega_{m-1}\sinh^{m-1}r
=\omega_{m-1}2^{-(m-1)}e^{(m-1)r}(1+O(e^{-2r})),
\]
so \(h=m-1\), \(k=0\), and \(C=\omega_{m-1}2^{-(m-1)}\); the formula reduces to the direct expansion of the exact radial integral. This specialization is a consistency check, not a separate novelty claim.

## Relationship to prior work

Jin and Yin prove a large-\(p\) expansion whose logarithmic coefficient detects geometric rank, with the remaining term bounded by \(O(p^{-1})\). Their proof uses two-sided sphere-growth bounds and does not state the coefficient of that remainder. The present theorem assumes the stronger asymptotic \(S(r)=Cr^k e^{hr}(1+O(r^{-1}))\) and resolves the next coefficient explicitly. Jin and Xiao provide exact radial capacity formulas in hyperbolic space; that is a special case, not the general model-manifold statement here. The radial capacity identity and the incomplete-gamma expansion are established tools; novelty is claimed only for the stated prefactor-sensitive asymptotic under the explicit hypothesis.

## Limitations

The result does not prove that a given manifold has the required sphere-area asymptotic. It does not apply to arbitrary non-radial manifolds, to a radius \(R=R(p)\) varying with \(p\), or to sphere areas known only up to multiplicative constants. The exact coefficient is derived from a standard integral asymptotic and should be regarded as a focused refinement rather than a new general capacity theory. The literature search is not an exhaustive priority certification; independent audit has not been performed.

## References

1. X. Jin and J. Yin, *New Asymptotic Geometric Quantities in Riemannian Geometry and Their Geometric and Dynamical Applications*, arXiv:2604.14600v1 (first public 2026-04-16).
2. X. Jin and J. Xiao, *Sharply estimating hyperbolic capacities*, arXiv:2502.13651v1 (first public 2025-02-19).
