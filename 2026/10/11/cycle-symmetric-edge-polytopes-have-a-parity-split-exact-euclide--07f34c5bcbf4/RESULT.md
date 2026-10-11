# Cycle symmetric edge polytopes have a parity-split exact Euclidean inradius
## Finding
Let
\[
n\ge3
\]
and let \(C_n\) be the cycle with vertex set
\[
\mathbb Z/n\mathbb Z.
\]
Its symmetric edge polytope is
\[
P_n
=
\operatorname{conv}
\left\{
\pm(e_i-e_{i+1}):
i\in\mathbb Z/n\mathbb Z
\right\}
\subset
H_0,
\tag{1}
\]
where
\[
H_0
=
\left\{
x\in\mathbb R^n:
\sum_i x_i=0
\right\}
\tag{2}
\]
has its inherited Euclidean metric.

The exact Euclidean inradius has a parity split.

If \(n\) is even, then
\[
\boxed{
r_{\mathrm{in}}(P_n)
=
\sqrt{\frac{48}{n(n^2+8)}}.
}
\tag{3}
\]
The polytope has
\[
\binom{n}{n/2}
\]
facets, and exactly
\[
\boxed{n}
\tag{4}
\]
of them are tangent to the origin-centered maximal insphere.

Writing
\[
n=2k,
\]
the complete incenter set has affine dimension
\[
\boxed{k-1=\frac n2-1.}
\tag{5}
\]
Its affine hull is
\[
\boxed{
\left\{
c\in H_0:
c_{i+k}=c_i
\text{ for every }i
\right\},
}
\tag{6}
\]
and the origin lies in its relative interior.

If \(n\) is odd, then
\[
\boxed{
r_{\mathrm{in}}(P_n)
=
\sqrt{
\frac{48n}{(n^2-1)(n^2+3)}
}.
}
\tag{7}
\]
The number of facets is
\[
n\binom{n-1}{(n-1)/2},
\tag{8}
\]
and exactly
\[
\boxed{2n}
\tag{9}
\]
facets are tangent to the maximal insphere. In this case
\[
\boxed{
0\text{ is the unique incenter.}
}
\tag{10}
\]

The tangent facets have a simple walk description. A facet labeling records increments around the cycle.

For
\[
n=2k,
\]
the tangent facets are precisely the cyclic rotations of
\[
(\underbrace{+1,\ldots,+1}_{k},
\underbrace{-1,\ldots,-1}_{k}).
\tag{11}
\]
Sign reversal is already a rotation by \(k\), so there are \(n\) such facets.

For
\[
n=2k+1,
\]
the tangent facets are precisely the cyclic rotations of
\[
(\underbrace{+1,\ldots,+1}_{k},
0,
\underbrace{-1,\ldots,-1}_{k})
\tag{12}
\]
and their negatives.

Equivalently, if \(f\) is a facet labeling and
\[
g_f=f-\bar f\mathbf1
\]
is its centered intrinsic normal, then
\[
\boxed{
\max_f\|g_f\|^2
=
\begin{cases}
\dfrac{n(n^2+8)}{48},&n\text{ even},\\[6pt]
\dfrac{(n^2-1)(n^2+3)}{48n},&n\text{ odd}.
\end{cases}
}
\tag{13}
\]

Both radii satisfy
\[
r_{\mathrm{in}}(P_n)
\sim
4\sqrt3\,n^{-3/2}.
\tag{14}
\]

## Assumptions and scope
The realization is exactly the standard symmetric edge polytope, also called the PV-type adjacency polytope, of the unweighted cycle.

The metric is intrinsic to the \((n-1)\)-dimensional space \(H_0\). This matters because facet labelings are only defined up to an additive constant; subtracting the mean produces the unique normal in \(H_0\).

For unit edge weights, the same polytope is the Kantorovich--Rubinstein polytope of the graph metric on \(C_n\). The theorem therefore applies to that canonical unweighted-cycle realization, not to arbitrary weighted-cycle KR polytopes or to affinely equivalent cyclohedral realizations.

