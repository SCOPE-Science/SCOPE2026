# Independent mathematical audit

## correctness

PASS

For B_n with iid Bernoulli p, q=1−p² and s=1−2p²+p³. Each diagonal missing Boolean square entry has probability (1−p)q^(n−1); each off-diagonal missing entry has probability s q^(n−2), because k=i,j walk conditions share b_ij. Thus expected missing entries are exactly μ=n(n−1)s q^(n−2)+n(1−p)q^(n−1). For two distinct missing positions, intermediates outside at most four endpoints provide independent upper bounds s^(n−4) when source or target coincides, q^(2(n−4)) otherwise; sum over O(n³)+O(n⁴) pairs is o(μ) since 0<s<q<1. Bonferroni proves Pr(D>0)~μ; diagonal defects and multiple defects vanish relative to μ, giving unique off-diagonal defect. Conditioning on nonempty rows/columns alters probabilities by at most 2n(1−p)^n=o(μ), and simultaneous label symmetry makes unique off-diagonal position uniform. At p=1/2, s=5/8, q=3/4 and s/q²=10/9. J is absorbing for no-empty-row/column relations. Independently enumerated every binary n×n matrix through n=4, verifying exact missing-entry expectations and known success counts 1,3,73,6003. This finite enumeration is not an asymptotic proof.

## originality

PASS

Qualified best-of-knowledge priority for the sharp fixed-density self-square failure equivalent and unique off-diagonal defect shape. OEIS A307232 already tabulates exact small-n success counts; those are explicitly credited and not claimed new. Moon–Moser established the qualitative exponent-two phenomenon, while Carvalho–Martin is structural and Shitov cites results for two independent factors. Complete Moon–Moser 1966 article was not obtained; priority risk is material but does not by itself falsify the new quantitative claim.

## value

PASS

The monoid of multipermutations and the first failure of two-step reachability are canonical algebraic/probabilistic questions. The sharp fixed-density exponentially rare error equivalent, its 10/9 constant under uniform monoid sampling and the conditional single missing ordered-pair geometry supply meaningful quantitative refinements of the classical exponent-two almost-sure statement. Known small-n OEIS counts alone do not determine this new asymptotic structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
