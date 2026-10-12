# Reflection reduction for divisibility-aware integer Chebyshev lower certificates
## Finding
Let \(\rho(x)=1-x\). For a nonzero polynomial \(Q\in\mathbb Z[x]\) of degree \(d\) with positive leading coefficient, define its normalized reflection by
\[
Q^{\rho}(x)=(-1)^dQ(1-x).
\]
This operation preserves degree, positive leading coefficient, and irreducibility, and it is an involution.

Fix a finite, pairwise-distinct irreducible library \(\mathcal L=\{Q_1,\ldots,Q_J\}\) that is closed under \(Q\mapsto Q^\rho\). Use the notation of Theorem 7 of Giraudin: \(d_i=\deg Q_i\), \(a_i\) is the positive leading coefficient, \(L_i=\log(a_i)/d_i\), \(\nu_i\) is the normalized root-counting measure, \(c_i\ge0\),
\[
B=\sum_i c_i d_i\le1,
\]
\[
A_{\mu,c}(z)=U_\mu(z)-\sum_i c_i\log|Q_i(z)|,
\]
and
\[
G_i(\mu,c)=L_i(1-B+c_i d_i)+\int U_\mu\,d\nu_i-\sum_{j\ne i}c_j\int\log|Q_j|\,d\nu_i.
\]
Write
\[
V(\mu,c)=\min\left\{\inf_{x\in[0,1]}A_{\mu,c}(x),\ -\sum_i c_i\log a_i,\ \min_iG_i(\mu,c)\right\}.
\]
Whenever these displayed quantities are finite, Giraudin's theorem gives the lower certificate \(t_{\mathbb Z}([0,1])\ge \exp(V(\mu,c))\).

Then
\[
\sup_{\mu,c}V(\mu,c)
=
\sup_{\substack{\mu=\rho_*\mu\\ c_i=c_{i^\rho}}}V(\mu,c),
\]
where the suprema use the same reflection-closed library and the same constraints \(\mu\) probability, \(c_i\ge0\), and \(B\le1\). Thus reflection symmetry is a no-loss restriction for the divisibility-aware lower program, not only for the upper program.

For symmetric data,
\[
A_{\mu,c}(x)=A_{\mu,c}(1-x),\qquad G_{i^\rho}(\mu,c)=G_i(\mu,c).
\]
Consequently the continuum minimum needs only \(x\in[0,1/2]\), and one divisibility constraint per reflection orbit is sufficient. If \(w(x)=x(1-x)\) and \(\eta=w_*\mu\), then
\[
U_\mu(x)=\frac12 U_\eta(w(x)).
\]
An arbitrary finite library can first be enlarged by adjoining any missing normalized reflections with zero weight. This cannot weaken its best lower certificate; the enlarged library then admits the exact reduction above.

## Assumptions and scope
The statement concerns the lower-bound functional in Theorem 7 of arXiv:2610.00386v1. It does not assert that any fixed finite library is optimal for the integer Chebyshev problem, and it does not improve the numerical bound \(0.422228600019\) by itself.

The library is a set of pairwise-distinct irreducible integer polynomials normalized to positive leading coefficient. If a reflected polynomial already belongs to the library, it is identified with that member; otherwise it may be adjoined. The involution on indices is denoted by \(i\mapsto i^\rho\).

The equality of suprema is stated for finite-valued certificate data. Equivalently, one may interpret the formulas in the extended-real sense and discard data with value \(-\infty\), since such data cannot improve a finite certificate.

## Proof
First record the exact covariance under reflection. Let \(\mu^\rho=\rho_*\mu\), and define reflected weights by
\[
(c^\rho)_i=c_{i^\rho}.
\]
Because reflection preserves every degree and leading coefficient,
\[
B(c^\rho)=B(c).
\]
For every complex \(z\),
\[
U_{\mu^\rho}(z)=U_\mu(1-z).
\]
Also
\[
|Q_i(z)|=|Q_{i^\rho}(1-z)|.
\]
Reindexing the finite sum therefore gives
\[
A_{\mu^\rho,c^\rho}(z)=A_{\mu,c}(1-z).
\]
In particular, the first component of \(V\) is unchanged. The term at infinity is unchanged because \(a_{i^\rho}=a_i\).

The root measures transform as
\[
\nu_{i^\rho}=\rho_*\nu_i.
\]
Hence
\[
\int U_{\mu^\rho}\,d\nu_{i^\rho}=\int U_\mu\,d\nu_i.
\]
Similarly, for every pair of indices,
\[
\int\log|Q_j|\,d\nu_{i^\rho}
=
\int\log|Q_{j^\rho}|\,d\nu_i.
\]
After the substitution \(k=j^\rho\), the exclusion \(j\ne i^\rho\) becomes \(k\ne i\), and \((c^\rho)_{i^\rho}=c_i\). Thus
\[
G_{i^\rho}(\mu^\rho,c^\rho)=G_i(\mu,c).
\]
All three entries in the minimum defining \(V\) are therefore permuted or fixed, so
\[
V(\mu^\rho,c^\rho)=V(\mu,c).
\]

