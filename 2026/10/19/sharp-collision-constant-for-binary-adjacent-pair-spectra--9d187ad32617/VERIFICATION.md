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
# Verification of the binary two-mer collision law

The supplied `verify.py` uses only Python's standard library. `python3 verify.py` cross-checks three separate exact finite calculations: explicit enumeration of binary words and grouping by literal ordered pair counts, a dynamic transfer enumerator indexed by endpoints and loop counts, and a binomial run-composition identity. It checks lengths \(2\) through \(16\), then computes exact sums at \(20,30,60,100,160\) to illustrate approach to \(3/(4\pi)\). Those samples are evidence of computational consistency, not a proof of asymptotic convergence.

The proof is the matrix integral and spectral-gap argument in RESULT.md. In particular, the signed endpoint-flow class distinguishes the linear model from a cyclic Markov-type calculation, and the two unit-modulus points each contribute half of the limiting coefficient. No independent external validation was performed.
