# Scientific review: The moment triangle of Euclidean parallelograms

## Correctness — PASS

The two independent uniform coordinate differences have the exact triangular law. Expanding the squared Euclidean distance gives the three moment identities in RESULT.md. The normalized Gram conditions are necessary and sufficient for positive-area planar parallelograms. Their affine image has nonzero determinant and gives the moment triangle, inverse formula, complete sharp two-moment nonuniqueness and Hölder stability. The verifier supplied in this package passed 7,449 rational checks and independent numerical sampling; the universal conclusions are proved analytically, not inferred from experiments.

## Originality — PASS, with qualifications

Averkov–Bianchi (first preprint 2007; journal 2009) prove injectivity from a complete direction-labelled covariogram, not from three scalar moments. Gasparyan–Ohanyan (2014) give forward covariogram and invariant-line chord distributions for parallelograms. Martirosyan (2023) computes direction-dependent chord laws for arbitrary quadrilaterals. Two nearby public mathematical results address a boundary-to-interior *fourth*-moment ratio and recovery from *projection-width* statistics. Their statements were checked against the new inverse and do not subsume it. Historical priority still carries a risk from unindexed finite-moment work; literature-search noncoverage is not used as a proof of novelty.

## Mathematical value — PASS

The new claim is a complete inverse and feasibility classification for three natural orientation-free scalar distance statistics. It identifies the exact minimal consecutive-even-moment cutoff, an explicit continuum of ambiguous shapes below it, and a sharp feasible normalized-moment triangle with boundary strata corresponding to rectangles, rhombi and degenerate limits. This is more than merely tabulating moments; it gives an executable geometric reconstruction and a precise determination of all possible observed moment pairs.

## Limitations and reproducibility

Only positive-area Euclidean parallelograms with independent area-uniform endpoints are treated. Sampling-error rates are not proved, and inverse stability deteriorates at geometric degeneracy. `verify.py` uses only the Python standard library. The same-scientific-review check does not replace expert or independent validation.

Self-review: passed. Independent audit: not yet performed.
