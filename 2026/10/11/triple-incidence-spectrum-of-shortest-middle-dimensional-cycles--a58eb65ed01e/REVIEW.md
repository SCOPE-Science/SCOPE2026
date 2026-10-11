# Same-model review

## Correctness
PASS. The exact published facet-orbit representatives and group generators were reconstructed independently in `verify.py`. They give the published face vector and a one-dimensional \(H_4(K;\mathbf F_2)\). Every one of the \(490\) missing six-set boundaries is tested to be nonzero modulo \(5\)-boundaries. The support lower bound is a complete simplicial-chain argument, not an experimental extrapolation. Exhaustive incidence counts establish the design parameter, the entire triple spectrum, and the five-triple orbit.

Risk: the computation is label-specific, so the printed source data and permutation convention are critical. The verifier checks the published orbit sizes and f-vector before any new count.

## Originality
PASS. Exact-object and alias searches covered complementarity, tightness, missing six-sets, minimum-support middle homology, design language, the numerical triple spectrum, and the A5 block-system formulation. Köhler--Lutz provide the exact complex and orbit data; Balagopalan provides a detailed 490-block construction; later work identifies and classifies fifteen-vertex \(\mathbb H P^2\) triangulations. The inspected statements do not give the complete triple-incidence spectrum or the unique five-triple minimum stratum.

Residual risk: the 1992 article was not available for a line-by-line reading, so an unindexed earlier observation cannot be ruled out absolutely.

## Value
PASS. The result studies the complete set of shortest vertex-supported representatives of the unique nonzero middle-dimensional mod-two homology class. The first two incidence levels are uniform, while the first nonuniform level recovers an invariant five-block partition. This gives a structural bridge between homology carriers and the symmetry of the triangulation rather than an arbitrary finite statistic.

Same-model review: passed. Independent audit: not yet performed.
