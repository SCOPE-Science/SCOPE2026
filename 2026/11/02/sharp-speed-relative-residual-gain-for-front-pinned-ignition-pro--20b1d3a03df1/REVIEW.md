# Self-review

## Correctness — PASS

The statement concerns the unique entire heteroclinic of the explicitly defined scalar ignition equation, not numerical iterates. Direct differentiation verifies the time function and the homogeneous velocity solution; variation of constants yields the exact Green map, with \(\varepsilon\equiv1\) realizing its norm. On the left of the pin the derivative of the root-gap function is strictly positive and nonintegrable at zero, giving one and only one maximum. On the right, monotonic velocity gives a strict logarithmic bound below the left limiting gain. For growing reaction order, a rescaling of the root equation converges locally to a strictly decreasing function with one zero; bracketing proves the location and gain limits without relying on finite sampling. The unweighted comparison is explicitly a lower-bound asymptotic, not a claimed sharp operator norm. The independent standard-library checker passed 3,139 supplementary tests.

## Originality — PASS, with priority risk

The directly inspected source is Boros, arXiv:2610.27864v1, especially Proposition 4.1, Theorem 4.2, the discrete translation-mode lemma, and its statements about unweighted residual growth. It proves \(P(t,s)=G_q(y(t))/G_q(y(s))\) and proposes the maximizing-velocity pin. It does not optimize the speed-relative forcing-to-response norm, identify the unique worst state before the pin, or derive the high-reaction-order constant. These are derived by an additional exact global extremum calculation and a large-order limiting root theorem, rather than being presented as independent new propagator formulas. A published mathematical-record index returned related projection, PINN weighting, and spectral stability results but no directly covering profile-specific formula. Tee–Trefethen concerns mapped interpolation, and Du concerns integral-preconditioned matrix conditioning; only their summaries were available, so whole-document absence is not claimed. An unlocated older sharp Green-operator estimate remains a genuine historical risk.

## Mathematical value — PASS

Boros explicitly leaves a residual-forcing growth caveat even after pinning. The theorem identifies one natural residual normalization for which the continuous inverse has a sharp \(q\)-dependent bound independent of the small ignition-layer parameter, plus the unique state at which the error is most amplified. The limiting constant and shift locate the critical error-sensitivity region at high reaction order, supplying a quantitative criterion for weighted-residual tolerances and a reproducible benchmark for continuous versus discrete conditioning. The theorem neither certifies numerical Jacobians nor removes the need to control near-equilibrium weights; it is an exact invariant, not a solver-wide guarantee.

## Related literature and limitations

- Boros, *Front-pinned spectral collocation for the flame problem and related ignition problems*, arXiv:2610.27864v1, §2, §4, §5, §6, read in full HTML.
- Tee and Trefethen, *A rational spectral collocation method with adaptively transformed Chebyshev grid points*, SIAM J. Sci. Comput. 28 (2006), publisher abstract and bibliographic metadata (not full text).
- Du, *On well-conditioned spectral collocation and spectral methods by the integral reformulation*, SIAM J. Sci. Comput. 38 (2016), publisher abstract and bibliographic metadata (not full text).

Correctness was assessed internally and supported by an analytic proof and a reproducible numerical checker; there has been no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
