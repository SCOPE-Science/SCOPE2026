# Scientific review: prism majority fixed-point spectrum

## Correctness — PASS

The fixed-state condition is exactly two agreeing neighbors among three. A single mismatched rung forces both horizontal neighbors on each layer to agree with its endpoint, which inductively forces every rung to share the same ordered mismatch. A matched rung already supplies one agreeing neighbor, leaving the necessary-and-sufficient condition of no solitary cyclic column. These mutually exclusive alternatives exhaust every binary configuration. The blue-count formula uses a marked blue-run start and two compositions with parts at least two; the factor of \(1/r\) corrects exactly \(r\) marked starts per labeled word. The transfer-matrix trace counts independent transition edges at \(z=\pm1\), giving the exact Lucas and cosine total. Independent exhaustive finite-state tests and checks of every composition total through \(n=200\) passed. Finite enumeration is corroboration, not the argument for infinitely many prism sizes.

## Originality — PASS, subject to residual literature risk

The earliest identified motivating source is Zehmakan's arXiv:2302.06760v1 (14 February 2023), with expanded journal publication in 2024. It characterizes fixed states of degree-two cycles and supplies their asymptotic number, not an exhaustive cubic-prism classification or the blue-opinion spectrum. Its appendix has a *synchronized-trajectory embedding* into odd-degree doubled networks, which implies the existence of an included subset of states but does not exclude partially mismatched rungs or supply the complete size-refined count. The new mismatch-rigidity lemma is the step that makes the prism enumeration exhaustive. Arkhipov's arXiv:2406.07026v1 explains the internal-partition equivalence on regular graphs but provides simulations of random regular graphs, not a prism formula. Index and literature searches for prism fixed states, internal cuts, stable binary opinion configurations, and Ising metastability did not locate the asserted exact size distribution. Equivalence to a known broader transfer-matrix/Ising enumeration cannot be excluded, and searches do not establish absolute priority.

## Value — PASS

This is a natural complete classification of a specified infinite family of connected, cubic, vertex-transitive social networks, a case distinguished from cycles because degree three removes tie-breaking altogether. It resolves all labeled absorbing singleton states, including the exact number at each opinion balance. The spectrum exposes a fixed-state parity restriction and proves a sharp four-person minimum size for a nonempty persistently present color group on all prisms beyond the triangle. It also gives exponential coexistence-pattern abundance on the simplest degree-three vertex-transitive cycle extension, despite the two-only stable states of random majority on the underlying degree-two cycle. The enumeration is not a parameter renaming or a single finite table. It does not establish basins of attraction, typical dynamics, other regular graph families, or metastable two-cycles.

## Closest coverage and remaining limits

The cycle stable-coloring theorem and no-singleton characterization are previously known and acknowledged. The new claim is limited to the cubic prism's exhaustive classification, size-refined enumeration and consequences. A similar count could exist under the terminology internal partitions, Ising blocked configurations, or zero-temperature spin-flip stability. No independent audit or independent priority confirmation is asserted.

Self-review: passed. Independent audit: not yet performed.
