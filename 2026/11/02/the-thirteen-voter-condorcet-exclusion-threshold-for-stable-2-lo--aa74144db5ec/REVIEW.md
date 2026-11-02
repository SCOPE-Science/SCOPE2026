# Scientific review: sharp Condorcet-support cutoff for stable \(2\)-lotteries

## Correctness — PASS

The exact domain is three strictly ranked alternatives with independent sampling of two defenders and the rank-copy convention used in the primary literature. The payoff polynomial \(\ell^2+\ell z+z^2/3\) follows by integrating squared ranks over an alternative's interval; the probability-weighted payoff identity gives the \(1/3\) minimax lower bound, with the upper bound supplied by the cited stable-lottery existence theorem. The exclusion hypothesis forces both rival probabilities positive, where stationarity gives a rational grid constraint. Condorcet pairwise inequalities and integer parity imply a strict payoff contradiction for at most twelve voters. The constructed thirteen-voter profile has rational payoffs \((703/2197,1/3,1/3)\), and a separate global inequality argument proves uniqueness. The exact-rational verifier corroborates the polynomial calculations and all bounded anonymous profiles without being substituted for a universal proof.

## Originality — PASS, with a specific prior-art qualification

The nearest primary source, Cai et al. (2026), already includes an Appendix A symmetric construction which **implies** that a strict Condorcet winner may be excluded: its two-rival specialization yields an eighteen-voter example. Thus the qualitative observation alone is covered and is not claimed as new. The precise first electorate of thirteen, the parity-dependent impossibility through twelve, and a unique minimizing lottery for the thirteen-voter witness are not consequences asserted or calculated in that source. Charikar et al. (2025) develop stable-lottery representation for tournament voting; Cheng et al. (2019/2020) use a different committee-lottery formulation. Searches for the exact cutoff, aliases and the two-rival payoff equations did not reveal a stronger covering statement. Residual risk: an unindexed small-profile or appendix classification could already encode the sharp cutoff. A failed search alone is not a novelty proof.

## Mathematical value — PASS

A strict Condorcet winner is the strongest pairwise-majority benchmark for an election. Stable \(2\)-lotteries are a current technique for limited-information, low-distortion randomized voting. Identifying the **smallest** electorate at which the mechanism can give the uniquely pairwise-majority-preferred candidate zero support provides a sharp and naturally motivated axiom boundary, not just another distortion example. The unique thirteen-voter witness also shows the failure cannot be dismissed as a choice among tied minimizers. The existing eighteen-voter example demonstrates that the boundary is meaningful and not an unsupported assertion of entirely new failure behavior.

## Limitations and closest sources

Exactly three alternatives, strict complete rankings, and uniform independent rank copies. No claim for arbitrary candidate numbers, distinct committees sampled without replacement, alternative activation functions, or strategic behavior. Relevant primary texts: Cai et al., arXiv:2609.08259v1, Section 3 and Appendix A; Charikar et al., arXiv:2505.13630v1, Sections 5.1–5.2; Cheng et al., arXiv:1905.04438, Sections 1–2. The latter two are not independent tests of the new sharp cutoff. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
