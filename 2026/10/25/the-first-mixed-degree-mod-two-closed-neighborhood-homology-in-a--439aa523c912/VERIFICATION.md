---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For categorical graph product G_n=K3×Kn with edges precisely (i,j)~(a,b) iff i≠a and j≠b, the closed neighborhood B_ij has 2n−1 vertices. The complex consists of all nonempty subsets of the 3n prescribed balls. Independent construction of every ball and all its subfaces for each n=2,...,6, followed by complete bitwise GF(2) elimination on every consecutive simplicial boundary, reproduces every source f-vector and rank vector. The only positive reduced Betti numbers are n2 β1=1; n3 β2=14; n4 β3=25; n5 β4=44; n6 β4=47,β5=36. At n6 exactly 26016 nonempty simplices are counted; alternating Euler values agree. The first mixed-positive-degree case in the claimed finite indexed range is exactly n6; no statement about n>=7, integral homology or homotopy type is made.

## originality

PASS

The primary closed-neighborhood paper's explicit graph-product result concerns the Cartesian rook graph K_m□K_n, whereas the current graph input is categorical K3×Kn. The 2023 categorical-product independence-complex theorem applies, through the canonical-double-cover relation, to the complement/Cartesian problem, not directly to these categorical closed-neighborhood ranks. Resultary's triangular-graph mixed-degree finding and open-neighborhood Cartesian-product results are distinct graph families and invariants. A stronger closed formula under complementary graph reformulation remains a historical risk, not currently established coverage.

## value

PASS

The first occurrence of mixed positive-degree mod-two homology in a simple naturally indexed product family is a motivated finite cutoff; the exact degree-4 and degree-5 ranks provide a reproducible structural benchmark beyond the established Cartesian computations. This natural invariant remains independently useful even without an all-n theorem or integral classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
