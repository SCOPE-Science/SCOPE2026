# Order-Optimal Affine Locality Witnesses

## Claim

For every prime power q>=3 there is a connected simple bipartite q-regular graph
G_q of girth at least 6 with an induced matching M_q such that

\[
|V(G_q)|=2q(2q-1),\quad |M_q|=2q-1,\quad \nu_s(G_q)=q^2.
\]

M_q is locally optimal under one-edge additions and one-for-two exchanges.
No q-regular graph with the same ratio can have fewer vertices.

## Lower Bound

For a triangle- and 4-cycle-free q-regular graph, Theorem 5 of
Fürst--Leichter--Rautenbach (arXiv:1708.02028) gives
\(|M|\ge m/q^2=|V|/(2q)\) for a matching with these local-search conditions.
Every induced matching has disjoint conflict sets of size at most 2q-1, so
\(\nu_s(G)\le m/(2q-1)=q|V|/[2(2q-1)]\). If the ratio is q^2/(2q-1),
these force \(|M|=|V|/(2q)\). Integrality and
\(\gcd(q^2,2q-1)=1\) imply \(2q-1\mid |M|\), hence
\(|V|\ge2q(2q-1)\).

## Construction

Let F be the field of q elements. Make two copies s=0,1 of the partial affine
incidence graph with point vertices P_s(x,y), x,y in F, and line vertices
L_s(a,b), a in F* and b in F. Join P_s(x,y) to L_s(a,b) iff y=ax+b.
Add cross edges

\[
P_0(x,y)P_1(y-x,y).
\]

The map (x,y)->(y-x,y) is an involution. Every point has q-1 incidence
neighbors and one cross neighbor; every line has q incidence neighbors. Thus
the graph is q-regular, bipartite, and has
\(|V|=2q^2+2q(q-1)=2q(2q-1)\) and \(m=q^2(2q-1)
\) edges.

Let F0 be all q^2 cross edges. It is an efficient edge dominating set: every
incidence edge has exactly one endpoint at a cross edge, namely its point
endpoint. Cardoso et al., DOI 10.1016/j.dam.2008.01.021, Theorem 2.1, proves
that an efficient edge dominating set is a maximum induced matching. Hence
\(\nu_s=q^2=m/(2q-1)\).

For the local matching, let A consist of all points P_s(0,y), together with
the lines L_s(1,b) for b nonzero. The induced edges in A are the cross edge
at (0,0) and, in each copy, the q-1 edges
P_s(0,b)L_s(1,b), b nonzero. They form M and |M|=2q-1.

Every vertex has exactly one neighbor in A: a point lies on one selected
slope-1 line unless it lies on the omitted line b=0, in which case its unique
cross neighbor is in A; each line has its unique x=0 point in A. Therefore A
is a total perfect code and M is an induced matching. The incidence copies
are connected because at least two nonzero slopes occur; the cross edges join
them. There are no triangles by bipartiteness. There are no 4-cycles inside
an affine incidence copy, and a 4-cycle using cross edges would require two
distinct point-point cross edges plus impossible point-line cross adjacencies.
Thus girth is at least 6.

The total-perfect-code property plus girth at least 6 implies every edge outside
M conflicts with at least one member of M, while the private conflict edges of
one member are pairwise mutually conflicting. Hence no addition or one-for-two
replacement is possible. This local predicate is also enumerated directly by
the checker.

## Independent Verification
Run `python3 artifacts/affine_locality_check.py`. It independently checks
the raw edge list for degrees, simplicity, connectedness, bipartition, girth,
both induced-matching predicates, total-perfect-code ownership, efficient-edge
domination, and every possible one-for-two exchange. It uses its own finite-field
arithmetic for prime and non-prime prime powers. For q=3 it exhaustively solves
maximum induced matching and finds 9 (6898 cached states). The observed checks
pass for q=3,4,5,7,8,9,11, with orders 30,56,90,182,240,306,462.

## Literature Boundary

Cardoso et al., Theorems 2.1 and 3.1, supplies the efficient-edge-domination
optimum certificate and regular equality. Fürst--Leichter--Rautenbach, Theorem 5
and Corollary 6(ii), supplies the local-search bound. Their hypotheses and
proofs do not impose the simultaneous total-perfect-code structure or the
minimum order. Neumann, arXiv:0906.2496, states Leighton's common finite-cover
theorem; it explains why the earlier arbitrary-size locality-gap candidate was
a routine cover consequence, but it does not produce this minimum-order result.

The Gotthilf--Lewenstein chapter (DOI 10.1007/11671411_21) remains inaccessible
through the full-text service. Its title and the later 2018 primary paper's
recovery of its approximation guarantee provide no specific theorem about this
simultaneous affine construction or its minimum order; the access failure is
recorded rather than treated as absence evidence.
