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

# Verification scope

The mathematical proof establishes the exact mean, existence of optimizing rates, compactness of all optimizer sequences and the unique limiting optimizer for every integer target distance. The numerical program `verify.py` compares the Bessel-square Laplace integral with Legendre Q, evaluates an independent toroidal Q representation, checks finite Hamiltonian propagation against the Bessel amplitude, and tests finite-distance optimizer convergence and normalized K0 asymptotics.

From the delivered executable and its listed dependencies, the completed run returned:

`VERIFY_OK bessel_legendre=15 legendre_integrals=8 finite_path=16 optima=5 scaling=4 root=1.552651255645 constant=3.262211749336 max_error=1.65e-09`

Execute `python verify.py` in a directory containing the supplied script and `requirements.txt` after installing those requirements. Finite-path and grid comparisons are numerical corroboration, not exhaustive proof over all positive rates, all target distances or all valid restarting protocols. Mathematical uniqueness is proved only for the asymptotic optimal scaled rate, not each finite-distance optimizer. The waiting time is exponential independently on each trial, every failure discards and reprepares the initial pure state, and measurement overhead is assumed zero. No independent audit has been performed.
