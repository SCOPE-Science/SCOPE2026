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

# Reproducibility and mathematical scope

Compile and run the complete enumeration and integral Morse/dihedral certificate with a C++17 compiler:

```sh
g++ -std=c++17 -O3 -Wall -Wextra -pedantic verify_dihedral_cut.cpp -o verify_dihedral_cut
./verify_dihedral_cut
```

Expected successful final line: `ALL_CHECKS_PASSED`. The executed successful run and its five detailed case lines are reproduced verbatim in `verification_output.txt`. Source is standalone; no dependencies beyond the C++17 standard library. The face universe for the largest case contains \(2^{27}\) masks and requires substantial RAM; the executable visits them all. Each of the 210 dihedral elements is checked, rather than only using a few examples. The sequential matching is exact on the full face poset and leaves only the seven-face mask `21846`; the critical theorem is the acyclicity of sequential element matchings as stated in Bayer et al. (Theorem 7.5).

An independently written Python 3 test recomputes the complete face set from a different combinations-based construction, and directly evaluates the signed fixed-simplex traces (not orbit sums) in the \(n=15\), \(k=4\) case:

```sh
python3 verify_signed_15.py
```

Expected line: `INDEPENDENT_SIGNED_CHECK_OK 30 dihedral elements, reduced Lefschetz -1`.

The evidence proves only the five explicitly stated finite cases. Other values of \(k\) or \(n\) are untested and unproved. Integral homology of topological orbit spaces and their homotopy types are not asserted. The nonequivariant sphere classification precedes this calculation, and this package claims only its new full orientation character and rational quotient consequence. Independent external mathematical audit has not been performed.
