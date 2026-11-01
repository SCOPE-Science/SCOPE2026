# Research review: exact oscillatory basins for balanced majority–minority dynamics

## Correctness — PASS
For each integer \(k\ge1\), the exact three-case global update identity follows by counting neighbors of a vertex in each bit state. This yields the unique four-cycle, the even-\(k\) isolated period-two states, all first-entry counts, and the Gaussian critical-window limit. The labelled-state verifier checks independent vertexwise updates for all 87,380 initial configurations with \(1\le k\le8\). Those finite checks support but do not establish the all-size proof, which is complete in `RESULT.md`.

## Originality — PASS, with material historical risk
Cannings (2009) already studied the exact majority/minority complete-graph rule and its special balanced four-cycles. This prior work is credited, not claimed as new. The full accessible Haslegrave–Cannings 2016 manuscript attributes period restrictions and the balanced four-cycle criterion to Cannings; the accessible Cao–Qin–Yang–Zhang 2013 article treats conformist/rebel updates and structural cycle conditions. None of their inspected statements gives the exact labelled central-binomial period-two census, their basins, the complete first-entry shell formula or the Bernoulli scaling window. A full-text comparison with Cannings (2009) could not be completed, leaving a significant historical-equivalence risk. Negative searching alone is not interpreted as proof of novelty. Details of equivalence and stronger-coverage checks are in `AUDIT.json`.

## Mathematical value — PASS
A natural exactly solvable social-network dynamical model has a surprising parity-selective collection of isolated two-cycles coexisting with a universal four-cycle; the microscopic population count, complete two-step relaxation census, and probability law quantify their physical prevalence. The questions are model-intrinsic and non-arbitrary.

## Limitations
The theorem applies only to synchronous strict-neighbor binary votes with equal-sized conformist and contrarian classes on complete graphs. There is no independent audit and no claim of historical uniqueness. The most directly relevant 2009 conference full text was inaccessible.

Self-review: passed. Independent audit: not yet performed.
