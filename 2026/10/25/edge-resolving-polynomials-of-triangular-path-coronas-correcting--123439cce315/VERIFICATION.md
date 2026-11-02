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

PASS. Reconstructed H_n with path vertices and one tip per edge; computed every edge-to-vertex distance by BFS for n=2..8 and independently enumerated all 43,688 graph-vertex subsets in n=2..8, checking resolving signatures against covers of the specified auxiliary graph and confirming exact polynomial counts/minima. The symbolic table of d(w_j,A_i),d(w_j,L_i),d(w_j,R_i) is verified from shortest paths, and the necessary two-witness pairs force auxiliary edges. For sufficiency the proof classifies all nonconsecutive tip-witness supports by block-index piecewise-affine distance differences, reducing to the six displayed boundary pairs (small overlapping cases direct); independently found precisely six boundary configurations for each n=6,7,8,9,12,18,28. The cover polynomial follows exactly by complementation of independent sets and counting free interior path vertices; leading coefficients yield edim ceil(n/2)+1 and minimum counts. Finite exhaustive cases corroborate, but do not replace the general piecewise-affine argument; its case analysis remains the sensitive nonstandard lemma. The original proposed edim=2 is already refuted at n=3.

## originality

PASS

PASS, best of knowledge with clearly bounded literature/access risks. The previous erroneous constant-dimension theorem is contradicted rather than a stronger prior. For n=3 exactly four resolving 3-sets exist and no 2-set resolves; for n>=4 a linear dimension replaces constant 2. Published general mixed results do not imply the full edge-resolution polynomial.

## value

PASS

PASS. Correcting a published theorem for a standard infinite graph family is a substantive mathematical clarification, especially because the error grows linearly with n. The full characterization of all edge-resolving sets and their cardinality-generating polynomial gives an exact structural solution, strictly more than another sample basis count, and cleanly separates edge from mixed metric dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
