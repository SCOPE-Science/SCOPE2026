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

# Verification of the two-rainbow hexagon theorem

The attached `verify.py` uses only Python's standard library and exact integer and rational arithmetic. It has been executed successfully against the same source code embedded here:

```text
python3 verify.py
PASS: 36 exact kernel identities, sharp 2/3 example, uniqueness determinants
```

The 36 pairwise checks verify \(6A_{jk}=3+x_jx_k+3y_jy_k-(-1)^{j+k}\). The script then verifies that the two uniform alternating triples are normalized, collectively centered, and attain exact success probability \(2/3\). Finally it verifies that each alternating triple's normalization-and-centroid coefficient matrix has nonzero determinant of absolute value \(6\).

The infinite-domain conclusion for **all** real nonnegative vertex distributions is not an enumeration. It is derived in `RESULT.md` by linearly averaging the universal kernel identity, using the collective balance constraints, and proving \(1+ab\ge0\). The equality case follows from the strict nonnegativity of its terms and the unique centered probability law on each alternating triangle.

The review has compared the mathematical claim to the motivating open problem and its cube/facet-depth results, related indexed records, and accessible historical claims. Searches are fallible and cannot prove publication priority. No independent external audit or formal proof certification has been performed.
