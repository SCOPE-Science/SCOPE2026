# Scientific review: first unsolvable perfect-roommate Pareto separation

## Correctness — PASS

Takahashi's Definition 1 was checked against the full source text, including the equivalent two-condition formulation for domination. The four-person part reduces to the established complete two-orbit unsolvable classification and the elementary fact that each of its three perfect pairings has a different singleton blocking-pair set. Takahashi's Lemma 1 prohibits domination between those pairings. The six-person upper bound follows from a direct cross-pair parity argument, characterization of all nine Pareto optima, and exhaustive classification of possible blocking-neutral dominators after one adjacent preference reversal. These steps prove six is the first possible even order. The standalone script enumerates every one of \(1296\) four-person strict preference profiles and checks all fifteen perfect matchings in each specified six-person profile; all assertions passed. No random sample is used as an exhaustive proof.

## Originality — PASS with residual priority risk

Takahashi, *A Solution to the Roommate Problem* (arXiv:2608.11682v1, 2026), introduces blocking-neutrality, proves existence and its relation to stability and Pareto optimality, and gives separate three- and eight-person examples. Its inspected primary full text does not state this sharp six-person separation **conditional on nonexistence of a stable perfect matching**, the exact six-versus-nine count, or the one-adjacent-swap transition. The published four-person stable-roommates census determines the two unsolvable isomorphism classes and \(48\) labeled profiles, but makes no blocking-neutral claims. Searches of relevant published mathematical records and accessible research ledgers identified no exact equivalent. The general inclusion theorem and four-person stability census do not jointly imply the six-person witness. An unindexed treatment of this restriction remains possible.

## Value — PASS

The finding identifies the first population size at which a recently introduced stability fallback is *strictly more selective than Pareto efficiency* after stability fails, under natural compulsory perfect-pairing feasibility. The one-adjacent-swap example shows that the additional selection is substantively distinct from Pareto optimality: the Pareto set remains of size nine while the blocking-neutral set shrinks from nine to six. It is a sharp motivated boundary, not an arbitrary enumeration of unrelated parameter values. The claim is not extended to markets with singles, arbitrary feasibility constraints, or weak preferences.

## Closest literature and limitations

The main mathematical prior source is Meina Takahashi (2026), https://pdfs.assets.alphaxiv.org/2608.11682v1.pdf (Definition 1, Lemma 1, Theorems 1–3 and Examples 1–3). The four-person classification is https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-stability-stratified-isomorphism-census-for-four-person-stable-r--0bfa73dccf63. The independent four-person census and witness-specific six-person checks are replayable with `python3 verify_bn.py`. No general six-person population census or independent scientific audit is claimed. Remaining originality risk concerns unindexed computational notes or equivalent constrained-roommate examples.

Self-review: passed. Independent audit: not yet performed.
