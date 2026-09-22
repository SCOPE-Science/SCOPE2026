# Independent audit — 2026-09-22

## Scope and source identity

Separate AI audit of `2026/09/07/010`, reviewed 2026-09-22 UTC. The audit began from repository commit `b491a8d1d4b639eb085a4c66fe4951ac3f344663` (after the separately published audit of record 001).

Source blobs: `RESULT.md` c793f80b8479f7496b587972c03fe22cc02dd8d3; `METADATA.json` dc82d208b06b17e5ac97013cfc20a7a51b728395; prior `AUDIT.json` 7ef56e31e371407458fcc15786f97f52b6d15c8e; prior `VERIFICATION.md` 83b03a7f246da30fad50fa39962dbb6d7f0519f0.

Reviewed claim: At C=24 in the stated box, all two-type and three-type instances satisfy IRUP; five displayed instances have exact Delta=1; and all 63 stated Hamming-1 neighbors have Delta=0.

## Correctness — PASS

PASS after two bounded textual repairs. I independently solved all 3,520 two-type and all 84,465 three-type instances using exact dual-vertex enumeration for LP_GG and exact dynamic programming over bin patterns for OPT; every case has Delta=0. One-type cases are trivially IRUP. For each of E1–E5 I independently regenerated the complete pattern set, checked the rational primal and dual certificates exactly, verified the displayed packing, and independently proved OPT−1 infeasible by item-branching search. I also regenerated the 63 Hamming-1 neighbors; an independent exact dual lower-bound certificate plus exact packing search proves Delta=0 for every one. The original table had a clerical E3 total S=187; direct summation is S=192. The phrase 'k≤2 (3,520 instances)' also conflated the 3,520 two-type cases with trivial one-type cases. Both are corrected in RESULT.md in this audit commit; no optimization conclusion changes.

## Originality — PASS relative to checked evidence

PASS relative to checked evidence. Prior IRUP/MIRUP work organizes results by other structural parameters and supplies broader theory and counterexamples. Searches by the exact C=24 instances and certificates did not locate this capacity-stratified benchmark catalog. No full-stratum maximality is claimed.

## Scientific value — PASS

PASS. The exact primal/dual/packing certificates make the five instances useful solver benchmarks, and the exhaustive two-/three-type closure plus local-neighbor closure give them context. The unproved full C=24 MIRUP conjecture remains explicitly outside the theorem.

## Bounded repair

This audit corrects `RESULT.md` only: E3 has `S=192` (not 187), and Theorem A now states that the enumerated count 3,520 refers to `k=2`, while `k=1` is trivial. The certificates, LP values, OPT values, Delta values and scientific conclusions are unchanged.

## Prior-art checks

1. Minimal proper non-IRUP instances of the 1D Cutting Stock Problem — https://arxiv.org/abs/1405.5988 — Prior structural/minimal-instance classification; distinct from this C=24 table.
2. The modified integer round-up property of the 1D cutting stock problem — https://doi.org/10.1016/0377-2217(95)00022-I — MIRUP background.
3. Large gaps in 1D cutting stock problems — https://doi.org/10.1016/j.dam.2007.08.052 — Asymptotic/large-gap constructions, complementary to the finite benchmark.

The originality verdict means no substantive covering result was found in the checked evidence; it does **not** establish or award scholarly priority.

## Residual risks / limitations

- The full k≤6 C=24 box is not exhausted, so G*(24)=1 remains conjectural.
- Repairs are clerical scope/table corrections only; no prior audit artifact is overwritten.

## Final disposition

- Correctness: **PASS**
- Originality: **PASS relative to checked evidence**
- Scientific value: **PASS**
- Disposition: **passed** after bounded repair.
