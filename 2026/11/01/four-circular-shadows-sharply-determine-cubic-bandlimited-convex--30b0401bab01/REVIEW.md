# Scientific review: four circular shadows and cubic support functions

## Correctness — PASS

The proof uses the restriction identity for support functions under orthogonal projection and the unique degree-0–3 spherical-harmonic decomposition. Three coordinate disks kill all five trace-free quadratic coefficients, and the third-angular-mode condition on the cubic leaves precisely the harmonic monomial \(u_1u_2u_3\). The fourth-plane frame gives the exact \(\sin(3\theta)/(3\sqrt6)\) coefficient. The signed body-diagonal normals prove the optimal nearest-ball Hausdorff residual and uniqueness. For the sharp three-view lower bound, seven-dimensional harmonic cubics face at most six independent linear tests, and small perturbations preserve strict convexity. Every assertion holds for all specified parameters, not only finite samples. The standalone `verify.py` passed the rational ranks (6, 9, 10), 720 deterministic trigonometric checks, eight extremizers, and the residual factor.

## Originality — PASS (qualified by historical priority risk)

Myroshnychenko–Ryabogin–Saroglou (arXiv:2609.27192v1, Theorems 1.2–1.4 and Proposition 5.1) prove all-direction rotational projection rigidity and supply the cubic threefold-symmetry exception; they do not state the finite four-disk tomography theorem. The indexed *Sharp convexity threshold for the cubic constant-width support family* determines an allowable amplitude, not finite-view identification. The especially close indexed *Exact brightness profile of the cubic threefold-projection exception* calculates projected areas for one fixed cubic family and already identifies its three coordinate circular shadows and body-diagonal area minimum; **those observations are prior work**. Its indexed statement neither classifies all degree-three supports with three circular projections nor establishes the universal three-plane obstruction or the exact nearest-ball stability constant. Goodey–Schneider–Weil (1997) study global projection size data, not four full projection shapes. Actual source text/abstract and indexed summaries were compared by logical implication. Full contents of the two indexed technical records and Kuz'minykh (1973) were not accessible, so an equivalent unpublished/unindexed result cannot be excluded.

## Mathematical value — PASS

This is a natural finite-view inverse problem: it establishes the optimal number of complete circular-shadow measurements in a nontrivial convex-harmonic bandlimit, completely identifies the invisible cubic degree of freedom after three optimally placed views, and gives an exact measurable harmonic residual equal to the global distance to the nearest ball. The sharp any-three-plane impossibility shows the four-view threshold is structural, not an arbitrary isolated calculation. The finite-degree hypothesis is necessary and clearly stated.

## Limits

No unrestricted-body result; no all-four-view perturbative stability assertion; no assertion that an arbitrary set of four planes suffices. Experimental checks do not replace the analytic proof. Some older primary texts were inaccessible. Scientific attribution remains subject to independent literature review.

Self-review: passed. Independent audit: not yet performed.
