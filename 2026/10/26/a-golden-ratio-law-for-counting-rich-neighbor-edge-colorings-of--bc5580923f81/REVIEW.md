# Scientific review: rich-neighbor cycle-coloring enumerator

## Correctness — PASS

The sign encoding is bijective up to the three choices of initial named color, and a closed 24-state matrix walk accounts for precisely that factor. The four-sign local condition matches total domination of the rich-edge set, including the nontrivial requirement that a rich edge itself have an adjacent rich edge. The characteristic polynomial factorization was reproduced by exact integer Newton identities from the actual finite matrix. The directed graph is strongly connected with coprime closed-walk lengths three and five, so its Perron root is simple and strictly dominant. The degree-eight factor is positive on the real interval from the golden ratio upward, proving that the Perron root is the golden ratio. The trace asymptotic has leading coefficient one. The attached direct exhaustive 3-color checks for cycle lengths three through ten agree with the trace values. Risk: an implementation transcription error remains possible, but the matrix definition, proof and independent short-length enumerator permit reproduction without a computer algebra system.

## Originality — PASS, subject to bibliographic limits

Kashima et al., arXiv:2610.16446v1, Proposition 2, directly covers cycle three-colour *existence* and four-colour exceptions: this earlier result is credited, not repackaged. Kong, arXiv:2610.21036v1, addresses general bounds and complete/complete bipartite exact chromatic indices, not the cycle coloring-count sequence. Chen–Tan–Zhou (2025) concerns upper bounds for subcubic graphs. Targeted literature and mathematical-record searches did not locate an exact counting formula or a golden-ratio asymptotic for rich-neighbor cycle colorings. A related published enumeration for other coloring notions does not imply the present local-richness filter. The 2024 originating article could not be read in full; the absence of that comparison is a residual priority risk, not evidence of uniqueness.

## Value — PASS

Once minimum palette existence is known, the exact number of optimal named colourings is the next natural counting invariant: it measures their availability and rarity. The result gives a complete infinite enumerator and an unexpectedly sharp exponential growth constant (the golden ratio), compared with the \(2^n\) growth of all proper three-colourings. The transfer formulation also supports exact counts at arbitrary lengths, rather than a finite table or a routine single substitution. Limitations: it does not count colorings using four or more colors or dihedral equivalence classes.

Self-review: passed. Independent audit: not yet performed.
