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

Run `python3 verify.py` from the directory containing the standalone checker. Only Python's standard library is needed. All projector and positivity operations in the five exact examples use `fractions.Fraction`; no floating-point computation is used to decide a sign, nullspace dimension, or matrix identity. The printed decimal \(LDL^{\mathsf T}\) pivot summaries are merely displays of exact rational pivots, not eigenvalue estimates.

The program enumerates four-cycles and their edge sets, searches for distinct pairs meeting precisely at each prescribed root edge, and checks that alternating signed cycle vectors lie in the unsigned-incidence kernel and have isolated coordinatewise products. In five exact test graphs, it constructs the orthogonal projector onto that kernel, checks its symmetry, idempotence, and incidence-nullspace property, and confirms that every rational pivot of \(P\circ P-I_m/(16m)\) is positive. It separately checks cycle witnesses for \(Q_d\), \(3\le d\le7\), and confirms the certificate hypothesis fails for \(Q_2\).

Successful replay ends with:

```
VERIFY_OK exact_projectors 5 certificate_edges 861 cycle_witnesses 1087 nonexample_Q2_confirmed
```

The finite checks validate the implemented instances but cannot certify the theorem for all graphs or dimensions. The general proof is the alternating-cycle/Schur-compression argument in RESULT.md, including the requirement that every Cartesian factor have no isolated vertices.
