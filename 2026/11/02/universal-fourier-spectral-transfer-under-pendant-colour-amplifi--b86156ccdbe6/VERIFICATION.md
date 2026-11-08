---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For q≥3 uniform proper colourings, the conditional expectation of a leaf character given its parent equals -r times the parent character, with r=(q-1)^-1; residual variance δ=1-r² and distinct leaves have conditionally orthogonal residuals. This yields G_s=[[C,-r C R],[-rR^T C,δI+r²R^TC R]]. Leaf contrasts give δ multiplicity n(s-1) and core+leaf averages yield B_s(c) 2x2 blocks with trace δ+(1+s r²)c and determinant δc, giving exact eigenvalues and nullity. Both λ± increase strictly in c>0; as s grows trace increases while product fixed, so condition worsens; λ+=sr²c+O(1), λ-=δ/(sr²)+O(s^-2), squared condition grows b r⁴/δ*s². Independent direct colouring enumeration and Gram spectral calculations agree for four examples.

## originality

PASS

Graph-corona adjacency/Laplacian spectral transfers concern deterministic graph matrices, not a correlation Gram for uniform colourings. H-colouring tori and equitable corona colouring study counts/thermodynamic measures, not arbitrary-core pendant conditional residual spectra. Ordinary block-Schur complement methods are prior algebra; the specific universal colouring Gram statement and sharp conditioning transfer were not located.

## value

PASS

Exact rank, spectrum, condition number and asymptotics for first-frequency Fourier sampling after arbitrary pendant augmentation; useful structural spectral transfer even when core C is unknown, and a concrete singularity threshold for decorated cliques.

The dated certificate retains the supplied scientific assessment, sources and limitations.
