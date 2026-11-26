---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The analytic proof in `RESULT.md` checks the global generator definition, the node separation, the chronological order of the two nonidentity exponentials, and their exact signed coordinates. The negative abscissa printed in the preprint is within the domain of the generator and gives zero; replacing it by the upper in-interval half-step Gauss node also gives zero for this generator. Run `python3 verify.py` for a finite decimal check of the ordered stage propagation and a control with the reversed order. The proof of strict negativity at all specified step sizes is analytic, not numerical.
