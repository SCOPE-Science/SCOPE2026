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

The standalone checker reconstructs the simplicial complex from `source_facets.txt` and verifies the following exact facts over \(\mathbf F_3\):

- the face vector is \(f=(12,66,108,54)\);
- \(\operatorname{rank}(\partial_1)=11\) and \(\operatorname{rank}(\partial_2)=54\), so \(\dim H^1=1\);
- the embedded explicit \(1\)-cochain has weight \(28\), is a cocycle, and is not a coboundary;
- all \(3^{11}=177{,}147\) normalized coboundary shifts are exhausted;
- minimum weight is exactly \(28\), attained by exactly \(18\) cocycles in each nonzero class;
- scalar negation pairs the two nonzero classes without changing their \(18\) supports;
- the full coset weight enumerator agrees with the hard-coded expected table;
- the published permutations generate a six-element facet-preserving group, and the \(18\) minimum supports split into orbits of sizes \(3,3,6,6\).

The checker uses integer arithmetic and modular Gaussian elimination only. No randomized search or floating-point inference is used. The finite computation proves only the stated invariant of this exact triangulation and coefficient field.
