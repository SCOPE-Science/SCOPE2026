# Roman-domination polynomial of triangular graphs, with minimum-function census

## Finding

For an integer \(n\ge5\), let \(T_n=L(K_n)=J(n,2)\) be the triangular graph: its vertices are the two-element subsets of \([n]\), adjacent when they intersect in one element. A Roman dominating function is \(f:V(T_n)\to\{0,1,2\}\) such that every vertex of label zero has an adjacent vertex of label two. Define the full weight polynomial
\[
R_n(z)=\sum_{f\text{ Roman dominating}}z^{\sum_{v\in V(T_n)}f(v)}.
\]
Put \(M=\binom n2\), and for integers \(c\ge2\) and \(0\le k\le\binom c2\) put
\[
A_{c,k}=\sum_{j=0}^{c}(-1)^j\binom cj\binom{\binom{c-j}{2}}k,
\]
where a binomial coefficient with lower argument outside its allowed range is zero. Then, for every \(n\ge5\),
\[
\boxed{
R_n(z)=z^M+\sum_{c=2}^{n}\binom nc
\sum_{k=1}^{\binom c2}A_{c,k}
 z^{2k+\binom{n-c}{2}}
 (1+z)^{M-k-\binom{n-c}{2}}.}
\]
In particular, the minimum exponent is \(n-1\), and its coefficient is
\[
\boxed{[z^{n-1}]R_n(z)=
\begin{cases}
 n(n-2)!!,&n\text{ odd},\\
 \binom n2(n-3)!!,&n\text{ even}.
\end{cases}}
\]
Here the odd double factorial \((2s-1)!!\) is the product of the positive odd integers not exceeding \(2s-1\). Every minimum-weight function is uniquely of one of these types: for odd \(n\), choose one uncovered original vertex and label the edges of a perfect matching of the other \(n-1\) vertices by two, all other edges by zero; for even \(n\), choose two uncovered original vertices, label the edges of a perfect matching of the other \(n-2\) vertices by two, label the edge between the uncovered vertices by one, and label all remaining edges by zero.

## Assumptions and scope

All graphs are finite, simple and undirected, with labeled original vertices \([n]\). The polynomial counts labeled functions, including functions using no label two. The theorem is asserted for \(n\ge5\); smaller triangular graphs are already encompassed by complete-graph or complete-multipartite cases. The formula is an explicit finite sum of nonnegative-integer coefficient polynomials although \(A_{c,k}\) is expressed by alternating inclusion-exclusion. A selected edge refers to a vertex of \(T_n\); its endpoints refer to original vertices of \(K_n\). No randomness or genericity assumptions are made.

## Proof

**Support decomposition.** Fix any Roman function \(f\) and let \(H\subseteq E(K_n)\) be exactly the original edges given label two. If \(H=\varnothing\), no vertex may have label zero, and the unique such function labels all \(M\) vertices by one, giving \(z^M\). Suppose \(H\ne\varnothing\), and write \(C\) for the set of endpoints incident with some edge of \(H\), \(c=|C|\), \(r=n-c\), and \(k=|H|\). The spanning graph \((C,H)\) has no isolated vertices by the definition of \(C\). An original edge \(e\notin H\) is adjacent in \(T_n\) to a vertex labeled two exactly when \(e\) has an endpoint in \(C\). Thus every edge of the complementary complete graph on \([n]\setminus C\) is *forced* to carry label one, while each of the remaining \(M-k-\binom r2\) edges outside \(H\) may independently carry zero or one. With fixed \(H\), the weight enumerator is precisely
\[
z^{2k+\binom r2}(1+z)^{M-k-\binom r2}.
\]
Conversely, every labeling constructed this way obeys the Roman condition, so the decomposition is bijective and no functions are counted twice.

**Counting selected supports.** Once \(C\) is specified, the possible sets \(H\) with \(k\) edges and exactly endpoint set \(C\) are precisely the labeled simple graphs on \(C\) with \(k\) edges and no isolated vertices. By inclusion-exclusion over vertices of \(C\) that are isolated, their number is
\[
A_{c,k}=\sum_{j=0}^{c}(-1)^j\binom cj\binom{\binom{c-j}{2}}k.
\]
There are \(\binom nc\) choices of \(C\). Summing the preceding fixed-support enumerator yields the boxed polynomial, with all exponents nonnegative because \(k\le\binom c2\le M-\binom r2\).

**Minimum-weight profiles.** If \(H\ne\varnothing\), the number \(k\) of two-labeled edges satisfies \(2k\ge c=n-r\). Every function therefore has weight at least
\[
2\left\lceil\frac{n-r}{2}\right\rceil+\binom r2
=n+\frac{r(r-3)}2+\epsilon_r,
\qquad\epsilon_r\in\{0,1\},\quad
\epsilon_r\equiv n-r\pmod 2.
\]
The restriction \(2\le c\le n\) means \(0\le r\le n-2\). For odd \(n\), the bound equals \(n-1\) only when \(r=1\); for even \(n\), only when \(r=2\). To see this without an asymptotic argument, check \(r=0,1,2,3\) directly, and observe that the displayed bound exceeds \(n-1\) for every \(r\ge4\). The no-two function has weight \(M>n-1\) for \(n\ge5\).

