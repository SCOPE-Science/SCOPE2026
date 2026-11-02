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

# Exact verification and boundaries

The standalone file `verify_hesse12.py` needs Python 3 and SymPy. Running `python3 verify_hesse12.py` reproduces the characteristic-three reductions of twelve input conics, nonzero Hessian determinants on \(t\notin\{0,1\}\), the smooth three-branch contacts, the residual-conic cubic intersection identity, ordinary coordinate nodes, the exact 9+12 marked-point specialization patterns, and the genus/delta consistency identity. Success prints `HESSE_12_CONICS_CHAR3_NINEFOLD_COMPONENT_THREE_DELTA7_TRIPLES_OK`.

The proof of completeness of the six singular points and the exact local intersection multiplicities requires the explicit elimination and Bézout calculations in RESULT.md. The symbolic checks are identities in \(\mathbb F_3[t,x,y,z]\), rather than a finite enumeration offered as an infinite proof. Characteristic-three parameters \(t=0,1\) are excluded. This is the special fiber of one particular published integral presentation, not the universal stable reduction of the configuration.

Independent external mathematical audit and validation have not been performed.
