# The Hochschild-lattice polytope has the exact permutahedral inradius
## Finding
For \(n\ge2\), let
\[
\mathrm{Hoch}(1,n)\subset\mathbb R^{n+1}
\]
be the Pilaud--Poliakova deformed-permutahedron realization of the Hochschild lattice. Put
\[
N=n+1.
\]
The source realization lies in
\[
H_N=
\left\{
x\in\mathbb R^N:
\sum_{i=1}^{N}x_i=\binom{N+1}{2}
\right\}.
\]
Equip \(H_N\) with its intrinsic Euclidean metric.

Then
\[
\boxed{
r_{\mathrm{in}}\!\left(\mathrm{Hoch}(1,n)\right)
=
\frac{\sqrt{N(N-1)}}2
=
\frac{\sqrt{n(n+1)}}2.
}
\tag{1}
\]
This is exactly the inradius of the standard permutahedron in the same affine hyperplane.

The incenter is unique and equals
\[
\boxed{
c_*=\frac{N+1}{2}\mathbf1
=
\frac{n+2}{2}\mathbf1.
}
\tag{2}
\]

Thus the Hochschild-lattice deformation preserves the standard permutahedron's Euclidean inradius and unique uniform Chebyshev center, even though its facet system and combinatorics are substantially different.

## Assumptions and scope
The polytope is the specific \((1,n)\)-Hochschild polytope introduced by Pilaud and Poliakova, not an arbitrary polytope having the Hochschild lattice as an oriented skeleton. The source proves that this \((1,n)\)-polytope is a deformed permutahedron.

The metric is the intrinsic Euclidean metric of \(H_N\). The result is realization-dependent and is not invariant under arbitrary affine transformations.

For a nonempty subset \(J\subseteq[N]\), write
\[
x(J)=\sum_{j\in J}x_j
\]
and let
\[
z_J=
\min\{x(J):x\in\mathrm{Hoch}(1,n)\}
\]
be the source's tight right-hand side.

## Proof
The source's general deformed-permutahedron framework places all of its polytopes in
\[
H_N:
\sum_i x_i=\binom{N+1}{2}
\tag{3}
\]
and parametrizes them by tight subset-sum right-hand sides \(z_J\).

For \(\mathrm{Hoch}(1,n)\), specialize the source's explicit \(z\)-parametrization to \(m=1\). For each nonempty proper
\[
J\subsetneq[N],
\]
let
\[
a=|J\cap\{1\}|\in\{0,1\}.
\]
Among the elements of
\[
J\cap\{2,\ldots,N\},
\]
let \(C\) be the largest final interval ending at \(N\) that is contained in \(J\), and let \(c=|C|\). Let \(B\) be the remaining elements and put \(b=|B|\). Then
\[
k=|J|=a+b+c
\]
and the source formula becomes
\[
z_J
=
\binom{a+c+1}{2}+b.
\tag{4}
\]
Set
\[
t=a+c.
\]
Since \(b=k-t\), equation (4) rewrites as
\[
z_J
=
k+\frac{t(t-1)}2.
\tag{5}
\]
Because
\[
0\le t\le k,
\]
one has
\[
t(t-1)\le k(k-1),
\]
and therefore
\[
\boxed{
z_J\le\binom{k+1}{2}.
}
\tag{6}
\]

Now consider the uniform point
\[
c_*=\mu\mathbf1,
\qquad
\mu=\frac{N+1}{2}.
\]
Its slack in the valid inequality
\[
x(J)\ge z_J
\]
is, by (6),
\[
k\mu-z_J
\ge
\frac{k(N+1)}2-\binom{k+1}{2}
=
\frac{k(N-k)}2.
\tag{7}
\]

Inside the tangent space
\[
\mathbf1^\perp,
\]
the intrinsic normal to the hyperplane
\[
x(J)=z_J
\]
is
\[
\nu_J=
\mathbf1_J-\frac{k}{N}\mathbf1.
\]
Its squared norm is
\[
\|\nu_J\|^2
=
k-\frac{k^2}{N}
=
\frac{k(N-k)}{N}.
\tag{8}
\]
Hence the intrinsic distance from \(c_*\) to that hyperplane is at least
\[
\frac{k(N-k)/2}
{\sqrt{k(N-k)/N}}
=
\frac12\sqrt{Nk(N-k)}.
\tag{9}
\]
For
\[
1\le k\le N-1,
\]
\[
k(N-k)\ge N-1,
\]
so every defining facet hyperplane is at distance at least
\[
r_*=
\frac12\sqrt{N(N-1)}.
\tag{10}
\]
Thus
\[
B_{H_N}(c_*,r_*)
\subseteq
\mathrm{Hoch}(1,n).
\tag{11}
\]

