# Independent mathematical audit

## correctness

PASS

For fixed prime ell, multiplicativity yields nu_ell(sigma(n))=sum_{p^e||n}nu_ell(sigma(p^e)). For e=1, local term nu_ell(p+1). For e>=2, 0<=nu_ell(sigma(p^e))<=(e+1)log(p)/log(ell) and nu_ell(p+1)<=log(p+1)/log(ell), so |difference|<=C_ell e log p; averaging over n<=x bounds the error by C_ell sum_p sum_{e>=2} e log p / p^e<infinity, hence error/loglog n converges to 0 in density. For each fixed J, g_{ell,J}(n)=sum_{p|n}min(nu_ell(p+1),J) is strongly additive; min= sum_{j<=J}1_{p=-1 mod ell^j}. Each fixed reduced progression has reciprocal prime sum (1/phi(ell^j))loglog x+O(1); Turan-Kubilius variance is O_{ell,J}(loglog x), implying density concentration at c_{ell,J}loglog n. For j>J, mean of nonnegative tail is bounded by sum_{j>J}sum_{p<=x,p=-1 mod ell^j}1/p. Uniform Brun-Titchmarsh for ell^j<=x^delta gives O_{ell,delta}(ell^{-J}loglog x); for larger ell^j elementary harmonic counting of p=k*ell^j-1 gives O(log x * x^{-delta})=o(1); Markov then J->infinity. Sum_{j>=1}1/phi(ell^j)=ell/(ell-1)^2, including ell=2 with coefficient 2. n with n<=x^a has density 0 for any fixed 0<a<1, justifying loglog n versus loglog x. This reconstructs the proof, not merely finite tests. Local inequality and all quantifiers verified for fixed ell only. Independent six-entry Git tree SHA recomputation matches f43753a0c914926d2fb1d041e93d18a9327de179. Prior small-n arithmetic checks are only corroboration; no false finite-to-infinite inference.

## originality

PASS

Best-of-knowledge claim-specific novelty, qualified: the exact fixed-prime density-one normal-order coefficient ell/(ell-1)^2 for nu_ell(sigma(n)) was not established by the inspected primary full texts, OEIS valuation table, or Resultary semantic matches. Local p-adic formulas, unconditional pointwise upper bounds, and normal orders for omega(s(n))/Omega(s(n)) are prior and are not claimed as new. Applying classical Turan-Kubilius to a specifically constructed strongly additive proxy is the proof method; priority could be subsumed by an older general theorem or neglected literature. Search absence does not prove originality.

## value

PASS

The fixed-prime exponent of the natural multiplicative sum-of-divisors function is a motivated arithmetic statistic. The exact typical coefficient ell/(ell-1)^2 quantifies density-one prime-adic divisibility, distinguishes ell=2 from odd primes and relates it to the hierarchical arithmetic progressions p=-1 mod ell^j. This is more than a known local table and supplies an independently useful leading constant; no downstream general theorem or paper-scale requirement is imposed. Standard proof tools and the possibility of earlier general coverage limit claims of scope but do not alone negate the mathematical utility. It does not claim an exceptional-set rate, fluctuations, or uniformity in ell.

The dated certificate retains the supplied scientific assessment, sources and limitations.
