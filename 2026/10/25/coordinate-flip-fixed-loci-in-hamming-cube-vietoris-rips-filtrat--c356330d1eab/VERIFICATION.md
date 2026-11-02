---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The ORIGINAL first theorem statement is FALSE: it identifies |VR_{≤r}(Q_{n-1})| with |VR_{≤r}(Q_n)|^{flip}. For n=2,r=1, the left side is a connected interval while the right has two isolated orbit-edge midpoints. The source proof, slogan, and finite face checker correctly use radius r−1. The complete attached replacement RESULT.md fixes the theorem to |VR_{≤r-1}(Q_{n-1})| ≅ |VR_{≤r}(Q_n)|^{flip}. For each orbit O_x={(x,0),(x,1)}, the maximum cross-orbit distance is d_{n-1}(x,y)+1; fixed barycentric coordinates occur with equal weights on each O_x. The map e_x→(e_{(x,0)}+e_{(x,1)})/2 therefore extends to a PL homeomorphism with explicit inverse and commutes with scale inclusions and unflipped symmetries. At r=4, n≥6, substituting m=n−1 in Feng 2023 Theorem 24 establishes a_n=Σ_{j=4}^{n−2}2^{j−4}C(j,4) four-spheres and b_n=2^{n−5}C(n−1,4) seven-spheres; n=6 gives S4∨10S7. All C/O/V findings assess the CORRECTED final claim, not the disproved original.

## originality

PASS

PASS, qualified best-of-knowledge: literature comparison of exact statements/implications. An abstract simplicial fixed-orbit construction may subsume the PL part, and its general statement is not claimed as new. The precise metric shift of the Boolean cube and equivariant filtration are the assessed application. The earlier theorem and the corrected orbit-union criterion combine to prove the fixed-space formula; one component alone does not cover the final theorem. Remaining general equivariant priority is a real risk.

## value

PASS

The exact natural filtration-level fixed-space model is geometrically stronger than computing invariant ambient homology. The coordinate flip is a canonical cube symmetry, the one-unit scale shift is essential, and the previously known scale-three integral wedge theorem yields a complete mixed-dimensional scale-four fixed-locus classification for all n≥6. The general orbit-barycenter lemma is acknowledged elementary; the specific all-scale identification is a motivated topological invariant, not a formal relabeling of the ambient homology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
