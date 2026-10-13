# Exact retractions of the multiplicative monoid modulo an odd prime power
## Finding
Let \(p\) be an odd prime and \(e\ge2\). Write
\[
M_{p,e}=(\mathbb Z/p^e\mathbb Z,\cdot),\qquad
N=p^{e-1}(p-1),\qquad N_-=p^{e-2}(p-1).
\]
Then the number \(R(p,e)\) of idempotent monoid endomorphisms of \(M_{p,e}\), equivalently retractions onto their images, is
\[
R(p,e)=1+2^{\omega(N)}+
\prod_{\ell\mid N}\bigl(1+\ell^{\nu_\ell(N_-)}\bigr),
\]
where the product is over the distinct prime divisors of \(N\).

More precisely, these idempotents are exactly the following three disjoint types.

1. The constant-one endomorphism.
2. For every residue \(t\pmod N\) with \(t^2\equiv t\pmod N\), the zero-collapse map that sends every nonunit to \(0\) and every unit \(b\) to \(b^t\).
3. For every such \(t\) and every \(r\in(\mathbb Z/p^{e-1}\mathbb Z)^\times\) satisfying \(r^t=1\), the valuation-preserving map
\[
p^u b\longmapsto p^u r^u b^t\pmod{p^e}
\]
for \(0\le u<e\) and unit \(b\), together with \(0\mapsto0\).

For example,
\[
R(3,2)=11,\qquad R(3,3)=17,\qquad R(5,2)=15,\qquad R(7,2)=33.
\]

## Assumptions and scope
The monoid operation is multiplication modulo \(p^e\), and endomorphisms preserve the identity. The result is restricted to odd primes and \(e\ge2\). The recent classification of Atalaye, Baker, and Marques gives every endomorphism as either the constant-one map or a map of the form
\[
\psi_{r,\phi,v}(p^u b)=p^{uv}r^u\phi(b),
\]
with the usual truncation to \(0\) once the valuation reaches \(e\). For odd \(p\), the unit group is cyclic of order \(N\), so \(\phi\) is uniquely a power map \(b\mapsto b^t\) with \(t\pmod N\).

## Proof
Take a nonconstant endomorphism \(\psi=\psi_{r,t,v}\) from the cited classification. Its restriction to the unit group is \(b\mapsto b^t\). If \(\psi\) is idempotent under composition, then the unit restriction is idempotent, hence
\[
t^2\equiv t\pmod N.
\]

Consider the image of \(p\). If \(v<e\), then \(\psi(p)\) has \(p\)-adic valuation \(v\), whereas \(\psi^2(p)\) has valuation \(v^2\) unless it has already reached the zero class. Equality therefore forces \(v=1\). If \(v\ge e\), all nonunits are sent to \(0\), and every such presentation gives the same zero-collapse map. Consequently there are only two nonconstant idempotent valuation behaviors: \(v=1\) and total collapse of positive valuation.

For the collapse type, the sole condition is \(t^2\equiv t\pmod N\). By the Chinese remainder theorem an idempotent residue modulo \(N\) is obtained independently by choosing \(0\) or \(1\) modulo each prime-power divisor of \(N\). Hence there are
\[
2^{\omega(N)}
\]
collapse maps.

For the valuation-preserving type \(v=1\), one has \(\psi(p)=pr\). Applying \(\psi\) once more gives
\[
\psi^2(p)=p\,r^{t+1}.
\]
Thus \(\psi^2(p)=\psi(p)\) if and only if
\[
r^t\equiv1\pmod{p^{e-1}}.
\]
Together with idempotence on units this is sufficient, because \(p\) and the units multiplicatively generate every nonzero residue class. The group \((\mathbb Z/p^{e-1}\mathbb Z)^\times\) is cyclic of order \(N_-\), so for a fixed \(t\) the number of admissible \(r\) is
\[
\gcd(t,N_-).
\]

It remains to sum this quantity over the idempotent residues \(t\pmod N\). Write the prime-power factorization of \(N\). For each distinct prime \(\ell\mid N\), an idempotent \(t\) chooses either \(t\equiv0\) or \(t\equiv1\) modulo the full \(\ell\)-primary factor. In \(\gcd(t,N_-)\), the choice \(0\) contributes \(\ell^{\nu_\ell(N_-)}\), while the choice \(1\) contributes \(1\). Therefore
\[
\sum_{t^2\equiv t\ (\mathrm{mod}\ N)}\gcd(t,N_-)
=
\prod_{\ell\mid N}\bigl(1+\ell^{\nu_\ell(N_-)}\bigr).
\]
Adding the constant-one map and the collapse maps proves the formula.

## Verification
A standalone checker is included as `check_retractions.py`. For the moduli \(9\), \(27\), \(25\), and \(49\), it enumerates all monoid endomorphisms directly from possible images of a primitive unit generator and of \(p\), verifies multiplicativity on the complete finite monoid, tests composition-idempotence, and compares the resulting count with the closed formula. The output ends with `CHECK_OK`.

The finite computation is a cross-check only. The formula for all odd primes and all \(e\ge2\) follows from the symbolic proof above.

## Relationship to prior work
Atalaye, Baker, and Marques classify all homomorphisms between multiplicative monoids modulo prime powers and specialize their result to the full endomorphism set. Their paper also studies a pointwise product on morphisms. The inspected text does not classify idempotents under composition, retractions, or retract images. The earlier Atalaye--Baker--Marques paper treats automorphisms of these monoids; invertible endomorphisms do not contain the noninvertible retractions counted here.

The present statement is therefore a composition-theoretic refinement of the new endomorphism classification: it identifies every retraction and gives a closed exact count.

## Limitations
The proof uses cyclicity of the unit group for odd prime powers and does not claim the same formula for powers of \(2\). It also does not classify isomorphism types of the retract images, only the retractions themselves.

A 2026 thesis by Atalaye on the multiplicative structure of \(\mathbb Z/n\mathbb Z\) is cited by the motivating paper but its full text was not available in the inspected sources. It remains a residual originality risk for an independently stated retraction classification. No accessible searched source was found that states the formula above.

## References
1. J. Atalaye, L. Baker, and S. Marques, “Prime-Power Multiplicative Modular Monoid Morphisms,” arXiv:2610.02393v1, 2026. In particular Proposition 3.1 and Corollary 3.2.
2. J. Atalaye, L. Baker, and S. Marques, “On the automorphism group of the monoid of the integers modulo a prime power,” arXiv:2408.06278v2, 2024.
