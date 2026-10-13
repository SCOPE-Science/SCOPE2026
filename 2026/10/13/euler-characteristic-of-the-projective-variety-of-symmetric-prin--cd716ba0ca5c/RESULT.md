# Euler characteristic of the projective variety of symmetric principal minors
## Finding
For every integer
\[
n\ge4,
\]
let
\[
Z_n\subset\mathbb P((\mathbb C^2)^{\otimes n})\cong\mathbb P^{2^n-1}
\]
be the projective variety of vectors of principal minors of complex symmetric
\[
n\times n
\]
matrices. Then
\[
\boxed{\chi_{\mathrm{top}}(Z_n)=2^n.}
\]
Thus, despite
\[
\dim Z_n=\binom{n+1}{2}
\]
while the ambient projective dimension is
\[
2^n-1,
\]
the variety has exactly the ambient Euler characteristic:
\[
\boxed{
\chi_{\mathrm{top}}(Z_n)
=
\chi_{\mathrm{top}}(\mathbb P^{2^n-1}).
}
\]
Equivalently,
\[
\boxed{
\chi_c(\mathbb P^{2^n-1}\setminus Z_n)=0.
}
\]

## Assumptions and scope
The base field is
\[
\mathbb C.
\]
The notation
\[
Z_n
\]
is the projective variety used in the principal-minor literature: it is the closure of the homogeneous principal-minor map
\[
[A,t]
\longmapsto
[t^{n-|I|}\Delta_I(A)]_{I\subseteq[n]},
\]
where
\[
A
\]
is symmetric and
\[
\Delta_I(A)
\]
is the principal minor indexed by
\[
I.
\]

The novelty claim is restricted to
\[
n\ge4.
\]
The low-dimensional cases are boundary checks. In particular,
\[
Z_3
\]
is Cayley's
\[
2\times2\times2
\]
hyperdeterminant hypersurface, whose Euler characteristic is already covered by the corresponding Segre-dual calculation.

No smoothness assumption is made. The argument applies directly to the singular projective variety.

## Proof
The archival literature proves that
\[
Z_n
\]
is invariant under
\[
(\operatorname{SL}(2)^{\times n})\rtimes\mathfrak S_n
\]
acting on
\[
(\mathbb C^2)^{\otimes n}.
\]
Choose the diagonal one-parameter subgroup
\[
\lambda(z)
=
\left(
\begin{pmatrix}z^{a_1}&0\\0&z^{-a_1}\end{pmatrix},
\ldots,
\begin{pmatrix}z^{a_n}&0\\0&z^{-a_n}\end{pmatrix}
\right),
\qquad
a_i=2^{i-1}.
\]

Index the tensor-coordinate basis by subsets
\[
I\subseteq[n].
\]
The corresponding coordinate line has weight
\[
w_I=\sum_{i\in I}a_i-\sum_{i\notin I}a_i.
\]
These weights are pairwise distinct. Indeed, if
\[
w_I=w_J
\]
and
\[
k
\]
is the largest index in the symmetric difference, then the contribution
\[
2a_k
\]
has absolute value strictly larger than the sum of all possible lower-index contributions. Hence
\[
I=J.
\]
Therefore the ambient fixed locus consists exactly of the
\[
2^n
\]
tensor-coordinate points.

Every one of these coordinate points lies in
\[
Z_n.
\]
There are two independent ways to see this. First, setting
\[
A=0,\qquad t=1
\]
in the homogeneous principal-minor map gives the coordinate point indexed by the empty subset, and the Weyl elements in the
\[
\operatorname{SL}(2)
\]
factors move that point through all
\[
2^n
\]
coordinate points because
\[
Z_n
\]
is invariant under the full product group.

There is also a direct degeneration. Fix
\[
I\subseteq[n]
\]
and let
\[
t=s,
\qquad
A_s=\operatorname{diag}(a_1(s),\ldots,a_n(s)),
\]
where
\[
a_j(s)=1\quad(j\in I),
\qquad
a_j(s)=s^2\quad(j\notin I).
\]
For a subset
\[
J\subseteq[n],
\]
the homogeneous principal-minor coordinate has order
\[
n-|J|+2|J\setminus I|.
\]
Its difference from the order at
\[
J=I
\]
is
\[
|I\setminus J|+|J\setminus I|,
\]
which is positive unless
\[
J=I.
\]
After projective rescaling, the image therefore tends to the coordinate point indexed by
\[
I.
\]

