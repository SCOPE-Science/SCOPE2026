# Zero forcing polynomial of clique-path lollipop graphs
## Finding
For integers \(k\ge3\) and \(\ell\ge1\), let \(L(k,\ell)\) be the clique-path lollipop obtained from a clique \(\{a\}\cup X\cong K_k\), where \(|X|=k-1\), by joining \(a\) to the first vertex \(p_1\) of a path \(p_1,\ldots,p_\ell\). For an initial blue set \(S\), put \(W_X=X\setminus S\).

Then \(S\) is zero forcing if and only if exactly one of the following structural alternatives holds:

1. \(|W_X|=0\).
2. \(|W_X|=1\) and \(a\in S\).
3. \(|W_X|=1\), \(a\notin S\), and the selected path vertices contain \(p_\ell\) or contain two consecutive path vertices.

No set with \(|W_X|\ge2\) is zero forcing.

Let
\[
I_{\ell-1}(x)=\sum_{j=0}^{\lfloor\ell/2\rfloor}\binom{\ell-j}{j}x^j.
\]
This is the independence polynomial of the path on \(\ell-1\) vertices. The exact zero forcing polynomial is
\[
\mathcal Z(L(k,\ell);x)
=x^{k-1}(1+x)^{\ell+1}
+(k-1)x^{k-1}(1+x)^\ell
+(k-1)x^{k-2}\bigl((1+x)^\ell-I_{\ell-1}(x)\bigr).
\]
In particular,
\[
Z(L(k,\ell))=k-1,
\]
and there are exactly \(2k-1\) minimum zero forcing sets. They are \(X\), the \(k-1\) sets \((X\setminus\{u\})\cup\{a\}\), and the \(k-1\) sets \((X\setminus\{u\})\cup\{p_\ell\}\), with \(u\in X\).

## Assumptions and scope
All graphs are finite, simple, and undirected. A blue vertex may force its unique white neighbor blue. A set is zero forcing if repeated legal forces eventually color every vertex blue.

The result concerns the nondegenerate clique-path lollipops with \(k\ge3\) and \(\ell\ge1\). The boundary \(k=2\) is a path and is deliberately excluded; its zero forcing polynomial is already covered by the known path formula. The boundary \(\ell=0\) is a complete graph and is likewise classical.

The polynomial counts every zero forcing set by cardinality:
\[
\mathcal Z(G;x)=\sum_{S\text{ zero forcing}}x^{|S|}.
\]

## Proof
Suppose first that at least two vertices of \(X\) are white. Every vertex adjacent to one of those white clique vertices is adjacent to all of them: the only possible forcing vertices are in the clique, and each such blue clique vertex sees at least two white vertices in \(X\). Path vertices see no vertex of \(X\). Hence no omitted vertex of \(X\) can be the first one forced. Therefore \(|W_X|\ge2\) is impossible for a zero forcing set.

Now suppose \(|W_X|=0\). If \(a\) is initially white, any blue vertex of \(X\) forces \(a\). Once \(a\) is blue, the path clears from its clique end: if \(p_1\) is white then \(a\) forces \(p_1\), and the force propagates along the path; if \(p_1\) is already blue, the same propagation starts at \(p_1\). Thus every set containing all of \(X\) is zero forcing.

Next suppose \(|W_X|=1\), say \(W_X=\{u\}\), and \(a\in S\). Because \(k\ge3\), at least one vertex of \(X\setminus\{u\}\) is blue. Such a vertex has \(u\) as its unique white neighbor in the clique and therefore forces \(u\). The path then clears from \(a\) exactly as above. Hence every set in alternative 2 is zero forcing.

It remains to treat \(|W_X|=1\) with \(a\notin S\). Initially every blue vertex of \(X\setminus W_X\) has the two white clique neighbors \(a\) and the unique vertex of \(W_X\), so the clique cannot move before \(a\) becomes blue.

If \(p_\ell\in S\), the terminal path vertex forces leftward until \(p_1\) is blue; then \(p_1\) forces \(a\), after which the clique clears. If instead two consecutive path vertices are blue, the left member of some consecutive blue pair starts a leftward forcing chain until \(p_1\) is blue, and again \(p_1\) forces \(a\). This proves sufficiency of alternative 3.

