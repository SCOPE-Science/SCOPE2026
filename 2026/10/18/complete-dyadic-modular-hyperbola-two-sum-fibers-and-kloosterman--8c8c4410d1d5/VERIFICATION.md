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

The unrestricted theorem is proved by congruences and complete dyadic square-root classification; direct finite enumeration is not used as an infinite proof. The collision calculation independently cross-checks the entire sum of squared fiber multiplicities. For a fixed first sum of valuation one, the proof reduces the collision probability to the valuation of the product \(\ell(c-\ell)\) and evaluates every valuation layer exactly.

Execute `python3 check_fibers.py` with Python 3. The program enumerates all ordered pairs of odd units and compares every two-coordinate fiber with the closed arithmetic formula for exponents 2 through 10 inclusive, including zero cases. It asserts the sumset-energy formula on each ring, and separately checks directly computed complex Fourier fourth moments for exponents 2, 3, 4 and 5 against two-dimensional orthogonality.

Observed output ends with:

`VERIFY_OK exact_fiber_positions=1398096 exponents=2..10 direct_complex_fourth_moments=4`

Finite enumeration covers precisely those finite moduli, and floating-point comparisons for four small Fourier transforms use a relative numerical tolerance. Neither check extends to arbitrary modulus or provides independent scientific certification. Historical priority remains subject to additional source inspection, notably full text of Zhang (2011).
