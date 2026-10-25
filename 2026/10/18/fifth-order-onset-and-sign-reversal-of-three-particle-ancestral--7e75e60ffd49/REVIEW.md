# Independent mathematical audit

## correctness

PASS

The 10-state population-count process has transitions c->c-e_i+e_j at c_i+c_ic_j k_i/(N-1), while a distinguished founder has an 18-state linear harmonic generator incorporating movement, killed founder loss, and uniform-parent copying. Fixing total stationary mass 1 and the same-site identical-founder anchor h(0,(2,0,0))=1/3 makes both augmented matrices invertible near epsilon=0. Expanding these finite matrices as L0+epsilon L1,T0+epsilon T1 gives the exact rational recurrence L0^T pi_r=-L1^T pi_(r-1), T0 h_r=-T1 h_(r-1) and a convolution for F_02-F_20. Independently reconstructed all event entries, rational matrix inverses and residual equations using SymPy; obtained coefficients r=0..7 exactly [0,0,0,0,0,89/56010528,0,-410017/1524382530048]. The N=3 fifth term is positive, while site reflection sends epsilon to -epsilon and current to its negative, giving odd analyticity and the O(epsilon^7) remainder. The N>=4 negative cubic is explicitly attributed to Lin–Lu, not re-proved by the N=3 computation; its N=4 numerical coefficient is stated in the source. No finite-epsilon uniform sign interval or large-N interchange claimed.

## originality

PASS

The underlying three-site Fleming–Viot model, generic N>=3 circulation and negative cubic behavior at N>=4 are Lin–Lu prior results. The exact exceptional N=3 cancellation through cubic and nonzero quintic coefficient are a different finite-size invariant; exact coefficient keyword and semantic source searches found no stated duplicate, but Lin–Lu entire updated preprint was inaccessible in this run and its Appendix A/B coverage is an explicit significant risk.

## value

PASS

The minimal possible circulating population is a natural boundary where a known factor N-3 cancels the leading general cubic. Resolving whether current vanishes identically or first appears later, and determining its opposite direction, is motivated finite-dimensional exact mathematics independent of any new large-population theorem. Rational 89/56010528 has concrete dynamical sign content, not an arbitrary small numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
