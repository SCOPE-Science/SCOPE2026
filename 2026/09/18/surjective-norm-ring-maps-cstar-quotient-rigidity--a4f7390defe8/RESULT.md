# Surjective norm-ring maps between unital C*-algebras factor through C*-quotients

## Statement

Let \(A\) and \(B\) be nonzero unital C*-algebras and let \(T:A\to B\) be **surjective**. Assume that for every \(a,b\in A\),
\[
\|T(a+b)\|=\|T(a)+T(b)\|,\qquad
\|T(ab)\|=\|T(a)T(b)\|,
\qquad T(a^*)=T(a)^*.
\tag{1}
\]
Then there are uniquely determined objects

- a central symmetry \(u\in Z(B)\), namely \(u=T(1_A)\), and
- a surjective real *-homomorphism \(\Phi:A\to B\), namely \(\Phi=uT\),

such that
\[
T(a)=u\Phi(a)\qquad(a\in A).
\tag{2}
\]
Moreover,
\[
I:=\ker T=\ker\Phi
\]
is a closed two-sided *-ideal of \(A\), and the induced map
\[
\widehat\Phi:A/I\longrightarrow B,
\qquad \widehat\Phi(a+I)=\Phi(a),
\]
is a real *-isomorphism. In particular,
\[
\boxed{\ \|T(a)\|=\|a+I\|_{A/I}=\operatorname{dist}(a,I)\quad(a\in A).\ }
\tag{3}
\]
Thus the only possible failure of injectivity is passage to a C*-quotient.

Conversely, if \(I\triangleleft A\) is a closed two-sided *-ideal, \(\Psi:A/I\to B\) is a real *-isomorphism, and \(u\in Z(B)\) is a central symmetry, then
\[
T(a)=u\Psi(a+I)
\tag{4}
\]
is a surjection satisfying (1). Hence (2)--(4) give an exact classification.

A useful immediate corollary is that if \(A\) is simple, every surjection satisfying (1) is automatically bijective and therefore falls back to the isomorphism theorem of Matsuzaki.

## Context

Matsuzaki proved in arXiv:2609.18121 (submitted 16 September 2026) that a **bijection** satisfying (1) has the form \(u\Phi\), where \(u\) is a central symmetry and \(\Phi\) is a real *-isomorphism. The proof explicitly obtains additivity from surjectivity via Tabor's Fischer--Muszely theorem. The argument for centrality later invokes injectivity at one specific point: from \(T(a^2)=0\), it concludes \(a^2=0\). The observation below removes that use of injectivity and shows that the remaining noninjectivity is exactly a quotient kernel.

The extension is strict. For example,
\[
T:C([0,1])\to\mathbb C,\qquad T(f)=f(0),
\]
is surjective and noninjective, yet satisfies all three identities in (1). More generally, every quotient *-homomorphism \(A\to A/I\) is an example.

## Proof

### 1. Additivity and the symmetry \(u=T(1_A)\)

By Tabor's Corollary 1 for the Fischer--Muszely equation, surjectivity together with the first identity in (1), applied to the additive group \((A,+)\), implies that \(T\) is additive. Hence \(T(0)=0\) and \(T(ra)=rT(a)\) for rational \(r\).

Set \(u=T(1_A)\). Involution preservation gives \(u=u^*\). For every \(x\in B\), choose \(a\in A\) with \(T(a)=x\). Then the product-norm identity gives
\[
\|ux\|=\|T(1_A)T(a)\|=\|T(a)\|=\|x\|.
\tag{5}
\]
Thus left multiplication by \(u\) is an isometry. Matsuzaki's functional-calculus argument proving Lemma 2.1 uses only this surjectivity statement and shows that \(\sigma(u)\subset\{-1,1\}\). Therefore
\[
u=u^*,\qquad u^2=1_B.
\tag{6}
\]

### 2. Centrality without injectivity

