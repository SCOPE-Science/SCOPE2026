---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For k>=1 let m=4k+2 and t=2pi/m. Pm distances are integer cyclic steps and P4 adjacent/opposite distances are (k+1/2)t and (2k+1)t. Each correspondence covers all m vertices by its four square fibers, hence one fiber has >=k+1 elements. If all its pairwise circular distances were <k, fix one vertex at 0 and represent the others in [-(k-1),k-1]; extremal signed representatives -b and a have a+b< m/2 and hence a+b<=k-1, bounding the fiber size by k, a contradiction. Thus dis R >= kt for every, including multivalued, R. A surjective map with consecutive blocks of sizes k+1,k,k+1,k has within-block step distance <=k, between adjacent blocks steps 1..2k and opposite-block steps >=k+1 (and for short blocks >=k+2) up to 2k+1. Comparing to target 0,k+1/2,2k+1 yields discrepancies respectively <=k, <=k-1/2, <=k, with equality on endpoints 0,k in the first block. Therefore min distortion=kt and GH=kt/2=pi*k/(4k+2). The proof uses only finite pigeonhole, circular distance geometry and the exact correspondence characterization, valid uniformly for k>=1; no claim for chord metric, odd target, arbitrary 4-point source or all optimal correspondences. Independent check of 100 block maps, 84,317 enumerated k+1-subsets for k<=5, and all 1,560 surjective maps P6->P4 agrees with proof; those checks do not prove uniformity.

## originality

PASS

Compared all four statement-level checks against exact same-object primary Talipov paper and Lim–Mémoli–Smith appendix, and later stronger-looking metric graph paper. Talipov covers divisible n|m or n=2,3, excluding 4 and 4k+2; Lim–Mémoli–Smith calculate circle-versus-polygon or consecutive counts only and explicitly pose remaining polygon distance question. Later metric graph bounds do not imply exact matching of two sparse finite samples; published SCOPE/Resultary close hits concern chord hyperbolicity/convexity and unrelated polygon invariants. No equivalent all-k statement or stronger direct implication found in inspected texts. Priority is best of current knowledge, not guaranteed exhaustive.

## value

PASS

The exact Gromov–Hausdorff metric is a natural and difficult invariant, and p_{4,n} is the first source size not covered by two-/three-point equilateral-simplex formulas. The all-k residue-class determination complements Talipov’s n|m square case, completing distances from the geodesic square to all even regular circle vertex sets, with a sharp obstruction for arbitrary correspondences and explicit matching witness. The parity-sensitive complementary class is a specifically motivated outstanding subfamily of the published all-pairs problem, not a parameter rename, a finite table recomputation or an arbitrary tiny instance. No claim is made of a general odd-target or all-polygon theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
