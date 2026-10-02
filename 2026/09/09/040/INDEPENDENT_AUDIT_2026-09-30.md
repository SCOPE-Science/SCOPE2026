# Independent audit — SCOPE-20260909-040

Audited at: 2026-09-30T22:49:30Z

Final disposition: **repaired**.

## Correctness

**PASS** — Fresh exact finite-field recomputation rebuilt PG(2,13), the three graph sets, all 183 line incidences, tangents and spectra. It reproduced W21 direction set {1,3,4,5,8,9,10,12} with spectrum 1:126,2:18,3:36,8:3; W23 with ten stated directions and spectrum 1:96,2:52,3:32,6:1,10:2; and W24 with eleven stated directions and spectrum 1:91,2:59,3:16,4:14,6:2,11:1. Separate exhaustive direction-count scans reproduced N=9 count zero for all monomials, binomials, monic trinomials, and normalized degree<=6 polynomials. The original text nevertheless made a false global-status statement that size 22 remained open; Kadoo (2010) reports size-22 Redei-type existence. The repaired claim removes that statement while keeping the verified low-complexity graph exclusion.

## Originality

**PASS** — Kadoo 2010 covers global size-22 Redei-type existence, and later SCOPE-20260910-049 gives a degree-7 normalized-family obstruction. Neither checked source supplies the exact W21/W23/W24 witness package plus the all-monomial/binomial/trinomial and degree<=6 N=9 exclusion. The repaired claim explicitly avoids global size-22 novelty.

### Equivalent formulations

Searches checked: published-record search: PG(2,13) Redei blocking set 21 22 23 24 directions; Kadoo 2010 minimal blocking set size 22 PG(2,13).

Evidence: Kadoo reports a 22-point Redei-type minimal blocking set but not the exact repaired low-complexity exclusion as stated.

Reasoning: Global size-22 existence is prior art; the repaired graph-family statement is distinct.

### Broader coverage

Searches checked: SCOPE-20260910-049 degree-7 9-direction graph F_13; Ball number of directions function finite field; Csajbok Redei type bisecants.

Evidence: SCOPE049 excludes the AGL-normalized monic degree-7 family and explicitly notes Kadoo existence. It does not subsume the all-degree <=3-term exclusion; general direction theorems constrain cardinalities but do not yield the reported exact family census.

Reasoning: The later degree-7 result strengthens one degree boundary but does not imply the entire repaired witness/exclusion package.

### Exact database or table

Searches checked: PG(2,13) minimal blocking sets direction spectra 21 23 24; 9-direction functions F_13 tables.

Evidence: No checked table provided the three exact line spectra and four-family N-value sets {1,8,12,13}, {1,8,10,11,12,13}, {8,10,11,12,13}, {1,11,12,13}.

Reasoning: The numerical spectra/family census were not found in the primary source checked.

### Claim versus prior implication

Searches checked: Kadoo 2010 size 22 Redei-type; Ball direction theorem q=13.

Evidence: Kadoo establishes existence of a 22-point Redei-type set, so it defeats the old open-status wording, but does not by itself imply whether monomials/binomials/trinomials/degree<=6 graph functions attain 9 directions.

Reasoning: After correction, the remaining claim needs the explicit finite-field census.

### Source inspections

- **The Minimal Blocking Set Of Size 22 In PG(2,13)** (https://doi.org/10.33899/csmj.2010.163898): CORRECTIVE_PRIOR_ART. Material read: full-text HTML/OCR including abstract and introductory construction pages. Abstract explicitly states existence of a minimal blocking set of size 22 of Redei type in PG(2,13).
- **No 9-direction graph in the AGL-normalized monic degree-7 family over F_13** (SCOPE-20260910-049): PARTIAL_STRONGER_COVERAGE. Material read: complete RESULT.md. Excludes all normalized degree-7 representatives and explicitly treats Kadoo size-22 existence as known; it does not cover the full low-term census here.

Checked sources: published SCOPE findings search; Kadoo 2010 DOI 10.33899/csmj.2010.163898; SCOPE-20260910-049; Ball 2003 direction theorem; Csajbok arXiv:1504.06748.

Residual risks: The precise projective equivalence between Kadoo constructions and the narrow graph normalization used here was not needed for the repair, because the corrected text makes no global graph-existence claim.

## Scientific value

**PASS** — Explicit minimal blocking-set witnesses at the Blokhuis boundary and nearby sizes, together with a structured exclusion of all low-complexity graph polynomials for the missing 9-direction case, provide a motivated finite-geometry boundary result. The repaired claim no longer treats the already-known global size-22 existence question as open.

## Repair

The old sentence treating size-22 existence as open is removed. Kadoo (2010) is cited as prior global Rédei-type existence. The final theorem is explicitly limited to the three verified witnesses and the low-complexity graph-function exclusion. The repaired claim was reassessed on all three axes above.
