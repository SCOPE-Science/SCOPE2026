# Self-review

## Correctness: PASS

The Euclidean projection has a unique radius determined by a strictly monotone scalar KKT equation. Differentiating on open active-set charts gives explicit scalar and vector Jacobian rows. The vector row is convex in the radius ratio, and its two endpoints reduce to a scalar row bound or a strictly concave one-variable maximum. Realizable active charts prove sharpness. Generic translated-segment integration establishes the global bound without treating finite experiments as an infinite proof. A separate standard-library program replayed 164490 deterministic numerical assertions covering projection evaluations, smooth-chart derivatives, global-pair bounds and limiting extremizers.

## Originality: PASS within inspected evidence

The original 2014 full preprint defines the extended Lorentz cone but classifies isotone projection sets relative to its order, not the sharp \(\ell^\infty\) modulus of Euclidean projection onto the cone. The 2015/2016 cylinder article also studies projection onto a cylinder; the 2016 paper on cone-positive linear operators gives conditions for linear maps rather than a nonlinear projector modulus. Existing single-scalar Lorentz-cone constants, and planar or ball-projection stability findings, do not imply the multi-scalar sharp phase boundary. Searches did not reveal stronger coverage; this is not proof of priority, and related terminology remains a residual risk.

## Value: PASS

The extended Lorentz cones form an established and geometrically natural bridge from polyhedral constraints to second-order conic geometry. Coordinate maximum error is important when no coordinate may deviate excessively despite Euclidean nonexpansivity. The exact modulus solves all positive integer dimension pairs and identifies which class of output coordinate drives worst-case amplification; the crossover grows like the square root of vector dimension. The result is not an arbitrary parameter slice or a renamed standard inequality.

## Scope of review

The proof was checked for definitions, domain, chart boundaries, and all dimension quantifiers. Numeric checks only support the finite sample, and no assertion of third-party scrutiny or historical certification is made.

Self-review: passed. Independent audit: not yet performed.
