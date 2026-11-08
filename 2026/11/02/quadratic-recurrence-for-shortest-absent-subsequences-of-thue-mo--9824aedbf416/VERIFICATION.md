---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The 2^m complementary two-symbol blocks each contribute at least one greedy matched symbol to a target, and there are exactly 2^m zeros, establishing shortest absent length 2^m+1. For any orientation b of h blocks, a target of length h+1 is absent iff its i-th adjacent target pair is not the i-th full complementary pair; this greedy proof holds for every h. Counting allowed adjacent transitions uses L=[[1,0],[1,1]], R=[[1,1],[0,1]], e=(1,1), and the Thue–Morse identity T_{m+1}=T_m complement(T_m) yields P_{m+1}=(P_m J)^2. det P_m=1 and direct 2x2 multiplication give A_{m+1}=2+A_m(b+c) and D_{m+1}=D_m(A_m-D_m), with initial L. This is an induction for all m; independent brute-force absent-subsequence enumerations through m=3 and recurrence computed 3,5,12,74,2666. Source verify.py also independently implements the next-occurrence automaton. Checks do not prove the infinite result.

## originality

PASS

General greedy/arch structural characterizations, global extremal absent-subsequence counts and Thue–Morse fixed-depth binomial factor complexity are earlier work. The all-level two-scalar trace recurrence for the specific shortest absent count is neither an extremal bound corollary nor a factor-subsequence statistic. Potential OEIS or automatic-word trace identities remain a genuine best-of-knowledge priority risk.

## value

PASS

Exact counting for an exponentially long canonical morphic word from only m small polynomial steps is a meaningful natural exact invariant; it distinguishes support/absence from embedding multiplicities and yields infinitely many nontrivial exact counts. No general arbitrary-factor result is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
