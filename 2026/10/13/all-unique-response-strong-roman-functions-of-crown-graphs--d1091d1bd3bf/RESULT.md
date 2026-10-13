# All unique-response strong Roman functions of crown graphs
## Finding
Let
\[
\operatorname{Cr}_n=K_{n,n}-M,\qquad n\ge3,
\]
have bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where \(M=\{a_i b_i:1\le i\le n\}\) is the deleted perfect matching. Put
\[
h=1+\left\lceil\frac{n-1}{2}\right\rceil .
\]

Every unique-response strong Roman dominating function on \(\operatorname{Cr}_n\) belongs to exactly one of the following three families.

The first family consists only of the all-one function, of weight
\[
2n.
\]

For the second family, choose one vertex \(d\). Assign
\[
f(d)=h,
\]
assign \(0\) to every neighbor of \(d\), and assign \(1\) to every remaining vertex. There are \(2n\) such functions, each of weight
\[
n+h.
\]

For the third family, choose one deleted matched pair \(\{a_i,b_i\}\). Assign
\[
f(a_i)=f(b_i)=h
\]
and assign \(0\) to every other vertex. There are \(n\) such functions, each of weight
\[
2h.
\]

Consequently the complete weight enumerator is
\[
U_{\operatorname{Cr}_n}(z)
=
z^{2n}+2n z^{n+h}+n z^{2h}.
\]

In particular, there are exactly
\[
3n+1
\]
unique-response strong Roman dominating functions,
\[
u_{StR}(\operatorname{Cr}_n)
=
2h
=
\begin{cases}
n+1,&n\text{ odd},\\
n+2,&n\text{ even},
\end{cases}
\]
and exactly \(n\) minimum functions.

## Assumptions and scope
A strong Roman dominating function on a graph of maximum degree \(\Delta\) is a function
\[
f:V(G)\to\left\{0,1,\ldots,\left\lceil\frac{\Delta}{2}\right\rceil+1\right\}
\]
such that every vertex labeled \(0\) has a neighbor \(w\) with label at least
\[
1+\left\lceil\frac{|N(w)\cap V_0|}{2}\right\rceil,
\]
where \(V_0\) is the zero-labeled set.

It is unique-response when every zero-labeled vertex has at most one neighbor with label at least \(2\), while every positive-labeled vertex has no neighbor with label at least \(2\).

For \(\operatorname{Cr}_n\), the maximum degree is \(n-1\), so the largest permitted label is \(h\).

## Proof
Let
\[
V_2=\{v:f(v)\ge2\}.
\]
The unique-response condition implies that \(V_2\) is a \(2\)-packing. Indeed, two adjacent vertices cannot both lie in \(V_2\), because then each positive vertex would have a neighbor in \(V_2\). Two vertices at distance \(2\) cannot both lie in \(V_2\), because their common neighbor would either be zero and have two \(V_2\)-neighbors, or be positive and have a \(V_2\)-neighbor.

In a crown graph, any two distinct vertices in the same bipartition class have distance \(2\). Two vertices in opposite classes are adjacent unless they form one deleted matched pair. Hence
\[
|V_2|\le2,
\]
and a two-vertex \(V_2\) must be exactly one deleted pair \(\{a_i,b_i\}\).

If \(V_2=\varnothing\), then no vertex can be labeled \(0\), because a zero needs a strong defender. Since labels at least \(2\) are also absent, every vertex has label \(1\). This gives the unique all-one function.

Suppose \(V_2=\{d\}\). Every neighbor of \(d\) must be zero: it cannot be positive, because a positive vertex may not have a \(V_2\)-neighbor. Conversely, every nonneighbor of \(d\), other than \(d\) itself, must be positive because a zero there would have no \(V_2\)-neighbor. Thus the labeling outside \(d\) is forced. The defender \(d\) has exactly \(n-1\) zero neighbors, so the strong Roman inequality forces
\[
f(d)\ge1+\left\lceil\frac{n-1}{2}\right\rceil=h.
\]
Since \(h\) is also the maximum allowed label, \(f(d)=h\). This gives exactly \(2n\) functions of weight \(n+h\).

Finally suppose \(|V_2|=2\). Then
\[
V_2=\{a_i,b_i\}
\]
for some \(i\). Every other vertex is adjacent to exactly one of these two defenders, so the unique-response condition forces every other vertex to be zero. Each defender has exactly \(n-1\) zero neighbors, hence both must receive label \(h\). Conversely, this labeling is valid: every zero has exactly one defender, the two defenders are nonadjacent, and each has sufficient strength. Thus there are exactly \(n\) such functions of weight \(2h\).

These three cases are exhaustive, proving the enumerator. Since
\[
2h<n+h<2n
\]
for every \(n\ge3\), the third family is precisely the minimum family.

## Verification
The included verifier constructs \(\operatorname{Cr}_n\) directly and tests the unique-response and strong Roman conditions from their definitions for every allowed labeling for
\[
3\le n\le5.
\]
It independently compares every feasible labeling with the three-family classification and compares the full weight distribution with the displayed enumerator.

## Relationship to prior work
The 2021 paper introducing unique-response strong Roman domination proves that the vertices with labels at least \(2\) form a \(2\)-packing and gives a general optimization characterization over \(2\)-packings. It also determines
\[
u_{StR}(K_{n,m})
=
\left\lceil\frac n2\right\rceil+m
\qquad(n\ge m\ge1).
\]
Its searchable full text contains no crown occurrence.

A 2026 paper determines the ordinary strong Roman domination number of crown graphs and obtains the same parity-dependent scalar value
\[
n+1\quad\text{or}\quad n+2.
\]
Its crown construction uses the two endpoints of one deleted matched pair as strong vertices. The result here is stronger in a different direction: it proves that this construction is unique-response, classifies every unique-response strong Roman function at every weight, and counts all of them.

The contrast with complete bipartite graphs is structural. Deleting one perfect matching creates \(n\) two-vertex \(2\)-packings, and these support the \(n\) minimum functions. Thus a sparse, highly organized edge deletion can substantially reduce the unique-response strong Roman number while simultaneously making all feasible functions rigid enough to enumerate.

## Limitations
The theorem concerns unique-response strong Roman domination, not ordinary strong Roman domination by itself. The scalar ordinary strong Roman value for crowns is prior work and is not claimed as new.

The exhaustive verification through \(n=5\) is corroborative only. The arbitrary-\(n\) result follows from the \(2\)-packing classification and the forced labels in the proof.

A differently phrased or non-indexed crown treatment may exist despite the targeted literature searches.

## References
1. D. A. Mojdeh, G. Hao, I. Masoumi, A. Parsian, “Unique response strong Roman dominating functions of graphs,” Electronic Journal of Graph Theory and Applications 9(2) (2021), 469–484, DOI 10.5614/ejgta.2021.9.2.18; published 16 October 2021.
2. J. C. Valenzuela-Tripodoro, M. A. Mateos-Camacho, M. Cera López, M. P. Álvarez-Ruíz, “Complexity and Exact Values for [k]-Roman and Strong Roman Domination for Specific Graph Families,” Mathematics 14(9) (2026), 1535, DOI 10.3390/math14091535.
