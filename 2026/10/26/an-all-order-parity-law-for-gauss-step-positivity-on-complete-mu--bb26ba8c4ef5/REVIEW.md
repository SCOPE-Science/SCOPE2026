# Scientific review

## Correctness — PASS

The result holds for all finite connected unweighted complete multipartite graphs, arbitrary positive real steps and every integer stage count. The proof directly computes all eigenprojectors, reconstructs each entry, proves a stage-uniform strict divided-difference inequality by coefficient ratios, uses an exact positive integral for the even-stage Padé numerator and establishes the odd-stage obstruction by the limiting spectral projector. This is a complete analytic all-quantifier argument, not an extrapolation from tests. The denominator of the rational stability map is strictly positive on the nonnegative spectrum. Exact rational verification checks finite examples separately.

## Originality — PASS, with residual risk

The result was compared by *statement and implication* with primary literature and available specialized fixed-stage claims. Earlier complete-multipartite conclusions for the two- and three-stage Gauss methods are subsumed; they are **not** presented as independently new. The differentiating assertion is a parity-complete characterization for every integer number of stages, including arbitrarily high even order, coupled to a proved stage-uniform off-diagonal positivity mechanism. The 2013 SSP paper bounds explicit multistep Runge–Kutta schemes; the 2020 adaptive-weights work changes the step; the 2021 positivity paper identifies diagonal Padé positivity as an open challenge; and the 2024 Gauss paper treats convolution-quadrature order reduction and high-stage stability functions, not these graph-dependent entry signs. Indexed summaries gave no identical or stronger all-stage statement. Residual possibility of specialized older unpublished/unindexed work, a differently named rational-functional calculus theorem, or a full publication uninspected here remains; novelty is not certified by search absence.

## Mathematical value — PASS

Unconditional endpoint positivity at arbitrarily high even Gauss order is a nontrivial structural exception to the familiar general high-order positivity obstruction. The classification covers all stage counts and all multipartite sizes and separates off-diagonal positivity from the odd-stage diagonal obstruction. It gives a provably safe class of high-order numerical heat steps and an algebraic principle (monotonicity of the Padé divided difference) that can be tested for other rational integrators, although extension beyond this class is unproved. This is not merely a higher numerical order in one fixed case or a recomputation of a table.

## Closest work and limitations

The closest prior specialized claims cover stage counts two and three on the same graphs, while the closest broader publications supply scalar stability functions or general positivity theory without this entrywise conclusion. The current result is restricted to completed endpoints of unweighted graph heat equations; even-stage high-step positivity is not \(L\)-stability and the map approaches the identity as the step tends to infinity. It does not imply stagewise positivity, positivity on arbitrary graph Laplacians, or an exact odd-stage transition step. Verification uses exact arithmetic on finite cases but is not independent mathematical certification.

Self-review: passed. Independent audit: not yet performed.
