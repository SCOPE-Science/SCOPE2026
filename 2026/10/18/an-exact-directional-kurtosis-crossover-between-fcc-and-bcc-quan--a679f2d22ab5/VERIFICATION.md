---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The displayed FCC and BCC Voronoi halfspace systems follow from all even/two-odd D3 lattice vectors and all even/all-odd BCC lattice vectors, respectively. In the signed-permutation FCC chamber x1>=x2>=x3>=0, x1+x2<=1, simplex Jacobian is 1/4; BCC positive octant is the 3/2-simplex minus three disjoint translated 1/2-simplices. Exact rational independent integration reproduced volume (2,4), radial second (3/8,19/32), fourth (41/240,409/960), sixth (1397/16128,27217/80640), A=E Xi^4 (3/80,89/960), C=E Xi²Xj² (7/720,71/2880). Cubic invariance yields K_F=(28+8w)/15, K_B=(3408+864w)/1805, w=sum_i u_i^4∈[1/3,1], difference 4(74w−29)/5415, sharp crossing w=29/74. Recomputed radial gaps R4=308/48735 and R6=1758278/58335795, positive. Independent rational sums were NOT based solely on the saved verifier.

## originality

PASS

Classical quantizer optimality compares mean-square error or second moments; no inspected source states the orientation-specific quartic comparison surface at w=29/74 plus two radial higher-moment gaps for these aligned Voronoi cells. The exact quadrature method is textbook, but the paired moment and sharp sign reversal are not found in checked primary statements. Priority risk: older quantization/crystallographic higher-moment tables.

## value

PASS

Scale-free cubic directional kurtosis tests how lattice quantization errors depend on measurement direction. The exact sign reversal, transition locus on S² and simultaneous disagreement with higher radial moment ordering supply a physically motivated boundary not recoverable from classical second-moment optimality. Both cells and invariants are standard, not arbitrary small slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
