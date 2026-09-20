# Same-model scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof divides according to whether a one-edge maximal matching exists. If none exists, every maximal matching has size at least two and the claimed lower bound is immediate. If `{uv}` is maximal, then `uv` is an edge-dominating edge, so every edge is incident with `u` or `v`. Partitioning the remaining vertices into private neighbors of `u`, private neighbors of `v`, and common neighbors gives the exact cyclomatic identity `r=|N(u) cap N(v)|`. Because `r>=2`, `uv` is the unique one-edge maximal matching. Every other maximal matching has size two, and exact counting gives `t=ab+r(n-3)` such matchings, hence `avm=2-1/(ab+r(n-3)+1)`. The lower bound and equality condition `ab=0` follow immediately. The equality graph has the required order and cycle rank, and swapping the two endpoints shows uniqueness up to isomorphism.

Exact finite enumeration over all connected Graph Atlas graphs of order at most seven agrees with both the value and uniqueness for every parameter pair in the sharp range. The computation is supporting evidence only; the proof is symbolic.

## Originality

**PASS, to the best of our knowledge.** Engbers and Erey (2023) initiated extremal questions for the average size of maximal matchings and asked for extensions from unicyclic to k-cyclic graphs. Zhang (2026) explicitly quotes that question and solves the bicyclic minimum, obtaining `(4n-11)/(2n-5)` with the unique two-page-book extremal graph. Substituting `r=2` in the present theorem recovers that value and structure. Zhang's paper uses the size-one/dominating-edge observation inside its bicyclic case analysis but does not state the cyclomatic identity or an all-r lower bound.

Searches using exact and synonymous terminology for average maximal matching size, tricyclic/k-cyclic graphs, cyclomatic number, book graphs, dominating edges, and independent domination in line graphs did not locate the present formula or equality classification. The August 2026 follow-up by Zhang concerns the bicyclic maximum rather than the all-r minimum.

The full text of Engbers and Erey (2023) was not inspected in this review. Its bibliographic scope and the relevant open extension were checked through Zhang (2026), which quotes the question. This is the most relevant inaccessible source capable of affecting originality. Residual risk also remains from differently indexed or very recent work.

## Value

**PASS.** The result replaces a core-by-core analysis by a general structural mechanism and yields the exact minimum for every cyclomatic number `r>=2` throughout the range `n>=r+2`. Thus it extends the known bicyclic minimum simultaneously to all fixed higher cyclomatic numbers, including an explicit tricyclic formula and a unique extremal family. The result directly advances the minimum side of the stated k-cyclic extension problem.

## Evidence and limitations

The lower bound is universal for connected graphs with `r>=2`, but exact fixed-parameter optimality is asserted only when `n>=r+2`. The denser range `n<r+2`, where a dominating-edge equality graph cannot exist, is not classified. The maximum side is not addressed. Finite enumeration does not replace the proof. Originality remains to the best of our knowledge subject to the access and indexing limitations above.
