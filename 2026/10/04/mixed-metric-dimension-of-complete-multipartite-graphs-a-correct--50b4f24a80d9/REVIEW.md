# Independent mathematical audit

## correctness

PASS

In a complete multipartite graph, an edge code with respect to selected landmarks is simply the selected-endpoint indicator vector: every nonendpoint landmark is distance one from the edge. Hence two omitted vertices in one part collide as vertices, and three omitted vertices always create two omitted-endpoint edges with identical all-one codes. With one omitted vertex, the only further obstruction is a selected vertex in a singleton other part colliding with its incident edge. With two omitted vertices, distinct parts and exactly two graph parts are necessary; each part must retain at least two selected vertices to separate endpoint incidents, which is equivalent to original part sizes at least three. These conditions are also sufficient by direct code comparison. A fresh direct computation gives \(\operatorname{mdim}(K_{3,3,5})=10\), and the frozen verifier exhausts all multipartite types through order ten.

## originality

PASS

The 2022 primary article explicitly claims a complete-multipartite mixed-metric formula, but its Theorem 5 is false: it gives \(N-r\) when no part has size two, so it predicts 8 for \(K_{3,3,5}\), whereas exact mixed codes force 10. The foundational complete-bipartite formula remains valid and is preserved as prior coverage. Targeted searches found no erratum or later corrected all-set classification. The surviving new contribution is therefore a genuine correction plus a complete generator classification and enumerator.

## value

PASS

The theorem corrects an exact published formula on a canonical graph family, identifies the precise missing obstruction, handles singleton parts, and upgrades the corrected minimum value to a classification and count of every mixed generator. This is a substantive correction rather than a cosmetic refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