It follows that
\[
Z_n^{\lambda}
\]
is exactly the full set of
\[
2^n
\]
ambient coordinate fixed points.

For a complex algebraic variety
\[
Y
\]
with an algebraic
\[
\mathbb C^*
\]
action, compactly supported Euler characteristic localizes to the fixed locus:
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
One proof removes the fixed locus and uses a finite Rosenlicht stratification of the remainder; every nonfixed stratum has a
\[
\mathbb C^*
\]
-orbit factor and hence compactly supported Euler characteristic zero.

Since
\[
Z_n
\]
is projective,
\[
\chi_{\mathrm{top}}(Z_n)=\chi_c(Z_n).
\]
Consequently
\[
\chi_{\mathrm{top}}(Z_n)=\#Z_n^{\lambda}=2^n.
\]
Finally,
\[
\chi_{\mathrm{top}}(\mathbb P^{2^n-1})=2^n,
\]
so additivity of
\[
\chi_c
\]
gives
\[
\chi_c(\mathbb P^{2^n-1}\setminus Z_n)=0.
\]

## Verification
The bundled checker verifies the two finite combinatorial ingredients of the proof for
\[
4\le n\le18.
\]
It checks that the signed binary weights coming from
\[
a_i=2^{i-1}
\]
are all distinct and that their number is exactly
\[
2^n.
\]

It also checks the direct diagonal degeneration for every subset
\[
I\subseteq[n]
\]
through
\[
n=9,
\]
verifying that the exponent
\[
n-|J|+2|J\setminus I|
\]
has the unique minimum at
\[
J=I.
\]

These finite checks are regression evidence only. The proof for arbitrary
\[
n\ge4
\]
is the symbolic weight and degeneration argument above.

## Relationship to prior work
Holtz and Sturmfels introduced the complex algebraic image of the symmetric principal-minor map and derived its hyperdeterminantal relations. Oeding then defined the projective variety
\[
Z_n
\]
precisely, proved its invariance under
\[
(\operatorname{SL}(2)^{\times n})\rtimes\mathfrak S_n,
\]
and established its set-theoretic equations. The same source records
\[
\dim Z_n=\binom{n+1}{2}
\]
and emphasizes applications to probability, statistical physics, spectral graph theory, and related tensor geometry.

The inspected archival papers do not state the ordinary Euler characteristic, a Poincaré polynomial, or a fixed-point formula for
\[
Z_n.
\]
Later work of Al Ahmadieh and Vinzant recovers Oeding's complex characterization by determinantal multiaffine methods but likewise does not state the Euler formula in the inspected record.

Targeted searches under the aliases “variety of principal minors,” “symmetric principal-minor variety,” and
\[
Z_n
\]
found no equivalent topological formula. Searches for Poincaré, topology, fixed points, and Euler characteristic likewise produced no covering result.

The case
\[
n=3
\]
is deliberately excluded from the novelty claim because it is the
\[
2\times2\times2
\]
hyperdeterminant hypersurface and is covered by the corresponding Segre-dual Euler calculation. For
\[
n\ge4,
\]
principal-minor varieties are higher-codimensional objects and are not implied by that hypersurface case.

## Limitations
The theorem computes only ordinary Euler characteristic and the compactly supported Euler characteristic of the complement. It does not determine Betti numbers, mixed Hodge numbers, intersection cohomology, singularity type, degree, or the integral cohomology ring.

The localization argument is short once the large
\[
(\operatorname{SL}(2)^{\times n})\rtimes\mathfrak S_n
\]
symmetry is brought to bear, so an unindexed or folklore observation remains a residual originality risk.

The real principal-minor image has additional inequalities and is not covered by this complex-projective statement.

## References
Olga Holtz and Bernd Sturmfels, *Hyperdeterminantal relations among symmetric principal minors*, arXiv:math/0604374, first submitted 17 April 2006; *Journal of Algebra* 316 (2007), 634--648, DOI 10.1016/j.jalgebra.2007.01.039.

Luke Oeding, *Set-Theoretic Defining Equations of the Variety of Principal Minors of Symmetric Matrices*, arXiv:0809.4236, first submitted 24 September 2008; *Algebra & Number Theory* 5 (2011), 75--109, DOI 10.2140/ant.2011.5.75.

Abeer Al Ahmadieh and Cynthia Vinzant, *Characterizing principal minors of symmetric matrices via determinantal multiaffine polynomials*, arXiv:2105.13444, first submitted 27 May 2021.
