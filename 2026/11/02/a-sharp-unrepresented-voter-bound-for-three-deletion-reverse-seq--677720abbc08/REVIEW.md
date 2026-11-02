# Scientific review of a sharp three-deletion representation bound

## Correctness — PASS

For a fixed deletion history and a voter with deleted-candidate incidence mask and \(b\) winning approvals, the marginal loss of an approved candidate is the reciprocal of the current number of approved remaining candidates. Five nonpositive aggregate loss differences follow by comparing each deleted candidate with available alternatives and the average of the eventual winners. A five-multiplier, nonnegative dual inequality upper-bounds the indicator of approval of the first deleted candidate without representation; the stated eight-mask table expresses the residual, multiplied by \((3k+1)(k+2)\), as nonnegative rational expressions valid for every integer \(k\ge2\) and every \(0\le b\le k\). Separate two-gap inequalities bound representation failure among voters approving either later deletion by \(1/(k+1)\). The sharp family achieves the first bound exactly. The strict 252-voter case has verified positive margins at all three removals. These algebraic statements prove the universal claim; finite checks do not replace them.

## Originality — PASS, subject to literature coverage

Aziz's 2017 *A Note on Justified Representation Under the Reverse Sequential PAV Rule* establishes JR when at most two candidates are deleted and gives a distinct JR counterexample requiring at least seven deletions in its construction. Papasotiropoulos, *Reverse Sequential Proportional Approval Voting Rule: Proportionality and Approximation Guarantees* (arXiv:2609.35331v1, first public September 28, 2026), proves EJR for at most two deletions, exhibits a three-deletion EJR failure for twelve winners, and proves a general approximate-EJR bound. The latter yields a looser bound for wholly unrepresented voters than the present sharp three-deletion fraction. An EJR counterexample does not imply a JR counterexample. The first sharp three-deletion unrepresented-voter fraction, five-seat universal JR range, and strict six-seat JR counterexample are not stated or logically implied by the inspected sources. Targeted public-literature and indexed research-record searches did not reveal an equivalent theorem. This is a qualified scientific comparison, not a claim to exhaustive priority or independent validation.

## Value — PASS

The quantity \(\max_{c
otin W}U(c,W)/n\) measures the worst possible completely unrepresented cohesive group, directly controlling JR. Its exact extremum is a natural fairness invariant in the smallest deletion budget not already covered by the strong two-deletion theorem. The closed formula identifies a sharp transition between guarantees and failure at six seats, accompanied by a small strict counterexample. It is therefore substantially more informative than an isolated negative instance or a routine reparameterization.

## Closest literature, boundaries and remaining risks

The closest primary comparisons are the September 28, 2026 paper at https://arxiv.org/html/2609.35331v1 and Aziz's working paper at https://cgi.cse.unsw.edu.au/~haziz/invseqpav.pdf. The claim does not classify the entire approval-profile space, establish an EJR threshold, or control other numbers of deletions. An unindexed or inaccessible equivalent earlier result remains a possible publication-priority risk. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
