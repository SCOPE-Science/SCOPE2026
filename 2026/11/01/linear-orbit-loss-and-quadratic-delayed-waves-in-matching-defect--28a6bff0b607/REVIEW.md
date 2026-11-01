# Scientific review

## Correctness — PASS
The local obstruction rule is necessary and sufficient: only the unique successor at the sole nonneighbor of a vertex can stop that vertex from advancing. At most one obstruction is present in an onto-three-color configuration. The proof separates all monochrome, exactly-two-color, three-color unobstructed, one-obstruction and two-obstruction cases and counts them without double counting. In the two-obstruction case the condition \(n-k\ge4\) ensures at least two available successor-colored neighbors at update two, so the process becomes a global three-phase rotation. The exact six-class formulas, period identity and sharp two-step delay therefore hold for all admitted \(n,k\). Verification is secondary: independent exhaustive programs checked 1,560,978 and 498,096 labelled states respectively.

## Originality — PASS, qualified
The closest inspected primary source is Gravner–Lyu–Sivakoff, arXiv:1610.07320v1 (2016), Theorem 3: it gives the exact successor-contact rule, a cycle-integral synchronization criterion and a general diameter bound, not the six-entry labelled transient census. A related previously derived complete-multipartite period identity covers the non-novel qualitative period bound; its tripartite numerical result covers only the three-part boundary, excluded here. The claim under review is the four-or-more-shore exact all-matching-size census and its linear/quadratic perturbation laws. Actual literature and research-record searches of graph names, variants of the update rule, aliases and equivalent claims did not reveal stronger covering formulas; undiscovered older material remains a risk.

## Mathematical value — PASS
The deleted matching size is a canonical structural variable. A non-obvious contrast follows: eventual consensus changes by precisely six states per missing edge, whereas the number of immediate primitive three-cycle orbits loses exponentially many per missing edge. Two separate missing edges generate a strictly quadratic population of delayed oscillations. These are exact natural dynamical invariants across an infinite, growing graph family, with a transparent mechanism and no need to assert any larger theorem beyond the census.

## Closest literature and limitations
The general 2016 irrotationality theorem addresses qualitative behavior; the new combinatorial blocking-pair decomposition determines labelled populations and temporal entry times not supplied there. Previously available three-shore formulas and all-shore period restrictions are explicitly treated as background. This result does not classify separate attraction basins of individual three-cycles, arbitrary nonmatching deletions or different update rules. The self-review checked the proof and verification files; an independent historical novelty and scientific audit remains open.

Self-review: passed. Independent audit: not yet performed.
