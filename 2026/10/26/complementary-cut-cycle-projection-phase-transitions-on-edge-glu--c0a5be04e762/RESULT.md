# Complementary cut–cycle projection phase transitions on edge-glued cliques

## Finding

Let \(a,b\ge2\) be integers, and form a simple graph \(G_{a,b}\) by identifying one edge, including both endpoints, of \(K_{a+2}\) with one edge of \(K_{b+2}\), keeping the common edge only once. Equip all edges with unit weight. On the real edge-coordinate spaces let \(Q\) be the Euclidean-orthogonal projection onto the cut space, and let \(P=I-Q\) project onto the cycle space. Both the induced \(\ell_1\) and \(\ell_\infty\) norms of each projection agree.

Write \(T=a+b+2\), and define
\[
 A(a,b)=\frac{2a+1}{a+2}+\frac{b+1}{T},\qquad
 B(a,b)=1+\frac{2(a-1)}{a+2}+\frac bT.
\]
The exact endpoint operator norms are
\[
 \boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=\max\{A(a,b),A(b,a)\}},
\]
\[
 \boxed{\|P\|_{1\to1}=\|P\|_{\infty\to\infty}
 =\max\left\{3-\frac6T,B(a,b),B(b,a)\right\}}.
\]
The five edge-orbit column sums, including the common-edge and private-internal-edge columns, are given in the proof. The maximizing edge type for the cut projection changes according to the sign of \((a-b)(a+b+2-ab)\). The corresponding comparison between the two private-to-common edge types for the cycle projection changes according to the sign of \((a-b)(4a+4b+8-ab)\), while common-edge columns also compete when one of the private part sizes is at most four.

In particular, for every integer \(b\ge5\), on \(G_{2,b}\) **every** cut-norm maximizing edge joins the common edge's endpoints to the private two-vertex side, whereas **every** cycle-norm maximizing edge joins them to the private \(b\)-vertex side. Thus the two canonical complementary projections have strictly different maximizing edge orbits in an infinite natural family.

The sharp unattained global bounds are
\[
 \boxed{\sup_{a,b\ge2}\|Q\|=3,\qquad \sup_{a,b\ge2}\|P\|=4}.
\]
Both suprema are approached by \(a=k\), \(b=k^2\) as \(k\to\infty\). These bounds are one unit larger than the limiting respective canonical projection norms on standalone complete graphs.

## Assumptions and scope

There are precisely two common vertices \(u,v\), which are adjacent. Their private vertex sets \(U\) and \(W\) have sizes \(a\) and \(b\), respectively. The induced graphs on \(\{u,v\}\cup U\) and \(\{u,v\}\cup W\) are cliques and no edge joins \(U\) to \(W\). A graph edge is oriented arbitrarily for incidence bookkeeping. If \(D\) is the vertex-by-edge signed incidence matrix and \(L=DD^{\mathsf T}\), then \(Q=D^{\mathsf T}L^+D\) and \(P=I-Q\), with \(+\) denoting the Moore–Penrose pseudoinverse. Coordinate norms use standard unit edge weights; no minimization over other projections is asserted. Every edge belongs to a triangle because \(a,b\ge2\).

## Proof

For an oriented edge \(e=rs\), solve \(Lf=\delta_r-\delta_s\). Its \(Q\)-column has components \(f(x)-f(y)\) for graph edges \(xy\), up to an irrelevant orientation sign. Hence its absolute column sum is the sum of the absolute potential differences along *all* edges. The diagonal entry \(Q_{ee}=f(r)-f(s)\) is effective resistance; it is strictly between zero and one on this graph. Since \(P=I-Q\), each cycle-column sum equals
\[
 1+\sum_{xy\in E}|f(x)-f(y)|-2[f(r)-f(s)]. \tag{1}
\]
For all below, potentials are specified only up to an additive constant. The three displayed source types and their exchanges of \(a,b\) exhaust every edge orbit under permutations of each private set and interchange of \(u,v\).

**Common edge.** For \(e=uv\), put \(d=1/T\) and set \(f(u)=d\), \(f(v)=-d\), all other potentials zero. The Laplacian equation holds because \(u\) and \(v\) have degree \(a+b+1\). There is one edge carrying magnitude \(2d\) and \(2(a+b)\) edges carrying \(d\). Hence the cut column sum is \(2(a+b+1)/T\), the diagonal is \(2/T\), and by (1) the cycle column sum is \(3-6/T\).

**Internal edge.** For distinct \(x,y\in U\) put \(c=1/(a+2)\), set \(f(x)=c\), \(f(y)=-c\), all other potentials zero. It solves \(Lf=\delta_x-\delta_y\): the local clique's nonzero antisymmetric mode has eigenvalue \(a+2\) and neither the common vertices nor the second clique carry net current. The absolute sum is \(2(a+1)/(a+2)\), the diagonal is \(2/(a+2)\), and the cycle sum is \(3-6/(a+2)\). Exchange \(a,b\) for edges internal to \(W\).

**Private-to-common edge.** For \(e=ux\) with \(x\in U\), write \(c=1/(a+2)\), \(d=1/T\). Set
\[
 f(u)=\frac{c+d}2,\qquad f(v)=\frac{c-d}2,\qquad
 f(x)=-c,\qquad f(z)=0\quad(z\in U\setminus\{x\}),
\]
\[
 f(w)=\frac c2\quad(w\in W).
\]
Indeed, on \(W\) the contribution from \(u,v\) cancels because \(f(u)+f(v)=c\); on \(U\setminus\{x\}\) it cancels against \(f(x)=-c\); at \(x\) the Laplacian is \(-1\); at \(u\) and \(v\) it is \(+1\) and zero, respectively. These equations also follow by splitting the source into the antisymmetric pair \((\delta_u-\delta_v)/2\) and a symmetric source localized to the first clique.

