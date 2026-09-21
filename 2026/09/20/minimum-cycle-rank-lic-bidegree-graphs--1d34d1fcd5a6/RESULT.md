# Minimum cycle rank for locally irregular-connected bidegree graphs

## Definitions

For a finite simple connected graph \(G\), write
\[
\mu(G)=|E(G)|-|V(G)|+1
\]
for its cycle rank. An edge \(uv\) is **irregular** if \(d(u)\ne d(v)\).
The graph is **locally irregular-connected** (LIC) if every two vertices are
joined by a path all of whose edges are irregular. Equivalently, the spanning
subgraph consisting of all irregular edges is connected.

For integers \(1\le a<b\), let
\[
\mu_{\rm LIC}(a,b)=\min\{\mu(G): G\text{ is LIC and }\mathcal D(G)=\{a,b\}\}.
\]

## Main theorem

For every \(1\le a<b\),
\[
\boxed{
\mu_{\rm LIC}(a,b)=
\begin{cases}
\dfrac{b(a-1)}2,& a\text{ odd or }b\text{ even},\\[2mm]
\dfrac{a(b-1)}2,& a\text{ even and }b\text{ odd}.
\end{cases}}
\tag{1}
\]

Except for one flexible boundary family described below, all graphs attaining
(1) have the minimum possible order \(b+1\).

More precisely:

1. If \(a\) is odd or \(b\) is even, every minimizer is
   \[
   G=K_1\vee H,
   \]
   where \(H\) is an \((a-1)\)-regular graph on \(b\) vertices.

2. If \(a\ge4\) is even and \(b\) is odd, every minimizer is
   \[
   G=K_2\vee H,
   \]
   where \(H\) is an \((a-2)\)-regular graph on \(b-1\) vertices.

3. If \(a=2\) and \(b\) is odd, every minimizer has exactly two vertices
   \(u,v\) of degree \(b\). Put \(\varepsilon=1\) when \(uv\in E(G)\) and
   \(\varepsilon=0\) otherwise. There are \(t\ge1\) degree-2 vertices adjacent
   to both \(u\) and \(v\), and
   \[
   s=b-\varepsilon-t\ge0
   \]
   private degree-2 neighbors of each of \(u\) and \(v\). The \(2s\) private
   vertices induce a perfect matching, while the \(t\) common neighbors have
   no neighbor among the degree-2 vertices. Conversely every graph of this
   form is LIC, has degree set \(\{2,b\}\), and has cycle rank \(b-1\).

Thus (1) gives the exact first cycle rank at which a prescribed two-element
positive degree set can occur in an LIC graph.

## Proof

Let \(X\) be the vertices of degree \(b\), let \(Y\) be the vertices of degree
\(a\), and put \(x=|X|\), \(y=|Y|\). In a bidegree graph the irregular edges
are exactly the edges between \(X\) and \(Y\). Since \(G\) is LIC, the
bipartite spanning graph \(G[X,Y]\) is connected. In particular every vertex
has a neighbor in the opposite degree class. Also \(x+y\ge b+1\), because a
vertex of degree \(b\) is present.

The degree sum gives
\[
2|E(G)|=bx+ay,
\]
and hence
\[
\mu(G)=\frac{(b-2)x+(a-2)y}{2}+1.
\tag{2}
\]

### When one vertex has degree \(b\)

Suppose \(x=1\). Connectivity of \(G[X,Y]\) forces the unique vertex of \(X\)
to be adjacent to every vertex of \(Y\). Its degree is \(b\), so \(y=b\).
Every vertex of \(Y\) therefore has \(a-1\) neighbors inside \(Y\). Thus
\(G=K_1\vee H\), where \(H\) is \((a-1)\)-regular on \(b\) vertices.
Such an \(H\) exists exactly when
\[
b(a-1)\equiv0\pmod 2,
\]
because \(0\le a-1<b\); this parity condition is equivalent to
"\(a\) odd or \(b\) even".

### Lower bound for \(a\ge3\)

Since \(y\ge b+1-x\), equation (2) gives
\[
\mu(G)\ge
\frac{(a-2)(b+1)+(b-a)x}{2}+1.
\tag{3}
\]
The right side is strictly increasing in \(x\), because \(b>a\).

If \(a\) is odd or \(b\) is even, \(x=1\) is feasible and (3) gives
\[
\mu(G)\ge\frac{b(a-1)}2.
\]
Equality forces \(x=1\) and \(x+y=b+1\), giving exactly the graphs in item 1.

If \(a\) is even and \(b\) is odd, the preceding parity argument rules out
\(x=1\), so \(x\ge2\). Equation (3) gives
\[
\mu(G)\ge\frac{a(b-1)}2.
\]
Equality forces \(x=2\), \(y=b-1\). Since the graph then has order \(b+1\),
both degree-\(b\) vertices are universal. Consequently they are adjacent,
every vertex of \(Y\) is adjacent to both, and \(G[Y]\) is
\((a-2)\)-regular. This is item 2. Such regular graphs exist because
\((b-1)(a-2)\) is even and \(0\le a-2<b-1\).

### The cases \(a=1\) and \(a=2\)

If \(a=1\), connectedness of \(G[X,Y]\) forces \(x=1\): a degree-1 vertex
cannot lie internally on a path joining two vertices of \(X\). Hence
\(G=K_{1,b}\), and \(\mu(G)=0\), agreeing with (1).

