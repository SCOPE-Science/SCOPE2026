# Review

## Correctness

**PASS.** The statement reduces after a homothety to the coefficient-one relation. The farthest-point Hessian test forces a point with two positive principal curvatures on each connected component, hence forces the coefficient to be positive. For odd exponent \(p\), either branch of the relation gives \(K=c\kappa^{p+1}\ge0\), with \(K=0\) exactly when both principal curvatures vanish.

On a positive-curvature component the positive normal and the strictly increasing map \(t\mapsto t+t^p\) give a unique \(C^1\) parameter with spectrum \(\{t,t^p\}\). Away from \(t=1\), Codazzi yields
\[
\omega(e_1)=\frac{e_2t}{t(1-t^{p-1})},\qquad
\omega(e_2)=\frac{p t^{p-2}e_1t}{1-t^{p-1}},
\]
and hence the displayed formula for \(dt\wedge\omega\). These specialize exactly to Cheng's cubic structure equations. The weak Gauss identity \(d\omega=-K\,d\mu\) uses the same local reference-frame argument as in the cubic proof.

The \(t>1\) branch contradicts Stokes on a compact boundaryless positive-curvature component. In the \(0<t<1\) branch, the cutoff identity leaves a positive contribution bounded by
\[
C\delta^{p-3}\operatorname{Area}\{\delta<t<2\delta\}.
\]
For \(p=3\) the layer area tends to zero; for \(p>3\) there is additional decay. Dominated convergence simultaneously forces the cutoff curvature integral to converge to the positive total curvature of the component, giving the contradiction. Scaling back gives the forced umbilic curvature \(c^{-1/(p-1)}\). No step uses the later cubic-specific local-rigidity or completion arguments.

## Originality

**PASS, to the best of our knowledge.** Cheng's September 2026 paper was inspected at the theorem and Section 4 level. Proposition 4.3 states the componentwise nonzero-umbilic result for the cubic relation and its proof contains the \(p=3\) cutoff estimate. The paper's stated global theorem and Section 4 are cubic; no higher odd-power version of Proposition 4.3 was located.

Kühnel--Steller (2005) was inspected in the section on generalized Hopf surfaces. Their Proposition 9 constructs closed convex rotational surfaces satisfying \(\kappa=c\lambda^\alpha\), analytic exactly for odd integral \(\alpha\), and explicitly includes \(\alpha=5,7,9,\ldots\). Thus higher odd powers are established examples, not a new construction here. Their result is rotational and does not state the arbitrary \(C^3\) per-positive-curvature-component umbilic forcing theorem.

Classical Hartman--Wintner and related elliptic Weingarten sphere results were checked as possible stronger coverage. They impose regularity/nondegeneracy conditions on the Weingarten relation that do not transparently include the crossing unordered monomial relation; the existence of nonround generalized Hopf examples also rules out interpreting those results as a blanket sphere theorem for the present class.

A remaining historical risk is K. Voss, *Über geschlossene Weingartensche Flächen*, Math. Ann. 138 (1959), 42--54, whose full text was not inspected here. Kühnel--Steller describe Voss's result as rotationality of closed analytic genus-zero Weingarten surfaces. That is a different regularity and conclusion from the present \(C^3\), componentwise statement, so it is not concrete evidence of coverage, but it remains the most plausible older source capable of containing a related observation. The motivating Cheng preprint is also very recent, so a later revision or unindexed parallel observation remains a genuine originality risk.

## Value

**PASS.** The result extends the exact global ingredient that starts Cheng's cubic classification to every higher odd monomial exponent while preserving \(C^3\) regularity and allowing arbitrary compact immersions, flat regions, and disconnected positive-curvature sets. It is stronger than mere existence of an umbilic on a connected surface because each positive-curvature component must contain its own nonzero umbilic. The proof also exposes a sharp structural feature of the method: \(p=3\) is the critical cutoff exponent, while \(p>3\) gains the factor \(\delta^{p-3}\). Kühnel--Steller's analytic generalized Hopf families show that the higher-power cases are populated by nonround examples.

## Limitations

The theorem does not classify the \(p\ge5\) surfaces, does not address even exponents, and does not improve the \(C^3\) regularity threshold. Its novelty is a structural extension of a very recent cubic argument rather than a new construction of higher-power examples. Historical and very recent parallel coverage cannot be excluded completely.

**Same-model review: passed. Independent audit: not yet performed.**
