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

# Reproducibility and scientific limits

The new theorem is a complete finite classification at modulus \(124\), not a statement deduced from a finite sample of unbounded cases. The direct C++ enumerator traverses exactly \(\binom{122}{5}=207288004\) sorted normalized subsets; it checks all \(64\) subset sums of the six nonzero residues and then tests all \(1716\) seven-coordinate nonnegative multiplicity vectors summing to seven. It returns ten valid sets and \(5192384\) subset-sum-injective candidates. The separately implemented bitset-pruned enumeration returns the identical ten sets and reaches exactly the same \(5192384\) leaves. Direct source-to-source and output-to-output comparison was performed with independent algorithms. The Python checker enumerates all \(7440\) affine maps of the canonical seven-set and verifies that its orbit is free and that the ten normalized orbit images agree with the exhaustive list.

With an GNU-compatible C++17 compiler with 128-bit unsigned integer support and Python3 in the package directory, run:

```
c++ -O3 -std=c++17 enumerate_direct.cpp -o enumerate_direct
./enumerate_direct > direct.txt
c++ -O3 -std=c++17 enumerate_pruned.cpp -o enumerate_pruned
./enumerate_pruned > pruned.txt
cmp direct.txt pruned.txt
cmp direct.txt normalized_valid.txt
python3 verify_affine.py
```

Expected program summaries: `all_combinations=207288004 subset_distinct=5192384 valid=10`, `leaf=5192384 valid=10`, and `ORBIT_OK orbit=7440 normalized=10 canonical_stabilizer=1`. The direct enumeration may take longer than the bitset-pruned one. Integer sizes are exact for these specified counts, and arithmetic residues are reduced modulo \(124\). The foundational unit-difference lemma and affine normalization argument are mathematical and independent of any programming language. The executable census is necessary for closing this particular finite inverse classification. No claim of formal-machine, third-party, or independent mathematical certification is made.
