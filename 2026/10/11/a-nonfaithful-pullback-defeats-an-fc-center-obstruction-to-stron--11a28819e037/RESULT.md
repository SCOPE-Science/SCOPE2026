# A nonfaithful pullback defeats an FC-center obstruction to strong double minimality
## Finding
Remark 5.3 of Bitar--Donoso--Petite, arXiv:2609.26479v1, is false for the paper's stated notion of strong double minimality unless an effectiveness hypothesis is added. Let \(G=\mathbb Z\times S_3\) and let \(\pi:G\to\mathbb Z\) be projection. Since \(Z(S_3)=\{e\}\), one has \(Z(G)=\mathbb Z\times\{e\}\) and hence \(\pi(Z(G))=\mathbb Z=Z(\mathbb Z)\). Take any strong doubly minimal \(\mathbb Z\)-system and pull it back along \(\pi\). Proposition 5.15 of the same paper proves that this pullback is again strong doubly minimal, while every element of \(\ker\pi\) acts trivially. But \(g=(0,(12))\) is noncentral and has finite conjugacy class, so \(g\in\operatorname{FC}(G)\setminus Z(G)\). Thus \(G\) admits a strong doubly minimal action despite \(\operatorname{FC}(G)\setminus Z(G)\ne\varnothing\), contradicting the group-level conclusion of Remark 5.3. The proof in Remark 5.3 fails here because the graph of \(S^g=\operatorname{id}\) is the diagonal, and Definition 5.1 imposes density only on pairs from different \(Z(G)\)-orbits. No claim is made against a faithful or effective-action version of the obstruction.

## Assumptions and scope
Let \(S_3\) be the symmetric group on three letters and let
\[
G=\mathbb Z\times S_3,
\qquad
\pi:G\longrightarrow\mathbb Z,
\qquad
\pi(n,\sigma)=n.
\]
Strong double minimality means two-fold strong topological minimal self-joining in Definition 5.1 of Bitar--Donoso--Petite: the diagonal orbit of every pair of distinct points lying on different \(Z(G)\)-orbits is dense in the square. The claim concerns Remark 5.3 and Proposition 5.15 of arXiv:2609.26479v1 exactly as first posted on 2026-09-22. It does not assert that any faithful reformulation of Remark 5.3 is false, and it does not challenge the paper's main theorems on non-deterministic horofunctions.

## Proof
The center of a direct product is the product of the centers. Since \(Z(S_3)=\{e\}\),
\[
Z(G)=\mathbb Z\times\{e\}.
\]
Consequently
\[
\pi(Z(G))=\mathbb Z=Z(\mathbb Z).
\]
Strong doubly minimal \(\mathbb Z\)-systems exist; the motivating paper itself recalls this immediately after Definition 5.1, and classical constructions of King and Weiss supply such systems.

Fix one such \(\mathbb Z\)-system \((X,T)\). Define the pullback \(G\)-action by
\[
S^{(n,\sigma)}x=T^n x.
\]
Proposition 5.15 of arXiv:2609.26479v1 applies because \(\pi\) is onto and \(\pi(Z(G))=Z(\mathbb Z)\). Hence \((X,S,G)\) is strong doubly minimal. The source explicitly notes after Proposition 5.15 that such pullbacks need not be faithful because elements of \(\ker\pi\) act trivially.

Now choose
\[
g=(0,(12))\in G.
\]
The transposition \((12)\) is not central in \(S_3\), so \(g\notin Z(G)\). Since \(S_3\) is finite, the conjugacy class of \(g\) in \(G\) is finite; indeed it consists of the three transpositions in the second factor. Therefore
\[
g\in\operatorname{{FC}}(G)\setminus Z(G),
\]
so \(\operatorname{{FC}}(G)\setminus Z(G)\ne\varnothing\).

Remark 5.3 states that this group-theoretic condition prevents \(G\) from admitting a strong doubly minimal system. The pullback just constructed is such a system, so that conclusion is false as stated.

The mechanism pinpoints the proof gap. Because \(g\in\ker\pi\),
\[
S^g=\operatorname{{id}}_X.
\]
Hence the graph of \(S^g\) is just the diagonal \(\Delta_X\). Its orbit under the diagonal \(G\)-action remains \(\Delta_X\), but this does not contradict Definition 5.1: points on the diagonal are in the same \(Z(G)\)-orbit, whereas strong double minimality requires density only for pairs on different \(Z(G)\)-orbits. Thus the finite-orbit-of-graphs argument in Remark 5.3 needs an additional condition ensuring that the relevant graph contains a pair from distinct central orbits; faithfulness is one natural way to rule out this particular kernel collapse.

## Verification
The argument is symbolic and finite at the group-theoretic step. The center computation uses \(Z(S_3)=\{e\}\); the conjugacy class of a transposition in \(S_3\) has three elements. The dynamical step is exactly Proposition 5.15 applied with \(H=\mathbb Z\), together with the paper's Definition 5.1. The source was inspected at the actual PDF pages containing Definition 5.1, Remark 5.3, Proposition 5.15, and the explicit statement that pullback systems from Proposition 5.15 are not faithful. No numerical experiment, finite approximation of an infinite orbit, or computational log is used as proof.

## Relationship to prior work
Bitar, Donoso and Petite introduce the group-action form of strong topological minimal self-joinings and, in Remark 5.3, claim the obstruction
\[
\operatorname{{FC}}(G)\setminus Z(G)\ne\varnothing
\]
precludes a strong doubly minimal system. Later in the same preprint, Proposition 5.15 proves that strong topological minimal self-joinings pull back through an epimorphism \(\pi:G\to H\) whenever \(\pi(Z(G))=Z(H)\), and immediately observes that these pullback actions are nonfaithful. Combining those published statements with \(G=\mathbb Z\times S_3\) gives the counterexample above.

King's classical construction and Weiss's subsequent work supply the needed existence of strong doubly minimal \(\mathbb Z\)-systems. Targeted searches for Remark 5.3, the \(\operatorname{{FC}}(G)\)-center obstruction, nonfaithful pullbacks, and the specific \(\mathbb Z\times S_3\) construction located no prior correction or equivalent counterexample. The available arXiv record remained version 1 during this review.

## Limitations
The result invalidates only the unconditional group-level conclusion in Remark 5.3 of arXiv:2609.26479v1. It does not show that the conclusion fails for faithful actions, does not give a complete corrected characterization of groups admitting strong doubly minimal systems, and does not affect Proposition 5.15 itself. A later author revision or an unindexed correction could remove the issue; none was located in the searches performed.

## References
1. N. Bitar, S. Donoso and S. Petite, *Non-determinism in group actions and topological minimal self-joinings*, arXiv:2609.26479v1, 2026.
2. J. L. King, *A map with topological minimal self-joinings in the sense of del Junco*, Ergodic Theory Dynam. Systems 10 (1990), 745--761, doi:10.1017/S0143385700005873.
3. B. Weiss, *Multiple recurrence and doubly minimal systems*, Contemporary Mathematics 215 (1998), 189--196, doi:10.1090/conm/215/02940.
