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

# Finite-field verification and scope

Compile `verify_counts.cpp` with a C++17 compiler using `g++ -std=c++17 -O2 verify_counts.cpp -o verify_counts` and execute `./verify_counts`. The program generates points on the projective hyperplane \(e_1=0\) in unique homogeneous normal form and calculates \(e_2,e_3\) over exact binary extension fields.

Observed output:

```
extension=1 points=5 expected=5
extension=2 points=5 expected=5
extension=3 points=5 expected=5
extension=4 points=29 expected=29
extension=5 points=5 expected=5
extension=6 points=125 expected=125
VERIFY_OK
```

These checks were executed on the included source; no external data files are needed. Exhausting these six fields is not a proof of the formula for all \(n\); that proof uses the geometric Frobenius-graph decomposition and point counts of projective lines. The proof of component multiplicities is by exact bidegree intersection and five local double-vanishing conditions, rather than a black-box symbolic factorization. Independent external audit has not been performed.
