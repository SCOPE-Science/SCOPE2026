# Independent mathematical audit

## correctness

PASS

The map x=−cot(πu) has Jacobian π csc²(πu); multiplication by the tilted Gaussian density yields exactly g_a and integral (2γ)^(−1/2). Near zero, cot²(πu)=(πu)^(−2)−2/3+O(u²), so g_a∼(√(π/2)e^(2γ/3)/π²)u^(−2)exp(−γ/(π²u²)), with the same behavior at one by reflection. On complex disks of radius κu about small positive u the real part of cot² is bounded below by b/u², and the csc² factor by C/u² in modulus. Cauchy's estimates give C r! κ^(−r) u^(−r−2) exp(−bγ/u²); for fixed r the bound tends to zero, justifying all flat endpoint derivatives, and maximization over u gives A B^r(r!)^(3/2) using Stirling. Uniform analytic disks handle the compact interior. Flatness and Taylor remainders for a putative order 1<s<3/2 give |g_a(u)|≤A(Bu)^r(r!)^(s−1) for every r, and optimizing forces exp(−b u^(−1/(s−1))), incompatible with the positive asymptotic. Monotonicity in s excludes orders ≤1 as well. Absolute Fourier convergence allows the n-point sum to retain only frequencies ℓn; Parseval in the one uniform U proves the exact variance and zero-frequency unbiasedness. Integration by parts with r proportional to |k|^(2/3) gives stretched-exponential coefficients; in the variance sum one can split the exponent using n^(2/3)|ℓ|^(2/3)≥(n^(2/3)+|ℓ|^(2/3))/2. Conversely RMS dominates |ĝ(n)| at each n. If a faster envelope held, reality would give it on both signs of k; splitting the exponent in half and maximizing x^r exp(−c x^β/2) proves a derivative bound of order 1/β (or use any smaller β still above 2/3). Finitely many possible exceptions could be absorbed by increasing the prefactor, so failure is infinite, not necessarily at every n. The finite floating-point verifier was inspected, not run, and cannot prove the rates.

## originality

PASS

The cotangent mapping and shifted trapezoid framework are established; applying the same map to the tilted Gaussian is exactly a Möbius trapezoid. The inspected sources do not establish or mechanically imply this integrand's exact Gevrey order and the sharp fixed-count RMS envelope. Value and novelty attach to that exact rate characterization, not the mapping, alias identity, or use of Gevrey theory itself.

## value

PASS

The result tells a user of the existing Möbius rule exactly what speed can be guaranteed, uniformly over sample sizes, for a natural unbounded Gaussian moment. It separates strict stretched-exponential behavior from both the weaker superalgebraic statement and an unattainable exponential envelope. Using exact flatness to rule out faster convergence avoids inferring a lower bound from finite samples or assuming that oscillatory Fourier terms have uniform pointwise size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
