# Independent mathematical audit

## correctness

PASS

In the shifted problem write Δ=uvᵀ with u unit and v=pu+qJu. The trace/determinant conditions are independently recovered as p≤−2α and α²+b²+αp−bq≥0; every pair (p,q) is realizable and its norm is √(p²+q²). Thus the problem is projection of zero onto two half-planes. At b=0 the determinant is at most −α² in the trace-feasible region. For 0<b<α the feasible coordinates obey p≤−2α and q≤(b²−α²)/b<0, both closest-to-zero bounds attained together, giving (α²+b²)/b and forcing nonsymmetry. Both invariants then vanish and C is nonzero (entry b in the (u,Ju) basis), so C²=0 and C is defective. For b≥α the closest trace-feasible point is (−2α,0), with determinant b²−α², giving exactly the symmetric minimizers and nilpotent/imaginary boundary cases. Unrestricted trace–Frobenius equality forces −α I. For passive Δ the invariants give precisely the stated interval and its strict interior; above the upper endpoint the margin fails (actual zero-margin instability at the shifted threshold only when δ=0). Arbitrary rank-one strict feasibility for b>0 follows by lowering p by ε and q by more than αε/b; strict unrestricted feasibility follows by increasing the scalar correction. Trace equality is necessary at each finite closed optimum, proving nonattainment and giving the strict infima; b=0 remains infeasible. The frozen exact-arithmetic checker and recorded assertions were inspected, not executed. Separate reproduction `python3 /workspace/checks/frozen_math_checks.py 1` passed for sampled trace/determinant coordinates, nilpotent endpoints and overdamping. The analytic half-plane argument, not sampling, establishes the complete profile.

## originality

PASS

The general minimum-Frobenius stabilization objective and standard 2×2 eigenvalue and determinant tools are established. The supported distinct result is the exact fixed-rank cost and full optimizer/passive/strict classification for the real rotation–dilation model. No inspected prior statement covers that profile mechanically; the most plausible inaccessible source is explicitly noted.

## value

PASS

A sharp distance and minimizer classification for the basic rotating unstable mode is a useful low-rank nearness benchmark. It quantifies the rank penalty, which diverges as rotation vanishes despite a fixed unrestricted cost, and distinguishes a fragile defective optimum from passive feasibility and its upper amplitude cutoff. This is not a higher-dimensional or fixed-actuator stabilization theorem, nor a robustness guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
