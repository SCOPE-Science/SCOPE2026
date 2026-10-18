# Independent mathematical audit

## correctness

PASS

Follow each of the n initial states. Each a increments modulo n; each effective b encountered at state n−1 also increments the state modulo n. A reset word with A cyclic letters must have pairwise distinct event-count residues B_i mod n, since final state equals i+A+B_i mod n; hence one initial state experiences at least n−1 effective b events. Between successive events it must encounter at least n−1 a letters (the only letter moving it from 0 toward n−1). Thus the specified W occurs as an unavoidable scattered subsequence. Direct image induction shows W reduces Q through S_j={0,…,n−j−1} to {0}; shortest length follows, and no distinct word of equal length can contain W. At one additional symbol every candidate is a single a or b insertion. Endpoint a insertions are good (2), doubled b sites are good (n−1), and in each of n−2 internal a runs all n−3 sites except t=j are good, giving n²−4n+7; n=2 handled separately. The boundary t=j cycle preserves final rank two. Independent separately coded subset-transition DP exhausted both length layers for n=2,…,9; shortest count=1 and excess-one counts all matched formula. An additional product-state BFS search n≤10 found no resetting word avoiding W; this is corroboration not proof for all n.

## originality

PASS

The Černý family and the known optimal (n−1)^2 reset length are classic, not claimed. Volkov 2022 survey details the automaton and classical threshold proof but not an all-reset-word scattered subsequence theorem or one-step multiplicity count in inspected Chapter 3. The 2013/15 Kisielewicz–Kowalski–Szykuła shortest-word algorithms, published Resultary k-avoiding thresholds, and published Černý early deficiency profile address different quantifiers (lengths/avoided target sets). Mandatory W subsequence for every reset input and first-excess literal word count appear not implied by those, subject to substantial older-language combinatorics priority risk.

## value

PASS

Černý is a canonical extremal synchronizing automaton, and the result characterizes a necessary pattern shared by ALL reset inputs, not merely one shortest witness. The exact first-excess multiplicity quantifies one-symbol slack and distinguishes redundancy/multiplicity from classical reset threshold. The count is valid for arbitrary n and precisely the natural next-length layer, not an arbitrary finite instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
