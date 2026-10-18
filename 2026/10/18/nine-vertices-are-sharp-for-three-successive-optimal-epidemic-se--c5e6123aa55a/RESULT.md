# Nine vertices are sharp for three successive optimal epidemic sentinels on trees

## Finding
Let \(T\) be a finite undirected tree on \(n\ge2\) vertices. Each edge is independently open with probability \(p\in(0,1)\), and one vertex is selected uniformly as the outbreak seed. A single perfect sentinel detects the outbreak if it is connected to the seed by open edges. Call a vertex **uniquely optimal** at \(p\) when it strictly maximizes detection probability over all vertices.

**Sharp minimum.** No tree with at most eight vertices has three distinct vertices, each uniquely optimal for some transmissibility in \((0,1)\). A tree on nine vertices has precisely three successive unique optimal choices, with two exact interior crossovers.

Specifically, use vertices \(0,1,\ldots,8\) and edges
\[
\{01,12,05,23,34,56,67,68\}.
\]
Write \(C_v(p)=\sum_{u\ne v}p^{\operatorname{dist}_T(u,v)}\). Its detection probability is \((1+C_v(p))/9\). Define \(r\) as the unique root of \(r^4+r^3+r^2+r-1=0\) in \((0,1)\), and \(s=(\sqrt5-1)/2\). Then \(0<r<s<1\), and the unique optimal sentinel is vertex \(6\) when \(0<p<r\), vertex \(5\) when \(r<p<s\), and vertex \(0\) when \(s<p<1\). At \(r\), vertices \(6\) and \(5\) tie at the maximum; at \(s\), vertices \(5\) and \(0\) tie. No other maximizers occur.

## Assumptions and scope
The contact graph is a tree; all edges open independently with a common probability \(p\); the seed is uniform over the full vertex set, including the sentinel; the sentinel detects only eventual infection, perfectly and without delay. The model is a finite bond-percolation epidemic, not a claim about general continuous-time SIR models with correlated transmissions. The uniqueness assertion concerns strict maximizers on open parameter intervals, not tied vertices at isolated parameter values or indistinguishable symmetric vertices.

## Proof
**Detection-polynomial reduction.** In a tree there is one path between every seed \(u\) and sentinel \(v\), with \(d(u,v)\) edges. The path is open with probability \(p^{d(u,v)}\). Averaging over the uniformly selected seed gives \(\Pr(\text{detect at }v)=(1+C_v(p))/n\). Thus optimizing detection is exactly maximizing the classical decay-centrality polynomial.

**A finite lower-bound certificate.** Let \(a_j(v)\) denote the number of other vertices distance exactly \(j\) from vertex \(v\), completed by zeros through \(j=n-1\). Let \(A_j(v)=\sum_{i=1}^j a_i(v)\). Summation by parts yields
\[
C_u(p)-C_v(p)=(1-p)\sum_{j=1}^{n-2}\big(A_j(u)-A_j(v)\big)p^j.
\]
(At \(j=n-1\), both cumulative counts equal \(n-1\).) If \(A_j(u)\ge A_j(v)\) for all \(j\), with one strict inequality, then \(C_u(p)>C_v(p)\) for every \(p\in(0,1)\). Identical distance profiles give identical polynomials and cannot both be uniquely optimal. Hence a uniquely optimal vertex must have a **nondominated** cumulative-distance profile.

The accompanying standard-library program enumerates every unlabeled tree through eight vertices by repeated leaf attachment followed by rooted-center canonicalization. Completeness follows inductively: every tree with at least two vertices has a leaf; deleting one leaf yields a smaller tree, and every reattachment location is considered. Center-rooted parenthesis codes, sorted across children and compared across the one or two centers, are exact isomorphism invariants for trees. The resulting counts of unlabeled trees for orders \(1\) through \(8\) are \(1,1,1,2,3,6,11,23\). Among all these trees, the largest numbers of different nondominated cumulative-distance profiles at orders \(1\) through \(8\) are \(1,1,1,1,1,2,2,3\). Exactly one unlabeled eight-vertex tree has three profiles. For this exceptional tree, two of the three candidates have the exact decay-polynomial difference \(p^2(1-p)^2>0\). The third candidate cannot produce a third uniquely optimal vertex because one of these two is never optimal. Every other tree has at most two nondominated profiles. This proves the lower bound for every real \(p\in(0,1)\); it does not rest on parameter-grid sampling.

