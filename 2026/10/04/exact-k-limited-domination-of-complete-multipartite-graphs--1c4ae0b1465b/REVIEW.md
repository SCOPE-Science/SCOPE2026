# Same-model review

## Correctness
PASS. For a candidate set \(D\), the proof writes \(q=|V(G)\setminus D|=k+t\). In any part met by \(D\), the capacity condition is exactly \(q-x_i\le k\), hence \(x_i\ge t\) and \(d_i\le n_i-t\). Summing these exact partwise capacities yields the necessary inequality \(\sum_i\min\{n_i,t\}\le k+t\). The converse allocates \(N-k-t\) selected vertices inside the capacities \((n_i-t)_+\) across at least two parts, which directly gives both domination and the capacity condition. The boundary requirement \(t\le N-k-2\) rules out an impossible one-vertex solution in the nontrivial range. The balanced corollary follows by reducing the feasibility inequality to \((r-1)t\le k\).

## Originality
PASS. The initiating 2026 paper defines the invariant, proves the complete-bipartite case, and explicitly asks for additional graph families, but does not give a complete-multipartite formula. Its discussion of equivalent pitchfork terminology states that the \((0,k)\) case had not been studied in that literature. Semantic-index searches for the exact invariant, complete multipartite and Turán aliases, the \((0,k)\)-pitchfork formulation, and the threshold expression returned no covering statement. The closest indexed complete-multipartite findings concern different invariants. The complete-bipartite theorem is a strict special case of the new formula rather than a stronger statement that implies it for arbitrary part counts.

## Value
PASS. Complete multipartite graphs are a standard family containing complete graphs, stars, bicliques, and balanced Turán graphs. The theorem extends the initiating paper's exact biclique calculation to all part profiles, gives a compact computable criterion, and yields the especially simple balanced formula \(rm-k-\lfloor k/(r-1)\rfloor\). This directly answers a graph-family direction identified by the initiating paper and exposes how capacity is shared across more than two parts.

## Closest literature and limitations
The closest source is Božović--Radić--Kovijanić-Vukićević--Tepeh, arXiv:2606.22422, whose Proposition 1(iv) determines \(K_{m,n}\) exactly. The older pitchfork paper DOI:10.1142/S1793830920500251 studies the lower-bound-one, upper-bound-two case rather than the equivalent \((0,k)\) regime. The present theorem is restricted to complete multipartite graphs; the finite computation through order \(11\) is only a stress test. An unindexed older \((0,k)\)-pitchfork treatment remains a residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
