---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For positive integer income profile x with n households and total S, direct logs give Theil T=(1/S)log∏x_i^{x_i}+log(n/S), MLD=log(S/n)−(1/n)log∏x_i. Thus signs depend exactly on integers Q=∏x_i^{x_i} and P=∏x_i with opposite direction for MLD. Enumerate all nondecreasing compositions/partitions x of S for 2≤n≤S≤11 and every within-(n,S) pair (408 total). Independent full integer census finds no even weak discrepancy for S≤10 and three strict reversals at S=11: (1,4,6)/(2,2,7), (1,5,5)/(2,2,7), (1,3,3,4)/(2,2,2,5). Independent Q and P products match given integers exactly. No float comparisons used.

## originality

PASS

Generalized entropy endpoints, their decomposability, and rank sensitivity are classical. The finite partition-lattice smallest strict ranking-reversal threshold S=11 and three complete first-layer pairs were not implied or tabulated in available checked prior statements. This is a narrow arithmetic-granularity finding, not an allegedly new inequality measure.

## value

PASS

Theil T and mean log deviation are canonical generalized-entropy endpoints with contrasting tail sensitivity. The exact first integer total at which their ordinal judgments conflict identifies a natural resolution boundary, and three-pair complete first layer improves on an arbitrary numerical example. Scope is mathematically finite and motivated, with no claim of absolute monetary universality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
