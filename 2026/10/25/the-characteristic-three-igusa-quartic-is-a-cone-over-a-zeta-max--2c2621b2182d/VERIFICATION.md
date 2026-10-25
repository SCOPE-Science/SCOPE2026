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

# Exact computational checks and limits

Run `python check_igusa.py` in a Python environment with SymPy. The program verifies the polynomial translation identity modulo three, computes the finite list of rational singular points and rank-three Hessians of the four-variable base, and exhaustively evaluates its quartic over all \(40\) points of \(\mathbb P^3(\mathbb F_3)\) and all \(820\) points of \(\mathbb P^3(\mathbb F_9)\). The extension field is implemented exactly as \(\mathbb F_3[u]/(u^2+1)\). Observed totals are \(15\) rational nodal directions, \(25\) base rational points over \(\mathbb F_3\), and \(145\) over \(\mathbb F_9\).

The algebraic proof, rather than any finite enumeration, establishes that there are no further geometric singularities. The Weil trace formula and equality in the weight-two bound convert the two exact finite counts into the all-extension zeta function. No independent audit or external mathematical validation has been performed.
