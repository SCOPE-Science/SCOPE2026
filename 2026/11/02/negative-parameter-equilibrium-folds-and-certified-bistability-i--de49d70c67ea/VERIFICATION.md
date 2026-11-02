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

# Algebraic verification

Run `python check_negative_etm.py` with Python 3 and SymPy. The script reconstructs the printed differential equations, eliminates the two linear equilibrium equations, and checks the quartic identity. It independently recomputes the exact polynomial discriminant, the negative-root Sturm sign variations and isolations, sample quartic root counts, and the two exceptional zero-root parameters.

For the explicit bistability witness at \(\rho=-2\), it checks the cubic factor discriminant, the interval bracketing its unique real zero, and the Jacobian characteristic-polynomial identities. The positivity of the displayed coefficient polynomials on \(6/5<t<5/4\) and Routh--Hurwitz are part of the human-readable proof, rather than empirical extrapolations from the script.

The first public source date is the initial arXiv posting on 2026-10-03. Source coverage is based on a read of the paper's full accessible HTML text and the closest published positive-branch result. This is a mathematical check without independent verification, and does not assert a complete literature census.
