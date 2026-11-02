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
# Reproducible finite checks

The standalone checker `verify.py` requires Python 3 and only the standard library. From the directory containing the extracted files, execute:

```text
python3 verify.py
```

Observed exact output:

```text
VERIFY_OK cases=43 modulus_states_examined=1696943
```

It independently builds each finite-field first-hit basin, iterates each residue of the selected basin modulo the whole prime-power ring, records the first entrance into the exact two-cycle, and checks every predicted histogram coefficient. Its 43 test cases span primes 3, 5, 7, 11, 13, 17, and 19, taking all exponents for which the complete ring has no more than 500,000 elements. In total, 1,696,943 residue states were traversed in the complete moduli, with basin states exhaustively tested.

The verifier also checks basin sizes and the sharp maximum for each case where the level is at least two. Its comparison algorithm uses direct modular orbit iteration, independently of the proof's p-adic valuation-doubling mechanism. The infinite all-prime/all-level statement relies on the symbolic argument in `RESULT.md`, not finite enumeration. No external computational certificate and no independent audit is claimed.
