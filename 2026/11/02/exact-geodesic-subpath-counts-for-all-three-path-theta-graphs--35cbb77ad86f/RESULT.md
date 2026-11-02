# Exact geodesic-subpath counts for all three-path theta graphs

## Finding

Let \(\Theta(a,b,c)\) be the simple graph formed from three internally vertex-disjoint paths of respective edge lengths \(2\le a\le b\le c\), with their first and last vertices identified as common poles. Its order is \(N=a+b+c-1\). Let \(\operatorname{gpn}(G)\) count every distinct shortest path between unordered distinct vertices and also one length-zero path at each vertex.

The following formulas use only integer arithmetic and parity, giving the **exact** value for every triple of path lengths, without iterating over any vertices. Set \(\varepsilon(u,v)=1\) when \(u\equiv v\pmod2\) and zero otherwise. Define

\[
R(t,s)=\begin{cases}(t-s)/2+1,&t>s\text{ and }\varepsilon(t,s)=1,\\0,&\text{otherwise},\end{cases}
\]

\[
Q(c,a)=\begin{cases}\frac{k(k+1)}2-1,&c>a,\quad k=\left\lceil\frac{c-a}{2}\right\rceil,\\0,&c=a,\end{cases}
\]

\[
L=\max\left\{0,\left\lfloor\frac{b-a-1}{2}\right\rfloor\right\},\qquad
M=\begin{cases}b-1,&a=b,\\a+\varepsilon(a,b),&a<b,\end{cases}
\]

and the cross-arm contribution

\[
H=\varepsilon(b,c)M
 +2\mathbf 1_{\{c\ge a+2,\;\varepsilon(c,a)=1\}}L
 +2\mathbf 1_{\{b\ge a+2,\;\varepsilon(b,a)=1\}}
  \left\lfloor\frac{c-a}{2}\right\rfloor.
\]

**Theorem.** For all integers \(2\le a\le b\le c\),

\[
\boxed{\begin{aligned}
\operatorname{gpn}(\Theta(a,b,c))={}&\binom{N+1}{2}
 +\mathbf1_{\{a=b\}}\bigl(1+\mathbf1_{\{b=c\}}\bigr)\\
&+R(b,a)+\bigl(1+\mathbf1_{\{a=b\}}\bigr)R(c,a)
 +\mathbf1_{\{a=b\}}Q(c,a)\\
&+(a-1)\bigl(\varepsilon(a,b)+\varepsilon(a,c)\bigr)+H.
\end{aligned}}
\]

The expression is symmetric in the original unsorted path lengths after sorting. As a compact specialization, for every integer \(t\ge2\),

\[
\operatorname{gpn}(\Theta(t,t,t))=\binom{3t}{2}+3t-1.
\]

For instance, \(\operatorname{gpn}(\Theta(2,8,8))=176\), \(\operatorname{gpn}(\Theta(3,3,9))=125\), and \(\operatorname{gpn}(\Theta(2,2,2))=20\).

## Assumptions and scope

All graphs are finite, simple, undirected, and unweighted; each of the three paths has at least two edges, with only its poles shared. Different vertex sequences are distinct geodesics, even with the same endpoints. Each zero-length path is counted exactly once. A \(\Theta(a,b,c)\) graph is a two-connected noncactus graph: its three basic cycles share edges, so cactus-only formulas do not apply directly. Sorting the lengths is solely notation, not an extra mathematical restriction.

## Proof

**1. Baseline and poles.** Every unordered pair of different vertices has at least one geodesic; together with the \(N\) length-zero paths this supplies \(\binom{N+1}{2}\). It remains to count, for each distinct vertex pair, its number of shortest paths minus one. Between the two poles, the shortest paths are precisely the arms of minimum length. Therefore the pole pair contributes \(\mathbf1_{\{a=b\}}(1+\mathbf1_{\{b=c\}})\).

**2. Pairs lying on one arm.** Consider two vertices on an arm of length \(t\), at separation \(\delta\), excluding the pole pair. There are \(t+1-\delta\) such unordered vertex pairs. Every simple path between them is either the direct arm segment of length \(\delta\), or the complementary portions of that arm joined through one of the other two pole-to-pole arms. If \(s\) is the shorter alternative-arm length and \(m\in\{1,2\}\) is its multiplicity, the competing shortest detours have length \(t-\delta+s\). When \(2\delta=t+s\), there are \(m\) geodesics beyond the direct one; when \(2\delta>t+s\), the \(m\) detours are shortest, contributing \(m-1\) beyond the baseline; otherwise the direct route is unique.

On the shortest arm of length \(a\), no pair other than the excluded pole pair contributes. The arm of length \(b\) contributes \(R(b,a)\). When \(a<b\), the arm of length \(c\) contributes \(R(c,a)\). If \(a=b\), the two other arms provide two equal shortest detours on arm \(c\); ties with the direct segment contribute \(2R(c,a)\). Strictly shorter detours occur at \(\delta> (c+a)/2\) with \(\delta\le c-1\), contributing one excess geodesic for each pair. With \(k=\lceil(c-a)/2\rceil\), their number is \(2+3+\cdots+k=k(k+1)/2-1=Q(c,a)\) when \(c>a\), and zero otherwise. Thus all same-arm excess is

\[
R(b,a)+\bigl(1+\mathbf1_{\{a=b\}}\bigr)R(c,a)
+\mathbf1_{\{a=b\}}Q(c,a).
\]

