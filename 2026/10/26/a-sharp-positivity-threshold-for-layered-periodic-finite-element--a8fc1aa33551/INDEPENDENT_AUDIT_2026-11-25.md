# Independent mathematical audit

## correctness

PASS

The local consistent mass and stiffness contributions give normalized diagonal d=1−x−y and alternating neighbor entries x=1/6−σa and y=1/6−σb, σ=τ/ℓ². For nonnegative time, d−(|x|+|y|)=1−2(max(x,0)+max(y,0))≥1/3. Above or at the cutoff both off-diagonals are nonpositive, giving an inverse-positive A by a Neumann series; at zero the step is identity. Below cutoff relabel so a≤b, hence x>0. Even/odd Schur inversion gives R=(uI−xy(S+S⁻¹))⁻¹, u=d²−x²−y². Multiplication by the actual consistent mass gives the stated EE and EO expressions. If y=0 the EE neighbor is −x/(6u); if y>0 the recurrence gives 6(P_EE)₀₁=(Q−x)R₀+(Q−y)R₂. Both coefficients are strictly negative by the two positive-coefficient expansions in p=σa,q=σb and R is strictly positive. The equal-coefficient point x=y=0 is at the cutoff, not in this subthreshold case. For y=−Y<0, periodizing the infinite resolvent with geometric ratio −r yields the stated cyclic formula, verified by the recurrence and the unit jump at k=0. It gives R₁<0, R₂=R₁ for m=3, and 0≤R₂/|R₁|≤2xY/u<1/5 for m≥4: the even formula is bounded by 2r/(1+r²), and the odd m≥5 ratio is less than r. Since the driver ratio (a+5b)/(5a+b)<5, the indicated EO entry is strictly negative. The bound u−10xY=(1−2x)+(2−12x)Y>0 holds because 0<x<1/6. As an exact exception at N=4, direct multiplication of the full proposed propagator by M+K/8 recovers M, with least entry 9/4004. The calculation and sign-polynomial checks replay with `python /workspace/independent_reproduction.py`; the frozen verify.py was inspected, not executed. The all-size result rests on the analytic resolvent argument.

## originality

PASS

Credit the M-matrix sufficient direction and the covered homogeneous special case. The independently supported distinction is necessity for periodically alternating diffusivities on equal cells for all even N≥6; neither the exact alternating-length examples nor the inspected general sufficient criteria give this. Date order within the same day was not inferred.

## value

PASS

On a canonical periodic two-material mesh, a sufficient inverse-positive matrix criterion is shown to be exactly necessary for every even size at least six, regardless of contrast. The small-size exception proves the geometry cannot be dismissed and the mixed-sign proof identifies a negative propagator entry precisely in the regime where inspecting matrix signs alone is insufficient. This is a usable timestep boundary for the stated discretization, not an arbitrary isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
