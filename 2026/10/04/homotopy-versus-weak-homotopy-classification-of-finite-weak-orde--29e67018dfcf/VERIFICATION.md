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

The mathematical proof is analytic. The bundled `verify.py` is an independent finite stress test, not a substitute for the quantified proof.

It checks: (1) absence of beat points for six no-singleton level vectors; (2) the full mod-two simplicial homology of their order complexes by explicit boundary-matrix rank computation; (3) the pointwise inequalities and order preservation in the explicit singleton-level contraction; and (4) the example \(W(2,4,2)\), \(W(2,2,4)\).

The replay output on the packaged script ends with `VERIFY_OK`. The tested top Betti ranks are \(1,4,1,3,3,4\), matching \(\prod_i(r_i-1)\). No claim of exhaustive verification over all parameter values is made.

The decisive infinite steps are the structural arguments in `RESULT.md`: intrinsic level decomposition, beat-point exclusion, the exact join description, the cone-quotient join identity, Stong core rigidity, and McCord's weak-equivalence correspondence.