If \(a=2\), equation (2) becomes
\[
\mu(G)=\frac{(b-2)x}{2}+1.
\tag{4}
\]
For even \(b\), \(x=1\) is feasible and gives \(\mu=b/2\); the preceding
one-high-vertex argument gives item 1 (here \(H\) is a perfect matching).
For odd \(b\), \(x=1\) is impossible, so \(x\ge2\); (4) gives
\(\mu\ge b-1\), with equality exactly when \(x=2\).

Let the two degree-\(b\) vertices be \(u,v\). Every degree-2 vertex must be
adjacent to at least one of \(u,v\), and connectedness of the irregular-edge
subgraph forces at least one common neighbor of \(u,v\). A common neighbor
already has both of its incident edges, while every private neighbor has one
remaining incident edge, necessarily to another private degree-2 vertex.
Thus the private vertices induce a perfect matching. Comparing the degrees of
\(u\) and \(v\) gives the same number \(s=b-\varepsilon-t\) of private
neighbors on each side. This proves item 3 and its converse is immediate.

This completes the proof of (1) and of the extremal classification.

## Least size consequence

Let \(q_{\rm LIC}(a,b)\) be the least number of edges of an LIC graph with
degree set \(\{a,b\}\). Then
\[
\boxed{
q_{\rm LIC}(a,b)=
\begin{cases}
\dfrac{b(a+1)}2,& a\text{ odd or }b\text{ even},\\[2mm]
\dfrac{ab+2b-a}{2},& a\text{ even and }b\text{ odd}.
\end{cases}}
\tag{5}
\]
Indeed,
\[
|E(G)|=\frac{a(x+y)+(b-a)x}{2},
\]
with \(x+y\ge b+1\). In the first parity regime \(x\ge1\), while in the
second \(x\ge2\), giving (5); the constructions above attain equality.
Every size minimizer has order \(b+1\). In the exceptional case \(a=2\),
\(b\) odd, the larger-order graphs in item 3 minimize cycle rank but not size.

The unrestricted least-size problem for two-element degree sets is established
prior art; equation (5) is included here only to record that imposing LIC does
not increase the least size. It is not claimed as a new unrestricted degree-set
formula.

## Relation to the 2026 cycle-rank results

Chartrand and Zhang introduced the LIC degree-set problem in its present form.
Their Theorem 5 proves that every finite positive degree set with at least two
elements has an LIC realization of minimum possible order \(\max S+1\). Their
Proposition 5 / Theorem 9 proves that a two-element set is realizable by an LIC
graph of cycle rank exactly 2 if and only if it is \(\{2,3\}\) or \(\{2,4\}\).
Equation (1) strictly extends that bidegree statement: its value is 2 exactly
for those two sets. Their closing problem asks about prescribed cycle rank
\(r\ge3\); the present theorem determines, for every two-element degree set,
the exact first cycle rank at which such a realization becomes possible.

Tripathi and Vijay previously solved the unrestricted least-size problem for
all degree sets of cardinality at most three. Later work continued the general
least-size degree-set problem. Those results are treated here as prior art and
are not part of the novelty claim.

## Computational checks

The accompanying verification script performs two checks. First, it examines
every graph in the NetworkX Graph Atlas and verifies the minimum-size and
minimum-cycle-rank formulas for every LIC bidegree pair occurring there, as
well as the asserted extremal structure for every Atlas cycle-rank minimizer.
Second, it constructs the regular-graph extremizers deterministically for
1580 parameter pairs with \(1\le a\le40\) and \(a<b\le60\), checking degrees,
LIC connectivity, size, and cycle rank. The finite computation supports but
does not replace the proof.

## Originality and limitations

To the best of our knowledge, no checked source states the all-parameter
minimum cycle-rank formula (1) or the extremal classification above for LIC
bidegree graphs. The closest source is the May 2026 paper of Chartrand and
Zhang, whose full theorem statements for minimum order and cycle rank at most
2 were inspected; it stops at fixed cycle rank 2 and explicitly asks about
higher cycle rank. The older unrestricted least-size literature is a separate
problem and already covers two-element degree sets, so no novelty is claimed
for that unrestricted result.

Residual originality risk remains from very recent follow-up work after the
introduction of locally irregular-connected graphs, or from a result indexed
under bidegreed/cyclomatic terminology rather than degree-set terminology.
The complete theorem text of the 2006 least-size paper was not inspected
page-by-page in this review; its abstract explicitly covers degree sets of
cardinality at most three, and that unrestricted least-size result is therefore
conservatively treated as prior art.

## References

1. G. Chartrand and P. Zhang, *Locally Irregular-Connected Graphs*,
   Mathematics 14 (2026), 1827. https://doi.org/10.3390/math14111827
2. S. F. Kapoor, A. D. Polimeni, and C. E. Wall, *Degree sets for graphs*,
   Fundamenta Mathematicae 95 (1977), 189--194.
   https://eudml.org/doc/215021
3. A. Tripathi and S. Vijay, *On the least size of a graph with a given degree
   set*, Discrete Applied Mathematics 154 (2006), 2530--2536.
   https://doi.org/10.1016/j.dam.2006.04.003
4. J. Moondra, A. Sahdev, and A. Tripathi, *Exact and approximate results on
   the least size of a graph with a given degree set*, Discrete Applied
   Mathematics 333 (2023), 32--42. https://doi.org/10.1016/j.dam.2023.02.012
