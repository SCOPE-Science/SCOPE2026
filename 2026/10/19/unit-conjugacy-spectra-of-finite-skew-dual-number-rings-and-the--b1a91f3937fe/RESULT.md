# Unit-conjugacy spectra of finite skew dual-number rings and the Frobenius-twist ambiguity

## Finding
Let \(q=p^f\), let \(F=\mathbb F_q\), and choose \(0\le k<f\). Put \(\sigma(a)=a^{p^k}\) and \(q_0=p^{\gcd(f,k)}\), where \(\gcd(f,0)=f\). For the skew dual-number ring
\[
R_\sigma=F[\varepsilon;\sigma]/(\varepsilon^2),\qquad \varepsilon a=\sigma(a)\varepsilon,
\]
unit conjugation on the \(q^2\) elements has the following **complete conjugacy-size distribution**, expressed as numbers of distinct classes:
\[
\begin{array}{c|c}
\text{orbit size}&\text{number of orbits}\\\hline
1&q_0\\
(q-1)/(q_0-1)&q_0(q_0-1)\\
q&q-q_0
\end{array}
\]
Rows with equal orbit size must be added. In particular the class count is \(q+q_0^2-q_0\), and at fixed \(q\) the spectrum determines precisely \(q_0\), not necessarily \(\sigma\).

Two rings of this family over a fixed finite field are isomorphic precisely when their defining field automorphisms agree, and anti-isomorphic precisely when these automorphisms are inverse. Nevertheless every ring in the family has the same nonzero zero-divisor graph \(K_{q-1}\). The commuting probability is
\[
\operatorname{cp}(R_\sigma)=\frac1q+\frac{(q-1)q_0^2}{q^3}.
\]
For \(q=32\), the twists \(\sigma(a)=a^2\) and \(\tau(a)=a^4\) are neither equal nor inverse. Their non-(anti)isomorphic rings nevertheless each have two conjugacy classes of size \(1\), two of size \(31\), and thirty of size \(32\); their commuting probabilities and zero-divisor graphs coincide.

## Assumptions and scope
Here all rings are associative and unital. For \(k=0\) the ring is the ordinary commutative dual-number ring and every element has a singleton conjugacy orbit. The theorem includes this case. The action is **inner conjugation by units on all elements**; it is not skew-polynomial evaluation conjugacy, conjugacy solely on units, or additive translation equivalence.

## Proof
Write an element as \((a,b)=a+b\varepsilon\). The multiplication is
\[
(a,b)(c,d)=(ac,ad+b\sigma(c)).
\]
The Jacobson radical is \(J=F\varepsilon\) and \(J^2=0\); an element is a unit exactly when its constant coefficient is nonzero. For \(u=(c,d)\), \(c\ne0\), direct multiplication with its inverse yields
\[
u(a,b)u^{-1}=\left(a,\frac{cb+d(\sigma(a)-a)}{\sigma(c)}\right).
\]
If \(\sigma(a)\ne a\), letting \(d\) range over \(F\) makes the second coordinate arbitrary, so the \(q\) elements with the same \(a\) constitute a single orbit. There are \(q-q_0\) such values of \(a\). If \(\sigma(a)=a\), the second coordinate instead changes by multiplication with \(c/\sigma(c)\). The kernel of \(F^\times\to F^\times\), \(c\mapsto c/\sigma(c)\), is \(F_0^\times\) of size \(q_0-1\); hence its image has size \((q-1)/(q_0-1)\). Each of the \(q_0\) fixed values of \(a\) gives one singleton at \(b=0\), and \(q_0-1\) nonzero cosets of this image. These exhaust all \(q^2\) elements, proving the distribution and count.

