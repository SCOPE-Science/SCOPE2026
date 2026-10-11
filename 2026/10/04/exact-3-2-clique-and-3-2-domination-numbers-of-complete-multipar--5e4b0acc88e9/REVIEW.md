# Independent mathematical audit

## correctness

PASS

For a complete multipartite graph, a three-vertex set lies on a geodesic of length at most two exactly when its part-multiplicity pattern is two plus one. From that characterization, a \((3,2)\)-clique meets at most two parts and uses at most two vertices from each, giving \(2+\min\{2,s\}\), where \(s\) is the number of non-singleton parts. For domination, a two-set in one part dominates exactly when that whole part has order two, while a cross-part two-set dominates exactly in the bipartite case; otherwise two vertices in a part of size at least three plus one outside give a dominating three-set. Independent shortest-path brute force over every complete multipartite type of total order at most nine reproduced both formulas for 87 graph types.

## originality

PASS

No prior source found the exact formulas. The complete Cody--Detore paper defines the invariants but leaves classical families beyond its path/cycle program open and specifically lists complete bipartite graphs; older multipartite general-position results concern a different avoidance invariant. The package's multipartite geodesic characterization therefore survives implication-level comparison.

## value

PASS

Complete multipartite graphs are a canonical diameter-two family, and the foundational 2026 paper explicitly asks for exact \(k,d\)-invariants on other classical families, including the bipartite subfamily. Simultaneously determining the clique and domination numbers from the same geodesic-type lemma is a natural structural classification, even though the resulting formulas are short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
