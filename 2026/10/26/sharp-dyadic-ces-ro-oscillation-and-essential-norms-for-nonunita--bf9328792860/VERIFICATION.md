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
# Reproduction checks

The principal identity is the polynomial equality \(p_n(z)=-(1-z^n)^2/[2n(1-z)]\), extended at \(z=1\) by zero. Substitute \(z=e^{i\theta}\) to recover exactly \(f_n(\theta)=\sin^2(n\theta/2)/(n\sin(\theta/2))\). Strict decrease of the logarithmic derivative on the first lobe and a global bound beyond it prove the root equation rather than merely locating a local numerical maximum.

For a wandering unit vector \(w\) and \(|\zeta|=1\), the normalized vector \(u_L=L^{-1/2}\sum_{j=L}^{2L-1}\zeta^{-j}V^jw\) satisfies \(\|(V-\zeta I)u_L\|=\sqrt{2/L}\) and weak convergence to zero. All compact perturbations thus vanish on this sequence in norm, making the essential-norm lower bound reproducible algebraically.

Solving the strictly defined scalar equations by bisection or another guaranteed one-dimensional root routine gives the checks:

| \(n\) | \(M_n\) |
|---:|---:|
| 1 | 1 |
| 2 | 0.7698003589195008 |
| 3 | 0.7436128024718242 |
| 5 | 0.7312709633307475 |
| 10 | 0.7262580115150891 |
| 20 | 0.7250218962922163 |
| 100 | 0.7246277611776691 |

The unique limiting root is \(x_*=2.331122370414423\ldots\), yielding \(C=0.7246113537767085\ldots\) and \(Cx_*^2/24=0.1640680577938391\ldots\). The analytic implicit-function and stationary-point estimates, not these finite checks, establish the \(O(n^{-4})\) theorem. No independent audit has been performed; full text of one older oscillation paper was unavailable.
