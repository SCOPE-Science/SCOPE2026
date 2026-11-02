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

# Verification

The universal proof can be checked directly using the identities \([D,\operatorname{diag}f]q=(f(x)-f(y))v\) and \([D,\operatorname{diag}f_*]=vq^{\mathsf T}-qv^{\mathsf T}\) with \(q=(e_x-e_y)/\sqrt2\), \(q\perp v\), and \(\|v\|^2=C\). These establish both the necessary lower bound and an attainable equality witness. The infinite-distance case follows because the explicit witness then has zero commutator.

The standalone `check_twin.py` script requires Python 3 and no third-party dependencies. Running `python3 check_twin.py` produced `EXACT_RATIONAL_OK cases=539`. It checks rank-two Gram identities and an arbitrary-potential vector identity using exact rational arithmetic, including signed weights and arbitrary connections among other vertices. It cannot certify all input sizes or prove novelty; the analytical proof supplies the universal quantifiers. No separate independent audit has been performed.
