# Scientific review

## Correctness — PASS

The claim is finite and precisely specifies connected simple bipartite incidence graphs, original NODF (equal-degree pair contribution zero), maximum unipartite Newman–Girvan modularity, and degree-preserving two-by-two switches with connected endpoints. For a guild of size at most two, NODF is invariant under swaps by degree-count identities. Thus only the three-by-three and three-by-four cases need finite exclusion through seven vertices. The standard-library certificate enumerates all binary incidence matrices, all eligible switches, checks connectedness, and evaluates NODF as exact fractions. Modularity uses an exhaustive subset-partition recurrence whose induction proof is included in the result. The witness is checked independently by enumeration of all 4140 eight-vertex set partitions. Both exact increases are positive. The theorem makes no unbounded claim from finite enumeration.

## Originality — PASS (same-model, bibliographic uncertainty remains)

Almeida-Neto et al. (2008) define NODF and analyze nestedness under fixed-margin null models. Fortuna et al. (2010) compare nestedness and modularity with a swap null model and show changing correlations with connectance, but report empirical and simulation comparisons, not a smallest-order, connected, exact co-improvement theorem. Joppa et al. (2011) study individual NODF contributions, not joint optimum modularity. Leung and Weitz (2015) exhibit nested-modular structures through network growth and use Barber rather than unipartite Newman–Girvan modularity. A 2026 generative-null-model article treats estimation biases rather than the sharp eight-species switch question. Research-index comparisons located graph-incidence and network-degree results but no theorem implying this precise threshold. Terminology differences, unexamined supplements, and possible unindexed network-theory results remain risks; the absence of a search hit alone is not presented as a proof of novelty.

## Mathematical value — PASS

The finite minimum isolates a natural structural issue in ecological null-model practice: whether one elementary degree-preserving step can improve both nestedness and modular community organization without changing the degrees of any species. Degree-matched comparisons remove a major confounder, and exact optimization avoids heuristic modularity artifacts. The result gives both a sharp low-dimensional obstruction and an explicit unicyclic witness; it is a useful benchmark when interpreting fixed-degree network rewiring. Its value does not depend on claims about ecological dynamics, which are not proven.

## Limits and further verification

The conclusion is specific to NODF and maximum Newman–Girvan modularity. It does not cover Barber modularity, nestedness temperature, degree-weighted interaction matrices, disconnected graphs, or ecological population dynamics. Some equivalent treatments outside the inspected primary literature may have escaped discovery. No independent scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
