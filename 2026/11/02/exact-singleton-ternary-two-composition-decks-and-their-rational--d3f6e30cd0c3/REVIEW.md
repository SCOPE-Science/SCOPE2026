# Scientific review: exact singleton ternary two-composition decks

## Correctness — PASS

The source object is a noncyclic word of known length \(m+1\), and the observation is its six multiplicity counts of unordered contiguous length-two pairs. Translating the observation into an undirected looped multigraph is exact. Connectivity is necessary and sufficient for Euler-trail realization on at most three active vertices because the handshaking lemma excludes four odd-degree vertices. The proof separates all four ordinary-edge-support sizes, then checks distinct reversal orbits of Eulerian vertex skeletons and whether loop placements at repeated visits create additional realizations. Every term of the singleton generating function corresponds to one disjoint family. The total-deck enumerator provides a separate cross-check and implies the claimed asymptotic ratio. The standalone verifier enumerated all \(797{,}160\) ternary words through length \(12\) and agreed on the unique-fiber predicate and both counts at every tested length.

**Limits and risk:** Computation does not certify all lengths; the full proof depends on the loop-placement and excursion-swapping arguments, which are explicitly reconstructed in `RESULT.md`. The word of length one has one deck but three realizations and is excluded from the positive-length-edge singleton formula.

## Originality — PASS, with residual risks

The 2022 Ye–Elishco paper introduces length-limited composition observation but does not provide the ternary length-two singleton classification; its relevant full-text sections were inspected. A previously reported exact binary two-multispectrum result characterizes singleton profiles only for two letters. The exact quaternary unordered-bigram count addresses total realizable observations rather than the uniqueness of individual ternary fibers; the exact ternary ordered-bigram count retains pair orientations, changing the observation. These are not assertions of blanket novelty: both the graph-theoretic Euler criterion and their generic counting techniques are established, and the auxiliary ternary total-deck census is a direct application. The new claim is specifically the complete ternary singleton classification and its rational, parity-sensitive enumeration.

**Limits and risk:** General graph-theoretic unique-Eulerian-trail results may subsume the classification without the present vocabulary, and accessible record summaries do not substitute for full-text exclusion. No independent priority certificate is claimed.

## Mathematical value — PASS

A ternary readout is the first genuinely nonbinary case of unordered digram-composition reconstruction. At this alphabet size, arbitrary graph-degree parity becomes automatic but exact uniqueness is still constrained by a nontrivial interaction between repeated traversals, loops and reversal. The classification gives an implementable test on just six counts for whether a fragment-composition read has a unique source up to reversal, and the generating function gives exact availability of such profiles at every length. The scarcity law \(U_m/H_m\sim180/m^3\) quantifies how such uniquely decodable observations become sparse as lengths increase. This is a complete natural classification rather than a collection of finite values or an arbitrary numerical slice.

**Limits and risk:** It does not improve error-correcting codes or yield a decoding theorem for noisy reads. Practical significance depends on the accuracy of the exact adjacent-composition observation model.

Self-review: passed. Independent audit: not yet performed.
