# Sharp asymptotic for binary trigram multispectrum capacity

## Finding
For every integer \(n\ge3\), let \(M_3(w)\) be the multiset of the \(n-2\) consecutive length-three factors of a binary word \(w\in\{0,1\}^n\), retaining multiplicities. Let
\[
Q_3(n)=\bigl|\{M_3(w):w\in\{0,1\}^n\}\bigr|.
\]
Then, as \(n\to\infty\),
\[
\boxed{Q_3(n)=\frac{13}{288}n^4+O(n^3).}
\]
Equivalently, the maximum cardinality of a binary length-\(n\) code whose words are distinguished by their complete linear trigram multispectra is \(Q_3(n)\), and its leading term has coefficient \(13/288\). The constant counts one balanced and twelve distinct endpoint-imbalance sectors, each contributing \(1/288\) at fourth order.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); words are **linear**, not cyclic, and all observed factors have length exactly three. Each occurrence contributes separately. A code distinguishes any two different words in it by their multispectra; exactly one representative can be chosen from each observed multispectrum class.

Put \(m=n-2\). The binary order-two de Bruijn digraph has vertices \(00,01,10,11\) and, for each \(abc\in\{0,1\}^3\), an edge labeled \(abc\) from \(ab\) to \(bc\). A vector \(x=(x_{abc})\) of eight nonnegative integers is an edge-multiplicity vector, with total \(\sum_{abc}x_{abc}=m\). Define its divergence at a vertex to be outgoing multiplicity minus incoming multiplicity.

## Proof
**1. Endpoint flows and the thirteen sectors.** A length-\(n\) word traces \(m\) successive directed edges, beginning at its first two bits \(s\) and ending at its last two bits \(t\). Its divergence is \(e_s-e_t\). There are exactly thirteen distinct such divergence vectors: one zero vector for \(s=t\), and twelve vectors for the ordered pairs \(s\ne t\). These sectors are disjoint in the edge-count space. Conversely, the directed Euler-trail criterion says that a nonnegative integer edge vector of positive total with divergence \(e_s-e_t\) comes from a walk from \(s\) to \(t\) precisely when the subgraph of positive-degree vertices is connected in the underlying undirected sense. The Eulerian walk spells a binary word because neighboring edges overlap on two symbols.

**2. A rational generating function for balanced flows.** Let \(H_m\) count all nonnegative edge vectors of total \(m\) with zero divergence, whether or not the support is connected. Write
\[
 A=x_{000},\quad B=x_{001},\quad C=x_{010},\quad D=x_{011},\quad
 E=x_{100},\quad F=x_{101},\quad G=x_{110},\quad J=x_{111}.
\]
Vertex balance gives \(E=B\), \(G=D\), and \(F=C+D-B\). Thus every balanced vector corresponds bijectively to integers \(A,J,B,C,D\ge0\) satisfying
\[
 0\le B\le C+D,\qquad A+J+B+2C+3D=m.
\]
Summing geometric series, with \(z\) an ordinary generating variable, yields
\[
\begin{aligned}
 \sum_{m\ge0}H_m z^m
 &=\frac{1}{(1-z)^2}\sum_{C,D\ge0}z^{2C+3D}\sum_{B=0}^{C+D}z^B\\
 &=\frac{1}{(1-z)^3}\left(
 \frac{1}{(1-z^2)(1-z^3)}-
 \frac{z}{(1-z^3)(1-z^4)}\right)\\
 &=\boxed{\frac{1+z^3}{(1-z)^2(1-z^2)(1-z^3)(1-z^4)}}.
\end{aligned}
\]
At \(z=1\), the rational function equals \((1/12)(1-z)^{-5}+O((1-z)^{-4})\) in a punctured neighborhood. Every other pole is a root of unity of order at most two. Partial fractions therefore give
\[
 H_m=\frac1{12}\binom{m+4}{4}+O(m^3)=\frac{m^4}{288}+O(m^3).
\]
This coefficient estimate concerns *all* balanced nonnegative integer vectors, including a lower-order exceptional disconnected set.

**3. All endpoint sectors have the same leading coefficient.** For \(s\ne t\), let \(F_m(s,t)\) count all nonnegative edge vectors of total \(m\) with divergence \(e_s-e_t\), without connectivity imposed. Every vertex \(s=ab\) has a directed path of length two to any vertex \(t=cd\), using edges \(abc\) then \(bcd\). Adding the multiplicity vector of this fixed path gives an injection from balanced vectors of total \(m-2\) into the \((s,t)\) sector at total \(m\). Adding the reverse length-two path gives an injection from that sector at total \(m\) into balanced vectors of total \(m+2\). Hence for all \(m\ge2\),
\[
 H_{m-2}\le F_m(s,t)\le H_{m+2},
\qquad F_m(s,t)=\frac{m^4}{288}+O(m^3).
\]
The zero-divergence sector has count \(H_m\) and the same leading term.

