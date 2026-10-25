# Independent mathematical audit

## correctness

PASS

Two explicit 11-vertex simple trees each have 10 distinct connected edges; markers all degree 1, distances (3,4,3), ambient neighbor degrees (2,4,3), and tree resistance R(u,v)=3. For each visited S and x in S, the finite absorbing Markov-system equation deg(x)F(S,x)−Σ_(y∈S∩N(x))F(S,y)=deg(x)+Σ_(y∉S∩N(x))F(S∪{y},y) uniquely determines exact rational cover time, including the start-visited convention. The supplied code solves this and an independent inclusion–exclusion hitting-time system. I independently reconstructed all 1023 nonempty hitting targets by direct Dirichlet solves for all four graphs: A cover ≈86.31575829848333→84.88662138536927 (negative), B ≈90.957934020003→90.9955742530426 (positive), agreeing with claimed exact rational signs −1162717427/813580152 and +3127/83076. Numeric reproduction supports rather than replaces exact rational finite-state certificate. No minimal order/all radii claim.

## originality

PASS

The motivating 2026 Si construction explicitly compared different graph orders for all radii, leaving its same-order question open; this constructs a valid equal-order radius-one sign reversal (including matching stronger marked-distance data), not implied by a global cover-time perturbation bound.

## value

PASS

Equal graph order was explicitly absent from a motivating nonlocality construction; a precise two-tree same-order counterexample at radius one, retaining distances and resistance as well as local degrees, is an independently useful sharp structural witness, without claiming an all-radius result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
