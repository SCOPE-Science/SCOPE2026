# Independent three-axis audit — record 2026/09/08/043

Review date (UTC): 2026-09-24  
Reviewer: separate AI audit under the SCOPE historical-record campaign

## Source identity

- Source path: `2026/09/08/043`
- Audited source tree: `ee171dd2686aa0e5c7c9f8b62be95819cdc070ec`
- `RESULT.md` blob: `6617a310e7d60865d9565b07cfcbbe90df8235`
- Historical `AUDIT.json` was preserved and was not treated as evidence of a new independent pass.
- No repair to `RESULT.md` is required by this audit.

## Exact claim audited

The record claims
`ex(7,C6)=13`, `ex(8,C6)=16`, `ex(9,C6)=20`, and `ex(10,C6)=21`,
where `C6` means a not-necessarily-induced six-cycle, and supplies explicit
C6-free witnesses. It separately claims only lower bounds
`ex(11,C6)>=23`, `ex(12,C6)>=26`, `ex(13,C6)>=30`, and `ex(14,C6)>=31`.
It does not claim optimality for n=11..14.

## Correctness — PASS

I independently checked the headline without relying on the record's branch-and-bound
node counts.

For n=7,8,9 I formulated the extremal problem as a 0-1 MILP with one binary
variable per edge and, for every simple 6-cycle, the inequality saying that at
most five of its six edges may be present. HiGHS, via SciPy `milp`, returned
proven optima 13, 16, and 20 respectively. The model used all simple 6-cycle
constraints (420 for n=7, 1680 for n=8, 5040 for n=9).

For n=10 the unrestricted solve was too slow for this bounded audit, so I used
a complete maximum-degree split to test whether a 22-edge C6-free graph exists.
Any 22-edge graph on 10 vertices has maximum degree d at least 5. Up to
relabelling, choose a maximum-degree vertex 0, fix its neighbourhood to
`{1,...,d}`, cap every degree by d, require at least 22 edges, and impose all
12,600 six-cycle inequalities. The five cases d=5,6,7,8,9 were each certified
infeasible by HiGHS. This split is exhaustive: a maximum-degree vertex exists,
its neighbours can be relabelled into the fixed set, and d ranges over every
possible maximum degree. Therefore no 22-edge C6-free graph exists. The
record's explicit 21-edge witness supplies the matching lower bound.

I also independently parsed all eight displayed witness edge lists, enumerated
all six-vertex subsets and all Hamiltonian cycles on each such subset, and
confirmed zero C6 subgraphs in every witness. Their edge counts are exactly
13,16,20,21,23,26,30,31 for n=7,...,14. Thus the four exact values and the four
one-sided lower bounds are correctly stated. The distinction between exact
values and lower bounds is preserved.

## Originality — PASS, qualified to the literature checked

The novelty claim was tested against standard terminology (`extremal number of
the hexagon`, `ex(n,C6)`, small-order C6-free graphs) rather than only the
record's wording.

Full text was available openly for Zhiyang He's *New Upper Bound on Extremal
Number of Even Cycles*, arXiv:2009.04590. Its stated result is an asymptotic
upper bound
`ex(n,C_{2k}) <= (16 sqrt(5) sqrt(k log k)+o(1)) n^(1+1/k)`;
it does not supply or imply the exact n=7..10 values or extremal edge lists.

I also checked the open arXiv record for Füredi--Simonovits,
*The history of degenerate (bipartite) extremal graph problems*,
arXiv:1306.5167, a broad survey of bipartite extremal graph theory. Searches
for the exact small values and for a small-order C6 table did not identify
coverage. The closest dedicated classical source found was Füredi--Naor--
Verstraëte, *On the Turán number for the hexagon*, Advances in Mathematics
203 (2006), DOI 10.1016/j.aim.2005.04.011; its published abstract describes
asymptotic bounds for the hexagon problem rather than an exact finite census
at orders 7--10. Additional exact-string searches for `ex(7,C6)` through
`ex(10,C6)` did not surface a prior exact table.

Accordingly, to the best of the evidence inspected, the finite exact values
with explicit replayable witnesses are not covered by these prior results.
This is not a guarantee that no unindexed table exists.

## Scientific value — PASS

After subtracting the known asymptotic theory, the surviving contribution is a
small but concrete exact invariant: four consecutive exact C6 Turán numbers,
together with explicit extremal witnesses and reusable C6-free witnesses at
the next four orders. Exact small-order extremal data are useful as regression
tests for extremal-graph software, as seeds/lower bounds for subsequent exact
searches, and as calibration points showing where asymptotic bounds are far
from sharp. The contribution is therefore more than a restatement of the
asymptotic theorem or a routine parameter substitution.

The value claim is deliberately limited: this is not a general theorem about
all n, it does not classify all extremal graphs, and the n=11..14 entries are
only lower bounds.

## Literature/search record

Queries included exact forms of `ex(7,C6)`, `ex(8,C6)`, `ex(9,C6)`,
`ex(10,C6)`, `Turán number hexagon small n`, and equivalent `C6-free graph`
terminology.

Sources substantively compared:

1. Z. He, *New Upper Bound on Extremal Number of Even Cycles*,
   arXiv:2009.04590.
2. Z. Füredi and M. Simonovits, *The history of degenerate (bipartite)
   extremal graph problems*, arXiv:1306.5167.
3. Z. Füredi, A. Naor, and J. Verstraëte, *On the Turán number for the
   hexagon*, Advances in Mathematics 203 (2006), 476--496,
   DOI 10.1016/j.aim.2005.04.011.

No third-party full text is reproduced here.

## Final disposition

- Correctness: **PASS**
- Originality: **PASS**, qualified to the literature actually checked
- Scientific value: **PASS**
- Disposition: **passed**

This audit is computational and literature-based; it is not a Lean proof or
human expert attestation.
