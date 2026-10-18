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

# Reproducibility and verification

**Scope.** The finite graph is the explicit 20-vertex generalized Petersen graph \(GP(10,2)\). In this instance, all \(2^{20}=1048576\) initial coloring configurations are exhaustively enumerable. No infinite graph family is claimed to have been verified.

The four included artifacts are `direct.cpp`, `fort.cpp`, `verify.py`, and `orbit_certificate.json`. From their common directory on a conventional 64-bit little-endian system with a C++17 compiler and Python 3, execute:

```sh
g++ -O3 -std=c++17 direct.cpp -o direct
./direct
g++ -O3 -std=c++17 fort.cpp -o fort
./fort
python3 verify.py
```

The C++ programs independently generate the binary decisions as well as the minimal-set and minimal-fort masks; the Python program checks all decisions, all masked minimality conditions, reconstructs the entire full automorphism group and verifies every orbit certificate representative. The status files are generated locally by these commands; they are not missing input dependencies. Direct forcing enumerates success and propagation rounds; the second algorithm checks the mathematically equivalent absence of forts by a 20-dimensional subset-zeta transform.

Observed successful verifier output:

```text
CROSSCHECK_OK all_1048576_masks_agree=true total_forcing=804264
MINIMALITY_OK minimal_forcing=3000 sizes=6:2040,7:180,8:780 minimal_forts=830
ORBITS_OK minimal_zero_forcing_orbits orbits= 30 sets= 3000 spectrum= {(6, 60): 6, (6, 120): 14, (7, 60): 1, (7, 120): 1, (8, 60): 3, (8, 120): 5}
ORBITS_OK minimal_fort_orbits orbits= 15 sets= 830 spectrum= {(7, 60): 1, (8, 5): 1, (8, 15): 1, (9, 20): 1, (9, 60): 1, (9, 120): 1, (10, 30): 1, (10, 40): 2, (10, 60): 3, (10, 120): 1, (11, 120): 1, (12, 20): 1}
VERIFY_ALL_OK graph_vertices=20 edges=30 automorphism_order=120
```

**Limitations.** These checks rely on exact finite computations and source correctness; an independent scientific audit has not been carried out. The established previously published minimum value is credited, and the calculations cannot exclude a prior unindexed table of the same results. No other graphs are assessed.
