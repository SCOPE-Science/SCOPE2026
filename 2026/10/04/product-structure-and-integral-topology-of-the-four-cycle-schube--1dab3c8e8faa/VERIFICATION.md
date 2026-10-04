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

The verification artifact `verify.py` performs exact symbolic-coefficient checks without numerical approximation. It verifies the Pluecker identity for the displayed parametrization, the factorization \(p_{34}=ad(1-xy)\), the coefficient convolution giving \(1+3t+4t^2+3t^3+t^4\), the Hodge--Deligne expansion, and the source formula at \(d=4\).

The algebraic isomorphism itself is established by the explicit mutually inverse regular maps in `RESULT.md`. The homology statement uses Alexander duality for \(\mathbb C^2\setminus\mathbb C^*\) and the integral Kunneth theorem; the script is a consistency check, not a substitute for those arguments.

Unproved limits: no assertion is made for other cycle arrangements, for arbitrary relabelings not induced by the stated coordinate instance, for real topology, or for the full mixed Hodge structure.
