# Scientific review

## Correctness — PASS
The projective flag-normalization proof covers every cubic having a smooth rational point, while cubics without one have no contributing tangents. The exact finite-field program exhausts all \(9^7\) normalized coefficient tuples and returns a universal maximum of 85 covered projective points; the independent example script verifies the attaining smooth cubic, its 16 tangent lines, and its six uncovered points. The elementary line/conic lower-degree argument and the known Hermitian quartic complete the minimum-degree proof. Risk: the all-cubic upper bound is computer-assisted; independent code or mathematical auditing is still desirable.

## Originality — PASS
Asgarli--Ghioca (arXiv:2302.13420), Question 1.5 and Example 3.1, supply the general question and the already-known Hermitian upper bound, but their Theorems 1.1--1.2 do not cover cubics over \(\mathbf F_9\). Their text does not contain the complete 85-point cubic extremum. Asgarli--Ghioca--Yip (arXiv:2208.13299) address ordinary point-blocking rather than the entire plane covered by tangents. Targeted literature and mathematical-record searches revealed no covering equivalent, but search cannot exclude unpublished or unindexed computations. The Hermitian curve and its tangent-filling property are expressly credited to prior work.

## Value — PASS
The exact 85-point extremum is a sharp natural finite-plane invariant and provides the missing lower bound in the published minimum-degree question for the first odd nonprime square field. The all-cubic statement handles singular and reducible degenerations, and the explicit maximal example resolves a meaningful sharp boundary rather than an arbitrary coefficient slice.

Self-review: passed. Independent audit: not yet performed.
