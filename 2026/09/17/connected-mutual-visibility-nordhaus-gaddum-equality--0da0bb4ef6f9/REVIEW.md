# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The near-maximum criterion is direct and reversible. If \(S=V(G)\setminus\{x\}\) is a connected mutual-visibility set and \(y\) is nonadjacent to \(x\), then \(y\) must be adjacent to every other vertex of \(S\): otherwise a nonadjacent pair \(y,z\in S\) would require an \(S\)-avoiding geodesic whose only possible internal vertex is \(x\), contradicting \(xy\notin E(G)\). Conversely, if \(G-x\) is connected and every nonneighbor of \(x\) is universal in \(G-x\), then every nonedge inside \(G-x\) has both endpoints adjacent to \(x\), so the length-two geodesic through \(x\) witnesses visibility.

The complement decomposition \(\overline G=K_{1,r}\cup Q\) follows immediately: all complement-neighbors of the witnessing vertex are leaves. In a Nordhaus--Gaddum equality case with \(n\ge5\), the source inequalities force the unordered parameter pair \(\{n-1,n-2\}\). Since a star component contributes at most \(2\), the decomposition forces \(r\le1\). The cases \(r=1\) and \(r=0\) respectively yield
\[
\overline G=K_2\cup K_{n-2}
\]
and
\[
\overline G=K_{n-2}\cup 2K_1,
\]
giving exactly the two families in the statement and their complements.

As an additional finite stress test, the characterization was checked on every graph in the NetworkX graph atlas (all unlabeled graphs through seven vertices). No mismatch occurred for the \(n-1\) criterion; for \(n=5,6,7\), exactly four unlabeled equality graphs occur, matching the two families and their complements. This computation is supporting evidence only; the published proof is general and does not rely on enumeration.

## Originality

The primary source inspected in full is:

- Tonny K B and Shikhi M, *Connected Mutual-Visibility in Graphs*, arXiv:2609.18877v1, submitted 16 September 2026.

The source introduces \(\mu_c\), characterizes the values \(n\) and \(2\), proves the Nordhaus--Gaddum bounds
\[
\mu_c(G)+\mu_c(\overline G)\le2n-3,\qquad
\mu_c(G)\mu_c(\overline G)\le(n-1)(n-2),
\]
and gives an example proving sharpness. It does not characterize \(\mu_c(G)=n-1\) and does not classify all equality graphs for the Nordhaus--Gaddum inequalities.

Searches used exact and synonymous phrases for connected mutual visibility, the value \(n-1\), second-largest-value characterizations, Nordhaus--Gaddum equality, and the complete-bipartite/complement families. They returned the introducing preprint and general mutual-visibility literature, but no prior statement implying the two theorems recorded here.

No inaccessible paper was identified as a concrete likely source of prior coverage. The main residual risk is the extreme recency of the parameter: parallel work may exist but not yet be publicly indexed.

## Value

The first theorem gives a complete local structural description of the second-largest possible connected mutual-visibility number. The second theorem upgrades sharp Nordhaus--Gaddum inequalities into a full equality classification for every \(n\ge5\), showing that only two complementary construction types occur.

## Limitations

The order-\(4\) boundary is excluded from the equality classification because additional small-order equality cases occur. The record does not attempt to classify \(\mu_c(G)=n-2\) in general.

The originality assessment is to the best of our knowledge. No independent validation, formal verification, or peer review is asserted.
