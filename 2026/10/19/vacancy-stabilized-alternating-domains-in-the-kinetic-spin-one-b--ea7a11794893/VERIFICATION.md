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

To reproduce the independent finite-state checks, run `python verify_blume.py` using Python 3. The program evaluates exact rational local flip energies for every configuration of cycles of sizes 3 through 11, at eight representative crystal-field ratios including both threshold equalities. It also verifies the cyclic renewal polynomial through size 28 by a separate formal-series integer recurrence. Actual successful output: `PASS: 72 direct Hamiltonian checks and 26 renewal-polynomial coefficient checks.`

Analytical checks: derive \(e_i(t)=D t^2-Jt(s_{i-1}+s_{i+1})\); verify each neighbor-sum case, the even number of vacancy separators, and the pointed cyclic-block factor \(2n/k\). The pole of \(2x f\partial_x f/(1-f^2)\), with \(f=zx^3/(1-x)\), gives \(\lambda(z)^3-\lambda(z)^2-z=0\). Its derivative at \(z=1\) yields the vacancy density. Finite enumeration does not establish the infinite-volume limit or originality.
