# Scientific review: A moving conductance threshold for sharp cut–cycle projection norms on weighted wheels

## Correctness — PASS

The claim precisely specifies the edge-coordinate Banach norm, conductance normalization, graph family, and boundary ranges \(n\ge3\), \(t>0\). The grounded wheel Laplacian is a positive-definite cyclic tridiagonal matrix, so the displayed Green kernel is determined by a directly checked recurrence and periodicity. The sign pattern of that kernel gives two exact absolute column sums for each complementary projection. Strict monotonicity of the diagonal transfer coefficient \(tg_0\) follows from its Fourier spectral expression, proving one threshold per graph and strict growth with graph size. The asymptotic follows from the exact root-formula kernel. The accompanying exact symbolic checker independently recomputes 63 rational parameter configurations, 882 edge columns, and 18 radical Green identities; these finite checks are supportive, not the infinite proof.

## Originality — PASS, subject to bibliographic residual risk

The earliest cited research lead is the May 21, 2023 preprint by Dilworth, Kutzarova, and Ostrovskii (2020 MSC primary 46B04). Their work provides the cycle-space projection framework but explicitly computes other graph families. The 2025 resistance-distance work of Sedlák and Slavík contains strong related Green-inverse information for wheel joins but treats effective resistances/Kirchhoff sums, not absolute projection columns, conductance-dependent maximizing-edge bifurcations, or their moving threshold. The 2021 paper by Balaji, Bapat and Goel studies a *distance-matrix* inverse, not these operator norms. Searches for weighted-wheel cut/cycle projection norms, electrical transfer currents, equivalent formulations, and the \(4/3\) threshold did not return a paper proving this joint statement. Existing wheel *minimum-projection* norms concern a different operator optimization, and do not imply the canonical orthogonal norm formula. Incompletely indexed electrical-current literature is a residual uncertainty; absence of a match is not treated as proof of novelty.

## Mathematical value — PASS

The quantities are natural induced Banach norms of canonical Hodge cut and cycle projections, not arbitrary toy parameters. Across every wheel size and continuous spoke-conductance ratio, the result determines the exact two-edge-orbit endpoint behavior and a sharp, unique geometric change in extremizing edges. The finite-size transition strictly drifts with the number of rim vertices toward a nontrivial limit \(4/3\), and the exact norm has parity-dependent exponential corrections. This is a complete, motivated two-parameter classification distinct from existing resistance or minimum-projection constants.

## Scope and limitations

Only the specified normalized Euclidean projections in real coordinate \(\ell_1\) and \(\ell_\infty\) are considered. No universal best-projection constant is claimed. Nonstandard normalization is defined explicitly; the source article's weighted-edge length norm is not equated with it. Originality remains subject to independently checking older less-searchable literature. No independent mathematical audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
