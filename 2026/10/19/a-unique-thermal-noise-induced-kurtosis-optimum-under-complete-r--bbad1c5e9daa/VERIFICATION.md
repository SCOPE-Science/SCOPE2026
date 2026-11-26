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

At a stationary independent Poisson age U of rate k, the dimensionless conditional position is centered Gaussian with variance hU+2U−3+4e^(−U)−e^(−2U), using force initialized at zero. Independently reconstructed the rational excess kurtosis via the stationary generator of the scaled position and force, with reset term −k on each nonconstant monomial: (k+j)M_ij=iM_(i−1,j+1)+h·binom(i,2)M_(i−2,j)+j(j−1)M_(i,j−2). Exact symbolic differentiation gives the stated degree-seven sign pattern: + for degrees 7 through 3, unrestricted degree 2, − for degrees 1 and 0. For h>0 there is one positive root by Descartes and the opposite signs at 0 and infinity; the derivative has the opposite sign of this polynomial. Both endpoint excesses are 3. For h=0 the independent formula reduces to 3+54k(k+2)/[(k+3)(k+4)], strictly increasing to 57. The thermal derivative is strictly negative pointwise, hence the optimized height strictly decreases between positive h values. Under h=e³, k=c/e, multiplying the critical polynomial by e² gives limiting sign polynomial 128c⁵−720c²; bracketing its nonzero root and using uniqueness proves the weak-noise scaling. The peak tends to 57 by comparison to the h=0 curve, taking h→0 at fixed k and then k→∞ for the lower bound. At h=1: k*=1.173900687945557, K=5.522908937170489. Replay: python /workspace/calculations/reproduce_frozen.py (check reset_kurtosis). No stationary regime at zero reset rate is used.

## originality

PASS

Best of current knowledge: the same process and full-reset Gaussian renewal propagator are known. The supported distinction is the global shape classification of the stationary kurtosis and its singular change at zero thermal noise, including proof of a unique maximizer for every strictly positive thermal ratio. Computing mixture moments from the propagator is not a novel method.

## value

PASS

Different variances need not order standardized excursion amplitudes. The result identifies the unique extremum of a concrete shape observable and a sharp boundary in thermal noise: the optimum escapes to infinite reset rate on approaching the noise-free limit. Establishing this for arbitrarily small positive noise, rather than for a few plotted choices, is the value. It does not rank first-passage performance or determine positional tail laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
