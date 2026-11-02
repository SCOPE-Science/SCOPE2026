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

Uniform binary words with a>=1 ones, b>=2 zeros, n=a+b>=6. Each fixed specified configuration with r ones and s zeros has probability (a)_r(b)_s/(n)_(r+s). For the ordered 001/010 window pairs, exactly (n-4)(n-5) disjoint and two compatible overlap families (n-4) length-five 01001 and (n-3) length-four 0010 contribute; other overlaps are incompatible. The resulting mixed moment and subtracting equal mean squared gives Cov=-ab(b-1)P(a,b)/(n²(n-3)(n-2)(n-1)²). For b<=a+1 set v=a-b+1 and positive polynomial coefficients show P>0; for b>=a+2 set v=b-a-2 and negative coefficients show P<0, including the b=2,a>=4 and a=1,b>=5 edge cases. New independent direct word enumeration confirmed 39 complete composition cases 6<=n<=11 and all covariance signs; universal proof rests on finite overlap partition plus polynomial identities, not extrapolation.

## originality

PASS

The full integer-composition positive/negative threshold for the two literal contiguous trigrams and exact rational covariance are assessed original relative to inspected references, not the classical method of counting overlapping motifs or finite-population hypergeometric probabilities.

## value

PASS

The covariance changes sign across a simple exact composition threshold despite equal motif means. This is a natural finite-population joint word-statistic invariant relevant to sequence motif dependence, with no hidden asymptotic condition and no equality cases; its finite overlap geometry and all-composition sign proof are stronger than a small numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
