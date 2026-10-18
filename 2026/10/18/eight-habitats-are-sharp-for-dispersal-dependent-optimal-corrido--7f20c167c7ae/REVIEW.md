# Scientific review: dispersal-dependent corridor reinforcement

## Correctness — PASS

For a single reliable-edge upgrade on a tree, split the tree at that edge and sum over unordered pairs separated by the split. This proves the exact gain identity \(2(1-p)F_e(p)/n\) for mean reachable-component size. Equal patch-area probability-of-connectivity and its equivalent-connected-area transform induce exactly the same edge ranking. The Prüfer enumeration is complete for \(n\le8\); center-rooted canonical encodings avoid repeated isomorphism types. Coefficientwise domination is a rigorous all-parameter comparison for \(0<p<1\). For every nontrivial maximal-vector pair, the exact polynomial difference is one of five checked forms, yielding two changes and no other crossings. The two labeled examples have verified polynomials, and direct enumeration of edge-operating states tests the probabilistic identity independently. Risk: the finite exhaustive classification depends on inspection and reproducible execution of the supplied ordinary verifier; it is not a general theorem about larger trees.

## Originality — PASS (self-review)

Saura–Rubio's established probability-of-connectivity and link-importance machinery already covers the exact objective and, on homogeneous trees, produces equivalent rankings for edge removal and reinforcement. Hamonic–Albert–Couëtoux–Vaxès already formulate general budgeted link upgrades and can solve instances at fixed parameters. Williams–Snyder already motivate corridor restoration, using a different landscape-spanning-path objective. The additional mathematical assertion assessed here is that all trees through seven patches have one edge optimal throughout the full probability interval, while precisely two of 23 eight-patch trees do not, with explicitly determined crossings. The cited full texts inspected do not state or imply that sharp census without a further exact finite classification. Risk: a specialized graph-polynomial classification, including an older edge-reliability table, might already contain it; literature search cannot prove universal absence.

## Value — PASS

The size cutoff and exact exceptional topologies are interpretable benchmarks for sensitivity of a one-link restoration decision to species dispersal probability, using a standard habitat-connectivity objective rather than an invented invariant. At small passage probability, short connections affect local pair reachability; near certainty, the same upgrade favors a more balanced cut. The concrete minimal examples show when that tradeoff can actually change the optimal edge. This is a complete natural finite classification, not a claim that eight patches are biologically typical. Limitations are equal patch qualities, homogeneous independent link probabilities, one upgrade and trees; no population-persistence or field-performance claim is made.

Self-review: passed. Independent audit: not yet performed.
