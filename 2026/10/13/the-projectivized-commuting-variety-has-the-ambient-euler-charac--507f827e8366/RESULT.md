# The projectivized commuting variety has the ambient Euler characteristic
## Finding
Let
\[
\mathfrak g\neq0
\]
be any finite-dimensional complex Lie algebra, and let
\[
\mathcal C(\mathfrak g)
=
\{(x,y)\in\mathfrak g\oplus\mathfrak g:[x,y]=0\}
\]
be its commuting variety. Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\mathbb P\mathcal C(\mathfrak g)\right)
=
2\dim\mathfrak g
=
\chi_{\mathrm{top}}\!\left(\mathbb P(\mathfrak g\oplus\mathfrak g)\right).
}
\]

If
\[
U=
\{[x:y]\in\mathbb P\mathcal C(\mathfrak g):x\neq0,\ y\neq0\},
\]
then
\[
\boxed{\chi_c(U)=0.}
\]
Thus all Euler characteristic is carried by the two coordinate boundary pieces.

## Assumptions and scope
The base field is
\[
\mathbb C.
\]
No reductivity, semisimplicity, irreducibility, or smoothness assumption is required.

The projectivization is
\[
\mathbb P\mathcal C(\mathfrak g)
=
\bigl(\mathcal C(\mathfrak g)\setminus\{(0,0)\}\bigr)/\mathbb C^*,
\]
where the quotient scales both entries simultaneously.

The open locus \(U\) is not projective, so its invariant is compactly supported Euler characteristic.

## Proof
Define an algebraic
\[
\mathbb C^*
\]
action on
\[
\mathbb P(\mathfrak g\oplus\mathfrak g)
\]
by
\[
t\cdot[x:y]=[tx:y].
\]
This preserves the commuting variety because
\[
[tx,y]=t[x,y].
\]

Suppose
\[
[x:y]
\]
is fixed. For every
\[
t\in\mathbb C^*
\]
there is a scalar
\[
c_t\in\mathbb C^*
\]
such that
\[
(tx,y)=c_t(x,y).
\]
If both
\[
x\neq0
\qquad\text{and}\qquad
y\neq0,
\]
then the first coordinate forces
\[
c_t=t,
\]
while the second forces
\[
c_t=1.
\]
For
\[
t\neq1
\]
this is impossible.

Conversely, every point with one coordinate zero is fixed, and every such point belongs to the commuting variety. Hence
\[
\bigl(\mathbb P\mathcal C(\mathfrak g)\bigr)^{\mathbb C^*}
=
\mathbb P(\mathfrak g\oplus0)
\sqcup
\mathbb P(0\oplus\mathfrak g).
\]
Both components are
\[
\mathbb P^{\,\dim\mathfrak g-1}.
\]

For a complex algebraic variety
\[
Y
\]
with an algebraic
\[
\mathbb C^*
\]
action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
One proof removes the fixed locus and stratifies the remainder into invariant locally closed pieces whose orbit fibers have compactly supported Euler characteristic zero.

Since
\[
\mathbb P\mathcal C(\mathfrak g)
\]
is projective,
\[
\chi_{\mathrm{top}}\!\left(\mathbb P\mathcal C(\mathfrak g)\right)
=
2\,\chi_{\mathrm{top}}\!\left(\mathbb P^{\,\dim\mathfrak g-1}\right)
=
2\dim\mathfrak g.
\]
The ambient projective space is
\[
\mathbb P^{\,2\dim\mathfrak g-1},
\]
whose Euler characteristic is also
\[
2\dim\mathfrak g.
\]

The same action has no fixed points on \(U\), so
\[
\chi_c(U)=0.
\]

## Verification
The bundled checker verifies for
\[
1\le\dim\mathfrak g\le200
\]
that the two fixed projective components contribute
\[
2\dim\mathfrak g,
\]
equal to the Euler characteristic of the ambient projective space.

It also checks the numerical specializations for
\[
\mathfrak{gl}_n,\quad
\mathfrak{sl}_n,\quad
\mathfrak{so}_n,\quad
\mathfrak{sp}_{2n}
\]
over a finite regression range.

These computations are consistency checks only. The theorem for every finite-dimensional complex Lie algebra is the fixed-locus argument above.

## Relationship to prior work
Richardson's classical work proves irreducibility of commuting varieties for reductive Lie algebras in characteristic zero. Popov studies the same commuting variety
\[
\mathcal C(\mathfrak g)
\]
for noncommutative reductive Lie algebras, analyzes its irregular and singular loci, proves a codimension bound for the singular locus, and proves rationality.

The complete inspected Popov text does not state the topological Euler characteristic of the projectivized commuting variety. Targeted full-text searches found no occurrence of “Euler,” “fixed point,” or “projective.”

Ginzburg's work on the isospectral commuting variety studies a finite cover and its normalization, proving Cohen--Macaulay and Gorenstein properties. Those results concern a related but different space and do not imply the Euler formula here.

Targeted literature and semantic searches for the projectivized commuting variety, Euler characteristic, commuting matrices, and the scaling fixed-point formulation did not locate an equivalent or stronger statement.

A previously recorded result for projectivized commuting nilpotent matrix pairs concerns the proper subvariety obtained by requiring both entries to be nilpotent. Its fixed locus is smaller and does not imply the formula for the full commuting variety.

## Limitations
Ordinary Euler characteristic is coarse. The theorem does not determine irreducibility, singularities, local topology, intersection cohomology, mixed Hodge structure, or individual Betti numbers.

The formula does not extend automatically to subvarieties obtained by imposing nilpotency, rank conditions, or membership in prescribed orbit closures.

The proof is short and uses only a natural one-parameter scaling action, so an older unindexed or folklore observation remains a residual originality risk.

## References
R. W. Richardson, *Commuting varieties of semisimple Lie algebras and algebraic groups*, *Compositio Mathematica* 38 (1979), 311--327.

Vladimir L. Popov, *Irregular and singular loci of commuting varieties*, arXiv:0801.3074, first submitted 20 January 2008; *Transformation Groups* 13 (2008), 819--837, DOI 10.1007/s00031-008-9018-9.

Victor Ginzburg, *Isospectral commuting variety, the Harish-Chandra D-module, and principal nilpotent pairs*, arXiv:1108.5367, first submitted 26 August 2011.
