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
The proof is analytic and holds for all integers \(a,b\ge2\). The exact-rational checker `CHECKER.py` independently constructs the full edge-space projection columns for the integer rectangle \(2\le a,b\le8\), verifies that every gradient is fixed, evaluates both operator norms, and checks rational identities, parameter ordering, and the two orthogonal-optimality thresholds. Run it using only the Python standard library:

```
python3 CHECKER.py
```

Observed output: `CHECK_OK 49 parameter pairs, 1813 edge columns, exact rational identities`.

As an additional noncertifying numerical cross-check, unconstrained finite-dimensional linear programs for \((a,b)=(2,2),(3,2),(3,3),(4,2)\) gave the analytical minima on both sides to tolerance \(10^{-8}\). The finite tests do not establish the universal theorem; its proof is the invariant normal-form classification and the sharp lower-bound inequalities in `RESULT.md`. No independent mathematical audit was performed.
