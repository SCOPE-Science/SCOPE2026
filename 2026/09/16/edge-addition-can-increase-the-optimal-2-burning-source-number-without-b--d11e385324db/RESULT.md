# Edge addition can increase the optimal 2-burning source number without bound

## Claim

For every integer q >= 1 there are connected finite simple graphs H and G on
the same vertex set, with E(H) contained in E(G), such that

\[
 t_2(H)=2,\qquad t_2(G)\ge q+2.
\]

Both graphs have a universal vertex and diameter two. The construction has
2+(q+4)(q+6) vertices. It also satisfies

\[
 b_2(H)=q+6,\qquad b_2(G)\le q+5.
\]

Here the synchronous threshold-two burning process starts with no blue vertices.
In round t, at most one source is made blue, and every vertex with at least two
neighbors blue at the end of round t-1 becomes blue. Blue vertices stay blue.
The parameter b_2 is the minimum completion round. The parameter t_2 is the
minimum number of sources among schedules completing by round b_2. Sources may
be taken in consecutive initial rounds, as in [1, Definitions 2.1-2.3]. Moving
sources earlier cannot delay activation, so permitting idle rounds gives the
same two optimum values.

Thus adding edges can increase the secondary optimum by an arbitrarily large
amount, even when the smaller graph has the minimum possible source number.
This disproves the t_2 assertion of [1, Lemma 2.4] in the inspected arXiv v2.
It does not contradict that lemma's valid assertion b_2(G) <= b_2(H).

## Construction and proof

Put k=q+2, L=k+2=q+4 and m=L+2=q+6. Take vertices a,c and, for
1 <= i <= m, distinct vertices x(i,1),...,x(i,L).
The edges of H are:

1. Every edge from a to any other vertex.
2. The edges c x(i,1), for all i.
3. The edges x(i,j) x(i,j+1), for all i and 1 <= j < L.

Equivalently, H is the cone over a spider with m arms, each of length L.
Construct G by adding c x(i,j) for k < i <= m and 2 <= j <= L.
The first k arms stay unchanged. Exactly four arms receive shortcuts.

**Unseeded-arm bound.** In either graph, consider an unchanged arm containing
no source in the schedule under consideration. Its last vertex cannot turn
blue before round L+2.

To prove the bound, the colored vertices in this arm always form a prefix
starting at x(i,1). Initially the prefix is empty. With no source in the arm,
an interior vertex beyond the next position has no blue arm neighbor and has
at most the one blue neighbor a outside the arm. The endpoint likewise cannot
activate ahead of this prefix. Hence at most the next prefix vertex can
activate in each round. To activate the first vertex when the prefix is empty
requires both a and c to be blue in the preceding round. At most one vertex
is blue after round 1, so this first activation is no earlier than round 3.
The j-th activation is therefore no earlier than round j+2, proving the bound.
This proof allows arbitrary choices of sources outside the arm, including
schedules in which a or c is activated through propagation.

**The smaller graph.** Selecting a in round 1 and c in round 2 colors every
x(i,j) by round j+2. Thus H finishes in round L+2 with two sources.
If a schedule finished H by round L+1, it would contain at most L+1 sources.
There are m=L+2 disjoint arms, so at least one arm would contain no source.
The unseeded-arm bound is a contradiction. Thus b_2(H)=L+2.
A single source never triggers a threshold-two activation in a simple graph,
so at least two sources are necessary. Consequently t_2(H)=2.

**The larger graph.** Select a in round 1 and c in round 2, followed by
x(1,L),...,x(k,L) in rounds 3,...,k+2=L.
All vertices of the four shortcut arms turn blue by round 3, because they
are adjacent to a and c. On each unchanged arm, x(i,j) for j < L turns blue
by round j+2 <= L+1, while its endpoint is explicitly selected by round L.
Thus b_2(G) <= L+1.

Every time-optimal schedule for G consequently finishes before round L+2.
The unseeded-arm bound forces that schedule to contain a source in each of
the k unchanged arms. Those arms are vertex-disjoint, so t_2(G) >= k=q+2.
Subtracting t_2(H)=2 proves the claimed gap.

The universal vertex a makes both graphs connected and of diameter at most
two. Vertices in two distinct unchanged arms are nonadjacent, so the diameter
is exactly two. This completes the proof.

## A small counterexample and reproducibility

A separate seven-vertex example uses vertices 0,...,6 and

```
E(H) = {01,03,04,06,12,14,15,24,25,26,36,56}
E(G) = E(H) union {05}.
```

