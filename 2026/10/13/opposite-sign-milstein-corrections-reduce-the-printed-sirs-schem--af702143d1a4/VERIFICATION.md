---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The open-access source PDF page 6731 prints three diffusion terms -epsilon*sigma_i*X_i dB_i and negative 1/2*(epsilon*sigma_i)^2*X_i centered-square correction terms, whereas Higham Eq. (6.1) is +1/2*g*g_prime times that increment and g*g_prime=q_i^2*X_i>0. For dX=-qX dW, exact normal moments give E[M_minus^2]=1+r+r^2/2, E[M_minus*E]=1+r-r^2/2, E[E^2]=e^r, yielding X0^2[(1+r+r^2/2)^N+e^(Nr)-2(1+r-r^2/2)^N]. For r=q^2T/N its leading MSE is 2X0^2 e^(q^2T)q^4 T h, hence RMS Theta(sqrt(h)). The correct positive Milstein correction yields MSE X0^2[e^(Nr)-(1+r+r^2/2)^N] with leading X0^2 e^(q^2T) q^6 T h^2/6. The Gaussian identities and expansions prove the theorem for any q,T,X0>0 and integer N as specified; an independent 75-digit decimal check for N=64,...,8192 (q=.7,T=1,X0=1.2) confirmed the asymptotic constants, not replacing proof.

## originality

PASS

The comparison is source-specific: Huang, Du, and Liang explicitly print -epsilon*sigma_i*X_i in Model (4.1) and a negative half-square correction in Eq. (4.3), whereas Higham (2001) Eq. (6.1) requires positive one-half*g*g_prime. The exact finite-N scalar wrong-sign mean-square law and its sharp O(h) leading term do not appear in the inspected earlier work. Searches cannot prove absolute priority, and the generic formula makes the sign diagnosis elementary once sources are compared.

## value

PASS

The motivating 2026 SIRS paper uses the printed scheme to support stochastic numerical illustrations, making the correct stochastic Taylor coefficient a mathematically motivated fidelity question rather than an unmotivated sign exercise. The exact scalar witness quantifies a full-order drop from RMS h to RMS h^(1/2), a practically significant convergence-property failure. Source-specific quantitative reproducibility diagnostics are worthwhile despite reliance on elementary Gaussian moments and without new broad SDE theory; the benchmark does not certify the full nonlinear model or authors’ code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
