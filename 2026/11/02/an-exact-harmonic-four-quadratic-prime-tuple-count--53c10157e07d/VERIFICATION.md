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
Run `python3 verify.py`. The script requires only Python 3 and its standard library. Its checks enumerate both roots of the parameter equation in 25 prime fields below 500 of cardinality \(7\pmod8\), as well as the degree-three extension \(\mathbb F_{343}\) defined using the irreducible polynomial \(U^3+U+1\) over \(\mathbb F_7\). Each case independently enumerates the simultaneous quadratic-character conditions, quartic character sum, boundary correction, and polynomial involution relation. A successful execution prints `VERIFY_OK field_cases=26`.

These finite checks establish the listed examples but do not certify the infinite theorem. The argument for all relevant prime powers is the algebraic proof in `RESULT.md`. No independent audit was undertaken.
