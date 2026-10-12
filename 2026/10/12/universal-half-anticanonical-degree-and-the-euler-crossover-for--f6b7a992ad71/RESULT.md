# Universal half-anticanonical degree and the Euler crossover for full flag varieties
## Finding
Let \(G\) be a nontrivial connected simply connected complex semisimple group, let
\[
B\subset G
\]
be a Borel subgroup, and choose a positive-root system \(\Phi^+\). Put
\[
N=|\Phi^+|=\dim_{\mathbb C}(G/B),
\qquad
\rho=\frac12\sum_{\alpha\in\Phi^+}\alpha,
\]
and let \(L_\rho\) be the homogeneous line bundle associated with the strictly dominant weight \(\rho\).

Then for every integer
\[
m\ge0
\]
one has the exact section formula
\[
\boxed{
h^0(G/B,L_\rho^{\otimes m})=(m+1)^N.
}
\]
Consequently the projective degree of the full flag variety in the \(L_\rho\)-embedding is
\[
\boxed{
\deg_{L_\rho}(G/B)=N!.
}
\]

Thus the degree of the \(\rho\)-polarized full flag variety depends only on its complex dimension and is independent of its root-system type.

On the other hand, the Schubert-cell decomposition gives
\[
\boxed{
\chi_{\mathrm{top}}(G/B)=|W|,
}
\]
where \(W\) is the Weyl group. The comparison is completely sharp:
\[
\boxed{
N!<|W|
}
\]
exactly for root systems
\[
A_1,\qquad A_1^2,\qquad A_1^3;
\]
\[
\boxed{
N!=|W|
}
\]
exactly for
\[
A_2;
\]
and
\[
\boxed{
N!>|W|
}
\]
for every other nontrivial semisimple root system.

Since
\[
K_{G/B}^{-1}\cong L_{2\rho},
\]
the line bundle \(L_\rho\) is the natural half-anticanonical polarization.

## Assumptions and scope
The group \(G\) is connected, simply connected, complex, and semisimple. Simple connectivity ensures that the weight \(\rho\) defines a homogeneous line bundle without an integrality ambiguity.

The weight \(\rho\) is strictly dominant, so \(L_\rho\) is very ample on the full flag variety \(G/B\).

The projective degree is computed with respect to this specific polarization. It is not the degree in a fundamental-weight embedding of a partial flag variety.

The result allows reducible semisimple root systems. If
\[
\Phi=\Phi_1\sqcup\cdots\sqcup\Phi_s,
\]
then
\[
N=\sum_i|\Phi_i^+|
\]
and
\[
W=W_1\times\cdots\times W_s.
\]

## Proof
Borel--Weil identifies
\[
H^0(G/B,L_{m\rho})
\]
with the irreducible \(G\)-representation of highest weight \(m\rho\). The Weyl dimension formula gives
\[
\dim H^0(G/B,L_{m\rho})
=
\prod_{\alpha\in\Phi^+}
\frac{\langle m\rho+\rho,\alpha^\vee\rangle}
{\langle \rho,\alpha^\vee\rangle}.
\]
Since
\[
m\rho+\rho=(m+1)\rho,
\]
every factor is exactly \(m+1\). There are \(N\) positive roots, hence
\[
h^0(G/B,L_\rho^{\otimes m})
=
(m+1)^N.
\]

For a projective \(N\)-fold with a very ample line bundle \(L\), the leading term of the Hilbert polynomial is
\[
\frac{\deg_L(X)}{N!}m^N.
\]
The polynomial \((m+1)^N\) has leading coefficient \(1\), so
\[
\deg_{L_\rho}(G/B)=N!.
\]

The Bruhat decomposition is
\[
G/B=\bigsqcup_{w\in W}C_w,
\]
with every \(C_w\) an affine space. Each cell therefore contributes \(1\) to the topological Euler characteristic, giving
\[
\chi_{\mathrm{top}}(G/B)=|W|.
\]

It remains to compare \(N!\) and \(|W|\). Let
\[
e_1,\ldots,e_r
\]
be the exponents of the Weyl group. The standard exponent identities are
\[
|W|=\prod_{i=1}^r(e_i+1)
\]
and
\[
N=\sum_{i=1}^r e_i.
\]
For every integer \(e\ge1\),
\[
e+1\le2^e,
\]
with equality only at \(e=1\). Hence
\[
|W|\le2^N.
\]
If \(N\ge4\), then
\[
N!>2^N,
\]
so
\[
N!>|W|.
\]

Only \(N\le3\) remains. The nontrivial semisimple root systems with at most three positive roots are:
\[
A_1,\quad A_1^2,\quad A_1^3,\quad A_2.
\]
Their pairs
\[
(N!,|W|)
\]
are respectively
\[
(1,2),\qquad(2,4),\qquad(6,8),\qquad(6,6).
\]
This gives the stated complete crossover classification.

## Verification
The bundled checker encodes the exponent lists of all irreducible finite Weyl types, including the exceptional types, and verifies
\[
|W|=\prod_i(e_i+1),
\qquad
N=\sum_i e_i,
\]
together with the claimed comparison.

It also enumerates products of low-\(N\) irreducible root systems to check that the only sub-equality cases are
\[
A_1,\ A_1^2,\ A_1^3
\]
and that the only equality case is
\[
A_2.
\]

The finite table is regression evidence only. The all-type theorem follows from the symbolic exponent inequality
\[
e+1\le2^e
\]
and
\[
N!>2^N
\]
for \(N\ge4\).

## Relationship to prior work
Brion and Lakshmibai develop homogeneous coordinate rings for ample line bundles on arbitrary flag varieties and record that regular dominant weights give very ample line bundles. Brion's flag-variety lectures give the Schubert-cell description and its Weyl-group indexing in the classical model.

The Borel--Weil theorem and Weyl dimension formula provide the representation-theoretic Hilbert-function input. The standard theory also gives
\[
K_{G/B}^{-1}\cong L_{2\rho}
\]
and
\[
\chi_{\mathrm{top}}(G/B)=|W|.
\]

The comparison made here isolates a root-system-independent degree phenomenon for the canonical half-anticanonical polarization and classifies exactly when that universal degree lies below, equals, or exceeds the cell count. Targeted searches for the \(L_\rho\) degree, the factorial formula, and its comparison with \(|W|\) did not locate this complete crossover statement.

## Limitations
The theorem concerns full flag varieties and the \(\rho\)-polarization. It does not assert root-system independence for other ample weights or for partial flag varieties.

The proof is short once Borel--Weil, Weyl's dimension formula, and the exponent identities are placed together. An older representation-theoretic source may contain the same observation under a different formulation.

No claim is made that the \(\rho\)-embedding is minimal among homogeneous projective embeddings.

## References
Michel Brion and V. Lakshmibai, *A geometric approach to Standard Monomial Theory*, arXiv:math/0111054, first submitted 6 November 2001; *Representation Theory* 7 (2003), 651--680.

Michel Brion, *Lectures on the geometry of flag varieties*, arXiv:math/0410240, first submitted 9 October 2004; in *Topics in Cohomological Studies of Algebraic Varieties*, Trends in Mathematics, Birkhauser, 2005, 33--85.
