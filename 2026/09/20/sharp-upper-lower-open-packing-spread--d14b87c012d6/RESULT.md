# Sharp upper-lower open-packing spread at fixed order

## Definitions

Let \(G\) be a finite simple graph of order \(n\). An **open packing** is a set
\(P\subseteq V(G)\) such that
\[
N(x)\cap N(y)=\varnothing
\qquad\text{for all distinct }x,y\in P.
\]
The **open packing number** \(\rho^o(G)\) is the maximum size of an open packing,
and the **lower open packing number** \(\rho_L^o(G)\) is the minimum size of a
maximal open packing.

## Main theorem

For every finite simple graph \(G\) of order \(n\ge2\),
\[
\boxed{2\rho^o(G)\le n+\rho_L^o(G).}
\tag{1}
\]
If \(\rho_L^o(G)=1\), the stronger estimate
\[
\boxed{2\rho^o(G)\le n}
\tag{2}
\]
holds. Consequently,
\[
\boxed{\rho^o(G)-\rho_L^o(G)\le
\left\lfloor\frac{n-2}{2}\right\rfloor.}
\tag{3}
\]
For every \(n\ge2\), equality in (3) is attained by a connected graph. Hence
\[
\max_{|V(G)|=n}\bigl(\rho^o(G)-\rho_L^o(G)\bigr)
=
\max_{\substack{|V(G)|=n\\G\text{ connected}}}
\bigl(\rho^o(G)-\rho_L^o(G)\bigr)
=
\left\lfloor\frac{n-2}{2}\right\rfloor.
\tag{4}
\]

For trees, the exact fixed-order maximum is
\[
\boxed{
\max_{|V(T)|=n}\bigl(\rho^o(T)-\rho_L^o(T)\bigr)=
\begin{cases}
0,&2\le n\le4,\\[1mm]
\left\lfloor\dfrac{n-2}{2}\right\rfloor,&n\ge5.
\end{cases}}
\tag{5}
\]
The upper bound in (5) for trees is not claimed as new: Henning and Slater
proved in 1999 that every tree \(T\) of order \(n\ge2\) satisfies
\(\rho^o(T)-\rho_L^o(T)\le(n-2)/2\), and exhibited equality for an infinite
subsequence of orders. The new claims here are the graph-wide inequalities
(1)--(3), the exact fixed-order extremum (4), and the order-by-order tree
sharpness in (5).

## Proof of (1)

Let \(P\) be a maximum open packing and let \(Q\) be a minimum-cardinality
maximal open packing. Write
\[
A=P\setminus Q,\qquad B=Q\setminus P,\qquad C=P\cap Q,
\qquad R=V(G)\setminus(P\cup Q).
\]
For every \(x\in A\), maximality of \(Q\) implies that \(Q\cup\{x\}\) is not
an open packing. Hence there are \(q_x\in Q\) and a witness
\(w_x\in N(x)\cap N(q_x)\). Necessarily \(q_x\in B\): if \(q_x\in P\), then
\(x\) and \(q_x\) are two vertices of the open packing \(P\) with a common
neighbor.

Fix \(q\in B\). The witnesses \(w_x\) belonging to distinct vertices
\(x\in A\) with \(q_x=q\) are distinct, since a repeated witness would be a
common neighbor of two vertices of \(P\). Among these witnesses at most one
can lie in \(P\), because two vertices of \(P\) that are both adjacent to
\(q\) would have the common neighbor \(q\). Similarly, at most one can lie
in \(Q\). All remaining witnesses lie in \(R\). Moreover, the sets of
\(R\)-witnesses associated with two distinct vertices of \(B\) are disjoint:
a common witness would be a common neighbor of two vertices of the open
packing \(Q\). Therefore
\[
|A|\le 2|B|+|R|.
\]
It follows that
\[
\rho^o(G)-\rho_L^o(G)=|A|-|B|
\le |B|+|R|=n-|P|=n-\rho^o(G),
\]
which is equivalent to (1).

## The case \(\rho_L^o(G)=1\)

Let \(Q=\{q\}\) be a maximal open packing of size one and let \(P\) be a
maximum open packing. If \(|P|>1\), then \(q\notin P\): otherwise every other
vertex of \(P\) would, by maximality of \(\{q\}\), have a common neighbor with
\(q\), contradicting that \(P\) is an open packing.

For each \(x\in P\), choose a witness
\(w_x\in N(x)\cap N(q)\). These witnesses are distinct, and at most one of
them lies in \(P\). Also \(q\) itself is not a witness. Thus the \(|P|\)
witnesses fit into at most \(n-|P|-1\) vertices outside \(P\cup\{q\}\), plus
at most one vertex of \(P\). Hence
\[
|P|\le n-|P|,
\]
which proves (2). The case \(|P|=1\) is immediate for \(n\ge2\).

If \(\rho_L^o(G)=1\), (2) gives
\[
\rho^o(G)-\rho_L^o(G)
\le \left\lfloor\frac n2\right\rfloor-1
=\left\lfloor\frac{n-2}{2}\right\rfloor.
\]
If \(\rho_L^o(G)\ge2\), (1) gives
\[
\rho^o(G)-\rho_L^o(G)
\le \frac{n-\rho_L^o(G)}2
\le \frac{n-2}{2},
\]
proving (3).

