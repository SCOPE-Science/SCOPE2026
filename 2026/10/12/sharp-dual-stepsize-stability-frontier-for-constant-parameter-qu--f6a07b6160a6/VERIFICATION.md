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

# Verification evidence and limits

The proof reduces APAPC's exact quadratic core to independent real singular modes. It checks all three necessary-and-sufficient quadratic Schur inequalities, proves strict positivity of the first two, and identifies the third with the claimed sharp parameter boundary. A scalar singular-vector initialization creates the \(-1\) root at equality and a root less than \(-1\) beyond the boundary. Averaged primal and dual outputs satisfy scalar contractive filters.

The accompanying `verify.py` is standalone, uses the Python standard library and exact rational arithmetic, and checks the update-to-matrix identities, characteristic polynomial coefficients, Schur conditions, rational threshold equivalence, and an equality witness. Running `python verify.py` must report `VERIFY_OK`. Independent floating-point eigenspectrum checks were also run on 3,000 parameters. These are finite consistency tests, not substitutes for the algebraic universal proof.

This theorem does not address nonzero smooth gradients, nonquadratic penalties, varying parameters, endpoint convergence for every initialization, infinite-dimensional bounded operators, or full objective convergence guarantees outside the specified quadratic problem. Prior work already supplies the limiting undamped \(4/3\) boundary; broader historical equivalents remain a literature risk. No independent audit or external certification has been performed.
