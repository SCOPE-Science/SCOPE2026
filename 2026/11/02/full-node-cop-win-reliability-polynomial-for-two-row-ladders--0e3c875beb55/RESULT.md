# Full node cop-win reliability polynomial for two-row ladders

## Finding
For every integer \(n\ge1\), let \(L_n=P_2\square P_n\), and define the **cop-win vertex-subset polynomial**
\[
C_n(z)=\sum_{\substack{\varnothing\ne S\subseteq V(L_n)\\L_n[S]\text{ is cop-win}}}z^{|S|}.
\]
The complete size-refined enumeration, simultaneously for all ladder orders, is
\[
\boxed{\sum_{n\ge1}C_n(z)t^n=
\frac{tz(2+z+3tz^2)}{(1-t)^2(1-tz-2t^2z^3)}.}
\tag{1}
\]
In particular, writing \(c_{n,k}=[z^k]C_n(z)\), there is a finite closed formula for every \(1\le k\le2n\):
\[
\boxed{c_{n,k}=2(n-k+1)\mathbf 1_{\{1\le k\le n\}}+
\sum_{\substack{r\ge1\\2r-1\le k-r\le n}} (n-k+r+1)2^{r-1}
\left[\binom{k-2r+1}{r}+2\binom{k-2r}{r}+\binom{k-2r-1}{r}\right].}
\tag{2}
\]
All binomial coefficients with a negative upper index or with the lower index outside the interval from zero to the upper index are zero. The sum in (2) is finite because its constraints imply \(3r-1\le k\).

