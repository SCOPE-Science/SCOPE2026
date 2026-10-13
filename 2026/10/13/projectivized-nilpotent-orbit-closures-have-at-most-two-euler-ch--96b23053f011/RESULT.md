# Projectivized nilpotent orbit closures have at most two Euler characteristics in each simple Lie type
## Finding
Let
\[
\mathfrak g
\]
be a complex simple Lie algebra with root system
\[
\Phi.
\]
Let
\[
\mathcal O\subset\mathfrak g
\]
be a nonzero nilpotent orbit.

Write
\[
\Phi_{\mathrm{long}}
\]
and
\[
\Phi_{\mathrm{short}}
\]
for the long and short roots, with the short set empty in the simply laced case. If two root lengths occur, let
\[
\mathcal O_{\mathrm{short}}
\]
be the nilpotent orbit of a nonzero short-root vector.

Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\mathbb P\overline{\mathcal O}\right)
=
|\Phi_{\mathrm{long}}|
+
\mathbf 1_{\mathcal O_{\mathrm{short}}\subseteq\overline{\mathcal O}}
|\Phi_{\mathrm{short}}|.
}
\]

Therefore a simply laced simple Lie algebra has the same Euler characteristic for every nonzero projectivized nilpotent orbit closure:
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\mathbb P\overline{\mathcal O}\right)=|\Phi|.
}
\]

In the non-simply-laced types there are only two possible values:
\[
\begin{array}{c|c}
\text{type}&\chi_{\mathrm{top}}\!\left(\mathbb P\overline{\mathcal O}\right)\\
\hline
B_\ell&2\ell(\ell-1)\ \text{or}\ 2\ell^2\\
C_\ell&2\ell\ \text{or}\ 2\ell^2\\
F_4&24\ \text{or}\ 48\\
G_2&6\ \text{or}\ 12.
\end{array}
\]

For the simply laced types the common values are
\[
\ell(\ell+1)
\]
for \(A_\ell\),
\[
2\ell(\ell-1)
\]
for \(D_\ell\), and
\[
72,\ 126,\ 240
\]
for \(E_6,E_7,E_8\), respectively.

## Assumptions and scope
The base field is
\[
\mathbb C.
\]

The orbit closure
\[
\overline{\mathcal O}
\]
is a cone: scalar multiples of a nilpotent element are conjugate to it by the one-parameter subgroup furnished by a Jacobson--Morozov triple. Hence its projectivization is a closed projective subvariety of
\[
\mathbb P(\mathfrak g).
\]

The theorem is stated for simple Lie algebras. Direct sums require bookkeeping of which simple factors are active in the chosen orbit and are not included in the claim.

## Proof
Fix a Cartan subalgebra
\[
\mathfrak h\subset\mathfrak g
\]
and the root-space decomposition
\[
\mathfrak g
=
\mathfrak h
\oplus
\bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha.
\]
Each root space is one-dimensional.

Choose an integral cocharacter
\[
\lambda:\mathbb C^*\longrightarrow T
\]
of the maximal torus with Lie algebra \(\mathfrak h\) such that
\[
\langle\alpha,\lambda\rangle\neq0
\]
for every root and
\[
\langle\alpha,\lambda\rangle
\neq
\langle\beta,\lambda\rangle
\]
whenever \(\alpha\neq\beta\). Such a cocharacter exists because the cocharacter lattice is not contained in the finite union of rational hyperplanes cut out by these equalities.

The projective fixed locus of this action on
\[
\mathbb P(\mathfrak g)
\]
is therefore
\[
\mathbb P(\mathfrak h)
\sqcup
\coprod_{\alpha\in\Phi}\mathbb P(\mathfrak g_\alpha).
\]

The closure of a nilpotent orbit lies in the nilpotent cone. A nonzero element of
\[
\mathfrak h
\]
is semisimple, so
\[
\overline{\mathcal O}\cap\mathfrak h=\{0\}.
\]
Consequently no point of
\[
\mathbb P(\mathfrak h)
\]
lies in the projectivized orbit closure.

Every root vector is nilpotent. The Weyl group is transitive on the roots of any fixed length, and representatives of Weyl-group elements in the normalizer of the torus conjugate root spaces. Torus conjugation rescales each root vector. Hence all nonzero long-root vectors form one nilpotent orbit, and, when short roots exist, all nonzero short-root vectors form a second nilpotent orbit.

The standard minimal-orbit theorem says that the unique minimal nonzero nilpotent orbit is the orbit of a highest-root vector. The highest root is long. Thus every nonzero nilpotent orbit closure contains the orbit of every long-root vector.

