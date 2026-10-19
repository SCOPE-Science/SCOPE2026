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

Run `python3 verify_parity.py` with standard Python 3. The program constructs weighted necklace coefficients from the formal formulas and independently enumerates canonical rooted-tree/cycle/component objects, comparing the two counts with exact signed Burnside sums. It also conjugates every labeled map on \(2\) through \(5\) points by explicit even and odd permutations. The program prints `CHECKER_OK` only after all assertions pass.

The actual packaged run returned `CHECKER_OK`, symmetric counts \(1,3,7,19,47,130,343,951,2615\) and split counts \(1,1,4,9,20,45,111,276,666\) in degrees \(1\) through \(9\), with direct labeled cases verified through degree \(5\). The signed partition arithmetic was checked through degree \(15\). These tests do not establish a theorem for all degrees; the proof supplies that scope. No external independent audit was performed.
