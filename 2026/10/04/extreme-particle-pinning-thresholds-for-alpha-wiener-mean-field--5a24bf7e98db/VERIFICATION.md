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

The analytic verification has four steps.

1. Subtract the equal-weight ensemble average from the particle SDE. This gives an exactly solvable linear residual equation and removes the common initial position.
2. With \(f(t)=\alpha/(T-t)\), variation of constants gives the kernel \(((T-t)/(T-s))^\alpha\). At each fixed \(t<T\), the kernel integrals driven by the idiosyncratic Brownian motions are independent centered Gaussians with variance \(v_\alpha(t)\).
3. The centered Gaussian maximum differs from the ordinary absolute-Gaussian maximum by at most \(|\bar Z_n|\). Since \(\sqrt{\log n}|\bar Z_n|\to0\) in probability, both first-order extreme scaling and the Gumbel refinement transfer unchanged.
4. Direct integration of \(v_\alpha(t)\) yields the three endpoint regimes. Combining these with the extreme scaling gives the exact condition \(v_\alpha(t_n)\log n\to0\) for simultaneous pinning.

The companion `verify.py` checks the closed-form variance against numerical quadrature and checks the Gaussian tail normalization underlying the Gumbel centering at several large values of \(n\). It prints `VERIFY_OK` when these finite sanity checks pass. These checks do not replace the asymptotic proof.

Unproved extensions include unequal weights, heterogeneous diffusion scales, non-Gaussian driving noise, arbitrary admissible interaction functions, and continuous-time particle suprema.