If each vertex survives independently with probability \(p\in[0,1]\), the probability \(R_n(p)\) that the surviving vertices induce a **nonempty cop-win graph** is
\[
R_n(p)=\sum_{k=1}^{2n}c_{n,k}p^k(1-p)^{2n-k}.
\]
Its full length generating function is
\[
\boxed{\sum_{n\ge1}R_n(p)t^n=
\frac{tp\bigl(2-p+3tp^2(1-p)\bigr)}
{\bigl(1-t(1-p)^2\bigr)^2\bigl(1-tp(1-p)-2t^2p^3(1-p)\bigr)}.}
\tag{3}
\]
The specializations
\[
C_n(1)=3(2^{n+1}-n-2),\qquad
C_n'(1)=8(n-2)2^n+4n+16
\tag{4}
\]
show that a uniformly chosen nonempty cop-win induced vertex set has mean cardinality \(C_n'(1)/C_n(1)\), and hence
\[
\boxed{\lim_{n\to\infty}\frac{C_n'(1)}{2nC_n(1)}=\frac23.}
\tag{5}
\]
The unweighted total in (4) is already represented in OEIS A360202; the new object here is the complete cardinality distribution (1)--(3), not that total.

## Assumptions and scope
Graphs are finite, simple, and undirected. The path \(P_n\) has \(n\) vertices, and \(P_1\) is allowed; thus \(L_1\) is a single edge. A graph with one vertex is cop-win, and the empty graph is **not** counted. The standard finite cop-win/dismantlable characterization uses deletion of vertices whose closed neighborhood is contained in another vertex's closed neighborhood. Vertices and rows of each ladder are distinguished; every subset is counted once. In (3) all vertices, but no edges separately, fail independently with the same parameter \(p\).

## Proof
**1. Cop-win means an induced tree.** Every \(L_n\) is bipartite, hence triangle-free. In a connected triangle-free graph containing at least two vertices, a vertex \(v\) dominated by a distinct vertex \(u\), meaning \(N[v]\subseteq N[u]\), has degree exactly one: if \(w\ne u\) were another neighbor of \(v\), the domination inclusion would make \(u,v,w\) a triangle. Therefore any valid dismantling removes only leaves. Every nonempty tree dismantles by successive leaf removal. Conversely, a connected graph with a cycle retains a nonempty minimum-degree-at-least-two core after all possible leaf removals and cannot dismantle. Thus a nonempty induced subgraph of \(L_n\) is cop-win exactly when it is a tree.

**2. Complete column-word characterization.** Encode a selected column by \(T=(1,0)\), \(B=(0,1)\), \(D=(1,1)\), or \(E=(0,0)\). A connected selected subgraph occupies an interval of nonempty columns; an internal \(E\) disconnects it. Across a boundary between consecutive nonempty columns, \(T\) followed by \(B\), or conversely, gives no horizontal edge and disconnects. Two consecutive \(D\) columns induce a four-cycle. These are the only restrictions: starting with a nonempty single-column tree, append a \(T\) or \(B\) that overlaps the previous column in its row, attaching a leaf; or append \(D\) after a singleton, attaching two new vertices along a path. Each operation preserves connectedness and acyclicity. Consequently, the allowed words are exactly those over \(\{T,B,D\}\) that avoid adjacent \(T,B\), adjacent \(B,T\), and adjacent \(D,D\). The letters carry weights \(z,z,z^2\), respectively.

**3. Rational size-enumerator.** Let \(U_\ell(z)\) enumerate allowed words of length \(\ell\) ending in one of \(T,B\), and \(V_\ell(z)\) those ending in \(D\). Their exact initial conditions and transitions are
\[
U_1=2z,\quad V_1=z^2,\quad
U_{\ell+1}=z(U_\ell+2V_\ell),\quad
V_{\ell+1}=z^2U_\ell.
\]
The factor two in the first transition records the two possible singleton successors of \(D\). Summing the two generating functions gives
\[
\sum_{\ell\ge1}(U_\ell+V_\ell)t^\ell
=\frac{tz(2+z+3tz^2)}{1-tz-2t^2z^3}.
\]
An allowed nonempty word of length \(\ell\) can start in exactly \(n-\ell+1\) positions inside \(L_n\); zero columns are forced outside this interval. Therefore
\[
C_n(z)=\sum_{\ell=1}^n(n-\ell+1)(U_\ell(z)+V_\ell(z)),
\]
and the identity \(\sum_{n\ge\ell}(n-\ell+1)t^n=t^\ell/(1-t)^2\) proves (1).

**4. Independent coefficient count.** A word of length \(\ell\) with no \(D\) is either entirely \(T\) or entirely \(B\), giving two words of weight \(z^\ell\). For \(r\ge1\) letters \(D\), write \(g_0,\ldots,g_r\) for the lengths of the intervening singleton blocks, with \(g_1,\ldots,g_{r-1}\ge1\), and \(g_0,g_r\ge0\). Each nonempty block must use a constant row, hence has two choices. After extracting the mandatory \(r-1\) internal singleton letters, the generating function for the remaining singleton letters is
\[
2^{r-1}\frac{(1+u)^2}{(1-u)^{r+1}}.
\]
The coefficient of \(u^{\ell-2r+1}\) is therefore
\[
2^{r-1}\left[\binom{\ell-r+1}{r}+2\binom{\ell-r}{r}+\binom{\ell-r-1}{r}\right].
\]
Such a word has \(k=\ell+r\) selected vertices and \(n-\ell+1\) placements. Summing these contributions and the no-\(D\) case proves (2), independently of the rational-function calculation.

**5. Reliability and first moment.** For \(0\le p<1\), independence gives \(R_n(p)=(1-p)^{2n}C_n(p/(1-p))\). Substitute \(t\mapsto t(1-p)^2\) and \(z\mapsto p/(1-p)\) into (1), then simplify to obtain (3). Both sides are polynomials in \(p\) coefficientwise, so (3) remains valid at \(p=1\) by continuity. At \(z=1\), the unshifted word generating function cancels to \(3t/(1-2t)\), yielding the first identity in (4). Differentiating (1) and setting \(z=1\) gives
\[
\sum_{n\ge1}C_n'(1)t^n=\frac{4t}{(1-t)^2(1-2t)^2},
\]
whose coefficient is the second identity in (4). Dividing the two expressions proves (5).

## Verification
The standalone file `verify_ladder_copwin.py` reconstructs edges from the graph definition. For each \(1\le n\le9\), it exhaustively checks every nonempty vertex subset, independently tests graph connectivity and acyclicity using a disjoint-set cycle test, and compares the exact cardinality polynomial with both the column automaton and the closed binomial coefficient formula. These are 349,515 graph-level subsets altogether. For \(1\le n\le7\), a separate dominated-vertex dismantling implementation confirms the cop-win/tree equivalence directly on every nonempty induced graph. A further 100 complete polynomials are checked by independent arithmetic evaluation of the coefficient and transfer recurrences, including the total, first moment, and top coefficient.

For instance,
\[
C_4(z)=8z+10z^2+16z^3+18z^4+16z^5+10z^6.
\]
Run `python3 verify_ladder_copwin.py`; the program ends with `VERIFY_OK`. The infinite theorem follows from the complete word characterization and algebraic identities above, not from finite testing.

## Relationship to prior work
Ahmed and Cameron introduced node cop-win reliability and its cop-win polynomial, analyzing unicyclic and bicyclic graphs. A ladder with \(n\ge4\) has at least three independent cycles, so the cited classification by cycle rank does not itself give this complete size-refined ladder polynomial. Vince analyzed connected vertex subsets of ladders and their average size, without an acyclicity restriction in the accessible abstract. The present theorem distinguishes nonempty induced trees from cyclic connected subsets and yields a limiting density of \(2/3\) rather than the previously reported \(3/4\) for all connected induced subsets.

The OEIS entries A360202, A360918, and A360920 already tabulate, respectively, the **unweighted numbers**, **maximum-tree multiplicities**, and **maximum-tree cardinalities** for grids, including the two-row case. These scalar specializations are expressly **not claimed as new**. They do not supply the complete coefficient distribution in (1)--(3), which is necessary to evaluate node cop-win reliability at arbitrary failure probabilities. The relevant Ahmed--Cameron and Vince full articles could not be fully inspected through accessible sources; only their public abstracts and indexed passages were available. The possibility of an unindexed or differently described size-refined formula remains a publication-priority limitation.

## Limitations
The theorem concerns only two-row path grids and independently retained vertices. It does not enumerate cop-win induced subgraphs of wider grids or circular ladders, treat separate edge failures, or compare reliability uniformly among different host graphs. It provides a self-contained proof and reproducible checks but does not certify publication priority independently; particularly relevant full texts were not fully accessible.

## References
1. Andrew Vince, *The average size of a connected vertex set of a graph—Explicit formulas and open problems*, Journal of Graph Theory 97 (2021), 82–103; first published online 2020-11-03. DOI: 10.1002/jgt.22643.
2. Maimoonah Ahmed and Ben Cameron, *The node cop-win reliability of unicyclic and bicyclic graphs*, arXiv:2011.10641, first posted 2020-11-20; Networks 79 (2022), 189–201. DOI: 10.1002/net.22055.
3. Andrew Howroyd, OEIS A360202, *Number of non-null induced trees in grid graphs*, initial entry 2023-02-22, https://oeis.org/A360202.
4. Andrew Howroyd, OEIS A360918, *Number of maximum induced trees in grid graphs*, initial entry 2023-02-26, https://oeis.org/A360918.
5. Andrew Howroyd, OEIS A360920, *Maximum cardinality of induced trees in grid graphs*, initial entry 2023-02-26, https://oeis.org/A360920.
