# Canonical positivity dichotomy for Fano surfaces of complete intersections
## Finding
Let
\[
X\subset\mathbb P^r_{\mathbb C}
\]
be a general complete intersection of type
\[
(d_1,\ldots,d_m),
\qquad
d_i\ge2,
\]
and let \(k\ge1\). Assume that the expected dimension of the Fano scheme of \(k\)-planes is
\[
\delta
=
(k+1)(r-k)
-
\sum_{i=1}^{m}\binom{d_i+k}{k}
=
2,
\]
and that
\[
r\ge2k+m.
\]
In this standard range the general Fano scheme
\[
F=F_k(X)
\]
is a smooth connected projective surface.

Define
\[
B
=
\sum_{i=1}^{m}\binom{d_i+k}{k+1}
-
r
-
1.
\]
Then
\[
K_F\simeq\mathcal O_F(B),
\]
where \(\mathcal O_F(1)\) is the Pluecker polarization, and
\[
B\ge0.
\]

Equality is completely rigid:
\[
B=0
\]
if and only if, up to permutation of the defining equations,
\[
k=1,
\qquad
r=5,
\qquad
(d_1,d_2)=(2,2).
\]
Thus every such Fano surface has ample canonical bundle, hence is of general type, except the Fano surface of lines on a general intersection of two quadrics in
\[
\mathbb P^5.
\]
The exceptional surface has trivial canonical bundle; classically it is an abelian surface, in fact a Jacobian of a genus-two curve, and its Pluecker degree is
\[
32.
\]

In particular, within this entire expected-surface family there are no del Pezzo cases and no K3 cases: the only non-general-type surface is the abelian two-quadric line surface.

## Assumptions and scope
The ground field is \(\mathbb C\). The complete intersection is general, all defining degrees are at least two, and the parametrized linear spaces have positive dimension \(k\ge1\).

The numerical range
\[
r\ge2k+m
\]
is the standard irreducible-surface range used in the literature on Fano schemes of general complete intersections. Together with
\[
\delta=2,
\]
it excludes the exceptional maximal-linear-space behavior of quadrics and puts the problem in the smooth connected expected-dimensional regime.

The theorem concerns the canonical class with respect to the Pluecker polarization. It does not classify special complete intersections whose Fano schemes acquire excess dimension, singularities, or extra components.

## Proof
The standard normal-bundle computation on the Grassmannian gives
\[
K_F
\simeq
\mathcal O_F
\left(
\sum_{i=1}^{m}\binom{d_i+k}{k+1}
-
r
-
1
\right).
\]
Thus it remains to prove that the coefficient
\[
B
=
\sum_i\binom{d_i+k}{k+1}
-r-1
\]
is nonnegative and to classify equality under the expected-dimension constraint.

Put
\[
q=k+1\ge2
\]
and
\[
R_i=\binom{d_i+k}{k}.
\]
The equation
\[
\delta=2
\]
is
\[
q(r-k)=2+\sum_iR_i.
\]
Using
\[
\binom{d_i+k}{k+1}
=
\frac{d_i}{q}R_i,
\]
we obtain
\[
qB
=
\sum_i(d_i-1)R_i
-
(q^2+2).
\]
Therefore
\[
B\ge0
\]
is equivalent to
\[
\sum_i(d_i-1)R_i\ge q^2+2.
\]

For every \(d_i\ge2\),
\[
(d_i-1)R_i
\ge
\binom{q+1}{2}
=
\frac{q(q+1)}2,
\]
with equality exactly at \(d_i=2\).

If \(m\ge3\), then
\[
\sum_i(d_i-1)R_i
\ge
\frac{3q(q+1)}2
>
q^2+2
\]
for every \(q\ge2\). Hence \(B>0\).

If \(m=2\), then
\[
\sum_i(d_i-1)R_i
\ge
q(q+1)
\ge
q^2+2.
\]
Equality in the second inequality occurs only for
\[
q=2,
\]
and equality in the first requires
\[
d_1=d_2=2.
\]
The expected-dimension equation then becomes
\[
2(r-1)=2+3+3,
\]
so
\[
r=5.
\]
This produces exactly the line surface on a \((2,2)\) complete intersection in \(\mathbb P^5\).

