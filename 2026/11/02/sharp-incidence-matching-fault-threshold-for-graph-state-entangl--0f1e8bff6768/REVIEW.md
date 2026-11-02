# Scientific review

## Correctness — PASS

The claim concerns any even-order projective plane and a matching of at most \(q+1\) omitted incidence gates. The standard stabilizer rank formula reduces entropy to \(\mathbb F_2\)-rank. A direct geometric parity argument proves the distance and complete minimum-word classification of both incidence codes without coordinatization. The exact augmented-matrix rank identity then handles all three configurations of deficiency, including the simultaneous line-and-pencil case; the matching requirement rules out a possible additional cancellation. Explicit constructions show both critical outcomes. The Desarguesian baseline is independently derived from a finite-field monomial factorization. The self-contained algebra, parameter endpoints, quantifiers, and equality cases have been reconstructed; the finite checks in `VERIFY.py` agree with the closed formula.

## Originality — PASS on examined evidence, with residual risk

The individual ingredients—the graph-state cut-rank relation [1], binary incidence minimum words [2], and relevance of projective-plane incidence graphs to quantum resource states [3]—are established and expressly credited. Relevant full text was examined for all three; [1] has general one-edge deletion bounds, [2] classifies minimum-weight codewords without discussing quantum preparation-gate faults, and [3] concerns vertex minors and pairability, not the matching-deletion entropy classification. The added claim is the *sharp all-plane endpoint geometry iff*, including the case where both endpoint classes are singular and the dependency does not double. Binary-matrix rank variants of the statement could exist under other terminology. General bounds and minimum-distance alone do not state the necessary and sufficient threshold and would not by themselves resolve the simultaneous-deficiency case. Independent historical-priority verification is still outstanding.

## Mathematical value — PASS

Projective-plane incidence graphs are studied as finite quantum entanglement resources [3]. The finding gives a placement-independent exact tolerance regime for disjoint failed preparation gates, then the exact geometric condition for the first failure of independence; the two realizable outcomes at the threshold distinguish structurally significant faults. It applies to arbitrary even-order planes, not merely tested finite examples or a single graph, and provides a quantitative entanglement benchmark. No bulk physical phase-transition or noise-robustness claim is made.

## Risks and scientific limits

Specific older binary incidence-code and newer finite-geometry quantum graph-state literature could contain a disguised or stronger matching-fault theorem; it was not possible to establish universal historical priority. The 1985 coding result already proves the classical minimum-word component for Desarguesian planes. Computational tests cover Desarguesian orders \(2,4,8,16\), not non-Desarguesian examples, for which the general geometric proof applies. Every current verification step is internal to this result and does not amount to independent audit.

Self-review: passed. Independent audit: not yet performed.
