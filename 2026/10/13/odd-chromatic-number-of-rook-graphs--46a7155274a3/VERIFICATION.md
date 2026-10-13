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

The checker represents \(R_{m,n}\) as an \(m\)-by-\(n\) color matrix and verifies the odd-coloring definition directly from each cell's open neighborhood.

It separately checks the symbolic local criterion:
\[
(i,j)\text{ has an odd neighborhood color}
\quad\Longleftrightarrow\quad
\mathcal R_i\ne\mathcal C_j.
\]

For the rectangular cases
\[
(2,3),\ (2,4),\ (3,4),
\]
every proper \(n\)-coloring is enumerated after fixing the first row to remove color-permutation symmetry, and every one is odd.

For square orders
\[
n=2,3,4,
\]
all normalized proper colorings with \(n\) and \(n+1\) colors are enumerated; none is odd. The explicit cyclic \(n+2\)-color construction is then checked directly.

Recorded output:

```text
VERIFY_OK
rectangular m=2, n=3, normalized proper n-colorings=2, all_odd=2
rectangular m=2, n=4, normalized proper n-colorings=9, all_odd=9
rectangular m=3, n=4, normalized proper n-colorings=24, all_odd=24
square n=2: normalized proper n-colorings=1, odd=0; normalized proper n+1-colorings=3, odd=0; n+2 construction OK
square n=3: normalized proper n-colorings=2, odd=0; normalized proper n+1-colorings=44, odd=0; n+2 construction OK
square n=4: normalized proper n-colorings=24, odd=0; normalized proper n+1-colorings=4920, odd=0; n+2 construction OK
normalized_proper_colorings_checked = 5029
construction_checked_n = 2..50
direct neighborhood parity agrees with row/column-set criterion in all enumerated cases
```

The exhaustive portion checks \(5{,}029\) normalized proper colorings. The construction is also replayed for every
\[
2\le n\le50.
\]

These finite computations corroborate the theorem but do not establish its arbitrary-order quantifiers. The all-order proof is the row/column-set argument in `RESULT.md`.
