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

Python 3 standard library is sufficient. Execute, in the directory containing the two supplied source files:

```bash
python3 verify_price.py
python3 verify_orbits.py
```

**Observed results:** `VERIFY_OK profiles=46673 sharp_ratio=9/4 maximizing_profiles=144` and `VERIFY_ORBITS_OK profiles=46656 orbits=669 max_ratio=9/4`.

The first number \(46673\) includes the \(1+16+46656\) complete one-, two-, and three-pair profile domains; it is not a count restricted to three pairs. The separate orbit checker covers exactly \(46656\) three-pair profiles and obtains \(669\) orbits. Both programs use exact integer arithmetic and rational fractions, not simulations or floating point thresholds. The first also checks the exact sharp instance and the published stable-matching multiplicity marginals.

The mathematical claim is restricted to those finite domains. Executing these programs verifies the exhaustive finite certificate but does not constitute independent scientific audit, generalization, or a claim of priority.
