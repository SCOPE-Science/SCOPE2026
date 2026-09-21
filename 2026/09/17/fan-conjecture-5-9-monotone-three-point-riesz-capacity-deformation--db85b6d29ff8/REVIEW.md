# same-model review

## Review status

- Corrected research/audit end: `2026-09-17T10:40:28.518560Z`
- Reported status: `SAME_MODEL_REVIEW_PASS`
- Corrected accepted finding: Fan Conjecture 5.9 / odd-polygon Riesz-capacity Step 2

## Correction

The preliminary NCI draft was withdrawn because it overlapped an existing SCOPE research direction. It remains separately archived as a protocol-invalidated attempt, not an accepted finding. See CORRECTION.md. This Riesz-capacity finding is a distinct mathematical claim.

## Correctness

**PASS (same-model assessment).**

The source report re-derived the three-point-energy derivative reduction, checked the hypotheses needed for `0<u<=v<=1`, proved the power-difference lemma analytically, and checked continuity and branch behavior at `D=0`. It explicitly audited the boundary cases `r=2`, `psi=0`, and `phi=2pi/3`, as well as the possibility of multiple support-branch switches.

The companion verifier reports dense-grid, deterministic deformation-grid, and randomized checks. Those computations corroborate but do not replace the proof.

No independent review has been performed.

## Originality

**PASS, qualified to the best of our knowledge (same-model assessment).**

The direct parent source, arXiv:2609.11186v1, was reported to state the Step-2 assertion as Conjecture 5.9 and to say that the odd-polygon formula follows from it and the already proved symmetric step. The source report searched exact, equivalent, and stronger-coverage formulations and found no public proof.

The principal unresolved originality risk is extreme freshness: the parent preprint was about one week old. An unposted author revision, private communication, or contemporaneous independent solution could overlap. The scalar power-difference inequality may also be known independently even if this application is not.

## Value

**PASS (same-model assessment).**

The result addresses the explicit analytic bottleneck identified by the parent paper rather than an isolated numerical case. Under Fan's published reduction, it upgrades the stated odd-regular-polygon equilibrium formula from conjectural to proved for every odd `N>=3` and every real `r>2`.

## Review disclaimer

This is a same-model review, not independent validation, peer review, formal verification, or a guarantee of scholarly priority.

## Recorded review qualifications

> **Review status: same-model review.** Correctness, originality, and value were assessed by the same-model review, not an independent reviewer. Originality is only to the best of our knowledge.
