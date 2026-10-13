# Perfect Roman domination of direct products of complete graphs

## Finding

For every pair of integers \(m,n\ge 3\), the direct (tensor or categorical) product of complete graphs satisfies
\[
\gamma_{\mathrm{pR}}(K_m\times K_n)=m+n.
\]
Every minimum perfect Roman dominating function is classified as follows. Except on \(K_3\times K_3\), choose any one vertex \(v\), assign it label \(2\), assign label \(1\) to every other vertex in its row or column, and assign label \(0\) everywhere else. All optimal functions are of this form, so their number is \(mn\). For \(K_3\times K_3\) these nine functions remain optimal, and there are six further optimal functions: put label \(2\) on the three positions of a permutation matrix and label \(0\) at the other six positions. Hence exactly \(15\) optimal functions occur in that exceptional case.

## Assumptions and scope

The graph \(G=K_m\times K_n\) has vertex set \([m]\times[n]\), where distinct vertices \((i,j)\) and \((i',j')\) are adjacent if and only if \(i\ne i'\) **and** \(j\ne j'\). This is the graph complement of the rectangular rook graph, not the Cartesian product \(K_m\square K_n\). The parameters \(m,n\) are integers at least three, with no ordering assumption.

A perfect Roman dominating function (PRDF) on a graph \(G\) assigns each vertex one of \(0,1,2\); every zero-labeled vertex has **exactly one** neighbor labeled \(2\). The function's weight is the sum of all vertex labels, and \(\gamma_{\mathrm{pR}}(G)\) is its minimum possible weight. Vertices labeled \(1\) or \(2\) are not subject to the unique-neighbor condition.

## Proof

Let \(A\subseteq V(G)\) be the set of vertices labeled \(2\), write \(t=|A|\), and put
\[
q(A)=\left|\left\{v\in V(G)\setminus A:\ |N_G(v)\cap A|=1\right\}\right|.
\]
For a fixed support \(A\), the least-weight possible PRDF with that support is uniquely obtained by putting label \(0\) at precisely the \(q(A)\) eligible outside vertices and label \(1\) at every other outside vertex. Indeed, an outside vertex with an inadmissible number of neighbors in \(A\) cannot be labeled zero, whereas labeling any eligible vertex one would increase the weight. Thus the canonical weight is
\[
w(A)=mn+t-q(A),
\]
and all noncanonical functions of the same support have strictly larger weight.

If \(t=0\), all vertices must receive label \(1\), yielding weight \(mn>m+n\) for \(m,n\ge3\). For \(t=1\), the unique support vertex has \((m-1)(n-1)\) neighbors, all of which have exactly one support neighbor. Therefore
\[
w(A)=mn+1-(m-1)(n-1)=m+n.
\]
These are exactly the \(mn\) single-support optimal functions described above.

Suppose \(t=2\). The two selected cells lie in the same row, the same column, or distinct rows and columns. In these cases, respectively,
\[
q(A)=2(m-1),\qquad q(A)=2(n-1),\qquad q(A)=2(m+n-4).
\]
The last expression excludes the two selected cells, which are adjacent to each other. Substituting in \(w(A)\) gives the respective excesses above \(m+n\):
\[
(m-1)(n-3)+1,\qquad (n-1)(m-3)+1,\qquad (m-3)(n-3)+1.
\]
Each is strictly positive because \(m,n\ge3\).

Now suppose \(t\ge3\). Fix a row \(i\), and let \(s_i\) be the number of selected cells outside that row. For a cell \((i,j)\), the number of its selected neighbors equals \(s_i-b_{ij}\), where \(b_{ij}\) counts selected cells outside row \(i\) in column \(j\). Let \(q_i\) be the number of *unselected* cells in row \(i\) having exactly one selected neighbor. If \(s_i=0\), then \(q_i=0\). If \(s_i=1\), the only possible eligible columns are the \(n-1\) columns different from the column containing that outside-row support, so \(q_i\le n-1\). If \(s_i=2\), an eligible column must contain precisely one of the two outside-row supports, hence \(q_i\le2\). Finally, if \(s_i\ge3\), an eligible column must contain exactly \(s_i-1\) outside-row supports. Two distinct such columns would jointly contain at least \(2(s_i-1)>s_i\) selected cells, an impossibility. Hence \(q_i\le1\) in this case.

