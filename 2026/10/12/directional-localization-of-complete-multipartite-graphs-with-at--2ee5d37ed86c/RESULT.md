# Directional localization of complete multipartite graphs with at least three parts
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite complete multipartite graph with \(r\ge3\) and every \(n_i\ge1\). Put \(s=\min_i n_i\). In the directional localization game,
\[
\zeta_d^*(G)=1,
\qquad
\zeta_d(G)=\min\{s,3\},
\]
where \(\zeta_d^*\) is the full-feedback parameter and \(\zeta_d\) is the partial-feedback parameter.

The partial-feedback upper bound is always achieved in one probing round. If \(s\le2\), probe every vertex of a smallest part. If \(s\ge3\), probe one vertex in each of three distinct parts.

## Assumptions and scope
Graphs are finite, simple, connected, and complete multipartite, with at least three nonempty parts. The game conventions are those of Jones and Kinnersley: in the partial-feedback model, each probe receives one permissible next vertex on a shortest path toward the robber; in the full-feedback model, the response contains all permissible next vertices. The robber may remain in place or move to a neighbor after a probing phase, and the cops must force unique localization in a bounded number of rounds.

The theorem does not assert a new value for complete bipartite graphs. Jones and Kinnersley already proved that if \(m\ge n\), then \(\zeta_d^*(K_{m,n})=1\) and \(\zeta_d(K_{m,n})=n\). The present result determines the previously untreated complete multipartite case with at least three parts.

## Proof
Fix the multipartition \(P_1,\ldots,P_r\).

For the full-feedback game, choose any part \(P\) and order it as \(p_1,\ldots,p_t\). One cop probes \(p_1,p_2,\ldots\) in successive rounds. If the robber is at the probed vertex, the response is that vertex. If the robber is outside \(P\), the probed vertex is adjacent to the robber, so the full response is the singleton consisting of the robber's vertex. If the robber is in \(P\) but is not the probed vertex, then the distance is two and every vertex outside \(P\) is a permissible first step; hence the full response is exactly \(V(G)\setminus P\). Because \(r\ge3\), this last set has at least two vertices and cannot be confused with a singleton response.

After a response \(V(G)\setminus P\) to the probe at \(p_i\), the robber is known, at that instant, to lie in \(P\setminus\{p_1,\ldots,p_i\}\). During recontamination he may move outside \(P\), but then the next probe returns his exact vertex as a singleton. If the next response is again \(V(G)\setminus P\), then he stayed in the still-unprobed portion of \(P\). Therefore at most \(t\) probes are needed, proving \(\zeta_d^*(G)=1\).

Now consider partial feedback.

If \(s\le2\), probe all vertices of a smallest part \(P\). If the robber lies in \(P\), one of those probes hits him. If the robber lies outside \(P\), then every probe in \(P\) is adjacent to him, and a length-one shortest path has only the robber as its next vertex. Thus the robber's response identifies his vertex. Hence \(\zeta_d(G)\le s\).

If \(s\ge3\), choose probes in three distinct parts. Any two candidate robber vertices lie in at most two parts, so at least one of the three probes lies in a part different from both candidates. From that probe, both candidates are adjacent to the probe, and the response is forced to be the candidate itself. Distinct candidates therefore cannot produce the same complete response vector. Thus three probes locate the robber in one round, proving \(\zeta_d(G)\le3\).

It remains to prove the lower bounds. Suppose first that \(s\ge2\) and only one cop probes a vertex \(p\) in part \(A\). Choose an unprobed vertex \(x\in A\) and a vertex \(y\) in a different part. The robber can answer \(y\). This response is valid if the robber is actually at \(y\), because \(p\) is adjacent to \(y\); it is also valid if the robber is at \(x\), because \(p,y,x\) is a shortest path of length two. Hence both \(x\) and \(y\) remain possible. Since they lie in distinct parts,
\[
N[x]\cup N[y]=V(G),
\]
so recontamination restores every vertex. Repeating this response strategy forever shows that one cop cannot win. Therefore \(\zeta_d(G)\ge2\) whenever \(s\ge2\).

Finally suppose \(s\ge3\) and two cops probe. If both probes are in the same part \(A\), choose an unprobed \(x\in A\) and a vertex \(y\) in another part, and answer \(y\) to both probes. Both \(x\) and \(y\) are consistent with both responses. If the probes lie in distinct parts \(A\) and \(B\), choose unprobed vertices \(x\in A\) and \(y\in B\). Answer \(y\) to the probe in \(A\) and \(x\) to the probe in \(B\). Again both \(x\) and \(y\) are consistent with the full pair of responses. In either case \(x\) and \(y\) lie in distinct parts, so their closed neighborhoods cover all vertices and recontamination resets the game to full uncertainty. Hence two cops cannot win when \(s\ge3\), proving \(\zeta_d(G)\ge3\).

Combining the upper and lower bounds gives \(\zeta_d(G)=\min\{s,3\}\).

## Verification
A standalone verifier exhaustively solved both feedback games by finite-state backward induction for every integer multipartition of total order at most eight having at least three parts. For each contaminated-state set, it enumerated every cop probe set, every adversarial response vector compatible with at least one robber position, and the exact closed-neighborhood recontamination step. The computed values agreed with the theorem for all tested graphs. This finite computation is a stress test only; the proof above establishes the result for all allowed part sizes.

## Relationship to prior work
Jones and Kinnersley introduced the directional localization game and proved the exact complete-bipartite values \(\zeta_d^*(K_{m,n})=1\) and \(\zeta_d(K_{m,n})=\min\{m,n\}\). Their paper also proves general bounds via degeneracy and treewidth and proves that chordal graphs need only one cop. A full-text inspection of the initiating paper found no occurrence of complete multipartite graphs beyond the complete-bipartite proposition.

The new multipartite formula exposes a sharp structural discontinuity. In the bipartite case the partial-feedback number can grow without bound with the smaller shore, whereas the presence of a third part forces the partial-feedback number down to at most three. The proof also identifies why: three probe parts destroy every two-candidate ambiguity, while two surviving candidates in distinct parts recontaminate the whole graph.

Targeted searches of a semantic research index for directional localization, complete multipartite and complete tripartite formulations returned no statement implying this theorem. The closest returned records concerned unrelated locating-domination and general-position invariants on complete multipartite graphs.

## Limitations
The theorem concerns complete multipartite graphs with at least three parts and the exact game rules of the initiating paper. It does not address noisy responses, restricted robber movement, directed graphs, or variants in which cops are required to probe distinct vertices. The finite verifier checks graphs only through total order eight and is not used as an infinite proof. Because the directional localization invariant is very recent, concurrent or poorly indexed work remains a residual originality risk.

## References
1. John Jones and William B. Kinnersley, *The directional localization game on graphs*, arXiv:2609.01745v1, first public 2026-09-01, primary MSC 05C57.
