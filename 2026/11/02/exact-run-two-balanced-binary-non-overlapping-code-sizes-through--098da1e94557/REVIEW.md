# Scientific review

## Correctness — PASS
The exact statement is finite and correctly quantifies over all codes of the six stated lengths, with each codeword balanced and subject to the **cyclic** run-two restriction. Exhaustive generation includes exactly the 2, 6, 10, 24, 52 and 128 eligible unbordered words. Each of the explicit partitions into 1, 2, 3, 5, 11 and 24 color classes satisfies the directly checked property that any two words sharing a color overlap, providing rigorous upper bounds. Matching sets of pairwise non-overlapping words supply the lower bounds. A separate direct Dyck enumerator confirms Construction 7 sizes. The standalone checker completed with `VERIFY_OK`; no search-program conclusion is assumed without a finite certificate.

## Originality — PASS, qualified
Chee et al. and Blackburn analyze general non-overlapping codes, not this exact jointly constrained optimum. Stanovnik et al. (2024) analyze unconstrained maximum codes. The most relevant work, Stanovnik et al. (2025), explicitly treats both balance and run-length restrictions and presents Construction 7 as a lower-bound construction, obtaining 20 words at length fourteen. Its general framework can in principle enumerate all maximal codes but does not assert or imply a specific value of 24 without doing the additional optimization. Neither its stated upper/lower theory nor the inspected tables give this exact finite size profile. Targeted published-record and same-topic prior-claim comparisons did not reveal a covering result. Historical priority remains qualified by potentially unindexed datasets and later literature.

## Value — PASS
Balancing and suppression of long homopolymer runs are simultaneous physical constraints in synchronization and DNA-inspired coding. The new size 24 is a sharp, completely certified 20% improvement over a specifically documented natural construction at the first failing block length, with all earlier even lengths in the tested range classified. The explicit coloring certificate is independently reproducible and exposes a meaningful finite boundary; no all-length contribution is claimed.

## Closest source and residual limitations
Most relevant: Stanovnik, Moškon and Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths* (2025), Section 5, Construction 7, Proposition 13, and Table 2. Other sources: Chee et al. (2012 preprint); Blackburn (2013 preprint); Stanovnik et al. (2024). This finite result does not imply an exact sequence beyond length fourteen, uniqueness of maximizing codes or Hamming-distance guarantees. No independent audit or validation is asserted.

Self-review: passed. Independent audit: not yet performed.
