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

The proof uses two independent analytic checks. First, first-jump conditioning gives a renewal equation for the probability of continuous threshold passage, and direct Laplace inversion gives
\[
q(x)=\frac{c}{c+\lambda\theta}+\frac{\lambda\theta}{c+\lambda\theta}e^{-((c+\lambda\theta)/(c\theta))x}.
\]
Second, monotonicity implies \(\tau_x\le x/c\), so optional stopping of the compensated process is justified and gives
\[
(c+\lambda\theta)\mathbb E\tau_x=x+\mathbb E O_x.
\]
Combining this with exponential memorylessness yields the claimed finite-stage correction.

The bundled `verify.py` evaluates the closed forms at \(c=\lambda=\theta=1\), \(a=1\), and \(b=2\), confirms the martingale balance numerically to tight tolerance, and checks that the corrected mean stage duration is strictly larger than the uncorrected value. This computation is a reproducibility check only; it is not used to infer the universal statement.

Limits: the checker does not validate a general non-exponential jump law, the temperature-dependent model, or any empirical re-fit. Those are outside the accepted claim.
