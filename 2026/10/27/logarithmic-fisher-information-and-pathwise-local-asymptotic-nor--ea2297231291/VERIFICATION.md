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

The accompanying `verify.py` is a standalone standard-library program. It checks finite rational formulas for jump means, second-moment bounds of record minima, conditional score centering, and score variance; its current run passed 111 exact checks. It also runs finite, seeded stochastic diagnostics at horizons 2000 and 12000. Their numerical output is only an illustration; the normal limit, Fisher-information asymptotics, and MLE theorem rely on the analytic proof.

The analysis treats strict decreases as continuously observed and unchanged states as discrete mass events. Parameter \(p\) is interior to \((0,1)\). Source premises for the Markov transition and endpoint law are stated in arXiv:2604.22637v1, equations (1)–(3); all new inference steps are proved in `RESULT.md`.
