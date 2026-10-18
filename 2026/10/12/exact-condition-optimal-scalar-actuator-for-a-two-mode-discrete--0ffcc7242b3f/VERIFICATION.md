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

For stable real diagonal A=diag(a,d), a!=d, the exact series give W=[[px,rsqrt(x(1-x))],[rsqrt(x(1-x)),q(1-x)]], where p=(1-a^2)^-1, q=(1-d^2)^-1, r=(1-ad)^-1. The determinant is (pq-r^2)x(1-x)>0 interior. Since tr(W)^2/det(W)=kappa+1/kappa+2 is monotone in kappa>=1, the ratio (q+(p-q)x)^2/[x(1-x)] has its unique global minimum at x=q/(p+q), with boundary divergence. Optimal equal diagonal energies yield rho=r/sqrt(pq), kappa=(1+rho)/(1-rho)=coth^2(|atanh(a)-atanh(d)|/2). Independently repeated four rational pair checks and the a=0,d=3/5 example with W=[[25,20],[20,25]]/41 and kappa=9; finite tests are not the proof.

## originality

PASS

Known papers provide the discrete Gramian Hadamard kernel, controllability-energy interpretation and several actuator metrics, but the inspected finite-candidate determinant/trace objectives do not imply optimizing Gramian condition over a continuously variable direction. No matching two-eigenvalue hyperbolic optimizer found in searches; this is best-of-knowledge, not historical uniqueness.

## value

PASS

The condition number controls best/worst minimum control energy anisotropy. Its exact two-mode optimal direction, its difference from determinant optimization, and divergence under eigenvalue coalescence yield a useful quantitative actuator-design boundary even for the natural smallest nontrivial diagonal case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
