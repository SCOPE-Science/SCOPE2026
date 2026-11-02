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

`verify_periods.py` is standalone Python 3 using only `math` and `fractions`. Execute `python3 verify_periods.py`. It verifies all integral branch endpoints and the permutation induced on unit cells for \(1\le n\le50\), then checks the complete \(1440\)-cell permutation for \(R_{11,7}\) and its exact period masses. There is no numerical rounding. All included discontinuity boundaries are represented by the left-closed/right-open cell convention.

The infinite three-piece least-period law has a separate analytic proof: induction of integer rotation modulo \(S\) with \(\gcd(S,t)=1\) and return-section length \(L\). The checker is supplementary evidence, not an infinite certificate. The four-piece result is finite and fully exhaustive; it relies on the elementary fact that integer translations preserve the fractional part inside each unit cell.

The self-review assessed correctness, literature overlap and value; independent audit was not performed. The general pair classification and broad publication priority remain open.
