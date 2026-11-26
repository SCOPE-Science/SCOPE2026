# Independent mathematical audit

## correctness

PASS

Every primitive signed excursion of semilength ℓ has C_{ℓ−1} shapes per sign and contributes that semilength in the matching occupation variable and one return, including at the terminal step. Thus with P(z)(1−P(z))=z the marked function is F=1/[1−u(P(x)+P(y))]. At u=1 the Catalan divided difference has coefficient C_n in each occupation. Its u-derivative is F(x,y,1)^2−F(x,y,1), giving the stated conditional mean. Subtracting adjacent coefficient rectangles leaves the positive middle Catalan sum before the center and the zero central tie for odd n; reflection gives the other half. The endpoint is C_{n+1}/C_n−1=3n/(n+2). Stirling asymptotics of the Catalan products uniformly away from the boundary convert √n times the increments to the integral of [v(1−v)]^{−3/2}/√π from t to 1−t. The uniform bound on earlier unscaled increments follows by bounding the half-sum by a constant times Σ_{s≥j+1}s^{−3/2}, so the initial δn increments contribute O(√δ) after scaling. Integrating the resulting increment profile yields (8/√π)√{t(1−t)}, including the center by the same summation. Conditional fair signs give E[A|lengths]=n/2 and E[(A−n/2)²|lengths]=H/4, H=Σℓ_i². Marking one excursion of squared length gives 2D²P/(1−2P)^2; a return mark adds the factor (1+2P)/(1−2P) for KH. Coefficients give E[H]=n(n+2)/3, E[KH]=4^{n−1}n(n+3)/binom(2n,n)−E[H], and E[K]=4^n/binom(2n,n)−1. Subtraction and the factor 1/4 yield the exact negative covariance and its stated limit. At n=1 all means equal one and both covariances vanish; at n=2 the means are (3/2,2,3/2) and quadratic covariance −1/9. Frozen verification notes and verifier were inspected, not executed. Neither the reported enumeration nor a Brownian scaling analogy is used as proof of pointwise conditioning.

## originality

PASS

Credit exact overlap in a distinct Resultary record for the signed-occupation covariance and the full marked generating function, without inferring priority from indexing dates. The supported distinct contribution is the evaluated conditional return-count profile, its discrete strict shape, and the pointwise fixed-occupation-fraction asymptotics. The indexed overlap uses the generating function to take occupation moments, not to estimate returns conditional on each occupation or to prove a conditional limit. Classical Chung–Feller, standard excursion enumeration and the covariance in isolation do not establish originality of the full profile.

## value

PASS

Uniform occupation and an unconditional return-count law do not answer how frequent zero returns are among bridges with a specified imbalance. The evaluated shape and conditional scaling distinguish a bounded endpoint mean from a √n interior mean and locate the maximizing occupations exactly. This is usable for comparing occupation-conditioned bridge ensembles; the value does not depend on the separately indexed covariance being new or on asserting any ordering of full conditional distributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
