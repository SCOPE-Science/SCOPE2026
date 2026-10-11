# The standard cyclohedron has a unique barycentric incenter
## Finding
For \(n\ge3\), let \(C_n\) be the cycle graph on \([n]\). Let \(\mathcal B(C_n)\) be its set of nonempty connected vertex subsets, called tubes, and define the standard simplex-sum graph associahedron
\[
\mathcal W_n
=
\sum_{T\in\mathcal B(C_n)}\Delta_T,
\qquad
\Delta_T=\operatorname{conv}\{e_i:i\in T\}.
\]
This is the standard nestohedral realization of the cyclohedron.

It lies in the affine hyperplane
\[
H_n=
\left\{
x\in\mathbb R^n:
x([n])=n(n-1)+1
\right\}.
\]
With the intrinsic Euclidean metric of \(H_n\),
\[
\boxed{
r_{\mathrm{in}}(\mathcal W_n)
=
\frac{(n-1)^{3/2}}{\sqrt n}.
}
\tag{1}
\]

The incenter is unique and equals
\[
\boxed{
b_n=
\left(n-1+\frac1n\right)\mathbf1.
}
\tag{2}
\]
By cyclic symmetry, this point is also the vertex barycenter of \(\mathcal W_n\).

The centered maximal ball is tangent exactly to the \(n\) facets indexed by singleton tubes.

More explicitly, a proper tube \(S\) is a cyclic interval. If \(|S|=k\), then the intrinsic distance from \(b_n\) to its facet is
\[
\boxed{
d_{n,k}
=
\frac{
k\left(n-1+\frac1n\right)-\frac{k(k+1)}2
}{
\sqrt{\frac{k(n-k)}n}
}.
}
\tag{3}
\]
One has
\[
d_{n,1}
=
\frac{(n-1)^{3/2}}{\sqrt n}
\]
and
\[
d_{n,k}>d_{n,1}
\qquad
(2\le k<n).
\tag{4}
\]

## Assumptions and scope
The realization is fixed: \(\mathcal W_n\) is the Minkowski sum with coefficient \(1\) of the simplex faces indexed by all tubes of the cycle. Different affine realizations of the cyclohedron can have different Euclidean radii.

The cycle has \(n\ge3\) vertices. Distances are intrinsic to the codimension-one affine hull \(H_n\).

## Proof
The graph-associahedron literature gives the simplex-sum realization
\[
\operatorname{Asso}(G)
=
\sum_{T\in\mathcal B(G)}\Delta_T
\]
for every graph \(G\), and identifies cycle graph associahedra with cyclohedra.

For \(C_n\), there are exactly \(n\) tubes of each cardinality
\[
1,2,\ldots,n-1
\]
and one full tube \([n]\). Hence
\[
|\mathcal B(C_n)|=n(n-1)+1,
\]
which gives the affine equation of \(H_n\).

For any subset \(S\subseteq[n]\), the minimum of \(x(S)\) on a simplex \(\Delta_T\) is \(1\) if \(T\subseteq S\) and \(0\) otherwise. Therefore the simplex sum satisfies
\[
x(S)\ge
|\{T\in\mathcal B(C_n):T\subseteq S\}|.
\]
When \(S\) is a proper tube of cardinality \(k\), the induced graph on \(S\) is a path on \(k\) vertices. Its nonempty connected subsets are its intervals, so their number is
\[
\frac{k(k+1)}2.
\]
Thus the facet indexed by \(S\) has equation
\[
x(S)=\frac{k(k+1)}2.
\tag{5}
\]

The cycle acts transitively on coordinates and preserves \(\mathcal W_n\). Therefore its vertex barycenter is fixed by cyclic coordinate permutation, hence is scalar. The affine equation forces that barycenter to be \(b_n\) in (2).

Inside the tangent space \(\mathbf1^\perp\), the intrinsic normal to (5) is
\[
\nu_S=
\mathbf1_S-\frac{k}{n}\mathbf1,
\]
with
\[
\|\nu_S\|^2
=
\frac{k(n-k)}n.
\tag{6}
\]
At \(b_n\), the slack of (5) is
\[
k\left(n-1+\frac1n\right)-\frac{k(k+1)}2,
\]
which proves (3).

