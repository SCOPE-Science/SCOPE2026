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

The certificate is self-contained: `certificate.json` supplies the order, potentials, seven exceptional overlap costs, and an ordinary binary word of length \(142\). Only a Python 3 standard library interpreter is required.

Run from the extracted directory:

```sh
python3 verify.py
python3 verify_independent.py
```

The first command must output `VERIFY_OK`; the second must output `INDEPENDENT_OK`. The first script enumerates all \(32\) nine-bit palindromes from their five-bit halves and checks all \(496\) overlap inequalities, the integer potential sum \(81\), deficit sum \(20\), and all ordinary length-nine factors of the witness. The second independently enumerates nine-bit palindromes and recomputes overlap costs by integer masking and shifting. Neither script delegates optimality to an optimizer or relies on a previous computation log.

The mathematical lower bound follows from the overlap tour and the verified pair inequalities; the word proves the upper bound. This is a finite exact certificate, not an asymptotic statement or an independent literature-priority audit.
