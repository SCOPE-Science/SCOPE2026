# Scientific review

## Correctness

PASS. For a prescribed finite set of labels, one group draw has exact inclusion probabilities given by falling-factorial hypergeometric ratios. Uniform comparison with independent Bernoulli selections across \(O(\log n)\) rounds gives mixed factorial moments of independent Poisson first-discovery counts at finitely many late rounds. The unseen-count factorial moments, a union bound, and a Poisson left-tail estimate ensure last-discovery tightness. These steps justify the joint limit for last-round location and last-round multiplicity, including the sum over all possible completion offsets. The absolutely convergent phase-profile series permits Mellin/Fourier unfolding, and nonvanishing of Gamma proves nonconstant phases. Logarithmic equidistribution and the zero Fourier coefficient give the averaged logarithmic-series law. The verifier independently checks exact finite-size inclusion–exclusion against exhaustive subset transitions in 365 assertions; it does not replace these infinite proofs.

## Originality

PASS under the accessible-record, best-knowledge comparison, with priority caveats. The closest primary source, Berend and Sher (arXiv:2605.06953v1), gives a sharp expected completion-time asymptotic and a one-time Poisson limit for unseen coupon counts in proportional group drawings, not a multitime marked first-discovery limit or the law of how many types are first discovered *in the completing package*. Schilling–Henze (2021) and Betken–Thäle (2023) study fixed-size group drawing counts and marginal Poisson approximation. Extant mathematical records and accessible prior claims do not identify the exact terminal-batch phase profiles or their logarithmic-series averages. These are statement-level distinctions, not arguments from titles. Stadje (1990) might contain an equivalent finite distribution or a transform yielding this asymptotic, but its full text was inaccessible; the precise historical novelty is therefore not independently certified.

## Mathematical value

PASS. A proportional package can simultaneously reveal several as-yet-unseen coupons in the final round, so the classical unique-last-coupon property fails. The theorem resolves the natural multiplicity statistic, provides its full attainable phase family, proves genuine nonconvergence, and identifies a canonical logarithmic-series averaged law. The ratio \(c/[-\log(1-c)]\) has direct interpretation as the averaged probability of a unique last discovery. The phenomenon specifically isolates the macroscopic-batch regime rather than yielding an arbitrary special-case computation.

## Closest literature and remaining limits

Berend and Sher (2026), arXiv:2605.06953v1, Section 2 and the proportional-group proof in Section 3, supply the direct comparison. Schilling and Henze (2021), DOI 10.1017/jpr.2021.15, Theorem 2.1, and Betken and Thäle (2023), DOI 10.1017/jpr.2023.6, supply related group-coupon Poisson results in different scopes. Stadje (1990), DOI 10.2307/1427566, is an unresolved full-text priority risk. The result assumes fixed \(0<c<1\), independent uniform packages, fixed multiplicity \(r\), and finite-dimensional first-discovery windows only. No full historical-priority or independent theorem verification is claimed.

Self-review: passed. Independent audit: not yet performed.
