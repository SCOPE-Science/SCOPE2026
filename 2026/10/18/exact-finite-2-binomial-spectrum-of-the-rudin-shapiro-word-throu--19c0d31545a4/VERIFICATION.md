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

# Reproducibility and checks

The table is a complete classification only for positive integer lengths at most \(4096\). The all-length factor-cover formula is proved separately in `RESULT.md`.

From a directory containing `enumerate.cpp`, `verify_independent.cpp`, `spectrum.csv` and `dyadic_weights.csv`, use a C++17 compiler:

```sh
g++ -O2 -std=c++17 -Wall -Wextra -Werror enumerate.cpp -o enumerate
./enumerate reproduced_spectrum.csv reproduced_dyadic_weights.csv
cmp spectrum.csv reproduced_spectrum.csv
cmp dyadic_weights.csv reproduced_dyadic_weights.csv
g++ -O2 -std=c++17 -Wall -Wextra -Werror verify_independent.cpp -o verify_independent
./verify_independent spectrum.csv dyadic_weights.csv
```

Executed checks: both executables compiled without warnings, both printed `VERIFY_OK`, the two regenerated CSV files agreed byte-for-byte with the supplied files, and all \(4096\) spectrum rows plus dyadic weight distributions were reproduced with different generation strategies. The first enumerator also checks the complete substitution pair set and base-two coding for the initial \(65536\) positions. These computational checks are attached to a mathematical exhaustive-factor proof, rather than being extrapolated from a sample.

The second executable is independent as an *algorithmic construction*, not as an external audit. There is no independent human review or infinite-length numeric inference. A recipient can rerun all checks without network services, external datasets or unpublished dependencies.
