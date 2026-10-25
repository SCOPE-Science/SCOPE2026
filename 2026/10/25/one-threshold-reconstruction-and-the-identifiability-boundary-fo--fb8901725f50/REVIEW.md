# Review of the one-threshold ellipsoid section-radius reconstruction theorem

## Correctness — PASS
The single principal claim is the complete identifiability dichotomy and sharp one-threshold range for the largest central-section radius of a three-dimensional ellipsoid. With \(a>b\), Courant--Fischer interlacing gives the exact support \([b,a]\), and the normal-plane cone criterion
\[
 n_1^2\ge\alpha(n_2^2/\beta+n_3^2/\gamma)
\]
is derived directly from weighted Cauchy--Schwarz, rather than assumed from simulation. Haar coordinates make \(|n_1|\) uniform and the transverse azimuth independent, producing the exact integral. The integrand increases strictly with the smallest semiaxis on a set of positive measure, so the one-value inversion holds for all \(0<c\le b\). Evaluating both extreme parameter limits proves sharpness and the nonattainment assertion. Endpoint Taylor expansion and dominated convergence establish the elliptic-integral statistic and its strict inversion. If \(a=b\), every plane intersects the top two-eigenspace, proving the point-mass obstruction without exceptional cases.

The independently implemented eigenvalue-compression checker recomputes each sampled section radius, verifies the cone inequality for 90,000 orientations at five thresholds, integrates the predicted CDF numerically, and tests parameter monotonicity and the endpoint coefficient. These are finite checks, supplemental to the universally quantified analytic argument. Unproved limits include finite-sample robustness and higher-dimensional analogues.

## Originality — PASS under available source comparison
The strongest nearby earlier work is Cuenca's arXiv:1807.06134 on orbital orthogonal beta processes, which already incorporates the **complete joint forward distribution of compressed eigenvalues**. Its forward-law coverage is explicitly conceded and is not sold as new. The narrower asserted advance is the complete sharp *inverse* characterization: the two support endpoints plus one unlabeled diameter probability recover the third semiaxis exactly when the top eigenvalue is simple, with optimal range and complete failure when that eigenvalue has multiplicity two. The shape-identifiability and order/rigidity implications are not stated by the compared random-matrix source.

Guedon--Litvak--Tatarko--Vritsiou arXiv:2609.24131 is the recent motivating source. Its random section diameter bounds, including \(p\)-ellipsoids, do not state a three-dimensional one-threshold inverse or the top-axis failure classification. Prior work reconstructing axes from central-section **volume moments** requires different observations. The 2014 random-field stereology paper uses randomly positioned sections and filamentarity information, unlike the center-conditioned diameter statistic here. Query and implication comparisons with published mathematical research records found no exact covering inverse classification. Searches cannot prove absolute historical novelty. Residual risk: earlier stereology of ellipsoid major-section axes or random compression eigenvalues could contain an equivalent inverse argument.

## Mathematical value — PASS
This is a natural, exact inverse problem in geometric stereology: how much of a three-dimensional object's geometry can be recovered when each randomly oriented two-dimensional central section supplies only its largest axis and its orientation is discarded? The dichotomy gives a full answer for all positive ellipsoid semiaxes, an unexpectedly small sufficient dataset (two support endpoints and one CDF value), rigorous sharp error-free envelopes, and the precise nonidentifiability family. Unlike a routine recomputation of a classical distribution, the extremal envelope and reconstruction criterion distinguish information-bearing and information-losing parameter regimes. These facts supply exact geometric benchmarks for stochastic section inference even though no estimator for finite samples is proved.

## Closest references, scope and residual uncertainty
- Guedon, Litvak, Tatarko, Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131, September 21, 2026: high-dimensional random-section inequalities; not an inverse one-CDF theorem.
- Cuenca, *Universal behavior of the corners of orbital beta processes*, arXiv:1807.06134, 2018, Section 1.2--1.3: established general forward orthogonal-compression joint eigenvalue densities, so the forward integral must not be mistaken for an independent discovery.
- Makarenko, Fletcher, Shukurov, *3D morphology of a random field from its 2D cross-section*, arXiv:1407.4048, 2014: inverse morphology from different section sampling and morphology observables.
- Published research records on exact random radius laws of one-spike ellipsoids and ellipsoid inverse square section-volume moments: different distributional regimes and/or observables, not the strict-top-axis three-dimensional diameter one-threshold theorem.

Self-review: passed. Independent audit: not yet performed.
