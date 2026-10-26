# Absolute simplicity of the genus-three Jacobian in an explicit amoeba example

## Finding
Let \(i^2=-1\), \(P(x)=\frac14+16ix+(11-63i)x^2+16x^3-\frac14x^4\), and let \(C\) be the smooth projective normalization of the affine complex curve \(x+x^2y^2+yP(x)=0\). **The genus-three Jacobian \(J(C)\) is absolutely simple over \(\mathbb C\).** In particular it is not isogenous to a product of positive-dimensional abelian varieties and \(C\) admits no nonconstant morphism onto a curve of genus one or two.

There is a good reduction at the prime \((5,i-2)\) of \(\mathbb Z[i]\), with zeta numerator
\[
L_5(T)=1+T+9T^2+11T^3+45T^4+25T^5+125T^6.
\]
Its associated Frobenius characteristic polynomial is \(h(X)=X^6+X^5+9X^4+11X^3+45X^2+25X+125\). Its Galois group over \(\mathbb Q\) is \((C_2)^3\rtimes S_3\), the full group permuting and independently inverting the three reciprocal Frobenius pairs. This special-fiber certificate implies absolute simplicity.

## Assumptions and scope
Everything is over characteristic zero unless explicitly reduced modulo five. The smooth projective curve is identified with the smooth completion of the hyperelliptic model
\[
Y^2=P(x)^2-4x^3,
\]
obtained by taking \(Y=2x^2y+P(x)\); equivalently, with \(Q=4P\) and \(W=4Y\), \(W^2=Q(x)^2-64x^3\). The leading coefficient of the latter degree-eight polynomial is one. We choose the prime above five with \(i\mapsto2\); the conjugate prime is not claimed to have the same Frobenius polynomial.

