# Independent mathematical audit

## correctness

PASS

The positive equilibrium equations imply trace k−v² and determinant (F+k)(v²−F). Zero trace and positive determinant give s=v=√k, F s=(F+k)², and exactly the stated open arc t=F/k. I checked the physical-time coefficient independently using a scalar oscillator, rather than the source's complex quadratic homological calculation. With s the equilibrium v at the actual parameters, c=F+k and X=s−s²/v, elimination of u gives X''=(k−v²)X'+s²F−cF(s−X)−cs²v, with v=s/(1−X/s). At Hopf the quadratic/cubic force terms are −csX²−cX³; the corresponding damping terms are (−2sX−3X²)X'. In time-angle θ the leading radius term is a cos θ; its second-order constant/cos 2θ/sin 2θ corrections are h0=−cs/(2ω²), hc=cs/(6ω²), hs=−s/(3ω). The cubic cos θ force is a³[−2cs(h0+hc/2)−3c/4−sωhs]. Dividing the bracket by 2ω² gives the relative period coefficient, the claimed C(t). The change X=v−s+O((v−s)²) preserves the first-harmonic amplitude to leading order. To justify the detuned limit on any shrinking cycle, a smooth time-preserving linear and quadratic normalization gives an angular speed bounded away from zero and log radial derivative σ+O(ρ²). The simple orbit winds once; integrating log radius gives σ=O(max ρ²), and the radius varies relatively by O(max ρ²) per turn. Thus the linear stiffness in the scalar oscillator differs from ω_lin² only by σ²=O(a⁴); the detuned linear damping is quadrature, not an order-a³ in-phase contribution. Off-arc coefficient changes are o(1), and the quadratic corrections have no first harmonic. This argument does not divide by the real cubic coefficient and remains valid at t=1/3. Ordinary cycles exist near t≠1/3 (σ_F at fixed k is −1/t and the radial cubic in the source is nonzero there); cycles tending to t=1/3 also follow by choosing arbitrarily small ordinary cycles as neighboring Hopf points approach it, consistently with the established Bautin result. The derivative has sign opposite to the strictly decreasing quartic P on (0,1); P(0)=10, P(1)=−80 and both endpoints of C diverge. The bounded independent replay `python3 /workspace/review_checks.py 2` checks the algebra and yields t*=0.300154330325167455… and C(t*)=15.796641246067701232…, and C(1/3)=16 exactly. None of the frozen scripts was executed; shooting at two t values is optional corroboration only.

## originality

PASS

The supported distinction is the physical-time, same-parameter linear comparison with the measured v harmonic for arbitrary shrinking cycles in this model, and its full-arc sharp optimum. The Hopf and Bautin locations and the general normal-form machinery are not new. Inaccessible historical material is an unresolved priority risk, not evidence of absence.

## value

PASS

The frequency relevant to a real homogeneous oscillator is its physical-time frequency, not the unit angular speed of an orbital normal form. Calibrating it against the nearby focus and using a measurable first harmonic separates parameter detuning from nonlinear period softening. The exact sign and sharp quantitative minimum across the curve, including nonzero softening through a radial stability switch, answer a coherent comparison question beyond bifurcation existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