Its exact pairs (b_2,t_2) are (4,2) for H and (3,3) for G. Optimal source
lists are (0,2) and (0,2,3), respectively. This is not claimed to be a
smallest counterexample.
Run `python3 artifacts/verify_burning.py` from the record directory. The script
uses only the Python standard library and actually checks:

- The seven-vertex values by two separately implemented exhaustive methods:
  dynamic programming on blue-vertex bitmasks, and enumeration of ordered
  source lists with set-based synchronous simulation.
- The formulas in [1, Theorem 2.8 and Observation 2.9] on paths and cycles
  of orders 3 through 9. All 14 computed pairs equal the cited formulas.
- The construction with k=1,L=3,m=5, for which the computed pairs are
  (5,2) and (4,2). This checks a boundary case without falsely claiming a
  positive source gap for every parameter choice.
- The explicit H and G schedules for q=1,...,30, including failure of the
  two-source H schedule to finish a round early.

All assertions passed. The infinite-family result rests on the proof above;
finite schedule checks are not presented as exhaustive optimality checks on
the large instances. The exploratory search is in `artifacts/burning_probe.py`.

## Relationship to prior work

[1] introduces t_2 and in Lemma 2.4 claims monotonicity under spanning
supergraphs for both b_2 and t_2. Its proof transfers a schedule across an
edge inclusion. This proves the b_2 inequality, but a transferred optimal
schedule need not attain the new, smaller minimum time, so it does not prove
the t_2 inequality. Our construction makes that obstruction unbounded.

In equivalent constrained-optimization terminology, let F_J(T) be the minimum
number of sequential sources required to finish graph J by deadline T, or
infinity if this is impossible. Then t_2(J)=F_J(b_2(J)). Adding edges gives
F_G(T) <= F_H(T) at every *fixed* T, but does not give the inequality when
the two sides are evaluated at their respective earliest feasible deadlines.
If b_2(G)=b_2(H), the original t_2 monotonicity conclusion does hold by the
same schedule-transfer argument. The changing deadline is essential here.

The closest applicable established construction tool is [1, Proposition
2.12, p. 6]: after seeding a dominating set, the remaining process can be
bounded by ordinary burning. Applied to our universal vertex, it explains
the threshold-one behavior on the spider. It does not force the number of
sources at the optimum completion time, which requires the unseeded-arm
bound and the selective shortcuts above. The known spider formulas in [1,
Theorem 3.1] concern spiders themselves, whereas our graphs are cones over
spiders and have no leaves. Observation 5.1 compares t_2 with minimum
bootstrap-percolating-set size but does not determine this temporal optimum.
Indeed both H and G admit a two-vertex percolating set {a,c}.

The value is a correction to a published comparison principle and a precise
unbounded example of the difference between minimizing interventions and
minimizing interventions subject to fastest completion. This is a short
mathematical result, not a claim of a broad classification or new general
algorithm. Exact values of b_2(G) and t_2(G) throughout the family are not
claimed. No other theorem of [1] is declared false merely because it cites
Lemma 2.4.

## Originality scope and inaccessible sources

To the best of our knowledge, within the documented search scope and accessible
literature, no equivalent or stronger prior result was found. This is not an
exhaustive guarantee of novelty.

Searches covered the named parameter, spanning-subgraph monotonicity,
corrections and counterexamples, sequential target-set selection, timed
threshold diffusion, and graph joins with a universal vertex. The equivalent
fixed-deadline formulation was checked against the accessible definitions
and schedule-transfer proof, and broader sequential-diffusion terminology
was searched. Several final searches timed out; those are not negative
evidence. Evidence identifiers and exact limits are recorded in REVIEW.md.

The most plausible inaccessible related source identified is Yinkui Li,
Xiaoxiao Qin and Wen Li, *The generalized burning number of graphs* (2021),
DOI https://doi.org/10.1016/j.amc.2021.126306. It treats the parent process and
graph operations, so a related construction or tradeoff is possible. DOI and
exact-title acquisition attempts did not yield usable full text. Its full text was not obtained through
available channels; its theorems and proofs remain unverified. This is an
ACCESS_LIMITATION with possible relevance, not a specific claim of coverage.
The accessible 2024 paper describes t_2 as its new parameter, but that is
not proof that an equivalent formulation was absent earlier.

The DOI request for [1] returned the same arXiv v2; a separate publisher
revision was not inspected. Claims about the erroneous lemma are therefore
explicitly tied to that version. A later correction or covering result would
require revising this originality assessment.

## Reference

[1] C. B. Jacobs, M. E. Messinger and A. N. Trenk, *The 2-burning number of a
graph*, Ars Combinatoria 161 (2024), DOI https://doi.org/10.61091/ars161-16;
inspected version https://arxiv.org/abs/2411.02050v2 (13 November 2024).
