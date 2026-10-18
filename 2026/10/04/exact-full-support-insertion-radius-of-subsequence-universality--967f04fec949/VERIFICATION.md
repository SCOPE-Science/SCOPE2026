---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Proved I_k(w)=qk-C_k(w) by partitioning original symbols among k universal arches and inserting missing symbols, with reverse lower bound from any arch factorization. A full-support word has C_k>=min(n,q+k-1): refine a segment containing a repeated symbol so its symbol contributes to two blocks, increasing coverage at least one until k blocks or n positions. The heavy-first-symbol word a0^(n-q+1)a1..a_(q-1) attains equality. Independent dynamic programming checked full-support layers q=2,3,4 over n up to 8/7/6 with multiple k and found all predicted radii, but all-parameter validity follows from the combinatorial proof.

## originality

PASS

The extremal fixed-length full-support insertion-radius formula is a genuinely different quantified statement from the established per-input-word dynamic program; the sharp bound and extremizer do not appear in inspected STACS theorem claims.

## value

PASS

The insertion covering radius over the natural full-support layer is a sharp extremal companion to the established per-word algorithm. It gives an all-parameter closed form, explicit extremizer, and meaningful length-to-distribution transition; not a routine tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
