# Independent audit — 2026-09-22

## Scope and source identity

Separate AI audit of `2026/09/07/003`, reviewed 2026-09-22 UTC. The audit began from repository commit `b491a8d1d4b639eb085a4c66fe4951ac3f344663` (after the separately published audit of record 001).

Source blobs: `RESULT.md` 233f11af9cd6e8b29feaa394a16e4ee1f46e80f4; `METADATA.json` 9572fded3a988dcd3e29a0b92b396ce7be78e323; prior `AUDIT.json` 936256934beb4c41304badab49b473d2627d0a22; prior `VERIFICATION.md` 83b03a7f246da30fad50fa39962dbb6d7f0519f0.

Reviewed claim: For diagonal-ones J2-free binary matrices, r(2)=2,r(3)=3,r(4)=3,r(5)=4; r(n)≤ceil(3n/4); the bound is sharp for row-weight≤2; and r(n)≥ceil(n/2) for n≤8.

## Correctness — PASS

PASS. I independently enumerated all 2^{n(n-1)} diagonal completions for n=2,…,5 with exact integer rank, reproducing survivor/rank counts 3; 21; 311=6+305; and 8995=390+8605. I separately checked the peeling lemmas, the directed-cycle proof for row-weight≤2, the 4-cycle block rank, and the Frobenius lower-bound algebra through n=8. The conjectural all-n ceil(3n/4) statement remains clearly labeled conjecture.

## Originality — PASS relative to checked evidence

PASS relative to checked evidence. The 4×4 cycle block itself is not new and appears in nearby Boolean/binary-rank literature. The checked sources did not contain the specific diagonal-ones J2-free real-rank function, the n≤5 census/orbit data, or the all-n row-weight≤2 theorem in this formulation.

## Scientific value — PASS

PASS. Beyond a small census, the record supplies reusable peeling lemmas and a structural proof for the entire row-weight≤2 subclass; that is a substantive residue after removing novelty of the base cycle block.

## Prior-art checks

1. On Minimally Non-Firm Binary Matrices — https://arxiv.org/abs/2206.04089 — Same forbidden J2 configuration in a different Boolean-rank/isolation setting.
2. On Minrank and Forbidden Subgraphs — https://arxiv.org/abs/1806.00638 — Different minrank objective/direction.
3. A Study of the Binary and Boolean Rank of Matrices with Small Constant Real Rank — https://arxiv.org/abs/2507.05824 — Related small-real-rank extremal patterns; shows the cycle motif is not itself novel.

The originality verdict means no substantive covering result was found in the checked evidence; it does **not** establish or award scholarly priority.

## Residual risks / limitations

- The full all-n ceil(3n/4) equality remains open.
- Small-n orbit counts are computational classifications, albeit independently reproducible.

## Final disposition

- Correctness: **PASS**
- Originality: **PASS relative to checked evidence**
- Scientific value: **PASS**
- Disposition: **passed**.
