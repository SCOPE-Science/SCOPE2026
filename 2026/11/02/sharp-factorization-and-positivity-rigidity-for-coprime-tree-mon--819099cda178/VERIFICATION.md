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

Exact independent Fraction arithmetic reproduced the rational numerator factorization at rational x,y for every r=1..10. After cancellation, numerator N=1-V_r(x)V_r(y); for r>=3, N(c,0)=1 prevents x-c and y-c factors, while substituting y=c/x gives nonzero highest Laurent coefficient -c*x^(r-2) when c!=0, excluding xy-c. Over C every numerator of a single F(x)G(y)J(xy) product has only these factor types. The denominator is positive for x,y in (0,1), and monotonic V_r ensures maximal product at a=b=1; its unique crossing gives tau_r>1/2 and tau_3=(sqrt(5)-1)/2. The Calkin–Wilf telescoping sum is absolutely convergent by geometric decay, not merely finite numerical evidence.

## originality

PASS

Kalinin explicitly provides the r=1,2 kernels and telescoping mechanism; Hata supplies more general Farey-tree telescoping. Those cover the sum identity (which is not claimed new) but do not directly determine failure of factorization for every r>=3 or its complete sign threshold. The full Kalinin PDF was unavailable, so the comparison remains a best-knowledge mathematical statement with residual risk.

## value

PASS

The parameter r is a motivated monomial-pole extension of a published coprime sum; determining exactly when the telescope kernel maintains multiplicative separation and coefficientwise sign is a natural structural rigidity/positivity question, not a random isolated numerical substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
