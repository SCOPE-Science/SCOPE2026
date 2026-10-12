# The universal Hom-associative combinations of three trialgebra products

## Finding

Let \(K\) be a field of characteristic zero and let
\[
(A,\dashv,\vdash,\perp,\alpha)
\]
be a Hom-associative trialgebra. For scalars
\[
\lambda,\mu,\nu\in K,
\]
define a bilinear product by
\[
x*y
=
\lambda(x\dashv y)
+
\mu(x\vdash y)
+
\nu(x\perp y).
\]

This product is Hom-associative for **every** Hom-associative trialgebra if and only if
\[
\boxed{
\lambda(\mu+\nu)=0,\qquad
\mu(\lambda+\nu)=0,\qquad
\nu(\lambda-\mu)=0.
}
\]

In characteristic zero, the universal coefficient locus is therefore exactly
\[
\boxed{
K(1,0,0)\ \cup\
K(0,1,0)\ \cup\
K(0,0,1)\ \cup\
K(1,1,-1).
}
\]

The first three lines are the individual trialgebra products. The fourth is the only genuinely mixed universal direction:
\[
\boxed{
x*y=x\dashv y+x\vdash y-x\perp y.
}
\]

Consequently, the all-plus formula
\[
x*y=x\dashv y+x\vdash y+x\perp y
\]
is not universally Hom-associative in characteristic zero.

This gives a direct correction to Proposition 2.6 of Mosbahi--Zahari--Basdouri. Their following Corollary 2.7, with the minus sign on \(\perp\), is the unique nontrivial mixed universal combination up to scalar multiplication.

A counterexample already occurs inside the source's own two-dimensional classification. For the displayed algebra \(TH_2^7\), with \(\alpha=\operatorname{id}\), the all-plus associator satisfies
\[
(e_1*e_2)*e_2-e_1*(e_2*e_2)
=
-2e_1\ne0.
\]

## Assumptions and scope

The field has characteristic zero, matching the source.

The theorem is a universal statement: it classifies the coefficient triples \((\lambda,\mu,\nu)\) for which the resulting product is Hom-associative on every Hom-associative trialgebra. A particular trialgebra may admit additional accidental coefficient triples.

The proof uses only the Hom-associative trialgebra identities. Multiplicativity of \(\alpha\) is compatible with the source's convention but is not needed for the associator calculation.

The counterexample \(TH_2^7\) is independently checked against all defining trialgebra identities before it is used.

## Proof

Write the Hom-associator of \(*\) as
\[
\mathcal A_*(x,y,z)
=
(x*y)*\alpha(z)-\alpha(x)*(y*z).
\]

Expand it bilinearly. Every term is a scalar multiple of one of the nine composites formed by choosing one of
\[
\dashv,\quad\vdash,\quad\perp
\]
for the inner product and one for the outer product.

Use the defining Hom-trialgebra relations to reduce these composites. Three normal forms are relevant:
\[
A=\alpha(x)\dashv(y\dashv z),
\]
\[
C=\alpha(x)\vdash(y\vdash z),
\]
and
\[
E=\alpha(x)\perp(y\vdash z).
\]

After applying the eleven trialgebra identities and collecting coefficients, the complete associator is
\[
\boxed{
\mathcal A_*
=
-\lambda(\mu+\nu)A
+
\mu(\lambda+\nu)C
+
\nu(\lambda-\mu)E.
}
\]

Therefore the three displayed scalar equations are sufficient for universal Hom-associativity.

To prove necessity, use the source's valid two-dimensional algebra \(TH_2^7\). Its nonzero products are
\[
e_1\dashv e_2=e_1,\qquad
e_2\dashv e_2=e_2,
\]
\[
e_2\vdash e_1=e_1,\qquad
e_2\vdash e_2=e_2,
\]
and
\[
e_1\perp e_1=e_1,\qquad
e_1\perp e_2=e_1,
\]
\[
e_2\perp e_1=e_1,\qquad
e_2\perp e_2=e_2,
\]
with
\[
\alpha(e_1)=e_1,\qquad
\alpha(e_2)=e_2.
\]

