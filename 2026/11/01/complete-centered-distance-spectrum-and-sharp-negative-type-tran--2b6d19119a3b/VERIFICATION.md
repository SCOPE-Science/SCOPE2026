---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The vertex-to-vertex, vertex-to-midpoint and midpoint-to-midpoint shortest-path formulas are derived by minimizing endpoint Hamming distances. The Walsh decomposition separates frequencies |S|=0,1,>=2. The mean block has d-1 midpoint contrasts a-2 and one centered class contrast 2(a-2)/(d+2); singleton frequencies give eta+ and eta- (negative by trace<0, determinant 4a>0), and higher frequencies contribute -2 and zero. Multiplicities sum to (d+2)2^(d-1). Boundary d=1 path gives (-2,-2/3,0), d=2 gives (0,4,4) inertia, and d>=3 gives (d,d2^(d-1),2^d-d). The direction-1 minus direction-2 midpoint coefficient vector is zero-sum and has c^T D c=2a(a-2)>0, making the Schoenberg all-scales Gaussian criterion fail at small t. I independently reconstructed BFS distance matrices and numerically checked centered eigenvalues for d=1..5 exactly to floating tolerance 1e-8; proof of all d rests on the Walsh block identities, not finite checks.

## originality

PASS

After direct mathematical implication comparisons, no inspected prior theorem gives the entire final claim; positive classification is best-of-knowledge, not an absolute historical priority certificate. The once-subdivided binary d-cube has explicit full and centered geodesic-distance spectra; the centered matrix is conditionally negative semidefinite iff d<=2 and has precisely d positive eigenvalues for d>=3.

## value

PASS

This exact all-dimension spectrum and sharp d=3 negative-type boundary form a natural classification of a graph-metric embedding invariant, with a simple explicit obstruction; it is not a trivial finite lookup or renaming of a known Laplacian theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
