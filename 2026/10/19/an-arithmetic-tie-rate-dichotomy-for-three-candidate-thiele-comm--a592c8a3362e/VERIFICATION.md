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

The independent, standard-library-only `verify.py` computes exact ballot-score differences for all eight approval types, constructs the one-ballot integer covariance matrix, and exhaustively enumerates every anonymous histogram for electorates of sizes \(1,2,3,4,5,6,8,10,12\). It calculates the exact weighted probability of more than one maximizing Thiele committee for rational weights \(0,1,1/2,2/3\) and the irrational parameter \(\sqrt2-1\). Its independently derived combinatorial summation reconstructs the probability that a fixed pair of committee scores ties for irrational weights. It also tests the finite-denominator equality assertion for reduced rationals with denominators exceeding the electorate size.

Run `python verify.py` from this directory; the script uses no network, no input data files and no nonstandard Python libraries. Successful output ends `All exact-arithmetic checks passed.` Example output includes \(T_{12}(\sqrt2-1)=5619138349/68719476736\) and \(T_{12}(1/2)=10782093289/68719476736\).

**Proof boundary.** Finite enumeration and floating output cannot establish asymptotic rates. The asymptotic theorem is based on the full-lattice Fourier local limit and conditional Gaussian sign arguments proved in the accompanying result. No independent audit has been performed.