For \(k=1\), the slack is
\[
\frac{(n-1)^2}{n},
\]
so (6) gives
\[
d_{n,1}
=
\frac{(n-1)^{3/2}}{\sqrt n}.
\]

It remains to prove that no larger tube gives a closer facet. Put
\[
j=n-k.
\]
A direct simplification gives
\[
d_{n,k}^2-d_{n,1}^2
=
\frac{k-1}{4(n-k)}
\left[
nj^2+(2n^2-7n+4)j+(n-2)^2(n-1)
\right].
\tag{7}
\]
For \(n\ge3\) and \(1\le j\le n-1\), every term in the bracket is nonnegative and the first and last are positive; moreover
\[
2n^2-7n+4\ge1.
\]
Hence (7) is strictly positive for every \(k>1\). Thus the ball centered at \(b_n\) of radius (1) lies in every facet halfspace and touches exactly the singleton-tube facets.

Finally, let \(B_{H_n}(c,r)\subseteq\mathcal W_n\). The singleton facets are
\[
x_i\ge1.
\]
Their intrinsic normal length is
\[
\sqrt{\frac{n-1}{n}},
\]
so
\[
c_i-1
\ge
r\sqrt{\frac{n-1}{n}}
\qquad
(i\in[n]).
\]
Summing and using \(c([n])=n(n-1)+1\) yields
\[
(n-1)^2
\ge
nr\sqrt{\frac{n-1}{n}},
\]
and therefore
\[
r\le\frac{(n-1)^{3/2}}{\sqrt n}.
\]
Equality forces equality in every singleton constraint, hence forces
\[
c=b_n.
\]
This proves both optimality and uniqueness.

## Verification
The proof is symbolic for every \(n\ge3\). The accompanying `verify.py` uses exact rational arithmetic to check, for \(3\le n\le200\), the squared distance formula, the strict singleton-facet minimum, the affine total, and the equality case in the singleton upper bound.

The finite replay is corroborative only. Equation (7) is the all-dimensional proof that singleton tubes are the unique tangent-facet cardinality.

## Relationship to prior work
Padrol, Pilaud, and Poullot describe graph associahedra and nestohedra, identify cycle graph associahedra with cyclohedra, and explicitly record the realization as a Minkowski sum of simplex faces indexed by tubes. Their work studies nested fans and deformation cones. Its full text contains no occurrence of “inradius,” “Chebyshev,” “inscribed ball,” or “Euclidean.”

Hohlweg and Lange study many explicit realizations of associahedra and cyclohedra and emphasize that cyclohedra admit substantially different realizations. Their inspected full text contains no occurrence of “inradius,” “insphere,” “Chebyshev,” or “radius.” Their realizations are not assumed to have the metric value in (1); the claim here is specifically for the standard simplex-sum graph-associahedron realization.

Targeted searches for cyclohedron inradius, cyclohedron Chebyshev center, largest inscribed ball, graph-associahedron inradius, and the characteristic radical in (1) did not locate a covering statement.

## Limitations
The result is realization-dependent. It does not assert the same inradius for the type-\(B\) Cambrian realizations, secondary realizations, or arbitrary deformations of the cyclohedron.

No circumradius, John ellipsoid, or non-Euclidean radius is claimed.

An equivalent metric observation may exist under older graph-associahedron or generalized-permutahedron terminology. The literature comparison therefore retains a residual bibliographic risk rather than treating search nonappearance as a novelty certificate.

## References
1. Arnau Padrol, Vincent Pilaud, and Germain Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200, first public version 2021-09-19; European Journal of Combinatorics 107 (2023), 103594, DOI 10.1016/j.ejc.2022.103594.
2. Christophe Hohlweg and Carsten Lange, *Realizations of the associahedron and cyclohedron*, arXiv:math/0510614; Discrete & Computational Geometry 37 (2007), 517--543, DOI 10.1007/s00454-007-1319-6.