**The nine-vertex upper bound.** For the displayed witness, direct breadth-first distance enumeration gives
\[
\begin{aligned}
C_6(p)&=3p+p^2+p^3+p^4+p^5+p^6,\\
C_5(p)&=2p+3p^2+p^3+p^4+p^5,\\
C_0(p)&=2p+2p^2+3p^3+p^4.
\end{aligned}
\]
All other vertices have cumulatively dominated distance profiles: vertex \(1\) by vertex \(0\), vertex \(2\) by \(0\) or \(5\), and each of vertices \(3,4,7,8\) by at least one of \(0,5,6\). The exact finite checker confirms these strict dominance comparisons and prints the distance arrays.

Factorization gives
\[
\begin{aligned}
C_6(p)-C_5(p)&=p(1-p)(1-p-p^2-p^3-p^4),\\
C_5(p)-C_0(p)&=p^2(1-p)(1-p-p^2).
\end{aligned}
\]
The expressions in parentheses are strictly decreasing on \((0,1)\), starting positive and ending negative, hence each has exactly one zero there. At \(p=s\), \(s+s^2=1\) and \(s^3+s^4>0\), so the first parenthesis is already negative; consequently \(r<s\). The signs in successive intervals imply the claimed unique maximizing vertices and exactly two ties at the two crossing values. This completes the sharpness proof.

## Verification
Run `python3 verify_three_sentinel_winners.py` using Python 3 standard library only. It constructs all unlabeled trees of orders at most eight, recomputes each vertex's shortest-path distance histogram, checks profile dominance, identifies the sole eight-vertex exception, and checks its exact polynomial difference \(p^2(1-p)^2\) coefficientwise. It also rebuilds the nine-vertex example, verifies both polynomial factorizations via exact integer coefficient convolution, confirms the dominance of all other vertices, and locates the two roots numerically for display only. Every mathematical all-parameter assertion follows from the displayed algebra, strict monotonicity, and the finite exhaustive enumeration; the decimal roots are not proof certificates. Executed verifier output: orders \(1\)–\(8\) have \(1,1,1,2,3,6,11,23\) trees; the exceptional order-eight count is \(1\); both exact witness identities pass.

## Relationship to prior work
Tsakas (2016, arXiv:1604.05582) studies maximizing decay centrality, proves proximity to degree and closeness maximizers near the endpoints of the decay parameter, and reports intermediate-parameter behavior in random graphs. Hurajová, Gago and Madaras (2018) develop decay-centrality ranking comparisons and enumerate **ranking-stable** trees; their Proposition 2.2 supplies the cumulative-distance dominance principle, and their Table 1 gives aggregate stable-tree counts. A change anywhere in the entire vertex ranking is much weaker than a change of the **unique global maximizer**, and neither work's inspected theorems or tables states the sharp three-maximizer boundary at order nine with these two exact transition polynomials. The new claim uses their established concepts without claiming the general decay measure or the dominance lemma as new. Newman (2002) provides background on network epidemic-percolation modeling. Because the surveillance objective reduces exactly to decay centrality, other centrality literature could contain equivalent formulations; the novelty assessment is not an exhaustive mathematical bibliography.

## Limitations
The lower bound is exact for all trees through order eight only, not for general connected graphs or directed networks. Existence at order nine does not characterize all nine-vertex witnesses or larger trees. Transmissibilities refer to independent edge states and eventual reachability; not to detection time, adaptive sentinel choices, nonuniform seeds, multiple sentinels, or heterogeneous contacts. Literature searches do not establish absolute historical priority, and independent external scientific audit is not performed.

## References
1. N. Tsakas, *On Decay Centrality*, arXiv:1604.05582, first posted April 19, 2016; openly accessible 2016 working paper at https://papers.econ.ucy.ac.cy/RePEc/papers/04-16.pdf.
2. J. Coroničová Hurajová, S. Gago and T. Madaras, *On decay centrality in graphs*, Mathematica Scandinavica 123 (2018), 39–50, doi:10.7146/math.scand.a-106210; accessible full text at https://journals.msp.org/mscand/article/download/263/262/291.
3. M. E. J. Newman, *The spread of epidemic disease on networks*, arXiv:cond-mat/0205009, initially posted April 30, 2002.
