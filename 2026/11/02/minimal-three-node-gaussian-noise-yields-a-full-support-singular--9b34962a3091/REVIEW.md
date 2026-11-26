# Independent mathematical audit

## correctness

PASS

The recursion uses the exact OU drift coefficient and innovation variance, not the exact Gaussian transition. The three-atom rule has odd moments zero and even moments 1,3,9 at degrees 2,4,6. A one- or two-atom rule cannot be exact through degree four because the square of its vanishing polynomial would integrate to zero instead of a positive Gaussian value. For three atoms, the monic vanishing cubic is Gaussian-orthogonal to degrees 0–2 and hence is t^3-3t; the remaining linear moment equations fix the weights. Contraction gives the unique stationary innovation series. Finite series match all joint monomials of total degree <=5 by independence, and geometric L^5 convergence passes those identities to the stationary process at any finite set of grid times. The sixth cumulant is -6 v^3(1-r^2)^3/(1-r^6); exact rational evaluation at r=1/3 yields -384v^3/91 and centered moment 981v^3/91. The balanced ternary series at that r has support [-sqrt(6v),sqrt(6v)] because every ternary cylinder has positive mass, has no atoms since any point has at most two codings and prefix probabilities are <=(2/3)^n, and is singular by the disjoint almost-sure digit frequency vectors for its law and Lebesgue measure. Thus TV as defined is one. Typical cylinder masses have exponent H/log(3); counting typical cylinders gives the upper dimension, and a restriction of positive measure with cylinder mass bounded above by 3^(-ns) uniformly for large n gives the lower bound for every s<H/log(3), since short intervals meet at most two cylinders at comparable scale. The dimension of the measure is 0.789690082143 to the stated precision. For the support frontier r>=1/3 exactly makes the three first-level intervals touch or overlap; below it they are separated. The supplied verify.py was inspected but not executed; the analytic series and entropy arguments establish the infinite claims independent of those finite checks.

## originality

PASS

The Gaussian quadrature and biased-ternary measure facts are classical. The supported distinct claim is the scalar stationary numerical OU counterexample combining interval support, maximal TV error, and exact joint moments through degree five, with the first mismatch quantified. Neither the inspected numerical schemes nor the closest indexed invariant-law, covariance or ternary examples establish that combination.

## value

PASS

A scalar OU grid is a natural setting to test whether fitting finite moments controls a stationary law. The minimal Gaussian moment rule reaches the tight boundary at which every interval subcylinder is occupied, yet yields TV error one while matching joint grid moments through degree five. This isolates a concrete failure of invariant-law fidelity that is stronger than merely non-Gaussian noise or an obvious gap in support. It does not claim a small-step theorem or novelty for Gaussian quadrature or biased ternary measures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
