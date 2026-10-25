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

# Mathematical verification

Run `python3 verify.py` with a standard Python 3 interpreter. It uses only the `fractions` module. The expected final output is `VERIFY_OK exact assertions: 1403`.

The verifier recomputes the covariance operator using the two deterministic switching matrices instead of relying on the displayed moment matrix. It also verifies the exact factorization of the characteristic determinant at a rational interpolation grid. The total polynomial-degree bounds in the proof establish why these finite exact algebra checks certify the **polynomial identities**, rather than merely testing examples. The spectral-radius classification uses an analytical positivity-preserving-cone argument and is not certified by the grid alone.

The result applies to the local derivative cocycle; the state-dependent full iteration is not claimed to have the same global stability threshold. Independent scientific audit has not been performed.
