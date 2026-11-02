# Scientific review

## Correctness — PASS

The result concerns one precise domain: indexed binary length-\(n\) words of Hamming weight two, circular factors, \(n\ge4\). The mandatory edges in the order-\(n-1\) de Bruijn graph have one incoming and one outgoing edge at every incident vertex and split into necklace-rotation cycles. A covering walk's residual edge multigraph is balanced. For residual total length at most \(n-2\), all residual simple cycles have periods at most \(n-2\), and Fine–Wilf prohibits distinct residual cycles from sharing a length-\(n-1\) vertex. Every short residual cycle meeting the component of cyclically adjacent ones cannot leave that component through any other mandatory vertex, so the mandatory components cannot be connected. The matching \(n-1\)-edge cycle through all singleton-one vertices gives a connected balanced graph and an Eulerian cover. These two arguments independently establish matching bounds \(\binom n2+n-1\).

The included `verify.py` was actually executed and returned `VERIFY_OK`. It checks the complete multiset of circular windows of the constructed words for \(4\le n\le15\), enumerates and compares short residual periodic cycles for \(4\le n\le9\), and exhaustively excludes shorter circular words for \(n=4,5\). These finite tests support the derivation but do not replace its infinite proof. The proof correctly handles duplicated mandatory edges, residual loops, and the cyclic wraparound convention.

## Originality — PASS (qualified)

Blanca and Godbole's 2010 arXiv source (arXiv:1008.2251, Section 2, Theorem 4) is **the same covering problem** and gives an upper bound of \(\binom n2+n\) when specialized to weight two; it does not give the exact minimum. Ruskey, Sawada, and Williams (2012, DOI:10.1137/100808782, introductory definition and Section 2) work with shorthand length-\(n-1\) factors, so their length-\(\binom n2\) sequence does not supply the length-\(n\) factors required here. Dębski and Lonc (2016, DOI:10.1007/s00373-016-1727-6, Sections 1.1–1.2) explicitly distinguish their integer-alphabet subset coverings from Blanca–Godbole's binary encoding and do not derive this exact formula. Mitchell and Wild (2026, arXiv:2607.22350, Section 3) establish existence/connectivity for weight ranges and fixed-weight graph components, but do not optimize the shortest connected augmentation of those components. The debruijnsequence.org subset resource likewise describes shorthand and fixed-weight impossibility, not the exact covering number. Actual targeted searches of indexed mathematical research results and publicly searchable literature found no equivalent formula; prior local claims about Fibonacci-constrained and reversal-quotient coverings have different required languages, decoding equivalences, and/or linear/circular conventions.

Historical priority remains qualified by possible unindexed or inaccessible publications. A negative search does not establish uniqueness. The key originality comparison is at implication level: stronger shorthand coverage does not imply longhand coverage, and an existing upper bound larger by one does not imply an exact lower bound.

## Value — PASS

The task is a natural complete optimization introduced in the primary 2010 universal-covering work, rather than a deliberately selected slice. The exact all-order shortest length, elementary explicit Eulerian algorithm, and nontrivial short-period lower obstruction determine the optimal augmentation cost of a disconnected fixed-weight de Bruijn subgraph. Although the improvement over the earliest explicit construction is one symbol, identifying and proving the *sharp* minimum for every block length is structural information not supplied by correctness, code, or mere search. The result is a reusable exact benchmark for constrained cyclic windows.

## Limitations and related literature

No claim is made for weights other than two, linear superstrings, uniqueness of the optimum, or independently certified historical novelty. Critical primary passages read: arXiv:1008.2251, Section 2, Definition/Theorem 4; Ruskey–Sawada–Williams 2012, introduction and shorthand/longhand construction; Dębski–Lonc 2016, Sections 1.1–1.2; Mitchell–Wild 2026, Section 3; and the debruijnsequence.org subset resource. The Fine–Wilf theorem is used in the standard finite-word form.

Self-review: passed. Independent audit: not yet performed.
