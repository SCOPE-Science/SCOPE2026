# Scientific review

## Correctness

PASS. The cost normalization is exactly the sum of each agent's mean distance to all *other* coalition members; for a group of size at least two this equals twice the unordered pair-distance sum divided by group size minus one. The proof introduces positive weights matched to the two sorted candidate costs. All two-group allocations obey a normalized linear inequality: concavity at each fixed pair of group sizes reduces its verification to vertices of the three-type occupancy polytope; the explicit split-type cases are proved by endpoint concavity or nonnegative numerator differences. Singletons and the grand coalition are checked separately. The computer program independently checks 42,189 type-count allocations with rational arithmetic; it is corroboration, not the infinite proof.

## Originality

PASS under available evidence. The full accessible primary manuscript, *Metric Hedonic Games on the Line* (arXiv:2602.05888), posits sorted optimality for freely sized Average-Jump coalitions as Conjecture 3.11 and gives the general coefficient formula but no three-type optimum formula. This theorem proves a meaningful support-size restriction with explicit value. The manuscript's unsorted fixed-cardinality swap example is not a freely sized jump optimum and hence does not cover the finding. General min-sum clustering papers use unnormalized within-group sums, not this coalition-size normalization. Targeted mathematical research-record searches and textual literature searches returned no equivalent theorem. Unindexed or differently worded equivalent coverage remains a risk.

## Value

PASS. The result addresses an explicit open structural conjecture in metric hedonic games, in the natural lowest support size for which optimal cost cannot always be zero, and yields a closed-form optimum and constant-time selection rule from the three multiplicities and two type gaps. It separates a case of assured sortedness from published counterexamples under fixed group sizes, clarifying the dependence on coalition-size freedom. The result neither requires nor claims a general solution to the conjecture.

## Limits

At least one agent belongs to each of three distinct types; positive multiplicities are unbounded. Singletons have cost zero. The three-type conclusion is not a statement for arbitrary type supports, no fixed-cardinality restriction is imposed, and unique optimality is not claimed. An independent review has not been performed.

Self-review: passed. Independent audit: not yet performed.