The result concerns Euclidean inballs and incenter structure. It does not determine the minimum enclosing ball, John ellipsoid, Ehrhart polynomial, or normalized volume.

## Proof
The published facet theorem for a connected symmetric edge polytope says that an integer labeling
\[
f:\mathbb Z/n\mathbb Z\to\mathbb Z
\]
defines a facet exactly when
\[
|f(i+1)-f(i)|\le1
\tag{15}
\]
for every cycle edge and the edges on which equality holds form a spanning connected subgraph.

After fixing one vertex value, the labeling is unique. Let
\[
\bar f=\frac1n\sum_i f(i)
\]
and
\[
g_f=f-\bar f\mathbf1.
\tag{16}
\]
On \(H_0\), \(f\) and \(g_f\) define the same functional. Since the vertices of \(P_n\) are
\[
\pm(e_i-e_{i+1}),
\]
condition (15) implies
\[
\langle g_f,x\rangle\le1
\tag{17}
\]
on \(P_n\), and the facet itself is the equality hyperplane. Thus its intrinsic distance from the origin is
\[
\frac1{\|g_f\|}.
\tag{18}
\]

Because \(P_n\) is centrally symmetric, an arbitrary inscribed ball can always be recentered at the origin without shrinking it: if
\[
B(c,\rho)\subset P_n,
\]
then also
\[
B(-c,\rho)\subset P_n,
\]
and convexity gives
\[
B(0,\rho)
=
\frac12B(c,\rho)+\frac12B(-c,\rho)
\subset P_n.
\]
Therefore
\[
r_{\mathrm{in}}(P_n)
=
\frac1{\max_f\|g_f\|}.
\tag{19}
\]

We now determine the largest centered-normal norm.

Write the cyclic increments as
\[
s_i=f(i+1)-f(i).
\tag{20}
\]

If
\[
n=2k,
\]
the cycle is bipartite. The source proves that every edge of a facet labeling is active, so
\[
s_i\in\{-1,+1\}.
\]
Closure around the cycle gives exactly \(k\) positive and \(k\) negative steps. This also recovers the published facet count
\[
\binom{2k}{k}.
\tag{21}
\]

If
\[
n=2k+1,
\]
a spanning connected active-edge subgraph of a cycle has at least \(n-1\) edges. All \(n\) edges cannot be active, because an odd number of \(\pm1\) increments cannot sum to zero. Hence exactly one increment is zero and all remaining \(2k\) increments are \(\pm1\), with \(k\) signs of each kind. Consequently the number of facets is
\[
(2k+1)\binom{2k}{k}.
\tag{22}
\]

It remains to maximize the variance of the cyclic walk values, because
\[
\|g_f\|^2
=
\sum_i(f(i)-\bar f)^2.
\tag{23}
\]

We use the identity
\[
\sum_i(x_i-\bar x)^2
=
\frac1n
\sum_{i<j}(x_i-x_j)^2.
\tag{24}
\]
Shift a walk so that its minimum is \(0\), and let its range be \(h\). A closed nearest-neighbor walk that reaches both \(0\) and \(h\) visits each endpoint at least once and every intermediate integer level
\[
1,\ldots,h-1
\]
at least twice. Thus every value multiset contains the mandatory symmetric multiset
\[
\{0,h\}\cup
\{1,1,2,2,\ldots,h-1,h-1\}.
\tag{25}
\]

Any remaining visits lie in the interval \([0,h]\). In the pairwise expression (24), with all other entries fixed, the contribution of one extra value is a convex quadratic in that value. Moving it to one endpoint therefore cannot decrease the variance. Repeating this operation moves every extra visit to \(0\) or \(h\).

The mandatory multiset (25) is symmetric about \(h/2\), so an extra visit has the same interaction with it at either endpoint. The only split-dependent term is the pairwise energy among the extra endpoint visits, which is maximized by dividing them as evenly as possible.

