---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

At any strictly positive equilibrium of source reduced equation (18), a_i=beta0+gamma_i>0, w_i=c_i*beta0/a_i=N_i*/N0>0 sum to 1, and r=-N0*beta_prime(N0)/beta0. Re-derived A=-diag(a_i)+b1^T with b_i=w_i(a_i-r*gamma_i), hence det(lambda I-A)=prod_i(lambda+a_i) * sum_i w_i(lambda+r*gamma_i)/(lambda+a_i). For r>0 each summand has positive real part on Re(lambda)>=0 since gamma_i>0; no right-half-plane eigenvalue. For r=0 lambda=0 root; r<0 secular factor is negative at lambda=0 and tends to 1 on positive real axis, giving positive real eigenvalue. Independent rational symbolic check produced spectrum {-2,(-18+8sqrt(3))/5,(-18-8sqrt(3))/5} for supplied mixed-sign 3-state example, which escapes source extra sufficient hypothesis. Applies only finite n positive equilibria and A1-A3; gamma_i strictly positive as in source, no claim about nonhyperbolic nonlinear dynamics.

## originality

PASS

Primary source proves beta_prime<0 equivalent to Hurwitz for two states, but for finite general n Theorem 3.4(ii) adds a same-sign row condition. The present secular positive-real argument genuinely removes that condition in any dimension; no identified earlier published result does so for this exact source-reduced model.

## value

PASS

Eliminating a restrictive published stability hypothesis and giving a sharp necessary-and-sufficient local criterion uniformly in the number of epigenetic states is mathematically substantive. The mixed-sign stable example shows the old condition misses a real regime, not simply an algebraic restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
