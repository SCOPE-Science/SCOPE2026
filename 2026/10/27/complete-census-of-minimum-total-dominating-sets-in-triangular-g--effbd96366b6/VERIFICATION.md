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

The classification is proved for every integer \(n\ge4\) in `RESULT.md`. The computations below are finite checks, not substitutes for the infinite argument.

From a directory containing the provided standalone files, run:

```
g++ -std=c++17 -O3 -Wall -Wextra verify.cpp -o verify
./verify
python3 check_formula.py
```

The exhaustive checker enumerates all \(\binom{\binom n2}{\lceil2(n-1)/3\rceil}\) chosen subsets for each \(4\le n\le10\). Its test for each original Johnson vertex demands a **different** selected vertex sharing exactly one ground-set element. Accepted solutions are partitioned into the five possible component-profile categories. Full expected output is in `exhaustive_results.txt`.

The independent arithmetic checker constructs labelled-forest counts by component multiplicities and Prüfer tree counts, comparing these with the displayed simplified formula for each \(4\le n\le100\). Its output is `VERIFY_FORMULA_OK` with the seven exhaustive values. The finite comparison does not show absence of other configurations at arbitrarily large order; that absence follows from the component inequalities in the mathematical proof.

The numerical exhaustive counts are \(12,80,840,630,13440,277200,75600\) for orders \(4,5,6,7,8,9,10\), respectively. Both programs completed successfully with these counts. The source and output are bundled for reproducibility, without relying on external software libraries beyond a standard C++17 compiler and Python 3.
