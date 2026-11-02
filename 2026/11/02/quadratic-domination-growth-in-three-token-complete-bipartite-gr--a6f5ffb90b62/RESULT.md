# Quadratic domination growth in three-token complete bipartite graphs

## Finding
Let \(F_3(G)\) be the three-token graph of a finite simple graph \(G\): its vertices are the three-element subsets of \(V(G)\), and two configurations are adjacent when one token moves along one edge of \(G\) to an unoccupied vertex. Let \(\gamma\) denote ordinary closed-neighborhood domination. For all integers \(2\le m\le n\), \(n\ge4\), put
\[
q(n)=\binom n2-\left\lfloor\frac{n^2}{4}\right\rfloor
=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor.
\]
Then
\[
\boxed{q(n)\le\gamma(F_3(K_{m,n}))\le q(n)+\left(\binom{m-1}{2}+1\right)n-2.}
\]
Both bounds are proved, and the upper bound is achieved by an explicit dominating set, not asserted to be optimal. In particular, for each fixed integer \(m\ge2\),
\[
\boxed{\lim_{n\to\infty}\frac{\gamma(F_3(K_{m,n}))}{n^2}=\frac14.}
\]
For the first nonstar case \(m=2\), the finite sandwich simplifies to
\[
\left\lfloor\frac{(n-1)^2}{4}\right\rfloor
\le\gamma(F_3(K_{2,n}))
\le\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+n-2
\qquad(n\ge4).
\]
This determines the sharp quadratic growth coefficient for the first higher-token problem beyond two tokens, while leaving its linear correction unresolved.

## Assumptions and scope
Here \(K_{m,n}\) has bipartition \(A\sqcup B\) with \(|A|=m\), \(|B|=n\). Tokens are indistinguishable and occupy distinct graph vertices. Domination means every three-token configuration either belongs to the selected set or is adjacent to one that does. The inequalities are for all integer \(2\le m\le n\) with \(n\ge4\), including configurations with zero, one, two, or three tokens in \(A\). The limit holds with \(m\) fixed and \(n\to\infty\); no uniform limit is claimed when \(m\) grows proportionally to \(n\).

## Proof
**The Turán lower bound.** Let \(D\) be an arbitrary dominating set and partition it according to the number of its tokens in \(A\). Set \(T=D\cap\binom B3\). Define a graph \(P\) on \(B\) by declaring \(bb'\) an edge if \(D\) includes at least one configuration \(\{a,b,b'\}\) with \(a\in A\). Thus \(|E(P)|\le|D\cap\{\text{configurations with one token in }A\}|\). Write \(Q=\overline P\) for the complementary graph on \(B\).

Every triangle \(\{b,b',b''\}\) of \(Q\) must belong to \(T\). Indeed, a configuration of three \(B\)-tokens has neighbors only among the configurations with one \(A\)-token, and a neighbor in \(D\) would require one of its three pairs to lie in \(P\). Consequently the number of triangles of \(Q\) does not exceed \(|T|\). Remove one edge of \(Q\) from each of its triangles (the same edge can be removed more than once in the instructions, but is deleted only once). The resulting graph is triangle-free and retains at least \(|E(Q)|-|T|\) edges. Mantel's theorem therefore yields
\[
|E(Q)|-|T|\le \left\lfloor\frac{n^2}{4}\right\rfloor.
\]
Since \(|E(P)|+|E(Q)|=\binom n2\), it follows that
\[
|D|\ge |E(P)|+|T|
\ge \binom n2-\left\lfloor\frac{n^2}{4}\right\rfloor=q(n).
\]
For completeness, the requisite form of Mantel's theorem follows by summing \(d(u)+d(v)\le n\) over the edges \(uv\) of any triangle-free graph: \(\sum_vd(v)^2\le n|E|\), while Cauchy--Schwarz gives \(\sum_vd(v)^2\ge4|E|^2/n\).

**Constructive upper bound.** Label \(A=\{a_0,a_1,\ldots,a_{m-1}\}\). Partition \(B=B_0\sqcup B_1\) into parts of sizes \(\lfloor n/2\rfloor\) and \(\lceil n/2\rceil\); both have at least two members because \(n\ge4\). Choose any three-element subset \(R\subseteq B\). Form a set \(D^*\) of three-token configurations as follows:

1. For every pair \(b,b'\) lying in the same \(B_i\), include \(\{a_0,b,b'\}\).
2. For every \(b\in B\) and \(1\le i<j\le m-1\), include \(\{a_i,a_j,b\}\).
3. For each \(b\in B\setminus R\), include \(\{a_0,a_1,b\}\).
4. Include the one configuration \(R\subseteq B\).

The four families are disjoint. Their total cardinality is
\[
\left(\binom{\lfloor n/2\rfloor}{2}+\binom{\lceil n/2\rceil}{2}\right)
+\binom{m-1}{2}n+(n-3)+1
=q(n)+\left(\binom{m-1}{2}+1\right)n-2.
\]
We check domination in every layer, using the definition of token adjacency rather than relying on a numerical experiment.

A configuration consisting of three vertices of \(B\) contains two in the same \(B_i\) by pigeonhole, and is adjacent to the corresponding configuration in family 1. For a configuration \(\{a_0,b,b'\}\), if \(\{b,b'\}\subseteq R\), it is adjacent to the selected configuration \(R\); otherwise at least one of \(b,b'\) lies in \(B\setminus R\), and replacing the other \(B\)-token with \(a_1\) gives a selected configuration in family 3. A configuration \(\{a_i,b,b'\}\) with \(i\ge1\) is adjacent to a selected configuration in family 2 when \(m\ge3\), since another index \(j\in\{1,\ldots,m-1\}\setminus\{i\}\) exists. For \(m=2\), the only such index is \(i=1\), and the same argument using family 3 for a pair meeting \(B\setminus R\), or family 4 for a pair within \(R\), applies with the two \(A\) labels interchanged.

