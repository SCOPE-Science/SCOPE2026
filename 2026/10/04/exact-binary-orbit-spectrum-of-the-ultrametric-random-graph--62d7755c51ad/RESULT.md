# Exact binary orbit spectrum of the ultrametric random graph

## Finding

Let \(\mathcal U=(\omega^\omega,d,E)\) be the universal homogeneous closed graph on Baire space constructed by Kubiś, Pech, and Pech, with its canonical ultrametric taking the positive values \(2^{-k}\) for \(k\in\omega\). Let \(G=\operatorname{Aut}(\mathcal U)\), where automorphisms preserve both \(d\) and \(E\).

Then the ordered-pair orbit space is exactly
\[
G\backslash(\omega^\omega)^2
=
\{\Delta\}\cup\{O_{k,0},O_{k,1}:k\in\omega\},
\]
where \(\Delta=\{(x,x):x\in\omega^\omega\}\) and
\[
O_{k,\varepsilon}
=
\{(x,y):x\neq y,\ d(x,y)=2^{-k},\ \mathbf 1_E(x,y)=\varepsilon\}.
\]
In particular, there is one diagonal orbit and, at each positive distance level, exactly two off-diagonal ordered-pair orbits: adjacent and nonadjacent.

Consequently \(G\) has countably infinitely many ordered-pair orbits. For every \(x\in\omega^\omega\), the point stabilizer \(G_x\) has exactly two nontrivial point-orbits on each sphere \(\{y:d(x,y)=2^{-k}\}\), again distinguished by adjacency to \(x\).

## Assumptions and scope

The result concerns the specific universal homogeneous ultrametric graph supplied by the finite-graph instance of the inverse-limit construction in arXiv:2301.10953. Distances are the canonical Baire-space values \(2^{-k}\). The graph convention in the construction permits loops, but the classification above concerns off-diagonal pairs, so only the two possibilities \(E(x,y)\) and \(\neg E(x,y)\) matter.

No claim is made here about higher-arity tuple orbits, orbit growth, generic automorphisms, or arbitrary homogeneous ultrametric structures.

## Proof

Every automorphism in \(G\) preserves both the metric and the graph relation. Hence the pair
\[
\bigl(d(x,y),\mathbf 1_E(x,y)\bigr)
\]
is an invariant of every off-diagonal ordered-pair orbit. This shows that different sets \(O_{k,\varepsilon}\) cannot merge.

Conversely, suppose \((x,y)\) and \((x',y')\) are off-diagonal ordered pairs with
\[
d(x,y)=d(x',y')=2^{-k}
\]
and
\[
E(x,y)\iff E(x',y').
\]
The map \(x\mapsto x'\), \(y\mapsto y'\) is then an isomorphism between the induced two-point graph structures and is an isometry. The strict homogeneity of the universal ultrametric structure extends this finite partial isomorphism to a global automorphism of \(\mathcal U\). Thus the two ordered pairs lie in the same \(G\)-orbit.

Each \(O_{k,\varepsilon}\) is nonempty. The finite-extension property in the graph example realizes every compatible finite ultrametric graph extension while preserving the prescribed metric. Starting from one vertex, add a second vertex at distance \(2^{-k}\), choosing the off-diagonal graph relation either present or absent. Both choices therefore occur for every \(k\).

Singleton isomorphisms extend by homogeneity, so the diagonal is a single orbit. The displayed list is therefore exhaustive. Fixing the first coordinate gives the corresponding point-stabilizer statement.

## Verification

The argument was replayed as a four-part invariant/completeness check.

First, metric preservation forces every orbit to stay inside one distance level. Second, graph preservation splits each nonzero distance level into at most the adjacent and nonadjacent cases. Third, strict homogeneity merges any two pairs having the same distance and adjacency bit. Fourth, the finite-extension property realizes both bits at every canonical distance level.

These four steps prove both exhaustiveness and nonemptiness of the stated classes. No numerical experiment is needed for the infinite conclusion.

## Relationship to prior work

Kubiś, Pech, and Pech construct the relevant universal homogeneous ultrametric graph and prove the strict homogeneity and finite-extension properties used above. Their paper explicitly presents the Baire-space graph as a special case of the theory, but the checked text does not enumerate the automorphism group's ordered-pair orbits.

Delhomme, Laflamme, Pouzet, and Sauer prove that the isometry group of a homogeneous pure ultrametric space has arity at most \(2\). That is a broader structural result for the metric-only language, but it does not classify the graph-enriched pair orbits or yield the extra adjacency/nonadjacency split at every distance level.

Targeted exact, broader, and semantic-index searches did not locate the displayed orbital decomposition for the ultrametric random graph. Because the deduction from strict homogeneity is short, an unindexed or folklore occurrence remains a priority risk.

## Limitations

The finding is an exact low-arity invariant, not a classification of the full automorphism group. It does not determine higher tuple orbits or conjugacy classes.

The originality assessment is necessarily literature-search based. The pair-orbit classification may have been observed informally without being indexed or stated as a theorem.

The pure-ultrametric arity theorem predates the eligible source window and is used only as contextual prior art; the primary source anchoring this finding is the 2023 graph-enriched construction.

## References

W. Kubiś, Ch. Pech, M. Pech, *Homogeneous ultrametric structures*, arXiv:2301.10953. First public version: 2023-01-26. Primary MSC: 03C30.

C. Delhomme, C. Laflamme, M. Pouzet, N. Sauer, *On homogeneous ultrametric spaces*, arXiv:1509.04346.
