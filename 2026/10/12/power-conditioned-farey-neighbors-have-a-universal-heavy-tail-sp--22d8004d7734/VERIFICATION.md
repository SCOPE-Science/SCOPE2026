---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Classical exact ordered denominator correspondence maps neighboring Farey fractions uniquely to positive coprime (b,d) with b,d<=N, b+d>N; b=u^r,d=v^s iff gcd(u,v)=1. Scale u by U=N^(1/r), v by V=N^(1/s); region D={x^r+y^s>1 in (0,1)^2}. Möbius inversion plus O((U+V)/d+1) boundary cell errors yields area UV/zeta(2)+O(max(U,V)log N), with area C=1-Gamma(1+1/r)Gamma(1+1/s)/Gamma(1+1/r+1/s). The bounded product-cutoff area gives weak limit for G=N²/(u^r v^s). Near (0,1) and (1,0), widths ~x^r/s and ~y^s/r give tail terms t^(-1-1/r)/(s(r+1)) and t^(-1-1/s)/(r(s+1)), so alpha=1+1/max(r,s) and positive K; tail integral proves iff moment q<alpha. Independent full-Farey recurrence enumeration and separate primitive power-coordinate enumeration agreed for all 16 tests N=10,20,50,100 and r,s in {2,3}; they do not prove infinite estimates.

## originality

PASS

Cobeli–Iordache–Zaharescu 2003 full source gives Farey-neighbor denominator criterion and parity-restricted denominator distributions, while Augustin–Boca–Cobeli–Zaharescu study unrestricted Farey h-spacings. Those lead to the method but not directly to the zero-density two-exponent power-denominator event, the explicit beta area C, the limiting conditional gap variable, or its corner tail/moment boundary. These are new specialized implications requiring a distinct nonrectangular thin-grid scaling and corner analysis under best current inspection.

## value

PASS

Adjacent full-Farey fractions under independent fixed-perfect-power denominator restrictions form a natural sparse arithmetic sampling problem. The exact asymptotic and explicit weak gap law uncover a heavy-tail exponent with finite mean but potentially infinite variance and a precise moment threshold; this distributional statement is meaningful beyond reproducing classical Farey neighbor criterion or a count table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
