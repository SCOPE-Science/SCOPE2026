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

The checker enumerates proper colorings of \(\operatorname{Cr}_n\) by first assigning colors on one bipartition class and then generating exactly the color choices permitted on the other class by properness. It tests neighborhood parity directly from the color multiplicities after deleting each matched nonneighbor.

For every \(3\le n\le9\), all palettes below the claimed minimum are exhaustively checked and contain no odd coloring. At the minimum palette, every odd coloring is compared with the structural theorem, and the labeled count is verified.

Recorded output:

```text
VERIFY_OK
n_values_checked = 7
proper_colorings_checked = 1911416
minimum_odd_colorings_checked = 1620
parameters n = 3..9
n = 3 chi_o = 3 minimum_labeled_colorings = 6 proper_colorings_at_min_palette = 66
n = 4 chi_o = 2 minimum_labeled_colorings = 2 proper_colorings_at_min_palette = 2
n = 5 chi_o = 4 minimum_labeled_colorings = 240 proper_colorings_at_min_palette = 9372
n = 6 chi_o = 2 minimum_labeled_colorings = 2 proper_colorings_at_min_palette = 2
n = 7 chi_o = 4 minimum_labeled_colorings = 504 proper_colorings_at_min_palette = 123828
n = 8 chi_o = 2 minimum_labeled_colorings = 2 proper_colorings_at_min_palette = 2
n = 9 chi_o = 4 minimum_labeled_colorings = 864 proper_colorings_at_min_palette = 1773996
all smaller palettes had zero odd colorings
all minimum colorings matched the structural classification
```

The finite computation is corroborative only. The theorem for every \(n\ge3\) follows from the parity and properness proof.
