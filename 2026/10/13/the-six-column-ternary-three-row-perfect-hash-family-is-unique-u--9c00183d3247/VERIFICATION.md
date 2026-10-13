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

Run `python3 verify.py`. The verifier constructs all \(27\) ternary columns, checks every seven-subset and six-subset against the definition of \(\operatorname{PHF}(3;k,3,3)\), and asserts that there are no size-seven families and exactly \(36\) size-six families.

For every maximum it checks row multiplicities \(2,2,2\), constructs the three equal-symbol matchings, and verifies that their union is a \(K_{3,3}\). It then exhausts all \(1296\) row/symbol relabelings on a representative, proving one orbit of size \(36\) and stabilizer order \(36\). Finally, it checks the independent count \(10\cdot2\cdot3!\cdot(3!)^3=25{,}920\).

The search is exhaustive over a finite universe; no probabilistic or timeout-based inference is used. It proves only the stated finite parameter and does not establish any asymptotic perfect-hash claim.
