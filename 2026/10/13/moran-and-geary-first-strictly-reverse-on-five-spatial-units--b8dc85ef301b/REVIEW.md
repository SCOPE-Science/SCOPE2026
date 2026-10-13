# Self-review

## Correctness
**PASS.** The weighted squared-difference identity gives
\[
C=\frac{n-1}{S_0}\frac{\sum_i d_i z_i^2}{\sum_i z_i^2}-\frac{n-1}{n}I.
\]
On an \(r\)-regular graph this reduces exactly to \(C=(n-1)(1-I)/n\). For binary fields, independent exact formulas in \((k,q,s,m)\) agree with direct evaluation from the definitions. Complete permutation-canonicalized graph enumeration gives no reversal on any connected graph of order at most four, and exactly eleven reversal-admitting classes among the twenty-one connected graphs of order five. The explicit \(P_5\) witness and the all-path family are checked exactly.

Risk: the sharp finite cutoff changes if the weight convention or field class changes.

## Originality
**PASS.** The foundational literature owns the two autocorrelation statistics, and de Jong–Sprenger–van Veen explicitly study how their extreme values depend on a given network. That prior structural dependence is not claimed as new. The accepted claim is the exact regular-graph affine relation as an ordering obstruction together with the sharp binary reversal order, complete five-vertex graph-class census, and persistent path family. Targeted searches by aliases, exact values, graph language, and regularity language did not locate equivalent coverage.

Risk: the algebraic relation is natural from the graph Laplacian identity, so an unindexed lecture note or specialist exercise could contain the regular-graph observation or the small witness. No located source stated the combined sharp boundary and census.

## Value
**PASS.** Moran's \(I\) and Geary's \(C\) are canonical global spatial-autocorrelation statistics, and prior work emphasizes that network structure affects their behavior. The theorem pinpoints the mechanism: degree homogeneity forces complete ordering equivalence, whereas irregularity creates a degree-weighted variance term that can reverse rankings. The five-vertex minimum and exact first census provide compact benchmarks for interpretation and software validation rather than an arbitrary finite slice.

Self-review: passed. Independent audit: not yet performed.
