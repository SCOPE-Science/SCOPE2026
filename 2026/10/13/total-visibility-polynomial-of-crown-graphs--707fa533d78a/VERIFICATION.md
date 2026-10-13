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

The checker constructs \(\operatorname{Cr}_n\) for \(3\le n\le8\), explicitly enumerates all shortest paths for every unordered vertex pair, and tests every vertex subset directly from the total mutual-visibility definition.

It compares the direct result with
\[
|A\setminus X|\ge3,\qquad |B\setminus X|\ge3,
\]
and independently checks every coefficient of
\[
\left(\sum_{k=0}^{n-3}\binom nk z^k\right)^2,
\]
the degree \(2n-6\), and the maximal-set count \(\binom n3^2\).

Recorded output:

```text
n=3: valid_sets=1, degree=0, maximal_sets=1
n=4: valid_sets=25, degree=2, maximal_sets=16
n=5: valid_sets=256, degree=4, maximal_sets=100
n=6: valid_sets=1764, degree=6, maximal_sets=400
n=7: valid_sets=9801, degree=8, maximal_sets=1225
n=8: valid_sets=47961, degree=10, maximal_sets=3136
VERIFY_OK
n_range = 3..8
vertex_subsets_checked = 87360
shortest_path_families_enumerated = 1678
all direct total-visibility tests matched the complement-size criterion
all polynomial coefficients, degrees, and maximal-set counts matched
```

The finite computation is corroborative only. The arbitrary-\(n\) theorem follows from the complete shortest-path analysis in the proof.
