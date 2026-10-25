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

# Reproducibility and limits
Run `python3 verify_capsule.py` using Python 3 and only the standard library. An actual execution produced: `PASS: 8442 support comparisons; 42 isotropy/contact checks; 15 crossover checks; 3 wide-separation checks; max residual 7.275957614183426e-12`.

The script tests candidate semiaxes, positivity and tip strictness, the \((h/t)(s-t)^2\) support slack, isotropic-normalized contact geometry, and convergence of volume factors in two scaling regimes. It does not enumerate all real half-separations, dimensions or normals and is not an infinite proof. The mathematical proof is the universal certificate and contact argument in `RESULT.md`; no external independent audit or mechanized proof was performed. The Yıldırım (2006) full paper could not be accessed; potential equivalent prior formulas remain a literature-priority risk.
