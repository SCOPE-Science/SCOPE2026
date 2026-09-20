# Same-model scientific review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The computation extends the source paper's translation expansion by two orders. For the translated Gaussian factor, the fourth coefficient follows from exact Gaussian differentiation for the translated ball and the standard sphere moments E[t²]=1/n and E[t⁴]=3/(n(n+2)). For the polar factor, the exact radial function ρ(u)=(1+εt)^{-1} reduces the calculation to four derivatives of the one-variable Gaussian radial primitive. Re-expansion at s=2/(n+1) gives the stated coefficients, and the quadratic terms cancel exactly.

The normalized quartic coefficient factors as
\[
-\frac{R_n(n+1)}{32n(n+2)}D_n.
\]
Its sign proof is independent of numerical computation: integration of d(r^n e^{-xr²}) at x=(n+1)/4 gives R_n>(n-1)/2, which implies D_n>0 in all n>=2. Hence the critical translated ball is strictly quartically stable.

For the nearby branch, even analyticity permits q=ε² as a local coordinate. The q-derivative has a simple nondegenerate zero at the critical parameter after the quadratic coefficient crosses sign, so the implicit-function theorem yields the unique small positive branch for s>s_c. Its radius, radial maximality and gain follow by direct substitution. Rotational invariance promotes the scalar branch to a sphere of centers. The record consistently restricts these conclusions to the translated-unit-ball family.

The algebraic coefficient identities were recomputed within the same-model review, including the critical fourth-order polar coefficient and the simplifications for the branch radius and gain.

## Originality

**PASS, to the best of our knowledge.**

Artstein-Avidan--Fradelizi--Wyczesany, arXiv:2609.18472v1, was inspected directly. Their Theorem 1.5 and Proposition 5.1 calculate the translation variation only through order ε² and prove non-optimality for σ²>2/(n+1). Their text explicitly leaves the higher-dimensional interval 1/n<σ²<=2/(n+1) unresolved. Searches within the full current text for “fourth”, “quartic”, “bifurcation”, “pitchfork”, and an ε^4 formulation returned no occurrence of the present refinement.

Broader searches covered “Gaussian volume product” together with fourth variation, quartic translation, phase transition, translated balls, and bifurcation, as well as “uncentered Blaschke-Santaló” with the same concepts. They returned the 2026 source preprint and older symmetric or functional Blaschke--Santaló literature, but no matching endpoint quartic formula or translated-ball branch law.

Cordero-Erausquin's symmetric Gaussian Blaschke--Santaló theorem is explicitly treated as prior work. It does not address the nonsymmetric translated family studied here. In dimension two, the source preprint proves a stronger global statement at the endpoint, so no global-optimality novelty is claimed there; the new content is the explicit local fourth-order mechanism and the nearby branch.

No inaccessible paper was identified as specifically likely to contain the exact endpoint expansion. The principal residual risk is the extreme recency of arXiv:2609.18472v1: a later revision or an unindexed parallel observation could add the same fourth-order computation.

## Value

**PASS.**

The source paper identifies σ²=2/(n+1) as the exact sign-change point of the translation Hessian but leaves the equality case invisible to that second-order test. The quartic formula resolves that degeneracy: translations still decrease the functional at the endpoint, and the first translated local maxima above threshold occur at a quantitatively determined square-root distance from the origin.

This gives a precise local phase portrait for the simplest nonsymmetric mode. In dimensions n>=3 it also clarifies that translations do not by themselves dislodge the ball at the unresolved endpoint, while above the endpoint their symmetry-breaking onset is supercritical with an explicit radius and gain law.

## Limitations

- Only the translated-unit-ball family is analyzed; arbitrary support-function perturbations are not.
- Endpoint translation stability does not resolve global optimality for n>=3.
- The nonzero branch is only a local maximum within translations, not among all convex bodies.
- No assertion is made about other nonsymmetric shape modes or the full shape Hessian.
- The motivating preprint is very recent, leaving residual revision and parallel-work risk.
- Cross-model review has not been performed.
