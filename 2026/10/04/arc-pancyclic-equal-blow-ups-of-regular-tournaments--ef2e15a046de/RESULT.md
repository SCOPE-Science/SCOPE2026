# Arc-pancyclic equal blow-ups of regular tournaments

## Finding
Let \(T\) be a regular tournament on \(c\ge5\) vertices and let \(\alpha\ge1\). Form the equal independent-set blow-up \(T[\overline{K}_{\alpha}]\): every vertex \(x\in V(T)\) is replaced by a part \(X_x\) of size \(\alpha\), there are no arcs inside a part, and every pair \(X_x,X_y\) is oriented uniformly from \(X_x\) to \(X_y\) exactly when \(x\to y\) in \(T\). Then every arc of \(T[\overline{K}_{\alpha}]\) lies on a directed cycle of every length
\[
3,4,\ldots,c\alpha.
\]
Thus \(T[\overline{K}_{\alpha}]\) is arc-pancyclic. The blow-up is itself a regular \(c\)-partite tournament, with indegree and outdegree both equal to \(\alpha(c-1)/2\).

## Assumptions and scope
A tournament is regular when every vertex has the same indegree and outdegree. Hence its order \(c\) is odd. The theorem concerns \(c\ge5\); for \(c=3\) the conclusion fails when \(\alpha\ge2\), because a blow-up of a directed triangle has no directed cycle of length \(4\) or \(5\). An arc is arc-pancyclic when it belongs to a directed cycle of every possible length from \(3\) through the order of the digraph.

The construction is the standard digraph composition (lexicographic product) with an edgeless factor. No assumption is made that the base regular tournament is cyclic, circulant, or uniquely determined.

## Proof
Fix an arc \(xy\) of the blow-up, with \(x\in X_u\) and \(y\in X_v\). Then \(u\to v\) is an arc of the regular tournament \(T\).

Alspach's theorem states that every arc of a regular tournament belongs to a directed cycle of every length from \(3\) through the order of the tournament. Therefore, for each integer \(t\) with \(3\le t\le c\), there is a directed \(t\)-cycle of \(T\) containing \(u\to v\).

Fix a target length \(\ell\) with \(3\le \ell\le c\alpha\). For \(1\le k\le\alpha\), put \(I_k=[3k,ck]\cap\mathbb Z\). Since \(c\ge5\), consecutive intervals have no integer gap: for every \(k\ge1\),
\[
3(k+1)\le ck+1.
\]
Hence \(I_1\cup\cdots\cup I_{\alpha}=\{3,4,\ldots,c\alpha\}\). Choose \(k\le\alpha\) with \(3k\le\ell\le ck\). Because \(0\le \ell-3k\le(c-3)k\), distribute \(\ell-3k\) among \(k\) summands to obtain integers
\[
t_1,\ldots,t_k\in\{3,\ldots,c\},\qquad t_1+\cdots+t_k=\ell.
\]

For each \(j\in\{1,\ldots,k\}\), choose a directed \(t_j\)-cycle in \(T\) containing \(u\to v\), and write it as
\[
C_j=(u,v,w_{j,3},\ldots,w_{j,t_j},u).
\]
Index the vertices of every blow-up part as \(z^{(1)},\ldots,z^{(\alpha)}\). For the first layer choose \(u^{(1)}=x\) and \(v^{(1)}=y\); in all other parts and layers choose the correspondingly indexed vertices. Now concatenate the lifted cycle segments:
\[
u^{(1)},v^{(1)},w_{1,3}^{(1)},\ldots,w_{1,t_1}^{(1)},
 u^{(2)},v^{(2)},w_{2,3}^{(2)},\ldots,w_{2,t_2}^{(2)},\ldots,
 u^{(k)},v^{(k)},w_{k,3}^{(k)},\ldots,w_{k,t_k}^{(k)},u^{(1)}.
\]
Every displayed step is an arc of the blow-up. Inside a segment this follows from \(C_j\); between two consecutive segments it follows from the final arc \(w_{j,t_j}\to u\) of \(C_j\); the last segment closes in the same way. The walk is simple: each base cycle uses each part at most once, and different segments use different layer indices \(j\). Its length is \(t_1+\cdots+t_k=\ell\), and its first arc is the prescribed arc \(xy\). Since \(\ell\) and \(xy\) were arbitrary, the blow-up is arc-pancyclic.

