# Euler characteristic of homogeneous consistency loci
## Finding
Let
\[
n\ge2,\qquad m\ge1,\qquad d_1,\ldots,d_m\ge1,
\]
and put
\[
N_i=\binom{n+d_i-1}{n-1}.
\]
Consider
\[
A=
\prod_{i=1}^{m}
\mathbb P\!\left(\operatorname{Sym}^{d_i}\mathbb C^n\right).
\]
Let
\[
R\subset A
\]
be the locus of ordered systems
\[
([f_1],\ldots,[f_m])
\]
having a common zero in
\[
\mathbb P^{n-1},
\]
and set
\[
U=A\setminus R.
\]

Then
\[
\boxed{
\chi_c(U)=
\sum_{t=0}^{n}
(-1)^t\binom nt
\prod_{i=1}^{m}(N_i-t).
}
\]

Since
\[
\chi_{\mathrm{top}}(A)=\prod_{i=1}^{m}N_i,
\]
the consistency locus has
\[
\boxed{
\chi_{\mathrm{top}}(R)=
\prod_{i=1}^{m}N_i-
\sum_{t=0}^{n}
(-1)^t\binom nt
\prod_{i=1}^{m}(N_i-t).
}
\]

The formula has three sharp regimes. If
\[
m<n,
\]
then
\[
U=\varnothing
\]
and the alternating sum vanishes. If
\[
m=n,
\]
then
\[
\chi_c(U)=n!.
\]
If all forms are linear, then
\[
N_i=n
\]
and
\[
\chi_c(U)=n!\,{m\brace n},
\]
the number of surjections from an \(m\)-element set onto an \(n\)-element set.

## Assumptions and scope
The base field is
\[
\mathbb C.
\]
Each form is nonzero up to its own scalar, because every coefficient block is separately projectivized.

The common-zero locus is closed: it is the proper image of the incidence variety
\[
\left\{
(([f_i]),[x])\in A\times\mathbb P^{n-1}:
f_i(x)=0\text{ for all }i
\right\}.
\]

For
\[
m=n,
\]
this is the classical homogeneous resultant hypersurface. For
\[
m>n,
\]
it is the natural projectivized consistency locus for an overdetermined system.

## Proof
Choose diagonal weights
\[
w_1,\ldots,w_n
\]
so rapidly separated that distinct monomials occurring in every degree
\[
d_i
\]
have distinct weights. A base larger than
\[
1+\max_i d_i
\]
suffices.

The induced
\[
\mathbb C^*
\]
action on each projective coefficient space has monomial coordinate points as its fixed points. Hence
\[
U^{\mathbb C^*}
\]
consists of monomial systems.

For a monomial system
\[
(M_1,\ldots,M_m),
\]
consider the coordinate point
\[
[e_j]\in\mathbb P^{n-1}.
\]
Every monomial vanishes at
\[
[e_j]
\]
except the pure power
\[
x_j^{d_i}.
\]
Therefore the system has no common zero only if, for every
\[
j\in\{1,\ldots,n\},
\]
at least one chosen monomial is the pure power
\[
x_j^{d_i}.
\]

This condition is also sufficient. If
\[
[x_1:\cdots:x_n]
\]
is any projective point, choose
\[
j
\]
with
\[
x_j\ne0.
\]
The covering condition supplies some equation equal to
\[
x_j^{d_i},
\]
which is nonzero at that point. Thus the point cannot be a common zero.

So the fixed points in
\[
U
\]
are exactly the monomial tuples whose selected pure powers cover all
\[
n
\]
coordinate labels.

For a subset
\[
T\subseteq\{1,\ldots,n\}
\]
of forbidden pure-power labels with
\[
|T|=t,
\]
the \(i\)-th equation has
\[
N_i-t
\]
allowable monomials. Inclusion--exclusion gives
\[
\#U^{\mathbb C^*}
=
\sum_{t=0}^{n}
(-1)^t\binom nt
\prod_{i=1}^{m}(N_i-t).
\]

For an algebraic
\[
\mathbb C^*
\]
action on a complex algebraic variety,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
The fixed locus here is finite, so the displayed count is
\[
\chi_c(U).
\]
Additivity in
\[
A=R\sqcup U
\]
gives the formula for
\[
R.
\]

If
\[
m<n,
\]
the polynomial
\[
\prod_i(N_i-t)
\]
has degree less than \(n\), so its \(n\)-th finite difference vanishes. Geometrically, fewer than \(n\) positive-degree hypersurfaces in
\[
\mathbb P^{n-1}
\]
cannot have empty intersection.

If
\[
m=n,
\]
the same finite-difference identity applied to the monic-in-\((-t)\) degree-\(n\) product gives
\[
n!.
\]

For linear forms,
\[
N_i=n,
\]
and the inclusion--exclusion formula is the classical count
\[
n!\,{m\brace n}
\]
of onto maps.

## Verification
The bundled checker generates actual exponent vectors for homogeneous monomials in small dimensions and degrees. It exhaustively enumerates monomial systems, tests directly whether their pure-power labels cover all coordinate directions, and compares the result against the inclusion--exclusion formula.

It also verifies independently that the formula vanishes for
\[
m<n,
\]
specializes to
\[
n!
\]
for
\[
m=n,
\]
and specializes to
\[
n!\,{m\brace n}
\]
for systems of linear forms.

These computations are finite regression evidence only. The theorem for arbitrary
\[
m,n,d_i
\]
is proved by the symbolic fixed-point and inclusion--exclusion argument above.

## Relationship to prior work
Classical homogeneous resultant theory treats the square case of \(n\) forms in \(n\) variables. D'Andrea and Dickenstein give explicit determinant formulas for that resultant and describe its vanishing as the common-root condition.

Vassiliev studies the topology of spaces of non-resultant polynomial systems in two variables, using affine coefficient spaces and discriminant-complement methods. This is a finer topological analysis in a different parameter-space model and low variable dimension.

Later work on overdetermined systems uses the term *consistency variety* for the closure of systems admitting a common root and develops its algebraic geometry for general linear series. The formula here concerns the separately projectivized complete homogeneous linear-series case and computes the compactly supported Euler characteristic of its complement in every number of equations and every multidegree.

The square specialization recovers the degree-independent value
\[
n!.
\]
The new overdetermined regime
\[
m>n
\]
is qualitatively different: the answer depends on all coefficient-space dimensions through an inclusion--exclusion polynomial.

## Limitations
The result computes Euler characteristic only. It does not determine Betti numbers, Hodge structures, motives, singularities, degrees, or the number of irreducible components of the consistency locus.

The proof uses the complete homogeneous linear series and separate projectivization of every coefficient block. Sparse supports, affine coefficient spaces, or coupled scalar quotients have different fixed loci.

The formula is short once the torus-fixed monomial criterion is isolated, so an equivalent unindexed or folklore observation remains a residual originality risk.

## References
Carlos D'Andrea and Alicia Dickenstein, *Explicit formulas for the multivariate resultant*, arXiv:math/0007036, first submitted 6 July 2000; *Journal of Pure and Applied Algebra* 164 (2001), 59--86, DOI 10.1016/S0022-4049(00)00145-6.

V. A. Vassiliev, *Homology of spaces of non-resultant polynomial systems in \(\mathbb R^2\) and \(\mathbb C^2\)*, arXiv:1409.6005, first submitted 21 September 2014.

Leonid Monin, *Overdetermined Systems of Equations on Toric, Spherical, and Other Algebraic Varieties*, arXiv:1902.05119, first submitted 13 February 2019; *Advances in Mathematics* 369 (2020), 107147.
