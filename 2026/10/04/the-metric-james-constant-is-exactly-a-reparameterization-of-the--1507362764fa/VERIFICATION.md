---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The definitions were checked directly against the open-access full text of DOI 10.3390/sym14020405. For \(f(t)=t/(1+t)\), monotonicity gives the pointwise equality \(\min\{f(a),f(b)\}=f(\min\{a,b\})\), and continuity gives \(\sup f(m)=f(\sup m)\) even without an extremizing pair. These two steps reconstruct the complete proof of \(J_1(X)=J(X)/(1+J(X))\).

The source's Proposition 2 was also checked: \(J_1(X)\le2/3\). Substitution into the printed Corollary 2 right-hand side gives a quantity at most \(-7\). Independently, taking \(y=x\) in the definition of \(\rho_X(1)\) gives a candidate value \(0\), so \(\rho_X(1)\ge0\). Hence the printed Corollary 2 is impossible as written.

No numerical experiment, finite enumeration, or unproved asymptotic step is used. The verification does not claim an optimal replacement modulus-of-smoothness inequality and does not assess unrelated results in the source paper.
