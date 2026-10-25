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

## Reproducibility

Run `python3 check_stable_limit.py` with SymPy. Its assertions check the defining quartic identity, the parametrized conic, the branch octavic, its characteristic-independent discriminant, the strict-transform substitution, and all gradient identities. A passing run is an exact polynomial-identity check, not an audit of the algebraic-geometric proof.

The argument for proper, smooth reduction uses blow-up charts and the smooth branch divisor. The order-two inertia and its minimality use the explicit action \(s\mapsto-s\), \(w\mapsto-w\) and smooth proper base change. These mathematical steps are explained in RESULT.md; no standalone computation certifies the cohomological theorem.

## Limits

The residue field is algebraically closed and of characteristic not two or three. Prior literature includes the source quartic family, stable reduction type classifications, and the octahedral curve itself. Closely relevant full texts were inaccessible and equivalent coverage may exist. Independent scientific validation has not been performed.
