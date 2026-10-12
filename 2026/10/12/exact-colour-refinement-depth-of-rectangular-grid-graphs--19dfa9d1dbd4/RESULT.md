# Exact colour-refinement depth of rectangular grid graphs

## Finding

Let \(2\le m\le n\) be integers, and let \(G_{m,n}=P_m\square P_n\) be the simple, uncoloured Cartesian product of paths on \(m\) and \(n\) vertices. Start ordinary one-dimensional colour refinement with one uniform colour at round \(0\). Its exact stabilization round is
\[
\operatorname{Stab}(G_{m,n})=
\begin{cases}
\lfloor (m-1)/2\rfloor,&m=n,\\
\max\{m-1,\lfloor(n-1)/2\rfloor\},&m<n.
\end{cases}
\]
At that round, the colour classes are **exactly the vertex-automorphism orbits**. Writing \(k_m=\lceil m/2\rceil\) and \(k_n=\lceil n/2\rceil\), their number is
\[
\begin{cases}
k_m(k_m+1)/2,&m=n,\\
k_mk_n,&m<n.
\end{cases}
\]
In particular, the exact depth jumps from \(\lfloor (m-1)/2\rfloor\) on the square \(P_m\square P_m\) to \(m-1\) on the immediately non-square grid \(P_m\square P_{m+1}\).

## Assumptions and scope

Vertices of \(P_\ell\) are \(0,1,\ldots,\ell-1\); adjacent integers are joined. A vertex of \(G_{m,n}\) is \((i,j)\), and its four distances to the containing rectangle's sides, measured in grid edges perpendicular to each side, are \(i\), \(m-1-i\), \(j\), and \(n-1-j\). Colour refinement is the canonical partition sequence \(c_0,c_1,\ldots\), where \(c_0\) is constant and \(c_{t+1}(v)\) is determined injectively by \(c_t(v)\) and the multiset of colours of its neighbours. The stabilization round is the **least** \(t\ge0\) for which the partitions of \(c_t\) and \(c_{t+1}\) coincide. In particular, a vertex-transitive graph has depth \(0\) under this convention.

## Proof

**1. Walk moments are determined by refinement colours.** Let \(A\) denote a graph's adjacency matrix and let \(w_k(v)=(A^k\mathbf1)_v\), the number of \(k\)-step walks starting at \(v\). If two vertices have the same colour at round \(t\), they have equal \(w_k\) for all \(0\le k\le t\): use induction on \(k\), since \(w_{k+1}(v)=\sum_{u\sim v}w_k(u)\). Consequently, if the vectors of the first \(t\) walk moments separate some vertex types, colour refinement separates them by round \(t\).

**2. Boundary distances can be read from short walk moments.** Let
\[
Q_{\ell,i}(z)=\sum_{k\ge0}(A_{P_\ell}^k\mathbf1)_i\frac{z^k}{k!}.
\]
Let \(e_k(a)\) count length-\(k\) walks with steps \(+1\) or \(-1\) on the entire integer line, starting at \(a\ge0\), which visit \(-1\) at some time. Put \(E_a(z)=\sum_{k\ge0}e_k(a)z^k/k!\), and
\[
F_a(z)=\log\bigl(1-e^{-2z}E_a(z)\bigr).
\]
As \(e_k(a)=0\) when \(k<a+1\) and \(e_{a+1}(a)=1\), \(F_a\) starts with \(-z^{a+1}/(a+1)!\).

For \(0\le i<\ell\), a walk of at most \(\ell\) steps starting at \(i\) cannot visit both forbidden sites \(-1\) and \(\ell\), because those sites are \(\ell+1\) steps apart. Comparing unconstrained walks on the integer line with walks staying inside the path gives
\[
Q_{\ell,i}(z)\equiv e^{2z}-E_i(z)-E_{\ell-1-i}(z)
\pmod {z^{\ell+1}}.
\]
Taking formal logarithms and using that the first mixed term has degree \((i+1)+(\ell-i)=\ell+1\) gives the sharper additive description
\[
\log Q_{\ell,i}(z)\equiv 2z+F_i(z)+F_{\ell-1-i}(z)
\pmod {z^{\ell+1}}. \tag{1}
\]
Here the logarithm is formal; every series has constant coefficient \(1\) before the logarithm is taken.

For grid vertices, the adjacency matrix is a Kronecker sum, so the exponential walk-generating function factors:
\[
Q_{m,n;(i,j)}(z)=Q_{m,i}(z)Q_{n,j}(z).
\]
By (1), modulo \(z^m\),
\[
\log Q_{m,n;(i,j)}(z)
\equiv4z+F_i(z)+F_{m-1-i}(z)+F_j(z)+F_{n-1-j}(z).\tag{2}
\]
For every \(1\le r\le m-1\), its coefficients through degree \(r\) determine the multiset of side distances **strictly below** \(r\). Indeed, \(F_a\) starts in degree \(a+1\) with nonzero coefficient \(-1/(a+1)!\). Inductively, after the multiplicities of smaller \(a\)'s are known, the degree \(r\) coefficient determines the multiplicity of \(a=r-1\). Since formal logarithms preserve equality of truncated series, the walk moments through order \(r\) determine this truncated multiset.

**3. The square case.** Put \(m=n\) and \(p=\lfloor(m-1)/2\rfloor\). A coordinate has a nearest-side distance \(a\le p\). Among its two side distances, exactly one occurs below \(p\) if \(a<p\), and none if \(a=p\). Thus the multiset of side distances below \(p\) determines the unordered pair of nearest-side distances \(\{a,b\}\) for \((i,j)\), including the missing central values by subtraction. Reflections and interchange of coordinates map all vertices with the same unordered pair to one another. Equation (2) therefore shows that walk moments through \(p\) separate every reflection/axis-swap orbit. By step 1, colour refinement has reached the orbit partition by round \(p\), which is then stable.

