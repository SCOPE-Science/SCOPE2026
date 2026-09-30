# Independent Audit — 2026-09-28

**Record:** `2026/09/10/049`  
**Title:** No 9-direction graph in the normalized monic degree-7 family over F_13  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `5b6a29dd917a3594d89171e370a165eec8a5f5d1`  
**Disposition:** **REPAIRED**

## Independent checks

- Independently evaluated all 78 pairwise slopes for every one of the 13^5 normalized coefficient choices and counted distinct directions.
- Rechecked the AGL normalization algebra in characteristic 13.
- Read the Kadoo abstract directly rather than relying on the earlier audit’s truncated characterization.

## Three-axis assessment

- **Correctness — PASS**: The central exhaustive claim is correct. A fresh vectorized enumeration of all 13^5=371,293 normalized coefficient tuples reproduced the exact direction histogram {8:13, 11:117, 12:1196, 13:369967}, with zero 9-direction functions. The affine normalizations used (output scaling, input translation killing x^6, and vertical translation) preserve direction cardinality. The earlier research context, however, materially misstated Kadoo 2010 by saying it only excluded an 8-secant/no-9-secant subcase; the same abstract also states existence of a size-22 Rédei-type minimal blocking set. The core degree-7 obstruction survives after correcting that context.
- **Originality — PASS**: The exact normalized degree-7 census and histogram were not found in the cited finite-geometry literature or Resultary neighbors. Kadoo’s prior size-22 Rédei-type existence result removes any claim that this settles or nearly settles size-22 existence, but it does not provide the degree-7 normalized-family census. Novelty is therefore limited to that precise obstruction/data set.
- **Scientific Value — PASS**: The corrected result is a narrow but reproducible classification datum: it eliminates the natural degree-(p+1)/2 normalized polynomial family as a source of 9-direction graphs over F13. Its value is as a pruning lemma/benchmark, not as progress on the already-known existence of size-22 Rédei-type blocking sets.

## Findings

- Current main tree equals assigned SHA.
- Independent exhaustive recensus over all 371,293 normalized degree-7 polynomials reproduced the filed histogram exactly and found n9=0.
- Ball’s direction theorem allows N≥8 for q=13 and does not force the gap at N=9.
- Kadoo 2010 explicitly states both the 8-secant/no-9-secant nonexistence subcase and existence of a size-22 Rédei-type minimal blocking set; the original Context omitted the latter and must be repaired.

## Sources compared

- Repository record 049 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/049/RESULT.md — Contains the exhaustive degree-7 census and the contextual Kadoo misstatement.
- Ball, The number of directions determined by a function over a finite field (2003): https://doi.org/10.1016/j.jcta.2003.09.006 — For q prime, direction counts are 1 or at least (q+3)/2; for q=13 this does not exclude 9 directions.
- Csajbók, On bisecants of Rédei type blocking sets and applications: https://arxiv.org/abs/1504.06748 — Gives structural context and the small-direction threshold; it does not contain the normalized degree-7 census.
- Kadoo, The Minimal Blocking Set Of Size 22 In PG(2,13) (2010): https://doi.org/10.33899/csmj.2010.163898 — The abstract explicitly reports existence of a size-22 minimal blocking set of Rédei type as well as the 8-secant/no-9-secant nonexistence statement.

## Limitations

- The repaired claim is only about the normalized degree-7 polynomial family; it makes no global existence claim for size-22 Rédei-type blocking sets.
- Novelty is asserted only for the exact census after targeted literature/Resultary searches, not from search failure alone.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