Because \(c>d>0\), the potentials obey the strict ordering
\[
 f(u)>f(w)>f(v)>f(z)>f(x)
 \quad(w\in W,\ z\in U\setminus\{x\}).
\]
The edge \(uv\) contributes \(d\); the two edges \(ux,vx\) contribute together \(3c\); for each of the other \(a-1\) private vertices the three edges to \(u,v,x\) contribute \(2c\); and the \(2b\) edges from common vertices to \(W\) contribute \(bd\). All remaining edges contribute zero. Therefore the cut sum and the diagonal are
\[
 (2a+1)c+(b+1)d=A(a,b),\qquad Q_{ee}=\frac{3c+d}{2}.
\]
Equation (1) yields the cycle sum \(B(a,b)=1+2(a-1)c+bd\). Exchange \(a,b\) for an edge joining \(u\) or \(v\) to \(W\).

Collecting the five edge-orbit column sums gives the complete exact table:

| Edge type | Cut column sum | Cycle column sum |
| --- | --- | --- |
| Common edge \(uv\) | \(2(a+b+1)/T\) | \(3-6/T\) |
| Common–\(U\) | \(A(a,b)\) | \(B(a,b)\) |
| Common–\(W\) | \(A(b,a)\) | \(B(b,a)\) |
| Within \(U\) | \(2(a+1)/(a+2)\) | \(3-6/(a+2)\) |
| Within \(W\) | \(2(b+1)/(b+2)\) | \(3-6/(b+2)\) |

For the cut columns,
\[
 A(a,b)-\frac{2(a+b+1)}T=\frac{b(a-1)}{(a+2)T}>0,
 \quad A(a,b)-\frac{2(a+1)}{a+2}=\frac{b(a+1)}{(a+2)T}>0.
\]
The swapped inequalities eliminate the common and internal edges from cut-norm maximization. For the cycle columns,
\[
 B(a,b)-\left(3-\frac6{a+2}\right)=\frac bT>0,
 \quad B(a,b)-\left(3-\frac6T\right)=\frac{b(a-4)}{(a+2)T}.
\]
Again exchanging the parts eliminates the two internal-edge types, leaving precisely the stated three candidates. As the matrices \(Q,P\) are symmetric, their induced \(\ell_1\)- and \(\ell_\infty\)-norms equal their largest absolute column sums.

The differences between the private-to-common column types factor *exactly* as
\[
 A(a,b)-A(b,a)=\frac{(a-b)(a+b+2-ab)}{(a+2)(b+2)T},
\]
\[
 B(a,b)-B(b,a)=\frac{(a-b)(4a+4b+8-ab)}{(a+2)(b+2)T}.
\]
These give both phase boundaries. At \(a=2<b\), the first numerator is positive precisely when \(b>4\); the second is negative. Also \(B(b,2)>3-6/T\) precisely when \(b>4\). Thus for all \(b\ge5\) the cut and cycle maxima occur strictly on the opposite private sides, as claimed.

Finally,
\[
 A(a,b)=3-\frac3{a+2}-\frac{a+1}{T}<3,
\]
\[
 B(a,b)=4-\frac6{a+2}-\frac{a+2}{T}<4.
\]
The common-edge cycle candidate is below three, and the analogous swapped candidates satisfy the same bounds. Along \(a=k,b=k^2\) each displayed correction tends to zero, proving the sharp unattained suprema. This completes the proof.

## Verification

Run `python CHECK.py` with Python 3 and no third-party packages. It constructs the graphs, independently inverts grounded graph Laplacians over exact rational numbers, and verifies every edge column for sixteen parameter configurations, representative columns for four additional configurations, and 1,089 exact rational comparison identities. The checker does not certify the infinite theorem; that follows from the explicit Laplacian solutions and the algebra above.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii study invariant and minimum cycle-space projections and calculate the cut-projection norm on a Hamming cube. Their 2023 paper does not supply this two-clique edge-sum classification; in particular, gluing cliques along a single edge is not a Hamming graph. Polettini's 2014 graph paper develops complementary oblique cycle/cocycle projections and Kirchhoff–Symanzik matrices rather than these Euclidean-orthogonal endpoint norms. The result here is for **canonical orthogonal projections** only, not minimum-norm projections among all possible complements.

The individual complete graphs have cut endpoint norms \(2(a+1)/(a+2)\) and \(2(b+1)/(b+2)\); their cycle endpoint norms equal \(3-6/(a+2)\) and \(3-6/(b+2)\). Gluing along an edge creates new coupling through the common edge and, in the unbalanced large-clique regime, sharp unattained global constants three and four. This shows that neither endpoint norm simply equals the maximum of its separate-clique values.

## Limitations

The result is unweighted, finite, real and restricted to exactly two complete graphs identified along one existing edge. It classifies the canonical Euclidean-orthogonal cut and cycle projections only; it does not determine minimum norms over all projections, intermediate \(\ell_p\) norms, arbitrary clique-sum graphs, or positive edge weights. Bibliographic searches do not prove uniqueness or exclude every less-indexed equivalent electrical-current calculation. Independent mathematical audit has not been performed.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first posted 21 May 2023, especially Sections 1.1, 2.6 and 2.7.
2. M. Polettini, *Cycle/cocycle oblique projections on oriented graphs*, arXiv:1405.0899, first posted 7 May 2014, especially Sections 3.1 and 3.5.
