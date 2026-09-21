# A local-lemma criterion for sequential edge orderings in bipartite graphs

## Result

Let \(G=(X,Y;E)\) be a finite simple bipartite graph with a proper edge-colouring
\(c:E\to\mathcal C\).  For a total order \(\prec\) of \(E\), let
\(s_\prec(v)\) be the sequence of colours on the edges incident with \(v\), read
in the order induced by \(\prec\).  We call \(\prec\) *distinguishing* if
\(s_\prec(u)\ne s_\prec(v)\) for every edge \(uv\).

For \(y,z\in Y\), write \(y\sim_J z\) when \(N_G(y)\cap N_G(z)\ne\varnothing\).

**Theorem.** Suppose every vertex of \(Y\) has degree \(d\ge2\), and the graph
\(J\) on \(Y\) defined above has maximum degree at most \(D\).  If
\[
   d!>\mathrm e\,(D+1),
\]
then every proper edge-colouring of \(G\) admits a distinguishing total order of
the edges.

In particular:

**Corollary.** Every properly edge-coloured finite simple \(d\)-regular
bipartite graph is sequentially orderable for every \(d\ge5\).  Hence every
proper edge-colouring of every connected 5-regular bipartite graph satisfies
the sequential-orderability conjecture of Gorzkowska and Kwaśny.

## Proof

Fix once and for all a total order \(<_{\mathcal C}\) of the colours.  Choose a
uniformly random total order \(<_{X}\) of \(X\).  From it define a total order
\(\prec\) of \(E\) as follows: first order the edge-stars at the vertices of
\(X\) according to \(<_{X}\); inside the block belonging to \(x\in X\), order
the incident edges increasingly by their colours under \(<_{\mathcal C}\).

Thus, for every \(x\in X\), the sequence \(s_\prec(x)\) is exactly the
increasing listing of the palette
\[
   P(x)=\{c(e):e\ni x\}.
\]

For each \(y\in Y\), let \(B_y\) be the event that \(s_\prec(y)\) is the
increasing listing of \(P(y)\).  Since the colouring is proper and \(G\) is
simple, the \(d\) edges at \(y\) have distinct colours and distinct neighbours
in \(X\).  The event \(B_y\) therefore prescribes exactly one of the \(d!\)
possible relative orders of the vertices in \(N_G(y)\), so
\[
   \Pr(B_y)=\frac1{d!}.
\]

If \(N_G(y)\cap N_G(z)=\varnothing\), then \(B_y\) and \(B_z\) depend on
relative orders of disjoint subsets of a uniform random permutation.  More
generally, \(B_y\) is independent of the collection of all events \(B_z\) whose
neighbourhoods are disjoint from \(N_G(y)\).  Hence the graph \(J\) is a
dependency graph for the family \(\{B_y:y\in Y\}\).  The symmetric Lovász local
lemma applies because
\[
   \mathrm e\,\Pr(B_y)(D+1)
   \le \frac{\mathrm e(D+1)}{d!}<1.
\]
Consequently there is a choice of \(<_{X}\) for which no event \(B_y\) occurs.

Fix such a choice.  Consider an edge \(xy\).  If \(P(x)\ne P(y)\), then the two
sequences \(s_\prec(x)\) and \(s_\prec(y)\) cannot be equal because they have
different multisets of entries.  If \(P(x)=P(y)\), then \(s_\prec(x)\) is the
increasing listing of this common palette, whereas \(B_y\) does not occur, so
\(s_\prec(y)\) is not that listing.  In either case
\(s_\prec(x)\ne s_\prec(y)\).  Thus \(\prec\) is distinguishing.

For the regular corollary, if \(G\) is \(d\)-regular, each \(y\in Y\) has \(d\)
neighbours, and each such neighbour belongs to the neighbourhood of at most
\(d-1\) other vertices of \(Y\).  Therefore
\[
   \Delta(J)\le d(d-1).
\]
At \(d=5\),
\[
   5!=120>21\mathrm e
     =\mathrm e\bigl(5\cdot4+1\bigr).
\]
Moreover
\[
 \frac{(d+1)!}{d(d+1)+1}\Big/
 \frac{d!}{d(d-1)+1}
 =
 \frac{(d+1)(d^2-d+1)}{d^2+d+1}>1
 \qquad(d\ge5),
\]
so \(d!>\mathrm e(d(d-1)+1)\) holds for every \(d\ge5\).  The theorem gives the
claim.

## Context and significance

Gorzkowska and Kwaśny introduced the present global edge-ordering problem for a
fixed proper edge-colouring.  Their 2026 preprint proves sequential
orderability when adjacent vertices have distinct palettes, and also for
connected regular graphs of degree at least six.  Their conjecture asks for all
connected graphs other than the two stated exceptional families; the remaining
regular degrees include \(3,4,5\).

The corollary above settles the entire bipartite subcase at degree \(5\), which
lies outside the published degree-at-least-six theorem.  The more general
criterion isolates the relevant obstruction for the block-order construction:
on one side of a bipartite graph, only the overlap graph of neighbourhoods
enters the local-lemma calculation.

## Limitations

The result does not settle arbitrary 5-regular graphs, nor the general
3-regular or 4-regular cases.  The numerical local-lemma condition is sufficient
rather than claimed necessary or sharp.  Originality is asserted only to the
best of our knowledge.  The arXiv abstract and indexed descriptions of the
2026 source paper were inspected, but the full manuscript was not available for
inspection here; a body-only remark or very recent parallel result is therefore
a residual originality risk.

## References

1. A. Gorzkowska and J. Kwaśny, *Distinguishing adjacent vertices by ordering
   edges*, arXiv:2609.11832, 2026.
2. P. Erdős and L. Lovász, *Problems and results on 3-chromatic hypergraphs and
   some related questions*, in *Infinite and Finite Sets*, Colloquia
   Mathematica Societatis János Bolyai 10, 1975, 609--627.
