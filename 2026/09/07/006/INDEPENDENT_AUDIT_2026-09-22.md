# Independent audit — 2026-09-22

## Scope and source identity

Separate AI audit of `2026/09/07/006`, reviewed 2026-09-22 UTC. The audit began from repository commit `b491a8d1d4b639eb085a4c66fe4951ac3f344663` (after the separately published audit of record 001).

Source blobs: `RESULT.md` a8fd55e77d84ffb53e2bce5b7ec6e6460132fbf5; `METADATA.json` 7186ce652c47e8341d0d03ca7eac2561fef76a72; prior `AUDIT.json` c27a1417176f2f1e93aaead8dd4c63013589c6ac; prior `VERIFICATION.md` 83b03a7f246da30fad50fa39962dbb6d7f0519f0. Replay artifact blob: fcfdadbbe2684d074bdf1757c7b67c789ffa4210.

Reviewed claim: For partitions of 12, exactly 30336 of the 79079 S3-unordered Kronecker triples vanish; ordered zeros number 176524; and the unique unordered maximum is g((5,3,2,1,1)^3)=945.

## Correctness — PASS

PASS. I independently implemented Murnaghan–Nakayama with a different strip-order recursion, rebuilt the 77×77 character table, and verified exact orthogonality. Scanning all 79,079 unordered triples reproduced 30,336 zeros, 48,743 nonzeros, ordered counts 176,524/280,009, the unique maximum 945 at (5,3,2,1,1)^3, and the published top values. The class-sum integrality and the 945 certificate agree exactly.

## Originality — PASS relative to checked evidence

PASS relative to checked evidence, narrowly. General algorithms, software and modern public datasets make fixed-n Kronecker tables increasingly routine. Searches by the exact n=12 counts and maximum did not locate a prior publication of this full S3-reduced census with the stated certificate. This is not a claim that computing S12 coefficients is a new method.

## Scientific value — PASS

PASS, narrowly. The durable value is an exact, compact ground-truth table/certificate useful for testing algorithms and empirical conjectures, not a structural theorem about Kronecker coefficients.

## Prior-art checks

1. On vanishing of Kronecker coefficients — https://arxiv.org/abs/1507.02955 — Complexity/vanishing context; not an n=12 exhaustive census.
2. Bounds on the Kronecker coefficients — https://arxiv.org/abs/1406.2988 — General bounds rather than this finite table.
3. Computation of Dilated Kronecker Coefficients — https://arxiv.org/abs/1601.04325 — Algorithmic/dilated setting, distinct from a full fixed-n cube.

The originality verdict means no substantive covering result was found in the checked evidence; it does **not** establish or award scholarly priority.

## Residual risks / limitations

- Priority for a finite table is hard to establish because unpublished software-generated tables may exist.
- The record is computational ground truth and provides no new structural proof of the extremal shape.

## Final disposition

- Correctness: **PASS**
- Originality: **PASS relative to checked evidence**
- Scientific value: **PASS**
- Disposition: **passed**.
