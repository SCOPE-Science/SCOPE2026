# Review

## Correctness
PASS. The proof reduces the Roman condition to the location of label \(2\) across multipartite parts. Each of the three support cases is exhaustive and disjoint. The product-sum enumerator follows by direct generating-function counting. The minimum-weight formulas are obtained by exhausting the lowest possible weight patterns in those same cases. The packaged verifier independently enumerates all \(3^N\) assignments for every complete multipartite type through order \(10\) and matches the full coefficient vector.

## Originality
PASS, with residual indexing risk. The foundational Roman-domination paper defines the invariant and proves general properties but does not enumerate all functions on complete multipartite graphs. The 2018 forcing-Roman paper has a directly relevant complete-multipartite theorem, but its target is the forcing number of minimum-weight \(\gamma_R\)-functions; inspection of the complete-multipartite section shows minimum-function constructions, not an all-weight polynomial. A 2025 Roman-domination-polynomial paper confirms that the all-weight enumerator is a natural named object, but studies commuting and non-commuting graphs of dihedral groups. Targeted published-finding corpus and web searches found no equivalent complete-multipartite polynomial or stronger theorem implying it.

## Value
PASS. The finding converts a local domination constraint into a complete structural classification of all \(3^N\) labelings on an arbitrary multipartite shape, giving every weight coefficient at once. It strictly refines knowledge of the minimum Roman domination number by also counting all minimum functions and all higher-weight functions, and it specializes uniformly to complete graphs, complete bipartite graphs, stars, and Turán graphs.

The main residual risk is bibliographic: an older or poorly indexed source may contain an equivalent enumerator under different terminology. This risk is recorded explicitly and is not treated as proof of novelty.

Same-model review: passed. Independent audit: not yet performed.
