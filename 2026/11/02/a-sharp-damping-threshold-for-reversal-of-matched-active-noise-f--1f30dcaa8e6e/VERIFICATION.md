---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For stationary symmetric telegraph and sqrt(2)cos(theta) angular diffusion, both force covariances equal exp(-d|s|); four-time Markov propagators give ordered fourth-moment difference (1/2)exp(-d(u+4w+z)), while equal pair contractions remove the fourth-cumulant difference ambiguity. Integrating four ordered oscillator kernels e^{-as}sin(bs)/b (24 orders) gives the 16-signed-gap rational sum; independently reconstructed this expression and exactly matched its rational formula against six positive rational triples using SymPy. The denominator is positive, C0,C1>0 and C2=12a²-30ad-27d² changes sign at a/d=(5+sqrt(61))/4; concave quadratic in b² then has exactly one positive root when C2<0. Matched full output covariance and Gaussian-thermal fourth-cumulant cancellation follow from linear filtering. Six checks are corroboration rather than a universal symbolic simplification certificate.

## originality

PASS

Best-of-knowledge original contribution limited to complete claimed classification and quantitative threshold; classical ingredients and exact previously known special cases credited. Primary comparisons distinguish same mathematical objects from similar names; remaining equivalence risk explicitly documented.

## value

PASS

Two stochastic active mechanisms indistinguishable by ALL second-order stationary observables exhibit a sharp damping-dependent reversal in a higher-order signal. The formula and unique crossover classification resolve a naturally motivated identifiability question in the underdamped harmonic trap, not simply forward moment tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
