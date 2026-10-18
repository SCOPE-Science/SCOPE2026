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

Use the Exner-Kostenko-Malamud-Neidhardt Theorem 3.5 correspondence from minimal Kirchhoff quantum Laplacian to weighted discrete h0 with m(v)=sum incident edge lengths and b=1/edge length. At z=+i and -i terminal tooth equation gives f_leaf=f_k/(1-z*a^2), |denominator|>=1. The spine flux p_k=(f_k-f_(k+1))/ell_k obeys p1=z*q1*f1 and p_k-p_(k-1)=z*q_k*f_k, with |q_k|<=m(c_k)+a_(k,+)+a_(k,-) summable. All solutions determined by single f1 (dim <=1); summable transfer coefficients imply bounded solution for f1=1; total vertex weight =2 sum lengths finite implies it belongs to ell2(m) (dim >=1). Thus n_+(H0)=n_-(H0)=1 for arbitrary asymmetric tooth lengths. The actual package finite exact-rational checker was read; that check only supports the recurrence, not the infinite tail.

## originality

PASS

Exner et al., arXiv:1705.01831, Theorem 3.5 and Example 4.18, discuss precisely finite-length shrinking combs and explicitly leave index=1 as an expectation while establishing non-self-adjointness. Kostenko-Mugnolo-Nicolussi (2022), Theorem 4.1, Corollary 4.3, Remark 4.12, give general one-finite-volume-end lower bound and some symmetry-dependent equality conclusions, not the upper bound for arbitrarily unequal paired teeth. The direct scalar spine recurrence removes that extra symmetry condition. A weakly indexed decorated Jacobi formulation may already derive the same equality.

## value

PASS

The deficiency index is the precise natural number of self-adjoint extension boundary degrees of freedom at the incomplete comb end, expressly left open as an expectation by the main source. Resolving its exact (1,1) value without metric symmetry is mathematically useful and not a routine restatement of general finite-volume one-end theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
