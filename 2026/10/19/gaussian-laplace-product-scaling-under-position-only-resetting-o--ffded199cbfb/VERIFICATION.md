---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The corrected finding in /workspace/repairs/2/RESULT.md is the exact finite-time Fourier kernel and resulting law. Independence of the Poisson clock gives a reset age with density r exp(-ra) on 0<a<t and atom exp(-rt) at a=t. At age a, the conditional Itô integral against the independent W has variance 4 Lambda^2 times the integral of B_s^2 on [t-a,t], and the age-conditioned medium starts that interval with independent Gaussian B_{t-a} of variance t-a. For q=2 Lambda^2 k^2/t, write the conditional Laplace functional from starting value b as exp(-D(a)b^2/2)C(a). The heat equation with potential -q b^2 gives D'=2q-D^2 and C'/C=-D/2, D(0)=0,C(0)=1. The solution D=w tanh(wa), C=cosh(wa)^(-1/2), w=sqrt(2q), is bounded and gives the expectation by the stopped Itô formula and bounded convergence. Averaging over the initial Gaussian gives C(a)/sqrt(1+(t-a)D(a)), exactly the stated hyperbolic kernel, including a=0, a=t and k=0. In the whole-reset comparison only, the medium starts the final interval at zero and this Gaussian factor is absent. For k!=0 the integrands are strictly ordered in 0<a<t; the no-reset terms agree. The benchmark W_2 bound follows by conditioning on the whole medium path so the independent W integral has mean-square freezing error (2 Lambda^2/t)E[A_t^2]<=4 Lambda^2/(r^2t), then coupling sqrt(min(E,t)) with sqrt(E) using E[(E-t)_+]=exp(-rt)/r. Conditional Gaussian moments and Jensen with exponential age bounds give uniform integrability of each fixed order. The mixture is cZL, its moments give 18 versus 6, the center split at |y|/c and 1 gives the logarithmic coefficient, and the rescaled phase v^2/2+1/v has its unique minimum 3/2 with second derivative 3 at v=1, giving the stated tail constant. Integration of conditional variance gives the stated exact variance. The supplied NumPy/SciPy discretizations were inspected but not executed; they are optional sanity checks, not proof of the kernel or the asymptotics.

## originality

PASS

Pass applies only to the narrowed, exact transient age-conditioned and unconditional characteristic functions. The frozen headline product limit, logarithmic peak, tail and kurtosis materially overlap with the exact same-protocol Resultary record a81738fe04a3. Its L2 freezing estimate plus the elementary exponential censoring coupling yields the frozen W_2 bound without new stochastic analysis; the bound is not used as a novelty rescue. The surviving finite-time full-law kernel was in the frozen proof but is not supplied by the compared same-model scaling or moment results, nor by the exact free/whole-reset or deterministic-medium kernels. Its (t-a)w sinh(wa) term is specifically the transient distributional effect of the retained medium and is absent from the free-law kernel. An exact comparison of the conditional laws is necessary to compute it, not just a parameter substitution in the checked resetting theorems.

## value

PASS

The whole distribution at a specified observation time is a natural object in reset experiments; the long-time scaling law and variance alone cannot predict it. The evaluated single-quadrature transform separates an inherited environment from a renewed one at every finite horizon and provides a direct comparison at every nonzero Fourier frequency. Its explicit age and elapsed-time dependence gives an analytic benchmark without simulating Brownian paths. That is useful beyond restating an age mixture or multiplying the two limiting variables. The value does not rest on a rebranded product law or on the easy inequality in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
