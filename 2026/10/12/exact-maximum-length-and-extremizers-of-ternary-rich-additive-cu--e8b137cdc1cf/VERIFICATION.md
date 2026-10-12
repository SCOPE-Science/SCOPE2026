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

# Verification

Compile `additive_enum.cpp` using a conforming C++17 compiler, for example:

```sh
c++ -std=c++17 -O2 -Wall -Wextra additive_enum.cpp -o additive_enum
./additive_enum > additive_counts.txt
python3 verify_additive.py additive_counts.txt
```

The enumerator outputs `VISITED 404535`, `COUNT 104 8`, `COUNT 105 0`, eight unique `REP` words, and `VERIFY_ENUM_OK`. The independent Python checker outputs `VERIFY_OK max_len=104 labeled=8 symmetry_orbits=2 independently_bruteforced_lengths=0..10`.

The enumerator searches **all labeled** words over the integer alphabet 0, 1, 2 through length 105, pruning only exactly detected existing additive cubes or failures of rich-word extension. At length 105 no admissible prefix survives, which proves no longer admissible word exists. The program does not substitute a search timeout or a finite partial check for a proof. `representatives.txt` is a convenience copy of the eight complete maximal words.

The Python checker performs direct, independent factor testing and a complete brute-force comparison at lengths up to 10. It separately validates the eight length-104 representatives and every one-letter extension. The two implementations have distinct palindrome algorithms, though they share the elementary definitions. Scientific priority is not mechanically certified; independent audit remains unperformed.
