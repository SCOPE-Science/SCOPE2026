---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

At pinned RESULT.md, B_c=[[1+beta−eta c,−beta],[1,0]], P=B_bB_a; independent symbolic multiplication confirms determinant beta² and trace (1+beta−eta a)(1+beta−eta b)−2beta. Substitution in the strict quadratic Jury conditions yields 1−tr+det=eta ab(C−eta) and 1+tr+det=ab(eta−C/2)²−Delta/(4ab), proving the complete open two-island/isolated-point classification for all a,b>0, 0<=beta<1 and arbitrary initial pair. Independently multiplied witness a=9,b=1,beta=1/2,eta=3/2 to P=[[-1/2,0],[-12,-1/2]], and checked eta=1/2 has spectral radius>1. Determinant yields radius>=beta, attained exactly by eta=(1+beta)/a or /b with both eigenvalues −beta; for beta=0 nilpotence gives finite termination.

## originality

PASS

A fixed-period two-curvature, constant-step scalar heavy-ball monodromy has a sharp disconnected Schur region with exact momentum/contrast cutoff, including stable phase-cancellation resonances. The full-gradient heavy-ball literature has a single Hessian and the closest Tseng 1998 incremental-momentum paper has adaptive stepsize safeguards; neither accessed theorem supplies the presented fixed-two-cycle if-and-only-if region. Nearby semantic results concern asynchronous AdaShift or cyclic block minimization, with different transfers. The 1998 full text could not be retrieved through the institutional connection, explicitly a priority risk.

## value

PASS

Sharp stability boundaries for constant-step incremental momentum differ qualitatively from conventional monotone stepsize rules; a stable larger eta after unstable smaller eta and exact globally optimal phase-cancellation resonances are mathematically motivated, testable controls with explicit limitations on robustness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
