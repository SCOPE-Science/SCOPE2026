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

# Reproducible exact checks

The three standalone source files depend only on a conventional Python 3 standard library or a C++17 compiler, with no remote data, downloads or computer algebra system required.

Run from the package root:

```sh
python3 code/check_values.py > /tmp/check_values_output.json
c++ -std=c++17 -O2 code/check_coefficients.cpp -o /tmp/check_coefficients
/tmp/check_coefficients > /tmp/check_coefficients_output.txt
python3 code/verify_models.py > /tmp/verify_models_output.txt
```

Compare each generated file with `data/check_values_output.json`, `data/check_coefficients_output.txt`, and `data/verify_models_output.txt`, respectively, using an exact byte comparison, or compare the JSON files as parsed objects if differing JSON whitespace was introduced by a different Python installation. All outputs were reproduced from the delivered standalone source files. The coefficient enumeration exhausts all 823543 septuples, the interpolation independently exhausts all 924 permissible evaluation vectors, and the projective orbit check covers all 336 source projective transformations and three square scalar factors. The final model checker performs an independent quadratic-extension field enumeration and polynomial irreducibility certificate.

The conceptual proof that these finite domains are complete, including the evaluation-map hyperplane and the uniqueness of the genus-two hyperelliptic quotient, is given in `RESULT.md`. The programs do not prove general claims about other finite fields, other genera, unpublished prior results or uniqueness beyond the fully enumerated finite space. No external independent audit has been performed.
