# Exact shattering budgets for fixed-cardinality edge-hit traces and closed neighborhoods of triangular graphs

## Finding
Let \(n\ge2\) and \(1\le r\le n\). Write \(E_n=\binom{[n]}2\). For an \(r\)-element set \(U\subseteq[n]\), put
\[
 R(U)=\{e\in E_n:e\cap U\ne\varnothing\},\qquad
 \mathcal R_{n,r}=\{R(U): |U|=r\}.
\]
A set of edges \(F\subseteq E_n\) is **shattered** when every subset of \(F\) equals \(F\cap R(U)\) for some \(r\)-element \(U\).

**Theorem (exact shattering criterion).** Let \(H_F\) be the graph having the edges \(F\) and precisely their incident vertices; when \(F=\varnothing\), it has no vertices. Then \(F\) is shattered by \(\mathcal R_{n,r}\) if and only if the following three conditions hold:

1. Every component of \(H_F\) is a star \(K_{1,s_i}\) with \(s_i\ge1\) (a single edge is counted once as \(K_{1,1}\)).
2. There are at least \(r\) vertices outside \(V(H_F)\): \(n-|V(H_F)|\ge r\).
3. The **trace budget** satisfies \(\sum_i\max\{1,s_i-1\}\le r\).

The empty edge set satisfies all three conditions by taking the empty component sum.

**Corollary (sharp VC dimension).** The largest shattered set has cardinality
\[
 \operatorname{VCdim}(E_n,\mathcal R_{n,r})
 =\max\left\{0,\min\left(2r,\ n-r-1,\ \left\lfloor\frac n2\right\rfloor\right)\right\}.
\]
More precisely, for each integer \(k\ge1\), a shattered \(k\)-edge set exists if and only if
\[
 k\le2r,\qquad n\ge r+k+1,\qquad n\ge2k.
\]

**Corollary (all shattered sets for triangular graphs).** For \(r=2\), \(\mathcal R_{n,2}\) is exactly the system of closed neighborhoods of vertices of the Johnson graph \(J(n,2)=L(K_n)\): two edges of \(K_n\) lie in each other's closed neighborhood precisely when they intersect. Every nonempty shattered edge set has one of these types, with the indicated minimum \(n\): one edge (\(n\ge4\)); two adjacent edges (\(n\ge5\)); two disjoint edges (\(n\ge6\)); a three-edge star (\(n\ge6\)); a two-edge star plus a disjoint edge (\(n\ge7\)); or two disjoint two-edge stars (\(n\ge8\)). There are no others. Therefore
\[
\operatorname{VCdim}(J(n,2),\text{closed neighborhoods})=
\begin{cases}
0,&n=3,\\
1,&n=4,\\
2,&n=5,\\
3,&n=6,7,\\
4,&n\ge8.
\end{cases}
\]
For \(n\ge3\), let \(s_{n,k}\) be the number of shattered \(k\)-element subsets of \(V(J(n,2))\). With \(\mathbf1_P\) denoting the indicator of condition \(P\), their entire size distribution is
\[
\begin{aligned}
 s_{n,0}&=1,\\
 s_{n,1}&=\mathbf1_{n\ge4}\binom n2,\\
 s_{n,2}&=3\mathbf1_{n\ge5}\binom n3+3\mathbf1_{n\ge6}\binom n4,\\
 s_{n,3}&=4\mathbf1_{n\ge6}\binom n4+30\mathbf1_{n\ge7}\binom n5,\\
 s_{n,4}&=90\mathbf1_{n\ge8}\binom n6,\\
 s_{n,k}&=0\quad(k\ge5).
\end{aligned}
\]

## Assumptions and scope
All graphs are simple and finite. The parameter \(r\) counts chosen **vertices of \(K_n\)**, not chosen edges. The range \(R(U)\) includes every edge meeting \(U\); it is the complement in \(E_n\) of the edge set induced by \([n]\setminus U\). Membership of the center edge in its own neighborhood is essential for the Johnson-graph specialization: these are **closed** neighborhoods, not open neighborhoods. No assertion is made about arbitrary \(J(n,k)\) for \(k\ge3\).

