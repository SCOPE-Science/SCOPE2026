---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For G=(C_p)^r, Burnside lemma gives each M_H from F_0 and line marks F_L; conversely M_0 and M_L recover them, with independent mark rows. Orbit-size marginals are A_j=sum_{dimK=j}x_K. On the kernel each A_j (j>=2) vanishes. Each line coordinate is forced as x_L=-sum_{K>=L,dimK>=2}p^(1-dimK)x_K, and the total-cardinality mark forces x_0=0. Remaining parameters have one zero-sum constraint in each dimension >=2, giving nullity sum_{j=2}^r([r choose j]_p-1), image rank (p^r-1)/(p-1)+r. For U,W j-spaces, the integer relation p^(j-1)([G/U]-[G/W])-sum_{L<=U}[G/L]+sum_{L<=W}[G/L] cancels all line and size marks and has distinct leading nonreference coefficients, so these form rational kernel basis. Independent exact rank computation for (C2)^3 produced 16 subgroups, rank10, nullity6 and a zero-mark witness. This is not an integral Smith-basis claim.

## originality

PASS

The recent group-action criterion addresses identical statistics but states only qualitative injectivity. The new elementary abelian rank, complete rational kernel and explicit integral virtual relations are strictly more informative than a yes/no criterion, though classical marks/Brauer relation algebra raises a substantial prior-coverage risk.

## value

PASS

The dimension of the ambiguity space for a complete natural set of subgroup and orbit-size statistics quantifies exactly how many orbit configurations remain unidentified. Explicit integral virtual-set witnesses enable subsequent size-minimization and integral-lattice questions, though those are not claimed solved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
