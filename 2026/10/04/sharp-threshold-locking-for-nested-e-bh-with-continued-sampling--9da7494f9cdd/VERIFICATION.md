---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The deterministic proof has two components. First, keeping all current e-BH rejections above the current cutoff forces the next rank-
\(r\) order statistic to satisfy the same cutoff, so the next cutoff cannot increase. Second, lowering one old rejection below that cutoff while holding the other old rejections at the cutoff and all outsiders at zero makes every e-BH rank fail.

For the sequential construction, the update
\[
E_{t+1}=c_t+(E_t-c_t)X_{t+1}
\]
is nonnegative and has conditional null expectation at most \(E_t\) whenever \(E_t\ge c_t\) and \(\mathbb E[X_{t+1}\mid\mathcal F_t]\le1\).

`verify_lock_and_bet.py` checks the e-BH implication and sharp counterexamples over multiple finite grids and randomized outsider values, and checks the affine expectation calculation for discrete factors. It returned `VERIFY_OK` on the packaged version.

Scientific limits: base e-BH; coordinatewise worst-case pathwise nesting; common-filtration conditionally valid factors for the sequential interpretation; no claim of optimal sampling cost or power.
