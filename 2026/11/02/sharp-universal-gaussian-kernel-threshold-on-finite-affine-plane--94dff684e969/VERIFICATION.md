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

For any existing affine plane of order q>=2, point-line incidence axioms yield BB^T=qI+J and B^TB=(q-1)I+J-H. The zero-sum powered-distance form decomposes into parallel-class contrasts of dimension q with eigenvalue 2^p((q-1)2^p-q), q^2-1 paired 2x2 blocks with diagonal -2^p,-4^p and coupling sqrt(q)(1-3^p), and one global point-versus-line contrast. The paired determinants stay positive up to alpha_q=log_2(q/(q-1)); the scalar sector stays negative by the stated 3^p concavity bound; the parallel eigenvalue changes sign exactly at alpha_q. This proves CND iff p<=alpha_q and strictness below, with endpoint nullities q for q>=3 and 5 for q=2. Schoenberg and centered Gram rank yield PSD for every t and Euclidean dimensions. q2, p=0, non-Desarguesian applicability and nonexistence of some q are explicitly bounded. Finite numerical spectra cannot replace these sector inequalities.

## originality

PASS

The general Schoenberg, Li--Weston, and Sánchez machinery is established, including generic strictness inheritance and finite-matrix computation. The inspected primary sources do not state the incidence-distance-four threshold, parallel-class kernel, and exceptional q=2 ranks; Resultary's affine-plane Rips homotopy result is a different invariant. Originality is qualified pending broader resolvable-design negative-type literature.

## value

PASS

A full negative-type exponent and critical Euclidean embedding-dimension classification for Levi graphs of any affine plane is a motivated metric-geometry invariant. The parallel-class nullity and exceptional q=2 effect are nontrivial structural information beyond general Schoenberg equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
