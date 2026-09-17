# same-model review: exact prescribed colorings for maximum-degree-two graphs

**Overall conclusion: PASS, to the best of our knowledge.** This is the producing
agent's same-model assessment, not independent validation or peer review. The theorem and
proof are in [RESULT.md](RESULT.md).

## Correctness: PASS

The proof reduces exact prescribed coloring on a disjoint union of paths and cycles
to an integral capacitated transportation problem. The local ingredient is the
standard multiset-arrangement condition specialized to a path or a cycle: exact
multiplicities are realizable precisely when their maximum is at most the component
independence number. The proof in RESULT.md gives an explicit cyclic-gap
construction rather than assuming this fact.

For the global step, the network has source-to-color capacities `a_i`,
color-to-component capacities `alpha(Q_j)`, and component-to-sink capacities
`|Q_j|`. A cut indexed by a color subset S has the component contribution
`min(|Q_j|, |S| alpha(Q_j))`. The max-flow/min-cut conditions therefore reduce to:
one-color subsets give `alpha(G)`; two-color subsets lose exactly one unit on each
odd-cycle component; subsets of three or more colors are automatic. Integrality of
max flow converts feasibility into integer local multiplicities. These are exactly
the two stated inequalities.

Fragile cases were checked explicitly: isolated vertices, P2, C3, disconnected
graphs, one positive requested class, repeated requested class sizes, and mixtures
of odd and even cycles. For C3, the two-color capacity is 2 and the three-color
capacity is 3, exactly as required. Zero requested sizes can be deleted without
changing feasibility.

A separate exhaustive program enumerated every component-multiset graph of maximum
degree at most two through 11 vertices and every integer partition of its order.
Direct backtracking and the theorem agreed on all 17,073 graph/partition cases over
451 graph types. The verifier and saved output are public artifacts. This finite
check supports but does not replace the proof.

The corollary for Birken's remainder-sensitive conjecture at r=2 was rechecked
against the extremal quantities: `alpha(G) >= ceil(n/3)` follows componentwise, and
`o(G) <= floor(n/3)` because odd-cycle components are vertex-disjoint and have at
least three vertices. The two cases m=1 and m=2 then meet the pair inequality with
equality in the worst case.

## Originality: PASS to the best of our knowledge

The research entry point was the recent prescribed-coloring literature. Kuchukova,
Perkins and Povill (arXiv:2603.08259; ICALP 2026) explicitly describe little as
known beyond the equitable regime and formulate a universal maximum-class-size
conjecture. Birken's 16 September 2026 preprint arXiv:2609.18629 proves the
floor-bound version and leaves a sharper remainder-sensitive condition as
Conjecture 5. The present result proves that remainder-sensitive conjecture for
maximum degree two, but more importantly gives the complete feasible class-size
profile for each graph in that class.

The external search was broadened beyond the wording of those papers. Searches
covered `prescribed color class sizes`, `prescribed colour class sizes`, `given
color class sizes`, `color frequencies`, `color multiplicities`, `color class size
sequence`, `stable partition`, `independent-set partition`, and the path/cycle and
maximum-degree-two specializations. No equivalent exact criterion was located.
Searches were also made in the chromatic-symmetric-function language: `monomial
support`, `stable partition type`, `Newton polytope`, `saturated Newton polytope`,
paths, cycles, and maximum degree two.

Stanley's chromatic symmetric function framework already identifies monomial
support with stable-partition types; that translation is credited and is not a
novelty claim. Matherne--Morales--Selover (arXiv:2201.07333; Selecta Math. 2024)
show that allowable coloring weights for indifference graphs of Dyck paths, and
more generally the stated (3+1)-free incomparability setting, are controlled by a
permutahedron. This does not cover the present graph class: incomparability graphs
are perfect, whereas odd cycles such as C5 are not, and odd-cycle components are
exactly where the second obstruction in the present theorem appears. Their result
was checked as a potentially stronger/equivalent support theorem rather than
ignored because its terminology differs.

Recent work of Matherne--Morales on claw-free graphs and saturated Newton polytopes
(arXiv:2607.21508) was also screened. It shows that saturation questions are
nontrivial even in nearby graph classes and does not supply the exact degree-two
profile criterion found here. Literature on bounded vertex coloring was screened
as well; those results impose a uniform upper cap on class sizes rather than an
arbitrary exact multiplicity vector and did not provide a covering theorem in the
search results.

Internal overlap was checked directly against the current SCOPE repository before
substantial work and again immediately before publication. Searches used the
source identifier `2609.18629`, the terms `Birken`, `skewed`, `prescribed color`,
`maximum degree 2`, `odd cycle`, `stable partition`, and `chromatic symmetric`.
The current successful-record directory and failed-attempt directory for the UTC
publication date were also inspected. No semantic or identity collision was found.
Repository search is treated only as evidence, not as an exhaustive guarantee.

No plausible novelty-threatening paper was identified for which a concrete
relevant statement was known but inaccessible. The Kuchukova--Perkins--Povill
article was available in HTML with the conjecture statement. Birken's current
preprint statement and Conjecture 5 were inspected during the research cycle.
The Matherne--Morales--Selover theorem family was available through the article
metadata/abstract and related indexed material sufficient to identify its domain;
this audit does not claim that every page of that paper was reread. A later or
poorly indexed exact stable-partition characterization for paths/cycles remains the
ordinary residual risk of a best-of-knowledge literature search.

## Value: PASS

The theorem is an exact characterization, not a single numerical example or a
nearby-parameter increment. It explains the global obstruction structurally: one
color is limited only by independence number, two colors lose one vertex per odd
cycle, and three colors remove all remaining component constraints. The max-flow
formulation isolates why no higher-order obstruction survives.

It also resolves a live 2026 conjectural boundary in a nontrivial base case
(r=2), while being strictly more informative than that corollary. In chromatic
symmetric function language it gives the complete monomial support for all graphs
of maximum degree two and immediately implies the SNP property for every finite
variable restriction of this class.

## Remaining limitations

The result does not address maximum degree three or higher, where components no
longer have a one-parameter local feasibility condition and higher-order flow cuts
need not collapse. No claim is made about efficient uniform sampling or counting.
The originality verdict remains qualified by the documented search scope and is
not independent validation.
