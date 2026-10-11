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
# Verification of binary fourth moments

The complete standalone source is `checker.cpp`. Compile it using a standard C++17 compiler:

```sh
g++ -O3 -std=c++17 checker.cpp -o checker
./checker
```

Actual execution returned `CHECK_PASS`, with the exact integer outputs listed below.

| Family | Enumerated cases | Fourth-moment minimum | Minimizing graph classes |
| --- | ---: | ---: | ---: |
| Every binary sixteen-mode four-cube, after sign normalization | 2048 | 336 | 12 normalized sign patterns |
| Quadratic phase on 2 variables | 2 graphs | 20 | 1 |
| Quadratic phase on 3 variables | 8 graphs | 88 | 3 |
| Quadratic phase on 4 variables | 64 graphs | 336 | 12 |
| Quadratic phase on 5 variables | 1024 graphs | 1376 | 60 |
| Quadratic phase on 6 variables | 32768 graphs | 5440 | 360 |
| Quadratic phase on 7 variables | 2097152 graphs | 21888 | 2520 |

For the unrestricted binary four-cube, the checker constructs the \(81\) ordinary (noncyclic) convolution coefficients and squares them exactly for every normalized array. The five sign normalizations account bijectively for all \(65536\) arrays. For quadratic phases the checker independently computes all even-induced-degree vertex subsets, sums the weights \(2^{|S|}\), and compares the *complete set of minimizers* to the path graphs generated from permutations. All loops exhaust explicitly bounded finite sets. The arithmetic identity explaining why the graph formula equals the Fourier fourth moment is proved in `RESULT.md`, rather than assumed from a log.

The validity of the exact search is limited to the stated coefficient spaces and dimensions. No exhaustive claim is made for all binary arrays beyond four dimensions, for all quadratic arrays in dimension eight or above, or for general unit-circle coefficient phases. No independent mathematical audit is represented by these checks.
