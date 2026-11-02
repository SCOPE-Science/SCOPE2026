# Scientific review

## Correctness — PASS

The statement is restricted to binary linear words and exactly one deletion. An explicit syndrome-difference calculation proves that any clique of the confusability graph has at most \(n+1\) vertices. A two-common-supersequence lemma proves that at least three selected superstrings of one read share no alternative common read. Base examples of sizes four, five, and six are checked from literal deletion sets. The recursive construction appends an alternating bit, adds one new insertion-neighborhood word, and maintains an exceptional word sharing a read with every member while excluding the global common read. The induction is valid for every integer \(n\ge5\). The standalone verifier checks lengths through \(250\) and validates the two structural lemmas on finite test ranges. These checks are corroborating, not an infinite proof.

## Originality — PASS, qualified

Sloane [1] gives the single-deletion graph model and classical checksum-coloring bound. Nguyen, Cai and Siegel [2] optimize deletion-correcting codes and encoders, not pairwise-confusable cliques with empty common descendant. Wang and collaborators [3] work with a different permutation/Ulam graph and triangle counts, rather than repeated-symbol binary length-\(n\) words. Relevant public-repository records on the exact binary one-deletion triangle count and a two-read reconstruction edge count provide graph statistics but not a maximum non-Helly clique construction. Statement-level comparisons find no implication of the new sharp saturation phenomenon. Residual risk: a differently named Helly/intersection theorem or unpublished construction could cover it; the literature search is not a uniqueness certificate.

## Mathematical value — PASS

One-deletion ambiguity is an intersection-hypergraph problem: pairwise consistency is sometimes mistaken for a single shared candidate read. This theorem shows failure at the absolute maximum possible size of a confusable family at every length, not just in small sporadic counterexamples. The sharpness and elementary recurrence supply a useful structural obstruction when replacing read incidence with a pairwise conflict graph. The exact extremal theorem is motivated independently of any particular finite data table.

## Source and interpretation risks

The verification results do not determine uniqueness or a full extremizer classification. The graph-theoretic maximum \(n+1\) follows from old checksum ideas; only the sharp missing-global-read witness is asserted beyond them. A matching result could be hidden under alternative terminology (e.g. deletion neighborhoods, graph cliques, Helly property).

Self-review: passed. Independent audit: not yet performed.
