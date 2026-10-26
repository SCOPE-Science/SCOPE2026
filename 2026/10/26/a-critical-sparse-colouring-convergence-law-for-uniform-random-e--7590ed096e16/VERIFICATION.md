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

The standalone `checker.py` was executed on its actual included path with Python 3 and no nonstandard dependencies. It enumerated all set partitions with all unary markings for sizes zero through seven at marking probability \(2/5\) and checked nine exact factorial-moment identities per domain size (the zero-size identities are included). Reported output: `SPARSE_EQUIVALENCE_MOMENTS_OK 127203 72`. The checker verifies the coefficient identities; it cannot independently establish the Bell asymptotics, the infinite Poisson process limit, the Ehrenfeucht–Fraïssé argument, the threshold, or historical originality. Those are justified in `RESULT.md` with identified mathematical sources and explicit limitations. No independent audit or independent validation has been performed.
