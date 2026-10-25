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

# Verification of stationary gap edge laws

## Analytic checks
The proof derives the switch rates of the lumped three-state orientation process: both outer modes leave at \(2\gamma\); the zero mode transitions to either outer mode at \(\gamma\). The stationary angular-mode weights are \((1/4,1/2,1/4)\). The endpoint factorizations of the three deterministic gap fields, their simple restoring slopes, and the current-balance identities can be checked directly by differentiation and expansion.

For every fixed positive parameter tuple, the nonattracting mode integrated masses are suppressed by at least one additional power of endpoint distance. The attracting mode's integrated stationary mass therefore satisfies a first-order logarithmic differential asymptotic with bounded remainder. This controls the **positive, finite** leading constants and the density, not merely the formal exponents. The algebraic identities for the two critical rates follow from the explicit positive roots.

## Numerical procedure and observations
Run `python verify_gap_edges.py` with NumPy and SciPy. The program constructs the full stationary generator on a cosine-clustered grid with 5000 finite-volume cells and solves the normalized sparse stationary system. It checks mode probabilities and uses probabilities inside two small endpoint strips to estimate the power-law CDF slopes. With unit harmonic rate, repulsion, and propulsion, and with flip rates \(0.35, 0.8, 1, 2.8\), the predicted lower/upper slopes are approximately \((0.1479,0.5521)\), \((0.3381,1.2619)\), \((0.4226,1.5774)\), and \((1.1834,4.4166)\). Finite-volume slopes approximately \((0.1521,0.5543)\), \((0.3462,1.2605)\), \((0.4320,1.5724)\), and \((1.1965,4.3326)\) agree within the fixed stated tolerance. The four tests sample the two divergent-edge regime, the mixed regime, and the two vanishing-edge regime.

## Scope of verification
The proof, not the numerical computation, supports the asymptotic statements for infinitely small strips and all positive parameter tuples. Finite-volume upwinding has a first-order discretization bias, particularly for the exponent above four where boundary probabilities are extremely small. No numerical test can establish original publication priority. No external independent audit has been performed.
