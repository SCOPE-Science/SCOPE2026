# Dissociation and maximal-dissociation enumerators of rectangular rook graphs

## Finding
For all integers \(2\le p\le q\), let \(R_{p,q}=K_p\mathbin{\square}K_q\), the rook graph on a \(p\)-by-\(q\) board. A *dissociation set* is a vertex set inducing maximum degree at most one; inclusion-maximal means no strictly larger dissociation set contains it.

For nonnegative integers \(a,b,c\), define \(u=p-a-2b-c\), \(v=q-2a-b-c\), and, only when \(u,v\ge0\),
\[
W_{p,q}(a,b,c)=\frac{p!q!}{u!\,v!\,a!\,b!\,c!\,2^{a+b}}.
\]
The complete cardinality polynomial of **all** dissociation sets and the polynomial of **inclusion-maximal** dissociation sets are, respectively,
\[
D_{p,q}(z)=\sum_{\substack{a,b,c\ge0\\u,v\ge0}}W_{p,q}(a,b,c)z^{2(a+b)+c},
\]
\[
M_{p,q}(z)=\sum_{\substack{a,b,c\ge0\\u,v\ge0\\(c=0\land(u=0\lor v=0))\ \lor\ (c>0\land u=v=0)}}W_{p,q}(a,b,c)z^{2(a+b)+c}.
\]
Equivalently the first polynomial has bivariate labeled generating function
\[
\sum_{p,q\ge0}\frac{D_{p,q}(z)}{p!q!}x^py^q
=\exp\left(x+y+xyz+\frac{xy^2+x^2y}{2}z^2\right).
\]
The maximum cardinality and the minimum cardinality of an inclusion-maximal dissociation set are
\[
\operatorname{diss}^{+}(R_{p,q})=\min\left\{2p,\left\lfloor\frac{2(p+q)}{3}\right\rfloor\right\},\quad
\operatorname{diss}^{-}(R_{p,q})=\begin{cases}p,&p\text{ even, or }p=q,\\p+1,&p\text{ odd and }p<q.\end{cases}
\]
Hence the only well-dissociated rook graphs with both dimensions at least two (all inclusion-maximal dissociation sets have maximum size) are \(R_{2,2}\) and \(R_{3,4}\), up to transposing dimensions.

For the wide regime \(q\ge2p\), the maximal-set polynomial simplifies to
\[
M_{p,q}(z)=p!q!\sum_{b=0}^{\lfloor p/2\rfloor}
\frac{z^{2p-2b}}{(p-2b)!\,b!\,2^{p-b}\,(q-2p+3b)!}.
\]
Thus its nonzero degrees are exactly \(2\lceil p/2\rceil,2\lceil p/2\rceil+2,\ldots,2p\); in particular its largest-set coefficient is \(q!/(2^p(q-2p)!)\).

## Assumptions and scope
Graphs are finite, simple, and undirected. The Cartesian product \(K_p\mathbin{\square}K_q\) has vertices the cells \((i,j)\), adjacent exactly when they share one coordinate. Coefficients count labeled subsets of these cells, including the empty dissociation set in \(D_{p,q}\). The statement on maximal sets uses inclusion-maximal, not just maximum cardinality. All formulas and the classification hold for every integer \(2\le p\le q\). The bivariate generating function is a formal power series also encoding zero-size factor parameters; the graph assertions only concern \(p,q\ge2\).

## Proof
**Component correspondence.** Regard a selected cell \((i,j)\) as the edge joining left vertex \(i\) and right vertex \(j\) of \(K_{p,q}\). In the line graph, a selected edge \(ij\) has \(d_F(i)+d_F(j)-2\) selected neighbors, where \(F\) is the selected edge set. Requiring this number to be at most one for every selected edge implies that every nontrivial component of \(F\) has exactly one or two edges: a longer path or a vertex of degree at least three would give a selected edge at least two neighbors. Conversely, disjoint isolated edges and two-edge paths clearly satisfy the condition. Thus components are isolated edges and copies of \(P_3\).

