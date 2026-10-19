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

# Exact verification of the degree-five Clebsch zero-forcing classification

The standalone files `verify_white.cpp`, `verify_group.py`, and `six_white_orbit_certificate.csv` constitute a complete finite verification of all computational assertions in the theorem. Recompile and execute in their common directory:

```
g++ -O2 -std=c++17 -Wall -Wextra -o verify_white verify_white.cpp
./verify_white
python3 verify_group.py
```

Observed output:

```
VERIFY_CPP_OK vertex_sets=65536 forcing_sets=9961
VERIFY_CPP_OK polynomial=10:3872,11:3632,12:1760,13:560,14:120,15:16,16:1
VERIFY_CPP_OK inclusion_minimal_sets=3872 all_size_10=true
VERIFY_CPP_OK propagation_time_minimum_sets=2 all_3872=true
VERIFY_GROUP_OK subsets=65536 zero_forcing=9961 minimum_sets=3872
VERIFY_GROUP_OK 6-white-orbits=18 forcing_orbits=7 size_distribution=960,960,480,480,480,320,192
VERIFY_GROUP_OK all_1920_maps_are_automorphisms=true minimum_all_two_rounds=true
VERIFY_GROUP_OK inclusion_minimal_10=3872 no_larger_inclusion_minimal=true
```

The C++ program iterates all \(2^{16}\) initial blue masks by complement-white masks and performs bitwise simultaneous forcing. The independent Python program reconstructs all transitions with vertex sets, verifies each deletion-minimal black set, generates automorphisms from all 120 permutations of the five XOR generators and all 16 translations, checks adjacency preservation, then creates the 18 complementary six-white orbits. The supplied CSV is *mandatory input*, checked row-for-row by the Python program: a missing, truncated or altered certificate fails verification.

The graph is completely finite and the loops exhaust their stated universes. No random seeds, external network calls or third-party packages are needed; a Python 3 runtime and a C++17 compiler suffice. The spectral eigenvalue argument and the proof that the constructed subgroup is the full automorphism group are human-readable in `RESULT.md`; they do not depend on simulation logs. Independent mathematical audit and absolute historical priority are not claimed.
