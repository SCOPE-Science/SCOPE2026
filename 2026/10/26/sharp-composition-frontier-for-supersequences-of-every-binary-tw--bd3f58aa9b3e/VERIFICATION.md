---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reconstructed the lower bound including both parities. With excess e and Q=e+1, every length-Q integer window starting at a=0,…,N must hold two one-occurrences, counted with multiplicity, and the outer markers must span at least N zeros. For odd m=2k+1, disjoint windows force N<kQ. For even m=2k they again force N<kQ; when N≥(k−1)Q, the partitions starting at 0 and at r=N−(k−1)Q each exhaust the markers in ordered pairs, hence the first lies at or beyond r and the last at or before kQ−1. Thus 2N<(m−1)Q in every case. In the construction at h=N/(m−1)>0, the floor levels floor(ih) embed a target using the specified ceiling indices: if a=0 then i=1 and the middle gap bound is direct; if a>0 then ih<a+h and jh≥a+b+h. The available suffix is at least c by (m+1−j)h≥c, also when a+b=0 and j=2. Flooring preserves all required integer gaps. The total telescopes to N+floor(2h). For unrestricted length, the product maximum floor(T²/4)≤2N<floor((T+1)²/4) at T=floor(sqrt(8N+1)) proves the exact minimum of k+floor(2N/k); N=0 gives length two separately as well.

## originality

PASS

The inspected close coverage concerns the same layer and already gives its sharp leading overhead and a finite exact table, but does not give either the all-length exact optimum or the fixed-composition law. The latter optimizes using a stronger parity-sensitive packing argument and an attaining gap construction.

## value

PASS

This is an exact extremal result for a natural complete target layer. Fixing the number of ones reveals an entire composition tradeoff, gives a short explicit optimal host for each budget, and explains why the square-root asymptotic rounds to a particular exact integer at every length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
