# Exact wild number of the coordinate-coloured four-cube and a bound for the five-cube

## Finding

In the binary cube \(Q_d\), colour the edge \(\{u,u\oplus 2^i\}\) by \(i\). Let \(w_d\) be the smallest size of a set \(W\) of cube edges such that \(W\) together with each coordinate matching is connected and spans the cube. Then
\[
 w_4=10,\qquad 19\le w_5\le20.
\]
The constructive claims are explicit witnesses of size 10 and 20 respectively. The interval does not determine \(w_5\). The previously covered values \(w_2=2\) and \(w_3=5\) are included in the certificate file only as checks on the small cases.

## Assumptions and scope

Vertices are the integers from \(0\) to \(2^d-1\); \(\oplus\) means bitwise exclusive OR. Edges are unordered simple pairs, and the connectivity requirement is for the standard coordinate colouring only. No claim is made for different proper colourings of the same cube.

## Proof

If \(W\) has \(w_i\) edges of colour \(i\) and \(w\) edges in total, contract the colour-\(i\) perfect matching to get \(2^{d-1}\) vertices. The \(w_i\) edges of that colour in \(W\) are now loops. The remaining \(w-w_i\) edges must connect all quotient vertices, so \(w-w_i\ge 2^{d-1}-1\). Summing gives the specialization of the known general lower bound \(w\ge\lceil d(2^{d-1}-1)/(d-1)\rceil\), which is 10 for \(d=4\) and 19 for \(d=5\).

For \(d=4\), list the edges of \(W\) in the order
\[
(4,5),(8,9),(5,7),(9,11),(12,14),(1,5),(2,6),(9,13),(5,13),(6,14).
\]
After matching contraction, spanning trees are given by the following one-based edge indices:

| Colour contracted | Indices |
| --- | --- |
| 0 | 3,4,5,6,7,8,9 |
| 1 | 1,2,6,7,8,9,10 |
| 2 | 1,2,3,4,5,9,10 |
| 3 | 1,2,3,4,5,6,7 |

The listed seven edges per row span the eight quotient vertices: clear bit \(i\) in both ends to obtain the quotient pairs and traverse from vertex zero. Thus the lower bound for the four-cube is attained.

For \(d=5\), use the edges
\[
\begin{gathered}
(6,7),(12,13),(26,27),(0,2),(9,11),(12,14),(20,22),(29,31),\\
(0,4),(9,13),(17,21),(24,28),(6,14),(16,24),(19,27),(21,29),(22,30),\\
(1,17),(10,26),(12,28).
\end{gathered}
\]
Each pair is a distinct coordinate edge. After clearing bit \(i\) from each endpoint, a traversal starting at zero reaches all 16 quotient vertices for each \(i=0,1,2,3,4\). Equivalently, the full matching together with these edges reaches all 32 cube vertices for each \(i\). Hence the displayed set is a 20-edge witness.

## Reproducibility

The two lists are the entries `4` and `5` in `certificate.json`. `verify.py` uses integer labels and union-find to check the monochromatic quotient connectivity of all embedded lists. `verification_output.txt` records the certificate check. The lower bound is mathematical; neither the certificate nor its checker rules out a 19-edge five-cube solution.

## Relationship to prior work

Anders et al., arXiv:2508.06711v1, Proposition 5.4, establish the general lower bound; their Theorem 6.4(2) already gives \(w_2=2\) from the exact two-colour identity. Dawkins et al., arXiv:2610.22142v1, Theorem 4.4, also gives the square case; their Section 5 treats product lower bounds, not the upper witnesses here. The [complete-bipartite prism theorem](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-sharp-wild-number-of-properly-colored-complete-bipartite-prisms--1118d48ed828) gives \(w_3=5\): its \(K_{2,2}\square K_2\) instance includes the coordinate colouring. The contribution here is the four-cube ceiling attainment and the five-cube upper witness, not the smaller exact values or the general lower bound. The cited earlier material does not supply those two witnesses; differently indexed prior coverage is not ruled out.
