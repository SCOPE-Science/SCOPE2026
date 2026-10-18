# Independent mathematical audit

## correctness

PASS

Reconstructed the self-adjoint positive covariance operator T_p(C)=Σ p_i P_i C P_i, its PSD Gram nonzero spectrum, Perron nonnegative top eigenmatrix and the Rayleigh lower bound Γ(p)>=(1+||Σp_i z_i||²)/2. For r=0 isotropic moment identity yields exact 2^-k for every e0; for r>0 unique occupied semicircle endpoints split 1/2 achieve (1+r²)/2 and characterize all minimizers (up to duplicate rows). Exact-rational two-row covariance propagation checked 3 initial vectors over 10 steps, factor 17/25 for r=3/5. Does not assert quenched or adaptive rates.

## originality

PASS

Strohmer–Vershynin provide classical exponential expected convergence; Dai–Soltanalian–Pelckmans optimize the one-step eigenvalue upper bound; Agaskar–Wang–Lu establish exact lifted MSE operator and convex SDP for the annealed rate. Their inspected full text does not give the closed planar value, equality of optimizer sets, zero-distance all-time law, or complete positive-distance support classification. These are not automatic consequences of an SDP existence theorem; the new doubled-angle geometry and sharp Rayleigh equality provide the missing explicit optimization.

## value

PASS

Selecting optimal sampling probabilities for linear solvers is a canonical optimization problem. This exact characterization replaces a general SDP by a planar convex-hull construction and distinguishes the optimized exact annealed factor (1+r²)/2 from the previously optimized one-step bound (1+r)/2; both zero-distance and short-arc cases have meaningful different finite-time behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
