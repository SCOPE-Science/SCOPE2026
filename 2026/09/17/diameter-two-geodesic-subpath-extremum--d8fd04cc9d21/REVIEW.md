# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** For diameter-two graphs, every nontrivial geodesic has length one
or two. Edges contribute one geodesic each, while length-two geodesics are in
bijection with induced \(P_3\)'s together with their middle vertex; hence
\(\operatorname{gpn}(G)=n+m(G)+p_3(G)\).

The weighted lemma
\[
m(G)+p_3(G)\le \frac n2\left\lfloor\frac{n^2}{4}\right\rfloor
\]
was checked directly from the cut identity
\[
2(m+p_3)=\sum_x e(N(x),V\setminus N(x)).
\]
For each \(x\), the summand is at most
\(d(x)(n-d(x))\le\lfloor n^2/4\rfloor\). The equality argument was
stress-tested separately: equality makes every neighborhood cut complete;
nonadjacent vertices then have identical neighborhoods, forcing a complete
multipartite graph. Balanced-degree equality restricts every part to one of
the two half-sizes, leaving exactly the balanced complete bipartite graph for
\(n\ge4\). At \(n=3\), the weighted lemma also permits \(K_3\), but the
diameter-two hypothesis removes it. No hidden connectivity assumption is
used in the weighted lemma.

Boundary checks agree with the theorem: \(K_{1,2}\) is the unique extremal
diameter-two graph for \(n=3\), and \(K_{2,2}\) attains the formula for
\(n=4\).

## Originality

**PASS, to the best of our knowledge.** The closest source is Knor–Sedlar–
Škrekovski–Zhang (2026), which introduces \(\operatorname{gpn}\), gives an
upper bound for general connected graphs, computes several families, and
poses a bipartite extremal problem. Its concluding discussion explicitly
notes balanced complete bipartite graphs and the possibility that deleting a
perfect matching can increase \(\operatorname{gpn}\), but no diameter-two
extremal theorem was found there.

Pyatkin–Lykhovyd–Butenko (2019) proves the exact maximum number of induced
open triangles \(p_3(G)\) on \(n\) vertices, attained by the balanced complete
bipartite graph. That theorem does not by itself optimize the weighted
quantity \(m(G)+p_3(G)\) required here. Searches using “induced \(P_3\),”
“open triangle,” “diameter two,” “number of geodesics,” “shortest paths,”
“stress,” and weighted combinations with the edge count did not locate the
cut identity above or the stated diameter-two geodesic-subpath extremum.

Related stress literature includes Bhargava–Dattatreya–Rajendra
(arXiv:2208.13493), which computes vertex stress in diameter-two graphs.
This is consistent with the \(P_3\) interpretation but no result maximizing
the total geodesic-subpath number over diameter-two graphs was found.

### Access limitations and residual risk

The complete publisher text of Pyatkin–Lykhovyd–Butenko (2019) was not
available in the inspected source; its theorem statement, abstract, and
publisher preview were inspected. It is the most plausible source in which a
weighted auxiliary inequality could conceivably appear without being
advertised in the title or abstract.

Two later papers by A. V. Pyatkin on open triangles with prescribed sparse
edge counts were identified:
- DOI 10.33048/daio.2024.31.793 (English DOI 10.1134/S1990478924030128);
- DOI 10.33048/daio.2025.32.830 (English DOI 10.1134/s1990478925020103).

Their accessible descriptions concern sparse regimes with a fixed relation
between vertices and edges, rather than the dense weighted optimization here.
Not every full proof was inspected, so they remain a low but nonzero
originality risk. No inaccessible source was found whose available statement
already covers the claimed diameter-two theorem.

Internal SCOPE records were checked under the mathematical objects and
synonyms above; no prior record covering this result was found.

## Value

**PASS.** The result exactly solves the geodesic-subpath extremal problem on
the broad and natural class of diameter-two graphs, including nonbipartite
graphs, with a unique extremal graph for every \(n\ge3\). It also isolates a
structural boundary in the recent bipartite problem: constructions obtained
by deleting cross-edges from a complete bipartite graph can outperform the
complete bipartite family only after leaving diameter two. The weighted
open-triangle inequality is elementary, exact, and potentially reusable
outside this application.

## Review status

Same-model review: passed. Cross-model review: not yet performed.
