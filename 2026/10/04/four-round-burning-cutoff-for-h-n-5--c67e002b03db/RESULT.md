# Four-round burning cutoff for \(H(n,5)\)
## Finding
Let \(H(n,5)\) be the generalized Heawood graph with vertices \(r_0,\ldots,r_{2n-1}\), the rim cycle \(r_0r_1\cdots r_{2n-1}r_0\), and diagonal edges \(r_{2i}r_{2i+5}\), with indices modulo \(2n\). For every integer \(n\ge7\),
\[
b(H(n,5))=4 \quad\text{if and only if}\quad 7\le n\le15,
\]
and consequently \(b(H(n,5))\ge5\) for every \(n\ge16\).

Explicit four-round burning sequences, written as vertex indices, are
\[
\begin{array}{c|c}
n & (x_1,x_2,x_3,x_4)\\ \hline
7&(0,1,2,3)\\
8&(0,1,2,8)\\
9&(0,1,7,10)\\
10&(0,1,9,12)\\
11&(0,1,13,10)\\
12&(0,6,14,16)\\
13&(0,8,16,18)\\
14&(0,12,14,20)\\
15&(0,14,16,22)
\end{array}
\]
where source \(x_i\) has remaining propagation radius \(4-i\).

## Assumptions and scope
Graph burning is used in the standard synchronous sense: one new source is ignited in each round and fire propagates one graph edge per subsequent round. A length-\(t\) source sequence \(x_1,\ldots,x_t\) burns the graph when the balls \(B_{t-i}(x_i)\) cover all vertices; the displayed positive witnesses also satisfy the source-validity inequalities \(d(x_i,x_j)\ge j-i\) for \(i<j\).

The result concerns the fixed-diagonal family \(H(n,5)\) only, and only the girth-six range \(n\ge7\). It determines the exact threshold for four-round burning. It does not determine the exact burning number once \(n\ge16\).

## Proof
Every \(H(n,5)\) is cubic. In any graph of maximum degree three,
\[
|B_r(v)|\le 1+3\sum_{j=0}^{r-1}2^j=3\cdot2^r-2
\]
for \(r\ge1\). Hence four burning sources can cover at most
\[
|B_3|+|B_2|+|B_1|+|B_0|\le22+10+4+1=37.
\]
Therefore \(H(n,5)\), which has \(2n\) vertices, cannot be four-burned when \(n\ge19\).

It remains to settle \(n=16,17,18\). Direct exhaustive ball-cover enumeration gives the minimum number of vertices left uncovered after choosing arbitrary centers for radii \(3,2,1\): respectively \(2,4,5\). These minima are attained, for example, at centers \( (0,14,22)\) in each of the three graphs. Thus even before imposing source-validity constraints, three initial balls always leave at least two vertices, and one final radius-zero source cannot finish. Hence \(b(H(n,5))\ge5\) for \(n=16,17,18\).

For \(7\le n\le15\), the table in the Finding supplies explicit valid four-round sequences, so \(b(H(n,5))\le4\). For \(n\ge8\), any three-round cover has size at most
\[
10+4+1=15<2n,
\]
so \(b(H(n,5))\ge4\). For \(n=7\), exhaustive enumeration of all radius-two and radius-one centers shows that at least two vertices remain uncovered; a final radius-zero source therefore cannot complete a three-round burning. Thus \(b(H(7,5))\ge4\) as well. Combining upper and lower bounds proves the claim.

## Verification
The accompanying `verify.py` constructs \(H(n,5)\) directly from the rim and diagonal definition, computes exact graph distances by breadth-first search, verifies every displayed four-source sequence including source-validity constraints, and exhausts all center pairs for \(n=7\) and all center triples for \(n=16,17,18\). It reproduces minimum uncovered counts \(2\) for \(n=7\) after radii \(2,1\), and \(2,4,5\) for \(n=16,17,18\) after radii \(3,2,1\). It separately checks the degree-three capacity calculations \(15\) and \(37\).

The finite enumeration is used only for the four boundary orders \(n=7,16,17,18\). The infinite tail \(n\ge19\) is proved analytically by the maximum-degree ball bound.

## Relationship to prior work
Sim and Wong define these generalized Heawood graphs and report exact burning numbers for all members of girth four and for the girth-six subfamily \(H(2k,k)\). Their publisher abstract does not state an exact result for the fixed-diagonal family \(H(n,5)\); within that announced girth-six subfamily, the present family overlaps only at \(H(10,5)\). Targeted searches for fixed-\(5\) generalized-Heawood burning results did not surface a theorem implying the cutoff above.

A separate structural paper records that \(H(n,k)\) has girth six exactly when \(n\ge k+2\) and \(k\ge5\), which gives the present range \(n\ge7\). That paper concerns skewness rather than burning.

## Limitations
The publisher article page and abstract were available, but its full PDF could not be retrieved during this review. The originality comparison therefore does not assert that every proposition in the full article was inspected. This leaves a residual access risk that an unindexed internal result may cover additional fixed-\(5\) cases. No such stronger result was found in targeted title, parameter, alias, and implication searches.

The theorem classifies four-round burnability only. It does not give \(b(H(n,5))\) exactly for \(n\ge16\), and it makes no claim for other odd diagonal parameters.

## References
1. Kai An Sim and Kok Bin Wong, “On the Burning Number of the Generalized Heawood Graphs,” *Jordan Journal of Mathematics and Statistics* 19(2) (2026), 303–321. DOI: 10.47013/19.2.12. Published 2026-07-12.
2. Kai An Sim, Kok Bin Wong, and collaborators, “On the skewness of the generalized Heawood graphs,” 2024. DOI: 10.1080/09728600.2024.2441817.
