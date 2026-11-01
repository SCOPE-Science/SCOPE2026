---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The five-prime exponent transition follows literally from L2(p^u)=p^(u-1)(p-2), including 13->11->3^2 and 7->5->3. W=a+b+c+2d+2e decreases by [a>0] per step. Proved positive-a buffer invariant makes all idle steps occur at startup: with initial d>0 at most the first step; with d=0,e>0 at most first two steps, whose exact conditions are [a=0] and [a<=1 and b=0]. This yields R2=W+[a=0]+[d=0,a<=1,b=0]. Primewise comparison yields 7^R/n >=49/13>49/15, hence 49n<15*7^R. Independent literal exponent iteration matched 1024 complete starting vectors.

## originality

PASS

Defant (2015) states a global inequality as Conjecture 20 and studies Schemmel iteration but gives no 13-supported closed stopping-time formula. Harrington–Jones (2010) analyzes a related C2=R2-1 convention under a domain excluding p≡1 mod 3; e>=1 ensures a factor 13≡1 mod3 and excludes their domain. Existing 7-smooth evaluations cannot give the 13->11->3^2 start-up correction without new branching analysis. Unread Harrington–Jones full text is a genuine residual risk, not an automatic failure.

## value

PASS

Exact first-hitting times across an infinite, naturally invariant 13-smooth prime-support family and strict nontrivial sector of an explicit published conjecture; the first 13->11->3^2 branching changes the weight and delay law. Not merely a fixed finite table or restated 7-smooth substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
