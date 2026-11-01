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

# Reproducibility and validation

The central infinite-family proof is a finite *symbolic-support* reduction, not a finite-size data extrapolation. There are exactly nine matched-pair color types and 511 nonempty supports. Updates of all pairs with a given type are identical and depend only on the two clique-excitation flags, which depend only on the support. Thus checking all 511 supports proves the statements for every population size \(n\ge2\).

From the folder containing these files, run:

```sh
python3 verify_support.py
c++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_direct.cpp -o verify_direct
./verify_direct
```

`verify_support.py` checks \(F^{16}=F^4\), determines the minimal eventual period for every support, verifies the exact 9-row table, checks all periodic-support descriptions, and checks exact basin formulas and independent three-cycle configuration expressions for population sizes 2 through 12. The complete output is `support_output.txt`.

`verify_direct.cpp` updates each vertex by inspecting actual within-clique and matched-partner neighbors. It does **not** use the symbolic-support mapping to perform updates. It exhaustively checks all \(9^n\) configurations at each size \(n=2,3,4,5,6\), totaling 597,861 checked initial configurations. It checks exact period-stratified basins, least recurrent periods, sharp transient bounds and periodic configurations; output is `direct_output.txt`.

The exact symbolic support table plus surjection identity proves every all-size basin formula. The independent sitewise finite-size tests are consistency checks, not substitutes for a theorem. Neither an independent external audit nor formal proof-assistant certification is claimed.
