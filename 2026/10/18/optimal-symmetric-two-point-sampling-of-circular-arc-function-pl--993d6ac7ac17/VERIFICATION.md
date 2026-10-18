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

# Reproducibility and checks
Run `python verify.py` with Python 3 (standard library). The script tests the exact three-term formula for multiple admissible angle pairs against a dense scalar phase grid, checks the balancing equation, and compares sharp endpoint witnesses. The code performs a diagnostic, not an infinite proof. The analytic proof derives the complete norm for all phases, all amplitudes and all matrix sizes.

Originality comparisons read the full substantive arc-space section of Ray's arXiv:2610.04608v1 and the relevant statement and pointwise-extremizer section of Tikhonov–Yuditskii's arXiv:1809.09726v2. The polynomial-mesh preprint arXiv:2608.27618 was inspected only at abstract level. Broader unpublished and inaccessible classical literature may affect publication priority. No independent audit or external certification is claimed.
