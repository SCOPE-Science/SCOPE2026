# Scientific review

## Correctness
PASS. Two fixed permutations couple shared agents' positions so that their normalized rank fractions sum strictly above one but at most one plus the longer cycle's reciprocal. The residual analysis of two independent counters gives both upper and lower quota for every possible prefix. Exclusive agents satisfy ordinary round-robin quota. All overlap sizes, including empty and full, and all nonzero agent-set sizes are covered. A standalone verifier exhaustively checks all relative phases for sizes at most 30.

## Originality
PASS on presently accessible evidence. The motivating eligibility-aware fair-division paper considers arbitrary eligibility families and does not state the two-type full global-quota theorem. Online proportional apportionment establishes global quota for unrestricted streams with at most three parties, not arbitrarily many parties facing two fixed eligibility supports. An earlier laminar-family prefixwise upper-quota claim does not encompass crossing families, nor does it imply both quota directions. Targeted searches and direct comparison with these primary manuscripts did not uncover an equivalent result. An unindexed or differently formulated prior construction remains a realistic residual risk.

## Value
PASS. This separates the unlimited-agent two-eligibility-type regime from general online lower bounds and gives an explicit constructive exact quota rather than an approximation. Nonlaminar overlapping worker-qualification classes arise naturally in restricted assignment. Simultaneous lower and upper quotas strengthen Prop1 and may be useful as a primitive in further special-alphabet online rounding.

## Limits
The supports must be known and fixed, the job sizes identical, and the distinct type count at most two. Results for unrestricted online vectors or three eligibility classes are not claimed. Finite computation is corroborating evidence, not an infinite proof.

Self-review: passed. Independent audit: not yet performed.