**3. Cross pairs involving a shortest arm.** For one internal vertex on the \(a\)-arm and one on either the \(b\)- or \(c\)-arm, passage through either pole is the only potentially shortest route: detouring through the remaining arm cannot improve the route from the \(a\)-arm vertex to either pole, since the remaining arm is no shorter than \(a\). A tie occurs if the two chosen vertex positions \(x,y\), measured from the first pole, satisfy \(x+y=(a+t)/2\), where \(t\) is the other arm length. Such a solution exists exactly when \(a+t\) is even; then each of the \(a-1\) internal positions \(x\) yields one valid internal position \(y\). This supplies \((a-1)(\varepsilon(a,b)+\varepsilon(a,c))\).

**4. Cross pairs between the two longer arms.** Let \(x\in\{1,\ldots,b-1\}\) and \(y\in\{1,\ldots,c-1\}\) be positions on the \(b\)- and \(c\)-arms measured from the first pole. Precisely four possible simple paths connect them, with lengths

\[
x+y,\quad b-x+c-y,\quad x+a+c-y,\quad b-x+a+y.
\]

Group the two paths increasing in \(y\) and the two decreasing in \(y\). The group minima are \(y+p_x\) and \(c-y+q_x\), where

\[
p_x=\min\{x,b-x+a\},\qquad q_x=\min\{b-x,x+a\}.
\]

Each group minimum is attained by one path except at \(2x=b+a\), respectively \(2x=b-a\), where it is attained by two. First ignore these within-group double occurrences. The two group minima tie at \(2y=c+q_x-p_x\). For \(b-a\le2x\le b+a\), the difference is \(q_x-p_x=b-2x\); hence ties require \(b+c\) even, and there are exactly \(M\) eligible positions \(x\) because \(c\ge b\). For \(2x<b-a\) and \(2x>b+a\), the difference equals \(a\) and \(-a\), respectively. Each exterior interval has exactly \(L\) eligible positions. These provide ties precisely when \(c\equiv a\pmod2\) and \(c\ge a+2\). Thus the number of between-group ties is

\[
\varepsilon(b,c)M+2\mathbf1_{\{c\ge a+2,\varepsilon(c,a)=1\}}L.
\]

If \(b\ge a+2\) and \(b\equiv a\pmod2\), there are in addition two interior boundary positions \(x=(b-a)/2\) and \(x=(b+a)/2\). At each, one group has two routes of equal minimum length. It is globally shortest for exactly \(\lfloor(c-a)/2\rfloor\) eligible positions \(y\), counting ties with the other group. The additional number of geodesics at these boundaries is therefore \(2\lfloor(c-a)/2\rfloor\). These routes are counted once beyond any between-group tie, even if three distinct routes are simultaneously shortest. This proves that the entire cross-pair excess between the \(b\)- and \(c\)-arms is exactly \(H\).

**5. Sum.** The pole pair, the single-arm pairs excluding the poles, and the three types of cross-arm internal pairs partition all unordered pairs. Adding their nonoverlapping excess contributions to the baseline proves the theorem. In the equal-arm specialization, only the pole term, the two shortest-arm cross terms, and the between-longer-arm tie term survive; their sum is \(3t-1\), establishing the corollary.

## Verification

The included `verify.py` creates the graph afresh, runs breadth-first search from every labelled vertex, and propagates integer shortest-path counts along each shortest-path directed acyclic graph. This independent algorithm does not use the counting proof or its arm-classification formulas. It compares the result with the closed expression for all \(364\) unordered triples of lengths \(2\) through \(13\), and for \(200\) reproducible random triples with each length between \(2\) and \(70\). It separately checks the equal-arm specialization for \(2\le t\le99\) and six explicit values. The run ends with `VERIFY_OK`.

## Relationship to prior work

Knor, Sedlar, Škrekovski and Zhang introduced the geodesic subpath number and established exact results for grids, hypercubes, sequential joins of independent sets, and extremal cactus graphs. Their April 2026 complete preprint and August 2026 open-access journal article do not provide this arbitrary-length three-path theta formula. Here the shared edges of the three theta cycles create shortest-path competition not handled by their cactus decomposition. Earlier related analyses of geodesic transversals count hitting sets for maximal shortest paths, not the total number of shortest paths. A published result for bicliques with deleted matchings concerns a distinct diameter-two graph family, and a published extremal result for diameter-two graphs supplies no theta formula for arbitrary lengths. The theorem is presented as a new exact result subject to the historical-priority limitations below.

## Limitations

The theorem applies to theta graphs with exactly three paths; it does not classify extremizers among all graphs of fixed order, all series-parallel graphs, or theta graphs with four or more arms. It counts all shortest paths rather than the number of **maximal** geodesics. Computational tests corroborate, but do not replace, the proof. No independent mathematical audit has been performed, and unindexed prior equivalent results cannot be excluded merely by searching.

## References

1. M. Knor, J. Sedlar, R. Škrekovski, X.-D. Zhang, *Counting geodesic paths in graphs*, arXiv:2604.04907v1, first posted 2026-04-06; *Mediterranean Journal of Mathematics* 23 (2026), article 171, DOI: 10.1007/s00009-026-03159-3. Full public preprint: https://arxiv.org/abs/2604.04907.
2. P. Manuel, B. Brešar, S. Klavžar, *The geodesic-transversal problem*, arXiv:2101.08042, 2021. https://arxiv.org/abs/2101.08042.