Let \(a\) count two-edge paths centered at a left vertex (one left and two right original vertices), \(b\) those centered at a right vertex (two left and one right), and \(c\) isolated edges. The component decomposition occupies \(a+2b+c\) left vertices and \(2a+b+c\) right vertices; the remaining numbers are \(u,v\). An unused left or right vertex contributes formal weight \(x,y\); an isolated edge contributes \(xyz\); a left-centered two-edge path contributes \(xy^2z^2/2\); and a right-centered one contributes \(x^2yz^2/2\). The exponential formula for labeled disjoint components proves the displayed generating function. Expanding the exponential gives the integer multiplicity \(W_{p,q}(a,b,c)\), and hence the polynomial \(D_{p,q}\).

**Inclusion maximality.** If \(c>0\), take one isolated selected edge. Any unused original vertex in either bipartition class can be joined to the opposite endpoint of this edge, enlarging its component to a two-edge path without violating the degree condition. Thus a maximal set with \(c>0\) must have \(u=v=0\). Conversely, when \(u=v=0\), every original vertex is already incident to the selected components and adding an edge would give some selected edge at least two selected neighbors. If \(c=0\), every selected component is already a two-edge path and is saturated: any extension must join two unused original vertices. Since the underlying bipartite graph is complete, such an edge exists exactly when \(u>0\) and \(v>0\). This proves the maximality criterion and \(M_{p,q}\).

**Maximum size.** If \(s=2(a+b)+c\), then \(s\le2p\) because each left original vertex meets at most two selected edges. Also the two equations for occupied vertices give \(3s=2(p+q-u-v)-c\le2(p+q)\), so \(s\le\lfloor2(p+q)/3\rfloor\). These bounds are attainable. If \(q\ge2p\), take \((a,b,c,u,v)=(p,0,0,0,q-2p)\). If \(p\le q<2p\), write \(N=p+q\). For \(N\equiv0\pmod3\), take \(a=(2q-p)/3\), \(b=(2p-q)/3\), \(c=u=v=0\). For \(N\equiv1\pmod3\), take \(a=(2q-p+1)/3\), \(b=(2p-q-2)/3\), \(c=v=0,u=1\). For \(N\equiv2\pmod3\), take \(a=(2q-p-1)/3\), \(b=(2p-q-1)/3\), \(c=1,u=v=0\). In each case these are nonnegative integers, have the stated occupied-vertex counts, and attain \(\lfloor2N/3\rfloor\). The \(N\equiv1\) case at \(q=p\) has \(p\equiv2\pmod3\) and \(b=(p-2)/3\ge0\); all other endpoints are likewise valid.

**Smallest maximal size.** In the \(c=0,u=0\) maximality branch, \(p=a+2b\) and \(s=2(a+b)=p+a\), giving \(s\ge p\), and \(s\ge p+1\) when \(p\) is odd. In the \(c=0,v=0\) branch, \(q=2a+b\) and \(s=q+b\ge q\). In the \(c>0,u=v=0\) branch, subtracting occupied-vertex equations gives \(a-b=q-p\) and \(s=q+b\ge q\). Consequently every maximal set has at least \(p\) vertices; if \(p\) is odd and \(q>p\), each branch instead has at least \(p+1\). If \(p\) is even, take \(a=c=u=0,b=p/2,v=q-p/2\), giving a maximal set of size \(p\). If \(p=q\) is odd, take \(a=b=u=v=0,c=p\), giving size \(p\). If \(p\) is odd and \(q>p\), take \(a=1,b=(p-1)/2,c=u=0,v=q-(p+3)/2\), giving size \(p+1\); the last unused-vertex count is nonnegative for \(p\ge3\) and \(q\ge p+1\). This proves the lower formula.

