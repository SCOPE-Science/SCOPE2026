# Independent audit — All-vector Lévy measures and measure tomography in bidisc Dirichlet spaces

Date: 2026-10-01 UTC

Disposition: passed.

## Final claim

For every vector in the bidisc Dirichlet-type space, the coordinate forward-difference representing measures are radial pushforwards of trace energies; the zero pair-defect then gives the joint Lévy face decomposition and drift. A countable polynomial probe family reconstructs both defining measures, with interior mass carried by the Lévy part and boundary mass by the drift.

## Correctness

PASS. The full 10-page Bera–Sequeira preprint was inspected. It explicitly asks the arbitrary-vector question, proves the zero-defect all-vector face decomposition in Theorem 2.4, and computes the defining-measure formula only for the cyclic vector. The audited proof correctly combines the polynomial defect identity with bounded extension of the restriction maps, intertwining, Hausdorff uniqueness, and the one-variable Lévy relation. The tomography step is a valid Fourier disintegration argument; the fiber at radius zero is separately fixed by the radial mass.

## Originality

PASS. The primary preprint leaves the arbitrary-vector defining-measure relation as Question 1.3 and its explicit formula is only for the cyclic vector. Semantic searches of published records returned no earlier equivalent all-vector trace formula or countable interior/boundary tomography theorem. The prior zero-defect face theorem and polynomial defect identity are ingredients but do not themselves imply the countable angular reconstruction without the new probe argument.

## Value

PASS. This closes an explicit source-paper question and identifies an exact information boundary: interior defining mass is visible in the Lévy measure while boundary mass moves to the drift. The countable separating probe family is a natural structural consequence rather than an arbitrary finite computation.

## Source inspections

- arXiv:2609.20346v1, Bera–Sequeira, Lévy measures for Dirichlet-type spaces on the unit bidisc: complete 10-page primary preprint, including Question 1.3, Theorem 1.4, Theorem 2.4 and proof. Finding: Explicit defining-measure formula is only for h=1; Theorem 2.4 gives the abstract all-vector face decomposition.
- Santu Bera, New York J. Math. 32 (2026), 99–117: abstract/source record plus the exact defect identity as quoted and used in both the audited package and the later primary preprint. Finding: Provides the Dirichlet model and polynomial defect identity, not the arbitrary-vector tomography theorem.

## Residual risks

- Older one-variable completely-hyperexpansive literature may contain equivalent trace-map language, but no source located in the targeted searches covered the bidisc all-vector tomography statement.

The assessment concerns the single final claim stated above. Existing reproducibility material is evidence only and is not treated as independent certification.
