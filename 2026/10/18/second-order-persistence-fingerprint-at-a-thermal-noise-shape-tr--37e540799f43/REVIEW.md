# Scientific review

## Correctness — PASS
The stationary distribution is the known Gaussian convolution of the beta law with exponent \(\ell-1\). The critical root exists uniquely because \(F(0)=-1\), \(F(t)\sim(1-\ell)/t>0\) and \(F\) has strictly positive derivative at every root. The tilted-beta recurrence explicitly supplies its second and third moments. Gaussian Hermite differentiation gives \(P^{(4)}(0)/P(0)=2(\ell-1)/\nu_c^2<0\) and \(P^{(6)}(0)/P(0)=2(\ell-1)[1+(2\ell-9)\nu_c]/\nu_c^4\). The heat equation and analytic implicit-function theorem then give the asserted second-order mode law. The smooth Gaussian kernel's variation-diminishing property bounds the number of stationary modes; independent quadrature checks reproduce both signs of the next-order coefficient. The proof does not depend on numerical evidence.

## Originality — PASS, with residual risk
The beta stationary density, exact convolution, qualitative transition, critical curvature equation, and its endpoint behavior are prior results, especially Guéneau–Majumdar–Schehr (arXiv:2602.08436, Sec. V.1.1, Eqs. 96–98). The universal leading square-root coefficient is a generic heat-equation consequence and not claimed novel. The assessed claim is the explicit, *model-specific next coefficient* \(K(\ell)\) together with its qualitative sign reversal as the persistence ratio changes. The inspected full section of the closest source and the telegraphically driven-trap paper's shape-transition treatment do not state this second-order expansion; targeted research-record searches found no equal or dominating published claim. Residual risks include an implicit treatment in another source, the inaccessible full text of Sevilla–Meléndez Mora (arXiv:2608.21781), and a general heat-flow expansion that could render the calculation an application of prior higher-order theory.

## Value — PASS
Near the established morphology transition, the leading peak separation is universal, so it cannot distinguish different directional switching rates once the threshold is known. The calculated first correction is the lowest-order coefficient that detects persistence, and its sign changes between rare and frequent tumbling. This supplies a natural quantitative boundary for fitting stationary spatial peaks and interpreting activity, not an arbitrary parameter slice. Its value does not require a new general theorem for all noise-smoothed distributions; no claim of statistical robustness under noise is made.

## Scope and caveats
The result is a local stationary asymptotic for every fixed \(0<\ell<1\); it is not uniform at either endpoint. The zero of the correction is only proved to exist. No independent mathematical audit has been carried out. The strongest relevant published formulas remain prior work, and full coverage of all possible related literature is not certified.

Self-review: passed. Independent audit: not yet performed.
