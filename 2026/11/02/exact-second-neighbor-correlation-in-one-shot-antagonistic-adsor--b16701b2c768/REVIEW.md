# Scientific review: second-neighbor correlation in one-shot antagonistic adsorption

## Correctness — PASS

The proof conditions on both endpoint times and proposed colours, factors the independent exterior half-line shielding probabilities, and handles the intervening site's single attempt by the exact conditional factor \(1-\beta\min(u,v)\). The shielding equations are a two-dimensional linear ODE and reproduce the source's one-point density. A pointwise strict inequality \(h_A(s)^2<1-\beta s\), proved via convexity and endpoint estimates, makes the distance-two covariance integrand positive on a set of positive measure. Finite-time and bias ranges, colour symmetry, the first-separation interpretation and boundary exclusions are explicit. The standalone finite-path rational checker reports 8,859 passed assertions, but the all-size claim rests on the independent analytic argument and factorial stabilization.

## Originality — PASS, subject to historical-priority risk

The 2023 one-shot antagonistic model paper was inspected throughout its definition, calculation and concluding sections: its announced result is the one-site density, not the separated pair probability. The 2022 correlation paper is for a single-species hard-core model where adjacent occupation is forbidden regardless of colour, while the 2022 two-species percolation paper allows repeated proposals and principally studies two-dimensional percolation. The closest related finite consecutive-cluster formulas give \(A,A,A\), but not the frequency of distinct \(A\) clusters separated by one vacant site, \(A,X,A\). Therefore the new distance-two probability and strict covariance sign are not implied by the located source statements or by those consecutive-block marginals. Relevant general correlation literature could still contain an equivalent special case; there is no claim of independent priority certification.

## Value — PASS

The separation-two event is the smallest genuinely inter-cluster spatial observable in this process: nearest neighbours cannot have opposite colours and contiguous-block frequencies do not measure dependence across a possible vacancy. An exact second-neighbour law, positive sign for every colour ratio and time, and explicit balanced-bias expression identify a natural effect of single-site-mediated antagonism. The fact is finite-range but structural, covering a continuous parameter family and extending the physical information beyond the known one-point densities.

## Scope and checks

The claim concerns colour-specific occupancy at a fixed time on \(\mathbb Z\). It makes no assertion about arbitrary distances or positive association of the full process. The calculation is exact only under one attempt per site and independent times/marks. The independently computed rational finite-path diagnostics check the endpoint-pair probability and demonstrate diminishing boundary effects; they do not replace the infinite proof. The most relevant full-text sources were arXiv:2306.09786v1 and arXiv:2210.05627v2; the closely related repeated-attempt article arXiv:2211.04622v1 was also inspected.

Self-review: passed. Independent audit: not yet performed.
