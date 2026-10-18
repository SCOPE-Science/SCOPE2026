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

# Reproducibility

Run `python3 verify.py` in this directory. No third-party libraries, downloaded data, or special environment variables are required.

The verifier constructs the quadratic-residue graph, its thirteen neighborhood facets and all \(598\) nonempty faces. It establishes the mod-two ranks of the second, third, and fourth boundary matrices as \((66,130,65)\); enumerates exactly \(104\) missing tetrahedra whose boundaries define nontrivial ambient mod-two classes; calculates the three affine orbits with representatives \(\{0,1,3,9\}\), \(\{0,1,3,11\}\), \(\{0,1,6,8\}\) and sizes \((26,39,39)\); and checks that their individual mod-two homology spans have dimensions \((24,25,25)\).

The integral steps use a star spanning tree to identify the one-cycle lattice with \(\mathbb Z^{66}\). The checker selects a \(66\)-column triangle-boundary minor with exact determinant \(-1\), yielding an integral \(155\)-coordinate basis of second cycles. In each size-\(39\) orbit it selects \(130\) three-boundary columns and \(25\) four-point sphere-cycle columns whose \(155\)-square determinant is exactly \(-1\). These explicitly checked lattice certificates, along with the characteristic-zero rank bounds, prove full integral generation and exclude hidden torsion in degree two.

Limitations: the exact calculation is for the single order-thirteen Paley graph. The method does not compute all relations among the \(104\) cycles, nor assert a classification for other graphs. The checks have not undergone independent scientific audit.
