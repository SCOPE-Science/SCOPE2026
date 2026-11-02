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

Use Python 3.11 or later, without third-party packages. From the directory containing all the supplied artifacts, run:

```sh
python3 verify.py
python3 series_certificate.py
```

Both commands were run against these actual files. The first produced `VERIFY_OK` after checking the exact channel matrix, output mixture, constant conditional entropy, and positive gaps with high-precision optimization at six crossover probabilities. The second produced `SERIES_CERTIFICATE_OK` from exact rational formal power-series arithmetic and recovered the coefficients through order ten of the entropy gain. The recorded full outputs are `verify_output.txt` and `series_output.txt`.

These checks are finite or formal calculations and do not, by themselves, establish an all-parameter assertion; the analytic concavity proof and implicit-function argument are essential. Neither proof assistant certification nor independent mathematical auditing is claimed.
