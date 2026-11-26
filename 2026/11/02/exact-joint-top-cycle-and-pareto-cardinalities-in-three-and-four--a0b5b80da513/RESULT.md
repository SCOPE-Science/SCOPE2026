# Exact joint top-cycle and Pareto cardinalities in four-agent house allocation

## Finding

Four labeled agents have independent uniform strict rankings of four labeled houses. For the weak-majority graph on bijective assignments, let \(T\) be the number of vertices in its top cycle and let \(E\) be the number of Pareto-optimal assignments. The complete joint law consists of the following 35 nonzero counts; divide by \(24^4=331{,}776\) to obtain probabilities. Unlisted pairs have zero count.

| \(T\) | \(E\) | Labeled profiles |
|---:|---:|---:|
| 1 | 1 | 31,104 |
| 2 | 2 | 20,736 |
| 21 | 4 | 288 |
| 22 | 3 | 1,152 |
| 22 | 4 | 3,456 |
| 22 | 5 | 1,728 |
| 22 | 6 | 4,320 |
| 22 | 7 | 576 |
| 22 | 8 | 2,016 |
| 22 | 9 | 576 |
| 22 | 10 | 1,152 |
| 22 | 12 | 288 |
| 22 | 14 | 288 |
| 23 | 3 | 1,152 |
| 23 | 4 | 6,912 |
| 23 | 5 | 5,760 |
| 23 | 6 | 3,744 |
| 23 | 7 | 4,032 |
| 23 | 8 | 1,152 |
| 23 | 9 | 1,728 |
| 23 | 11 | 576 |
| 24 | 3 | 18,432 |
| 24 | 4 | 43,200 |
| 24 | 5 | 40,896 |
| 24 | 6 | 31,968 |
| 24 | 7 | 40,896 |
| 24 | 8 | 23,400 |
| 24 | 9 | 10,368 |
| 24 | 10 | 13,968 |
| 24 | 11 | 5,760 |
| 24 | 12 | 5,592 |
| 24 | 14 | 3,744 |
| 24 | 16 | 216 |
| 24 | 18 | 576 |
| 24 | 24 | 24 |

The top cycle is the entire assignment space in 239,040 profiles (probability \(415/576\)). In 18,432 profiles (probability \(1/18\)) the top cycle is the entire space although only three assignments are Pareto optimal. The Pareto set is always contained in the top cycle in this census, and the inclusion is strict with probability \(11663/13824\). The mean top-cycle size is \(1299/64\); the previously available Pareto mean \(1597/288\) is recovered as a marginal check.

## Definitions and scope

Agents and houses are each labeled \(0,1,2,3\). Each of the \(24^4\) ordered strict preference profiles has equal weight. An assignment is a bijection; let \(r_i(h)\) be the rank assigned by agent \(i\) to house \(h\), with smaller ranks preferred. For distinct assignments \(a,b\), add a directed edge \(a\to b\) when
\[
\sum_i \bigl(\mathbf 1[r_i(a_i)<r_i(b_i)]-\mathbf 1[r_i(a_i)>r_i(b_i)]\bigr)\geq 0.
\]
An unchanged house contributes zero; majority ties give two directions. The top cycle consists of assignments that can reach every assignment along directed paths, allowing a zero-length path. An assignment is Pareto optimal when no other assignment weakly improves all agents and strictly improves at least one. This is not the top-trading-cycles mechanism.

## Exact census and coverage

Simultaneously rename houses so that agent zero ranks the houses in the order \((0,1,2,3)\). This relabeling is unique, preserves all majority edges and Pareto comparisons, and has exactly 24 inverses on each normalized profile since a nonidentity house permutation cannot fix a strict ranking. Enumerate all \(24^3=13{,}824\) choices for the other three rankings and weight every result by 24.

For each representative, list the 24 bijections and compare every pair. The nonnegative margin test constructs the complete majority graph. Reachability from each assignment computes the top cycle by definition. For distinct assignments, if every changed recipient prefers the new house in one direction, the target of that directed preference is Pareto dominated. Exclude all such targets to obtain the Pareto set. Compare the resulting two sets and increment their cardinality pair. This enumerates every profile orbit and all possible directed edges and dominators. The table and the strict-containment frequency require no statistical estimation.

Run `python3 verify.py` alongside `joint_counts.csv` for the complete integer replay. The program compares every joint cell and its absence against the provided table and checks the total and selected aggregates.

## Relationship to existing results

Brandt, Chen, Dong, Lederer and Schlenga, [*Majoritarian Assignment Rules*](https://arxiv.org/html/2602.14816v1), Section 4.1, Remark 3, give the possible top-cycle sizes for small markets and the two symmetry types for a four-agent top cycle of size 21. The possible sizes, the exceptional types and the Pareto-in-top-cycle containment are not claims of novelty here. Their code supplement [10.5281/zenodo.18633210](https://zenodo.org/records/18633210) includes symmetry-reduced profile generation and separate cardinality routines; the cited experiments do not supply the four-agent labeled joint counts.

The [three-agent half-law](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-a-half-law-for-pareto-inefficient-top-cycles-in-three-agent-hous--7ae631a3665d) already gives the three-agent joint law by projecting its three-way table. The [four-agent random-priority lottery census](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-the-complete-four-agent-random-priority-matching-lottery-spectru--5de01f4eeb3e) gives the separate Pareto-size marginal: serial dictatorship produces exactly the Pareto-optimal assignments under strict preferences. Indeed, the outcome of any such order is undominated by considering the first deviating agent. Conversely, in a Pareto-optimal assignment at least one agent gets her favorite available house, since otherwise each agent can point to the holder of her favorite house and a directed cycle yields a strict improvement by cyclic exchange. Remove that agent and house and repeat. Thus the support count of random priority is the Pareto count. A histogram of random-priority support or its lottery shapes does not record the majority-reachability coordinate for each profile. The contribution here is the four-agent coupling, which quantifies how often a large or fully nonselective majority top cycle coexists with few efficient assignments; separate support or size summaries do not determine that coexistence.

## Limitations

This is a finite result for four agents with independent uniform strict preferences. It does not extend to larger markets, incomplete rankings or alternative priors. No absolute priority or formal verification is asserted.
