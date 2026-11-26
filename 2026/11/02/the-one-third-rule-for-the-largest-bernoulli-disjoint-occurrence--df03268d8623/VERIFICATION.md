---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Two disjoint witnesses require and are supplied by two disjoint k-subsets of the one-coordinates. Subtraction gives ΔG=b₂ₖ+b₂ₖ₊₁−bₖ(aₖ+aₖ₊₁). Before ⌈n/3⌉ both masses on the right are at least bₖ by binomial symmetry and unimodality (and the k=0 difference is positive separately). At the boundary the factorial ratios are less than one in the n≡1,2 cases where aₖ+aₖ₊₁≥1. For n=3m the ratio is (3m+1)/(2m+1)<3/2, and adding three fair bits changes the tail sum by (−qₘ₊₁+3qₘ+5qₘ₋₁+qₘ₋₂)/8>0, with 11/8 and 99/64 at m=1,2. After the boundary the consecutive factorial ratio bound 1/6 puts all remaining nonzero ratios below one before the witness mass vanishes, whereupon the difference is directly negative. This covers n≥2 and n=1 is direct. The deficit 2L−L²+R has the common binomial-tail exponential rate, including the rounding offsets at both tails. The analytic proof supplies the all-n quantifier; the frozen finite checker is supplementary.

## originality

PASS

The strongest same-day Resultary match has the identical diagonal tail formula and studies limiting windows, but does not determine the exact maximizing threshold. Its sharp tail equivalent is for a different product-space gap. Neither that record nor the inspected primary statements give the strict integer optimization. The entropy computation itself is standard once the relevant thresholds are known.

## value

PASS

Identical Hamming thresholds form a natural canonical subfamily for asking how far disjoint occurrence falls short of the BK bound. A unique exact threshold in every dimension, including the delicate divisible-by-three case, gives a usable sharp benchmark that neither a limiting window nor the bare large-deviation computation would supply. No value claim is made for a general BK improvement or biased optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
