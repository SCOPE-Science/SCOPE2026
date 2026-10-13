# Automorphisms and metric bases of three-dimensional finite-field dot-product graphs

## Finding

Let \(q\) be an odd prime power, put
\[
v=q^2+q+1,
\]
and let \(G_q=TD(\mathbb F_q,3)\) be the graph with vertex set
\[
\mathbb F_q^3\setminus\{0\},
\]
where distinct vectors \(x,y\) are adjacent exactly when
\[
x\cdot y=0.
\]

Then the \(q-1\) nonzero vectors on each projective point form a maximal twin class, the quotient by these classes is the orthogonal polarity graph of \(\operatorname{PG}(2,q)\), and
\[
\operatorname{Aut}(G_q)
\cong
S_{q-1}^{\,q^2+q+1}\rtimes \operatorname{P\Gamma O}(3,q).
\]

Furthermore,
\[
\operatorname{Det}(G_q)
=
\dim(G_q)
=
(q^2+q+1)(q-2),
\]
where \(\operatorname{Det}\) is the determining number and \(\dim\) is metric dimension.

The minimum determining sets and the metric bases coincide exactly: each is obtained by omitting one nonzero vector from every one-dimensional subspace of \(\mathbb F_q^3\). Consequently the number of minimum sets of either kind is
\[
(q-1)^{q^2+q+1}.
\]

## Assumptions and scope

The field has odd order \(q\). The bilinear form is the standard nondegenerate symmetric form
\[
B(x,y)=x_1y_1+x_2y_2+x_3y_3.
\]

The graph is the total dot-product graph in dimension three, with the zero vector deleted as in the original definition.

The notation \(\operatorname{P\Gamma O}(3,q)\) denotes the projective semilinear similarity group of this orthogonal form.

## Proof

For a projective point \(P=\langle x\rangle\), let
\[
C_P=P\setminus\{0\}.
\]
Every \(C_P\) has size \(q-1\).

If \(P\ne Q\), adjacency between \(C_P\) and \(C_Q\) is all-or-nothing, because
\[
B(ax,by)=ab\,B(x,y)
\]
for nonzero scalars \(a,b\).

Within \(C_P\), every pair is adjacent exactly when \(P\) is isotropic, meaning
\[
B(x,x)=0.
\]
Thus \(C_P\) is a clique for isotropic \(P\) and an independent set for anisotropic \(P\). In either case all its vertices have the same neighbors outside \(C_P\), so \(C_P\) is a twin class.

These twin classes are maximal. Indeed, two distinct projective points have distinct polar lines. For anisotropic points their open neighborhoods in the projective quotient are distinct polar lines; for isotropic points the polar line is recovered by adjoining the point itself to its open neighborhood. Hence two different projective points cannot produce the same twin neighborhood.

Let \(H_q\) be the quotient graph on the projective points. Distinct \(P,Q\) are adjacent in \(H_q\) exactly when
\[
P\subseteq Q^\perp.
\]
Thus \(H_q\) is the simple orthogonal polarity graph of \(\operatorname{PG}(2,q)\).

The isotropic points are graph-theoretically recognizable. A nondegenerate conic in \(\operatorname{PG}(2,q)\) has \(q+1\) points. An isotropic point has degree \(q\) in \(H_q\), whereas an anisotropic point has degree \(q+1\).

For each projective point \(P\), define
\[
L_P=
\begin{cases}
N_{H_q}(P)\cup\{P\},&P\text{ isotropic},\\
N_{H_q}(P),&P\text{ anisotropic}.
\end{cases}
\]
This is exactly the polar line \(P^\perp\).

Therefore every graph automorphism \(f\) of \(H_q\) sends polar lines to polar lines:
\[
f(L_P)=L_{f(P)}.
\]
Because polarity is a bijection between projective points and projective lines, \(f\) sends every projective line to a projective line. By the fundamental theorem of projective geometry, \(f\) is induced by a semilinear collineation.

The relation
\[
f(P^\perp)=f(P)^\perp
\]
says that this collineation preserves the orthogonality polarity up to a scalar multiplier and field automorphism. Hence
\[
\operatorname{Aut}(H_q)=\operatorname{P\Gamma O}(3,q).
\]

Conversely every projective semilinear orthogonal similitude preserves the quotient adjacency.

Since every fiber \(C_P\) has the same size and quotient automorphisms preserve whether \(P\) is isotropic, arbitrary permutations inside the fibers combine with the quotient action. Choosing fixed identifications of all fibers with a common \((q-1)\)-element set gives
\[
\operatorname{Aut}(G_q)
\cong
S_{q-1}^{\,v}\rtimes\operatorname{P\Gamma O}(3,q).
\]