**4. Disconnected vectors contribute only lower order.** The vector assigning one copy to every one of the eight edges is a strictly positive zero-divergence circulation. For every divergence sector, adding this circulation to an appropriate two-edge path (or using it alone in the balanced sector) gives a strictly positive feasible vector. Extra copies of the loop \(000\) show that such strictly positive vectors exist at every sufficiently large total \(m\), independently in every sector. The affine space of real vectors satisfying its fixed divergence and total \(m\) has dimension \(8-3-1=4\): the de Bruijn digraph is connected, so its incidence matrix has rank three, and total multiplicity adds one independent equation. Requiring any specified edge multiplicity to vanish intersects this four-dimensional affine space in a proper affine subspace of dimension at most three, since a positive solution exists at that same \(m\). All coordinates lie between zero and \(m\); after choosing three free coordinates, each other coordinate is fixed by linear equations, so each such face has only \(O(m^3)\) integer points. Taking the union of eight boundary faces still gives \(O(m^3)\). Every nonnegative vector with *all eight* coordinates positive has connected support and hence admits a directed Euler trail. Consequently, the number of realizable word spectra in each sector differs from its unrestricted flow count by at most \(O(m^3)\).

Summing the thirteen disjoint sectors gives
\[
 Q_3(n)=13\,\frac{m^4}{288}+O(m^3)
 =\frac{13}{288}n^4+O(n^3),\qquad m=n-2.
\]
Finally, choosing one word from every class attains the corresponding reconstruction-code cardinality by definition. This proves the claim.

## Verification
Run `python3 verify.py` with standard-library Python. The program enumerates every binary word for \(3\le n\le15\), independently obtains the same spectra by a two-bit-state de Bruijn dynamic program, and compares the profile sets exactly. It also computes dynamic-programming counts through \(n=24\) and verifies every coefficient of the rational balanced-flow generating function through total edge multiplicity \(60\) by an independent nonnegative-integer-solution sum. Representative exact counts are \(Q_3(10)=363\), \(Q_3(15)=1880\), \(Q_3(20)=6123\), and \(Q_3(23)=10876\). These are finite consistency checks; the infinite asymptotic follows from the analytic proof above.

## Relationship to prior work
Jacquet and Szpankowski (2004) describe arbitrary-order Markov types via the appropriate sparse de Bruijn transition graph, but their stated higher-order calculations concern numbers of strings of **a specified type** and minimax redundancy, not the total number of distinct linear binary trigram types or its sharp coefficient. Jacquet, Knessl, and Szpankowski (2009/2010) count **cyclic, first-order, unrestricted-alphabet** balanced frequency matrices, with exact asymptotic constants for complete transition graphs. Their brief higher-order comment does not evaluate the four-vertex, eight-edge de Bruijn support and the twelve open-ended endpoint sectors required here. In particular, replacing an alphabet size by four in their complete-transition graph is not equivalent to respecting the eight allowed edges of a binary second-order chain.

Gabrys and Milenkovic (2018) define linear fixed-read-length multispectrum reconstruction codes and give general counting bounds and constructions, but their analyzed read-length regimes do not give this fixed-length-three sharp capacity. A published count for binary length-two linear multispectra gives a quadratic polynomial rather than the quartic three-mer growth; it does not imply the coefficient here. Our counting argument is a specialization of standard Euler-flow ideas with an explicitly evaluated new balanced-flow series and careful treatment of all possible linear endpoints. An earlier unindexed calculation of the same specialized flow series remains a residual originality risk.

## Limitations
The theorem is asymptotic with additive error \(O(n^3)\), not an exact formula for each \(n\); no coefficient of the cubic error term is claimed. It does not cover cyclic observations, alphabet sizes greater than two, read lengths other than three, corrupted reads, or a computationally efficient representative-code encoder. The finite verification does not establish the infinite claim by itself.

## References
1. P. Jacquet and W. Szpankowski, *Markov Types and Minimax Redundancy for Markov Sources*, IEEE Transactions on Information Theory 50(7), 1393–1402 (2004), DOI:10.1109/TIT.2004.830765. Author-hosted manuscript: https://www.cs.purdue.edu/homes/spa/papers/red-f-markov.pdf.
2. P. Jacquet, C. Knessl, and W. Szpankowski, *Markov Types Again Revisited*, author-hosted manuscript dated September 2, 2009, https://www.cs.purdue.edu/homes/spa/papers/markov-types.pdf; *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768.
3. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548 (first posted 2018-04-12), https://arxiv.org/abs/1804.04548.
4. *Exact binary two-multispectrum code size and singleton classification*, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71.
