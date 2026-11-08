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

For all integers b>=2,t>=1,M=b^t-1, folding a positive multiple N=Qb^t+R to Q+R strictly decreases the integer while preserving M-divisibility and weakly decreasing base-b digit sum; it terminates at M and gives lower bound t(b-1). Congruence modulo b-1 forces all digit sums in (b-1)N. For each 1<=r<t the explicit witness W_r=M(b^t+b^r+1)=b^(2t)+b^(t+r)-b^r-1 has exactly (t+r)(b-1) digitsum; W_0=M and disjoint shifted copies of M realize all k>=t. Under N<b^(2t), write N=Ab^t+B, 0<=A,B<=M, so A+B=M or 2M; the two sums yield only t(b-1) and 2t(b-1). This enforces sharp minimal length 2t+1 for each first intermediate (t+r)(b-1). t=1 is handled without a nonempty intermediate range. Independent exact enumeration b in {2,3,4},t=1..4 corroborates.

## originality

PASS

Phunphayap et al. 2023 develop all digit-sums of multiples and prove congruence/concatenation inclusions, which for M=b^t-1 give only multiples of t(b-1), not missing intermediate k. Dartyge–Luca–Stănică 2009 analyze digit sums of multiples and same-sum conditions but inspected theorems do not state this all-base complete support or the exact first-hit length 2t+1. Best-of-knowledge novelty is the complete simple-modulus spectrum plus two-block threshold, with a substantive folklore/earlier-derivation risk.

## value

PASS

Exact support of digit sums for an arithmetic progression at the natural repunit-complement modulus M=b^t-1, and the optimal first intermediate witness length, are natural number-theoretic invariants. The two-block boundary is sharp and genuinely supplements the known congruence and concatenation results, despite the elementary proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