Suppose \(\Phi:R_\sigma\to R_\tau\) is a ring isomorphism. It preserves \(J\), and induces some field automorphism \(\rho:F\to F\) on \(R/J\). The one-dimensional left \(F\)-space \(J\) is carried to itself, with \(\Phi(\varepsilon)=u\varepsilon\), \(u\ne0\). Applying \(\Phi\) to \(\varepsilon a=\sigma(a)\varepsilon\) and discarding radical terms (they vanish because \(J^2=0\)) gives \(\tau(\rho(a))=\rho(\sigma(a))\) for all \(a\). All finite-field automorphisms commute, so \(\tau=\sigma\). The converse is immediate. The map \((a,b)\mapsto(a,\sigma^{-1}(b))\) is explicitly an anti-isomorphism from \(R_\sigma\) to \(R_{\sigma^{-1}}\); combining this fact with the isomorphism criterion proves the anti-isomorphism classification.

Every nonzero zero divisor lies in \(J\), because elements outside \(J\) are units. Distinct nonzero elements of \(J\) annihilate each other, producing \(K_{q-1}\). The center consists of the \(q_0\) elements \((a,0)\) with \(a\in F_0\), except in the identity case when the whole ring is central; the formula for centralizers below covers both cases via a direct count. The commuting equation is
\[
b(\sigma(c)-c)=d(\sigma(a)-a).
\]
For the pair \((\sigma(a)-a,\sigma(c)-c)=(0,0)\), there are \(q_0^2 q^2\) choices of \((a,b,c,d)\). Every other pair of constant terms yields a nonzero linear equation in \((b,d)\) and has exactly \(q\) solutions. Thus the total number of commuting ordered pairs is \(q_0^2q^2+(q^2-q_0^2)q=q^3+(q-1)q q_0^2\). Division by \(q^4\) proves the probability formula. For \(q=32\), the field automorphism group is cyclic of order five, and the exponents \(1\) and \(2\) are neither equal nor additive negatives modulo five; both have fixed field \(\mathbb F_2\), proving the stated collision.

## Verification
The standalone `verify.py` builds finite fields as polynomial quotients and exhaustively constructs unit-conjugacy orbits for all elements of selected skew dual-number rings. It independently checks exact commuting-pair counts and square-zero multiplication. Execute `python verify.py` with Python 3; no external libraries are needed. Configurations checked are \(q=4,8,9,16,25\), with all nonidentity Frobenius twists at these field orders (eight cases). The general proof is symbolic and does not extrapolate from this finite test set. The \(q=32\) example follows algebraically from the order-five Galois group, rather than an exhaustive million-pair computation.

## Relationship to prior work
Kinyon, *Rings with Finitely Many Zero Divisors* (2026), motivates small-zero-divisor phenomena in finite noncommutative rings; this work does not assert novelty of the observation that the present rings have \(q-1\) nonzero zero divisors. Baumbaugh and Manganiello, *Matroidal Root Structure of Skew Polynomials over Finite Fields* (2017), analyze \(\sigma\)-conjugacy of finite-field elements and the multiplicative quotient \(c/\sigma(c)\), which supplies an already-known ingredient of one orbit sector. Here the additional radical-unit translations, the complete **inner** conjugacy distribution of the finite quotient ring, and the isomorphism/anti-isomorphism ambiguity are the distinct claims. Dutta, Basnet, and Nath, *Commuting probabilities of \(n\)-centralizer finite rings* (2018), covers broad commuting-probability constraints; the probability formula is offered as a consequence, not an asserted first derivation of a general commuting bound.

## Limitations
The family has a one-dimensional square-zero radical as a left vector space over its residue field; the theorem does not classify all finite local rings with this cardinality, nor all groups of units up to abstract isomorphism. The conjugacy spectrum forgets the automorphism exponent beyond its fixed-field order. Publication overlap outside inspected sources, including equivalent affine-conjugacy formulations under different terminology, has not been excluded exhaustively. No independent audit has been conducted.

## References
- M. Kinyon, *Rings with Finitely Many Zero Divisors*, arXiv:2604.23423 (first posted April 25, 2026).
- L. Baumbaugh and F. Manganiello, *Matroidal Root Structure of Skew Polynomials over Finite Fields*, arXiv:1706.04283 (2017).
- S. Dutta, A. Basnet and R. Nath, *Commuting probabilities of \(n\)-centralizer finite rings*, arXiv:1803.04111 (2018).
