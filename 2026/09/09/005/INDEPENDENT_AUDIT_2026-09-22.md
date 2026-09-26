# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/09/005`  
**Audited source tree:** `77acdfe9685c8ba0ca5621d03cecb6c5191ed381`  
**Audit performed:** 2026-09-26 UTC  
**Disposition:** PASSED

## Correctness

PASS — A fresh permutation-orbit implementation reconstructed H-conjugacy classes for (S4,2+2), (S5,2+3), (S6,3+3): 10,18,38 classes, sizes totaling 24,120,720. For every ordered pair of classes, it multiplied all elements, divided classwise product counts by the target class size, and compared every dense tensor slot: zero mismatches in 1000,5832,54872 slots, with respectively 168,1032,9173 nonzero entries. This checks the counting-form structure constants, not the geometric Hurwitz surface interpretation. The finite stabilization coincidences are observational, not a theorem of eventual stability.

## Originality

PASS, finite data — Neretin defines the relative H-conjugacy algebra and gives its structure-constant formula. His open preprint supplies the method, not these explicit three two-block multiplication tensors and cross-size examples. The product convention and reduced-neck labels are necessary for the comparisons.

## Scientific value

PASS — Small complete tensors are exact reproducible benchmarks for this relative algebra and expose stable and drifting slots. They do not establish a general stabilization threshold.

## Prior work and source access

- https://arxiv.org/pdf/2509.07148
- https://arxiv.org/abs/2304.11690

## Scope of the decision

The verdict concerns “First relative H-conjugacy-class multiplication tables for two-block Young-subgroup algebras (S4/S5/S6), with Hurwitz counting-form check and stabilization read-across” as written in `RESULT.md` and the committed package at the source tree above. Replayed computations and any limitations are identified in each axis; no inaccessible full text or global statement beyond the record's finite scope is treated as verified.
