# Stable local edge metric bases of square-page book graphs
## Finding
For every integer \(r\ge5\), let \(B_r\) be the square-page book graph formed from \(r\) copies of \(C_4\) sharing the common edge \(xy\), with page \(i\) equal to
\[
x a_i b_i y x.
\]
Then
\[
\operatorname{edim}_{\ell}(B_r)=r-1.
\]

More strongly, every local edge metric basis is obtained as follows. Choose one page \(h\) to omit completely. From every other page choose exactly one of \(a_i,b_i\), subject to choosing at least two \(a\)-vertices and at least two \(b\)-vertices. Conversely, every such set is a local edge metric basis.

Therefore the exact number of local edge metric bases is
\[
r\bigl(2^{r-1}-2r\bigr).
\]

The threshold \(r=5\) is structural: a set of size \(r-1\) must have at least two selected vertices of each page orientation, which first becomes possible when four nonempty pages remain after one page is omitted.

## Assumptions and scope
All graphs are finite, simple, and connected. For a vertex \(s\) and an edge \(e=uv\), write
\[
d(s,e)=\min\{d(s,u),d(s,v)\}.
\]
A set \(S\subseteq V(G)\) is a local edge metric generator when every two adjacent edges have different distance representations with respect to \(S\). The minimum cardinality is denoted by \(\operatorname{edim}_{\ell}(G)\).

For \(B_r\), write
\[
P_i=\{a_i,b_i\}
\]
for the two non-spine vertices on page \(i\).

## Proof
All adjacent-edge pairs fall into three neighborhood types. Direct distance calculation gives, for distinct \(i,j\),
\[
R(xa_i,xa_j)=R(yb_i,yb_j)=P_i\cup P_j,
\]
where \(R(e,f)\) denotes the vertices that distinguish the adjacent edges \(e,f\). The pairs involving the common edge or the middle edge of one page give
\[
R(xy,xa_i)=R(a_i b_i,b_i y)=\{y,a_i\}\cup\{b_j:j\ne i\},
\]
and
\[
R(xy,yb_i)=R(xa_i,a_i b_i)=\{x,b_i\}\cup\{a_j:j\ne i\}.
\]
These formulas exhaust the adjacent-edge pairs.

Let \(S\) be a local edge metric generator. Since \(S\) must meet \(P_i\cup P_j\) for every distinct \(i,j\), at most one page can contain no selected non-spine vertex. Therefore \(S\) contains at least \(r-1\) non-spine vertices, so
\[
|S|\ge r-1.
\]

Suppose equality holds. Then \(S\) contains no spine vertex, exactly one page \(h\) is empty, and every other page contributes exactly one of its two non-spine vertices. Let \(A\) be the number of selected \(a_i\)'s and \(B\) the number of selected \(b_i\)'s, so
\[
A+B=r-1.
\]
The neighborhood
\[
R(xy,xa_h)=\{y,a_h\}\cup\{b_j:j\ne h\}
\]
forces \(B\ge1\). If \(B=1\), say only \(b_i\) is selected, then
\[
R(xy,xa_i)=\{y,a_i\}\cup\{b_j:j\ne i\}
\]
misses \(S\), a contradiction. Hence \(B\ge2\). By symmetry \(A\ge2\). Thus a size-\(r-1\) generator can exist only when
\[
r-1\ge4,
\]
which is exactly \(r\ge5\).

Conversely, assume \(r\ge5\). Omit one page \(h\), choose exactly one vertex from every other page, and suppose \(A\ge2\) and \(B\ge2\). Every set \(P_i\cup P_j\) is met because at most one page is empty. For a neighborhood of the form
\[
\{y,a_i\}\cup\{b_j:j\ne i\},
\]
either \(a_i\in S\), or there is a selected \(b_j\) with \(j\ne i\), because at least two \(b\)-vertices are selected. The symmetric argument handles every neighborhood of the other form. Hence \(S\) is a local edge metric generator of size \(r-1\), proving
\[
\operatorname{edim}_{\ell}(B_r)=r-1.
\]

For the count, choose the omitted page in \(r\) ways. On the remaining \(r-1\) pages there are \(2^{r-1}\) binary choices. Exclude the orientations having fewer than two choices of one type: zero or one \(a\)-choice, or zero or one \(b\)-choice. These four disjoint boundary classes have total size
\[
2+2(r-1)=2r.
\]
Therefore the number of bases is
\[
r\bigl(2^{r-1}-2r\bigr).
\]

## Verification
The included verifier constructs \(B_r\), computes all vertex-to-edge distances, enumerates every adjacent edge pair, and applies the local edge metric definition directly. For every \(5\le r\le8\), it checks every vertex set through size \(r-1\), rejects every smaller set, and compares every size-\(r-1\) generator with the structural classification above.

The finite computation is corroborative only. The theorem for arbitrary \(r\ge5\) follows from the neighborhood formulas and hitting-set argument.

## Relationship to prior work
The local edge metric dimension was introduced in 2020. Its foundational paper determines exact values for paths, ladders, cycles, stars, and wheels, then explicitly asks for characterizations on further special graph families and graph operations. The inspected full text does not treat book graphs or generalized theta graphs.

A 2024 structural continuation studies local edge metric dimension for corona products and edge-corona products and gives an integer-linear-programming formulation. Square-page books satisfy
\[
B_r\cong K_{1,r}\square K_2,
\]
so those corona-product results do not specialize to the present family.

The same square-page books have been studied for several other resolving and position-type invariants, but those statements do not determine local edge metric generators. In particular, a global edge-resolving or dominant edge-resolving set must satisfy constraints beyond adjacent-edge separation, so those parameters neither imply the size \(r-1\) nor the basis classification proved here.

## Limitations
The theorem is stated for the stable range \(r\ge5\). It does not classify the small books with two, three, or four pages, and it does not address books with longer cycle pages or arbitrary generalized theta graphs.

The 2024 same-parameter continuation was available through its abstract and indexed metadata rather than complete article text during comparison. Its stated scope is corona and edge-corona products, but inaccessible body material leaves a small residual literature risk.

## References
1. R. Adawiyah, Dafik, R. Alfarisi, R. M. Prihandini, I. H. Agustin, M. Venkatachalam, “The local edge metric dimension of graph,” Journal of Physics: Conference Series 1543 (2020), 012009, DOI 10.1088/1742-6596/1543/1/012009.
2. F. Amini, M. A. Henning, M. Tavakoli, “Local edge metric dimensions via corona products and integer linear programming,” Computational and Applied Mathematics 43(6) (2024), Article 358, DOI 10.1007/s40314-024-02879-0.
