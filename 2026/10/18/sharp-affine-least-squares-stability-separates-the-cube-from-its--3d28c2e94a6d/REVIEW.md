# Scientific review

## Correctness
**PASS.** The reproducing kernel is reconstructed from the full affine Gram matrix and scalar covariance, with normalized volume specified. Convexity reduces each evaluation supremum to vertices. The cross-polytope marginal is a normalized Beta density; its integral is exact. The cube formula follows from the Irwin--Hall distribution and a one-sided positive-part integral, checked independently. Equality at dimensions one and two and the ten exact positive finite gaps are certified rationally; for every larger dimension strictness follows from Bernoulli and Cauchy--Schwarz inequalities. The CLT is accompanied by a uniform second-moment bound guaranteeing passage to absolute moments. The accompanying checker passed 365 assertions.

## Originality
**PASS, subject to an explicit residual literature risk.** Barthe--Guédon--Mendelson--Naor provide the normalized \(\ell_p\)-ball law and moment estimates, which already yield order-of-growth context; that context is not claimed new. Hangelbroek--Narcowich--Sun--Ward establish least-squares projector boundedness under localization hypotheses rather than the present exact affine-volume calculation. The closest published simplex projector result uses a different domain and does not imply the exact dual-body formulas. The candidate's claimed contribution is the **paired exact constants**, all-dimensional **equality-versus-strictness classification**, and **sharp asymptotic ratio**. An older equivalent polynomial Lebesgue-constant computation may have escaped the searches.

## Value
**PASS.** Least-squares projection onto affine functions is a basic local approximation operation whose sharp \(L^\infty\) stability and failure to preserve positivity matter for worst-case bounds. The cube and its polar cross-polytope are the natural two extreme coordinate bodies, coinciding up to affine equivalence in dimensions one and two but behaving differently in higher dimensions. Exact endpoint values, the first strict dimension, and an unbounded asymptotic stability ratio identify a structural distinction not supplied by moment-order estimates. The result is a natural full-dimensional classification, not an arbitrary parameter slice or a small improvement to a prior numerical bound.

## Closest sources and limitations
Primary full-text passages inspected: Barthe et al. (2005), probabilistic representation and Khinchine/moment sections; Hangelbroek et al. (2010), localization assumptions and least-squares projection sections. The published simplex statement and proof were inspected, including its kernel and extremal-mass argument. This result does not determine projectors of higher polynomial degree, optimize over all possible projectors, or assert a polarity ordering for general convex bodies. Human bibliographic verification remains necessary to exclude an older equivalent formula.

Self-review: passed. Independent audit: not yet performed.
