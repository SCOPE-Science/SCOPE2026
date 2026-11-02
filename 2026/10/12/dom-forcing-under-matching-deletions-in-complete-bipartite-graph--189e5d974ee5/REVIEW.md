# Mathematical review

## Correctness
The formula for ordinary zero forcing follows from the fact that every vertex in a matching-deleted complete bipartite graph loses at most one cross-shore neighbor. If three vertices on either shore remain white, no force can reduce their number. With no deleted edges, at most two whites are forceable; with one deleted edge, exactly three are forceable; with at least two, four are forceable. The proof's explicit alternating forcing chains attain these bounds. For dom-forcing, minimum forcing complements can be chosen dominating except at the three stated low-shore regimes; in each exception the proof identifies the obstruction and constructs a one-vertex-larger dominating forcing set.

Independent finite checks on 58 connected small parameter profiles and 681 explicitly constructed larger witnesses agree with the formulas. The all-parameter conclusion rests on the symbolic proof, not the finite checks.

## Originality
Susanth, Dominic and Premodkumar (2026, Theorem 5.8) and Jiang and Wan (2026, Proposition 5.3) determine the unmodified complete-bipartite case. Jiang and Wan's Proposition 5.6 gives the general criterion for equality of dom-forcing and zero-forcing numbers, but does not determine which matching-deleted bicliques satisfy it. Boyer et al. (2018, Proposition 4) treat complete multipartite zero-forcing polynomials, not bicliques with edges removed. Closely related published results on multipartite forcing and crown-graph restrained domination concern different graph hypotheses or invariants. Known path, cycle and cube instances remain acknowledged prior coverage. The complete parameterized matching-deletion classification survives the inspected comparisons as a best-of-knowledge new result, subject to the risk of unindexed equivalent literature.

## Mathematical value
A deleted matching is a canonical degree-balanced sparse perturbation of a complete bipartite graph. The theorem precisely identifies both the two-step saturation in the zero-forcing threshold and the three low-shore configurations where static domination requires an extra vertex. This is a motivated exact robustness classification for a natural family, not an isolated numerical entry.

## Scope and qualifications
The theorem covers connected graphs of the form \(K_{m,n}-M_t\) with \(2\le m\le n\) and \(0\le t\le m\), excluding the disconnected \((2,2,2)\) case. It does not assert corresponding values for arbitrary deleted-edge sets, propagation time or connected forcing. External expert and formal proof attestations have not been performed.

## Primary literature
- P. Susanth, C. Dominic, K. P. Premodkumar, *Dom-forcing Sets in Graphs*, Asian Research Journal of Mathematics 22(3), 88–104 (2026), DOI 10.9734/arjom/2026/v22i31058; Theorem 5.8.
- H. Jiang and H. Wan, *Forcing and domination in graphs*, AIMS Mathematics 11(7), 19772–19783 (2026), DOI 10.3934/math.2026802; Propositions 5.3 and 5.6.
- K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (2018), Proposition 4.
