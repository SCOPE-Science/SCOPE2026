# Smoothness threshold for automorphism schemes of truncated polynomial algebras

## Finding

Let \(k\) be any field of characteristic \(p>0\), let \(m\ge2\), and set \(A_m=k[t]/(t^m)\). The automorphism group scheme of \(A_m\) is smooth over \(k\) if and only if \(p\nmid m\). If \(m=q=p^e\) for \(e\ge1\), its full representing scheme is

\[
\operatorname{Spec} k[c_0,c_1,c_1^{-1},c_2,\ldots,c_{q-1}]/(c_0^q).
\]

Thus the divisibility of the truncation length by the characteristic is exactly the boundary between a smooth automorphism scheme and one with an extra infinitesimal tangent direction.

## Assumptions and scope

- \(k\) is an arbitrary field of characteristic \(p>0\), and \(m\) is an integer with \(m\ge2\).
- \(A_m=k[t]/(t^m)\) is a commutative unital \(k\)-algebra.
- The automorphism group scheme represents the functor sending a commutative \(k\)-algebra \(R\) to \(\operatorname{Aut}_{R\text{-alg}}(R[t]/(t^m))\).
- The theorem concerns the full functor on possibly nonreduced base rings, not only automorphisms over fields. For the explicit coordinate-ring description, the length is restricted to a prime power \(q=p^e\).

## Proof

Write an arbitrary image of the generator as

\[
u=c_0+c_1t+\cdots+c_{m-1}t^{m-1}.
\]

The substitution defines an endomorphism precisely when \(u^m=0\); it is an automorphism when the resulting \(R\)-linear substitution map is invertible. The constant coefficient of \(u^m\) gives \(c_0^m=0\). Consequently \(c_0\) is nilpotent, and every field-valued point has \(c_0=0\). With \(c_0=0\), one has \(u=t(c_1+c_2t+\cdots+c_{m-1}t^{m-2})\), and substitution is invertible exactly when \(c_1\ne0\). Therefore the underlying topological space of the automorphism scheme has dimension \(m-1\), and its reduced scheme is \(\mathbb G_m\times\mathbb A^{m-2}\).

The tangent space at the identity is \(\operatorname{Der}_k(A_m,A_m)\). A derivation is determined by \(v=D(t)=a_0+a_1t+\cdots+a_{m-1}t^{m-1}\), subject to

\[
0=D(t^m)=m t^{m-1}v=m a_0t^{m-1}.
\]

If \(p\nmid m\), this forces \(a_0=0\), so the tangent dimension is \(m-1\). More directly, the coefficient of \(t^{m-1}\) in \(u^m\) has the form \(m c_0c_1^{m-1}+c_0^2H\), for a polynomial \(H\) in the coefficients. Since \(c_0\) is nilpotent and \(c_1\) is invertible on the automorphism scheme, when \(p\nmid m\) the factor \(m c_1^{m-1}+c_0H\) is a unit. The coefficient equation therefore forces \(c_0=0\) scheme-theoretically. In this case the full scheme is \(\mathbb G_m\times\mathbb A^{m-2}\), hence smooth.

If \(p\mid m\), the relation \(m a_0t^{m-1}=0\) imposes no restriction on \(a_0\). The tangent dimension is then \(m\), strictly greater than the scheme dimension \(m-1\); hence the automorphism scheme is not smooth.

Finally, suppose \(m=q=p^e\). In characteristic \(p\), the Frobenius identity gives

\[
u^q=\sum_{i=0}^{q-1}c_i^q t^{iq}=c_0^q,
\]

because \(t^q=0\). Thus the only equation defining substitutions is \(c_0^q=0\). The substitution is invertible exactly when \(c_1\) is a unit: modulo the nilpotent ideal \((c_0)\), its matrix in the basis \(1,t,\ldots,t^{q-1}\) is triangular with diagonal \(1,c_1,c_1^2,\ldots,c_1^{q-1}\), and invertibility lifts across a nilpotent ideal. Conversely, invertibility implies \(c_1^{q(q-1)/2}\) is a unit modulo \((c_0)\), so \(c_1\) is a unit in \(R\). This proves the displayed representing-scheme description. Its dimension is \(q-1\), while its tangent dimension is \(q\), exhibiting the non-smoothness explicitly.

## Verification

The proof uses the defining relation \(u^m=0\), the coefficient of \(t^{m-1}\), and the derivation relation \(D(t^m)=0\). The prime-power coordinate-ring formula follows from the Frobenius identity over every commutative base algebra. No finite-field enumeration or computational conjecture is used. The result does not assert a product decomposition of the group law in the prime-power case; the displayed isomorphism is an isomorphism of schemes.

## Relationship to prior work

Tziolas discusses automorphism group schemes in positive characteristic and gives an explicit description for \(k[t]/(t^p)\), including its non-smoothness, in *Topics in group schemes and surfaces in positive characteristic*, Example 3.23. The same work identifies the tangent Lie algebra of an automorphism group scheme with derivations. The present statement gives a necessary-and-sufficient smoothness criterion for every truncation length \(m\ge2\), and the full coordinate scheme for all prime-power lengths \(p^e\). The cited height-one example covers the case \(m=p\), but does not state this arbitrary-length criterion.

## Limitations

The classification is for the one-generator truncated polynomial algebra \(k[t]/(t^m)\). It does not classify the group law in the non-smooth case for arbitrary \(m\), nor does it extend to multivariable truncations or noncommutative algebras. Bounded literature searches did not establish universal novelty; a broader search may locate an equivalent formulation.

## References

1. N. Tziolas, “Topics in group schemes and surfaces in positive characteristic,” *Annali dell’Università di Ferrara* **70** (2024), 891–954. Published 16 May 2024. DOI: 10.1007/s11565-024-00514-8. See §3.4, Example 3.23, and Proposition 3.19. https://doi.org/10.1007/s11565-024-00514-8
2. P. J. Sancho de Salas, “Automorphism scheme of a finite field extension,” *Transactions of the American Mathematical Society* **352** (2000), 595–608. DOI: 10.1090/S0002-9947-99-02361-2. This concerns finite field extensions and is treated only as adjacent background, not as a result about \(k[t]/(t^m)\).
