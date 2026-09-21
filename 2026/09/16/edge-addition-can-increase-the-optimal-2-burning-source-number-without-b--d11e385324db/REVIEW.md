# same-model review

Overall: **PASS**, under TBOK-v1. This is the researcher's same-model assessment,
not independent validation.

## Correctness: PASS

The exact claim is that, for every q >= 1, connected spanning pairs H subset G
of diameter two exist with t_2(H)=2 and t_2(G)>=q+2. The proof in RESULT.md
specifies all vertices, edges, rounds and quantifiers. It also proves
b_2(H)=q+6 and b_2(G)<=q+5 without claiming an exact G optimum.

The decisive lemma is the prefix property of a source-free unchanged arm:
only its next vertex can activate, and the first requires both exterior
vertices a,c to have been blue the previous round. Since both cannot be blue
after round 1, the endpoint is no earlier than L+2. This remains true if a or
c is not a source, and if arbitrarily many other arms receive sources.
There are more arms in H than available source rounds at any earlier deadline.
In G, the explicit shorter schedule forces every remaining long arm to have
a source. The counts m=L+2, k=L-2 and the last source round k+2=L were checked.

Independent exact enumeration and bitmask dynamic programming agree on the
seven-vertex example: H=(4,2), G=(3,3). The test program also compared actual
computed pairs against [1, Theorem 2.8 and Observation 2.9] for every path and
cycle of orders 3-9, with all 14 equal. It tested constructed schedules for
q=1-30, and the k=1,L=3,m=5 boundary family gives H=(5,2), G=(4,2).
Command: `python3 artifacts/verify_burning.py`; all assertions passed.
These finite tests support, but do not replace, the general proof.

## Originality: PASS within documented scope

The problem was formulated after reading [1] and before
candidate-originality searches. Screening did not treat topical matches as
coverage. Research then found a small counterexample and proved the family.

Equivalent forms checked: this is failure of edge monotonicity of the second
coordinate of a lexicographically minimized (completion time, source count)
pair; equivalently t_2(J)=F_J(b_2(J)), where F_J is the minimum sequential
seed count for a fixed deadline. It is not failure of fixed-deadline seed
monotonicity and not failure of monotonicity of minimum percolating-set size.
Both of those quantities have valid schedule-transfer monotonicity. Both
graphs even have a two-vertex percolating set. The cone representation also
reduces the process after seeding a to ordinary burning on a spider, so the
universal-vertex reduction was explicitly checked as possible routine coverage.

Closest covering-looking assertion: [1, Lemma 2.4, p. 4], inspected with its
proof, asserts the opposite t_2 inequality. The proof does not preserve
optimal completion time when transferring schedules. This is a demonstrable
gap, not a theorem being ignored merely because it is inconvenient.

Closest valid general tool: [1, Proposition 2.12, p. 6] bounds b_2 by seeding
a dominating set and then using ordinary burning. Its specialization gives
an upper-bound mechanism here but neither a lower bound on fastest schedules
nor a source-count increase under edge addition. [1, Theorem 3.1, pp. 7-8]
computes parameters for spiders, not their cones. [1, Observation 5.1, p. 17]
relates minimum percolating sets to t_2 but also gives no such lower bound.
These passages were read. The residual is the unseeded-arm deadline bound
combined with shortcuts on four arms, proving that a feasible two-source
schedule loses time-optimality and every fastest schedule needs at least q+2
sources. It does not follow by substituting parameters in those results.

The searches below investigated stronger and equivalent coverage through
generalized burning, graph operations, source-optimal burning, sequential
target-set selection and timed threshold diffusion. No concrete unresolved
source clue asserting this phenomenon or the same construction was found.
Several searches were low-yield or timed out; the assessment does not turn
those failures into proof of absence.

## Value: PASS

The result corrects an explicit published universal assertion in the inspected
version and strengthens a single failure to an unbounded gap with t_2(H)=2.
The graphs have diameter two, and shortcuts on only four arms suffice.
The proof identifies why optimizing time first changes the comparison law,
and gives the valid replacement when the optimum times are equal. This is
a useful short correction with an extremal strengthening, not a general
solution to the open classification questions in [1]. The proof is elementary;
its value comes from the false comparison it resolves and the unbounded
phenomenon, rather than technical complexity.

## Evidence scope

- Discovery search sought current graph-burning
  developments and supplied [1]; unrelated hits were not used as evidence.
- Inspected primary version: arXiv:2411.02050v2.
  Read ranges 0-24000 and 40000-49373 include definitions, Lemma 2.4 and proof,
  paths/cycles, joins, spiders, conclusion and references. A later whole-text
  search retrieved Lemma 2.4 and its use before Corollary 4.2. Full-paper
  inspection is not claimed. DOI acquisition returned this same version.
- Search : 2-burning source monotonicity and
  counterexamples; burning source number and spanning subgraphs; corrections
  to Jacobs-Messinger-Trenk. Results led back to [1], with no identified
  correction. This is search evidence, not an exhaustive correction history.
- Search : sequential target-set selection and
  non-monotonicity; minimum sources, edges and threshold burning; generalized
  burning developments. It identified the inaccessible 2021 foundational
  paper, plus distinct diffusion models and later graph-family computations.
- Search : cones and source counts; spiders with
  a universal vertex; time-optimal target sets and edges. The relevant hit
  was [1]'s dominating-set reduction, inspected in the primary text.
- Final successful equivalent-form search :
  sequential threshold diffusion, minimum seeds, deadline, edge addition and
  nonmonotonicity. It gave no concrete matching theorem; largely irrelevant
  results are not substantive noncoverage evidence.
- Three additional final literature calls timed out: queries on source-number
  monotonicity, Lemma 2.4 counterexamples, adding edges, and sequential timed
  target-set selection. They returned no usable evidence and are not counted
  as completed literature checks. Earlier successful searches cover the
  central named parameter and the universal-vertex reduction, but breadth
  across all diffusion terminology remains a limitation.

## Originality scope and inaccessible sources

To the best of our knowledge, within the documented search scope and accessible
literature, no equivalent or stronger prior result was found. This is not an
exhaustive guarantee of novelty.

Yinkui Li, Xiaoxiao Qin and Wen Li, *The generalized burning number of graphs*
(2021), DOI https://doi.org/10.1016/j.amc.2021.126306, is the most plausible
inaccessible related source identified. It studies the parent process and
graph operations, making an equivalent construction possible. DOI and exact-title acquisition attempts did not yield usable full text. The full text was
not obtained through available channels. The relevant theorems and proofs
remain unverified. This is ACCESS_LIMITATION, with only possible relevance
and no concrete coverage evidence. The 2024 authors describe t_2 as new,
which informs but does not settle the question of earlier equivalent results.

A separate publisher revision of [1] was not inspected: its DOI request
returned the arXiv v2 already read. The correction claim is limited to that
version. No other inaccessible source with a specific plausible covering
theorem was identified. A later correction or equivalent stronger result
would require revising the originality verdict. Overall PASS is qualified
by this documented scope, with correctness and value assessed separately.

## Recorded review qualifications

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is claimed only to the best of our knowledge; consult REVIEW.md for search evidence and inaccessible sources. Publication is not peer review or a guarantee of priority.
