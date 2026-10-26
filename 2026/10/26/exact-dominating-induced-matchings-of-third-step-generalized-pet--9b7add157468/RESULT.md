# Exact dominating induced matchings of third-step generalized Petersen graphs

## Finding

For each integer \(n\ge7\), define the simple cubic generalized Petersen graph \(G_n=\operatorname{GP}(n,3)\) with outer vertices \(u_i\), inner vertices \(v_i\), and edges \(u_i u_{i+1}\), \(u_i v_i\), \(v_i v_{i+3}\), with subscripts modulo \(n\). An edge family \(M\) is a *dominating induced matching* (DIM) if every edge of \(G_n\) has precisely one member of \(M\) sharing at least one endpoint with it, counting the edge itself as sharing endpoints with itself.

**Theorem.** The number of DIMs of \(G_n\) is exactly
\[
\#\operatorname{DIM}(G_n)=\begin{cases}5,&5\mid n,\\0,&5\nmid n.\end{cases}
\]
When \(n=5m\), these five matchings are the cyclic shifts by \(r\in\{0,1,2,3,4\}\) of
\[
M_0=\{u_{5t}u_{5t+1},\;u_{5t+3}v_{5t+3},\;v_{5t+4}v_{5t+7}:0\le t<m\}.
\]
Each contains exactly \(3n/5\) edges, and no others exist.

## Assumptions and scope

All graphs are simple, undirected and vertex-labelled by the displayed coordinates. The condition \(n\ge7\) ensures \(3<n/2\), so the standard generalized Petersen edges are distinct and the graph is cubic. Matchings are counted as labelled edge subsets; no quotient by automorphisms is taken. An edge dominates itself and every edge incident to an endpoint. The assertion is an infinite-family theorem; finite computations are supplementary checks only.

## Proof

**1. The matching/colouring equivalence.** Colour a vertex black when it is incident with a selected edge and white otherwise. A DIM is equivalent to a two-colouring in which the white vertices form an independent set and the black vertices induce a \(1\)-regular graph. Indeed, when a selected edge dominates every edge exactly once, its endpoints are black, selected edges are disjoint, no additional black–black edges are possible, and no white–white edge can exist. Conversely, given such a colouring, all black–black edges are disjoint and each edge has exactly one incident black–black edge (including itself when black–black).

Set \(x_i=1\) if \(u_i\) is black, and \(y_i=1\) if \(v_i\) is black, with both indicators zero for white. Every cubic vertex has exactly \(3-2b\) black neighbours when its own indicator is \(b\): a white vertex sees three black neighbours, and a black vertex sees exactly one black neighbour. Therefore the colouring condition is equivalent to
\[
2x_i+x_{i-1}+x_{i+1}+y_i=3,\qquad
x_i+2y_i+y_{i-3}+y_{i+3}=3                         \tag{1}
\]
for every \(i\pmod n\), with \(x_i,y_i\in\{0,1\}\). Summing the two equation families gives \(4X+Y=3n\) and \(X+4Y=3n\), where \(X=\sum x_i\) and \(Y=\sum y_i\). Hence
\[
X=Y=3n/5.                                                     \tag{2}
\]
This immediately forces \(5\mid n\) for a binary solution. Independently, every chosen edge in the cubic graph dominates exactly five edges, and the \(3n\) edges are partitioned into such five-edge closed neighbourhoods.

**2. Spectral rigidity of the finite difference system.** Regard (1) over \(\mathbb C\), temporarily dropping the binary restriction. For an \(n\)th root of unity \(z\), Fourier coefficients of a nonconstant frequency satisfy
\[
\begin{pmatrix}2+z+z^{-1}&1\\1&2+z^3+z^{-3}\end{pmatrix}
\binom{\widehat x(z)}{\widehat y(z)}=\binom00.
\]
The determinant, multiplied by \(z^4\), is exactly
\[
P(z)=(z+1)^2(z^3+1)^2-z^4=\Phi_5(z)R(z),
\]
where
\[
\Phi_5(z)=z^4+z^3+z^2+z+1,\qquad
R(z)=z^4+z^3-z^2+z+1.                                         \tag{3}
\]
The quartic \(R\) is irreducible over \(\mathbb Q\): modulo two it becomes \(\Phi_5\), irreducible over \(\mathbb F_2\) because \(2\) has multiplicative order four modulo five (or by checking it has neither linear nor irreducible quadratic factor). If a zero of \(R\) were a root of unity, its minimal polynomial would be a degree-four cyclotomic polynomial, necessarily one of \(\Phi_5,\Phi_8,\Phi_{10},\Phi_{12}\). Their coefficients are visibly distinct from \(R\). Thus **no root of \(R\) is a root of unity**.