For \(n=2k\), there are
\[
2(k-h)
\]
extra visits. The resulting sharp upper profile is
\[
V_{\mathrm e}(h)
=
\frac{
h(3hk+2-2h^2)
}{6}.
\tag{26}
\]
Its increment is
\[
V_{\mathrm e}(h+1)-V_{\mathrm e}(h)
=
\frac{
2h(k-h-1)+k
}{2}
>0
\tag{27}
\]
for
\[
1\le h<k.
\]
Therefore the maximum occurs only at
\[
h=k.
\]
At that range there are no extra visits, and the only possible walk, up to cyclic rotation, is one monotone climb followed by one monotone descent. Hence (11), and
\[
\max_f\|g_f\|^2
=
V_{\mathrm e}(k)
=
\frac{k(k^2+2)}6
=
\frac{n(n^2+8)}{48}.
\tag{28}
\]
This proves (3)--(4).

For \(n=2k+1\), there are
\[
2(k-h)+1
\]
extra visits. The balanced endpoint split gives
\[
V_{\mathrm o}(h)
=
\frac{
h\left(
3hk(k+1)+(2k+1)(1-h^2)
\right)
}{
3(2k+1)
}.
\tag{29}
\]
Now
\[
V_{\mathrm o}(h+1)-V_{\mathrm o}(h)
=
\frac{
(k-h)(2hk+h+k+1)
}{
2k+1
}
>0
\tag{30}
\]
for
\[
1\le h<k.
\]
Thus the unique maximal range is again
\[
h=k.
\]
There is exactly one extra visit, so it must duplicate one endpoint. The zero step is therefore at the minimum or maximum, while the nonzero steps form one monotone rise and one monotone fall. This gives (12), and
\[
\max_f\|g_f\|^2
=
V_{\mathrm o}(k)
=
\frac{
k(k+1)(k^2+k+1)
}{
3(2k+1)
}
=
\frac{
(n^2-1)(n^2+3)
}{
48n
}.
\tag{31}
\]
Equations (19) and (31) prove (7)--(9).

We finish with the incenter statements.

For odd \(n=2k+1\), take one tangent normal \(g\) from (12) and all its cyclic rotations. The cyclic difference of \(g\) has step pattern
\[
(+1,\ldots,+1,0,-1,\ldots,-1).
\]
At a nontrivial \(n\)-th root of unity \(z\), its Fourier coefficient is proportional to
\[
\frac{
(1-z^k)(1-z^{k+1})
}{
1-z
}.
\tag{32}
\]
Because
\[
\gcd(k,2k+1)=
\gcd(k+1,2k+1)=1,
\]
this is never zero. Hence the cyclic rotations of \(g\) span all of \(H_0\).

If \(c\) were any other center of an inball of the optimal radius, applying the inequalities for a tangent facet and its opposite gives
\[
\langle g,c\rangle=0
\]
for every tangent normal. Their span is \(H_0\), so
\[
c=0.
\]
This proves (10).

For even \(n=2k\), a tangent normal from (11) satisfies
\[
g_{i+k}=-g_i.
\tag{33}
\]
Its cyclic rotations span the \(k\)-dimensional anti-periodic subspace
\[
\{g:g_{i+k}=-g_i\}.
\tag{34}
\]
For example, the cyclic difference has \(k\) consecutive \(+1\) entries followed by \(k\) consecutive \(-1\) entries, whose nonzero Fourier coefficients are exactly the odd cyclic frequencies.

Any optimal center must be orthogonal to every tangent normal, because each tangent facet and its opposite already use the entire radius. The common orthogonal complement in \(H_0\) is exactly
\[
K
=
\left\{
c\in H_0:
c_{i+k}=c_i
\right\},
\tag{35}
\]
which has dimension \(k-1\).

Every non-tangent facet has strict slack at the origin. Since there are finitely many facets, a sufficiently small relative neighborhood of \(0\) inside \(K\) preserves all those strict inequalities, while (35) preserves equality in every tangent pair. Hence that neighborhood consists of incenters. The complete incenter set therefore has affine hull \(K\) and dimension \(k-1\), proving (5)--(6).

Finally, the asymptotic statement (14) follows directly from (3) and (7).

