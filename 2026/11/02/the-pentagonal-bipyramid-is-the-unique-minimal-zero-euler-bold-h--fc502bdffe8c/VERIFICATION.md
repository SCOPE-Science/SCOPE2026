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

# Verification of the seven-vertex extremal classification

The standalone source `checks/bold_census.cpp` computes the exact connected domination cochain ranks over the two-element field for every simple connected graph on one through seven labeled vertices. It does not use random trials, external graph databases, floating point arithmetic, or symmetry assumptions to omit cases.

From a directory containing the extracted files:

```sh
g++ -std=c++17 -O3 -Wall -Wextra -pedantic checks/bold_census.cpp -o bold_census
./bold_census
```

`checks/bold_census_output.txt` contains the observed exact standard output, with the final line `ALL_GRAPHS_EXHAUSTED connected=1893732 chi_zero=1716865 positive=252`. The process exits unsuccessfully if any eligible graph does not have exactly the pentagonal-bipyramid structure or if any such graph does not have precisely one mod-two cohomology class in each of degrees two and three. To reproduce the integral witness calculation without relying on the census, inspect the five listed free pairs in `RESULT.md`, which collapse the complement of the connected-dominating upper ideal to an interval and a five-cycle; relative cohomology gives the result.

A finite exhaustive computation proves the finite classification only. No independent audit has been performed, and no general uniqueness assertion above seven vertices is tested or claimed.
