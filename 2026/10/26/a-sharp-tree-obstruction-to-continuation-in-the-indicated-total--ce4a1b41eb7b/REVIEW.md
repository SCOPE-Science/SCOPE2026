# Scientific review

## Correctness — PASS

For the tree family defined in `RESULT.md`, the leaf constraints force the two support vertices \(b,d\) into every total dominating set, and the unique common neighbor \(c\) is required for a three-vertex set. This yields the unique possible optimum \(\{b,c,d\}\). The ordinary game forces precisely that set in three moves. Declaring \(f\) pre-dominated prevents Dominator from using it as an indication; Staller can then avoid the unique three-element total dominating set, forcing four moves. The matching upper bound indicates the two outer leaves and then the remaining undominated support vertices. Every first indication is considered in the proof.

The minimum-order and uniqueness statements are exact finite consequences of the supplied standard-library Python enumeration: Prüfer sequences cover all labeled trees of orders two through six, rooted canonical codes reduce them to \(1,1,2,3,6\) isomorphism classes, and the minimax recurrence checks all \(B\subseteq A\). The checker was executed successfully from its actual artifact path. Only this finite boundary uses enumeration; every \(r\geq0\) is covered by the mathematical strategies.

## Originality — PASS, residual bibliographic uncertainty

Henning and Rall, *Indicated total domination game*, arXiv:2310.03506v3, Section 2, prove failure of continuation using an eight-vertex graph with a cycle and two initially declared vertices. They do not state this smallest-tree uniqueness theorem or the all-order family with a single pre-dominated vertex. Their later question about ordinary game values on trees is distinct and remains unaddressed. The related *Indicated domination game* arXiv:2310.14647 uses a different closed-neighborhood rule. Searches of relevant indexed mathematical records and the inspected primary texts revealed no covering theorem. Priority outside those sources is not independently certified.

## Value — PASS

Failure of a domination-game continuation principle is a mathematically motivated obstruction because it removes a standard monotonicity tool. The proposed theorem supplies a sharp boundary, the unique smallest tree shape, and one-vertex failures at every larger order rather than simply another unstructured counterexample. It also clarifies that partial-game monotonicity can fail on trees even when an independent conjecture concerns the ordinary game on those trees.

## Limitations

The theorem does not bound the largest possible continuation gap for trees or classify larger counterexamples. Finite uniqueness is computer-assisted and reproducible; the infinite family is independently proved by explicit strategies. An unindexed or inaccessible equivalent result is a remaining priority risk.

Self-review: passed. Independent audit: not yet performed.
