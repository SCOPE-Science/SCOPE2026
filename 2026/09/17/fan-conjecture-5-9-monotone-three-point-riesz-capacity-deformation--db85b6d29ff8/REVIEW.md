# same-model review

## Run identity

- Source run ID: `SCOPE-20260917T101839Z-001`
- Research start: `2026-09-17T10:18:39Z`
- Corrected research/audit end: `2026-09-17T10:40:28.518560Z`
- Actual elapsed: about 21 min 49.519 s
- Reported status: `SAME_MODEL_REVIEW_PASS`
- Result type: substantive target completed early
- Corrected accepted finding: Fan Conjecture 5.9 / odd-polygon Riesz-capacity Step 2

## Correction and independence

The run initially produced a quantitative Non-Cancelling Intersections draft before earlier-run history became visible. That history showed that `SCOPE-20260917T100054Z-R02` had already pursued the same NCI direction. the same-model review therefore explicitly invalidated the NCI draft as this run's accepted outcome under the cross-run independence rule and restarted on an unrelated Riesz-capacity target. The preliminary NCI material is retained separately as negative research memory and is not part of this accepted finding.

The final Riesz target was checked against the accessible earlier topics and was reported to be unrelated in objects, literature, and proof method. No earlier proof or unfinished method was used as the starting point.

The source run also reports that another unrelated execution ended at about `2026-09-17T10:21:19Z`, around 2 min 40 s after this run began. That overlap was not observable at the start, and the scheduling layer did not expose a hard mutual-exclusion lock.

## Correctness

**PASS (same-model assessment).**

The source run re-derived the three-point-energy derivative reduction, checked the hypotheses needed for `0<u<=v<=1`, proved the power-difference lemma analytically, and checked continuity and branch behavior at `D=0`. It explicitly audited the boundary cases `r=2`, `psi=0`, and `phi=2pi/3`, as well as the possibility of multiple support-branch switches.

The companion verifier reports dense-grid, deterministic deformation-grid, and randomized checks. Those computations corroborate but do not replace the proof.

No independent review has been performed.

## Originality

**PASS, qualified to the best of our knowledge (same-model assessment).**

The direct parent source, arXiv:2609.11186v1, was reported to state the Step-2 assertion as Conjecture 5.9 and to say that the odd-polygon formula follows from it and the already proved symmetric step. The source run searched exact, equivalent, and stronger-coverage formulations and found no public proof.

The principal unresolved originality risk is extreme freshness: the parent preprint was about one week old. An unposted author revision, private communication, or contemporaneous independent solution could overlap. The scalar power-difference inequality may also be known independently even if this application is not.

## Value

**PASS (same-model assessment).**

The result addresses the explicit analytic bottleneck identified by the parent paper rather than an isolated numerical case. Under Fan's published reduction, it upgrades the stated odd-regular-polygon equilibrium formula from conjectural to proved for every odd `N>=3` and every real `r>2`.

## Review disclaimer

This is a same-model review, not independent validation, peer review, formal verification, or a guarantee of scholarly priority.
