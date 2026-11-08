---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The directed confidence rule uses sigma|xi-xj|+(1-sigma)|xi-mean(N(j))|<epsilon. For 3-path endpoints a<b and center z, donor leaf has neighbor mean z, hence center test is sigma|z-donor|<=sigma d<epsilon; leaf donor center has mean (a+b)/2, giving leaf test >=(1-sigma)d/2>=epsilon. All states remain in [a,b] and the center satisfies an iid affine Bernoulli recursion. Arbitrarily long iid endpoint runs establish a.s. liminf=a,limsup=b; two-sided coupling gives unique stationary Bernoulli convolution, Wasserstein contraction, and ergodic occupation. Mean (a+b)/2 and variance rho*d^2/[4(2-rho)] are exact. For rho=1/2 the dyadic stationary series is Lebesgue uniform, the finite law has 2^t equimass atoms, quantile integration yields W1=[(y-a)^2+(b-y)^2]/(2d 2^t), while TV is always one. Exact rational checks independently confirmed moments/W1 and direct directional confidence at 101 rational center positions. Converse wedge and two-agent convergence follow from extremal center values and symmetric two-vertex confidence.

## originality

PASS

Krishnagopal–Porter introduce the neighborhood-aware directed opinion model, and their accessible published abstract reports simulations and nonstandard states rather than this exact 3-node invariant wedge and stationary distribution. Classical Bernoulli convolutions, the half-contraction uniform law, and coupling arguments are prior probability tools, not the originality claim. The new mathematical content is exact emergence under directional neighborhood tests, sharp all-state receptivity wedge, and pathwise nonconvergence in this named model. The original full paper was not accessible at present; there remains a priority risk that a worked minimal-path example is present in its uninspected body.

## value

PASS

This resolves a natural minimal network mechanism for persistent stochastic opinion motion despite entirely fixed graph and parameters, with exact rather than simulated stationary fluctuations. The all-state wedge and sharp W1/TV distinction are quantitative and meaningful benchmarks for neighborhood-confidence systems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