For the determining number, suppose a determining set omits two vertices from some \(C_P\). Their transposition is a nonidentity graph automorphism fixing the determining set pointwise. Hence every determining set contains at least \(q-2\) vertices from every one of the \(v\) twin classes:
\[
\operatorname{Det}(G_q)\ge v(q-2).
\]

Now choose exactly \(q-2\) vertices from every \(C_P\). Since \(q\) is odd, \(q-2\ge1\). An automorphism fixing all chosen vertices pointwise must fix every twin class setwise, and then it must also fix the unique omitted vertex in each class. Thus it is the identity, so
\[
\operatorname{Det}(G_q)=v(q-2).
\]

The same twin obstruction gives
\[
\dim(G_q)\ge v(q-2).
\]

For the reverse inequality, take the same set \(S\) containing all but one vertex from every \(C_P\). The graph \(G_q\) has diameter two. Indeed, if two nonadjacent vectors span distinct lines, a nonzero vector orthogonal to their span is a common neighbor; if they are nonadjacent scalar multiples, any nonzero vector in their common orthogonal plane is a common neighbor.

Only the omitted vertices require comparison. Let \(x_P\) and \(x_Q\) be the omitted vertices from distinct classes. The quotient \(H_q\) has no pair of twins, because distinct polar lines cannot agree, nor can two distinct polar lines differ only by their two defining points. Hence some projective point \(R\) is adjacent to exactly one of \(P,Q\). Since \(S\) contains a vertex of \(C_R\), the distances from \(x_P\) and \(x_Q\) to that selected vertex are \(1\) and \(2\), respectively. Thus \(S\) resolves \(G_q\), proving
\[
\dim(G_q)=v(q-2).
\]

Equality in either twin lower bound forces exactly one omitted vertex from each class. Therefore the minimum determining sets and metric bases are exactly those described, and their number is
\[
(q-1)^v.
\]

## Verification

The accompanying `verify.py` was read from its actual packaged path before replay.

For \(q=3\) and \(q=5\), it constructs the projective quotient directly, verifies the degree split between isotropic and anisotropic points, and exhaustively enumerates all quotient automorphisms. It obtains respectively
\[
24=3(3^2-1)
\]
and
\[
120=5(5^2-1),
\]
the expected prime-field projective orthogonal orders.

It independently constructs the full vector graphs, finds exactly \(q^2+q+1\) maximal twin classes of size \(q-1\), checks diameter two, and verifies that a set omitting one vector from every class resolves all vertices. It also checks the closed cardinality identities for \(q=3,5,7,11\).

Exact replay output:

```text
p=3: quotient_vertices=13, quotient_aut=24, twin_classes=13, determining_metric=13, canonical_basis=OK
p=5: quotient_vertices=31, quotient_aut=120, twin_classes=31, determining_metric=93, canonical_basis=OK
symbolic count checks OK
VERIFY_OK
```

The finite computations corroborate the arbitrary-\(q\) projective proof; they are not used as a substitute for it.

## Relationship to prior work

Badawi introduced total and zero-divisor dot-product graphs of commutative rings and proved basic connectivity, diameter, and girth results. That source supplies the graph definition and the algebra-primary ownership of the topic.

Mollahajiaghaei later studied product structure, degrees, regularity, finite-field isomorphism rigidity, domination, clique and independence numbers, and planarity for total dot-product graphs. The accessible abstract does not state an automorphism-group, determining-number, or metric-dimension theorem.

Orthogonal polarity graphs of finite projective planes are classical objects in extremal graph theory. Their projective-geometric structure is used here as quotient background. The new claim concerns the full vector-level dot-product graph, its complete fiber symmetry, and the exact coincidence and classification of determining sets and metric bases.

## Limitations

Characteristic two is excluded. In that case the quadratic and bilinear geometry of absolute points changes and the degree argument used to recognize the orthogonal polarity requires separate treatment.

No claim is made for dimensions other than three. In higher dimension the quotient is a higher-rank projective orthogonality graph and its resolving behavior need not reduce to the same argument.

For nonprime odd \(q\), field automorphisms are included in \(\operatorname{P\Gamma O}(3,q)\); the finite exhaustive checks supplied here use the prime cases \(q=3\) and \(q=5\).

## References

1. A. Badawi, “On the Dot Product Graph of a Commutative Ring,” *Communications in Algebra* 43 (2015), 43–50. DOI: 10.1080/00927872.2014.897188. Published online 1 August 2014.
2. M. Mollahajiaghaei, “Properties of the Dot Product Graph of a Commutative Ring,” arXiv:1601.05034, first submitted 19 January 2016.
3. M. Tait and C. Timmons, “Orthogonal Polarity Graphs and Sidon Sets,” *Journal of Graph Theory* 82 (2016), 103–116. DOI: 10.1002/jgt.21890.