At most one row can satisfy \(s_i=1\), because any such row contains \(t-1\) selected cells, and two disjoint rows would require \(2(t-1)\le t\), contrary to \(t\ge3\). Consequently,
\[
q(A)=\sum_i q_i\le (n-1)+2(m-1)=n+2m-3.
\]
Interchanging the row and column roles gives \(q(A)\le m+2n-3\). Therefore
\[
\begin{aligned}
w(A)-(m+n)&\ge(m-2)(n-3)+(t-3),\\
w(A)-(m+n)&\ge(n-2)(m-3)+(t-3).
\end{aligned}
\]
Both right-hand sides are nonnegative. For equality to hold in the desired minimum, they force \(t=3\) and \(m=n=3\); otherwise at least one is strictly positive.

It remains to classify equality on the \(3\times3\) board with \(t=3\). Equality demands \(q(A)=6\). If a row contains no selected cell, then \(s_i=3\) and that row contributes at most one to \(q(A)\), while each other row contributes at most two, so \(q(A)\le5\). Thus every row contains a selected cell; because there are three selected cells in total, each row contains exactly one. The symmetric argument gives exactly one selected cell in each column. Therefore \(A\) is a permutation-matrix support. Conversely, for any of the \(3!=6\) such supports, each of the six outside cells is adjacent to exactly one of the three selected cells, yielding \(q(A)=6\) and \(w(A)=9+3-6=6\). The canonical labeling puts zero on all six outside cells. These six functions and the nine single-support functions exhaust the optimum. \(\square\)

## Verification

Run `python3 verify.py` using the accompanying standalone standard-library script. It computes canonical weights directly from adjacency bitmasks and exhausts all \(2^{mn}\) choices of the two-label support for the seven boards \((m,n)=(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3)\), totaling \(1,188,352\) supports. Independently, it checks all \(3^{mn}\) full ternary labelings on the boards \((3,3)\) and \((3,4)\), totaling \(551,124\) assignments. It tests all support sets of size at most three and deterministic pseudorandom samples on four larger boards, and checks the predicted optimum and multiplicities. The output is captured in `verification_output.txt`. These finite computations test the implementation but do not prove the unbounded theorem, which follows from the inequalities above.

## Relationship to prior work

Cabrera Martínez, Peterin and Yero [1, Proposition 2.1] determine the **ordinary** Roman domination number of the same tensor products: it equals \(5\) when \(\min\{m,n\}=3\), and \(6\) when \(m,n\ge4\). Ordinary Roman domination requires at least one selected neighbor rather than exactly one. Their result does not imply the present optimal perfect Roman value or count. In particular, for \(m,n\ge4\), the gap between the perfect and ordinary Roman parameters is \(m+n-6\), which grows without bound. Almulhim, Akwu and Al Subaiei [2] study perfect Roman domination on **Cartesian products of paths and cycles**, which are not the graph family studied here. Work on regular-graph perfect Roman domination [3] provides general bounds but no matching exact classification identified for these tensor products.

## Limitations

The theorem assumes both factors have at least three vertices; products involving \(K_1\) or \(K_2\), and products with three or more complete-graph factors, are not addressed. The enumeration is of vertex-labeled functions, not automorphism orbits. The literature comparison is not an independent priority or novelty certification; equivalent historical work under alternate product terminology or in unindexed sources remains possible. The verification enumerations are finite only.

## References

[1] A. Cabrera Martínez, I. Peterin, I. G. Yero, *Roman domination in direct product graphs and rooted product graphs*, arXiv:2105.10006v1 (first public 20 May 2021), Proposition 2.1; subsequently AIMS Mathematics 6 (2021), 11084–11096, DOI:10.3934/math.2021643. https://arxiv.org/html/2105.10006v1

[2] A. Almulhim, A. D. Akwu, B. Al Subaiei, *The Perfect Roman Domination Number of the Cartesian Product of Some Graphs*, Journal of Mathematics 2022, Article 1957027, DOI:10.1155/2022/1957027. https://onlinelibrary.wiley.com/doi/10.1155/2022/1957027

[3] M. A. Henning, W. F. Klostermeyer, *Perfect Roman domination in regular graphs*, Applicable Analysis and Discrete Mathematics 12 (2018), 143–152, DOI:10.2298/AADM1801143H.
