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

# Reproducibility of exact algebraic checks

The accompanying `VERIFY.py` is standalone Python using only standard-library modules. From the directory containing this file, execute:

```text
python3 VERIFY.py
```

Expected final message: `ALL 24779 EXACT CHECKS PASS`.

The checker performs exact rational calculations of the Gram-orthogonal correction and the sketched Rayleigh shift for varied real diagonal eigenvalues and symmetric positive Gram matrices. It verifies the projective recurrence and the two critical bilinear identities, checks an exactly singular example at distortion \(\epsilon=3/5\), verifies exterior escape in the explicit diagonal family, and tests the proposed sharp one-step envelope against a deterministic collection of rational metrics. An explicit rational matrix shows the sharp possible quadratic Taylor coefficient at this distortion.

The non-rational general extremizing metric, sharp angular disk bound, unique projected solvability, universal convergence for every admissible sequence of sketches, and general sharp boundary are established analytically in `RESULT.md`. No finite test collection is asserted to establish an infinite universal statement. The program tests scientific mathematics only and makes no external network requests.
