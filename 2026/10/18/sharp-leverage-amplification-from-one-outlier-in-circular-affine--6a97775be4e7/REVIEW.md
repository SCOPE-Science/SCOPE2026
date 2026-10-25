# Independent mathematical audit

## correctness

PASS

PASS. The original n-gon design has Gram diag(n,n/2,n/2). Sherman--Morrison rank-one inversion for the added row (1,Rcosφ,Rsinφ) yields exact outlier H_{*,*}=(1+2R²)/D and H_{*,j}=(1+2Rcos(2πj/n−φ))/D, D=n+1+2R², giving M_n by signed row sums. Old-row leverage H_jj<=3/n implies the uniform ℓ∞ row bound sqrt(3(n+1)/n). Independent direct 3x3 Gram inversions checked the outlier row formula and old-row bound in 12 finite configurations. Shifted circle bounded-variation quadrature has uniform |S−nm(R)|<=8R and differentiated O(1) error away from upward absolute-value cusps. At radius R=ρ√n the leading profile 4ρ/[π(1+2ρ²)] uniquely peaks at ρ=1/√2, dominating all old rows; its next term 2ρ²/(1+2ρ²) yields +1/2. The stationary equation reduces to n−2R²+πR=O(1), giving every maximizing R=√(n/2)+π/4+O(n^−1/2), uniformly φ. Cusp derivatives jump upward so no local maxima occur there. No finite-n uniqueness claimed and finite checks are not a proof of asymptotics.

## originality

PASS

PASS best-of-knowledge for the optimized rank-one contaminated circular design, uniform two-term amplification and all-maximizer radius. Prior cyclic projector norms concern the uncontaminated design and general regression leverage literature does not logically dominate the specific endpoint asymptotic.

## value

PASS

PASS. It identifies the exact high-leverage instability of a canonical balanced sample under bounded response noise, the optimal outlier distance, and a universal second-order intercept, distinguishing a natural adversarial ℓ∞ stability problem from stochastic single-point influence and ordinary bounded cyclic projection norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
