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

# Verification and reproducibility

Run `python3 verify_two_size_multipartite.py` using Python 3 and no third-party packages. In the completed exact-rational run, the script printed:

```text
PASS: 576512 exact rational assertions; 4900 parameter cases; 144 full matrix eigenbasis cases
```

The 4,900 sampled parameter combinations cover \(2\le p,q\le8\) and \(1\le a,b\le10\), testing the rational minmax certificate, row-normalization, support cutoffs, and a grid of 101 candidate parameters each. The 144 full-matrix tests cover \(2\le p,q\le4\) and \(1\le a,b\le4\); each constructs the full edge-weight matrix independently and checks a complete rational eigenbasis. No floating-point eigenvalue estimates are needed for the reported checks.

For the all-dimensional theorem, the critical non-computational steps are: (i) convex group averaging for \(\|P-J_N/N\|_2\); (ii) the complete eigenbasis consisting of the constant, the two kinds of part contrasts, the aggregate type contrast, and within-part zero modes; and (iii) a minimax of two strictly decreasing affine functions and one strictly increasing affine function, with exact crossover and interval caps. These steps are developed in `RESULT.md`. Finite sampling does not establish an infinite-family identity, nor is the self-review an independent audit.
