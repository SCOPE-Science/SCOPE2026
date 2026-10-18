---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For R=G-A, the exact PSB update in a unit basis direction p is (I-pp^T)R(I-pp^T); commuting coordinate projections give R_S=P_{S^c}(LI-A)P_{S^c}. Since LI-A is positive semidefinite, a zero diagonal deficit entails its entire row/column vanish. Thus greedy positive scores are invariant until chosen, exactly s positive directions require updates, and quadratic Hessian variation has M=0. The primary MGPSB algorithm (36) performs t internal plus one final refinement per outer step, so G_q=A after ceil(s/(t+1)) steps (q=0 if s=0); the following primal solve is exact. In a diagonal Hessian with distinct positive deficits, error in the last selected coordinate persists before the final Newton step, establishing sharp worst-case count. Independently reconstructed exact-rational non-diagonal projection mask and s=5,t=1 batching example; no inference from finite tests alone.

## originality

PASS

The source paper combines a single-update quadratic finite termination theorem with a different general nonlinear multi-update rate theorem. Its equations (2),(3),(36) do not give the invariant initial deficit ordering, exact s reduction or sharp multi-update outer-iteration count. The exact-specific algorithmic count is not entailed by a generic at-most-n termination statement. Relevant preprints and database aliases were compared.

## value

PASS

The all-dimension exact identification law separates costly outer primal iterations from matrix refinements, determines when zero initial deficit directions need no work, and supplies a sharp worst-case solve count. This is a motivated exact complexity refinement for an actually published quasi-Newton variant, not just a restatement that PSB converges finitely.

The dated certificate retains the supplied scientific assessment, sources and limitations.
