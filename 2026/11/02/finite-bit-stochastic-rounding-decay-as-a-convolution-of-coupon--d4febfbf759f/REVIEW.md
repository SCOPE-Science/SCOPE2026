# Independent mathematical audit

## correctness

PASS

For the specified fixed-grid decrement scheme q_j=floor(Kj/N)/K, where N=2^p and K=2^r, independent geometric holding times at successive states give absorption at (N/K−1)/N for r<p and at zero for r≥p. For r≤p, L=N/K, the multiset of holding parameters is q_N=1 plus L copies of l/K (1≤l<K), yielding τ ≡ sum_{a=1}^L C_K^{(a)}−L+1. Sums of geometric means and variances give Eτ=1+NH_{K−1} and Varτ=NKH_{K−1}^{(2)}−NH_{K−1}. For r≥p, q_j=j/N so hitting time is C_N. Classical coupon-collector limit and variance bound prove fixed-deficit average-Gumbel and double-divergence concentration at gamma, respectively. Only exact independent decrement-rounding is asserted.

## originality

PASS

General stochastic-rounding bias studies and classical coupon-collector laws do not identify this finite-state dynamics/convolution for a truncated-random-bits Euler decrement. The all-(p,r) exact absorbing plateau and two-parameter fluctuation split are specific, best-of-knowledge results.

## value

PASS

The model isolates a practical and mathematically sharp distinction between state precision and random-bit precision, turning a qualitative rounding-stagnation concern into an exact absorbing state, full hitting-time distribution, and non-Gumbel crossover. The scheme is explicitly bounded and not confused with IEEE or state-rounding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
