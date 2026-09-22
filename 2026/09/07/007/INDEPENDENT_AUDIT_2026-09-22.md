# Independent audit — 2026-09-22

## Scope and source identity

Separate AI audit of `2026/09/07/007`, reviewed 2026-09-22 UTC. The audit began from repository commit `b491a8d1d4b639eb085a4c66fe4951ac3f344663` (after the separately published audit of record 001).

Source blobs: `RESULT.md` 739d0beb795b2de65a1eb6f4fa3e452f60d9af6d; `METADATA.json` 5030f86b94969569b975e993644ddf02d98bce95; prior `AUDIT.json` 81fc9787d95d59724dd975901fb6f34873623171; prior `VERIFICATION.md` 83b03a7f246da30fad50fa39962dbb6d7f0519f0.

Reviewed claim: The displayed 8-state binary one-cluster automaton has reset threshold 34; among the 14 canonical 5-cycle one-cluster a-types with permutation b, all 564480 automata have been exhausted and the maximum is uniquely 34.

## Correctness — PASS

PASS. A fresh subset-automaton BFS gives reset distance 34 for the displayed witness and verifies its reset word. Independently enumerating the 320 admissible attachments and quotienting by cycle rotations and S3 relabeling gives exactly 14 canonical a-types. A separate exhaustive C scan of all 14×40320=564480 permutation-b automata found 550796 synchronizing cases and a unique reset-threshold maximum of 34, matching the record.

## Originality — PASS relative to checked evidence

PASS relative to checked evidence, narrowly. Broader exhaustive studies already enumerate binary synchronizing automata at and beyond 8 states, and Steinberg’s theorem covers the prime-cycle one-cluster upper bound. I did not locate the same restricted prime-5-cycle/permutation-b census or this exact unique witness catalog in the checked sources.

## Scientific value — PASS

PASS, narrowly. The restricted census is useful as a reproducible benchmark for one-cluster theory/search, but it should not be presented as the first exhaustive information about 8-state binary synchronizing automata generally.

## Prior-art checks

1. The Cerny conjecture for one-cluster automata with prime length cycle — https://arxiv.org/abs/1107.3051 — Theoretical upper bound for the regime; no matching finite restricted census located.
2. Experiments with Synchronizing Automata — https://arxiv.org/abs/1309.0044 — Much broader computational enumeration, limiting the novelty claim to this specific slice.

The originality verdict means no substantive covering result was found in the checked evidence; it does **not** establish or award scholarly priority.

## Residual risks / limitations

- The full slice with arbitrary second letter remains unclassified.
- Restricted-slice novelty is relative to the checked literature only.

## Final disposition

- Correctness: **PASS**
- Originality: **PASS relative to checked evidence**
- Scientific value: **PASS**
- Disposition: **passed**.
