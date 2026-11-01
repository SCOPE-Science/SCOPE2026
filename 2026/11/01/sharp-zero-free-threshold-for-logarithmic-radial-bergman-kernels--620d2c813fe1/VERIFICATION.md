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

The theorem is established by the analytic proof in RESULT.md. Critical steps are the exact gamma-moment identity, two convergent Bernstein integral representations for the half-plane certificate, the Abel/Dirichlet-eta boundary sign for \(2<p<4\), and the explicit monotone alternating-tail upper bound for \(p\ge4\).

Execute `python checker.py` in an environment with Python 3 and `mpmath` installed. The checks test selected finite identities and real/complex values, not all exponents or the entire unit disk. The independent audit remains not performed.