In the unique minimizing \(r\)-case, \(c=n-r\) is even and equality forces \(k=c/2\), which forces \((C,H)\) to be a perfect matching. Equality also forbids optional label-one edges: all are labeled zero. The forced one-label edges comprise none when \(r=1\), and exactly the edge joining the two uncovered vertices when \(r=2\). Each such function is valid by the support characterization. For odd \(n\), choose the uncovered vertex in \(n\) ways and a perfect matching on \(n-1\) labeled vertices in \((n-2)!!\) ways. For even \(n\), choose the two uncovered vertices in \(\binom n2\) ways and a perfect matching on \(n-2\) labeled vertices in \((n-3)!!\) ways. The stated coefficient and structural classification follow.

## Verification

The standalone standard-library script `verify.py` builds the stated polynomial by inclusion-exclusion and checks it against direct enumeration of **all** Roman labelings for \(0\le n\le5\), where the small cases are verification boundary tests rather than part of the new claim. An independent enumeration first chooses each possible subset of two-labeled edges and then counts all freely selected one-labeled edges; its full coefficient dictionaries agree through \(n=6\). The minimum exponent and multiplicity formulas are checked for every \(3\le n\le18\). The script and its captured output are included with this result. Exhaustive finite checks are not used to infer the theorem for infinitely many orders; that conclusion follows from the proof above.

## Relationship to prior work

Roman domination and its edge version are established notions. The edge version on \(K_n\) is exactly Roman domination on \(L(K_n)\); this equivalence is essential, not a novelty claim. Pushpam and Mai (2009) introduced edge Roman domination and proved general and small-parameter results; Chang, Chen and Liu (2014) established general bounds and the complete-bipartite scalar case. Gangabylaiah, Indiramma, Soner and Alwardi (2021) introduced the all-weight Roman domination polynomial and gave formulas for stars, wheels, complete bipartite graphs, joins and certain coronas; none of these constructions determines the triangular graph family (indeed, for \(n\ge5\), the complement of \(T_n\) is connected, so \(T_n\) is not a nontrivial graph join). Abu-Khzam, Fernau and Mann (2022) studied algorithms for enumerating **minimal** Roman dominating functions on split graphs, forests, interval graphs and related classes, a different enumeration task. Deepak and coauthors (2023) tabulated Roman polynomials for all connected graphs of order at most six; the smallest \(T_n\) are necessarily among such tables. Published Roman-polynomial results for complete multipartite graphs likewise cover the small special cases \(T_3\cong K_3\) and \(T_4\cong K_{2,2,2}\), but do not imply the polynomial for \(n\ge5\), for which nonadjacency in \(T_n\) is not transitive.

The new claim is specifically the explicit **all-weight** coefficient enumeration and complete minimum-function profile for the infinite family \(n\ge5\). Existing scalar upper bounds, minimal-function algorithms, and finite small-graph tables do not imply it. Potential undiscovered equivalent formulae under the terminology of *edge Roman domination of complete graphs* are a residual originality risk.

## Limitations

The formula is an exact finite sum, not a proved asymptotic estimate or a closed factorization of its zeros. Its coefficients can be large, and direct evaluation may be computationally costly for large \(n\); no complexity improvement is asserted. No claim is made that the scalar minimum parameter was previously unknown, nor that the all-weight distribution determines graph isomorphism. The edge-Roman reformulation on complete graphs is equivalent to the stated Roman-polynomial question, and is therefore an explicit route for future equivalence checks.

## References

1. P. Roushini Leely Pushpam and T. N. M. Malini Mai, “Edge Roman Domination in Graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* **69** (2009), 175–182. https://combinatorialpress.com/article/jcmcc/Volume%20069/vol-069-paper%2019.pdf
2. G. J. Chang, S.-H. Chen, and C.-H. Liu, “Edge Roman domination on graphs,” arXiv:1405.5622 (first posted 2014-05-22), *Graphs and Combinatorics* **32** (2016), 1731–1747. https://arxiv.org/abs/1405.5622
3. D. Gangabylaiah, M. H. Indiramma, N. D. Soner, and A. Alwardi, “On the Roman domination polynomial of graphs,” *Bulletin of the International Mathematical Virtual Institute* **11** (2021), 355–365. https://www.imvibl.org/buletin/bulletin_imvi_11_2_2021/bulletin_imvi_11_2_2021_355_365.pdf
4. F. N. Abu-Khzam, H. Fernau, and K. Mann, “Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes,” arXiv:2208.05261 (first posted 2022-08-10). https://arxiv.org/abs/2208.05261
5. Deepak G., N. Manjunath, R. Manjunatha, J. M. Shashidhara, and A. Alqesmah, “An Atlas of Roman Domination Polynomials of Graphs of Order at Most Six,” *International Journal of Mathematical Combinatorics* **2** (2023), 87–104. https://fs.unm.edu/IJMC/IJMC-2-2023.pdf
