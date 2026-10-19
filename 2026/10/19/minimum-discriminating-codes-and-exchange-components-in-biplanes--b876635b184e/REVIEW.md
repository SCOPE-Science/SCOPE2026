# Scientific review: minimum discriminating codes of biplanes

## Correctness — PASS

The theorem quantifies over every symmetric \(2\text{-}(16,6,2)\) design, rather than relying on a census of its three known isomorphism types. The lower bound is the exact nonzero binary-signature capacity inequality \(2^4-1<16\). At size five, three incidence moments and the uniqueness of singleton signatures force a single five-point trace, making every minimum code a block punctured at one point. Conversely, the design's pair multiplicity and dual pair intersections partition the other fifteen blocks into five singleton traces and ten doubletons. Distinct blocks share only two points, yielding exactly 96 codes and the exchange components \(16K_6\). The packaged verifier checks the incidence axioms and all 4368 five-point candidates for an explicit example; its evidence is corroborative, not a substitute for the universal proof.

**Risk/boundary:** Discriminating codes *require* nonempty traces. A weaker semi-resolving set need not hit every block; the statement does not classify that larger collection. No infinite family or ordinary metric-basis theorem is asserted.

## Originality — PASS, with residual risks

The closest antecedent is Bailey, *On the metric dimension of imprimitive distance-regular graphs*, Proposition 14 (arXiv:1312.4971), which proves that puncturing a biplane block gives a semi-resolving set. This already establishes the construction and is expressly credited. The newly evaluated claim is the **if-and-only-if classification for the stronger, standard discriminating-code condition**, plus the enumeration of 96 exact optima and their entire minimum-exchange graph. The published work of Charon--Cohen--Hudry--Lobstein on bipartite planar graphs defines precisely this discrimination problem, but its inspected full text analyzes trees and planar families, not the biplane classification. Tang--Zhou--Chen--Zhang address metric resolving sets of the full incidence graph, with differing vertex choices and inequalities, and do not directly imply the claimed nonempty one-side characterization from the inspected material. Relevant research-record searches using `discriminating codes`, `semi-resolving`, `identifying test sets`, `symmetric (16,6,2)`, and `exchange graph` found no covering proposition.

**Residual risks:** The complete PDF of Charbit--Charon--Cohen--Hudry--Lobstein's 2008 broad survey/bounds paper was not obtained after open-access and institutional-access attempts, although its abstract was inspected. The full text of the 2021 metric-dimension paper was also unavailable; the accessible abstract and section-five excerpts were read. These restrictions leave a possibility of an unrecognized stronger implication. Unindexed literature may also contain a code enumeration. None of the inspected *stated* results proves the converse or minimum exchange classification; a failed search is not treated as proof of novelty.

## Value — PASS

Discriminating codes formalize a natural simultaneous detection-and-identification problem for the incidence graph of a biplane. Classifying **every** optimum, not just constructing one, identifies which sensors are mathematically interchangeable. The surprising obstruction is global: all local one-point replacements remain within a fixed six-point block, leaving sixteen disconnected components. Because the proof uses only \((16,6,2)\) axioms, it applies uniformly to every realization of the classical biplane parameters. Exact classification and disconnectedness at the information-theoretic minimum constitute a structural result useful for studying fault detection and constrained reconfiguration of identifying sets, rather than an arbitrary table entry.

## External validation

Independent external review has not been performed; the reproducibility program gives only same-study finite verification in one instance.

Self-review: passed. Independent audit: not yet performed.