It remains to treat \(m=1\). If \(d_1\ge3\), then
\[
(d_1-1)R_1
\ge
2\binom{q+2}{3}
=
\frac{q(q+1)(q+2)}3
>
q^2+2
\]
for every \(q\ge2\), so \(B>0\).

If \(m=1\) and \(d_1=2\), then
\[
r-k
=
\frac{2+\binom{q+1}{2}}q
=
\frac{q+1}{2}+\frac2q.
\]
The assumed range
\[
r\ge2k+1
\]
would force
\[
r-k\ge q.
\]
For \(q\ge3\) this is impossible because
\[
\frac{q+1}{2}+\frac2q<q.
\]
For \(q=2\), the expected-dimension equation would require
\[
r-k=\frac52,
\]
which is not integral. Hence no quadric hypersurface occurs in the stated surface range.

Thus
\[
B\ge0
\]
always, with equality only for
\[
(k,r,\mathbf d)=(1,5,(2,2)).
\]
Since \(\mathcal O_F(1)\) is ample, \(B>0\) makes \(K_F\) ample. In the equality case the canonical bundle is trivial. The classical geometry of an intersection of two quadrics identifies its line surface with an abelian surface, and the published Schubert computation gives Pluecker degree \(32\).

## Verification
The bundled exact checker exhausts a broad bounded family of
\[
(k,m,\mathbf d)
\]
values. Whenever the expected-dimension equation gives an integral ambient dimension satisfying
\[
r\ge2k+m
\]
and
\[
\delta=2,
\]
the script verifies
\[
B\ge0
\]
and records every zero.

In the tested range the unique zero is
\[
(k,r,\mathbf d)=(1,5,(2,2)).
\]
The script also checks the three symbolic inequalities used in the proof over a much larger range of \(q\).

These finite computations are regression evidence only. The infinite result follows from the exact reduction
\[
qB
=
\sum_i(d_i-1)R_i-(q^2+2)
\]
and the three-case argument above.

## Relationship to prior work
Debarre and Manivel establish the basic expected-dimension, smoothness, and connectedness theory for Fano schemes of linear spaces on general complete intersections; the first public version of their work appeared in November 1996.

Ciliberto and Zaidenberg later give the canonical-class formula
\[
K_F
\simeq
\mathcal O_F
\left(
\sum_i\binom{d_i+k}{k+1}-(r+1)
\right)
\]
and explicitly study the surface case. They compute the line surface of a general intersection of two quadrics in \(\mathbb P^5\), obtaining Pluecker degree \(32\), vanishing canonical square, and the classical abelian-surface identification. Their paper also classifies irregular Fano schemes.

The inspected sources do not state that the canonical coefficient is globally nonnegative for every expected-dimensional Fano surface in the standard range, nor that its zero locus consists of exactly the \((2,2)\) line surface in \(\mathbb P^5\). Claim-specific searches using canonical positivity, general type, trivial canonical bundle, and two-quadric formulations did not locate that dichotomy.

## Limitations
The theorem is specific to two-dimensional Fano schemes. In higher dimension, Fano schemes of complete intersections can themselves be Fano varieties; the sign of the canonical coefficient is not constrained in the same way.

The complete intersection must be general and the Fano scheme must lie in the standard expected-dimensional range. Special fibers may have singularities, extra components, or different Kodaira behavior.

The arithmetic argument is short once the canonical formula is known, so an unindexed classical source could contain the same global positivity corollary.

## References
Olivier Debarre and Laurent Manivel, *Schémas de Fano*, arXiv:alg-geom/9611033, first submitted 26 November 1996; published as *Sur la variété des espaces linéaires contenus dans une intersection complète*, Math. Ann. 312 (1998), 549--574.

Ciro Ciliberto and Mikhail Zaidenberg, *On Fano schemes of complete intersections*, arXiv:1903.11294, first submitted 27 March 2019.

Miles Reid, *The complete intersection of two or more quadrics*, Ph.D. thesis, Cambridge, 1972.
