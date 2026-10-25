# Independent mathematical audit

## correctness

PASS

The exact quartic equilibrium reduction P(x,r) uses y=5x/D and z=x(r+x)/D, D=2x²+rx+5-r², valid with D>29/10 on the critical rectangle. I independently recomputed disc_x P=12000 H(r) and P(0,r)=(r²−5)(2r²−5r−10). Four real discriminant roots are near −2.011934533, −1.308660544, 2.188758627 and 3.355161061; negative fold r_f≈−1.30866054409147 and transcritical r_t=(5−√105)/4≈−1.31173769148990 have gap ≈0.00307714739843. Exact rational Sturm and the proof’s uniform P_xx>12, P_r>28, endpoint positivity show two and only two positive x roots for r_t<r<r_f, with no extra real roots by root-count continuity. The equilibrium Jacobian satisfies det(J)=−x P_x/D on P=0, independently checked symbolically modulo P; its trace −8, principal-minor a2>12 and |a3|<7 give a sink at x_+ and one-unstable saddle at x_−. The origin polynomial and Routh–Hurwitz prove sink until r_t; nonzero x branch crosses the origin transversally at r_t. The global Lyapunov family V_u=1/2(ux²+y²+(2−u)z²), whose quadratic nonlinear derivative cancels, has negativity condition Phi(u,r)<1; strict convex minimization and resultant r^4 H(r) identify the same r_f as its exact negative threshold. A strict negative definite weighted symmetric linear part proves global exponential attraction for r_f<r≤0, not merely local stability. Verification script’s rational Sturm/inequality assertions were materially inspected; finite numerical eigenvalues were not used for interval proofs.

## originality

PASS

Best-of-knowledge originality PASS restricted to the exact negative-parameter coexistence window, its three equilibrium indices, generic bifurcation endpoints, and sharp origin stability; the original 2026 ETM-3D paper studied nonnegative parameters and a prior published mathematical result proves the positive first saddle-node threshold using the same H. The polynomial and energy cancellation are not credited as new. Opposite signs of r produce genuinely different root order and origin spectral sign; the published positive-half claim neither states nor mechanically yields the negative two-sink interval. Potential unindexed negative-domain analysis remains a priority risk.

## value

PASS

An exact, narrow negative parameter interval with two coexisting hyperbolic sinks in a named quadratic dynamical system is a genuine stability/bifurcation boundary, not merely a restated discriminant root: the proof certifies both sink indices, a saddle separating branches, transcritical/fold transitions, and a global origin-attraction frontier. These precise constraints matter for multistability and parameter selection. It does not claim global basin topology or absence of additional recurrent attractors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
