# Independent audit — sharp Massey-order boundary at the Limonchenko–Panov K0
- Record: `2026/09/10/007`
- Audited tree: `ab9e90d04613cbe4e9e59e80dd519a4faccbc5a1`
- Audited branch/commit: `main` / `e96707428e1608ae0287a471173e57e9f975206d`
- Disposition: **PASSED**

## Correctness

**PASS**

- Independent exact-Q recomputation from the record's fifteen pinned minimal non-faces gives H^p(Z_K0;Q) dimensions {0:1,5:4,7:3,8:10,9:3,10:4,11:13,12:21,13:21,14:8}; in particular H^3=0, the lowest positive degree is 5, and the top nonzero degree is 14.
- The same 512-induced-subcomplex sweep gives 61 nonempty Hochster supports, each on at least three vertices. Exhaustive set packing gives no four pairwise-disjoint supports and exactly one disjoint triple, {123},{456},{789}.
- The standard n-fold Massey degree formula puts every fourfold product of positive-degree classes in degree at least 4*5-2=18, above the top degree 14. Thus any defined value lies in the zero group. This is independent of the stronger disjoint-support obstruction.
- The committed independent homology engine builds faces downward from facets and agrees with the primary minimal-nonface engine on the full complex and selected induced subcomplexes; the record's principal theorem does not depend on the paper's separate dimension wording.

## Originality

**PASS_NARROW**

- Limonchenko-Panov 2201.12779 supplies this K0 example, trivial cup product, and a nontrivial triple Massey product; it does not state the audited H^3/support census or the degree-18-versus-14 fourfold obstruction.
- Grbić-Linton 1911.07083 develops general constructions of higher Massey products in moment-angle complexes. Targeted comparison did not locate this exact K0 cutoff as a stated result. The priority claim is therefore restricted to the explicit K0 obstruction profile, not to general Massey-product machinery.

## Scientific value

**PASS**

- The exact obstruction closes a natural next-order question for a published minimally-non-Golod reference example: the published triple is genuinely maximal in order for positive-degree Massey products over Q.
- The support census and full rational degree table are reusable invariants of the fixed nine-vertex complex rather than a free parameter tweak. The result is narrow, but it prevents repeated searches for nonexistent fourfold products on this standard example.

## Reproducibility and source checks

- Parsed the fifteen minimal non-faces fixed in RESULT.md and recomputed reduced rational homology for every induced subcomplex.
- Reaggregated the Hochster decomposition, obtaining the stated cohomology degree table and H^3=0.
- Enumerated all nonzero supports and all disjoint triples/quadruples; obtained exactly one triple {123},{456},{789} and zero quadruples.
- Inspected the committed primary and independent homology verifier sources and their exact tree/blob identities.

## Literature comparison

- [Minimally non-Golod face rings and Massey products](https://arxiv.org/abs/2201.12779): Limonchenko and Panov construct a minimally non-Golod complex whose moment-angle cohomology has trivial cup product and a nontrivial triple Massey product; this is the source example pinned by the record.
- [Non-trivial higher Massey products in moment-angle complexes](https://arxiv.org/abs/1911.07083): Grbić and Linton give a general construction framework for arbitrary higher Massey products in moment-angle complexes; it is relevant prior machinery but does not state the audited K0 cutoff.

## Limitations

- The paper source contains descriptive information beyond the fifteen-minimal-nonface presentation; this audit treats the explicit published list as the record's mathematical object.
- No integral-torsion extension is claimed.
- Audit is over rational coefficients, matching the record.
- Originality search is targeted and supports only the narrow K0-specific profile, not an unconditional global priority claim.

## Publication decision

The scientific claim survives this independent three-axis audit without a substantive research-file edit. The import plan keeps the source record and adds this audit evidence plus a canonical independent-audit update to `VERIFICATION.md`. No GitHub change is claimed as already applied.
