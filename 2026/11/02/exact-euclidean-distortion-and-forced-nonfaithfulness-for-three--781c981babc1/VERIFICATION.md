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
# Reproducible verification

Run `python3 verify_kneser.py` in the same directory. The standard-library checker implements the binomial finite-difference eigenvalues, exact candidate inequalities for every \(n\in\{8,\dots,60\}\), two distinct sharp orbit-distance patterns for \(n=9\), and complete centered Gram matrices and exact rational positive-semidefinite elimination for \(n=8,9,10\). For each of these three values it enumerates every triple pair, checks the graph distance classes and noncontracting upper and lower bounds, and checks zero Gram row sums. Its tests are reproducible without numerical tolerances or external packages.

Analytically the proof establishes the full \(n\ge8\) range. In particular, finite verification is not the source of the infinite lower bound: it follows from the \(W_1\) spectral inequality (and from the \(W_1,W_3\) combination when \(n=8\)). The upper bounds use a positive semidefinite, explicit invariant squared-distance matrix and the finite Euclidean distance criterion. The nonfaithfulness and rigidity conclusions use orbit-average saturation, not the checker. This verification does not assess priority or independently certify the mathematics.
