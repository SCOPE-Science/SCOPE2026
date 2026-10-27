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

# Reproduction and verification

Install the dependencies in `requirements.txt` and execute `python verify.py` with the files placed together. The checker reconstructs \(K_G(h)=\sum_{k=0}^4(-hL_G)^k/k!\) from exact integer Laplacians and checks 740 independent upper-triangular non-diagonal matrix entries against the proof's normalized polynomial classes. It verifies row sums, seven globally decreasing nearest-neighbor cubics via exact discriminants, five globally positive distance-two quadratics, the diagonal sum-of-squares identity, exact rational endpoint inequalities, exact rational intervals for all four nonrational thresholds, and path distance-three degree-sum identities. SymPy uses exact rational arithmetic, not fitted coefficients or numerical tolerances.

The infinite families are proved analytically by the graph classification and the fact that a degree-four matrix polynomial uses at most four-step walks. The program's finite cases do not establish an unbounded conclusion by themselves. Rounding the displayed roots is not a sign or uniqueness certificate; rational isolation and derivative arguments are the relevant checks. No assertions concern nonlinear RK4 stages or weighted diffusion. Independent validation has not been performed.
