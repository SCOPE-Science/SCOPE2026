# Independent mathematical audit

## correctness

PASS

For the specified heavy-over-light inviscid normal mode, unit interface displacement gives upper/lower interface velocity potentials −Γ coth(kh)/k and +Γ coth(k(L−h))/k; the hydrostatic jump and tension give Γ²D=k(G−σk²). At fixed k, the coth addition formula writes D=(a+b)coth S+(at+b/t)/sinh S for S=kL and t=sinh(k(L−h))/sinh(kh). The minimum is unique because t decreases bijectively from infinity to zero and equality in AM–GM fixes t=√(b/a). The allocation formula, strict half/square-root-share bounds, monotonicity in S and equal-depth deficit follow from this equality (z coth z is strictly increasing). The optimized denominator is a positive mixture of coth S and coth(S/2). Each component's negative logarithmic derivative q=2kd/sinh(2kd) strictly decreases; differentiation of the weighted mean gives mean(q′) minus Var(q), with the derivative in log k, so the elasticity drops strictly from 2 to 1. Its crossing with the increasing capillary term gives the unique maximum in scalar k, with k_c/√3<k_*<k_c/√2. At this crossing, increasing L lowers the elasticity at fixed k and shifts the crossing to smaller k, while D_* decreases pointwise and the maximum growth increases. The bounds keep k_* away from zero in the L limits, giving the stated wavenumbers, growth constants and thickness offset from the exact formulas. This is not uniqueness of a horizontal propagation direction. Read the frozen verification notes and script; the reported finite tests are corroboration, not the proof. The decision uses the analytic check, not execution of the supplied script.

## originality

PASS

Pass the fixed-total-height free-interface joint optimization, not the classical dispersion law or its infinite-depth most unstable wavenumber. The closest inspected total-depth calculation optimizes a different wave observable in a different regime. Available evidence does not establish prior coverage of the joint theorem; priority remains provisional where primary text could not be read.

## value

PASS

The fixed-height geometry supplies a natural design constraint. The exact allocation and strict wavenumber bounds answer how to place the interface and which mode then grows fastest, without a two-dimensional numerical search. The uniqueness proof and finite-size trends supply information not contained in the standard deep-layer result. This value is for linear inviscid theory under the stated wall and allocation assumptions, not nonlinear or viscous prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
