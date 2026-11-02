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

# Reproducibility and limitations

Run `python verify.py` with Python 3, NumPy, and SciPy. The executed output was:

```
CHECK_OK planes=3 incidence_edges=777 lp_instances=282
```

The checker constructs the incidence graphs of the prime-field projective planes of orders \(2\), \(3\), and \(5\). It checks integer incidence identities and all graph shortest-path distances, verifies the constructed Kantorovich dual potential, evaluates the heat matrices directly by matrix exponential at three positive times, and solves exact finite-dimensional **linear programming formulations** of Wasserstein-one transport (numerical solver tolerance checked). All vertex pairs are tested for the Fano plane. The large-order closed-form limit is also tested numerically.

The mathematical proof in `RESULT.md` is self-contained except for elementary finite projective plane axioms, Hall's matching theorem, and Kantorovich duality. The infinitely many possible orders and non-Desarguesian planes are handled by analytic incidence-count and matching arguments, **not** by finite computation. The checker cannot establish historical priority or mathematical independence. No independent external audit has been performed.
