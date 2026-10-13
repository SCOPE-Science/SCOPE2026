# Strong Roman domination of half graphs
## Finding
For every integer
\[
n\ge3,
\]
let \(H_n\) be the half graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and adjacency rule
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

Then
\[
\gamma_{StR}(H_n)
=
2\left(1+\left\lceil\frac{n-1}{2}\right\rceil\right)
=
\begin{cases}
n+1,&n\text{ odd},\\
n+2,&n\text{ even}.
\end{cases}
\]

If \(n\) is odd, the minimum strong Roman dominating function is unique:
\[
f(a_1)=f(b_n)=1+\left\lceil\frac{n-1}{2}\right\rceil,
\]
and
\[
f(v)=0
\]
for every other vertex.

If \(n=2q\) is even, the minimum is not unique. Besides the endpoint function above, the labeling
\[
f(a_2)=q,\qquad f(b_1)=1,\qquad f(b_n)=q+1,
\]
with every other vertex labeled \(0\), is also minimum.

## Assumptions and scope
A strong Roman dominating function on a graph \(G\) of maximum degree \(\Delta\) is a map
\[
f:V(G)\to\left\{0,1,\ldots,\left\lceil\frac{\Delta}{2}\right\rceil+1\right\}.
\]
Let
\[
B_0=\{v:f(v)=0\}.
\]
Every vertex \(v\in B_0\) must have a neighbor \(w\) such that
\[
f(w)\ge
1+\left\lceil\frac{|N(w)\cap B_0|}{2}\right\rceil.
\]
The minimum total weight is denoted by
\[
\gamma_{StR}(G).
\]

For \(H_n\), write
\[
\alpha=\left|\{a_i:f(a_i)>0\}\right|,
\qquad
\beta=\left|\{b_j:f(b_j)>0\}\right|.
\]
Thus \(n-\alpha\) vertices of \(A\) and \(n-\beta\) vertices of \(B\) are labeled \(0\).

## Proof
We first derive a lower bound that depends only on \(\alpha\) and \(\beta\).

Suppose \(B\) contains at least one zero vertex, and let \(b_j\) be the zero vertex of smallest index. Any defender of \(b_j\) must be a vertex \(a_i\) with
\[
i\le j.
\]
By minimality of \(j\), every zero vertex of \(B\) has index at least \(j\). Hence this same defender \(a_i\) is adjacent to every zero vertex of \(B\). Therefore
\[
|N(a_i)\cap B_0|=n-\beta,
\]
and its label is at least
\[
1+\left\lceil\frac{n-\beta}{2}\right\rceil.
\]
Since each of the other \(\alpha-1\) positive vertices of \(A\) contributes at least \(1\),
\[
\sum_{i=1}^{n}f(a_i)
\ge
\alpha+\left\lceil\frac{n-\beta}{2}\right\rceil.
\tag{1}
\]
If \(B\) has no zero vertex, then \(\beta=n\) and the same inequality remains true because the ceiling term is \(0\).

Symmetrically, if \(A\) has a zero vertex, choose the zero vertex \(a_i\) of largest index. Any defender \(b_j\) has \(j\ge i\), and therefore is adjacent to every zero vertex of \(A\). Hence
\[
\sum_{j=1}^{n}f(b_j)
\ge
\beta+\left\lceil\frac{n-\alpha}{2}\right\rceil.
\tag{2}
\]
Again this remains true when \(A\) has no zero vertex.

Adding (1) and (2),
\[
\omega(f)
\ge
g_n(\alpha)+g_n(\beta),
\qquad
g_n(t)=t+\left\lceil\frac{n-t}{2}\right\rceil.
\tag{3}
\]

If \(0<\alpha,\beta\), then for odd \(n=2q+1\),
\[
g_n(t)\ge q+1,
\]
with equality only at
\[
t=1.
\]
Thus
\[
\omega(f)\ge2q+2=n+1.
\tag{4}
\]
If one side has no positive vertex, then the opposite side must have all \(n\) vertices positive; otherwise a zero vertex on that opposite side would have no defender. Such a boundary case has weight strictly larger than \(n+1\) for \(n\ge3\). Hence (4) is the global lower bound.

For even \(n=2q\),
\[
g_n(t)\ge q+1
\]
for every positive integer \(t\), with equality precisely at
\[
t\in\{1,2\}.
\]
Therefore
\[
\omega(f)\ge2q+2=n+2
\tag{5}
\]
when both sides contain a positive vertex. If one side has no positive vertex, the opposite side must be entirely positive; this gives weight at least
\[
n+\frac n2,
\]
which is larger than \(n+2\) for \(n\ge6\), while for \(n=4\) it equals \(6=n+2\). Hence (5) is the global lower bound for every even \(n\ge4\).