## Sharp connected constructions

For \(n=2,3\), the bound is zero and is attained by \(K_2\) and \(K_3\).
For \(n=4\), take a triangle with one pendant leaf. It has
\(\rho_L^o=1\) and \(\rho^o=2\).

For odd \(n=2m+1\ge5\), take \(K_{m+1}\) and attach one pendant leaf to each
of \(m\) clique vertices, leaving one clique vertex without a pendant leaf.
The leafless clique vertex is a maximal open packing by itself, while the
\(m\) pendant leaves form an open packing. Equation (2) then forces
\[
\rho_L^o=1,\qquad \rho^o=m,
\]
so the gap is \(m-1=\lfloor(n-2)/2\rfloor\). This is the same family used by
Sahul Hamid and Saravanakumar to show that the two open-packing parameters can
be arbitrarily far apart.

For even \(n=2m\ge6\), choose positive integers \(p,q\) with
\(p+q=m-1\). Let \(D_{p,q}\) be the tree obtained from adjacent centers
\(u,v\), with \(p\) internally disjoint length-two pendant paths at \(u\)
and \(q\) such paths at \(v\). Then
\[
\rho_L^o(D_{p,q})=2,\qquad \rho^o(D_{p,q})=m+1.
\]
One transparent verification uses the open-neighborhood graph
\(N_o(G)\), whose edges join pairs of vertices having a common neighbor in
\(G\). Maximal open packings of \(G\) are exactly maximal independent sets of
\(N_o(G)\). In \(N_o(D_{p,q})\), the two bipartition classes of \(D_{p,q}\)
are separate components. On one side, \(u\) is universal, the \(q\) vertices
next to \(v\) form a clique, and the \(p\) terminal leaves on the \(u\)-arms
are independent; hence that component has independence number \(p+1\) and
independent domination number \(1\). The other component symmetrically has
values \(q+1\) and \(1\). Summing gives the displayed values, and the gap is
\(m-1=(n-2)/2\).

These constructions prove (4).

## Tree sharpness at every order

The cases \(2\le n\le4\) are immediate. The path \(P_5\) has
\(\rho_L^o(P_5)=2\) and \(\rho^o(P_5)=3\), giving the required gap at order
five. The trees \(D_{p,q}\) above settle every even order \(n\ge6\).

For odd \(n\ge7\), start with an even-order extremal tree \(D_{p,q}\) on
\(n-1\) vertices and attach one additional leaf to a support vertex of one
length-two arm, making two terminal leaves at that support. In the relevant
component of \(N_o\), this adds a vertex adjacent precisely to the universal
center and to the old terminal leaf. The independence number and independent
domination number of that component remain \(p+1\) and \(1\), respectively;
the other component is unchanged. Thus both open-packing parameters, and
hence their difference, are unchanged. This yields the value
\(\lfloor(n-2)/2\rfloor\) for every odd \(n\ge7\), proving (5).

## Computational checks

The accompanying script performs exact subset enumeration. It verifies (1),
(2), and (3) for every graph of order at least two in the NetworkX Graph
Atlas, and independently checks the tree formula for every nonisomorphic tree
of orders \(2\) through \(12\). The output is supplied separately in
`artifacts/expected_output.txt`. These finite checks support but do not replace
the proof.

## Relation to prior literature and originality

Henning and Slater introduced the lower and upper open-packing parameters and
proved the tree inequality
\(\rho^o(T)-\rho_L^o(T)\le(n-2)/2\) in their 1999 paper; their sharpness family
has order \(4k+2\). Sahul Hamid and Saravanakumar (2015) explicitly observed
that the difference can be arbitrarily large and gave realization theorems for
prescribed lower and upper open-packing values. Hartnell and Rall (2020)
recast maximal open packings as maximal independent sets of the
open-neighborhood graph and studied the equality class
\(\rho_L^o=\rho^o\). Recent work of Abiad, Yang, and Zhou (2026) develops
spectral bounds for the upper open-packing number.

To the best of our knowledge, the checked sources do not state (1), the
one-point sharpening (2), the exact fixed-order connected extremum (4), or the
all-order tree extremum (5). The principal residual originality risk is an
older or differently indexed result phrased in terms of the independence and
independent-domination numbers of open-neighborhood graphs. The already known
1999 tree upper bound is explicitly excluded from the novelty claim.

## References

1. M. A. Henning and P. J. Slater, *Open Packing in Graphs*, Journal of
   Combinatorial Mathematics and Combinatorial Computing 29 (1999), 3--16.
   https://combinatorialpress.com/jcmcc-articles/volume-029/open-packing-in-graphs/
2. I. Sahul Hamid and S. Saravanakumar, *Packing Parameters in Graphs*,
   Discussiones Mathematicae Graph Theory 35 (2015), 5--16.
   https://doi.org/10.7151/dmgt.1775
3. B. L. Hartnell and D. F. Rall, *On graphs having one size of maximal open
   packings*, arXiv:2006.01616 (2020).
   https://arxiv.org/abs/2006.01616
4. A. Abiad, Y. Yang, and J. Zhou, *Spectral bounds for distance coloring and
   packing parameters of graphs via semidefinite programming*, arXiv:2606.04856
   (2026). https://arxiv.org/abs/2606.04856
