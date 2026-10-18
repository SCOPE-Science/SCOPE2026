# Independent mathematical audit

## correctness

PASS

B is nonsingular with determinant 70 and every row has squared norm 29. For normalized A=B/√29, b=0, x0(t)=(-10,t,-30), and fresh uniform without-replacement β-samples per step, first-step coupling by nested subsets proves monotonic one-step expected squared error for every normalized consistent system. At horizon two all ordered sample pairs (β=1:9, β=2:9, β=3:1) have deterministic strict maximal-absolute-residual choices throughout t∈[1/2,3/2]. Independently reconstructed rational projection matrices P_i=I-b_i^T b_i/29, strict quadratic branch margins and all expected-risk coefficients: F1=4(26103t²-839010t+30675050)/219501, F2=2(43707t²-2466480t+57312850)/219501, F3=4(2836t²-170920t+3628725)/24389. Differences F1-F2=2(2833t²+262820t+1345750)/73167>0 and F3-F1=4(1983475-699270t-579t²)/219501>0 on the full closed interval. Thus F2<F1<F3 with β=3 worst, and horizon two is minimal. Unit relaxation, fixed 3x3 system and exactly two projections; not an asymptotic-rate claim.

## originality

PASS

Haddock–Ma describe the identical SKM normalized row selection and analyze convergence-rate bounds; no theorem there establishes monotonic realized expected squared error with sample size over a fixed multi-step horizon. Nutini et al. give greedy Kaczmarz one-step benefits and multi-step upper bounds, not exact three-way ranking; De Loera–Haddock–Needell analyze related sampling feasibility scheme. A published two-row cyclic-overrelaxation finite-horizon cost concerns relaxation, not subset size. The strict reversed ranking on an explicit open parameter interval after the provably minimal two-step horizon is a non-implied counterexample.

## value

PASS

A minimal-horizon counterexample shows a genuine algorithmic tradeoff: taking MORE candidate rows and applying the largest-residual projection can produce GREATER two-step mean squared error, with the intermediate sample size best. This sharpens interpretation of sampling-rate convergence guarantees and provides an exact reproducible benchmark; not just another parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
