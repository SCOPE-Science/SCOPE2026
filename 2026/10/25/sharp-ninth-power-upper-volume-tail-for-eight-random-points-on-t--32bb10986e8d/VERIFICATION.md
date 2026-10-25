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

# Reproducible verification and proof dependencies
Run `python check_tail.py` with the package's `requirements.txt` dependencies. The code verifies 105 pairings and the exact rational prefactor \(2916\), then tests an analytic determinant formula against independently computed four-dimensional convex-hull volumes in 270 fixed-seed configurations and probes the quadratic expansion of the volume deficit. The independent hull calculations and determinant checks passed; a reported finite-scale remainder of less than \(10^{-4}\) does not establish an all-scale bound.

The theorem is proved by the explicit 16-facet signed-determinant identity, the positive 18-dimensional normal quadratic form, orthogonal-frame orbit volume, exact combinatorial pairing count, and dominated convergence in normal tubes. Its only external global premise is Medgyes's 2026 theorem that the volume-maximizing eight-point configurations are precisely regular four-cross-polytopes. That theorem's separate computational certificates are cited but were not revalidated.

Verification checks are scientific reproducibility checks, not a claim of external, independent validation. The exact distribution at non-extremal volumes and independent source-priority completeness are not established.
