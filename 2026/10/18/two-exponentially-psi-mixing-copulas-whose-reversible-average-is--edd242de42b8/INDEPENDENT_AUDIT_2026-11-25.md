# Independent mathematical audit

## correctness

PASS

The deterministic transport takes Lebesgue mass on I_0 onto I_1. The other two cells each send half their mass uniformly into I_0 and I_2, so Lebesgue is invariant and reversal gives exactly R. The average kernel is therefore reversible. For each component, every path of length two has a uniform draw within some cell; subsequent deterministic translation or a new draw preserves uniformity conditional on the cell. At n≥2 this gives block densities 3(M^n)_{ij}, and rectangles of full cells attain the largest absolute density deviation from one. In the stated matrix, max|3(M²)_{ij}−1|=1 and M(M²−J)=−(M²−J)/2, giving exactly 2^(2−n); reversal transposes the stationary joint law and preserves ψ. The endpoint coefficient agrees with the full past/future definition: condition the past event on X_0 and the future event on X_n; integrating the nonnegative conditional weights preserves the relative-probability bounds, and endpoint events attain or approximate the endpoint supremum. For the mixture, the alternating word of length n starting with P has weight 2^(−n), and maps a subinterval of I_0 of length ε onto itself or its translate. The joint-to-product ratio is at least 2^(−n)/ε, hence infinite in supremum for each n≥1. Both components also have infinite one-step ψ; the usual definition requires convergence to zero rather than finiteness at lag one. Every entry of M³ is at least 1/4, so the all-P word gives Q³≥(1/8)(3/4)μ=(3/32)μ pointwise. Doeblin splitting and contraction give the uniform geometric TV bound, including intermediate times. The copulas have singular parts, and no claim for an absolutely continuous subclass is made. Read VERIFICATION.md and the finite exact-arithmetic verifier without executing the supplied script; the all-lag conclusions come from the recurrence and interval probability argument.

## originality

PASS

The result is an explicit counterexample to the unrestricted copula-mixture closure question under the usual two-sided ψ coefficient. Relevant positive results require one-step or density bounds that do not hold, or concern lower ψ. A general published assertion of closure has an invalid inference in the inspected proof, not a matching valid theorem or an equivalent counterexample. The related Doeblin example shows arbitrarily delayed but eventual finite ψ, not persistence under reversal symmetrization.

## value

PASS

The construction answers a documented closure question and shows that failure survives both reversibility and strong Doeblin control. Its transparent mechanism explains why exponential disappearance of a singular branch in total variation need not reduce a relative error tested on arbitrarily rare events. The exact component coefficients and explicit minorization make that contrast quantitatively checkable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
