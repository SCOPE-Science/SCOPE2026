# The bipermutahedron has a unique origin inball supported by only \(2n\) facets
## Finding
Let
\[
M_n
=
\left\{
x\in\mathbb R^n:
\sum_{i=1}^n x_i=0
\right\},
\]
and let
\[
\Pi_{n,n}\subset M_n\times M_n
\]
be the bipermutahedron in Ardila's standard coordinate realization.

For every
\[
n\ge3,
\]
the origin is the unique Euclidean incenter, and
\[
\boxed{
r_{\mathrm{in}}(\Pi_{n,n})
=
(2n-1)\sqrt{\frac{n}{n-1}}.
}
\tag{1}
\]

The source proves that \(\Pi_{n,n}\) has
\[
3^n-3
\]
facets. Nevertheless, its insphere touches exactly
\[
\boxed{2n}
\tag{2}
\]
of them, namely the facets indexed by
\[
[n]\mid\{j\}
\quad\text{and}\quad
\{j\}\mid[n],
\qquad
1\le j\le n.
\tag{3}
\]
Every other facet is strictly farther from the origin.

The case
\[
n=2
\]
is exceptional. Then
\[
\boxed{
r_{\mathrm{in}}(\Pi_{2,2})=4,
}
\tag{4}
\]
and the complete incenter set is
\[
\boxed{
\left\{
\bigl((t,-t),(t,-t)\bigr):
|t|\le3-2\sqrt2
\right\}.
}
\tag{5}
\]

## Assumptions and scope
The metric is the Euclidean metric inherited from
\[
\mathbb R^n\times\mathbb R^n.
\]

A bisubset
\[
S\mid T
\]
means a pair of nonempty subsets of \([n]\), not both equal to \([n]\), with
\[
S\cup T=[n].
\]

The source's minimal inequality description is
\[
\sum_{i\in S}x_i+\sum_{j\in T}y_j
\ge
-\bigl(|S|+|S-T|\bigr)\bigl(|T|+|T-S|\bigr),
\tag{6}
\]
together with
\[
\sum_i x_i=0,
\qquad
\sum_i y_i=0.
\tag{7}
\]

The inradius in (1) is intrinsic to the affine span \(M_n\times M_n\). No affine or unimodular invariance is asserted.

## Proof
Fix a facet indexed by a bisubset
\[
S\mid T.
\]
Put
\[
u=n-|S|,
\qquad
v=n-|T|.
\tag{8}
\]
Since
\[
S\cup T=[n],
\]
the complements
\[
[n]-S
\quad\text{and}\quad
[n]-T
\]
are disjoint. Hence
\[
u,v\ge0,
\qquad
u+v\le n.
\tag{9}
\]
Because \(S,T\) are nonempty and not both equal to \([n]\),
\[
u,v\le n-1,
\qquad
(u,v)\ne(0,0).
\tag{10}
\]

The two asymmetric differences have sizes
\[
|T-S|=u,
\qquad
|S-T|=v.
\]
Therefore the positive slack of the origin in (6) is
\[
\begin{aligned}
\sigma(u,v)
&=
\bigl(n-u+v\bigr)\bigl(n-v+u\bigr)\\
&=
n^2-(u-v)^2.
\end{aligned}
\tag{11}
\]

The ambient normal of (6) is
\[
(\mathbf1_S,\mathbf1_T).
\]
Its orthogonal projection to
\[
M_n\times M_n
\]
has squared norm
\[
\begin{aligned}
A(u,v)/n
&=
\frac{|S|(n-|S|)+|T|(n-|T|)}{n}\\
&=
\frac{u(n-u)+v(n-v)}{n}.
\end{aligned}
\tag{12}
\]
Thus the intrinsic distance from the origin to this facet is
\[
D(u,v)
=
\frac{n^2-(u-v)^2}
{\sqrt{\bigl(u(n-u)+v(n-v)\bigr)/n}}.
\tag{13}
\]

We now minimize (13).

Write
\[
q=|u-v|
\]
and
\[
s=u+v.
\]
Then
\[
u^2+v^2=\frac{s^2+q^2}{2},
\]
so
\[
A(u,v)
=
ns-\frac{s^2+q^2}{2}.
\tag{14}
\]
Since
\[
s\le n,
\]
the right side is at most
\[
\frac{n^2-q^2}{2}.
\tag{15}
\]

If
\[
q\le n-2,
\]
then (13)--(15) give
\[
D(u,v)^2
=
\frac{n\bigl(n^2-q^2\bigr)^2}{A(u,v)}
\ge
2n\bigl(n^2-q^2\bigr)
\ge
8n(n-1).
\tag{16}
\]
For
\[
n\ge3,
\]
\[
8(n-1)^2>(2n-1)^2,
\tag{17}
\]
so
\[
D(u,v)^2
>
\frac{n(2n-1)^2}{n-1}.
\tag{18}
\]

