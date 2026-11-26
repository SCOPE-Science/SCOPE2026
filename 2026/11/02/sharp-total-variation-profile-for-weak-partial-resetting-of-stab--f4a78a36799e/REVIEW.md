# Independent mathematical audit

## correctness

PASS

Independently reconstructed the weak-contraction expansion. Along a two-sided Poisson process the stationary age and earlier gaps are iid Exp(1); the stable increments across those intervals have characteristic exponents weighted by c^(jα). The sum of conditional stable scale times is almost surely finite, yielding the stationary scale mixture with normalized time V=δ Σ_j (1−δ)^j E_j. Coupling two initial states with the same resets and noise multiplies their difference by c to the number of resets, which tends to zero, proving uniqueness. The weights sum to one; sums of their rth powers times (r−1)! give the cumulants, so Var(V)=δ/(2−δ) and E(V−1)^4=3 Var(V)^2+6δ^4/(1−(1−δ)^4)=O(δ²). Hence E|V−1|³=O(δ^(3/2)). The needed three L1 derivatives in v can also be justified without the cited stable tail estimate: subordinate the Gaussian p_(2,s) with s=v^(2/α)T where T has Laplace transform exp(−u^(α/2)) (T=1 for α=2). Gaussian scaling gives ||∂_s^j p_(2,s)||_1=const_j s^(−j); after the chain rule the factors T^j cancel these negative powers of T, providing uniform L1 domination on [1/2,3/2]. The first Taylor term averages to zero and the quadratic term has exact coefficient Var(V)/2. Outside the interval, 2 bounds the density difference in L1 and the constant, linear and quadratic tail contributions are all O(δ²) by the fourth moment and |V−1|>1/2. Fourier differentiation gives the stated K_α, nonzero but integral zero, hence sign-changing. For Cauchy, a primitive of K_1 is 2x/[π(1+x²)²] and the sign boundary is 1/√3. For Gaussian, K_2=p_2 H_4(x/√2)/4 and the boundary contributions from −H_3 φ at a and b give ||K_2||_1=√6[aφ(a)+bφ(b)]. Halving the density error yields ||K_α||_1 ε_c/4 plus the stated remainder. The index is fixed; no uniformity or finite state variance for α<2 is needed. Inspected the frozen verification/check.py and its 171-assertion saved output without executing the upload; finite Fourier checks do not certify the L1 remainder.

## originality

PASS

The assessed contribution is the sharp first correction in L1 as the contraction approaches one, with the nonzero TV coefficient and endpoint constants. The reset process, stationary mixture, and Taylor method are not independent novelty claims. The closest checked work treats either a different convergence parameter, a different spatial regime, or moments rather than this correction to the full law.

## value

PASS

Weak resetting is a natural singular limit of the stationary family. The signed L1 correction gives the first measurable error in replacing a random operational time by its mean, valid even when the stable state lacks a variance. Strict positivity of the TV coefficient makes the order sharp, and the two tractable endpoints supply exact benchmarks not available from characteristic-function convergence alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
