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

For fixed pinned vertices S, solving h_i=lambda(h_{i-1}+h_{i+1})/2 on each source-to-source gap with endpoint values one gives the symmetric hyperbolic cosine profile, with strict decrease of its minimum psi_lambda(g) in gap length. Deleting a source in a cycle merges exactly its two neighbouring positive cyclic gaps; therefore all one-source failures preserve the floor tau iff g_(i-1)+g_i<=B for all i. Summing k inequalities gives 2n<=kB, hence k>=ceil(2n/B); explicit balanced integer gap allocations of k positive parts meet all inequalities, including B=2 and k=2, while B=1 is impossible because each adjacent sum is at least 2. A closed-walk transfer on states g in {1,..,B-1} counts rooted length-k gap sequences, with n/k adjustment from rooted starting vertices. At B=3 and B=4 elementary integer-gap case classification gives the stated residue formulas. Independent subset/composition enumeration checked all n=3..12/B and both special residue phases; separately 2,746 exact rational Gaussian-elimination assertions compared the direct discounted Dirichlet solution after each source loss to the gap criterion for n=3..7 and lambda in {2/5,3/5}. These are bounded corroborations, not universal proofs.

## originality

PASS

Allagan–Pereyra–Massey 2026 define the same discounted support and publish the hyperbolic gap profile in Lemmas 5.3–5.5. Those premises are attributed. Their exact optimization section treats spiders rather than robustness to deleting pinned-source status on cycles; it does not state the adjacent-gap condition, complete minimum-placement census, or B=4 arithmetic transition. Earlier cycle double domination supplies the limiting local B=3-style discrete case but does not immediately imply the fidelity-parametrized full one-failure result. Resultary related complete-bipartite discounted hitting domination is not a cycle source-failure theorem.

## value

PASS

Robust source placement after any single pin loss is a natural reliability version of a recently defined discounted-hitting domination parameter. Exact feasibility, all optimal sets and a labelled transfer census hold across an infinite family for every allowable fidelity. The B=4 even-gap phase produces a concrete phenomenon not equivalent to the ordinary distance-one domination result. This is a motivated full family classification, not an arbitrary computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
