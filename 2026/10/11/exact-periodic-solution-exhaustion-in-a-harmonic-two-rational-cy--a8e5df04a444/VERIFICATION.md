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

# Verification details

For every \(g>v>0\), \(w>s>0\), \(k>0\), the symbolic equalities and half-cycle comparison establish the exact claim. The proof relies on uniqueness and local Lipschitz regularity of the transformed equation away from \(x=0\), which holds for any hypothetical nonzero entire periodic solution. The sign of \(F_--F_+\) at a coincidence is fixed and nonzero; the two half-trajectories cannot have common values at both endpoints.

The numerical checker `verify.py` uses a fourth-order Runge--Kutta return integration and Simpson quadrature. It directly checks both constructed curves against the differential equation at sample phases, signs of return displacement in regions between roots, and multiplier agreement with the positive integral representation. The checker does not establish the global absence of unknown solutions or rigorous error bars. Those facts are proved analytically in `RESULT.md`; the tool's output is an additional finite consistency check, not an external certificate.

Independent audit has not been performed.
