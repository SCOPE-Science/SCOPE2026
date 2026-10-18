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

# Verification details

The standalone checker `verify.py` uses only Python's standard library. From the actual included source file, run `python3 verify.py`. It checks the identity for \(\bigl((a+b)(a+c)(b+c)\bigr)^2\) by exhaustive enumeration of the relevant degree-six semistandard-tableau Schur polynomials. For each \(3\le n\le12\), it computes both Plücker degrees by (1) the complementary Schubert partition and hook-length formula and (2) independent Vandermonde coefficient extraction from the ambient Grassmannian integral; the values agree exactly. It also checks the closed degree ratio against exact fractions in these cases.

More importantly for the infinite assertion, the script multiplies integer coefficient arrays representing the rational expressions' numerator and denominator, and checks **coefficientwise polynomial identities** for the full Schur sum and both factorized strict-bound numerators. These identities are exact for every value of their variable, not extrapolations from the ten sample dimensions. The accompanying written proof supplies regular-section intersection theory, Pieri multiplication, positivity on the given domain, and the ring-theoretic top-power argument; no finite computation is substituted for these theorems.

The source's geometric smoothness and additive cohomology theorem are cited inputs. The uninspected in-preparation related manuscript may contain prior calculations. Neither unavailability nor unsuccessful literature searches certify novelty. Independent audit or validation has not been conducted.
