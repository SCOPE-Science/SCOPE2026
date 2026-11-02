# Independent mathematical audit

## correctness

PASS

Uniform chord diagrams on 2n labeled circular endpoints have X_n mean n(n-1)/6 and variance n(n-1)(n+3)/45 as in published crossing CLT. Conditioning on any fixed K pairwise endpoint-disjoint chords leaves uniform matching of remaining endpoints; deleting marked chords preserves crossing relation among survivors, and each chord of length j has <=j crossings. Thus X_n=X_{n-K}+R, 0<=R<=KJ, uniformly for fixed K,J. The known Paguyo Kolmogorov O(n^-1/2) bound for crossings transfers after deterministic means/variances differ by O_K(n), while sigma_n grows order n^(3/2), giving conditional O_{K,J}(n^-1/2). For K zero-length chords R=0 exactly. Ordered k-tuples of disjoint cycle-adjacent pairs number N_{n,k}=[2n/(2n-k)](2n-k)!/(2n-2k)!; each occurs with matching probability product_{h=0}^{k-1}(2n-(2h+1))^-1, proving factorial deletion for every bounded h and 0<=k<=n. For fixed lengths j<=J, O(n^{K-1}) overlapping arrays of O(n^K) total candidates are negligible; mixed factorial moments conditioned on a bounded continuous test f(W_n) factor, and multivariate Poisson moment determinacy yields independence from Z. Independently enumerated 3,15,105,945,10395 pairings for n=2..6, comparing all k factorial deletion identities by exact integer distribution coefficients. Infinite CLT relies explicitly on Paguyo, not finite tests. Inspected RESULT.md ee ad3e... and verify.py blob 109319..., plus status sources.

## originality

PASS

Acan Theorem 4.2 gives jointly independent Poisson local chord counts; Paguyo Theorems 1.1-1.2 give separately crossing normal and short-chord Poisson estimates. Neither conclusion alone implies their mutual Gaussian-Poisson independence. This result adds a uniform conditional CLT for any prescribed bounded-length finite chord collection and exact zero-length factorial deletion. The earlier Flajolet–Noy chapter may contain a broader mixed enumeration and remains a named priority risk, not an automatic O rejection.

## value

PASS

Joint Gaussian–Poisson asymptotic independence of macroscopic crossing fluctuations from local short chords gives a meaningful new multiscale structural fact; the exact deletion identity strengthens this by a finite-n distributional transform and a uniform conditioning estimate. Natural probabilistic statistics, not a posthoc single small case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
