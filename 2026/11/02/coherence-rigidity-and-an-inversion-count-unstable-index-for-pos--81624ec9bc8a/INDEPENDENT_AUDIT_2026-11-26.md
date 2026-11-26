# Independent mathematical audit

## correctness

PASS

With C=B^{-1}, a positive fixed point obeys CHC=H-H^2. The right side is positive semidefinite and has the same rank as H, excluding eigenvalue 1; its range is then ran(H). The left side has range C ran(H), so C preserves the support and its orthogonal complement. On the support, H^(1/2) C H^(1/2) is the unique positive square root of H^2(I-H), so C=(I-H)^(1/2) there. This gives exactly the projector classification and its Grassmannian components, and substitution proves sufficiency. The differentiated map on a joint eigenbasis is diagonal on the real Hermitian matrix-unit basis: one real direction per diagonal entry and two per off-diagonal pair. With selected and omitted gains all in (1,3), the omitted block contributes m^2 expanding dimensions, mixed pairs have multiplier sqrt(a_omitted/a_selected), and selected-selected multipliers (a+b-ab)/sqrt(ab) decrease in either gain from the limiting value +1 at (1,1) to -1 at (3,3). Simplicity excludes a mixed unit multiplier. For the general candidate sink, omitted gains below 1 are strictly contracting in both omitted-omitted and mixed modes, including repeated gains. Omitting any gain above 1 gives an expanding diagonal mode; gain 1 forces +1, and gain at least 3 gives either an omitted expanding mode or an active multiplier at most -1. This proves the full local, hyperbolic criterion, not global convergence or stability at neutral gains. The extra bound B^2<=4I is only needed for invariance of the interval.

## originality

PASS

The strongest verified comparison is a later-dated Resultary record on the forward-invariant domain with the same commutation, Grassmannian classification, linearization and sink boundary. It does not state the full simple-spectrum inversion census, and its domain for the classification is narrower. The inspected primary coupled-map paper sets up the larger matrix map and studies spectral/chaotic dynamics, not the exact positive fixed-point classification and all-real-directions unstable census. The scientific case rests on that combined classification and census, not on claiming novelty for the scalar fixed point, the positive-square-root equation, or linearization methods. This is a bounded best-of-knowledge decision, not a priority certification.

## value

PASS

Although the dynamics allows states that do not commute with B, every positive equilibrium commutes with B, and the theorem classifies them even on rank-deficient supports. Counting all real modes gives information invisible to the scalar or diagonal model: for two ordered gains in (1,3), selecting only the smaller gain gives index 3, while selecting only the larger gives index 1. The classification and exact local criterion thus resolve a natural stability question, without extrapolating to basins or chaotic dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
