# Independent mathematical audit

## correctness

PASS

For repaired claim, thin QR gives F=ER⁻¹ with QᵀF=0 and ‖EA†‖=‖F‖. The normal equations give displacement −Tu+Kr with T=FᵀF(I+FᵀF)⁻¹ and KKᵀ=T−T². For unit z, putting a=‖Tz‖ bounds the dual pairing by ‖u‖[a+ρ√(a−a²)], since zᵀTz≤a and a≤δ²/(1+δ²). Scalar concavity gives the interior optimum a*=(1+1/√(1+ρ²))/2 for ρ>0 and the cap for ρ=0. F=−s wvᵀ with v=u/‖u‖ and w in the old orthogonal complement aligned with r (arbitrary if r=0) attains the bound. It is rank one for positive budgets and zero for zero budget; the retained assumptions ensure w exists. Independent exact replay: A=(1,0)ᵀ, b=(1,ρ)ᵀ and E=(0,−s)ᵀ give x̂=(1−ρs)/(1+s²), hence the stated normalized displacement. At ρ=1 and δ=3 the maximizer has s=1+√2<3 and gives (1+√2)/2, larger than the value 6/5 at s=3. The rewritten script distinguishes 6×7 positive-budget and 6 zero-budget scalar checks; supplied code was inspected, not executed. No computation is needed for the upper bound, attainment, or correction.

## originality

PASS

The surviving distinct claim is the fixed-data, dimension-free attained envelope including finite saturation and positive-budget rank-one attainment. Known residual-sensitive perturbation bounds and sharp sketching envelopes inspected do not materially cover it. The zero-budget correction is elementary, not a novelty claim.

## value

PASS

This natural orthogonal error geometry isolates loss of the original prediction from coefficient conditioning. Knowing the sharp envelope distinguishes quadratic sensitivity for consistent data from linear small-error sensitivity and finite saturation for inconsistent data. Attainment for each fixed data set makes the plateau a worst-case phenomenon, not just looseness in a bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
