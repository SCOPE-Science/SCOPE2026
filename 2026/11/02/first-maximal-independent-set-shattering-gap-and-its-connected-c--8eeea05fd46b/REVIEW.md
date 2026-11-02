# Review of the first maximal-independent-set shattering gap and its connected-cograph amplification

## Correctness — PASS

The cograph \(K_2\vee(K_2\sqcup K_1)\) has precisely four maximal independent sets, explicitly listed and checked. Its VC dimension is one because its only two-coordinate supports with an all-positive trace lack a required singleton trace; its Littlestone dimension is two because a query at the isolated-in-the-second-module vertex splits its hypotheses into two distinguishable pairs. The connected construction adds a universal vertex to the disjoint product of \(m\) copies. Its hypothesis count is \(4^m+1\), so the entropy ceiling gives Littlestone dimension at most \(2m\), matching concatenated depth-two witnesses. Its VC dimension is exactly \(m\), by a blockwise shattered support and the impossibility of all nonempty traces on any two coordinates within one block. The finite first-order and isomorphism classification is complete: two separate standard-library implementations exhaust all labeled graphs through five vertices, producing 90 gap graphs in two isomorphism classes.

## Originality — PASS under the accessible comparisons

The 2021 full text of Bassino and collaborators examines independent sets and random cographs, supplies the cotree join/disjoint-union structure, and specifically distinguishes a possible analysis of *maximal* independent sets. Ghazi and collaborators' 2020 preprint/2021 conference paper treats general closure bounds for Littlestone dimension; its inspected propositions do not calculate graph-specific maximal-independent-set dimensions. Searches also considered independent dominating sets, minimal vertex covers, P4-free graphs, and general online learning. Neither equivalent exact five-vertex boundary nor the explicit connected-cograph gap formula was located. Prior exact forest and cycle classifications do not contain the present joined cograph family. No search can certify absolute historical novelty; equivalent formulations and obscure tabulations remain possible.

## Mathematical value — PASS

The first strict example is found at the smallest possible graph order, with a complete two-type isomorphism classification. One minimal example is already a connected P4-free graph, and an exact join/union construction amplifies its gap from one to \(m\) in connected cographs. This identifies an unexpected unbounded online-learning disadvantage in a structurally tame hereditary graph family rather than merely reporting a small isolated numerical invariant.

## Limitations

No exact formula is asserted for arbitrary cographs or for graph orders beyond the completely classified smallest boundary. The full connected family has a mathematical proof independent of finite experimentation. Historical-priority checking is not exhaustive, and no independent scientific audit was undertaken.

Self-review: passed. Independent audit: not yet performed.
