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

Run `python verify.py` with the supplied file unchanged. It uses only the Python standard library.

The verifier reconstructs the 12-vertex simplicial complex from all 72 published facets and obtains face vector \((12,60,160,180,72)\). It checks two explicit integer 2-cochains against every tetrahedral boundary, exhausts all 495 four-vertex sets, and verifies exactly 60 missing tetrahedra with cochain evaluations \((\pm1,0)\) or \((0,\pm1)\). The corresponding unoriented support multiplicities are 30 and 30.

The verifier also closes two explicit vertex permutations to a group of order 240, checks every group element preserves the full facet set, and checks that the orbit of one minimum support is the complete 60-support set.

The inference from cochain evaluation to a complete integral homology classification uses the independently published premise \(K\cong S^2	imes S^2\), hence \(H_2(K;\mathbb Z)\cong\mathbb Z^2\). The finite verifier does not substitute experimental rank checks for that topological premise.

Expected output:

`VERIFY_OK f=12,60,160,180,72 missing4=60 class_supports=30,30 cocycles=2 symmetry_group=240 support_orbit=60`
