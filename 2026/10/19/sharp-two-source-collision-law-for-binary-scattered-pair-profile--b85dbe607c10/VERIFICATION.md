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

# Verification record

Run the embedded standalone `verify.py` with `python3 verify.py`; it requires only Python's standard library. The code computes every length-one and length-two scattered-subsequence count by independent direct pair enumeration for words through length ten, verifies equivalence with the proposed two-dimensional profile, and compares all composition/inversion histograms with a distinct dynamic recursion through length twelve.

The recursion is also checked against exact binomial composition counts through length 160. Under rational source probabilities, exact weighted collision identities agree through length ten. Numerical ratios of exact collision probabilities to the sharp leading expression approach one for equal and unequal sources; the largest included length is 160. These computational checks are finite and are not presented as certificates for the infinite claim.

The analytic proof relies on the published local limit theorem of Canfield, Janson and Zeilberger (2009), Theorem 4.5, with its applicability verified for compositions bounded away from the endpoints. The source's theorem, the Gaussian summation, the binomial composition integral, and the exact affinity change of measure are explicitly connected in `RESULT.md`.

No independent audit or externally certified proof has been performed. Uniformity in parameters as either parameter approaches zero or one is not claimed.
