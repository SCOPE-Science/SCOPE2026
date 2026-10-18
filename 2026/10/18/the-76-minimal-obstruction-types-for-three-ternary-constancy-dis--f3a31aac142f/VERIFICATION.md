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

# Exact finite verification

The 27 tuples are indexed by \(9a+3b+c\) with coordinates in \(\{0,1,2\}\). The first executable enumerates all \(\binom{27}{k}\) labelled subsets for every cardinality \(1\le k\le8\). It retains a subset precisely when its coordinate-selector compatibility intersection is empty while every one-point deletion admits a selector. This directly tests the formal definition; the multilinear rank argument in `RESULT.md` proves no larger minimal obstruction exists.

Commands with a C++17 compiler and Python 3:

```sh
g++ -O3 -std=c++17 ternary_constancy_census.cpp -o census
./census
./census --classes > reproduced_classes.csv
diff -u ORBIT_CLASSES.csv reproduced_classes.csv
python3 verify_size5.py
```

The complete labelled distribution is \(54,3672,36612,17793\) at sizes \(5,6,7,8\). The corresponding orbit counts under independent value permutations and attribute permutations are \(1,10,41,24\), totalling \(58,131\) labelled obstructions and \(76\) equivalence classes. The class-list file contains all orbit representatives, encoded by the least 27-bit integer in each orbit, and records each orbit's size. The separately implemented Python union-of-missed-neighborhoods method returns `INDEPENDENT_SIZE5_OK 54`.

The second implementation independently checks only the five-assignment layer; all four layers are exhaustively covered by the primary checker. Computation is a complete proof of the specified finite classification given the transparent enumeration conditions, not a proof of an unspecified infinite extension. Human independent review and external certification are not claimed.
