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

# Verification notes

`verify_direct.py` performs the full mixed-channel enumeration with directly generated deletion and adjacent-swap output sets and a proper greedy clique-coloring bound. Its latest completed execution printed:

```text
VERIFY_OK optimum=16 labeled=28 orbit_sizes={2: 2, 4: 6} classes=8 VT_classes_failing=8 nodes=159080
```

The independent C++ program `verify_deletion_filter.cpp` builds a deletion-only graph using bit-incidence masks, proves absence of any deletion-only 17-code and enumerates all \(408\) deletion-only 16-codes, of which \(28\) also satisfy adjacent-swap compatibility. Its completed execution printed:

```text
VERIFY_OK length=7 deletion_size17=0 deletion_size16=408 mixed_size16=28 nodes=511342
```

The Python program independently checks that the eight rows of `representatives.tsv` are complete canonical orbit representatives under global reversal and global binary complementation. The file's orbit sizes sum to \(28\). The independent witness file `vt_obstructions.tsv` explicitly supplies the two codewords and a shared transposition output in each syndrome class; the Python program validates all eight witnesses. The Python program additionally tests all eight size-\(16\) VT syndrome classes and confirms each is incompatible with the adjacent-swap condition.

Commands:

```sh
python3 verify_direct.py
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_deletion_filter.cpp -o verify_deletion_filter
./verify_deletion_filter
```

These are reproducible exhaustive computations on a finite universe of \(128\) possible words, not checks of larger lengths. The proof of exhaustiveness depends on the sound coloring bound and complete clique branching, not only on the printed totals. No independent audit has been performed.
