---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reflection splits the 2m-vertex weighted path Laplacian into irreducible Jacobi matrices N_m and N_m+2w e_me_mᵀ. Their spectra are simple and disjoint for w>0 by final-coordinate recurrence. PBH detects zeros of sensor coordinate. Neumann cosine eigenvectors vanish at j iff gcd(m,2j-1)>1; antisymmetric zeros have θ=(2r-1)π/(2j-1) with 1≤r<j, and the terminal boundary equation gives the exact positive W_r with nonzero denominator. Conversely any such W_r yields a nonzero zero-sensor eigenvector. Periodicity m↦m+(2j-1) changes numerator and denominator signs together. For j=2, residues m mod3 give all weights / {1/2} / empty; simple spectrum makes the unobservable dimension one. Independent 390 numerical eigenvector zero tests agree; they are not proof for unbounded m and real w.

## originality

PASS

Best-of-knowledge PASS for the complete interior-sensor resonance weights and all-length arithmetic periodicity for a single *central edge weight* in an even path. Uniform-path number theory, strong structural zero forcing and endpoint weighted adjacency radii are related but do not imply the specific all-w exceptional sets.

## value

PASS

A natural one-defective-edge path is the simplest weighted perturbation of a graph signal system; the result completely identifies all positive conductances at which a specified single interior sensor fails, with a striking exact periodic residue law and exact nullspace multiplicity. Useful in sensor placement and fragility analysis, not just endpoint textbook controllability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
