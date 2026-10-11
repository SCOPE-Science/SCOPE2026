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

The verification is finite and exhaustive. `artifacts/verify.py` reconstructs the \(48\) edges from the thirty-two published facets, computes the cocycle and coboundary ranks over \(\mathbf F_2\), extends a coboundary basis to a cocycle basis, and enumerates all \(131072\) cocycles. It therefore checks every representative of every cohomology class, not a sample.

The same program reconstructs the permutation group from the four published generators, verifies that its order is \(192\), checks that each element preserves the facet set, computes the induced action on \(H^1(K;\mathbf F_2)\), and exhausts the action on all minimum supports.

The replay output is stored in `artifacts/verification_output.txt`. The asserted class-orbit triples are \((6,16,1)\), \((10,24,4)\), \((12,6,8)\), \((14,16,18)\), and \((16,1,12)\). The support-orbit partitions at those weights are \(16\), \(48+48\), \(24+24\), \(96+192\), and \(12\).

The verification proves only the combinatorial \(\mathbf F_2\) statement for the specified labeled triangulation. It does not address other triangulations, other coefficient fields, or geometric edge lengths.
