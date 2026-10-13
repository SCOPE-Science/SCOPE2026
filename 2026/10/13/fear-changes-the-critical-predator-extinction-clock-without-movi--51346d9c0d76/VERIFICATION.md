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

# Verification of the exact critical extinction clock

The proof consists of global positive comparison, strictly negative Bendixson--Dulac divergence, analysis of boundary saddles, a nonautonomous scalar linear quotient equation, and a Cesaro-limit step for \(1/v\). No finite test is used as proof of global convergence or infinite-time asymptotics.

`python -m pip install -r requirements.txt` then `python verify.py` validates with exact SymPy rational arithmetic: the per-capita prey identity (after substituting the prey-only equilibrium equation), the predator/prey ratio identity at \(m=cbu_1\), the signs and exact expressions for both fear derivatives, and the exact rational example with limit coefficients \(1/2\). The checker prints `VERIFY_OK` on success.

No computer algebra proves the Poincaré--Bendixson application: the argument in `RESULT.md` establishes local attractiveness of the sole interior fixed point, absence of interior loops, and impossibility of a closed boundary connection graph. An initial state on a coordinate axis is excluded from the critical rate theorem. Independent audit: not performed.