Next, \(V\) is concave on the convex feasible set. For fixed \(x\), \(A_{\mu,c}(x)\) is affine jointly in \((\mu,c)\), so \(\inf_x A_{\mu,c}(x)\) is concave. The term \(-\sum_i c_i\log a_i\) is affine. Each \(G_i\) is affine, so \(\min_iG_i\) is concave. Finally, the pointwise minimum of these concave functions is concave: its hypograph is the intersection of their convex hypographs.

Now average any feasible data with its reflection:
\[
\mu_s=\frac12(\mu+\mu^\rho),\qquad
c_s=\frac12(c+c^\rho).
\]
The pair \((\mu_s,c_s)\) is feasible, satisfies \(\mu_s=\rho_*\mu_s\) and \((c_s)_i=(c_s)_{i^\rho}\), and concavity plus reflection invariance gives
\[
V(\mu_s,c_s)
\ge
\frac12V(\mu,c)+\frac12V(\mu^\rho,c^\rho)
=V(\mu,c).
\]
Thus every certificate is weakly improved by a symmetric one, proving equality of the two suprema.

For symmetric data, applying the covariance identities to the same data gives
\[
A(x)=A(1-x),\qquad G_{i^\rho}=G_i.
\]
This proves the half-interval and orbit reductions.

Finally let \(w(x)=x(1-x)\), let \(\eta=w_*\mu\), and assume \(\mu=\rho_*\mu\). Since \(U_\mu(x)=U_\mu(1-x)\),
\[
2U_\mu(x)
=
\int\log\left|(x-t)(1-x-t)\right|\,d\mu(t).
\]
The elementary identity
\[
(x-t)(1-x-t)=w(x)-w(t)
\]
turns the right-hand side into \(U_\eta(w(x))\). Hence
\[
U_\mu(x)=\frac12U_\eta(w(x)).
\]

## Verification
The proof is symbolic. The accompanying standard-library script `verify.py` independently checks the normalized polynomial-reflection involution on several integer polynomials, the identity
\[
(x-t)(1-x-t)=x(1-x)-t(1-t),
\]
and the reflection covariance of \(A\), the \(G_i\), and the symmetric-potential pushforward on a non-singular finite test model. The finite replay is corroborative only; the all-library theorem is established by the argument above.

## Relationship to prior work
Giraudin's 2026 paper proves a no-loss reflection symmetrization for its upper semi-infinite program and works there in \(w=x(1-x)\). Its lower Theorem 7 is different: it introduces the indexed quantities \(G_i\) specifically to pay for the case in which an extremal integer polynomial is divisible by a library polynomial. The paper notes that the \(G_i\) are affine and develops the lower certificate, but it does not state the reflection reduction proved here for the full lower functional.

Pritsker's earlier weighted-potential treatment of the integer Chebyshev problem already exploits the symmetry of \([0,1]\) and the substitution \(x(1-x)\) in lower-bound work. The contribution here is therefore not the generic symmetry substitution. It is the exact equivariance and no-loss averaging theorem after the 2026 divisibility penalties \(G_i\) are included, together with the resulting reduction of those indexed constraints by reflection orbits.

Targeted searches of published mathematical findings and the accessible primary literature found no statement equivalent to this divisibility-aware lower-certificate reduction. The closest located results are the upper-program symmetrization in Giraudin and the older weighted-potential symmetry in Pritsker.

## Limitations
No new numerical lower bound for \(t_{\mathbb Z}([0,1])\) is claimed. The result is a structural reduction for searching for and checking certificates. It does not show that a finite library is optimal, does not remove the need to verify irreducibility and pairwise distinctness in a concrete certificate, and does not reduce non-reflection symmetries that a particular library may possess.

Because the argument is an exact convex-symmetry reduction, its mathematical value is primarily methodological: it shows that the newly explicit divisibility obstruction does not destroy the natural symmetry of the interval. An independently discovered or unindexed application of the same averaging argument to Theorem 7 remains a priority risk.

## References
1. D. Niedbala Giraudin, *New bounds for the integer Chebyshev constant of [0,1]*, arXiv:2610.00386v1, 30 September 2026. In particular, Lemma 4 and Theorem 7.
2. I. E. Pritsker, *Small polynomials with integer coefficients*, arXiv:math/0101166; Journal d'Analyse Mathématique 96 (2005), 151--190.
3. K. G. Hare and P. W. Hodges, *Applications of integer and semi-infinite programming to the integer Chebyshev problem*, Experimental Mathematics 31 (2022), 694--700.
