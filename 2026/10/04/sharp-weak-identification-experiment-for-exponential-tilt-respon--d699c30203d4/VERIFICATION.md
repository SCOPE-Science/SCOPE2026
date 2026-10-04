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

The analytic verification checks the following chain.

1. Conditioning on the binary response mode gives the exact target-input density ratio
\[
r_{b,\eta}(v)=1+(q_b-p)\frac{\pi_\eta(v)-p}{p(1-p)}.
\]
2. The intercept equation preserving \(p\) is locally smooth and even in \(\eta\), hence the normalized gate perturbation is \(3\eta v+O(\eta^2)\) uniformly.
3. Exact centering removes the linear KL contribution; \(\mathbb E[V^2]=1/3\) supplies the coefficient \(3\) in the normalized gate second moment.
4. Differentiating the exact density with respect to \(b\) gives the Fisher information coefficient.
5. The triangular likelihood-ratio increments are bounded by a constant times \(\eta\), so Lindeberg applies once their means and variances are expanded.

`verify.py` is a deterministic numerical replay using only the Python standard library. It uses the motivating source value of \(p\), solves the intercept equation by bisection, integrates by composite Simpson quadrature, and checks that scaled KL divergence, Fisher information, and the target mean approach their derived constants. Running the packaged file returned `VERIFY_OK`.

The numerical replay is finite and is not evidence for the infinite asymptotic statements by itself. The phase transition and Gaussian limit rely on the analytic expansion and triangular-array argument above. No claim is made about source-model estimation, numerical fitting of ExTRA, or conformal coverage.