Direct evaluation gives
\[
\mathcal A_*(e_2,e_2,e_1)
=
\lambda(\mu+\nu)e_1,
\]
\[
\mathcal A_*(e_1,e_2,e_2)
=
-\mu(\lambda+\nu)e_1,
\]
and
\[
\mathcal A_*(e_1,e_2,e_1)
=
\nu(\lambda-\mu)e_1.
\]

Hence a coefficient triple that works for every Hom-associative trialgebra must satisfy all three scalar equations.

It remains to solve them in characteristic zero.

If two of \(\lambda,\mu,\nu\) vanish, one obtains the three coordinate axes.

Suppose at least two coefficients are nonzero. The equations then force
\[
\mu+\nu=0,
\qquad
\lambda+\nu=0,
\qquad
\lambda-\mu=0.
\]
Thus
\[
\lambda=\mu=-\nu,
\]
which is exactly the line
\[
K(1,1,-1).
\]

For the all-plus choice
\[
(\lambda,\mu,\nu)=(1,1,1),
\]
the second necessity computation gives
\[
\mathcal A_*(e_1,e_2,e_2)
=
-2e_1,
\]
so Proposition 2.6 fails over characteristic zero.

## Verification

The included exact checker performs three separate verifications.

First, it encodes the source's \(TH_2^7\) multiplication table and checks all eleven Hom-associative trialgebra identities on every basis triple.

Second, it computes the general \((\lambda,\mu,\nu)\)-associator on \(TH_2^7\) and confirms the three necessity evaluations above. It also verifies directly that the all-plus product fails and the signed product
\[
\dashv+\vdash-\perp
\]
is Hom-associative on every basis triple of the witness.

Third, it symbolically expands the universal associator in a normal-form module for the eleven defining identities and verifies the coefficient formula
\[
-\lambda(\mu+\nu)A
+
\mu(\lambda+\nu)C
+
\nu(\lambda-\mu)E.
\]

The checker returns `VERIFY_OK`.

No finite experiment is used in place of an infinite proof.

## Relationship to prior work

Mosbahi, Zahari, and Basdouri introduce Hom-associative trialgebras and, in Proposition 2.6, state that the all-plus sum of the three products is Hom-associative. Immediately afterward, Corollary 2.7 states that the signed combination
\[
\dashv+\vdash-\perp
\]
is Hom-associative.

The same paper later classifies two-dimensional Hom-associative trialgebras and provides the concrete \(TH_2^7\) algebra used above as an internal counterexample to Proposition 2.6.

The classical trialgebra literature treats an associative trialgebra as an object with three associative operations linked by mixed identities. In particular, the standard associativization construction is obtained by quotienting so that the three products are identified, rather than by simply summing the three operations. This does not imply the coefficient theorem above, but it confirms that an all-plus sum is not part of the standard trialgebra-to-associative-algebra mechanism.

Focused searches for the exact all-plus formula, the signed formula, linear combinations of the three trialgebra products, and a correction to Proposition 2.6 did not locate the universal coefficient classification proved here.

## Limitations

The theorem classifies universal scalar linear combinations only. It does not classify nonlinear constructions from the three products.

In characteristic \(2\), the signed line and the all-plus line coincide, so the characteristic-zero correction should not be transplanted verbatim to that boundary case.

A later or unindexed author correction may exist.

Failed searches do not prove novelty.

## References

1. B. Mosbahi, A. Zahari, and I. Basdouri, “Classification, \(\alpha\)-Inner Derivations and \(\alpha\)-Centroids of Finite-Dimensional Complex Hom-Trialgebras,” arXiv:2305.00471v1, first public 30 April 2023. MSC 2020: 17A30, 17A32, 16D20, 16W25, 17B63.
2. J. M. Casas, “Trialgebras and Leibniz 3-Algebras,” *Boletín de la Sociedad Matemática Mexicana* (3) 12 (2006), 165–178.
