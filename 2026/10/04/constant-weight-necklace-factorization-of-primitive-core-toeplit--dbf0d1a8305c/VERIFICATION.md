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

The proof has two logically independent parts.

First, from the published root-product formula, a primitive degree-\(d\) core over \(\mathbb F_Q\) has canonical modes \((-1)^k\alpha^{E_I}\), where \(E_I\) is the base-\(Q\) indicator sum of a \(k\)-subset. For \(1\le k<d\), these indicator sums are distinct integers strictly below \(Q^d-1\), so primitivity of \(\alpha\) makes the modes distinct. Raising a mode to the \(Q\)-th power cyclically rotates the indicator digits, giving the claimed Frobenius orbits and therefore the irreducible factors.

Second, an orbit of size \(d/h\) is an \(h\)-fold repeat of an aperiodic word of length \(d/h\) and weight \(k/h\). Möbius inversion on word period yields the factor-count formula in the finding.

The standalone script `verify_necklace_factorization.py` checks the orbit-count formula for every \(2\le d\le10\) and every \(1\le k<d\). It also implements exact arithmetic in binary extension fields, finds primitive cores, forms the mode factors from Frobenius exponent orbits, and verifies base-field coefficients and predicted degrees for \((d,k)=(4,2),(5,2),(6,2),(6,3)\). The saved output ends with `CHECK_OK`.

These computations do not prove the arbitrary-field theorem; they are consistency checks for the symbolic proof. No external independent audit has been performed.