The only nonconstant Fourier frequencies permitted by (1) are consequently primitive fifth roots. The constant frequency is fixed uniquely by \(4a+b=3\), \(a+4b=3\), giving \(a=b=3/5\). Thus whenever a solution exists, every \(x_i\) and \(y_i\) is **five-periodic**: \(x_{i+5}=x_i\) and \(y_{i+5}=y_i\) for all \(i\). This conclusion holds for *all* binary solutions, not merely for those tested computationally.

**3. Exhaustion of five-periodic binary solutions.** Once \(5\mid n\), (2) and five-periodicity imply that each five-term outer word has exactly three ones and two zeros. If \(x_i=0\), the first equation in (1) forces \(x_{i-1}=x_{i+1}=y_i=1\); in particular the two outer zeros may not be consecutive. A cyclic binary word of length five with exactly two nonconsecutive zeros has precisely five possibilities, the rotations of \(11010\). Inserting the displayed representative into (1) forces \(y=00111\) and directly satisfies all five inner equations, since the inner offsets \(\pm3\) are \(\mp2\pmod5\). By rotation, all five outer words give valid inner words; no others are possible.

For the representative words \((x,y)=(11010,00111)\), the black–black edges are exactly the three families in \(M_0\), and the remaining four representatives are its column rotations. The five edge subsets differ, and the matching/colouring equivalence proves they are precisely all DIMs. This proves the theorem.

## Verification

`verify_polynomial.py` uses integer polynomial arithmetic to check identity (3), binary reduction of \(R\), and all \(32\) possible five-bit outer words, obtaining exactly the five listed solutions. `verify_edge_cover.py` independently constructs all \(3n\) graph edges and enumerates exact covers by their five-edge closed neighbourhoods for every \(7\le n\le50\), obtaining exactly the theorem's count. `verify_coloring.py` independently enumerates every cyclic outer word satisfying necessary local constraints, recovers the inner word and tests all equations (1) for every \(7\le n\le32\), also obtaining the theorem's count. Corresponding `.out` files record the execution results. Finite enumeration is not the justification for the all-\(n\) statement; the Fourier/irreducibility argument and five-word exhaustion above are.

## Relationship to prior work

Domination by an induced matching, also called efficient edge domination, is a standard graph-invariant and algorithmic problem; Cardoso–Cerdeira–Delorme–Silva (2008) give general regular-graph results and spectral obstructions. Korpelainen–Lozin–Purcell (2014) study algorithmic recognition under forbidden-subgraph conditions. Mahmoodi–Behmaram–Došlić–Asadi (2024), Observation 7, exhibit a DIM for \(\operatorname{GP}(n,2)\) when \(5\mid n\) and deduce its size \(3n/5\). The present theorem instead treats the *third-step* family \(\operatorname{GP}(n,3)\), and determines both necessity and the **exact count and shape of all** such matchings. The step-two family result is not claimed as new. In particular, \(\operatorname{GP}(10,3)\) is bipartite, whereas \(\operatorname{GP}(10,2)\) contains an inner five-cycle, so the two graph families cannot be identified uniformly by a relabelling of that earlier result.

## Limitations

The classification is restricted to inner step three, with \(n\ge7\), and makes no claim about all steps in generalized Petersen graphs. The five matchings are counted without automorphism reduction. Although relevant accessible papers and indexed records were compared, mathematically equivalent results in unindexed material may exist; priority has not been independently certified. The proof and computations were reviewed together, but no independent external scientific audit has been performed.

## References

- D. M. Cardoso, J. O. Cerdeira, C. Delorme and P. C. Silva, “Efficient edge domination in regular graphs,” *Discrete Applied Mathematics* 156 (2008), 3060–3065. DOI: 10.1016/j.dam.2008.01.021. First publicly available online 2008-03-07 as recorded in the article front matter.
- N. Korpelainen, V. V. Lozin and C. Purcell, “Dominating induced matchings in graphs without a skew star,” *Journal of Discrete Algorithms* 26 (2014), 45–55. DOI: 10.1016/j.jda.2013.11.002.
- A. Mahmoodi, A. Behmaram, T. Došlić and N. Asadi, “Dominating induced matchings and other graph parameters,” *AKCE International Journal of Graphs and Combinatorics* 21 (2024), 261–267. DOI: 10.1080/09728600.2024.2342310, particularly Observation 7.
