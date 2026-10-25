# Independent mathematical audit

## correctness

PASS

For independent weighted Bernoulli variables, Plancherel gives C(p)=(2pi)^-1 int product_i[cos^2(w_i theta/2)+u sin^2(w_i theta/2)] dtheta. In the u-polynomial expansion, every gamma_j is a sum of integrals of products of nonnegative trig squares; each product is positive except a finite zero set for positive integer w_i, establishing gamma_j>0 for all 0<=j<=m, not just tested weights. Their sum is 1 by c_i+s_i=1; gamma_0=C(1/2). Thus C increases strictly in u; -log C has unique maximum at p=1/2. Because u=1-4v, for 1<=k<=m, (-1)^k d^k C/dv^k=4^k sum_{j>=k}(j!/(j-k)!) gamma_j (1-4v)^{j-k}>0, including v=1/4 via j=k. Bounds gamma0+gamma1*u<=C<=gamma0+(1-gamma0)*u follow from 0<=u^j<=u; strict for m>=2 and interior u, equality at m=1. Central asymptotic expansion follows by log Taylor. Independently coded exact Laurent-polynomial coefficients and direct collision convolutions match and remain strictly positive for 125 integer-weight multisets (length 1..5, weights 1..4), including gamma=(5,9,15,3)/32 for (1,2,3). These finite checks corroborate, but do not establish, the all-m proof.

## originality

PASS

Best-of-knowledge distinct structural result: all positive polynomial coefficients and the all-order variance derivative hierarchy for an arbitrary overlapping weighted Bernoulli sum with a common bias, not a general Shannon result. Full primary Neunhäuserer text confirms only Shannon concavity conjecture/extreme cases, despite sharing overlap construction; Li compares Renyi orders in fair weighted sums and says bias requires a new coupling. The previously published Resultary two-coin optimizer fixes total mean of two differing biases, unlike this common-p whole profile.

## value

PASS

Arbitrary subset-sum collisions are precisely the obstruction in an active overlap-distribution entropy question. The strict positive-coefficient representation is not merely the textbook fair-coin symmetry: it yields a full hierarchy of alternating derivatives in the variance variable, global two-sided envelopes and a sharp central entropy-loss coefficient uniformly over all finite positive-weight families. These provide exact benchmark invariants for overlap studies without pretending to solve the Shannon conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