Now define
\[
h=1+\left\lceil\frac{n-1}{2}\right\rceil
\]
and assign
\[
f(a_1)=f(b_n)=h,
\qquad
f(v)=0
\]
otherwise. The vertex \(a_1\) is adjacent to every vertex of \(B\), of which exactly \(n-1\) are zero, and \(b_n\) is adjacent to every vertex of \(A\), again with exactly \(n-1\) zero neighbors. Thus both labels are exactly large enough to defend all their zero neighbors, and every zero vertex has one of these two defenders. Hence
\[
\gamma_{StR}(H_n)\le2h.
\]
Together with the lower bounds,
\[
\gamma_{StR}(H_n)
=
2h
=
\begin{cases}
n+1,&n\text{ odd},\\
n+2,&n\text{ even}.
\end{cases}
\]

It remains to analyze uniqueness when \(n\) is odd. Equality in (3) forces
\[
\alpha=\beta=1.
\]
Let the unique positive vertices be \(a_r\) and \(b_s\).

Every zero vertex of \(B\) must be adjacent to \(a_r\). If \(r\ge2\), then every vertex
\[
b_1,\ldots,b_{r-1}
\]
is nonadjacent to \(a_r\), so all of them would have to be positive. Since there is only one positive vertex in \(B\), this gives
\[
r\le2,
\]
and the case \(r=2\) would force
\[
s=1.
\]
Symmetrically, every zero vertex of \(A\) must be adjacent to \(b_s\), so
\[
s\ge n-1,
\]
and the case \(s=n-1\) would force
\[
r=n.
\]
For \(n\ge3\), these exceptional possibilities are incompatible. Hence
\[
r=1,\qquad s=n.
\]
Equality in the side-weight bounds then forces
\[
f(a_1)=f(b_n)=1+\left\lceil\frac{n-1}{2}\right\rceil.
\]
So the odd-order minimum is unique.

Finally, let \(n=2q\). The distinct labeling
\[
f(a_2)=q,\qquad f(b_1)=1,\qquad f(b_n)=q+1
\]
has weight
\[
2q+2=n+2.
\]
Its zero vertices in \(B\) are \(b_2,\ldots,b_{n-1}\); they are all adjacent to \(a_2\), which has exactly \(n-2\) zero neighbors and therefore needs label
\[
1+\left\lceil\frac{n-2}{2}\right\rceil=q.
\]
Every zero vertex of \(A\) is adjacent to \(b_n\), which has \(n-1\) zero neighbors and therefore needs label \(q+1\). Hence this is a second minimum function, proving nonuniqueness for every even \(n\ge4\).

## Verification
The included checker constructs \(H_n\) from the defining nested-neighborhood rule and tests the strong Roman condition directly.

For
\[
3\le n\le7,
\]
it exhausts every labeling of total weight at most the claimed optimum. It verifies that no lighter labeling is feasible, that the endpoint labeling is minimum, that the odd cases have exactly one minimum function, and that each tested even case has the explicit distinct optimum from the proof.

## Relationship to prior work
Strong Roman domination was introduced in 2017 to model simultaneous attacks. The foundational paper proves NP-completeness even for bipartite graphs, gives general bounds, and develops the tree theory. Its full text contains no half-graph or chain-graph specialization.

A 2018 same-invariant paper, classified under Mathematics Subject Classification \(05C69\), studies further special families including fan-derived and web-like graphs. Its full text likewise contains no chain, half-graph, or Ferrers-graph theorem.

Targeted searches under “half graph,” “chain graph,” “Ferrers graph,” and “bipartite permutation graph,” together with exact strong-Roman terminology, did not locate a result implying the parity formula or the odd-order uniqueness statement. The closest published exact work concerns other graph families, and the later \(p\)-strong Roman generalization does not supply this half-graph specialization.

## Limitations
The theorem classifies all minimum functions only when \(n\) is odd. For even \(n\), it proves the exact minimum and explicit nonuniqueness but does not enumerate every minimum function.

The finite checker is corroborative only. The arbitrary-order value and odd-order uniqueness follow from the symbolic nested-neighborhood proof.

A differently phrased or non-indexed treatment of the same half-graph specialization may exist.

## References
1. M. P. Álvarez-Ruiz, T. Mediavilla-Gradolph, S. M. Sheikholeslami, J. C. Valenzuela-Tripodoro, I. G. Yero, “On the strong Roman domination number of graphs,” Discrete Applied Mathematics 231 (2017), 44–59, DOI 10.1016/j.dam.2016.12.013; available online 17 January 2017.
2. J. Xu, Z. Wang, “Note on Strong Roman Domination in Graphs,” Applied Mathematical Sciences 12(11) (2018), 535–541, DOI 10.12988/ams.2018.8351.
3. J. C. Valenzuela-Tripodoro, M. A. Mateos-Camacho, M. Cera López, R. Moreno Casablanca, M. P. Álvarez-Ruiz, “p-Strong Roman Domination in Graphs,” WSEAS Transactions on Mathematics 23 (2024), 1005–1017, DOI 10.37394/23206.2024.23.104.
