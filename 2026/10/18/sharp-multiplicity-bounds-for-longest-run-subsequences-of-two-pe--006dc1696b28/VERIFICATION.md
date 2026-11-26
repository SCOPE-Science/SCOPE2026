---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Both copies of two different labels cannot be used: the later first copy separates the earlier first copy from its second copy. Hence the length is at most m+1, with equality realized by doubling m. An optimum doubling i must retain all other labels; a value larger than i must be selected after i in the second permutation. This is feasible exactly at a record i=π_t. Of the smaller labels, exactly i−t can choose their side of ii; each choice vector uniquely determines a word because the order on each side is fixed. Write d_s=i_s−t_s for the r records. Each nonrecord is missing at its preceding record, so sum d_s≥m−r and sum 2^{d_s}≥m. Lower equality forces d_s∈{0,1} and no double-counted missing label: the first block must be (1) or (2,1), and deletion with relabeling preserves equality. For the upper bound, d_s≤m−r and r≤2^{r−1} with equality only at 1 or 2; both record-position/value bounds must be tight, giving exactly the two disjoint prefixes stated for m≥2. The tiling recurrence and factorial counts follow, with m=1 checked separately.

## originality

PASS

The all-permutation record formula and its exact extremizer families, rather than the numerical sequence or the elementary length, are the distinct claim. Retrieved LRS results on hardness/approximation and published special cases do not cover this enumeration.

## value

PASS

The natural length optimum is the same on the entire host family, while the diversity of optimal words varies from linear to exponential. The exact record statistic explains that difference and identifies every extremizing arrangement, a structural enumeration not supplied by approximation or length algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