## Verification
The proof above is exact for every
\[
n\ge3.
\]

The source-dependent facet theorem was checked in the open-access full text. The same paper explicitly derives the even-cycle facet walks by choosing exactly half of the cycle edges as increases and the other half as decreases.

A second full paper on facets and facet subgraphs was inspected because it provides a broader graph-theoretic description of the same facets in terms of maximal bipartite subgraphs and cycle-balance conditions. It contains no Euclidean radius result.

A third highly relevant full paper on Kantorovich--Rubinstein polytopes of weighted cycles was inspected. Its graph-metric lemma shows that for unit cycle weights the KR polytope is exactly (1), and its weighted-cycle results study boundary combinatorics through Bier spheres. Targeted full-text checks found no inradius, radius, or Euclidean metric theorem.

The accompanying `verify.py` independently enumerates every facet-label step pattern for
\[
3\le n\le14.
\]
Using exact rational arithmetic, it checks the complete facet counts, the maximum centered-normal norm in (13), the exact tangent-facet counts, and the rank of the tangent-normal system. In the even cases it also checks a basis of the periodic incenter affine hull. The finite replay is corroborative only; the all-\(n\) result follows from the proof.

## Relationship to prior work
D'Alì, Delucchi, and Michałek develop symmetric edge polytopes as a common object connecting graph polytopes, Kuramoto adjacency polytopes, and Kantorovich--Rubinstein polytopes. Their facet-label theorem and their explicit even-cycle facet count are the main structural inputs here. Their work focuses on face numbers, triangulations, Ehrhart data, volume, graph joins, and related combinatorics rather than Euclidean inballs.

Jevtić, Timotijević, and Živaljević study the same unweighted-cycle KR polytope as a special case of weighted cycles. Their results identify its boundary sphere combinatorially through short-set Bier spheres. This does not determine the Euclidean lengths of the facet normals or which facets support a largest Euclidean ball.

Chen, Davis, and Korchevskaia give a broader facet-subgraph theory for adjacency polytopes, including cycle-balance constraints, but again do not state an inradius theorem.

There are existing Euclidean inradius formulas for other symmetric edge-polytope graph families, including complete multipartite graphs and wheel graphs. They do not imply the cycle formulas: except for the isolated identity
\[
C_4=K_{2,2},
\]
a cycle is neither a complete multipartite graph nor a wheel, and deleting the hub of a wheel does not preserve an inradius. The case \(n=4\) is therefore a consistency check rather than a new special case.

Likewise, results on the numerical index of Lipschitz-free spaces over cycles concern a different Banach-space invariant of the same underlying finite metric and do not determine the Euclidean inball in the standard root-coordinate realization.

Targeted searches under symmetric-edge, adjacency-polytope, Kantorovich--Rubinstein, Lipschitz-free, cycle, inradius, insphere, tangent-facet, and Chebyshev-center terminology did not locate a statement implying (3)--(13).

## Limitations
The theorem concerns unweighted cycles in the standard root-coordinate realization. Weighted-cycle KR polytopes rescale the root vertices and generally have different Euclidean geometry.

The even case determines the affine hull and dimension of the complete incenter set but does not give a closed inequality-minimal description of that incenter polytope inside its affine hull.

The proof uses a one-dimensional variance extremum specific to cyclic facet walks. It does not by itself extend to arbitrary graph symmetric edge polytopes.

Older optimal-transport and adjacency-polytope literature uses several names for this object, so a differently indexed equivalent Euclidean statement remains a residual bibliographic risk despite the targeted comparisons.

## References
1. Filip D. Jevtić, Marinko Timotijević, and Rade T. Živaljević, *Polytopal Bier spheres and Kantorovich--Rubinstein polytopes of weighted cycles*, arXiv:1812.00397, first public version 2018-12-02, DOI 10.1007/s00454-019-00151-5.
2. Alessio D'Alì, Emanuele Delucchi, and Mateusz Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, first public version 2019-10-11.
3. Tianran Chen, Robert Davis, and Evgeniia Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, first public version 2021-07-26.