Put
\[
p=\frac{1_B+u}{2},\qquad q=\frac{1_B-u}{2}.
\]
These are orthogonal projections. Let \(x\in pBq\). Then \(x^2=0\), \(ux=x\), and \(xu=-x\). By surjectivity choose \(a\in A\) with \(T(a)=x\). The product-norm identity yields
\[
\|T(a^2)\|=\|T(a)^2\|=\|x^2\|=0,
\]
so \(T(a^2)=0\). Injectivity is not needed: additivity already gives
\[
T(1_A-a^2)=u.
\tag{7}
\]
Using (1), additivity, (6), and (7),
\[
\begin{aligned}
1
&=\|u\|
 =\|T(1_A-a^2)\|\\
&=\|T((1_A+a)(1_A-a))\|\\
&=\|T(1_A+a)T(1_A-a)\|\\
&=\|(u+x)(u-x)\|
 =\|1_B-2x\|.
\end{aligned}
\tag{8}
\]
Replacing \(a\) by \(-a\) gives \(\|1_B+2x\|=1\). Hence the positive elements
\[
(1_B\pm2x)(1_B\pm2x)^*
\]
have norm at most one and therefore are at most \(1_B\). Adding the two inequalities gives
\[
2\,1_B+8xx^*\le 2\,1_B,
\]
so \(x=0\). Thus \(pBq=\{0\}\); taking adjoints also gives \(qBp=\{0\}\). Consequently \(p\), and hence \(u=2p-1_B\), is central.

### 3. Normalize and obtain automatic boundedness

Define
\[
\Phi(a)=uT(a).
\tag{9}
\]
Since \(u\) is a central symmetry, \(\Phi\) is surjective and additive, satisfies
\[
\Phi(1_A)=1_B,\qquad \Phi(a^*)=\Phi(a)^*,
\tag{10}
\]
and retains the product-norm identity
\[
\|\Phi(ab)\|=\|\Phi(a)\Phi(b)\|.
\tag{11}
\]

The positivity argument in Matsuzaki's Lemma 3.1 does not need injectivity. For completeness, if \(a=b^2\ge0\), choose an integer \(k\ge\|\Phi(b)\|\), put \(c=b/k\), and note that \(\Phi(c)\) is self-adjoint with norm at most one. From (10)--(11),
\[
\|1_B-\Phi(c^2)\|
=\|\Phi(1_A-c^2)\|
=\|\Phi(1_A-c)\Phi(1_A+c)\|
=\|1_B-\Phi(c)^2\|\le1.
\]
Since \(\Phi(c^2)\) is self-adjoint, its spectrum is contained in \([0,2]\), hence \(\Phi(c^2)\ge0\), and therefore \(\Phi(a)\ge0\). Thus \(\Phi\) is positive on \(A_+\).

It follows exactly as in Matsuzaki's Lemma 3.2 that for every self-adjoint \(h\in A\),
\[
\|\Phi(h)\|\le\|h\|.
\tag{12}
\]
For arbitrary \(a\in A\), the C*-identity, (10), (11), and (12) now give the global estimate
\[
\begin{aligned}
\|\Phi(a)\|^2
&=\|\Phi(a)^*\Phi(a)\|
 =\|\Phi(a^*)\Phi(a)\|\\
&=\|\Phi(a^*a)\|
\le\|a^*a\|
=\|a\|^2.
\end{aligned}
\tag{13}
\]
Hence \(\Phi\) is contractive. A continuous additive map between real Banach spaces is real-linear, so \(\Phi\) is a bounded real-linear surjection.

### 4. The kernel is a C*-ideal

Let
\[
I=\ker\Phi.
\]
Equation (13) makes \(I\) closed. If \(k\in I\) and \(a\in A\), then (11) gives
\[
\|\Phi(ak)\|=\|\Phi(a)\Phi(k)\|=0,
\qquad
\|\Phi(ka)\|=0,
\]
so \(ak,ka\in I\). Also (10) gives \(k^*\in I\). Moreover, for \(\lambda\in\mathbb C\), \(\lambda k=(\lambda1_A)k\in I\), so \(I\) is complex-linear. Thus \(I\) is a closed two-sided *-ideal; in particular it is a C*-ideal. Since multiplication by \(u\) is invertible,
\[
I=\ker T.
\tag{14}
\]

### 5. Pass to the quotient and recover multiplication

