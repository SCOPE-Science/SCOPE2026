# Scientific review: rotated symmetric saddle switching

## Correctness — PASS

For the explicitly defined two-by-two symmetric saddle pair, the exponential formula and the identity \(\operatorname{tr}(HK)=2\cos(2\theta)\) determine the positive Floquet spectrum without approximation. The resulting condition \(\cos^2\theta\cosh(pT)+\sin^2\theta\cosh(p\Delta)<\cosh(aT)\) is necessary and sufficient. A strict weighted-power-mean argument proves that at each fixed duty fraction the stability deficit changes sign at most once, and that this crossing exists precisely for a Hurwitz average. Direct scalar inequalities establish the angular cutoff and exact duty window. Series and implicit-function expansions establish the nonzero square-root and logarithmic boundary laws. The proof covers \(0<a<p\), positive dwell times, all axis angles in \([0,\pi/2]\), and equality cases. The separately implemented numerical computation is a consistency check, not an infinite proof.

## Originality — PASS, with historical-priority limitations

The complete primary text of Xiedeng, Celli and Porfiri (2026) treats a different, companion-form mechanical model: its two-saddle non-stabilization applies within that restricted class, while its stable antiresonance windows require a saddle combined with an unstable focus or node. The present matrices are *symmetric* and rotate their unstable axes; stability here requires a stable average and admits no isolated intermediate-period stability windows. Gökçek (2004) gives the general Floquet criterion and fast-switching sufficiency. Hou, Wang and Xie (2021) give a hyperbolic criterion for a switched cooperative pair with individually stable matrices. Tripathi and Agarwal (2021) study planar pairs with Hurwitz modes. General matrix-product inequalities already imply related qualitative monotonicity, so that principle is not claimed as new. The assessed, more specific contribution is the **full exact angle–period–duty boundary and singular tolerance laws** for the canonical two-unstable-mode symmetric pair. A full copy of the Gökçek paper was not retrieved and older specialized coverage remains a priority risk; neither a search miss nor the different system names is treated as proof of novelty.

## Mathematical value — PASS

The question is a natural minimal two-dimensional inverse-stabilization design problem. Knowing only that rapid switching can stabilize a Hurwitz average does not specify the necessary rotation angle, the largest allowable physical period, the permissible duty imbalance, or whether disconnected stability tongues can occur. The theorem gives exact answers and sharp edge asymptotics, including a singular orthogonal limit where the finite cutoff disappears. It also makes precise why a saddle–saddle stabilization example does not contradict the mechanical companion-matrix obstruction. These constitute a complete, testable structural classification rather than an isolated parameter substitution.

## Limitations and closest literature

The calculation depends on equal eigenvalue spectra, symmetric saddle matrices, common scalar damping, and periodic two-state switching. It does not classify arbitrary planar linear switching, nonsymmetric oscillator companion matrices, or arbitrary switching sequences. The numerical program verifies 525 selected monodromy comparisons and representative boundary regimes, not all real parameters. The 2026 mechanical-oscillator paper is not asserted to be false or incomplete on its own stated class. The generic switched-systems and matrix-product literature should be rechecked independently for historical priority before publication.

Self-review: passed. Independent audit: not yet performed.
