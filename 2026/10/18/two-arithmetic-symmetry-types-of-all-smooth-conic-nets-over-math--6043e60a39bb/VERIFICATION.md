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
# Exact reproducibility checks

Run these commands in this directory, with a C++17 compiler, Python 3, NumPy, and SymPy:

```sh
g++ -O3 -std=c++17 census_nets.cpp -o census_nets
./census_nets
g++ -O3 -std=c++17 census_pencils.cpp -o census_pencils
./census_pencils
python independent_net_census.py
python verify_structure.py
python rankone_groebner.py
```

`census_nets.cpp` creates `conic_nets_q5.bin` as exactly 8,000 RREF three-by-six matrices with entries stored as individual bytes. `independent_net_census.py` generates its own RREF sweep and independently expanded determinant, requiring exact equality of all 8,000 records with the compiled result; a SHA-256 digest is also checked. `census_pencils.cpp` independently counts all smooth pencils. `verify_structure.py` checks projective orbit closure, orbit sizes, pencil incidence multiplicities and the fact that the two extensions have opposite orbit types, and verifies projective-point permutations for the two representatives. `rankone_groebner.py` computes exact ideals of geometric rank-one quadratics in three projective parameter charts. Outputs from the packaged executions are in `VERIFY_OUTPUT.txt`.

These are complete finite enumerations of their stated domains; they do not constitute a general-field proof or an independent external review. The irreducible cubic certificate in the first orbit, together with the unit ideals in the remaining charts and in the second orbit, proves the geometric rank-one assertion without treating a bounded extension-field search as exhaustive.