## Proof
**Step 1: singleton traces force a star forest.** Suppose \(F\ne\varnothing\) is shattered. For every edge \(ab\in F\), there is an \(r\)-set \(U\) whose trace on \(F\) is exactly \(\{ab\}\). Necessarily \(a\in U\) or \(b\in U\). The chosen endpoint has degree exactly one in \(H_F\): otherwise its other incident edge would also lie in the trace. Hence every edge of \(H_F\) has at least one degree-one endpoint. Each connected component of a finite graph with this property is a star. Indeed, if a connected component had two vertices of degree at least two, a shortest path between them would contain an edge with both endpoints of degree at least two (the first edge if adjacent; otherwise its next internal vertex also has degree at least two). A component with no such pair has at most one vertex of degree greater than one, hence is a star.

**Step 2: exact cost of a prescribed trace.** Let the nontrivial components of \(H_F\) be stars with disjoint edge sets \(F_i\) of sizes \(s_i\). Fix a requested trace \(T\subseteq F\), and write \(t_i=|T\cap F_i|\). We seek a vertex set meeting **exactly** the edges of \(T\) within \(F\). Its minimum number of vertices chosen from \(V(H_F)\) equals
\[
 C(T)=\sum_i c_{s_i}(t_i),\qquad
 c_s(t)=\begin{cases}
0,&t=0,\\
1,&t=s,\\
t,&0<t<s.
\end{cases}
\]
For a nonempty proper subset of the edges of a star, the hub cannot be selected, and each chosen edge needs its own leaf; for the full edge set the hub alone suffices. Components are vertex-disjoint, so costs add. Consequently
\[
 \max_{T\subseteq F} C(T)=\sum_i\max\{1,s_i-1\}.
\]
For \(s=1\), the maximum cost is one. For \(s\ge2\), it is the larger of one (the full trace) and \(s-1\) (a largest proper trace).

**Step 3: exact equivalence.** A witness for the empty trace must use \(r\) vertices having no incidence with \(F\), hence \(n-|V(H_F)|\ge r\). For every trace \(T\), any witnessing \(r\)-set has at least \(C(T)\) vertices in \(V(H_F)\), so the budget sum is at most \(r\). This proves necessity. Conversely, assume the three stated conditions. For any \(T\subseteq F\), choose within each star an optimal realization from Step 2. Their union has cardinality \(C(T)\le r\). Add \(r-C(T)\) distinct vertices outside \(V(H_F)\); there are at least \(r\) available, and they meet no edge of \(F\). The resulting \(r\)-set realizes \(T\), proving sufficiency.

**Step 4: exact dimension.** Let \(F\ne\varnothing\) have \(k\) edges and \(m\ge1\) star components. Its support has exactly \(k+m\) vertices. If \(a\) components are single edges, its trace budget is
\[
 W=\sum_i\max\{1,s_i-1\}=k-m+a.
\]
For fixed \(k,m\), the smallest achievable \(a\) is \(\max\{0,2m-k\}\). Indeed, every nonsingle-edge star uses at least two edges, yielding \(k\ge a+2(m-a)=2m-a\); the bound is attained by assigning two edges to each remaining component and distributing any surplus edges among those components. Thus
\[
 W_{\min}(k,m)=\max\{m,k-m\}.
\]
There is a shattered \(k\)-edge set exactly when an integer \(m\) satisfies
\[
 1\le m\le k,\quad m\le r,\quad k-m\le r,
 \quad k+m+r\le n.
\]
The smallest feasible \(m\) is \(m_0=\max\{1,k-r\}\). It does not exceed \(\min\{k,r\}\) exactly when \(k\le2r\). Its support requirement is \(n\ge r+k+\max\{1,k-r\}\), equivalent to the stated two inequalities \(n\ge r+k+1\) and \(n\ge2k\). Using the explicit star-size construction just given, these conditions are also sufficient. Maximizing \(k\) proves the displayed VC-dimension formula, including the zero case.

