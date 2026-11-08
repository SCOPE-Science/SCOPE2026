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

Independent enumeration of the eight activation sets reproduces the exact joint three-variable PGF and symbolic differentiation verifies all three Rayleigh differences equal p²(1-p)/12 [p²(z_k−b_ij)²+(8−8p−p²)/4] with stated shifts. Thus at 0<p<1 stability iff p<=2sqrt(6)-4 by the all-real multiaffine criterion; p=1 gives independent continuous lower-record indicators. The iid thinned-minimum coupling exactly realizes the Markov kernel. Strict stochastic dominance of X_i after an actual jump against its unconditional distribution and strictly increasing later jump hazard give negative covariances for all i<j, 0<p<1. Earlier univariate PGF matches a positive-weight Meixner orthogonal polynomial after c=1-p transform and hence factors into Bernoulli PGFs; p=1 handled separately. Two-variable Bernoulli stability follows from nonpositive covariance, proving minimal horizon. No assertion for 4+ time strong Rayleigh.

## originality

PASS

The model and univariate count PGF are due to Yoshida 2026; the independent-Bernoulli count factorization is a consequence of that PGF and classical Meixner orthogonality and is expressly not credited as an original result. The specific first-three-time generating polynomial and exact real-stability threshold were not present in the materially inspected primary model paper or relevant general strong-Rayleigh statements. This is a qualified best-of-knowledge priority decision, not a proof of absence from the literature.

## value

PASS

A sharp minimum-horizon counterexample to the inference from pairwise negative covariance and Poisson-binomial sums to strong Rayleigh dependence is an intrinsically motivated structural classification. The restoration at the p=1 endpoint identifies the role of the upper atom in the record process; this is not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
