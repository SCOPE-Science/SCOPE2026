# Scientific review — acyclic-orientation shattering gap

## Correctness (PASS)

The forest-extension argument proves \(\operatorname{VCdim}(\mathcal A(G))=|V|-c(G)\) for every finite graph. The classification of acyclic orientations of \(K_{2,3}\) as the union of two ternary cubes gives exactly \(46\) hypotheses. Since \(46<64\), depth six is impossible; a fully listed, replayed depth-five shattered tree supplies the matching lower bound. The additivity of VC and Littlestone dimensions on disjoint query domains is proved, and the constructed bridges do not occur in directed cycles. These steps yield exact dimensions \(5s-1\) and \(6s-1\). A second implementation verifies the finite certificate without invoking the first verifier.

Potential scientific risks: the standard optimal online mistake-bound characterization underlies the additivity proof, and the leaf-indexing convention must match the verifier. Both are explicitly stated and independently reconstructed. The main infinite-family statement is mathematical, not a claim extrapolated from computations.

## Originality (PASS; bounded checks)

Compared against direct acyclic-orientation-query research (Pikhurko 2009), generic Littlestone/tree-dimension results (Walker 2022; Pradeep–Nachum–Gastpar 2022), general dimension-computation hardness (Manurangsi 2023), relevant public research records, and earlier accessible comparison-class results. Pikhurko's \(c(G)\) measures worst-case adaptive **identification queries**, not adversarial **prediction mistakes**; a lower bound on identification queries does not yield a shattered binary mistake tree. The remaining general results do not establish the graph-specific \(46\)-hypothesis depth-five certificate or the exact connected planar subcubic amplification. Previous full-comparison results concern all pairs on a complete graph, and their restriction does not entail the depth-five lower bound for \(K_{2,3}\). No dominating result was found in the bounded searches. Historical priority remains uncertain because some relevant works or full texts may be unindexed or inaccessible.

## Mathematical value (PASS)

The obstruction is the smallest bipartite example where acyclic-orientation VC dimension and Littlestone dimension differ, and the qualitative distinction is structural: a single cycle cannot create the gap but the two overlapping four-cycles of \(K_{2,3}\) can. Bridge additivity amplifies the five-vertex certificate into an unbounded quantitative separation even among **connected planar maximum-degree-three bipartite graphs**. This answers a natural structural question about how a graphic-matroid VC rank can differ from adaptive shattering while retaining strong graph restrictions.

## Scope and outstanding validation

The exact graph-specific computation has independently replayable finite certificates. No assertion of a formula for arbitrary graph families, or of absolute publication priority, is made. The result is subject to independent proof review and wider literature checks.

Self-review: passed. Independent audit: not yet performed.
