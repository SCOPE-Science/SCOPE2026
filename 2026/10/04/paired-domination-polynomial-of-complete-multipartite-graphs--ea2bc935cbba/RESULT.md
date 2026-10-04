# Paired-domination polynomial of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge 2\), partite sets \(V_1,\ldots,V_r\), and \(N=\sum_i n_i\). For \(S\subseteq V(G)\), write \(s_i=|S\cap V_i|\).

A set \(S\) is paired-dominating exactly when there is an integer \(q\ge 1\) such that
\[
|S|=2q \quad\text{and}\quad s_i\le q\ \text{for every }i.
\]
Consequently, if
\[
D_p(G;x)=\sum_{k=0}^{N} d_p(G,k)x^k,
\]
then every odd coefficient is zero and, for \(1\le q\le \lfloor N/2\rfloor\),
\[
d_p(G,2q)=\binom{N}{2q}-
\sum_{i=1}^{r}\sum_{j=q+1}^{\min\{n_i,2q\}}
\binom{n_i}{j}\binom{N-n_i}{2q-j}.
\]
If \(m=\max_i n_i\), the nonzero degrees are exactly
\[
2,4,\ldots,2Q,\qquad Q=\min\{\lfloor N/2\rfloor,N-m\}.
\]
In particular,
\[
\gamma_p(G)=2,
\qquad
d_p(G,2)=|E(G)|=\sum_{1\le i<j\le r} n_i n_j.
\]

For the complete bipartite specialization \(K_{a,b}\), this becomes
\[
D_p(K_{a,b};x)=\sum_{q=1}^{\min\{a,b\}}
\binom{a}{q}\binom{b}{q}x^{2q}.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. A paired-dominating set is a dominating set whose induced subgraph contains a perfect matching. The theorem concerns connected complete multipartite graphs, equivalently \(K_{n_1,\ldots,n_r}\) with \(r\ge2\) and every \(n_i\ge1\). No claim is made for disconnected graphs or for other domination polynomials.

Paired domination was introduced by Haynes and Slater in 1998. Puttaswamy, Alwardi, and Nayaka introduced the paired-domination polynomial in 2016 and reported computations for some standard graph families.

## Proof
Fix \(S\subseteq V(G)\) and let \(|S|=t\). After suppressing empty parts, \(G[S]\) is a complete multipartite graph with part sizes \(s_1,\ldots,s_r\).

Suppose first that \(S\) is paired-dominating. A perfect matching of \(G[S]\) forces \(t=2q\) for some \(q\ge1\). Each selected vertex in \(V_i\) must be matched to a selected vertex outside \(V_i\), so
\[
s_i\le 2q-s_i,
\]
and therefore \(s_i\le q\) for every \(i\).

Conversely, suppose \(|S|=2q\ge2\) and \(s_i\le q\) for every \(i\). Order the selected vertices so that each part forms one consecutive block. Pair position \(h\) with position \(h+q\) for \(1\le h\le q\). The two endpoints of such a pair cannot lie in the same part: a consecutive part-block containing both positions would contain at least \(q+1\) vertices, contradicting \(s_i\le q\). Hence all \(q\) pairs are edges, and they form a perfect matching of \(G[S]\).

The same condition gives domination. Since no single part can contain all \(2q\) selected vertices, \(S\) meets at least two parts. Every vertex outside \(S\) is adjacent to a selected vertex in a different part. Thus \(S\) is paired-dominating.

For the coefficient formula, begin with all \(\binom{N}{2q}\) subsets of size \(2q\). Such a subset fails the characterization exactly when some part contains at least \(q+1\) selected vertices. Two distinct parts cannot both contain at least \(q+1\) selected vertices, because that would require more than \(2q\) selected vertices. Therefore these overload events are disjoint. For part \(i\), the number of overloaded subsets is
\[
\sum_{j=q+1}^{\min\{n_i,2q\}}
\binom{n_i}{j}\binom{N-n_i}{2q-j}.
\]
Subtracting the disjoint bad counts proves the stated coefficient formula.

It remains to determine the support. A set of size \(2q\) satisfying the balance condition exists exactly when the part capacities \(\min\{n_i,q\}\) can supply \(2q\) vertices. Necessarily \(q\le\lfloor N/2\rfloor\). If \(m>N/2\), at least \(q\) selected vertices must lie outside a largest part, so also \(q\le N-m\).

These bounds are sufficient. If \(m>N/2\) and \(q\le N-m\), choose \(q\) vertices from a largest part and \(q\) outside it. If \(m\le N/2\), choose any part containing at least \(q\) vertices when such a part exists, take \(q\) vertices there and \(q\) outside it; if every part has fewer than \(q\) vertices, then the total capacity is \(N\ge2q\), so a selection of \(2q\) vertices respecting the cap \(q\) is immediate. Hence the positive degrees are exactly \(2,4,\ldots,2Q\).

Finally, at \(q=1\), paired-dominating sets are precisely pairs from two different parts, namely the edges of \(G\). This yields \(d_p(G,2)=|E(G)|\) and \(\gamma_p(G)=2\).

## Verification
The included `verify.py` constructs every complete multipartite graph whose sorted positive part-size tuple has total order at most \(9\). It enumerates every vertex subset, checks domination directly, tests perfect-matching existence by exact recursive search, and compares the result with the structural characterization and coefficient formula. It also verifies the support interval and the identity \(d_p(G,2)=|E(G)|\).

The finite computation is a regression check rather than an infinite proof; the symbolic proof above is independent of the enumeration.

## Relationship to prior work
Haynes and Slater introduced paired domination in 1998, defining a paired-dominating set as a dominating set whose induced subgraph contains a perfect matching. Puttaswamy, Alwardi, and Nayaka introduced the paired-domination polynomial in 2016; the accessible one-page proceedings record says that the polynomial is computed for some standard graph families, without naming those families.

Targeted literature and database searches using the exact invariant name together with “complete multipartite”, “complete bipartite”, “balance condition”, and coefficient-enumeration language did not locate the arbitrary-part-size characterization or coefficient formula above. The complete-bipartite formula is therefore presented only as a specialization, because it could overlap an unnamed standard-family computation in the 2016 source. The originality-bearing statement is the characterization and coefficient formula for arbitrary \(r\ge2\) and arbitrary positive part sizes.

## Limitations
The accessible 2016 proceedings record is one page and does not identify the standard graph families computed in the underlying work. A separately indexed author-uploaded copy could not be inspected, and the full 1998 article was likewise not available from the accessible sources. Thus a residual risk remains that poorly indexed or inaccessible literature contains a special case. No inspected source states the arbitrary complete-multipartite theorem or coefficient formula given here.

## References
1. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199--206. DOI: https://doi.org/10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F
2. Puttaswamy, Anwar Alwardi, and S. R. Nayaka, “Introduction to Paired Domination Polynomial of a Graph,” *International Journal of Physical and Mathematical Sciences* 10(9) (2016), conference record for ICMAGT 2016, 26--27 September 2016. https://publications.waset.org/abstracts/52964.pdf
