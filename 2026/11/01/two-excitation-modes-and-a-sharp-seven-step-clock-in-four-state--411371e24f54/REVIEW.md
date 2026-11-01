# Scientific review

## Correctness — PASS

The eight-class capping lemma is proved by induction: identical initial vertices on one shore evolve identically, and the threshold at two depends on population counts only through truncation at two. `cap_certificate.py` exhaustively checks every \(3^8=6561\) exact quotient signature, including all boundaries, periodic-state shapes, the global iterate identity, and the size-feasibility phase diagram. `direct_check.cpp` separately enumerates 4,657,408 labelled configurations over ten graph sizes and checks recurrence and first-entry histograms. The coefficient basin formula follows from exact labelled exponential generating functions and has an independent weighted check. Finite checks alone would be insufficient without the class-capping lemma, which is what transfers the exhaustive result to every graph size. Critical computational dependencies are fully supplied.

## Originality — PASS (best-knowledge qualification)

Actual semantic mathematical-record queries compared four-color threshold-two GHM, complete bipartite recurrence, contact-threshold dynamics, and aliases (four-phase excitable networks). The closest published record on complete multipartite parity automata uses a **binary linear parity update**, not a thresholded four-state refractory map; the irreversible multipartite threshold-conversion record is monotone and cannot imply recurrent four-cycles. The closest accessible pre-existing biclique result treats three-state threshold-two GHM, while a four-state biclique classification concerns excitation threshold one. Neither statement entails the two families, orbit count or seven-step transition for four-state threshold two.

Primary full-text comparisons: Fisch–Gravner–Griffeath study planar multicolor/threshold excitability rather than exact biclique orbit counts; Gravner–Lyu–Sivakoff study three-color excitation; Bello–Sivakoff treat infinite regular trees. A separate numerical sequence match in OEIS A132813 is an unrelated binomial triangle, not the present two-parameter dynamics. The original Greenberg–Hastings 1978 source was inspected at abstract level only; no unsupported negative claim is made about its full text. Unindexed or inaccessible equivalent results remain a historical-priority risk. Novelty is necessarily best-knowledge, not a uniqueness certification.

## Mathematical value — PASS

The threshold of two contacts is a natural cooperative-excitation modification of a classical excitable-media update. A complete labelled recurrence classification for all biclique shore sizes distinguishes two disjoint mechanisms, with sharp four-vertex and eight-vertex occupancy thresholds, and an unexpected seven-step entrance barrier that first occurs at the asymmetric \((7,8)\) size. The finite coefficient formula also determines all transient-length and eventual-period basins, not just recurrent states. This is a motivated complete infinite-family classification rather than a routine parameter substitution or an isolated numerical record.

## Limits and closest antecedents

Only the specified four-color, threshold-two deterministic update on finite bicliques is covered. Existing multistate excitation literature establishes the update model and broader behavior in other settings; the present claims are precise biclique combinatorial/dynamical formulas. An equivalent unindexed source remains possible and independent verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
