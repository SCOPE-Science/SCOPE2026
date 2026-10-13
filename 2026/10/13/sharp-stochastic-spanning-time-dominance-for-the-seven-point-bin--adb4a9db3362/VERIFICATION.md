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

# Reproducibility and verification

Execute `python3 verify.py` from a directory containing this document's accompanying standalone Python program. The certificate uses only the standard library and no external files, random seeds, network requests, or unpublished data.

It enumerates \(\binom{14}{7}=3432\) multisets of seven columns from \(\mathbb F_2^3\); \(2696\) span the whole space. It constructs Fano planes by modular dot products and checks pair incidences, generates the 16 subspaces by XOR closure, and checks the rank-closure dynamic program against the Möbius formula for **each** spanning multiset at every \(t=1,\ldots,6\). The simplex failure numerators at \(t=3,4,5,6\) are exactly \(175,553,1687,5089\). The minimum non-simplex excess numerators are exactly \(24,192,1080,5280\), each achieved by 42 distinct column multiplicity vectors with no zero columns, one missing projective point, and one other duplicated point. The executable terminates with `VERIFY_OK` when every assertion passes.

This certificate establishes the four finite-time comparisons and sharp equality cases by exhaustive exact arithmetic. It is **not** a finite verification of the infinitely many \(t\ge7\); those are proved using the Fano plane occupancy lemma and \(4^t>7\cdot3^t\) for all integer \(t\ge7\). Scientific originality has not been independently audited; a materially relevant October 2026 paper was available only at abstract level.
