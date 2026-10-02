# Independent audit — SCOPE-20260909-007

Audited at: 2026-09-30T22:14:07Z

Disposition: **passed**

## Correctness

**PASS** — A fresh bytearray sieve and independent finite scan to 5,000,000 reproduce exactly 546 prime quadruplets, the unique maximal consecutive least-prime gap 56910 from 3741161 to 3798071, the stated 18-record chain, 478 occupied square intervals among n=1..2235, and the unique maximal 22-interval empty run n=187..208 bracketed by 34841 and 43781. Independent recomputation also reproduces a=12690.52, T0=72353.63, R0=-1.2169 and Hardy–Littlewood totals 538.45 and 461.40 within the stated rounding.

## Originality

**PASS** — The bare maximal gap 56910 and its starting point are prior table data, which the record explicitly disclaims as novelty. The audited final contribution is the combined exact square-interval occupancy census, maximal empty-run witness and calibrated estimator/Hardy–Littlewood comparison to the fixed 5e6 cutoff. Searches of the prime-constellation tables, OEIS entries and published record index found no prior source containing the 478 occupancy count, the 22-interval witness, or the combined finite comparison. This supports best-of-knowledge originality for the bounded census rather than for the known gap value.

### Equivalent formulations

The census is an exact bounded statement; the known maximal-gap table is only one component and is not equivalent to square occupancy.

Evidence: No equivalent statement of the 478 occupied intervals or 22-square empty run was located.

### Broader coverage

The broader asymptotic/record-gap literature motivates the calculation without implying the exact occupancy sequence.

Evidence: Kourbatov provides statistical trend formulas, a Legendre-type conjecture and much larger record-gap tables, but not this complete square-occupancy census or its finite empty-run maximum.

### Exact database or table

The record correctly separates prior bare-gap data from the original combined census.

Evidence: A113404/A229907 cover the known gap and witness; A192870 records a conjectural threshold context. No checked table contains K=478 and E=22 with the stated square witness.

### Claim versus prior implication

The exact finite census requires enumeration and is not a corollary of the heuristic formulas.

Evidence: The prior formulas predict trends and occupancy behavior but do not determine which of the first 2235 square intervals contain a quadruplet.

## Scientific value

**PASS** — The square-occupancy statistic is directly motivated by Kourbatov’s Legendre-type conjecture for prime quadruplets, and the same exact census gives a reusable small-scale benchmark for the maximal-gap estimator and Hardy–Littlewood occupancy model. The finite cutoff is modest and proves no asymptotic theorem, but the result is a self-contained exact benchmark of a natural constellation and a specifically motivated interval statistic, with its limitations stated.

## Sources inspected

- **Maximal gaps between prime k-tuples: a statistical approach** (arXiv:1301.2242): Full paper with focus on the maximal-gap trend formula and the section stating the square-interval conjecture for prime quadruplets. Assessment: MOTIVATING_NOT_COVERING. Evidence: The paper supplies the heuristic framework and conjectural square-interval question, not the audited finite census.
- **Tables of record gaps between prime constellations** (arXiv:1309.4053): Primary arXiv record and table scope description. Assessment: PARTIAL_COVERAGE. Evidence: Record gaps are tabulated to far larger bounds, so the bare gap value is prior art; square occupancy is not the table’s object.

## Residual risks

- The cutoff 5e6 is a bounded benchmark and does not approach the conjectural eventual-occupancy threshold; no asymptotic or statistical significance claim is validated.
