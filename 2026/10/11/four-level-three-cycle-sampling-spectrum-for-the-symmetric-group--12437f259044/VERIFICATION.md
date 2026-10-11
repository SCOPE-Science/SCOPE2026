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

# Reproducibility checks

Run `python3 verify.py` using Python 3 and its standard library. The program enumerates both orientations of each three-cycle in \(S_n\) for \(4\le n\le8\). It constructs the integer Gram matrix with entries equal to the number of fixed points of \(g^{-1}h\) minus one, which is the Hilbert--Schmidt inner product of the corresponding standard-representation matrices. It verifies the spectral multiplicities via the first four integer power traces and verifies the complete annihilator polynomial by exact matrix multiplication. The output must begin with `VERIFY_OK exact_conjugacy_gram_n=4..8` and report five checked dimensions.

The verification was executed against the exact checker embedded in this package and returned `VERIFY_OK`. These cases include both the rank-deficient boundary and level-collision boundary. The checker does not certify the theorem for arbitrarily large \(n\), and the universal proof rests on the representation decomposition, exact projection norms, and Schur averaging in `RESULT.md`. The limiting boundary of the checker is computational rather than a proof limitation.
