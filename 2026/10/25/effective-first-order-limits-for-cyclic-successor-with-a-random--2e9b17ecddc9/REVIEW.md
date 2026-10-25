# Scientific review: effective first-order limits for a random matching on a directed cycle

## Correctness (PASS)

Each set of \(b\) disjoint prescribed matching edges has probability \(\prod_{j=0}^{b-1}(N-(2j+1))^{-1}\). The directed-successor-path embedding count is \(N^k+O(N^{k-1})\) for a core with \(k\) matching edges and \(k\) directed paths. Dividing by the coloured automorphism group gives the proposed mean. Distinct overlapping coloured cycles have excess at least one, hence their factorial-moment contributions vanish as \(O(N^{-1})\). Joint independent Poisson limits follow by factorial moments. Distance-separated short cores and an abundant unique cycle-free rooted-ball type satisfy the hypotheses of effective bounded-degree Hanf locality. The converse is obtained using finite embedded cycle diagrams and asymptotic separation. Rational Poisson means imply the exponential field constraint, and a family of independent mean-one chord counts yields density of the complete spectrum. The checker corroborates but does not replace the proof.

## Originality (PASS, subject to stated historical-priority risk)

Paguyo (arXiv:2104.01134, Sections 1.1, 3, 4.1) already proves the fixed-length short-chord Poisson marginal and attributes the more general single-length marginal to Acan; neither is presented as original. Acan (arXiv:1501.01489, Sections 2–6) studies chord intersection graphs, not the first-order limit spectrum in a named successor-and-involution language. McKay, Wormald and Wysocka (DOI 10.37236/1819, Theorem 1) treat uncoloured short cycles of uniformly random regular graphs, not a planted directed Hamilton cycle with a random matching. Dolan and Lynch (DOI 10.1002/rsa.3240040404) treat full-order random matching structures and report nonconvergence; the full text was inaccessible and the abstract does not decide this successor-only case. Koponen (arXiv:2610.16163, Introduction and Remark 2.15) motivates random expansions, but does not prove this concrete law. A potentially stronger general theorem for random edge-coloured configuration models remains a material historical-priority risk; semantic search alone does not resolve it.

## Value (PASS)

The result identifies a sharp logical-language boundary in a canonical random chord model: a prescribed cyclic successor plus a random perfect matching has an effective first-order convergence law, with a complete and dense limiting probability spectrum, while existing work on its fully ordered counterpart reports nonconvergence. The joint coloured cycle-core process and exact automorphism-normalized Poisson intensities provide structural rather than merely individual-chord information; they support a decision algorithm for arbitrary fixed first-order sentences.

## Limits

Only even sizes, a uniformly sampled perfect matching, and a named *directed immediate successor* are included. The method does not include full linear order, chord crossing, or growing quantifier rank. The literature comparison is bounded by accessibility of Dolan–Lynch full text and by possible stronger general prior theory. The published papers are not reproduced.

Self-review: passed. Independent audit: not yet performed.