It remains to prove that no larger intrinsic Euclidean ball fits and that \(c_*\) is the only optimal center.

For every singleton
\[
J=\{i\},
\]
formula (4) gives
\[
z_{\{i\}}=1.
\]
Therefore every point of the polytope satisfies
\[
x_i\ge1.
\tag{12}
\]
The intrinsic normal of the hyperplane
\[
x_i=1
\]
has norm
\[
\sqrt{\frac{N-1}{N}}.
\tag{13}
\]
If an intrinsic ball of radius \(r\), centered at \(c\in H_N\), is contained in the polytope, then (12)--(13) give
\[
c_i-1
\ge
r\sqrt{\frac{N-1}{N}}
\qquad
(1\le i\le N).
\tag{14}
\]
Summing (14) and using (3),
\[
\binom{N+1}{2}-N
\ge
Nr\sqrt{\frac{N-1}{N}}.
\]
The left side is
\[
\frac{N(N-1)}2,
\]
hence
\[
r
\le
\frac{\sqrt{N(N-1)}}2
=
r_*.
\tag{15}
\]
Together with (11), this proves (1).

If equality holds in (15), equality must hold in every inequality (14). Consequently
\[
c_i
=
1+r_*\sqrt{\frac{N-1}{N}}
=
1+\frac{N-1}{2}
=
\frac{N+1}{2}
\]
for every \(i\). Hence
\[
c=c_*,
\]
proving uniqueness.

## Verification
The proof is arbitrary-dimensional and symbolic. The crucial source-dependent inputs are the common affine hyperplane, the deformed-permutahedron tight-right-hand-side parametrization, and the explicit \(z_J\) formula for the Hochschild polytope.

The accompanying `verify.py` does not attempt to prove the source formula. Instead, it independently checks the complete algebraic reduction that follows from it. For dimensions up to \(200\), it enumerates all abstract triples
\[
(a,b,c)
\]
allowed by the specialization \(m=1\), verifies
\[
z_J\le\binom{|J|+1}{2},
\]
and verifies exactly, using rational arithmetic, that every resulting centered facet distance is at least the claimed radius. It also checks the singleton equality that forces the upper bound.

These finite checks are corroborative only and are not used as an infinite proof.

## Relationship to prior work
Pilaud and Poliakova introduce the \((m,n)\)-Hochschild polytopes by deleting inequalities from multiplihedra. Their main geometric conclusion for \(m=1\) is that \(\mathrm{Hoch}(1,n)\) is a deformed permutahedron whose oriented skeleton realizes the Hochschild lattice. They explicitly develop vertex, facet, Minkowski, and tight-right-hand-side parametrizations.

The same paper records that the classical permutahedron has
\[
z_J=\binom{|J|+1}{2}.
\]
Equation (6) shows that every Hochschild tight right-hand side lies below the corresponding permutahedral one. The new metric statement is that this deformation nevertheless preserves the exact largest intrinsic Euclidean ball: the singleton lower constraints remain rigid enough to keep both the radius and the unique center unchanged.

Earlier work on Hochschild lattices gives other geometric and cubic realizations. Those realizations are not Euclidean-isometric to the Pilaud--Poliakova deformed permutahedron and therefore do not determine its inradius.

Targeted literature and published-result searches for Hochschild-polytope inradii, Chebyshev centers, largest inscribed balls, freehedron inradii, and broader deformed-permutahedron inradii did not locate a theorem implying (1)--(2). The inspected exact paper contains no inradius, Chebyshev-center, or largest-inscribed-ball statement.

## Limitations
The theorem concerns only the \((1,n)\)-Hochschild family. No formula is claimed here for general \((m,n)\)-Hochschild polytopes.

The metric is realization-specific. Cubic realizations, freehedra, and other combinatorially related models can have different Euclidean radii.

The proof uses the exact tight-right-hand-side formula from the cited source. It does not independently rederive the Hochschild facet parametrization.

A residual originality risk remains that a sufficiently general Chebyshev-center theorem for deformed permutahedra could imply the result under terminology not exposed by the searches.

## References
1. Vincent Pilaud and Daria Poliakova, *Hochschild polytopes*, arXiv:2307.05940, first public version 2023-07-12; Mathematische Annalen 392 (2025), 2395--2441, DOI 10.1007/s00208-025-03120-x.
2. Camille Combe, *A geometric and combinatorial exploration of Hochschild lattices*, arXiv:2007.00048; Advances in Applied Mathematics 128 (2021), 102196.
