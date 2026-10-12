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

The bundled `verify.py` performs exact arithmetic over \(\mathbb F_2\). It checks the paired generator group order \(168\); the unique perfect intertwining pairing between the two three-dimensional reduction factors; uniqueness of the invariant alternating form; nondegeneracy of the hyperbolic form; invariance, polarization, and \(36/28\) value split of \(q\); absence of nonzero invariant linear functionals; the full orbit decomposition \(1+7+7+21+28\); and all sixteen nontrivial ordered rows of the orbit-addition fusion table.

The finite computation is exhaustive on the \(64\)-element two-torsion space. It does not attempt to certify statements about odd-order torsion, the full Jacobian outside two-torsion, or absence of equivalent formulations in unindexed literature. The published orbit lengths and invariant-theta facts are used as consistency checks rather than novelty evidence.

Expected success line:

`VERIFY_OK group=168 module=V+Vdual pairing_space_dim=1 invariant_alt_dim=1 q_zero=36 q_one=28 orbits=1+7+7+21+28 fusion=verified`
