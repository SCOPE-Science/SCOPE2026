---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For v>=2, v2(D_2(x))=v+v2(v)-1. Every odd v>=3 immediately decreases to even; for even v with k=v2(v), k=1 means a fixed valuation and k=2 the exact 2-cycle; k>=3 descends to T(k)=1+v2(floor((k-1)/2))<k in one or two iterates (parity accounted). Thus the least eventual period from m is F(m+1), where F(1)=1,F(2)=2,F(r>=3)=F(T(r)). Inverting the unique T fibers gives the disjoint residue-class decomposition A={2} union_{t in A,h>=0}{2^t(2h+1)+1,2^t(2h+1)+2}. Counting its two residue classes mod 2^(t+1), with only t<=log2 N active and geometric omitted tail, yields A(N)=N*sum_{t in A}2^-t+O(log N), hence same density for exponents m. Non-eventual periodicity of the binary indicator: for q>=2, compare r=2^K+1 and r+q, whose T-values are K and fixed 1+v2(floor(q/2)), while F(K) takes both values at arbitrarily large K; for q=1 use r=2^K+2 with K in A and r+1, which has label 1. Thus the binary expansion is not eventually periodic, so alpha is irrational. Independent direct valuation trajectory cycle detection for m=2..100000 agrees with F(m+1), count 29705, and alpha computed from first 120 exact binary digits is about 0.29705882370403475. Finite data are not the irrationality proof.

## originality

PASS

The known Emmons–Xiao theorem provides ultimate periodicity and valuation-period classification. This exact self-similar exponent-set description, natural density with O(log N) error, and the proof that the period-two density is irrational are additional quantified number-theoretic assertions. A similar period tree may be derived from their results, but explicit density and nonperiodicity are not proved in the inspected Theorems 8-9.

## value

PASS

The density of an eventual valuation period among the natural input-exponent family m is a canonical frequency statistic, not a contrived slice of integers. The explicit irrational limiting constant, recursively defined digit set, logarithmic discrepancy, and nonperiodicity are a meaningful quantitative complement to previously known per-trajectory classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
