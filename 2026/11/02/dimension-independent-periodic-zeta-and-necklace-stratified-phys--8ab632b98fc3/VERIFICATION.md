---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Read RESULT.md from frozen Git tree. On [0,1/2) the first g branch contracts geometrically to 1/2, while J=[1/2,1] is a full slope ±2 tent with mixing normalized Lebesgue. F_n^n=g×⋯×g; each a.e. low/high word s has low coordinates tending to c=1/2 and k high coordinates generic for k-product tent measure, with n interleaved phases. Distinct rotating words yield μ_[s] average of product δ_c or λ over necklace; a.e. basin is union d(s) open cells of volume 2^-n, so exact mass d/2^n; ergodicity follows cyclic mixing components, entropy k/n log2 by power/product formulas. Burnside enumerates total and k-specific binary necklaces. Any periodic point must be in J^n; F_n restricted there has exactly two inverse branches, and each length-m inverse word composition has contracting n-th power with ratio≤2^-m, hence one fixed point. Critical tent preimages cannot yield distinct periodic symbolic duplicates since critical 3/4 goes to 1 then c; #Fix=2^m for any n,m. Uniform random inverse-branch contractions yield unique stationary λ^⊗n and weak equidistribution; h_top F_n=log2 and this is unique MME. Independent exact Burnside enumeration n=2..8 confirms necklace counts, not an all-n proof.

## originality

PASS

Best-of-knowledge claim-specific originality after actual Resultary semantic search and primary literature comparisons, rather than title-only matches. Known two-dimensional omega-limit results and general symbolic entropy tools do not logically assert uniqueness of the physical laws by necklace, exact basin masses or all n,m fixed point counts. The new proof uses the special one-link identity structure, not arbitrary Cournot maps and not the entire open problem. Inaccessible/nonexhaustively read sources are not asserted to be whole-document noncoverage; residual risks below.

## value

PASS

The explicit cyclic extension of an established Cournot dynamical example yields a natural exactly solvable higher-dimensional system. The contrast between exponentially-many physical basins and dimension-free zeta / periodic-point equidistribution is a mathematically motivated dynamical/statistical classification; the special one-active-link restriction is candidly stated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
