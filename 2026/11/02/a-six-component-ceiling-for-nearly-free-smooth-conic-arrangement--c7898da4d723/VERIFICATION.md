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

# Verification scope

The scientific argument is elementary after invoking the published nearly-free syzygy identities, Dimca--Sernesi lower bound, and Zieliński orbifold inequality, all stated with precise domains in RESULT.md. Exact symbolic elimination gives the necessary inequality \(271u+333n+462s\le2800k-458k(k-1)\). At \(k=8\) the right side is negative. At \(k=7\), all compatible nonnegative pairs \((u,n)\) fail the required residue identity.

The independent verifier `verify_cutoff.py` is standard-library Python, requires no external input and inspects the finite, rigorously bounded weak-combinatorics integer cases at \(k=7,8\). Executing `python3 verify_cutoff.py` on the packaged file produced:

```
k=7: certificate_rhs=364, preliminary_pairs=[(0, 0), (0, 1), (1, 0)], admissible_count=0
k=8: certificate_rhs=-3248, preliminary_pairs=[], admissible_count=0
CONIC_CEILING_EXACT_OK
```

The enumeration is a secondary exact arithmetic check, not a computation over arbitrary geometric arrangements. No numerical sampling certifies the published foundational theorems; their stated hypotheses and formulas were examined in the primary full-text articles. No external independent audit has been performed.
