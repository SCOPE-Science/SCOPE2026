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

The proof was reconstructed from the published transmission formula and a direct Green-identity calculation for the boundary-normalized compact-graph solution. The critical slope is
\[
\Lambda'(E_0)=\frac{1}{c|\psi_0(v_0)|^2},
\]
which fixes all leading line-shape constants.

`verify_filter_linewidth.py` checks the exactly solvable interval with Neumann condition at the remote endpoint. It verifies the Dirichlet-to-Neumann derivative, exact half-maximum points, FWHM coefficient, and rescaled Lorentzian profile for several lengths, kinetic constants, eigenmodes, and coupling values. The replay prints `VERIFY_OK`.

The computational check is finite and illustrative; the all-graph result is supplied by the Green-identity and inverse-function proof in `RESULT.md`.

The main source was inspected in full text, including its exact transmission formula and conclusion. Related bandwidth work for distinct quantum-star and flat-passband filters was compared explicitly. No independent audit has been performed.
