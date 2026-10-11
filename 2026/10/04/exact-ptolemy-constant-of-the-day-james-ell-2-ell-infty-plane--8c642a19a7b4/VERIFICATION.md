---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The quadratic form H(u,v)=1/2 sqrt(3u^2+2uv+3v^2) is Hilbertian. On uv>=0 the two exact differences establish H<=N<=sqrt(3/2)H; on uv<=0, after |u|=a>=b=|v|, the differences factor as (a-b)(a+3b)/4 and (a-3b)^2/8, proving the same sharp sandwich. Hilbert Ptolemy therefore yields C_Pt<=3/2. The triple (-1,-1),(2,-2),(1,-3) has numerator 9 and denominator 6, so equality holds. Every step is exact algebra.

## originality

PASS

Mizuguchi--Saito--Tanaka study the same Day--James plane but compute the Dunkl--Williams constant, not Ptolemy. Zuo's 2012/2018 exact Ptolemy criteria after the package's linear normalization require midpoint or symmetry hypotheses that this nonsymmetric associated function does not satisfy. Resultary found the audited value as the direct exact Ptolemy hit and no earlier covering theorem.

## value

PASS

The Day--James plane is a standard nonabsolute Banach-space example and the Ptolemy constant is a natural exact geometric invariant. A sharp value with an optimal Hilbert comparison and explicit extremizing triple is a motivated exact classification, not an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
