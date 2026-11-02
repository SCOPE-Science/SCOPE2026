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

# Verification and reproducibility

`RESULT.md` gives the reduction, global small-parameter estimate, local quadratic coefficient, rational strict witness, and compactness/coexistence argument. `CHECK.py` is standalone Python 3 (standard library only). Execute `python CHECK.py` in the same directory; the expected completed output is `CHECK_OK 6022`.

The checker validates exact coefficient convolution, the two strict rational witnesses, the quartic lower-bound certificate, and five exact-rational local Taylor identities. Six thousand seeded finite sample comparisons are supplementary stress tests only; they neither certify global optimization nor replace the analytical proof. The outer-extremal reduction invokes Theorem 1 of Brevig and Søvik (arXiv:2610.21788v1). No independent audit or external certification has been performed.

The exact first-departure parameter is not computed. The rigorous proved interval is \(1/5<t_*<47/100\). The transition statement does not determine later optimizer phases.
