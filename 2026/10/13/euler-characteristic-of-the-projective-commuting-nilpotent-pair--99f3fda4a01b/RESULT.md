# Euler characteristic of the projective commuting-nilpotent pair variety
## Finding
Let
\[
n\ge2.
\]
Let
\[
\mathcal N_{2,n}
=
\{(A,B)\in M_n(\mathbb C)^2:
A\ \text{and}\ B\ \text{are nilpotent},\ AB=BA\}.
\]
Its defining conditions are homogeneous, so it is a cone. Let
\[
\mathbb P\mathcal N_{2,n}
\subset
\mathbb P^{2n^2-1}
\]
be its projectivization.

Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\mathbb P\mathcal N_{2,n}\right)
=
2n(n-1).
}
\]

For the first three nontrivial matrix sizes this gives
\[
4,\ 12,\ 24.
\]
By contrast, the published projective degrees for
\[
n=2,3,4
\]
are
\[
4,\ 72,\ 5440.
\]
Thus ordinary Euler characteristic and projective degree separate immediately after the smallest case.

## Assumptions and scope
The base field is \(\mathbb C\).

The projectivization uses simultaneous scalar multiplication on
\[
M_n(\mathbb C)\oplus M_n(\mathbb C).
\]
The result concerns the projective variety itself, not a quotient by conjugation.

No smoothness assumption is made. The commuting-nilpotent pair variety is highly singular, but Euler localization for algebraic \(\mathbb C^*\)-actions does not require smoothness.

## Proof
Choose an integer
\[
Q\ge3
\]
and put
\[
c_i=Q^i
\qquad
(1\le i\le n).
\]
Let
\[
D(z)
=
\operatorname{diag}\!\left(z^{c_1},\ldots,z^{c_n}\right).
\]
Choose an integer
\[
L>2Q^{n+1}.
\]
Define a one-parameter action by
\[
z\cdot(A,B)
=
\left(
D(z)AD(z)^{-1},
z^L D(z)BD(z)^{-1}
\right).
\]
Conjugation and scalar multiplication preserve nilpotency, and
\[
[A,B]=0
\]
is preserved because the commutator is multiplied by a scalar and conjugated.

The coordinate \(A_{ij}\) has weight
\[
c_i-c_j,
\]
while \(B_{ij}\) has weight
\[
L+c_i-c_j.
\]

For \(i\ne j\), all ordered differences
\[
Q^i-Q^j
\]
are distinct. Indeed, if the difference is positive, its \(Q\)-adic valuation determines the smaller exponent, and then the quotient determines the larger exponent; negative differences are handled by sign. The choice of \(L\) separates every \(A\)-weight from every \(B\)-weight.

The only repeated weights are the diagonal weights: all \(A_{ii}\) have weight \(0\), and all \(B_{ii}\) have weight \(L\). Hence the fixed locus in the ambient projective space is the union of:
the off-diagonal coordinate points in the first matrix factor;
the off-diagonal coordinate points in the second matrix factor;
the projective space of diagonal \(A\)-matrices;
and the projective space of diagonal \(B\)-matrices.

A nonzero diagonal complex matrix is never nilpotent. Therefore the two diagonal fixed projective spaces do not meet
\[
\mathbb P\mathcal N_{2,n}.
\]

For every
\[
i\ne j,
\]
the matrix unit
\[
E_{ij}
\]
satisfies
\[
E_{ij}^2=0.
\]
Thus both
\[
(E_{ij},0)
\quad\text{and}\quad
(0,E_{ij})
\]
are commuting nilpotent pairs. Consequently
\[
\left(\mathbb P\mathcal N_{2,n}\right)^{\mathbb C^*}
=
\{[(E_{ij},0)],[(0,E_{ij})]:i\ne j\},
\]
a finite set with
\[
2n(n-1)
\]
points.

For every complex algebraic variety \(Y\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
One may prove this by removing the fixed locus and applying a finite Rosenlicht stratification; every nonfixed stratum has a factor isomorphic to a finite quotient of \(\mathbb C^*\), whose compactly supported Euler characteristic is zero.

Since
\[
\mathbb P\mathcal N_{2,n}
\]
is projective,
\[
\chi_{\mathrm{top}}\!\left(\mathbb P\mathcal N_{2,n}\right)
=
\chi_c\!\left(\mathbb P\mathcal N_{2,n}\right)
=
2n(n-1).
\]

## Verification
The bundled checker verifies for
\[
2\le n\le30
\]
that the selected one-parameter subgroup separates all off-diagonal coordinate weights within and between the two matrix factors.

It also verifies the predicted count
\[
2n(n-1)
\]
and directly checks, in a finite matrix range, that every surviving coordinate matrix unit squares to zero and therefore gives a valid commuting nilpotent pair with the other factor zero.

These finite computations are regression evidence only. The all-\(n\) theorem is proved symbolically above.

## Relationship to prior work
Baranovsky proved that the affine variety of pairs of commuting nilpotent matrices is irreducible and related it to the punctual Hilbert scheme. Ngo and Šivic study the more general varieties of commuting nilpotent tuples, including the pair case. Silva and Vainsencher study the projectivized pair variety enumeratively and compute its projective degree for matrix sizes \(2,3,4\).

The inspected full text on commuting nilpotent tuples studies irreducibility, dimension, and perturbation by regular nilpotent tuples; targeted searches found no Euler-characteristic or fixed-point statement. The enumerative source reports projective degrees but does not state the Euler formula above in the accessible material.

The formula therefore complements the known degree data: projective degree grows rapidly even for small \(n\), whereas ordinary Euler characteristic collapses to the quadratic count of off-diagonal coordinate directions.

## Limitations
The theorem determines only ordinary topological Euler characteristic. It does not give the Betti numbers, mixed Hodge structure, singularity stratification, intersection cohomology, or projective degree.

The fixed-point calculation is deliberately global and coarse. It does not describe the geometry of the nonfixed orbits or the connection with punctual Hilbert schemes.

Because the localization proof is short, an older unindexed observation remains a residual novelty risk.

## References
Vladimir Baranovsky, *The variety of pairs of commuting nilpotent matrices is irreducible*, *Transformation Groups* 6 (2001), 3--8, DOI 10.1007/BF01236059.

Nham V. Ngo and Klemen Šivic, *On varieties of commuting nilpotent matrices*, arXiv:1308.4438, first submitted 20 August 2013; *Linear Algebra and its Applications* 452 (2014), 237--262.

Adriana R. Silva and Israel Vainsencher, *Degree of the variety of pairs of nilpotent commuting matrices*, *Bulletin of the Brazilian Mathematical Society, New Series* 45 (2014), 837--863, DOI 10.1007/s00574-014-0078-2.
