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

The proof in RESULT.md derives the infection-free vaccination-age density and the exact infected-subsystem characteristic equation directly from the unaveraged age-structured host–vector model. In particular, the vaccination boundary flux cancels after summation of infected classes, so the formula is not an assumption inherited from a reduced averaged-efficacy equation.

Run `python3 verify.py` after extracting this package. Its rational-interval calculation encloses \(e^{-1}\) between the partial sums of orders 29 and 30, then checks the three closed-form elementary integrals and that \(\mathcal K(0)>1\), \(\mathcal K(1)<1\), and \(\mathcal K(\infty)>1\). The expected final line is `VERIFY_OK`.

The exact arithmetic checks only the three parameter inequalities. The proof of the infinite-dimensional mode criterion and the continuity-based existence of two distinct crossings is in RESULT.md. No numerical simulation is treated as proof of global stability, of exactly two transitions, or of any nonlinear endemic state. Independent verification has not been performed.
