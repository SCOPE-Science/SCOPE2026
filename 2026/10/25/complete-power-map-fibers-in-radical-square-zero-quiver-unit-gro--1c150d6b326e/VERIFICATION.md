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

# Reproduction and scope

Execute `python3 verify_power_fibers.py` with a standard Python 3 installation. The program independently implements multiplication in the radical-square-zero path algebra, exhaustive element powers, and the theorem's predicted root fibers. Every group target is compared; no sampled target selection is used. Tests comprise 14 distinct small quiver/field configurations and nine exponents each (126 full-target cases); characteristic two and a nonprime finite field are represented. The same program independently checks the exact image-size, identity-fiber and Fortuin--Kasteleyn subset formulas.

Expected terminal output:

```
VERIFY_OK_SQUARE_ZERO_QUIVER_POWER_FIBERS 126 complete-target cases 5298 elements per exponent setting
SAMPLE_CYCLE3_Q5_K2_TORSION 152
SAMPLE_CYCLE3_Q5_K5_IMAGE 3904
```

These are finite verifications; the universal proof is algebraic. The checker does not establish originality and no independent mathematical audit has been performed. The literature's full 2012 article text was unavailable; stronger historical coverage cannot be excluded.
