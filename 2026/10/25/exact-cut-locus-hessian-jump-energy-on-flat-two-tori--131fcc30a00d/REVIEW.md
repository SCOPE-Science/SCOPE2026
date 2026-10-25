# Review: Exact cut-locus Hessian jump energy on flat two-tori

## Correctness

PASS. On each regular Voronoi facet, the two distance-gradient traces differ by \(|v|/|x|\). Centering the facet at \(v/2\) reduces the squared-jump integral to an exact arctangent integral. The rectangular formula follows by substituting the two facet lengths, and the derivative argument proves a unique global maximum at equal side lengths under fixed area.

## Originality

PASS, with scope limited to the stated aggregate and optimizer. The general singular-Hessian jump formula is established prior work. The inspected literature gives that local density and related flat-torus distance-energy results, but no inspected source states this squared cut-locus jump energy, its Voronoi-facet sum, or the fixed-area rectangular maximizer. Targeted exact-phrase and alias searches found related but non-equivalent results.

## Value

PASS. The quantity is a natural shape-sensitive measure of the singular part of the distance Hessian, and the exact facet formula plus sharp rectangular extremizer gives a reusable benchmark for cut-locus geometry and weak geometric analysis. The result is deliberately limited; no downstream PDE consequence is claimed.

## Closest literature and limitations

Mantegazza–Mascellani–Uraltsev, arXiv:1303.1421, establish the general singular-measure structure of the distance Hessian. Zhou, arXiv:2609.05622, treats facetwise Hessian contributions for radial distance kernels on flat tori and distance-energy optimization. Neither inspected result states the exact \(J_2\) aggregation or the rectangular fixed-area extremizer. The square-maximization statement is not extended to all lattice shapes.

Self-review: passed. Independent audit: not yet performed.
