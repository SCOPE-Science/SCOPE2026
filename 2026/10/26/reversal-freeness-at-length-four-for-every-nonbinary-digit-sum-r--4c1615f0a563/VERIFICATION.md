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
Run `python3 check.py` using Python 3 with standard library only. It independently computes each length-65536 prefix for moduli \(m=3,4,5,6,7,8\) by direct bit counts and by the recurrence \(t_m(j)=t_m(\lfloor j/2\rfloor)+j\bmod2\) interpreted modulo \(m\). It then verifies all two- and three-letter factor counts, exact permissible triple classifications, and the absence of any reflected factor of lengths four through ten. These checks are finite and do not establish the infinite claim alone; the accompanying mathematical proof does so using the valuation-one obstruction. The external independent audit has not been performed.
