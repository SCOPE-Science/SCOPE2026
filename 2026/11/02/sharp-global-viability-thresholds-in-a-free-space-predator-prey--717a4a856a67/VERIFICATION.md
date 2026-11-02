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

# Verification of the sharp viability theorem

The source's three polynomial differential equations are transcribed in `RESULT.md`. For all nonnegative species densities, the coordinate hyperplanes are invariant. At full habitat occupancy, the exactly derived free-space derivative is

\[
\dot s=(1-\alpha)p+\varepsilon\beta q+\xi r+(1-\varepsilon)pq-(1-\eta)pr-(\delta-\varepsilon\gamma)qr.
\]

Fixing the parasite density, concavity in the prey/predator allocation gives an exact two-edge minimum. Each edge flux is nonnegative precisely under its displayed square-root inequality; this establishes the full real-parameter theorem including boundary equality, not just a numerical test. Failure gives an outward-pointing initial state; success gives global invariance on a compact simplex.

`python3 verify.py` was run from the package staging directory. It reported:

```text
EXACT_CHECK_OK 5000 parameter tuples, 3222 inward and 1778 outward; boundary grid evaluations: 330000
Source reference outward flux: -39/1000
Source reference sharp xi cutoff: 9/10
```

The script uses `fractions.Fraction` to test 5,000 rational coefficient tuples, exact edge minimizers, 330,000 full-occupancy grid points and source-parameter threshold/witness cases. Finite cases cannot certify an infinite family. The proof in `RESULT.md` provides the unbounded quantifier argument. No numerical simulation is used to claim the existence of an impossible trajectory or of a global attractor.

Independent audit and independent validation have not been performed. A residual literature-priority risk remains because unlocated specialized results may exist.