When the root system is simply laced, this already puts every root line in
\[
\mathbb P\overline{\mathcal O}.
\]
When two root lengths occur, the short-root lines lie in
\[
\mathbb P\overline{\mathcal O}
\]
if and only if the short-root-vector orbit
\[
\mathcal O_{\mathrm{short}}
\]
is contained in
\[
\overline{\mathcal O}.
\]

Therefore the fixed locus is exactly
\[
\left(\mathbb P\overline{\mathcal O}\right)^{\mathbb C^*}
=
\coprod_{\alpha\in\Phi_{\mathrm{long}}}\mathbb P(\mathfrak g_\alpha)
\]
or, when the short-root orbit is contained,
\[
\left(\mathbb P\overline{\mathcal O}\right)^{\mathbb C^*}
=
\coprod_{\alpha\in\Phi}\mathbb P(\mathfrak g_\alpha).
\]
Every component displayed above is a point.

For any complex algebraic variety \(Y\) with an algebraic
\[
\mathbb C^*
\]
action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
Since
\[
\mathbb P\overline{\mathcal O}
\]
is projective, compactly supported and ordinary topological Euler characteristic agree. Counting the fixed root lines proves the formula.

The numerical values follow from the standard root counts:
\[
|\Phi(B_\ell)_{\mathrm{long}}|=2\ell(\ell-1),
\qquad
|\Phi(B_\ell)_{\mathrm{short}}|=2\ell,
\]
\[
|\Phi(C_\ell)_{\mathrm{long}}|=2\ell,
\qquad
|\Phi(C_\ell)_{\mathrm{short}}|=2\ell(\ell-1),
\]
and each of \(F_4\) and \(G_2\) has equally many long and short roots.

## Verification
The bundled checker constructs the classical root systems through rank \(12\), together with explicit \(F_4\) and \(G_2\) root sets.

For every tested system it checks the long-root and short-root counts and finds an integral cocharacter whose root weights are all nonzero and pairwise distinct.

It also checks the standard exceptional identities
\[
|\Phi|=\dim\mathfrak g-\operatorname{rank}\mathfrak g
\]
for \(E_6,E_7,E_8\).

These computations are regression evidence only. The theorem for all simple Lie algebras follows from the root-space fixed-point argument and the standard minimal-orbit theorem.

## Relationship to prior work
Fu studies nilpotent orbit closures as symplectic singularities and their symplectic resolutions. His archival full text records the scalar
\[
\mathbb C^*
\]
action on nilpotent orbits and the algebraic geometry of their closures.

A later archival paper of Fu studies exactly the projectivized nilpotent orbit closures as contact varieties and classifies when they admit contact resolutions. Targeted full-text searches in that paper found no occurrence of “Euler” and no fixed-point statement matching the root-line count above.

Fu and Namikawa study crepant and symplectic resolutions of nilpotent orbit closures; the published paper is classified under
\[
14E15.
\]

The standard nilpotent-orbit classification identifies the minimal orbit with the highest-root-vector orbit and, in the doubly-laced classical cases, separately records the orbit through a highest short-root vector.

The inspected literature does not state that every nonzero projectivized nilpotent orbit closure in a simply laced type has the same Euler characteristic, nor the two-value classification in the non-simply-laced types.

## Limitations
The theorem computes only ordinary Euler characteristic. It does not determine Betti numbers, intersection cohomology, mixed Hodge structure, singular strata, or whether a given non-simply-laced orbit closure contains the short-root orbit.

The final containment test for the short-root orbit can be decided from the standard closure order, but that orbit-by-orbit classification is not reproduced here.

Because the localization argument is short once the projective torus fixed locus is identified, an older unindexed or folklore statement remains a residual originality risk.

## References
Baohua Fu, *Symplectic Resolutions for Nilpotent Orbits*, arXiv:math/0205048, first submitted 6 May 2002; *Inventiones Mathematicae* 151 (2003), 167--186, DOI 10.1007/s00222-002-0260-9.

Baohua Fu, *Contact resolutions of projectivised nilpotent orbit closures*, arXiv:math/0602088, first submitted 6 February 2006.

Baohua Fu and Yoshinori Namikawa, *Uniqueness of crepant resolutions and symplectic singularities*, arXiv:math/0306091, first submitted 5 June 2003; *Annales de l'Institut Fourier* 54 (2004), 1--19, DOI 10.5802/aif.2008.

David H. Collingwood and William M. McGovern, *Nilpotent Orbits in Semisimple Lie Algebras*, Van Nostrand Reinhold, 1993.
