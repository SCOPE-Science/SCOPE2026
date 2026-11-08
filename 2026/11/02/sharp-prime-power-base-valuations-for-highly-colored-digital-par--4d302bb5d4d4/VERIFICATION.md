---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The exact logarithmic coefficient of G_{p^a}=H_{p^a,1} is p^{a-r}/u for n=p^{aq+r}u, (p,u)=1. Writing m=p^s v and exp(m log G), every nonlinear j>=2 term has valuation at least j(s+1)-nu_p(j!)>=s+a+1 under s>=a if p=2, or s>=a-1 if odd. The unique lowest-valuation linear term therefore gives nu_p(S(n))=s+a-r and normalized mod-p unit v/u. At n=0 coefficient is one. Trailing-zero residue classes give stated natural densities and automaticity of the valuation levels. The actual recurrence script was inspected, and an independent finite integer-product expansion for 375 positive coefficients across five families reproduced both formulas.

## originality

PASS

The exact generating series and prime-base case are due to Ulas and Żmija, and the k=4 results are explicitly their Conjecture 6.6(5),(6); the theorem proves both and extends to a high-divisibility prime-power-base range including leading units. Stronger 2023 Żmija article could not be read in full, so originality remains qualified.

## value

PASS

Resolves two explicit open composite-base valuation conjectures, obtains all n sharp valuation levels and leading digits, and a systematic automatic-density classification under natural divisibility hypotheses. This is motivated independent arithmetic information rather than a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
