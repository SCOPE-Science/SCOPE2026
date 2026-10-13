# Review of Edge-version metric and double metric bases of friendship graphs

## Correctness
PASS. In the line graph, all spoke edges form a clique and each rim edge is adjacent exactly to the two spokes from its own page. This gives the complete distance table. For ordinary edge-version resolution, every page must contain a selected spoke, and two one-landmark pages would leave their unselected spokes metrically indistinguishable, forcing the sharp lower bound \(2r-1\). The equality construction resolves every omitted-edge pair and yields exactly \(2r3^{r-1}\) bases. For double resolution, a page containing at most one selected edge either fails ordinary resolution or leaves a spoke-rim pair with a constant distance-difference vector, forcing two selected edges per page. The converse is verified by direct pair types, giving \(2r\) and exactly \(3^r\) minima. Exhaustive checks for \(2\le r\le6\) agree with every statement.

## Originality
PASS. The foundational 2018 edge-version doubly resolving paper treats sunlets and prisms and contains no friendship or windmill result. The later same-invariant circulant paper is confined to \(C_n(1,2)\) and likewise contains no friendship or windmill theorem. Searches under the equivalent formulation “doubly resolving number of the line graph of a friendship graph,” as well as edge-based and double-edge terminology, did not locate an equivalent result. The known 2019 friendship edge-metric theorem uses vertex landmarks resolving edges and is therefore scientifically inapplicable to the edge-landmark line-graph parameter proved here.

## Value
PASS. Friendship graphs are a standard wheel-related family already used as a benchmark in metric-resolvability work. The result gives a complete pagewise structure theorem for both the edge-version metric bases and the stricter doubly resolving bases, exact enumerations of all minima, and an infinite family with a sharp constant gap \(\psi_E-\dim_E=1\). This directly develops the inequality \(\dim_E\le\psi_E\) emphasized in the defining literature rather than merely computing an isolated small case.

Self-review: passed. Independent audit: not yet performed.
