# Same-model review

## Correctness
**PASS.** In a complete multipartite graph, the closed-neighborhood count depends only on the selected total \(s\), the selected count \(s_i\) in the vertex's part, and whether the vertex itself is selected. The lower construction is checked in both the fully selected and non-fully-selected cases. Minimality is witnessed after every possible one-vertex deletion. For the upper bound, the standard tight-witness lemma for minimal \(k\)-tuple domination is reproved directly from deletion minimality, and the two possibilities for the witness—inside or outside the set—both force \(s\le L+k-1\). The boundary cases \(k=1\) and \(k=N-L+1\) are included. The exhaustive verifier independently agrees through order \(10\).

## Originality
**PASS.** The defining upper-parameter paper was inspected in full text: it gives the tight-witness lemma, regular-graph bounds, a claw-free regular bound, and hardness on bipartite/chordal graphs; “multipartite” does not occur in the document. The directly relevant complete-multipartite papers inspected concern minimum \(k\)-tuple domination and/or the open-neighborhood total variant. Targeted semantic-literature and web searches for upper \(k\)-tuple, upper double, minimal \(k\)-tuple, complete multipartite, and equivalent terminology found no statement implying the formula \(L+k-1\). The classical \(k=1\) specialization is prior-covered and is not treated as the novel content.

## Value
**PASS.** Upper \(k\)-tuple domination is an established invariant whose computation is hard even on bipartite graphs. Complete multipartite graphs are a natural test family for multiple domination, and the exact value across every feasible \(k\), together with a uniform extremal construction, gives a useful closed benchmark rather than a finite or arbitrary slice. The formula also separates the upper-minimal problem sharply from the already-studied minimum and total variants.

## Closest literature and limitations
The closest source is Chang–Dorbec–Kim–Raspaud–Wang–Zhao (2012), which defines \(\Gamma_{\times k}\) and supplies the minimality witness used in the proof but does not treat complete multipartite graphs. Henning–Kazemi (2010) treats complete multipartite graphs for minimum \(k\)-tuple total domination, and Kazemi (2012) compares minimum closed and total variants. The present result does not classify all extremal minimal sets. Older literature under alternate multiple-domination terminology remains a residual bibliographic risk.

Same-model review: passed. Independent audit: not yet performed.
