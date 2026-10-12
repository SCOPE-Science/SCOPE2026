# Scientific review

## Correctness — PASS

For the full domain of finite clique bouquets, positive spoke/internal-edge prices, and budget one, uniqueness follows from strict convexity of the inverse-Laplacian trace together with injectivity of the edge-to-Laplacian map. Symmetry then reduces each petal to two weights. The weighted-clique resistance identities and the one-hub cut decomposition give the exact separated Kirchhoff objective. Differentiating the dimensionless block objective yields the sharp price cutoff, including equality and the possibility of expensive internal edges receiving exactly zero conductance. Cauchy--Schwarz gives the unique global expenditure shares and the claimed objective. The standard-library checker verified 217 exact rational Kirchhoff identities and 700 heterogeneous allocation cases, plus 2,100 numerical feasible comparisons. The universal result does not rely on finite enumeration.

## Originality — PASS, with residual risk

The closest general source is Ghosh, Boyd, and Saberi (2008), which proves convexity and treats certain homogeneous graph families but does not give the heterogeneous clique-bouquet decision rule or the cutoff independent of clique size. Kooij (2019) gives spectra and other metrics on windmill graphs without solving conductance-price optimization. The available abstract of Sardar and Xu (2024/2025) concerns unit-resistor windmills; its complete text could not be inspected through the available lawful channels. Published-result searches for weighted bouquet, windmill, price deletion, cut-vertex reductions, and exact optimal Kirchhoff tables found no statement shown to imply the new all-block theorem. These searches do not prove novelty; a hidden historical specialization is a genuine remaining risk.

## Value — PASS

The model describes networks built from multiple internally redundant clusters connected through one shared terminal. The result resolves the complete nonnegative resource-allocation problem for arbitrary cluster sizes and pairwise distinct positive costs, not a finite test instance or an artificial numerical slice. Its structurally non-obvious statement is a **single identical purchase cutoff for all clusters** despite their heterogeneous sizes and prices, together with a precise rule for how to redistribute the global budget across clusters. This is useful whenever one must decide whether to retain expensive intracluster redundancy versus spend only on access to the shared terminal. The theorem specializes to weighted windmills and heterogeneous friendship graphs but is not a fixed-weight graph-index recomputation.

## Closest literature and limitations

A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1) (2008), DOI 10.1137/050645452; R. E. Kooij, *On generalized windmill graphs*, Linear Algebra and its Applications 565 (2019), DOI 10.1016/j.laa.2018.11.025; M. S. Sardar and S.-J. Xu, *Resistance Distance and Kirchhoff Index in Windmill Graphs*, Current Organic Synthesis 22(2) (2025), DOI 10.2174/0115701794299562240606054510. The classification does not extend without proof to graphs with cross-cluster edges or heterogeneous individual prices within a cluster. Independent audit and exhaustive historical novelty verification remain unperformed.

Self-review: passed. Independent audit: not yet performed.
