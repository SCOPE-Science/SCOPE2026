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

PASS: Uniform labelled matchings induce uniform double-occurrence subwords on any 3 or 4 specified chord labels. Independent complete enumeration (90 words on 3 labels, 2520 on 4) gives P(E=0)=2/3, P(E=1)=1/3; q=(3/10,2/5), r=(1/10,1/5), s=(3/35,17/105), with q=P(X02|E), r=P(X02 X12|E), s=P(X02 X13|E). Conditional degrees are E+Σ_{c>=2}X_{0c}, E+ΣX_{1c}. Pairing equal remaining chord c contributes (n-2)(r-q²), distinct c,d contributes (n-2)(n-3)(s-q²), an identity for ALL n due subword exchangeability. Simplifying gives Cov_nonedge=(n-2)(16-3n)/700 and Cov_edge=(n-2)(n+18)/525; law total covariance gives (3n+4)/45 unconditionally. All critical local table entries independently recounted from induced words (C4_OK). Sharp sign change at 5→6 is exact; bounded enumeration is a finite proof of the local table, not an unsupported extrapolation to large n.

## originality

PASS

PASS, qualified: Acan studies random chord intersection-graph degrees marginally, Paguyo exact crossing counts and fluctuation rates, and Arenas–Velilla–Arizmendi total crossings in randomly embedded graphs; the inspected main theorems are aggregate, not conditional two-vertex degree covariance. Existing aggregate variance may determine unconditional covariance but cannot separate E=0 and E=1 without additional three/four-chord mixed moments. An older graph-assortativity calculation could have equivalent conditional formulas.

## value

PASS

PASS: Conditional edge/nonedge degree dependence is a standard natural graph-assortativity statistic. A positive unconditional covariance conceals a strictly negative nonedge covariance beginning at n=6, while adjacent pairs stay positive. The exact smallest sign reversal is a meaningful finite cutoff accompanied by a full infinite-family formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