The only remaining possibility is
\[
q=n-1.
\]
Under (9)--(10), this forces
\[
(u,v)=(n-1,0)
\quad\text{or}\quad
(0,n-1).
\tag{19}
\]
For either pair,
\[
A(u,v)=n-1
\]
and
\[
\sigma(u,v)=2n-1.
\]
Hence
\[
D(u,v)
=
(2n-1)\sqrt{\frac{n}{n-1}}.
\tag{20}
\]
These two count types are exactly the facet families in (3).

It remains to show that the minimum distance from the origin is the global inradius rather than merely the largest origin-centered radius.

For any fixed radius \(\rho\), the set of all centers whose radius-\(\rho\) ball lies in \(\Pi_{n,n}\) is a convex intersection of inward-shifted facet halfspaces. It is invariant under simultaneous permutation of the \(n\) labels. Averaging any feasible center over that permutation group produces the origin, because both coordinate blocks lie in \(M_n\). Therefore, if any radius \(\rho\) is feasible, then the same radius is feasible at the origin.

Consequently the inradius is exactly the minimum origin-to-facet distance, which is (20).

For uniqueness when \(n\ge3\), suppose
\[
(x,y)\in M_n\times M_n
\]
is the center of an inscribed ball of radius (1). For the tangent facet
\[
[n]\mid\{j\},
\]
the original inequality is
\[
y_j\ge-(2n-1).
\]
Shifting inward by the inradius moves this supporting hyperplane exactly to
\[
y_j\ge0.
\]
Thus every incenter satisfies
\[
y_j\ge0
\qquad
(1\le j\le n).
\]
Since
\[
\sum_j y_j=0,
\]
we get
\[
y=0.
\]
The facets
\[
\{j\}\mid[n]
\]
similarly force
\[
x=0.
\]
This proves uniqueness and the exact tangency statement.

For
\[
n=2,
\]
write
\[
x=(a,-a),
\qquad
y=(b,-b).
\]
The six source facets reduce to
\[
|a|\le3,
\qquad
|b|\le3,
\qquad
|a-b|\le4.
\tag{21}
\]
In the inherited metric,
\[
\|(a,-a,b,-b)\|^2=2a^2+2b^2.
\]
The two diagonal facets
\[
a-b=\pm4
\]
are at intrinsic distance \(4\) from the origin, while the four coordinate facets are at distance \(3\sqrt2\). Hence the inradius is \(4\).

A center supports radius \(4\) exactly when its clearance from both diagonal facets is at least \(4\), forcing
\[
a=b,
\]
and its clearance from the four coordinate facets is at least \(4\), giving
\[
|a|=|b|
\le
3-2\sqrt2.
\]
This proves (4)--(5).

## Verification
The proof is symbolic for every \(n\ge2\).

The source-dependent inputs were checked directly in the full primary text: the definition of bisubsets, the statement that they index all \(3^n-3\) facets, and Proposition 2.8 giving the minimal inequality description (6)--(7). The publication metadata lists \(52B20\) as its primary Mathematics Subject Classification.

The accompanying `verify.py` exhaustively enumerates all bisubsets for
\[
2\le n\le8.
\]
It verifies the facet count \(3^n-3\), computes every intrinsic origin-to-facet squared distance exactly as a rational number, checks the formula (1), and confirms that for every \(n\ge3\) exactly \(2n\) facets attain the minimum. It also verifies the exceptional \(n=2\) metric inequalities and incenter segment.

Finite enumeration is corroborative only; the proof above establishes the theorem for arbitrary \(n\).

## Relationship to prior work
Ardila's paper determines the bipermutahedron's face structure, \(f\)- and \(h\)-theory, unimodular triangulations, deformation cone, symmetry, and its relation to the harmonic polytope. Its minimal facet description is the critical source input for the present metric calculation.

The inspected primary full text contains no occurrence of “inradius”, “circumradius”, “Euclidean”, or “sphere” in this metric context. Targeted searches under “bipermutahedron”, “inradius”, “insphere”, “Chebyshev center”, and “largest inscribed ball” did not locate a theorem implying (1)--(5).

The result is not determined by the known combinatorial symmetry alone: the facet offsets in (6) vary with
\[
|S-T|
\quad\text{and}\quad
|T-S|.
\]
The metric theorem identifies a sharp collapse among the exponentially many facets: for \(n\ge3\), only the \(2n\) most unbalanced bisubsets in (3) support the maximal ball.

## Limitations
The theorem concerns Ardila's standard Euclidean realization.

It determines the Euclidean inradius and incenter set, not the minimum enclosing sphere, John or Löwner ellipsoid, graph diameter, or lattice invariants.

The proof uses the exact source facet offsets. A different deformation of the bipermutahedral fan can have a different inradius.

A general theorem about Chebyshev centers of highly symmetric deformed permutahedra could imply the same result under different terminology; no such covering statement was located in the targeted comparisons.

## References
1. Federico Ardila, *The bipermutahedron*, arXiv:2008.02295, first public version 2020-08-05; *Combinatorial Theory* 2(3) (2022), Article 1, DOI 10.5070/C62359149.
