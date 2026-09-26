# Independent audit — 2026/09/09/086

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

I independently generated the 72 distinct 20-bit masks of labeled tight 5-cycles on six vertices, marked all their supersets among 2²⁰ graphs, and found exactly 371229 avoiding graphs. The independent edge-count distribution agrees at every m=0,…,13 with RESULT.md, including 60 at the unique maximal edge number 13 and none at 14+. I also fetched and reran the package's distinct stdlib verifier: it checked 835 representatives against the forbidden masks, true minimum canonical codes over all 720 vertex permutations, disjoint isomorphism orbits totaling 371229, and a second full 2²⁰ enumeration. The 835 types and unique 13-edge type therefore have both coverage and orbit-size certificates. The result is entirely finite at n=6 and makes no density claim.

## Originality — PASS

Bodnar–Leon–Liu–Pikhurko, arXiv:2506.03223, concerns density of short tight cycles and explicitly separates the single C₅³ case. The full 6-vertex labeled/type distribution is a concrete small-host census not reported in the consulted primary paper. Broader catalogue priority is not established.

## Scientific value — PASS

A verified extremal base case and near-extremal orbit list can constrain finite induction or flag-algebra experiments. Its 13-edge maximum does not transfer to an asymptotic Turán bound by itself.

Sources: https://arxiv.org/pdf/2506.03223 ; https://arxiv.org/abs/2209.08134 . Open preprints sufficed.
