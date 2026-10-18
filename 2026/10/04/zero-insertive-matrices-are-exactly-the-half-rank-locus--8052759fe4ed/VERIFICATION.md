---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: AB=0 implies im B⊂ker A, rank A+rank B≤n and rank ARB≤min(rankA,rankB)≤floor(n/2). Conversely rank-r X=U J_r V can be decomposed with A_r=∑_{i≤r}E_{i,r+i}, R_r=∑E_{r+i,i}, B_r=J_r; A_rB_r=0, A_rR_rB_r=J_r if 2r≤n. Invertibles transfer. Finite-field rank-r count is standard; n2 singular versus n≥3 rank n−1 excluded. Right-vector-space rank conventions are respected.

## originality

PASS

The elementwise 2025 zero-insertive work and September 2026 path/Leavitt paper establish definitions, n=2 nonsingular boundary, and ZINC ring properties, but available material does not give a determinantal rank iff classification for every n and division ring. The independent two-way construction supplies a natural exact locus not implied by the known n=2 special case. The 2026 full manuscript was inaccessible despite access attempts; this is recorded as a material residual originality risk, not converted automatically to FAIL.

## value

PASS

PASS: New zero-insertive algebraic notion naturally prompts classification of all matrices satisfying a zero-product sandwich. Exact rank cutoff and determinantal-locus description uniformly for all n and division rings give a structurally meaningful boundary and readily usable finite-field enumeration; not just a tiny-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
