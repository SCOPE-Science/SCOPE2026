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

The explicit source formula used is \(J_4=(256\sigma/\rho^9)f(A\sigma^2+B)\), with \(f>0\) for \(\tau>0\). At \((\tau,\alpha)=(\pi,0)\), the following identities were checked directly:

\[
A=0,\quad B=0,\quad \partial_\tau A=-2\pi^3,\quad \partial_\tau B=-\pi^3/2,\quad \partial_\alpha F=0,\quad \partial_{\alpha\alpha}F=2\pi^4\sigma^2.
\]

These give \(\partial_\tau F=-\pi^3(1+4\sigma^2)/2\) and the phase coefficient \(2\pi\sigma^2/(1+4\sigma^2)\) by the implicit-function theorem. The derivative and endpoint limits of the coefficient are elementary. The result is analytic, not a numerical fit. It uses the published Jacobian factorization and the source's theorem that no conjugate point occurs before the cut time. It does not independently reprove the global cut-locus theorem, and no independent audit or independent validation is claimed.
