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

The analytical proof in RESULT.md establishes the claim for every \(\gamma>0\) and real \(a,b\). The finite standalone `verify.py` provides exact-rational consistency checks of the Bloch characteristic polynomial and Laplace resolvent, and a rigorously bounded strict slowdown witness at \(a=b=\gamma=1\), \(t=2\).

Run `python3 verify.py`. The script requires only the Python standard library and reports the exact-rational assertion count and a numerical rendering of the *proved* positive rational lower bound. Its finite checks do not replace the universal spectral and perturbation arguments. The \(b\to0\) expansion assumes fixed \(a\ne0\) and \(\gamma>0\); the late-time asymptotic holds for each sufficiently small fixed nonzero \(b\).
