# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/08/090`  
**Audited source tree:** `ebe23d7f158d8b3624ac5689c657cd7a0d53de88`  
**Audit performed:** 2026-09-26 UTC  
**Disposition:** PASSED

## Correctness

PASS with theorem dependence — The stdlib verifier reconstructed all nine Apery sets, minimal c_i, complete listed Betti factorizations, length gaps and catenary values; the scan to 400 found no other Betti elements and matched the global columns. At 20 in <4,9,11>, (0,1,1) and (5,0,0) have lengths 2 and 5 and distance 5, giving gap 3. Five equality and four strict verdicts follow from the table. The passage from Betti data to global Delta and catenary values invokes established Betti-determination theorems; a bounded scan alone would not prove an all-elements claim.

## Originality

PASS, narrowly scoped — García-Sánchez and Martín-Cruz characterize the general equality setting and include <5,6,9> as an example. That row is prior art. The checked paper and cited factorization work do not report the remaining eight-row exact certificate table with the within-table extremals; no general theorem is claimed as new.

## Scientific value

PASS, modest — Exact Betti witnesses and equality/strict examples make a reproducible small semigroup test set. The nine triples are selected cases, not a complete multiplicity-band classification.

## Prior work and source access

- https://arxiv.org/abs/1909.09419
- https://arxiv.org/abs/1503.08351

## Scope of the decision

The verdict concerns “Exact Delta-set and catenary-degree table with Betti certificates for nine committed embedding-dimension-3 triples of multiplicity 4-6” as written in `RESULT.md` and the committed package at the source tree above. Replayed computations and any limitations are identified in each axis; no inaccessible full text or global statement beyond the record's finite scope is treated as verified.
