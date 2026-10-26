# Scientific review

## Correctness: PASS

The identified unknowns are the complete coefficient vectors in the linearly independent polynomial spaces \(\mathcal V_i\). The exact orbit equivalence follows in both directions by subtracting the two per-capita growth polynomials and using uniqueness of ODE solutions. The generic claim is witnessed by explicit decoupled rates \(2^{j-1}\): all squarefree degree-at-most-two monomial time exponents are distinct. Their Vandermonde determinants show the product of row Lie-Wronskians is a nonzero polynomial for any fixed positive initial abundance. The nonzero Taylor leading term in the common nearby-time sampling determinant gives finite recovery. The exceptional three-species orbit remains positive and bounded, has a nonzero initial derivative, and satisfies the conserved identity \(x_1x_2=1\), making a nonzero hard triadic term indistinguishable from a shift in intrinsic growth. A standalone exact arithmetic/symbolic program checks finite examples, including an explicit nonsingular model with nonzero hard interaction coefficients. No finite computation substitutes for the general argument.

## Originality: PASS, subject to historical-priority risk

The 2026 motivating study documents near-indistinguishable trajectories and a Hessian-based differential signature but does not prove all-dimension generic single-trajectory full recovery. General higher-order reconstruction (Malizia et al., 2024) and sparse equation discovery (Brunton et al., 2016) give the foundational regression formulation. They do not supply an explicit generic hard-triad orbit Wronskian certificate or the exact positive invariant-leaf counterexample. Duan et al. (2022) study a distinct low-dimensional state-sampling inverse problem; Tahmasebi and Weber (2026) study a symmetry-based discrete-time identification mechanism. Published mathematical-record searches found analogues in other population models but no statement matching or subsuming this combined result. The residual historical risk is a more general theorem for analytic polynomial vector-field identification or persistent excitation that immediately subsumes the special class. Full independent literature vetting has not occurred.

## Mathematical value: PASS

The source identifies a central ecological interpretability problem: empirical nearly equal time series do not tell whether the true mechanism contains higher-order interactions. Here a precise algebraic distinction is proved between exact structural ambiguity and (possibly severe) numerical ill-conditioning. The one-trajectory sufficiency guarantee scales to every community size and uses no designed interventions. The exceptional positive nonstationary example prevents the generic conclusion from being misread as universal. The model-specific guarantee and boundary example can inform which additional interventions are mathematically necessary, although this work does not supply a noise-robust experimental protocol.

## Closest literature and limits

- Calleja-Solanas et al., arXiv:2605.06301 (2026): closely matching ecological growth class and motivating identifiability problem; numerical near-indistinguishability and Hessian signature do not imply the result here.
- Malizia et al., DOI:10.1038/s41467-024-49278-x (2024): general higher-order interaction reconstruction by regression, covering the linear-algebra mechanism but not a model-specific generic trajectory full-rank theorem.
- Brunton et al., DOI:10.1073/pnas.1517384113 (2016): foundational sparse polynomial-library identification, not a complete universal hard-triad orbit characterization.
- Duan et al., arXiv:2209.14191 (2022): single-trajectory inverse dynamics, chiefly for planar LV and state-only snapshots.
- Tahmasebi and Weber, arXiv:2608.08091 (2026): single-trajectory learning under finite-group equivariance, a different structural assumption.

Only exact complete-state and derivative observations are treated. Open sign-constrained coefficient domains are included in the generic claim, but parameter manifolds imposed by conservation laws or biology may lie in its algebraic exceptional locus. Independent review of historical priority and empirical significance remains to be done.

Self-review: passed. Independent audit: not yet performed.
