# Scientific review

## Correctness — PASS

The source's normal-diameter condition is reproduced independently. Strict convexity and antipodal symmetry ensure that all two-impact geometric orbits are normal diameters. The exact derivative computation yields \(K(u)=2(1+u)(1-3u+6u^2)/[(1+3u)(1+3u-2u^2)]\); standard reflection/free-flight matrices give \(\operatorname{tr}DT^2=4(1-K)^2-2\). The identity \((1+3u)(1+3u-2u^2)-(1+u)(1-3u+6u^2)=4u(1-u)(3u+2)\) proves strict \(0<K<2\) on the entire open range. Polynomial derivative/sign arguments prove exactly two exceptional resonances; Cayley–Hamilton proves the two-step matrix equals \(-I\) there. A standalone SymPy checker independently runs the geometry, algebraic and numerical tests; the infinite assertions rest on the written proof, not on the sample.

## Originality — PASS under inspected evidence

Fonseca–Leonel–Oliveira, arXiv:2610.29128v1, Section III.1, derives exactly the same boundary, existence condition and axial traces, but explicitly marks diagonal monodromy as still requiring examination; its final summary likewise does not give a diagonal formula or resonance classification. This result does not claim their diameter existence count or axial stability thresholds as new. Indexed mathematical results about external ellipsoidal billiards, the cos-five-theta destruction of a rotation-one-third caustic, and general centrally symmetric integrability do not imply the explicit spectrum of this boundary without additional geometry. The general two-bounce curvature matrix is an acknowledged standard prerequisite, not a novelty claim. Priority remains provisional against any unindexed exact study of the same boundary and against the general theoretical possibility of deriving the answer from standard formulas.

## Mathematical value — PASS

The primary paper identifies the exact missing diagonal stability calculation while both axial trajectories are hyperbolic. Closing it yields a natural complete four-orbit period-two classification and establishes the unusual coexistence of two hyperbolic axial and two elliptic diagonal normal diameters throughout the entire interval. The two exactly located minus-one resonances quantify the exceptional linear regimes and cannot be inferred merely from the source's existence count. This is a meaningful sharp classification of a physically motivated billiard family, not an arbitrary isolated parameter computation.

## Residual limitations

The analysis is linear. It neither proves nonlinear KAM stability nor excludes other rational rotation resonances with elliptic trace. It does not address periods three or higher. An independent historical and mathematical audit remains to be performed.

Self-review: passed. Independent audit: not yet performed.
