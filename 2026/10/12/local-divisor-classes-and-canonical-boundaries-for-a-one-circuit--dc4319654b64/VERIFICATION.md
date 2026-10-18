---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For n>=6 and 3<=k<=n-3, the one-deleted-basis polytope is exactly the hypersimplex clipped by x(H)<=k-1, where the cut passes through all k(n-k) adjacent vertices and creates no fractional vertices. At each surviving vertex B the normal cone has n primitive signed-coordinate rays, plus h=sum_{i in H}e_i only at |B∩H|=k-1. In N=Z^n/Z(1,...,1), M={m:sum m=0}, the signed-coordinate divisor map has saturated image; the extra-ray coordinate is an integral linear combination of coordinates, giving Cl=Z or Z² without torsion. Its unique Q-Cartier canonical character has m_i=+1 for i∈B, -1 otherwise, whence n=2k and, at new-facet vertices, k-2=1. This proves local criterion, all singular fixed points, and global iff (n,k)=(6,3). The exact-rational CHECKER.py inspected tests only n=6..9 and cannot replace the lattice proof.

## originality

PASS

Best-of-knowledge originality of the narrow final statement, not a general absence certificate. The new local integral class group and per-fixed-point Cartier stratification survive broad known global theorems.

## value

PASS

The one-circuit-hyperplane sparse-paving matroid is the minimal nonuniform departure from a hypersimplex. Its extra facet changes the intrinsic integral local class groups at exactly k(n-k) natural fixed points and alters pointwise canonical Cartierness; these are natural structure invariants unavailable from aggregate face counts. The global Gorenstein corollary alone is not claimed as novel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
