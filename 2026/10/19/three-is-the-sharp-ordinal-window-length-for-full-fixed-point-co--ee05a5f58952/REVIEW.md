# Scientific review: sharp covariance-rank threshold for ordinal windows

## Correctness — PASS

A uniform permutation conditioned on a single positional fixed point leaves a uniform injection into the remaining values. Exact counting gives the published covariance expression with one combinatorial choice for each prescribed small/large value set; there are no spurious factorial multipliers. Non-overlap gives zero covariance by exchangeability. The length-two rank follows from the bidiagonal support and two-direction pivot argument. At length three, two within-window pattern swaps give a strictly nonzero two-by-two determinant \(2(n-2)(3j^2-3jn+n^2-1)\), forcing all three local coefficients to vanish. Covering the coordinate set with consecutive triples yields full rank; summing the indicators of extending patterns embeds the triple-pattern row span in every longer window space. These arguments hold for every integer \(n\ge2\) and \(1\le k\le n\), with all edge cases included.

The standalone standard-library checker produced PASS: \(482,297\) exact covariance cells by exhaustive permutation enumeration through \(n=8\), \(41\) rational rank calculations for sizes through \(n=12\), and \(124,251\) integer determinant checks through \(n=500\). Finite tests corroborate the general proof; they do not prove its infinite range.

## Originality — PASS, subject to stated priority risk

The strongest directly comparable prior public note, “Boundary localization of fixed-point–descent dependence in a uniform permutation” (2026), proves the length-two coordinate covariance law. Its first-order descent covariances do not determine the covariance of the two-descent conjunctions specifying three-position patterns, and do not state full rank for \(k\ge3\). The earlier formula is explicitly treated as covered here, with no new priority claimed for it.

Diaconis–Evans–Graham's full arXiv manuscript (2013) is about the random fixed-point set and *consecutive-value* adjacency equivalence, not relative-order triple patterns. Désarménien–Wachs' 1993 full text, including Theorem 5.1 and Section 6, tracks the **number** of fixed points in descent classes rather than each fixed point's location. Eriksen–Freij–Wästlund (2008) tracks fixed-point restrictions under specified descent sets, again without the displayed ordinal-pattern/fixed-position covariance matrix. Janson–Nakamura–Zeilberger (2013) gives joint pattern-count limit laws, not the finite full-rank comparison with labeled fixed points. Searches for equivalent local ordinal-pattern or anchored fixed-point formulations did not establish dominating earlier coverage. Absence of a result in these searches is not proof of first priority; an implicit older identity could exist.

## Mathematical value — PASS

The result resolves a natural *minimal local information* question: how many consecutive order observations are needed before the complete family of fixed-point-position indicators is visible to linear covariance? The answer is the sharp universal threshold three, valid at every finite size and every longer window. The unexpectedly strong change from an \((n-1)\)-dimensional cross-covariance row space to full dimension arises from joint three-position order structure, not from a mere reindexing of descents. The closed kernel permits exact finite-size comparisons. It does not promise samplewise fixed-point reconstruction or a conditioning bound.

## Sources and remaining limits

Primary motivating source: Diaconis, Evans, Graham (Berkeley Report 822, 2013-08-01; arXiv:1308.5459), with primary MSC 60C05. Directly relevant earlier sources: Désarménien and Wachs (1993), Eriksen et al. (2008), Janson et al. (2013), and the public 2026 fixed-point/descent note. Potential implicit coverage by more general refined permutation-enumeration machinery remains a scientific priority risk. The sole acceptance claim is the formula and the \(0,n-1,n\) rank classification as stated, not novelty of the earlier descent law.

Self-review: passed. Independent audit: not yet performed.
