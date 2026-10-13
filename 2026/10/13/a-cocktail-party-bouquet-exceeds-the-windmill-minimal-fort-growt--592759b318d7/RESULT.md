# A cocktail-party bouquet exceeds the windmill minimal-fort growth base

## Finding
For every integer \(r\ge 1\), construct the connected graph \(B_r\) from \(r\) disjoint copies of \(Q=K_6-M_3\), where \(M_3\) is a perfect matching, by adding one common vertex \(c\) adjacent to every vertex of every copy. No edges join distinct copies outside \(c\). Thus \(|V(B_r)|=6r+1\). A *fort* in a finite simple graph is a nonempty vertex set \(F\) for which every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is *inclusion-minimal* if no proper nonempty subset is a fort.

Let \(\mathfrak M(G)\) denote the inclusion-minimal forts of \(G\), and let \(P_G(z)=\sum_{F\in\mathfrak M(G)}z^{|F|}\). Then
\[
\boxed{P_{B_r}(z)=3rz^2+8rz^3+12^rz^{2r+1}.}
\]
Consequently, \(|\mathfrak M(B_r)|=12^r+11r\) and
\[
\boxed{\lim_{r\to\infty}|\mathfrak M(B_r)|^{1/(6r+1)}=12^{1/6}>3^{1/3}.}
\]
In particular, this explicitly constructed connected family has strictly greater minimal-fort *per-vertex exponential growth base* than the previously exhibited four-vertex-page windmill family.

## Assumptions and scope
All graphs are finite, simple, undirected, and labeled only to distinguish their vertices. The \(r\) copies of \(Q\) are ordered for counting. Each copy contains three disjoint *mate pairs* (the three nonedges of \(K_6-M_3\)); a *transversal triple* chooses exactly one vertex from each mate pair. The hub \(c\) belongs to no copy of \(Q\). The formula includes \(r=1\), where the two size-three contributions coincide in degree and sum to \(20z^3\). For the limit, the order is \(6r+1\), not \(r\).

## Proof
**1. Minimal forts inside a copy of \(Q\).** For a vertex \(v\) of \(Q\), its sole nonneighbor among the other five vertices is its mate \(v'\). A singleton \(\{v\}\) is not a fort, because each of the other four nonmate vertices has exactly one selected neighbor. A mate pair is a fort: any exterior vertex sees both vertices of the pair. A nonmate pair \(\{u,v\}\) is not a fort: the mate \(u'\) of \(u\) sees \(v\) but not \(u\). Every set \(S\subseteq V(Q)\) of size at least three is a fort, because each exterior vertex has at least \(|S|-1\ge2\) neighbors in \(S\). Consequently the minimal forts of \(Q\) are precisely its three mate pairs and its eight transversal triples: a triple is inclusion-minimal exactly when it contains no mate pair, and every set of size at least four contains a mate pair. In particular, the least size of a nonempty fort in \(Q\) is two.

**2. Forts without the hub.** Suppose \(c\notin F\subseteq V(B_r)\), and set \(F_i=F\cap V(Q_i)\) for the copy indexed by \(i\). Every exterior vertex in \(Q_i\) sees only vertices of \(F_i\), so \(F\) is a fort if and only if each nonempty \(F_i\) is a fort of \(Q_i\), and the exterior hub has at least two neighbors in \(F\). The latter condition is automatic because a nonempty local fort has at least two vertices. If two blocks have nonempty local forts, either block supplies a proper subfort of \(F\). If one nonempty local fort is not minimal, it similarly supplies a proper subfort. Conversely, a minimal fort of one copy is still a fort of \(B_r\) and none of its proper subsets can be a fort. Thus precisely \(3r\) minimal forts of size two and \(8r\) of size three omit \(c\).

**3. Forts containing the hub.** Suppose \(c\in F\). Every exterior vertex \(v\in Q_i\) has \(c\) as one selected neighbor. The fort condition is therefore equivalent to requiring an additional neighbor of \(v\) in \(F_i\), for every \(v\notin F_i\). In other words, each \(F_i\) must be a (closed-neighborhood) dominating set of \(Q_i\). No singleton dominates \(Q_i\), because it misses its mate; every pair dominates, because any vertex outside that pair can fail adjacency to at most one of its two members. Hence each \(F_i\) has at least two vertices, and if any \(F_i\) has at least three, deleting all but two of its vertices gives a proper fort still containing \(c\). Thus a minimal hub-containing fort has exactly two selected vertices per block.

If one of these pairs is a mate pair, the pair alone is a proper fort of \(B_r\) omitting \(c\), so the hub-containing set cannot be minimal. Therefore every local pair must be a nonmate pair. Conversely, for a hub-containing fort with one nonmate pair per block, every proper subset containing \(c\) leaves fewer than two selected vertices in at least one block and hence fails to dominate that block. Every nonempty proper subset omitting \(c\) has no nonempty local fort, since its intersection with each block is contained in a nonmate pair, and so also fails the fort condition. Thus all such forts are inclusion-minimal. There are \(\binom62-3=12\) nonmate pairs in every block, chosen independently, yielding exactly \(12^r\) minimal forts of size \(2r+1\).

**4. Count and growth.** The hub-free and hub-containing families are disjoint and exhaustive by Steps 2 and 3. Their sizes give the displayed polynomial and its value at one. Finally, \(12^r+11r\) has \(r\)-th root tending to \(12\); because \((6r+1)/r\to6\), its per-vertex root tends to \(12^{1/6}\). Taking sixth powers, \(12^{1/6}>3^{1/3}\) is equivalent to \(12>9\).

## Verification
The standalone standard-library program `verify.py` constructs \(B_r\), checks the fort definition for all nonempty subsets and checks inclusion minimality against **all proper subsets**, via subset dynamic programming. Its exhaustive results for \(r=1,2,3\) are recorded in `verification_output.txt`. A fresh execution from the extracted files must reproduce that output. These finite checks are separate from the symbolic classification, but do not constitute the proof for arbitrary \(r\); that is Steps 1–4.

## Relationship to prior work
Becker, Cameron, Hanely, Ong and Previte (2024), *On the Number of Minimal Forts of a Graph*, arXiv:2404.05963v1, studied minimal-fort enumeration and vertex-sum constructions. Their Corollaries 28–29 give for the four-vertex-page windmill \(W^d(4,r)\) the exact count \(3^r+3r\), with per-vertex base \(3^{1/3}\); their Conjecture 31 motivates a larger growth base. The vertex-amalgamation framework and the windmill enumeration are **prior results**, not claimed as new. The new, specific result is the complete minimal-fort classification and polynomial for the matching-deleted-clique bouquet, producing \(12^{1/6}\). The classification of minimal forts in one \(K_{2,2,2}\) block is a known special case of complete-multipartite fort classification and is re-proved here only to make the new bouquet argument self-contained.

## Limitations
No claim of the globally optimal growth base is made. The subsequence of orders \(6r+1\) supplies the stated per-vertex limit; it does **not alone** prove the literal consecutive-*order* limit in Conjecture 31 as written. Matching a stronger previously published all-bouquet result has not been ruled out with certainty; exact literature priority requires external verification. The independent scientific audit has not been performed. Neither the verifier nor finite exhaustive checks establish the infinite case without the written proof.

## References
1. P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, *On the Number of Minimal Forts of a Graph*, arXiv:2404.05963v1, publicly posted 2024-04-09, https://arxiv.org/abs/2404.05963 (especially Sections 2, 5.3, Corollaries 28–29 and Conjecture 31).