## Verification
The standalone verifier reconstructs several nonisomorphic regular base tournaments (cyclic tournaments of orders \(5,7,9,11,13\) and Paley tournaments of orders \(7,11\)). For every base arc it independently searches for a containing base cycle of every length from \(3\) through \(c\), applies the interval decomposition and splicing construction for \(1\le\alpha\le4\), and checks that the resulting lifted cycle is simple, directed, has the requested length, and begins with the prescribed lifted arc.

The computation is a finite stress test only. The universal theorem is proved above from Alspach's arc-pancyclicity theorem and the explicit splicing argument.

## Relationship to prior work
Alspach proved in 1967 that every regular tournament is arc-pancyclic. The present theorem lifts that conclusion from a regular tournament to all of its equal independent-set blow-ups.

Pan and Zhang proved in 2004 that, in every regular multipartite tournament with at least four parts, each arc lies on a cycle meeting exactly \(k\) partite sets for every \(k\) from \(4\) through the number of parts. That statement controls how many parts a cycle meets, not its number of vertices, and therefore does not imply the present all-length conclusion after parts have size greater than one.

Xia's 2026 paper proves that all regular \(c\)-partite tournaments are \(4\)-arc-pancyclic for \(c\ge93\), proves large intervals of guaranteed cycle lengths under weaker hypotheses, and formulates a conjecture asserting almost the full number of distinct cycle lengths for every arc when \(c\ge4\). The equal blow-ups considered here form a natural infinite subclass in which the stronger \(3\)-arc-pancyclic conclusion holds for every regular base tournament and every \(\alpha\ge1\), including all odd \(c\ge5\), without a large-\(c\) requirement.

Yeo's theorem that regular multipartite tournaments with at least five parts are vertex-pancyclic is weaker in a different direction: it guarantees each vertex, but not each arc, on cycles of every length.

## Limitations
The theorem is a sufficient-condition result for equal blow-ups of regular tournaments. It does not classify all regular multipartite tournaments that are arc-pancyclic, and it does not address unequal blow-ups. The hypothesis \(c\ge5\) is necessary for this proof and conclusion: the equal blow-up of the directed triangle fails to contain some intermediate cycle lengths once \(\alpha\ge2\).

Originality was checked against the initiating 2026 full text, classical arc-cycle results for regular multipartite tournaments, composition terminology, targeted web searches, a semantic research index, and prior published findings. A residual literature risk remains that an older result about digraph compositions may imply the same statement under terminology not surfaced by the searches.

## References
1. B. Alspach, “Cycles of Each Length in Regular Tournaments,” *Canadian Mathematical Bulletin* 10 (1967), 283–286. DOI: 10.4153/CMB-1967-028-6.
2. L. Q. Pan and K. M. Zhang, “On Cycles Containing a Given Arc in Regular Multipartite Tournaments,” *Acta Mathematica Sinica, English Series* 20 (2004), 379–384. DOI: 10.1007/s10114-004-0327-1.
3. Z.-B. Zhang, X. Zhang, G. Gutin, and D. Lou, “Hamiltonicity, pancyclicity, and full cycle extendability in multipartite tournaments,” *Journal of Graph Theory* 96 (2021), 171–191. DOI: 10.1002/jgt.22606.
4. W. Xia, “4-Arc-Pancyclicity of Regular Multipartite Tournaments,” arXiv:2609.12372, first submitted 2026-09-11.
