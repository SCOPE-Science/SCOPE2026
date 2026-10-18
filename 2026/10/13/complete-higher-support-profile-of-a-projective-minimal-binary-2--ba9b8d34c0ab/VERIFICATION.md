---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Over F8=F2[X]/(X³+X+1) reconstruct D1={(x,y):x nonzero,Tr(x²y+xy+x)=0}, |D1|=24. Six linear trace-evaluation generators from (a,b) in F8² have rank 6; all 64 codewords yield ordinary enumerator 1+24z10+12z12+24z14+3z16 exactly matching primary Table 4. Every r-dimensional message space has a unique binary reduced row echelon matrix. Independently enumerate all Gaussian-binomial counts (63,651,1395,651,63,1), 2824 total, and take bitwise OR of generator-row codeword supports for each subspace. This independently reproduces every six support histogram in RESULT.md, minima (10,15,19,21,23,24) and minimizer multiplicities (24,32,144,32,24,1). Actual artifacts/verify.py and certificate.json inspected and agreed; enumeration is exhaustive within exact 6-dim message space.

## originality

PASS

The code construction and ordinary enumerator for the projective minimal [24,6,10] D1 trace code are exactly prior Liao–Zhang–Zheng. The new complete SSWD and generalized hierarchy involve support intersections in 2–6 dimensional subcodes; neither prior enumerator nor projectivity/minimality fixes these. Pan et al solve other simplex-derived families; an older parameter-matching self-orthogonal [24,6,10] code has an inequivalent ordinary enumerator.

## value

PASS

Generalized Hamming weights and full subcode-support weight distributions are canonical higher-order invariants of a projective minimal code, important for generalized support properties. The complete exact 2824-subspace census fills a meaningful all-dimensional data gap for the first explicitly highlighted D1 code, and is not a routine extraction of its ordinary weight enumerator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
