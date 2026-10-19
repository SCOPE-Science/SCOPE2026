# Mathematical review: five-point Walsh Riesz conditioning

## Correctness — PASS

The claim quantifies over every \(d\ge4\), every five-element binary support \(A\), and every five-element frequency set \(B\). A universal spectral inequality shows that a \(5\times5\) sign matrix with Riesz ratio at most \(9/4\) must have determinant magnitude \(48\): trace of the Gram matrix is exactly \(25\), the variance/logarithm bound forces its determinant square above \(1024\), and determinant divisibility and Hadamard's upper bound leave only \(48\). Dependence of the five support positions forces a reduction to the order-eight Walsh table; complementary minors limit the determinant to \(32\). For independent support positions, the quotient character map reduces equality to the exact \(4\times4\) binary maximal-minor lemma. The included checker tests all \(1820\) binary four-subsets by two independent exact determinant routines and verifies that the only five maxima form the rooted translation orbit of the dual simplex. All optimal Gram matrices have spectrum \(\{9,4,4,4,4\}\), proving both sharpness and equality classification. Counting uses a surjective four-coordinate quotient and independent choices of lifts. The general result is not inferred from sample dimensions.

## Originality — PASS, with bibliographic risk

Ferguson, Mayeli, and Sothanaphan develop finite-group quantitative spectrality and prove broad existence and bounds, but do not give the five-point Walsh optimal ratio. Seberry and Mitrouli identify the classical \(5\times5\) D-optimal determinant and its order-eight non-embedding. Brent and Osborn tabulate the determinant-value spectrum of the order-sixteen Sylvester matrix; **their order-sixteen determinant-48 total of \(43{,}008\) is prior work**, not a new claim. Huckle and Kravvaritis discuss spectral properties of leading principal Sylvester submatrices, not the unrestricted support-frequency Riesz minimization in all dimensions. The newly asserted comparison is of *least Gram eigenvalue to greatest Gram eigenvalue* and the complete equality-locus in binary Fourier geometry, rather than a determinant census. Full access to Huckle and Kravvaritis was unavailable, and an older equivalent characterization could exist.

## Value — PASS

The Riesz ratio is a natural quantitative stability measure of exponential interpolation on finite abelian groups. The theorem gives an exact optimum, a sharp obstruction for affine-dependent five-point supports, and an explicit prescription for every optimal frequency choice in every binary ambient dimension. Maximizing determinant does not generally minimize spectral condition number; the nontrivial variance/determinant barrier makes that equivalence precise here. The cardinality formula gives a reproducible design count and recovers an existing small-dimension tabulation as a consistency check, not as its main value.

## Scope and limitations

The theorem is limited to unweighted five-point Walsh Fourier bases. The finite four-column lemma is exhaustively proved using a short standard-library checker, and the remaining dimension dependence is analytic. Publication overlap in uncatalogued historical matrix-design treatments remains a residual risk. No independent external mathematical audit or certification has been performed.

Self-review: passed. Independent audit: not yet performed.
