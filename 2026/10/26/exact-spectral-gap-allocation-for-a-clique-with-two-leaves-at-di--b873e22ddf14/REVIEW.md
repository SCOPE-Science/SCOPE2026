# Review: clique with two distinct pendant attachment vertices

## Correctness (PASS)

A globally applicable centered Euclidean trace-variance certificate bounds the second weighted Laplacian eigenvalue by the total budget divided by a known variance. The four explicit edge classes make every column of the certificate a Fiedler eigenvector and yield an unnormalized Laplacian with strictly positive remaining spectral gaps. The root exists uniquely by elementary monotonicity. Direct matrix assembly and numerical spectrum checks of the independent checker passed on 33 sizes. These finite checks corroborate, rather than replace, the proof for all integers \(k\ge1\).

## Originality (PASS, with limitations)

The closest primary antecedent is Sun–Boyd–Xiao–Diaconis (2006), which establishes budgeted continuous-time fastest mixing and its Euclidean dual but does not state this exact distinct-attachment clique solution. Jafarizadeh (arXiv:2501.02421v1) addresses discrete-time reversible-chain SLEM, clique lifts, and a single-attachment lollipop, with different admissible weights and topology. Accessible same-topic records include a clique with one two-edge pendant tail and two cliques joined by a bridge; neither specializes to different clique hubs bearing separate leaves. Broad Results/graph searches found no implication-equivalent formula, but rare alternate-name coverage remains possible. The 2009 symmetry primary full text could not be examined; only its abstract was available. Originality is not asserted as independently certified.

## Mathematical value (PASS)

The budgeted spectral-gap allocation models a heavily interconnected core with two different leaf bottlenecks. The formula gives all edge classes and a unique evaluable root, proves global rather than symmetry-restricted optimality, and shows a high-dimensional Fiedler eigenspace and sharp leading-order scaling. These facts provide practical coupling design rules and exact spectral optimization benchmarks beyond routine SDP feasibility.

## Limits

The claim does not cover discrete-time stochastic kernels, directed links, nonuniform vertex masses, or uniqueness of all optimizing conductance vectors. An exact mathematical proof supports all graph sizes; the attached numerical script uses NumPy and SciPy for reproducible finite tests. A specialized prior formula under a different topology name remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
