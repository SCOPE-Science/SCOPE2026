---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For k>=2 every length-k two-one target 0^a1 0^b1 0^c has K=k-2 zeros. With host Z>=K zeros and R ones, let zero-levels z_i. The target occurs iff distinct i<j satisfy z_i>=a, z_j-z_i>=b, Z-z_j>=c. Every adjacent-one target b=0 requires two ones in each length-d zero-level window, d=Z-K+1. There are T=k-1 windows; each host one meets at most d windows, so Rd>=2T. Hence |W|>=k-3+d+ceil(2T/d)>=k-3+ceil(2sqrt(2T)), using integer max product at fixed d+r. Construct Z=K+d-1 zeros and one at every zero-level congruent 0 or floor(d/2) modulo d (d>=2 chosen near sqrt(2T)). Every d-window has exactly two markers, separated by at most ceil(d/2); use the first marker of a-window and last of (a+b)-window to satisfy all three subsequence gap inequalities, including distinct markers for b=0. Exact residue count gives R<=ceil(2T/d)+2. Optimizing d gives length <=k-1+ceil(2sqrt(2T)); sandwich yields lim (L_k-k)/sqrt k =2sqrt2. Independently exhaustively checked k=2..8 minima and tested all target a,b,c and integer bounds for 103 k values through 500, not used as infinite proof.

## originality

PASS

General k-subsequence universal words cover all 2^k targets, unlike the complete weight-two layer; arbitrary selected sets of length-k two-one words are an input to a shortest-common-supersequence complexity problem, rather than the exact complete-layer optimum. The sharp 2sqrt2 overhead plus two-unit all-k envelope are neither obtained by simply restricting their quantified statements nor present in the inspected source material.

## value

PASS

Minimum universal host length for an entire Hamming weight layer is a canonical combinatorics-on-words invariant, and the exact square-root overhead constant plus additive-two envelope constitutes a nontrivial infinite-family extremal construction and lower bound. The finite optimum is deliberately not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
