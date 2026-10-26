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

# Reproduction

Run `python3 verify.py` (Python 3 standard library only). The script enumerates all 90 double-occurrence words on three labels and all 2520 words on four labels, checks each exact conditional probability displayed in the proof, then checks the algebraic conditional-covariance expressions against the closed forms for all integers from 2 through 300. The computations certify the small labeled-pattern counts; the uniform-subword lemma and covariance decomposition prove the unrestricted theorem. A second exact check exhaustively enumerates all perfect matchings on 4, 6, 8, 10 and 12 endpoints and computes both conditional degree covariances directly, for chord counts 2 through 6. This separate enumeration agrees with the unrestricted formulas at those sizes but is not a substitute for the analytic proof. Checks do not constitute an independent audit or historical-priority certification.
