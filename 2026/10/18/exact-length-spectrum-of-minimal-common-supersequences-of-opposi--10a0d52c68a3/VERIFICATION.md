---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

PASS. Minimality in subsequence order is equivalent to all single deletions destroying at least one target. For A=0^m1^m and B=1^m0^m, any minimal W must be union-covered by chosen embeddings; disjoint embeddings can be replaced with intersecting embeddings, contradicting deletion-minimality. Shared positions must all have one symbol, since the order of any shared zero and one is opposite in A and B. After complementing, exactly 2m zeros straddle a central positive ones run of length g; extremal deletion arguments force j=m-g ones on each side, so W=P1^(m-j)Q, with P/Q each having m zeros and j ones. The forced boundary zero leaves C(m+j-1,j)^2 per complement orientation; j=0..m-1, otherwise no minimal words. Dominated geometric tail (ratio <=1/4^k) and Stirling give T_m~16^m/(6 pi m). Independent exhaustive subsequence and deletions agrees for 24 (m,L) strata m=1..4. Finite m<=4 is not the infinite proof.

## originality

PASS

Best-of-knowledge PASS after actual Git proof and independent bounded checks, Resultary semantic search, and comparisons of the precise claim against materially read primary texts and theorem scopes. No examined theorem/database supplies the same final formula or exact incidence certificate. Identified overlaps and access limits are credited; failed searches alone are not treated as a proof of novelty.

## value

PASS

PASS. Minimal, not shortest, common supersequences are a natural subsequence-poset invariant central to string algorithms; the opposite long two-run input family gives exact nontrivial spectrum spanning 3m..4m-1 and asymptotic count with a clean structural decomposition. This supplies a precise benchmark for general enumeration algorithms and distinguishes minimality from shortest length; not just brute recomputation or parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
