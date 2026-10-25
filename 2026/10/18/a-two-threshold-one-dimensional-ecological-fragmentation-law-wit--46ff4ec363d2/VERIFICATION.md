---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Synchronous capacity-2 competitive update with alpha>1 maps every initial {1,2}-configuration exactly to Bernoulli bits after one update. Thereafter a surviving bit has either zero, one or two occupied neighbors, leading to support Y_i=X_i(1-X_{i-1}X_{i+1}) for alpha<=2 and Z_i=X_i(1-X_{i-1})(1-X_{i+1}) for alpha>2. For alpha in (1,2), length-two runs alone oscillate; at equality they freeze at weight one. Window enumeration gives means 3/8 and 1/8, adjacent/distance-2 covariances (-5,1)/64 and (-1,1)/64 respectively, and common exact Var(S_n)=7n/64 for n>=5. A stationary 2-dependent CLT with nonzero asymptotic variance proves Gaussian limits; cyclic boundary error is O(1). Independent exact evolution of 2^n states for n=5..9 with alpha=3/2,2,5/2 (2,976 state/regime cases) reproduced supports and moments. The open-interval odd/even biomass contrast follows Q_n counts with E Q_n=n/16. These are discrete cycles, not continuous LV systems.

## originality

PASS

The precise ring-degree-two strong-competition attractor support formulas, equal finite-size variances in distinct phases, and CLT for Bernoulli initial data are additional to the general model/period-at-most-two results in Sergo et al.; no corresponding theorem was located in inspected full text. A general upper period bound does not identify attractors, their basins, or exact occupancy fluctuations.

## value

PASS

A natural solvable dimension-one sector of a recently studied ecological competition dynamical system exhibits a non-obvious variance coincidence, two occupancy thresholds and a temporal oscillation threshold invisible to final occupancy. Exact local formulas and CLT give a benchmark for higher-dimensional/random regular ecological fragmentation, rather than just reproducing the general model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
