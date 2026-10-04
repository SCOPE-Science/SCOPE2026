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

The analytic proof checks the complete parameter range \(\mu>0\), \(0<\alpha<1/2\), and \(\tau>0\). The critical nonstandard step is strict log-concavity of the Gaussian CDF: for \(h=\phi/\Phi\), \(h'(x)=-h(x)(x+h(x))<0\), with \(x+h(x)>0\) from the Gaussian Mills inequality. This makes the log discovery objective strictly concave after the \(\tau=\tan\theta\) reparameterization. Endpoint derivative signs and the derivative at \(\theta=\pi/4\) establish uniqueness and the strict inference-heavy allocation.

`verify.py` is a standard-library numerical replay, not an infinite proof. It checks covariance algebra, solves the unique first-order condition by bisection over representative levels and signals, reproduces the reported \(\alpha=0.05,\mu=1\) values, approaches the weak-signal closed form, and verifies \(D_{0,\alpha}=\alpha/2\) over several allocations. Its output should end with `VERIFY_OK`.

Unproved extensions include unknown variance, multivariate or adaptive screening, two-sided rules, and objectives other than joint screening and rejection. The literature comparison also retains the stated Cox (1975) access risk.
