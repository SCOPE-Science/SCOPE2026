# Self-review

## Correctness

**PASS.** The rooted-tree feasibility sets obey three explicit invariants. Their induction uses the fact that each feasible child-count set is an integer interval, and that two consecutive integers cannot both lie in \(\{0,q\}\) when \(q\ge2\). The obstruction is an exhaustive four-case proof on two hub actions. The smallest-case claim uses exact generation of all labeled connected unicyclic graphs through six vertices and brute-force checks of each profile, with no probabilistic sampling. A standalone program independently implements the finite comparisons. Scope limitations appear in `RESULT.md`.

## Originality

**PASS, subject to literature priority risk.** Klimm–Stahlberg (arXiv:2301.11849) and Gilboa (arXiv:2301.11580) treat NP-completeness on unrestricted graphs. Yu et al. (arXiv:1911.05788) provide a generic decision procedure for trees but do not assert unconditional equilibrium existence for the picky pattern; Maiti–Dey (arXiv:2012.01880) assert existence on paths, cycles and bicliques, not all branching trees. The inspected sources do not imply the constructive tree theorem or the sharp unicyclic \(q=3\) boundary. Related mathematical-programming and graphical-game results may remain unlocated, so absolute priority is not claimed.

## Mathematical value

**PASS.** The same finite nonmonotone best-response family has an NP-complete unrestricted equilibrium problem, but on *all forests* equilibrium existence becomes unconditional, with a linear-time witness. Adding one cycle can genuinely eliminate equilibria; the seven-vertex sharp threshold for the first nontrivial \(q=3\) case identifies the smallest obstruction and separates branching trees from cyclic networks. This is a structural boundary rather than a generic tree-DP implementation or an arbitrary finite sample.

## Limits and nearest literature

The minimum-order result applies to \(q=3\) unicyclic graphs only, while the construction for other \(q\ge3\) is an upper bound on possible obstruction order. Source proximity and remaining priority risks are recorded in `AUDIT.json`. General dynamic convergence and optimal welfare are not studied.

Self-review: passed. Independent audit: not yet performed.
