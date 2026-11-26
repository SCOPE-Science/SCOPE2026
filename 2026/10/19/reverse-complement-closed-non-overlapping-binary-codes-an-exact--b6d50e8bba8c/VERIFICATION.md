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

For binary n>=2 the first-bit and last-bit sets must be disjoint by length-one overlap, forcing one of two complementary orientations. The reversal-plus-bit-flip involution preserves the chosen orientation. Valid codes are unions of internally valid orbits, and pairwise conflict in either prefix/suffix direction is exactly the obstruction to joining orbits; sizes count words, hence weights one or two. Checked every frozen finite certificate row with independent checker /workspace/branches/ce9e9cb2-57a4-4e9e-ae32-1e8f26b6ebfa/check_record3.py, invoked on frozen certificates.json (without executing uploaded verify.py). The checker regenerated the whole oriented orbit graph, validated the primal selection and all weighted clique coverage, and obtained equal selected-word and clique totals at n=2..16: 1,0,1,0,2,0,5,2,14,10,42,44,132,170,430. The largest row has 592 vertices and 4034 edges. For the upper bound, an independent set uses at most one vertex of each clique, so integer cover cost bounds its total weight. The even fixed-word singleton is unbordered; for the odd family at k>=5, a short overlap is excluded by the opposite constant-bit end runs, and a longer one needs an initial zero-run of length >=k-2 in a proper suffix. In the first word this leaves cuts after the first or second symbol (the offsets called positions one and two in the text), and both fail by their initial pattern; in the partner no such proper suffix exists. For k=4 the extra proper suffix starting at the partner's interior two-zero run also mismatches both same-length prefixes (the third symbol already differs in the first word, and the fourth in the partner). The n=9 graph independently confirms positivity. At n=3,5,7 the checker exhausts the 2,8,32 oriented words respectively and finds no internally valid orbit. The n=1 exception holds vacuously for proper overlaps. This certifies the all-length positivity threshold and finite maxima only through 16.

## originality

PASS

Best-of-knowledge pass for the extended exact spectrum through n=16 and the all-length threshold. The configured indexed literature contains actual equivalent coverage of shorter rows, including a complete table through n=12, and a stronger n=3 theorem; these are not credited as independently distinct findings. Neither inspected result yields the four terminal maxima or the all-length threshold. No historical priority is inferred merely from catalogue dates. The mathematical claim reviewed concerns abstract binary words only.

## value

PASS

A whole-orbit closure condition is a natural symmetry restriction on synchronization codes and changes even the question of existence. The exact exceptional odd lengths and the sharp certificate-backed small maxima quantify its effect, especially the nontrivial terminal rows beyond the other indexed table. This supplies usable benchmarks for orbit-based constructions, not just a trivial extremum or a rerun of an unrestricted table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
