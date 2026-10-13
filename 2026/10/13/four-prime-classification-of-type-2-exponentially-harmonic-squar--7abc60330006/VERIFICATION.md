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

# Verification

Run `python3 verify.py` with a standard CPython interpreter. The script reconstructs the exponential divisors of a squarefree base's square and confirms that direct harmonic-mean integrality agrees with the claimed product divisibility for every squarefree base through \(12000\). It checks the four sharp three-support realizations and exhausts all larger fourth-prime candidates under the mathematically proved \(r+1\mid48q^2\) bound, using integer-only trial-division primality tests. The expected final message is:

`EXACT_CERTIFICATE_OK q_spectrum=5,7,11,23 four_support=9 largest_base=15906 finite_regression=12000`

The computation checks the nine fourth-prime solutions and no others in the *proven finite search domain*. It is not an infinite certificate for arbitrary prime support. The infinite-support restriction and all reduced cases are established in the proof in `RESULT.md`. No independent audit has been conducted.
