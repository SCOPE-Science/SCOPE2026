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

The bound is a finite exact result. To reproduce independently, compile the two provided C++17 source files and execute them separately:

```sh
g++ -std=c++17 -O3 -Wall -Wextra -pedantic insdel_exact.cpp -o insdel_exact
./insdel_exact
g++ -std=c++17 -O3 -Wall -Wextra -pedantic insdel_dp_verify.cpp -o insdel_dp_verify
./insdel_dp_verify
python3 verify_orbits.py
```

The first method enumerates all admissible codebook characteristic masks using exact received-word incidence. The second builds forbidden triples through independent three-word shortest-common-supersequence and longest-common-subsequence dynamic programs. Both enumerate all masks of the candidate optimum and next cardinality. The results are displayed in RESULT.md. The length-five insertion-optimal masks and orbit representatives are listed in `maxima_n5_ins.csv`. The third checker confirms all 185 masks are distinct admissible six-word codebooks, verifies that the list is closed under reversal and bit complementation, and reproduces the 52-orbit multiplicities.

The scan uses no Monte Carlo sampling or optimization-solver tolerances. The theorem is confined to lengths two through five. No independent audit or broader generalization is claimed.
