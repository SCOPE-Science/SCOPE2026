# Scientific review: sharp grazing ellipse and optimal drive balance

## Correctness — PASS

The precise domain is the four-state Matsuoka ReLU ODE at \(c=\sqrt{a_{12}a_{21}}=1+\tau_x/\tau_y<1+b\), with all positive parameters and fixed couplings and first drive. Substitution in the full-active affine vector field gives an exact invariant center plane and \(\ddot v+\omega^2v=0\). The closed firing conditions reduce to the sharp harmonic-amplitude cap \(K\rho\le\min(p,q/\sigma)\), including the tangential equality case. The full-active Jacobian's complementary eigendirections have negative real parts, excluding other nonconstant periodic orbits confined to this cell. Exact Jacobian integration supplies the projected area; an elementary monotonicity comparison proves the unique optimal input \(r=\sigma\). The included symbolic checker verifies the identities and a fully rational test family, including the ODE at threshold. The general theorem is analytical, not inferred from samples.

## Originality — PASS, with stated priority uncertainty

Muramatsu–Kori arXiv:2405.08409v1, Sections IV.4, V.2, VI and its appendix, already provide the fully active equilibrium, the center threshold and center plane, plus the **qualitative** outermost grazing orbit. Their result is credited; the proposed claim does not re-present the existence of a center as new. The inspected full primary text does not furnish the sharp input-dependent area profile, the classification of all active-cell periodic states, the unique input-ratio optimum, or the double-grazing mechanism at that optimum. Matsuoka (2011) announces approximate period/amplitude relations in the accessible abstract, but the full 2011 paper could not be inspected, leaving genuine priority risk. The inspected 2005 abstract and excerpts concern LMI regions for transversely switching attracting limit cycles, rather than a neutral center family entirely within one firing cell; the full 2005 article was not systematically inspected. No exact equivalent emerged from targeted published mathematical-literature comparisons. Absence from a search is not proof of unique historical priority.

## Value — PASS

The exact size of the neutral periodic island determines a natural quantitative boundary between purely active oscillations and threshold-contact dynamics at a discontinuity-induced bifurcation. For fixed synaptic and adaptation parameters, the theorem identifies the unique tonic-input balance that maximizes that island, with a cusp in the area profile, quadratic area collapse at both feasible-input boundaries, and a simultaneous contact of the two firing thresholds. These are exact measurable aspects of the model's critical regime beyond the previously reported eigenvalue criterion or approximate period, without requiring any downstream theorem.

## Limitations and closest literature

The strongest relevant predecessor is Muramatsu and Kori, arXiv:2405.08409v1, which already contains the center plane and the qualitative outermost grazing picture. Full published priority against Matsuoka (2011) remains unresolved because only its abstract was available. The claim applies only at critical coupling to trajectories permanently in the closed active firing region; it does not classify switching limit cycles or noise response, and it optimizes at fixed first drive rather than fixed total drive. The ordinary planar area is explicitly tied to the \((x_1,y_1)\) coordinates, with an intrinsic-area conversion supplied.

Self-review: passed. Independent audit: not yet performed.