**4. Unequal sides.** Assume \(m<n\), set \(s=m-1\), and write \(a=\min\{i,s-i\}\). The multiset of side distances below \(s\), obtained from (2) at order \(s\), determines \(a\). Here is an elementary uniqueness argument. If \(a>0\), both short-side distances \(\{a,s-a\}\) appear in the truncated multiset; if \(a=0\), only the value \(0\) appears from the short pair. Two different positive choices \(a,a'\) have disjoint two-element short pairs: otherwise a common element and its complement to \(s\) force the pairs to agree. The truncated multiset would then have to contain both entire pairs, exhausting all four side distances, so the long pair would sum to \(s\) rather than \(n-1>s\), an impossibility. If one candidate is \(a=0\) and another is \(a'>0\), then, in the second representation, the required zero must come from the long pair; its complementary long distance \(n-1\) is not below \(s\). The other two observed entries would therefore be precisely \(\{a',s-a'\}\). In the first representation they would be the two long distances, but their sum is \(s\), not \(n-1\). This too is impossible. Hence the shorter-coordinate reflection class is fixed by moments through \(m-1\).

Now let \(R=\max\{m-1,\lfloor(n-1)/2\rfloor\}\). If two grid vertices have equal walk moments through \(R\), step 4's first paragraph makes their shorter coordinates equal up to reflection. Their factors \(Q_{m,i}\) are then identical as formal series. Dividing \(Q_{m,n;(i,j)}=Q_{m,i}Q_{n,j}\) by this common series shows their longer path factors \(Q_{n,j}\) agree through degree \(R\). But a vertex at distance \(b\) from the nearer endpoint of \(P_n\) first loses an unrestricted-line walk at degree \(b+1\). Hence the moments through \(\lfloor(n-1)/2\rfloor\) distinguish all values of \(b\). The two grid vertices thus have equal \(b=\min\{j,n-1-j\}\). Reflections of the two coordinates map vertices with equal \((a,b)\) to one another; by step 1, at round \(R\) the colour classes have become precisely these orbits. They are stable.

**5. Sharpness.** The colour at round \(t\) depends only on the unlabelled rooted tree formed by unfolding all walks from the root to depth \(t\). Equivalently, a boundary first encountered at distance \(t\) affects degrees at round \(t+1\), not sooner. For every path length \(n\ge3\), writing \(p=\lfloor(n-1)/2\rfloor\), fix the first grid coordinate and compare second coordinates \(p-1\) and \(p\). The rooted unfoldings through depth \(p-1\) agree by translation along the longer path: none of their vertices at depth below \(p-1\) encounters a long-side boundary. Their nearest-long-side distances differ, so step 3 or step 4 proves that they are eventually separated. Thus the stabilization round is at least \(p\) (when \(p=0\) this bound is vacuous).

When \(m<n\), also compare \(u=(1,0)\) and \(v=(0,1)\). Interchanging the two lattice directions identifies their rooted unfolded walk trees through depth \(m-2\): the first unmatched opposite short side is reached by \(u\) at that depth but, since the vertices at the deepest level are still uncoloured, its missing outward neighbour is not yet visible. Their shorter-coordinate reflection classes differ (for \(m=2\), their longer-coordinate classes differ), so step 4 separates them eventually. Therefore stabilization cannot occur before round \(m-1\). These two lower bounds match the upper bounds. This proves the asserted exact formulas and stable class counts.

## Verification

The accompanying standalone \(\texttt{grid_depth_check.py}\) implements colour refinement and, independently, exact integer walk-count moments on every rectangular grid with \(2\le m\le23\) and \(m\le n\le36\). It checks the claimed depth, the equality of the stable partition with the geometric reflection/axis-swap orbit partition, and separation of that partition already by walk moments of the predicted order. The check completed on **539 grids**, comprising **147224 tested vertices** in total. These finite tests support the proof but are not offered as a proof for unbounded dimensions.

## Relationship to prior work

Kersting, Mladenov, Garnett and Grohe (2014) study colour refinement using random-walk and power-iteration viewpoints and include a numerical grid experiment; their reported counts are algorithmic iteration counts, not a theorem for all rectangular dimensions. Krebs and Verbitsky (2014/2015) relate refinement depth to universal-cover truncations and obtain general lower bounds. Arvind, Köbler, Rattan and Verbitsky (2015) analyze the graph classes amenable to or refinable by colour refinement. Kiefer and McKay (2020) determine near-sharp worst-case iteration numbers on arbitrary graphs. None of those statements gives the present exact two-parameter formula, including the square/non-square phase change. The result uses a local walk-moment reconstruction to establish a matching family-specific upper bound, not merely the known general depth bounds.

## Limitations

Only finite simple undirected uncoloured Cartesian products of two paths, with both factors having at least two vertices, are covered. The formula depends on starting refinement at round zero with one uniform colour. Higher-dimensional boxes, directed grids, edge colours, and nonuniform starting vertex colours are outside the stated result. Computational checks are finite; the formal walk-deficit and orbit arguments establish the all-parameter theorem.

## References

1. K. Kersting, M. Mladenov, R. Garnett and M. Grohe, *Power Iterated Color Refinement*, AAAI 2014, DOI:10.1609/aaai.v28i1.8992 (first available 2014-06-21), https://ojs.aaai.org/index.php/AAAI/article/view/8992/8851.
2. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175 (first posted 2014-07-11), https://arxiv.org/abs/1407.3175.
3. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first posted 2015-02-04), https://arxiv.org/abs/1502.01255.
4. S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, ICALP 2020, DOI:10.4230/LIPIcs.ICALP.2020.73, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.73.
