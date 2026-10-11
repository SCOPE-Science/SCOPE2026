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

# Exact reproducibility

Run `python3 verify_octahedral_matching.py` using Python 3 and no third-party packages. It constructs the ordinary matching complex from six graph vertices and the three omitted antipodal edges. It verifies the entire face vector \((12,30,8)\), the incidence of free faces, eight elementary collapses, connectedness of the residual graph, and an explicit basis of eleven integral cycles.

The verifier independently computes all forty-eight exact integer homology action matrices from fundamental graph cycles, including reduction modulo the removed triangle boundaries. It tests every one of the \(48^2=2304\) group composition identities, calculates signed simplicial-chain Lefschetz traces separately, confirms the ten conjugacy-class values, and takes inner products with the ten rational \(S_4\times C_2\) irreducible characters. The asserted multiplicities are four copies of distinct irreducibles, each with multiplicity one, and zero for all others. Successful completion prints `VERIFY_OK`.

The group-representation computation uses integer arithmetic without floating-point approximation. The full homotopy conclusion follows from the general elementary-collapse argument in `RESULT.md`, not from extrapolating the finite verification to other graphs. No independent audit was performed.