Conversely, assume that \(p_\ell\notin S\) and that no two selected path vertices are consecutive. Every selected internal path vertex then has two white path neighbors, while a selected \(p_1\) has the two white neighbors \(a\) and \(p_2\) when \(\ell\ge2\). For \(\ell=1\), the assumption \(p_\ell\notin S\) means the path has no selected vertex. Thus no path force can start, while the clique is already frozen by the two white vertices \(a\) and \(W_X\). The process is stuck. This proves necessity and completes the set classification.

To count, alternative 1 contributes
\[
x^{k-1}(1+x)^{\ell+1}.
\]
Alternative 2 contributes
\[
(k-1)x^{k-1}(1+x)^\ell.
\]
For alternative 3, choose the unique omitted vertex of \(X\) in \(k-1\) ways. A path subset is bad precisely when it omits \(p_\ell\) and is independent on \(p_1,\ldots,p_{\ell-1}\). The size enumerator of those bad subsets is \(I_{\ell-1}(x)\), so the good path subsets contribute \((1+x)^\ell-I_{\ell-1}(x)\). Summing the three disjoint alternatives yields the displayed polynomial.

The least possible degree is \(k-1\). It is attained by \(X\); by each set \((X\setminus\{u\})\cup\{a\}\); and, in alternative 3, only by \((X\setminus\{u\})\cup\{p_\ell\}\). Hence there are exactly \(1+(k-1)+(k-1)=2k-1\) minimum sets.

## Verification
The standalone script `verify.py` independently constructs the lollipop graphs, simulates the zero forcing rule on every vertex subset, checks the structural criterion above, compares the complete coefficient vector with the closed polynomial, and checks the minimum-set count. It tests every pair \((k,\ell)\) with \(3\le k\le6\) and \(1\le\ell\le8\), reaching order \(14\).

The packaged artifact reports the exact finite totals shown in `VERIFICATION.md`. These computations stress-test the statement and its small boundaries; the infinite result follows from the proof above.

## Relationship to prior work
The standard zero forcing rule was introduced in the 2008 AIM Minimum Rank--Special Graphs Work Group paper. Its published version records online availability on 26 November 2007 and AMS classification 05C50.

Aalipour and coauthors use exactly the clique-path lollipop notation \(L(k,\ell)\): a \(k\)-clique attached by one edge to an endpoint of a path on \(\ell\) vertices. Their lollipop section determines distance-matrix determinants and inertias. Although that paper recalls zero forcing elsewhere as a tool for bounding distance-eigenvalue multiplicities, the lollipop section does not classify zero forcing sets.

Boyer and coauthors introduced the zero forcing polynomial and proved exact formulas for several graph families. Their accessible full text contains no occurrence of “lollipop.” It does give the useful path fact that a subset is nonforcing precisely when it contains neither an endpoint nor two adjacent path vertices; that fact is consistent with, but does not imply, the extra clique-boundary condition proved here.

Menon and Singh later studied how graph operations affect the coefficients of the zero forcing polynomial, including path-based operations and coefficient inequalities. Those general comparison tools do not state the exact all-set classification or polynomial for clique-path lollipops.

The scalar equality \(Z(L(k,\ell))=k-1\) is not presented as the main novelty: minimum zero forcing values can often be accessible from broader structural or path-cover arguments. The retained contribution is the exact if-and-only-if description of every zero forcing set, the resulting closed polynomial, and the complete count and description of all minimum sets.

## Limitations
The theorem is restricted to \(k\ge3\) and \(\ell\ge1\); the path and complete-graph boundaries are excluded because they are already classical. The exhaustive computation reaches order \(14\) and is corroborative rather than a proof. Focused searches covered the standard lollipop, generalized-barbell, clique-path, zero-forcing-polynomial, and hanging-path formulations, but unindexed theses or older specialized literature remain a residual originality risk.

## References
1. AIM Minimum Rank--Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009. Available online 26 November 2007.
2. G. Aalipour, A. Abiad, Z. Berikkyzy, J. Cummings, J. De Silva, W. Gao, K. Heysse, L. Hogben, F. H. J. Kenter, J. C.-H. Lin, and M. Tait, “On the distance spectra of graphs,” arXiv:1509.01196, first posted 3 September 2015.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910, first posted 26 January 2018.
4. K. Menon and A. Singh, “Exploring the Influence of Graph Operations on Zero Forcing Sets,” arXiv:2405.01423, first posted 2 May 2024; later published in *Discrete Mathematics* 348 (2025), article 114516.
