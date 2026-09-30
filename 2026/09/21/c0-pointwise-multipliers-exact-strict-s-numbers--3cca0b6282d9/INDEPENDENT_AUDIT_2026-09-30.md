# Independent Audit — 2026/09/21/c0-pointwise-multipliers-exact-strict-s-numbers--3cca0b6282d9

- Audit date: 2026-09-30 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `badc4b0dab104c592a600acec02cd3d1b26f0d53`
- Disposition: **PASSED**

## Correctness

**PASS** — The finite strict-s-number identity is correct. For t above lambda_n the superlevel set is finite and clopen, so truncation there is rank <n and gives the upper bound. For t below lambda_n, n points in the superlevel set admit pairwise disjoint compactly supported bump functions; these form a 1-complemented isometric copy of l_infinity^n, and evaluation factors an invertible diagonal through M_phi, forcing every strict s_n above t. For the ideal distances, an infinite superlevel set in a locally compact Hausdorff space supplies disjoint bumps and an isometric c_0 copy on which M_phi is bounded below by t; no strictly singular perturbation can lie within t. Finite superlevel truncations give the matching compact upper bound, and K subset FSS subset SS closes the equality. On compact K, the finite-removal tail is exactly sup_{K'}|phi|, yielding the perfect-space flat profile.

## Originality

**PASS** — Classical work treats diagonal approximation/Kolmogorov numbers and general strict s-number theory; Edmunds-Lang give other non-Hilbert operators for which strict s-numbers coincide. Kiwerski-Tomaszewski (published 2026; preprint 2022) compute essential and weak essential norms for pointwise multipliers between Kothe spaces, not the all-strict-s-number profile or the K/FSS/SS distance collapse on arbitrary C_0(Omega). Aksoy-Lewicki (1997) is the closest diagonal/s-number source: its abstract and bibliographic material were available, but full theorem text could not be obtained after open-access attempts and authorized retrieval returned no verified PDF. That source could overlap the discrete diagonal subcase, but would not by its stated scope cover the arbitrary C_0 topological witnesses and three ideal-distance theorem; this residual overlap is recorded rather than claimed away.

## Scientific value

**PASS** — The theorem supplies a complete finite and essential profile for a broad natural operator class, showing that all strict s-number scales collapse to a simple topological order statistic and that compactness, finite strict singularity, and strict singularity have the same exact distance. The perfect-space flatness corollary is a particularly transparent structural consequence.

## Sources

- **s-Numbers of operators in Banach spaces** — Albrecht Pietsch. https://doi.org/10.4064/sm-51-3-201-223 — Foundational strict s-number framework.
- **Diagonal Operators, S-Numbers, and Bernstein Pairs** — Asuman Güven Aksoy; Grzegorz Lewicki. https://scholarship.claremont.edu/cmc_fac_pub/542/ — Closest older diagonal/s-number comparison. Abstract checked; full theorem text remained unavailable after lawful attempts.
- **Coincidence and Calculation of some Strict s-Numbers** — David E. Edmunds; Jan Lang. https://doi.org/10.4171/ZAA/1453 — Prior exact coincidence examples for integral operators and Sobolev embeddings, not pointwise C_0 multipliers.
- **Essential Norms of Pointwise Multipliers in the Non-Algebraic Setting** — Tomasz Kiwerski; Jakub Tomaszewski. https://arxiv.org/abs/2212.06723 — Recent essential/weak-essential norm theory for multipliers between Kothe spaces; no all-strict-s-number or SS/FSS distance theorem is stated in its abstract.

## Limitations

- Only scalar pointwise multipliers on C_0(Omega) are covered.
- The infinite-dimensional c_0 witness is not claimed complemented.
- Aksoy-Lewicki (1997) could not be inspected at theorem level; possible overlap with the discrete diagonal subcase remains a documented originality risk.
- No claim is made for weighted composition operators or arbitrary central operators on Banach lattices.

## Independent checks

```json
{
  "finite_rank_superlevel_upper_bound_checked": true,
  "one_complemented_linf_factorization_checked": true,
  "c0_strict_singularity_obstruction_checked": true,
  "derived_set_formula_checked": true,
  "aksoy_lewicki_abstract_checked": true,
  "open_access_first": true,
  "oxford_used": true,
  "oxford_job_id": "b33bb0371037091e4acfd891be4179f5",
  "oxford_status": "no_pdf",
  "inaccessible_material_not_claimed_read": true,
  "decisive_inaccessible_comparison": false
}
```

GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. Open-access/preprint sources were checked before authorized institutional retrieval. Inaccessible material is explicitly identified and is not claimed read.
