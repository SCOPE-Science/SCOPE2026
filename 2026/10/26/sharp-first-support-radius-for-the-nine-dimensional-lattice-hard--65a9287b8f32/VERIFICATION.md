---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the full Z^9 nearest-neighbor graph with zero values at the origin and outside B_R, expansion of undirected edge squares gives the Dirichlet matrix L=18I-A, not the Laplacian with the internal degree on the diagonal. For a positive w on B_11, expanding the weighted internal squares in the stated ground-state identity leaves the diagonal residual (Lw-49w/(4||x||_2^2))/w. Thus positivity of that residual proves strict positivity for every nonzero complex test, not just invariant or nonnegative ones. Independent replay with /workspace/reviews/evidence/hardy_replay.py (Python standard library, argument: frozen record directory) regenerated labels via coordinate multisets, cross-checked their multiplicities against the direct lattice ball count, and found all 191 integer residuals positive, with minimum 1458 (covering 7059734 sites). For B_12 it evaluated the energy directly by edge squares, counting each edge outward from its smaller l1 norm endpoint and adding the origin edges, rather than reusing the frozen Laplacian-defect sum. The 264-orbit witness (14218904 sites) gave exactly 4E-49H = -168023799157855578188041899511220364510317/66816567612546192522086437300. Nesting excludes all smaller radii. These are exact finite certificates at the stated coefficient and for the stated support sets only.

## originality

PASS

Best-of-knowledge distinct for the first graph-distance (l1) support radius, not for strict global failure of the continuum coefficient or for the use of a ground-state certificate. The close squared-Euclidean Resultary theorem gives neither half of this cutoff by inclusion. No priority is inferred from catalog dates.

## value

PASS

The radius is intrinsic to the nearest-neighbor graph: it gives the least graph distance from the puncture needed for instability at the continuum threshold in the first globally failing dimension. Eventual finite-support failure does not say which local neighborhoods rule it out. Exact positivity for all tests through eleven steps and a strict witness at twelve give a meaningful boundary for finite-volume Hardy or spectral analyses; the Euclidean cutoff cannot replace it. It does not compute a new global optimal constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
