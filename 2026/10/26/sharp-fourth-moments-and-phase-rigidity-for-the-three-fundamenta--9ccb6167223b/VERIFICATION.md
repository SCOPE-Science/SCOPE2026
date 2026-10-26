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

Execute `python3 check_su4.py` using Python 3 standard library; no external packages are required. It constructs the defining, dual and exterior-square \(SU(4)\) torus characters as integer Laurent polynomials, builds the squared Weyl denominator, and uses \(\frac1{24}\operatorname{CT}\) to compute Haar products. It compares the entire integer Gram matrix to the character-decomposition calculation. It also tests 216 Gaussian-integer coefficient combinations and the rational extremal profile. The text `verification_output.txt` records the observed run.

For the full analytic check, reconstruct the two-line moment polynomial from the six character product decompositions in `RESULT.md`, apply \(\operatorname{Re}w\leq |w|\), set \(S=|a|^2+|b|^2\) and \(p=|ab|\leq S/2\), and complete the square at \(z^2=5N/11\). Inspect the displayed exact deficit and derive its equality conditions. This proof, not finite samples, supports the universal quantifier.

Limitations: The checker independently tests the representation-theoretic coefficients but does not give an external mathematical audit or verify scientific priority. Independent audit has not been performed.
