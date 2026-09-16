# Order-Optimal Affine Locality Witnesses

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is claimed only to the best of our knowledge; consult REVIEW.md for search evidence and inaccessible sources. Publication is not peer review or a guarantee of priority.

## Claim

For every prime power \(q\ge3\), there is a connected simple bipartite
\(q\)-regular graph \(G_q\) of girth at least six with an induced matching
\(M_q\) such that

\[
 |V(G_q)|=2q(2q-1),\qquad |M_q|=2q-1,
 \qquad \nu_s(G_q)=q^2,
\]

and \(M_q\) is locally optimal under adding one edge or replacing one edge by
two edges. Among all \(q\)-regular girth-at-least-six graphs with this exact
locality ratio,

\[
 \frac{\nu_s(G)}{|M|}=\frac{q^2}{2q-1},
\]

the order \(2q(2q-1)\) is minimum.

Here an induced matching is a set of edges whose endpoints induce a 1-regular
graph, \(\nu_s\) is its maximum size, and a one-for-two move means deleting one
edge of the current matching and adding two edges outside it.

## Construction

Let \(F=\mathbb F_q\). For \(s\in\{0,1\}\), make point vertices
\(P_s(x,y)\) for \(x,y\in F\), and line vertices \(L_s(a,b)\) for
\(a\in F^*\), \(b\in F\). Join \(P_s(x,y)\) to \(L_s(a,b)\) exactly when
\(y=ax+b\). Add the cross edges

\[
 P_0(x,y)P_1(y-x,y)\qquad(x,y\in F).
\]

The map \((x,y)\mapsto(y-x,y)\) is an involution. A point has \(q-1\)
incidence neighbors and one cross neighbor; a line has \(q\) incidence
neighbors. Thus \(G_q\) is \(q\)-regular and bipartite, with

\[
 |V(G_q)|=2q^2+2q(q-1)=2q(2q-1),
 \qquad |E(G_q)|=q^2(2q-1).
\]

The incidence copies are connected because the two nonzero directions 1 and
any second nonzero field element generate all point differences; the cross edges
join the copies. There are no triangles. Two affine lines of distinct slopes
meet once and parallel lines do not meet, so an incidence copy has no 4-cycle.
A 4-cycle using cross edges would require two point-to-point cross edges and
point-to-line edges joining their endpoints, which is impossible. Hence the
graph is simple, connected, and has girth at least six.

## Maximum Matching Certificate

Let \(F_q^*\) be the set of all \(q^2\) cross edges. It is an induced matching.
Every incidence edge is dominated by exactly one cross edge, namely the cross
edge incident with its point endpoint. Therefore \(F_q^*\) is an efficient edge
dominating set (also called a dominating induced matching).

Cardoso, Cerdeira, Delorme and Silva, *Efficient edge domination in regular
graphs*, Discrete Applied Mathematics 156 (2008), DOI `10.1016/j.dam.2008.01.021`,
Theorem 2.1, proves that every efficient edge dominating set is a maximum
induced matching. Consequently \(\nu_s(G_q)=q^2\). The same value follows from
the regular equality \(|E|/(2q-1)
=q^2\), proved in their Theorem 3.1 for regular graphs possessing an efficient
edge dominating set.

## Local Certificate

Let

\[
 A=\{P_s(0,y):s\in\{0,1\},y\in F\}
   \cup\{L_s(1,b):s\in\{0,1\},b\in F^*\}.
\]

The edges induced by \(A\) are the cross edge at \((0,0)\), together with
\(P_s(0,b)L_s(1,b)\) for each \(s\) and each nonzero \(b\). They form an
induced matching \(M_q\) of size \(1+2(q-1)=2q-1\).

Every vertex has exactly one neighbor in \(A\). A point on a selected
slope-one line has that line as its unique \(A\)-neighbor; a point on the
omitted line \(y=x\) has its cross neighbor in \(A\). Every line has its unique
point with \(x=0\) in \(A\). Thus \(A\) is a total perfect code and \(M_q\)
is induced.

For every edge outside \(M_q\), its endpoint(s) in \(A\) identify a member of
\(M_q\) that conflicts with it. Girth at least six prevents two distinct
\(A\)-owners from coinciding through a triangle or 4-cycle, and prevents an
edge joining two private neighbors of the same matching edge. Therefore every
edge is blocked by \(M_q\), and the private edges of any one member of \(M_q\)
are pairwise mutually conflicting. No edge can be added, and no one edge of
\(M_q\) can be replaced by two outside edges.

## Minimum Order

Fürst, Leichter and Rautenbach, *Locally Searching for Large Induced Matchings*,
arXiv:1708.02028, Theorem 5, proves for triangle- and 4-cycle-free graphs that
a matching stable under the one-edge and one-for-two local moves has

\[
 |M|\ge\frac{m}{q^2}=\frac{|V|}{2q}.
\]

For every \(q\)-regular graph, conflict sets of the edges in an induced matching
are disjoint and each has at most \(2q-1\) edges. Hence

\[
 \nu_s(G)\le\frac{m}{2q-1}
 =\frac{q|V|}{2(2q-1)}.
\]

If \(\nu_s(G)/|M|=q^2/(2q-1)\), the two inequalities force
\(|M|=|V|/(2q)\). Since \(\nu_s(G)=|M|q^2/(2q-1)\) is integral and
\(\gcd(q^2,2q-1)=1\), \(2q-1\mid |M|\). Thus
\(|V|=2q|M|\ge2q(2q-1)\), attained by the construction.

## Reproducible Evidence

Run:

```text
python3 output/artifacts/affine_locality_check.py
```

The checker independently constructs finite fields, builds the raw edge list,
and verifies degrees, simplicity, connectedness, bipartition, girth, both
matching predicates, total-perfect-code ownership, efficient-edge-domination
ownership, and the complete one-for-two exchange pool. For \(q=3\), it also
exhaustively optimizes over all 45 edges and obtains \(\nu_s=9\). It passes for
\(q=3,4,5,7,8,9,11\), with orders
\(30,56,90,182,240,306,462\), respectively.

## Scope

The result is an extremal construction and exact locality benchmark, not an
improvement of the known approximation factor. It applies to prime-power
degrees; extension to all integers \(q\) is not claimed. The affine construction
uses two distinguished line directions and the total-perfect-code structure,
which are the substantive residual beyond the general local-search and efficient
edge-domination theorems.
