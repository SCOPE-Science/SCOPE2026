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

The verifier constructs each square-page book graph \(B_r\), computes all-pairs vertex distances by breadth-first search, converts them to vertex-to-edge distances, enumerates every adjacent edge pair, and evaluates the local edge metric definition directly.

For every \(5\le r\le8\), it enumerates every vertex set through size \(r-1\). It confirms that every smaller set fails and that every size-\(r-1\) generator has exactly one omitted page, exactly one selected non-spine vertex on every other page, and at least two selected vertices of each orientation. It also checks the exact basis count
\[
r\bigl(2^{r-1}-2r\bigr).
\]

Recorded output:

```text
VERIFY_OK
book_parameters_checked = 4
parameters r = 5..8
subset_trials_through_size_r_minus_1 = 82164
size_r_minus_1_candidate_trials = 42329
minimum_bases_checked = 1396
adjacent_edge_neighborhoods_checked = 252
all smaller sets failed
all minimum sets matched: one omitted page, one vertex per other page, at least two a-choices and two b-choices
all basis counts matched r*(2^(r-1)-2r)
```

The finite computation is corroborative only. The theorem for arbitrary \(r\ge5\) follows from the explicit neighborhood formulas and the hitting-set proof.
