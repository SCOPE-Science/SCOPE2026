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

The supplied source files compile and execute with a C++17 compiler and Python 3.10+ / NetworkX 3.x. Run the following commands from the directory containing the embedded files:

```sh
g++ -O3 -std=c++17 verify_cuts.cpp -o verify_cuts
./verify_cuts
g++ -O3 -std=c++17 verify_independent.cpp -o verify_independent
./verify_independent
python3 verify_orbits.py
```

Observed exact outputs:

```text
VERIFY_ENUM_OK tested_unordered_partitions=8388607 cut7=32 cut8=362
VERIFY_ENUM_OK cut8_types=C8:34,C7+leaf:224,theta(3,4,4):80,K4-subdivision:24
VERIFY_INDEPENDENT_OK recurrence_masks=16777216 cut7=32 cut8=362
VERIFY_INDEPENDENT_OK cut8_partition=8+16:258,10+14:80,12+12:24 exact_mask_equality=true
VERIFY_ORBITS_OK graph=McGee_24_36 girth_cycles=7:32,8:34 automorphisms=32
VERIFY_ORBITS_OK cut7=32,2_orbits cut8=362,21_orbits
VERIFY_ORBITS_OK cut8_types=C8:34,C7+leaf:224,theta:80,balanced_K4:AA:6+AB:16+BB:2
```

`verify_cuts.cpp` regenerates `cut_masks.csv`. `verify_independent.cpp` counts every vertex mask by a separate recurrence and compares the precise canonical cut-mask set to that CSV. `verify_orbits.py` verifies `cut_orbits.csv` and independently determines the component topologies, seven- and eight-cycles, full graph automorphism group, and orbit sizes. These finite checks establish the asserted enumeration if the supplied simple programs execute as written; they do not constitute independent human review, external certification, or a claim about other graphs.