## Proof
**Good reduction and exact Frobenius data.** Under \(i\mapsto2\pmod 5\), the polynomial \(Q\) becomes \(1+3x+4x^3+4x^4\). The resulting degree-eight polynomial \(D_5=Q^2-64x^3\) is
\[
x^8+2x^7+x^6-x^5+2x^4-x^3-x^2+x+1\quad\text{in }\mathbb F_5[x].
\]
An exact Euclidean polynomial-gcd check gives \(\gcd(D_5,D_5')=1\), so the hyperelliptic model has smooth genus-three reduction, as does its characteristic-zero generic fiber. For \(n=1,2,3\), enumerate the finite fields \(\mathbb F_{5^n}\) and count points from the quadratic-character sum, adding the two rational points at infinity. The respective counts are \(7,43,133\). Their Frobenius power sums are \((-1,-17,-7)\). Newton's identities and the functional equation give the displayed polynomial \(h\). In particular the coefficient of \(X^3\) is \(11\), prime to five, so the reduced Jacobian is ordinary.

**The full Galois group.** Put \(u_j=\alpha_j+5/\alpha_j\) for the three reciprocal pairs of roots of \(h\). Direct substitution gives
\[
h(X)=X^3g(X+5/X),\qquad g(U)=U^3+U^2-6U+1.
\]
The monic cubic \(g\) is irreducible over \(\mathbb Q\) (its only possible rational roots, \(\pm1\), are not roots), and its discriminant is the nonsquare integer \(761\); hence its splitting field \(L\) has Galois group \(S_3\). The roots above \(u_j\) are determined by \(X^2-u_jX+5\), whose quadratic discriminants are \(\delta_j=u_j^2-20\). Their product equals
\[
\prod_{j=1}^3\delta_j=g(\sqrt{20})g(-\sqrt{20})=21^2-20\cdot14^2=-7^2\cdot71.
\]
At \(71\), the cubic has factorization \(g(U)\equiv(U-34)(U^2+35U-23)\pmod{71}\), with the quadratic factor irreducible. Its discriminant \(761\) is prime to \(71\), so \(71\) is unramified in \(L\). At a prime of \(L\) above \(71\), exactly one \(\delta_j\) vanishes modulo that prime: \(34^2\equiv20\pmod{71}\) while the other two roots of \(g\) do not solve \(U^2\equiv20\pmod{71}\). The total product has \(71\)-adic valuation one, so that one \(\delta_j\) has odd valuation. Conjugating by \(S_3\) gives three distinct valuation-parity vectors, forming a basis of \((\mathbb F_2)^3\). Thus \(\delta_1,\delta_2,\delta_3\) are independent in \(L^\times/(L^\times)^2\). The splitting field of \(h\) over \(L\) consequently has Galois group \((C_2)^3\), and over \(\mathbb Q\) the full wreath-product group \((C_2)^3\rtimes S_3\).

**Absolute simplicity.** Since the Jacobian is ordinary, its six Frobenius roots cannot all have \(5\)-adic slope \(1/2\). In particular \(\alpha^2/5\) is not a root of unity for any Frobenius root \(\alpha\): otherwise every Galois conjugate would have slope \(1/2\). If two distinct Frobenius roots belonged to the same reciprocal pair and their quotient were a root of unity, this would contradict the preceding sentence. If they came from different pairs, apply an element of the full wreath-product Galois group that inverts one pair and fixes the other. The original and conjugated root-of-unity quotients would force \(\alpha^2/5\) to be a root of unity, again a contradiction. Thus no ratio of distinct Frobenius roots is a root of unity. For every \(n\ge1\), their \(n\)-th powers remain distinct and form one transitive Galois orbit, so the Frobenius characteristic polynomial over \(\mathbb F_{5^n}\) remains irreducible over \(\mathbb Q\). A nontrivial isogeny decomposition of the Jacobian over any finite extension would factor that characteristic polynomial; none exists. Therefore the reduced Jacobian is absolutely simple. An abelian subvariety of the characteristic-zero Jacobian over an algebraic closure would extend after a finite extension and specialize at a prime above \(5\) to a proper positive-dimensional abelian subvariety, contradicting the absolutely simple good reduction. Thus \(J(C)\) is absolutely simple over \(\mathbb C\).

## Verification
The complete standard-library script `verify.py` constructs \(\mathbb F_5\), \(\mathbb F_{25}\), and \(\mathbb F_{125}\) from explicit irreducible polynomials, reproduces all three counts, checks the good-reduction squarefreeness certificate, Newton identities, \(761\) discriminant, and the \(71\)-adic factorization ingredients. Run `python3 verify.py`; the expected output begins `VERIFY_OK`. The infinite absolute-simplicity assertion follows from the Galois and isogeny-theoretic argument above, not from finite enumeration alone.

## Relationship to prior work
Mounir Nisse, *Beyond Harnack Amoeba Boundaries* (arXiv:2610.15607v1, first posted 11 October 2026), Section 6, introduced the explicit genus-three curve and analyzed its Newton polygon, smoothness, genus, amoeba and contour. The present result concerns a different intrinsic invariant: the arithmetic Frobenius action on its Jacobian and the resulting absolute simplicity over \(\mathbb C\). The proof also uses standard facts on Weil polynomials, ordinary abelian varieties, the Tate isogeny theorem and specialization of abelian subvarieties. It does not rely on the paper's numerical contour identification.

## Limitations
This theorem concerns only the explicitly given genus-three curve, not every polynomial with its Newton polygon and not every contour-boundary example. The point-count certificate uses the chosen split prime \((5,i-2)\), not its conjugate. Same-source and indexed-literature comparisons did not identify an earlier absolute-simplicity result for these coefficients, but the absence of a match is not a uniqueness proof. Independent validation has not been performed.

## References
1. M. Nisse, *Beyond Harnack Amoeba Boundaries*, arXiv:2610.15607v1 (11 October 2026), especially Section 6, https://arxiv.org/abs/2610.15607.
2. J. Tate, *Endomorphisms of abelian varieties over finite fields*, Inventiones Mathematicae 2 (1966), 134–144 (standard isogeny criterion).
3. W. C. Waterhouse, *Abelian varieties over finite fields*, Annales scientifiques de l'École Normale Supérieure 2 (1969), 521–560 (ordinary reduction and finite-field isogenies).
