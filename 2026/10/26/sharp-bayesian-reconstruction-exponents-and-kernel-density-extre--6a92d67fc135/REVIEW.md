# Independent mathematical audit

## correctness

PASS

The nonzero constant/trailing coefficients make each N-output finite fiber have exactly 2^d input candidates, indexed by d-bit seeds, and the difference of candidates is a restriction of a finite collection of nonzero periodic bi-infinite recurrence kernels. For biased Bernoulli(q), q=min(p,1-p)<1/2, strict competitor likelihood requires >half minority bits on its kernel support; any MAP error is bounded by union of weak >=half events. The exact binomial half-tail exponent is log(1/(2sqrt(q(1−q)))); periodic support weights m_k(N+d)=rho(k)N+O(1) give the min-density coefficient alpha_Q. SLLN across the finitely many kernel differences gives shift-covariant almost-sure inversion for biased sources. For p=1/2 all 2^d seed candidates are equiprobable and e_N=1−2^(−d). Every nonzero kernel has at least one 1 in each d-window, giving alpha>=1/d; equality forces a d-periodic single-1 kernel, hence Q=1+z^d. Uniform average over all 2^d−1 nonzero recurrence states gives alpha<=2^(d−1)/(2^d−1), attained by primitive irreducible recurrences. Independent recurrence enumeration verified all 31 normalized polynomials degree<=5 and four exact rational posterior-error sandwiches. This proves the unlimited degree/rate theorem by the analytic argument, not finite samples.

## originality

PASS

Earlier additive-cellular-automaton work analyzes topological injectivity (Dow), entropy/pressure (Ban–Chang), and Gibbs/non-Gibbs properties of biased XOR output (Kari–Taati and Lőrinczi–Maes–Vande Velde). None of the materially read primary statements yields the exact finite-window entire-seed MAP exponent alpha_Q times the Bernoulli Chernoff rate plus sharp extremal alpha_Q bounds over all normalized binary rules. Generic likelihood large deviations and primitive-polynomial maximal-length sequences are well-known ingredients and not claimed new. Full Ban–Chang and Dow comparisons remain access-limited, and alternate coding-theoretic formulations may exist.

## value

PASS

For a noninjective but surjective additive cellular automaton, the information-theoretic question of whether an entire hidden seed can be recovered from a growing observation window is natural. The exact universal bias-dependent error exponent, the a.e. versus topological invertibility distinction and sharp all-degree minimum/maximum kernel-density envelopes form a complete quantitative classification with an intrinsic periodic recurrence invariant. These are substantive, not merely numerical code checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
