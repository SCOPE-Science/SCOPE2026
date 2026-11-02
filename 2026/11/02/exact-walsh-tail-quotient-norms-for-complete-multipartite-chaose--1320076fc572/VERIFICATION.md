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

The standalone `checks/verify.py` uses the Python standard library only. Executing `python checks/verify.py` checks 269 block-size tuples, each with two through four nonempty blocks and a total of at most eleven coordinates. It computes the Walsh–Hadamard transform in exact integers after scaling by an exact rational constant, then checks every Fourier coefficient of degree at most the number of blocks, the sharp dual pairing, the constructed supremum norm, and an exact weighted stability inequality under a high-degree parity perturbation.

Observed output: `PASS exact Fourier, dual, optimizer, and stability checks: 269 cases`.

The proof in `RESULT.md` establishes all integer dimensions. No numerical experiment establishes its infinite quantifiers, the asymptotic error, or literature priority. Independent audit has not been performed.
