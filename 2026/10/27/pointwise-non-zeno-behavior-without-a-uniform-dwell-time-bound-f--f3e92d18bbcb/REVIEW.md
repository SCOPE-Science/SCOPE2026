# Review

## Correctness — PASS

The state splits orthogonally into the constant Neumann mode and its heat-evolving complement. On a hypothetical finite accumulation tail, all hold intervals are shorter than one, so the constant-mode amplitude is bounded and nonincreasing. The nonzero high-mode component remains nonzero at every finite time and is smooth with bounded derivative on a compact interval away from zero. These facts give a positive lower bound on the state norm and a linear upper bound on the state increment, contradicting event intervals tending to zero. The pure constant mode has the explicit repeated interval \(\varepsilon/(1+\varepsilon)\); the zero state has no events. For each high eigenmode, direct solution of the trigger equation gives \(\log(1+\varepsilon)/(n^2\pi^2)\).

## Originality — PASS

The closest primary source is Wakaiki and Sano, *Event-triggered Control of Infinite-dimensional Systems*, arXiv:1801.05521, Section 3, Example 3.2. It proves that the infimum of the first event time over initial states is zero and derives the high-mode formula, but that result is not a pointwise no-Zeno theorem for arbitrary fixed initial states. The present claim adds the latter conclusion for the same specified heat model. Wang and Krstic (arXiv:2110.05680) prove a positive dwell-time result for a different PDE–ODE controller with a different dynamic trigger and an explicit maximum dwell time; it does not imply this claim. No exact equivalent was identified in the inspected literature. The search is not exhaustive, so unindexed prior work remains a risk.

## Value — PASS

The result separates two distinct properties that are often conflated in infinite-dimensional event-triggering: the lack of a uniform first-event lower bound over the entire state space, and actual finite-time accumulation along one fixed trajectory. It gives an exact counterexample family for the former and a rigorous pointwise exclusion for the latter in the self-review, which is directly relevant to interpreting event-trigger feasibility.

Self-review: passed. Independent audit: not yet performed.
