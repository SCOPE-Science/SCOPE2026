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

The claim is finite-dimensional and was checked symbolically.

For a finite Bessel family with Gram matrix \(G\), the focal theorem supplies a finite positive-weight decomposition by rank-one matrices \(zz^*\) with \(z\) in the unit polydisk. For every \(v\in\ker G\), the identity
\[
0=v^*Gv=\sum_s p_s|z_s^*v|^2
\]
forces every representing \(z_s\) into \(\operatorname{Ran}G\). This is the critical step that makes the bound depend on rank.

The set of admissible representing vectors inside the range is compact and convex, hence its rank-one image is compact and connected. The real dimension of Hermitian operators on a complex \(r\)-space is \(r^2\); the real dimension of symmetric operators on a real \(r\)-space is \(r(r+1)/2\). The Hanner--Rådström connected-set refinement of Carathéodory therefore gives the stated number of atoms.

The proof establishes only upper bounds. It does not prove that these atom counts are minimal, and it makes no finite-support claim for arbitrary countably infinite Bessel sequences. The case \(G=0\) is separately realized on one atom by zero functions.