**Rigidity and wide boards.** Direct comparison of the two exact extrema gives equality only for \((p,q)=(2,2)\) and \((3,4)\): for even \(p\ge4\), the maximum exceeds \(p\) already when \(q=p\); for odd \(p\ge5\) it exceeds \(p\) at \(q=p\) and exceeds \(p+1\) already at \(q=p+1\), while it is nondecreasing for larger \(q\); for \(p=2,3\) the remaining cases follow immediately. If \(q\ge2p\), a maximal configuration with \(c>0\) would have \(a-b=q-p\) and \(c=2p-q-3b\le0\), contradiction. A \(c=0,v=0\) maximal configuration requires \(q=2a+b\le2p\), thus only occurs at \(q=2p\) with \(a=p,b=0\), already having \(u=0\). Therefore all maximal configurations satisfy \(c=u=0\), whence \(a=p-2b\), \(v=q-2p+3b\), and \(s=2p-2b\). Substituting into \(W_{p,q}\) proves the displayed wide-board polynomial, full degree spectrum, and top coefficient.

## Verification
Run the standalone dependency-free script `verify_rook_dissociation.py` with Python 3; its standard output is also supplied as `verify_output.txt`. It checks the original graph-adjacency condition and inclusion-maximality independently of the component enumeration on 11 boards, comprising 1,419,088 vertex subsets. The script checks the exact formulas and extremal values across another 735 parameter pairs. For example \(D_{2,4}(z)=1+8z+28z^2+24z^3+6z^4\), while \(M_{2,4}(z)=4z^2+6z^4\); also \(M_{3,4}(z)=90z^4\) and \(M_{4,5}(z)=60z^4+240z^5+180z^6\). All checks passed; the infinite assertions follow from the proof, not finite computation.

## Relationship to prior work
Counting dissociation sets in *Cartesian grid graphs* \(P_p\mathbin{\square}P_q\) was studied by Zhou, Chen, Deng and Tu (2024). Their grid adjacency uses paths, whereas the present rook graphs use complete-graph factors; their transfer-matrix formulas do not supply the present enumerators. Tu, Xiao and Lang (2023) studied counts in cubic graphs, another distinct class. Orlovich et al. (2011) established the relationship between dissociation in line graphs and two-edge path/edge packings, and their maximum-size theorem already handles some line-graph cases; no novelty is asserted for this reduction or for a previously implied scalar maximum. Tian and Tu (2024) study maximal dissociation sets in grid, cylindrical, and toroidal grid classes; available metadata concern path/cycle products rather than rook graphs, but the full text was not accessible for a decisive comparison. The distinct contribution here is the simultaneous all-set and maximal-set formulas for the complete-factor rook family, together with the complete minimum/maximum maximal-set sizes and the two-exception well-dissociated classification.

## Limitations
Only rectangular rook graphs with both factor orders at least two are covered. Closed sums may have polynomially many terms but very large coefficients. Prior structural facts concerning line-graph dissociation are not new. An equivalent unindexed counting theorem, particularly under two-edge matching or maximum-degree-one set terminology, remains a bibliographic priority risk. Some relevant full text could not be inspected. The review is not independent mathematical validation.

## References
1. Zhou, Chen, Deng and Tu, “Enumeration of dissociation sets in grid graphs,” *AIMS Mathematics* (2024), DOI: 10.3934/math.2024721 (public 2024-04-24; primary MSC 05C30).
2. Tu, Xiao and Lang, “Counting the number of dissociation sets in cubic graphs,” *AIMS Mathematics* (2023), DOI: 10.3934/math.2023507.
3. Orlovich, Dolgui, Finke, Gordon and Werner, “The complexity of dissociation set problems in graphs,” *Discrete Applied Mathematics* (2011), DOI: 10.1016/j.dam.2011.04.023.
4. Tian and Tu, “Enumerating maximal dissociation sets in three classes of grid graphs,” *Applied Mathematics and Computation* (2024), DOI: 10.1016/j.amc.2024.128711 (available abstract only in this assessment).