**Step 5: triangular-graph structure and enumeration.** For \(r=2\), the weight budget permits exactly one star of size one, two, or three, or two star components with sizes \((1,1)\), \((2,1)\), or \((2,2)\). Requiring two unused vertices gives each minimum \(n\) above. Labeled single edges number \(\binom n2\). Adjacent and disjoint pairs of edges number \(3\binom n3\) and \(3\binom n4\). Three-edge stars number \(4\binom n4\); a two-edge star with a disjoint edge occurs in \(30\binom n5\) ways; two disjoint two-edge stars occur in \(90\binom n6\) ways. The latter coefficient is \(6!/8=90\), since a pair of two-edge stars on six prescribed vertices has automorphism group of order eight. Imposing the two-outside-vertices condition yields exactly the displayed \(s_{n,k}\) formulas. The largest nonzero degree gives the five-case closed-neighborhood VC-dimension formula.

## Verification
The self-contained file `verify.py` constructs the actual edge-incidence traces for every \(r\)-vertex witness and separately tests the three-condition structural criterion. It checks all edge subsets for \(2\le n\le6\), for every \(1\le r\le n\); checks all edge subsets of size at most four for \(n=7,8\), again for every \(r\); and independently counts all shattered sets of cardinalities zero through four in triangular graphs with \(3\le n\le8\). The execution was successful with the final line `VERIFY_OK uniform_starforest=PASS exact_vc=PASS triangular_enumeration=PASS`. General validity follows from Steps 1--5 rather than from finite testing.

## Relationship to prior work
Adler, Benediktsson, and Macpherson (arXiv:2007.16042, first public 2020-07-31) prove that the **open** neighborhood VC dimension of the Johnson-graph family is at most four, with equality for \(J(n,2)\) already at \(n=7\) (their Theorem 3.7 and Figure 4). Their closed-neighborhood statement gives boundedness, not the classification or the threshold established here. Coudert, Csikós, Ducoffe, and Viennot (arXiv:2405.07588, first public 2024-05-13) treat **closed** graph neighborhoods and their algorithmic computation, but do not state this family-specific formula in their manuscript. Byrne, Byrne, and Cioabă (arXiv:2609.10330, Section 4) explicitly study **open** neighborhoods of strongly regular graphs and recount the known dimension-four fact for sufficiently large triangular graphs; their open-neighborhood parameter does not settle the present closed case. The unrestricted induced-edge trace family has a star-forest obstruction; imposing the cardinality constraint on the vertex witnesses is the extra ingredient responsible for the sharp budget and the exceptional orders. In particular, one must not infer the current criterion merely from the unrestricted star-forest statement.

## Limitations
The proof concerns the fixed-size edge-hit range system on a complete graph and its triangular-graph specialization, not closed balls in general Johnson graphs. It counts shattered edge sets, not all possible distinct traces on arbitrary edge families. The comparisons do not establish absolute publication priority; alternative treatments under partial vertex covers, incidence hypergraphs, or Boolean trace terminology remain a residual risk. There is no independent external audit.

## References
1. I. Adler, B. G. Benediktsson, and D. Macpherson, *Vapnik--Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first posted 2020-07-31, https://arxiv.org/abs/2007.16042.
2. D. Coudert, M. Csikós, G. Ducoffe, and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588, first posted 2024-05-13, https://arxiv.org/abs/2405.07588.
3. I. Byrne, J. Byrne, and S. M. Cioabă, *The VC-dimension of strongly regular graphs*, arXiv:2609.10330, first posted 2026-09-09, https://arxiv.org/abs/2609.10330.