Every configuration with two \(A\)-tokens either lies in family 2 or 3, or contains \(a_0\) and a \(B\)-vertex \(b\). Because each part \(B_i\) has at least two vertices, select \(b'\ne b\) from the same part: the family-1 configuration \(\{a_0,b,b'\}\) is adjacent to the omitted two-\(A\)-token configuration (the non-\(a_0\) token moves to \(b'\)). Finally, a configuration with three \(A\)-tokens has two members among \(a_1,\ldots,a_{m-1}\); replacing its third \(A\)-token by any \(b\in B\) reaches family 2. Such configurations exist only for \(m\ge3\). Thus \(D^*\) dominates every configuration. The upper bound follows.

For fixed \(m\), both bounds are \(n^2/4+O_m(n)\). Division by \(n^2\) and squeezing establish the limit.

## Verification
Run `python verify.py` with the standard library. The checker directly constructs the prescribed sets for 95 parameter pairs with \(2\le m\le8\) and \(\max\{m,4\}\le n\le18\), and checks domination against the original three-token adjacency rule. It exhausts all simple graphs on three through six vertices (33,864 graphs) to test the elementary triangle-edge deletion inequality. It also exhaustively rules out dominating sets of size below four for \(F_3(K_{2,4})\), and checks the arithmetic identities at additional dimensions. Observed output ends in `VERIFY_OK`. These finite checks are corroboration only; the argument above proves the statements for unbounded parameters.

## Relationship to prior work
Chinman, Cortijo, Pedroni, Seong, and Stenger (arXiv:2610.28936, first posted 2026-10-20) determined \(\gamma(F_2(K_{m,n}))\) and gave general degree/independence bounds for \(\gamma(F_k(K_{m,n}))\) when \(k\ge3\). For fixed \(m\) and \(k=3\), their stated lower bound is only \((1/(6m)+o(1))n^2\), and their stated upper bound grows cubically. These do not imply the proved quadratic coefficient \(1/4\) or the explicit \(O_m(n)\) gap. Fabila-Monroy and Gómez-Galicia (arXiv:2509.16448) used Mantel-type ideas for the three-token *complete-graph* case and considered star-token graphs, but not the present two-nontrivial-part graph family. Acosta Troncoso, Caldera Caldera, and Rivera (arXiv:2610.31557, first posted 2026-10-22) determined only the two-token complete-bipartite case. Their concluding section identifies higher-token domination and Turán numbers as work in progress: this creates a material unpublished-priority risk and is explicitly not treated as inspected proof of the present bounds.

## Limitations
The exact finite value of \(\gamma(F_3(K_{m,n}))\) remains unproved here outside the displayed sandwich. In particular, numerical agreement of the construction with small optimization instances is not a proof of its optimality. The limit assumes fixed \(m\), not arbitrary joint growth. Possible unpublished work on higher-token domination and Turán numbers has not been compared in full, and independent mathematical audit is not performed. The proof uses the classical Mantel theorem; the novelty claim concerns the three-token domination bounds and their leading coefficient, not Mantel's theorem or the general token-graph definition.

## References
- N. Chinman, A. Cortijo, B. Pedroni, I. Seong, L. Stenger, *The domination number of the \(k\)-token graph of the complete bipartite graph \(K_{m,n}\)*, arXiv:2610.28936v1 (2026-10-20), https://arxiv.org/html/2610.28936v1.
- E. Acosta Troncoso, I. Caldera Caldera, L. M. Rivera, *The domination number of the 2-token graph of the complete bipartite graph*, arXiv:2610.31557 (2026-10-22), https://arxiv.org/abs/2610.31557.
- R. Fabila-Monroy, S. G. Gómez-Galicia, *Domination number of Token Graphs*, arXiv:2509.16448v1 (2025-09-19), https://arxiv.org/html/2509.16448v1.
- H. de Alba, W. Carballosa, J. Leaños, L. M. Rivera, *Independence and matching numbers of some token graphs*, Australasian Journal of Combinatorics **76** (2020), 387–403; first preprint arXiv:1606.06370 (2016-06-21).
- Mantel's triangle-free extremal theorem (classical); a self-contained proof of the needed inequality is given above.
