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

The standalone `verify.py` was executed from the packaged path.

It constructs \(T^0(\Gamma(M))\) directly for the regular modules \(M=R=\mathbb Z/n\mathbb Z\) with \(n=2,3,4,5,8,9\). Torsion elements are detected from the defining annihilation condition, not supplied as labels. Edges are then built from the condition that the sum of two distinct nonzero module elements is torsion.

The checker exhaustively searches all subsets for total domination and all even subsets for paired domination, with a recursive perfect-matching test. It also replays the component-count formulas on a bounded grid of admissible parameter profiles.

Exact output:

```text
VERIFY_OK
Zmod_case=(2, 1, 2, True, None, None, [0])
Zmod_case=(3, 1, 3, False, 2, 2, [1, 1])
Zmod_case=(4, 2, 2, True, None, None, [0, 1, 1])
Zmod_case=(5, 1, 5, False, 4, 4, [1, 1, 1, 1])
Zmod_case=(8, 4, 2, True, 4, 4, [2, 2, 2, 3, 3, 3, 3])
Zmod_case=(9, 3, 3, False, 4, 4, [1, 1, 3, 3, 3, 3, 3, 3])
abstract_parameter_profiles_checked=110
```

The finite checks realize the two nonexistence boundaries and all three finite-value branches. They do not replace the arbitrary-module proof, which is the torsion-coset argument in `RESULT.md`.
