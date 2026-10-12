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
# Verification
The cited input is Laga--Shnidman's exact involution count: four \(\tau\)-fixed bitangents and twelve \(\tau\)-pairs. The additional proof checks the complete list of projective lines fixed by the order-three subgroup and the intersection divisor on each type.

The bundled `verify.py` performs exact symbolic checks with SymPy: the horizontal bitangent square identity, the discriminant of the \(Y=0\) section, the projective restriction to \(X=uZ\), and the integer orbit-count equations. The finalized embedded checker was extracted and rerun after packaging. It returned:

`VERIFY_OK orbit=1+3+4x6 mu3_fixed=1 tau_fixed=4 prym_pairs=4x3`

The computation does not enumerate all 28 bitangents and is not used as a substitute for an exhaustive proof. Exhaustiveness comes from the projective eigenspace classification of order-three invariant lines together with the source's exact involution lemma. The Prym statement uses the source's Proposition 7.19 and equivariance of the construction under the commuting \(\mu_3\)-action.
