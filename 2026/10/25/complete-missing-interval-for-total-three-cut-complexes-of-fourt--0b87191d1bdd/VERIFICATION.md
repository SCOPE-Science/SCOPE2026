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
# Finite proof checks and reproducibility

From the directory containing the files, compile and execute the complete discrete-Morse face-poset checker:

```sh
c++ -O2 -std=c++17 -Wall -Wextra tools/verify_morse.cpp -o verify_morse
./verify_morse 16 20
```

Its stdout must equal `evidence/verify_morse_output.txt`. It tests all legal faces, all selected face pairs, all face-poset covers and a full Kahn topological ordering. A nonzero exit status signals a failed invariant. The program uses bounded 32-bit masks; all relevant orders are at most 20.

Recompute independently the mod-two homology of the Alexander dual by standard-library Python:

```sh
python3 tools/verify_dual.py
```

Its stdout must equal `evidence/verify_dual_output.txt`. This program generates the dual's admissible subsets directly, then reduces every mod-two boundary matrix. The reduced dual Betti groups in dimensions \(7,5,5,5,4\) have ranks \(3,1,1,1,3\). This agrees with integral Morse homotopy by combinatorial Alexander duality, but a mod-two check alone could not have proved integral homotopy.

The verifier outputs were regenerated from the exact packaged source before packaging. The enumerations exhaust the five orders and do not constitute a proof beyond them. There are no external datasets, computational heuristics or randomized steps.
