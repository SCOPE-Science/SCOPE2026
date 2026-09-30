# Independent Audit — 2026/09/20/finite-fiber-multiplication-s-number-profile--fe72e16da558

- Audit date: 2026-09-29 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `d2355324acbf974ee561ff25ab12dbf039d56b15`
- Disposition: **PASSED**

## Correctness

**PASS** — Decomposing the sigma-finite measure into its nonatomic part and positive atoms identifies the atomic part of L_p(Omega;C^d) with an l_p-direct sum of Euclidean d-spaces. On each atom, unitary singular-vector changes are isometries and multiplication by A_j has the ordinary Euclidean singular values. Retaining all atomic singular modes above a threshold gives the matching finite-rank upper bound max(gamma,beta_n). Conversely the selected singular modes form n-dimensional witness spaces on which M_A is bounded below by beta_n, while any positive-measure nonatomic set on which ||A(omega)||>t yields an infinite-dimensional L_p witness bounded below by t; these give the lower bounds for approximation, Bernstein and Gelfand numbers. Kolmogorov numbers follow by the exact duality d_n(T**)=c_n(T*) on reflexive L_p spaces and the fact that the adjoint multiplication field has the same fiber singular values and nonatomic essential norm. Finite-rank truncation gives the common upper bound rho=max(gamma,beta_infinity) for distances to compact, finitely strictly singular and strictly singular operators; the same atomic/nonatomic bounded-below witnesses give the reverse bound already for the largest strictly singular ideal. The compactness/FSS/SS equivalence follows immediately from rho=0.

## Originality

**PASS** — Hutton-Morrell-Retherford (1976) is classical prior art for diagonal operators, approximation numbers and Kolmogorov diameters; Gupta-Acharya (2011) relate approximation numbers of matrix transformations to component operators and characterize diagonal approximability; Plichko-Shevchik (1999) analyze subspaces on which scalar multiplication is an isomorphism; and Duru-Kitover-Orhon (2013) characterize vector-valued multiplication operators. Those ingredients cover important slices of the argument. Targeted searches did not locate the submitted exact mixed atomic/nonatomic profile simultaneously for a_n,b_n,c_n,d_n, together with the three operator-ideal distances and matrix-valued finite fibers. The originality claim is therefore a synthesis/classification theorem for this concrete finite-fiber setting, not a claim that scalar diagonal s-number theory is new.

## Scientific value

**PASS** — The theorem packages approximation behavior, lower-bound geometry and all three compactness-type ideal distances into one explicit profile determined by the nonatomic essential norm and reordered atomic fiber singular values. The compact=FSS=SS criterion is especially transparent in this setting and can serve as a reusable benchmark for more general operator-valued multipliers.

## Sources

- **Diagonal operators, approximation numbers, and Kolmogoroff diameters** — C. V. Hutton; J. S. Morrell; J. R. Retherford. https://doi.org/10.1016/0021-9045(76)90095-2 — Classical scalar diagonal s-number background.
- **Approximation numbers of matrix transformations and inclusion maps** — M. Gupta; L. R. Acharya. https://doi.org/10.5556/j.tkjm.42.2011.924 — Vector-valued sequence-space approximation-number background and diagonal approximability.
- **On Restriction Properties of Multiplication Operators** — A. Plichko; V. Shevchik. https://doi.org/10.4171/ZAA/867 — Prior work describing infinite-dimensional subspaces on which scalar multiplication operators are isomorphisms.
- **Multiplication operators on vector-valued function spaces** — Hülya Duru; Arkady Kitover; Mehmet Orhon. https://arxiv.org/abs/1104.2806 — Vector-valued multiplication-operator structural background.

## Limitations

- The fiber dimension is fixed and finite and the theorem is restricted to 1<p<infinity; infinite-dimensional fibers and endpoint L_1/L_infinity require separate analysis.
- The exact profile relies on Euclidean singular values inside each finite fiber; arbitrary fiber norms would not admit the same statement.
- Substantial scalar diagonal and multiplication-operator theory is prior art, so novelty is limited to the combined matrix-valued mixed-measure classification.
- No entropy, Weyl or other s-number scales beyond a_n,b_n,c_n,d_n are classified.

## Independent checks

```json
{
  "atomic_lp_direct_sum_reduction_checked": true,
  "finite_rank_upper_profile_checked": true,
  "atomic_and_nonatomic_bounded_below_witnesses_checked": true,
  "reflexive_duality_for_kolmogorov_numbers_checked": true,
  "ideal_distance_squeeze_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access/preprint sources were checked before institutional retrieval, and inaccessible material is explicitly identified rather than inferred.
