---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

PASS: Counted distinct palindromic factors by exact number of 1s (zero, one, two, three) in 0^a 1 0^b 1 0^c 1 0^d. For b!=c the two two-one palindrome families are disjoint and no three-one palindrome exists, yielding D=max(0,min(a,d)-max(b,c)); for b=c the reflected three-one family restores richness. Positive defect r requires b=m>c=j (or reversed), a=m+r+s,d=m+r+t with min(s,t)=0; summing m,j,s,t gives H_r(z)=2z^(2r+6)(1+z)/[(1-z)(1-z^3)(1-z^4)]. Summing strata gives the displayed rational bivariate series and rich density 5/6. Independently generated all three-one strings n=3..20, enumerated distinct palindromic factors by brute substrings and checked each defect plus nonrich counts. All-n theorem comes from factor classification and formal identities, not the finite tests.

## originality

PASS

Best-of-knowledge PASS on the precisely scoped new theorem, after direct mathematical implication comparisons with established results. No identified covering theorem after Resultary and primary-source review. The listed inaccessible/partial literature is a residual risk, not proof of priority.

## value

PASS

PASS: Exactly three 1s is the first binary weight at which richness fails, so the layer has an intrinsic extremal motivation; the complete defect classification, all positive strata and rational generating function describe a natural first nontrivial layer and recover the 5/6 density. This is not arbitrary fixed-instance enumeration or merely the known shortest non-rich word.

The dated certificate retains the supplied scientific assessment, sources and limitations.