The induced map
\[
\widehat\Phi:A/I\to B,
\qquad \widehat\Phi(a+I)=\Phi(a),
\]
is a bijection. It is additive, unital, involution-preserving, and satisfies
\[
\|\widehat\Phi(xy)\|=\|\widehat\Phi(x)\widehat\Phi(y)\|.
\]
Because it is additive, it also automatically satisfies the sum-norm identity from (1). Thus \(\widehat\Phi\) satisfies all hypotheses of Matsuzaki's bijective theorem.

That theorem gives
\[
\widehat\Phi=v\Psi
\]
for a central symmetry \(v\in B\) and a real *-isomorphism \(\Psi:A/I\to B\). But \(\widehat\Phi(1_A+I)=1_B\), while \(\Psi\) is unital, so \(v=1_B\). Hence
\[
\widehat\Phi=\Psi
\]
is itself a real *-isomorphism. Consequently \(\Phi=\widehat\Phi\circ q\), where \(q:A\to A/I\) is the quotient map, is a surjective real *-homomorphism.

A real *-isomorphism between C*-algebras is isometric, and \(u\) is unitary. Therefore
\[
\|T(a)\|=\|\Phi(a)\|=\|a+I\|_{A/I},
\]
which is (3).

### 6. Converse and uniqueness

Conversely, let \(I\triangleleft A\) be closed, let \(\Psi:A/I\to B\) be a real *-isomorphism, and let \(u\in Z(B)\) be a central symmetry. Define \(T\) by (4). Surjectivity is immediate. Additivity gives the first identity in (1). Since \(u^2=1_B\) and \(u\) is central,
\[
T(a)T(b)=\Psi(a+I)\Psi(b+I)=\Psi(ab+I),
\]
whereas \(T(ab)=u\Psi(ab+I)\); multiplication by \(u\) preserves norm, so the product-norm identity follows. Involution preservation follows from centrality and \(u=u^*\).

Finally, \(u=T(1_A)\) is forced, then \(\Phi=uT\) is forced, and \(I=\ker T\) is forced. This proves uniqueness of the factorization data.

## Consequences

1. **Simple-domain collapse.** If \(A\) is simple, then \(I=0\), because \(B\ne0\) and \(T\) is surjective. Therefore \(T\) is automatically bijective.
2. **Metric quotient identity.** The map is automatically contractive and satisfies the exact quotient formula (3); equivalently, all norm loss is precisely the distance to \(\ker T\).
3. **Sharp role of injectivity.** Injectivity is not required for centrality, positivity, boundedness, or multiplicativity after quotienting. It is equivalent here to the single condition \(I=0\).

## Limitations

This result still assumes surjectivity, which is used essentially to invoke Tabor's additivity theorem and to prove that \(T(1_A)\) acts isometrically on all of \(B\). No classification is claimed for nonsurjective maps or approximate versions of the three identities. The result relies on Matsuzaki's bijective theorem after passage to the quotient; it is therefore a strict extension of that theorem rather than an alternative independent proof of its bijective case.

Originality is claimed only to the best of our knowledge. The current arXiv version of Matsuzaki's paper states the theorem for bijections and contains no quotient or kernel formulation. Targeted searches for surjective/epimorphic norm-ring maps, quotient formulations, central-symmetry factorizations, and real *-epimorphisms did not locate this surjective classification. Older preserver literature is broad, so an equivalent result under different terminology remains the main residual originality risk.

## References

1. I. Matsuzaki, *Involution-preserving ring isomorphisms in norm between unital C*-algebras*, arXiv:2609.18121v1 (2026). https://arxiv.org/abs/2609.18121
2. J. Tabor, *Stability of the Fischer--Muszely functional equation*, Publ. Math. Debrecen 62 (2003), 205--211, DOI: 10.5486/PMD.2003.2725. https://doi.org/10.5486/PMD.2003.2725
3. N. Shibata, I. Matsuzaki, and T. Miura, *Ring isomorphisms in norm between Banach algebras of continuous functions*, arXiv:2608.03426 (2026). https://arxiv.org/abs/2608.03426
