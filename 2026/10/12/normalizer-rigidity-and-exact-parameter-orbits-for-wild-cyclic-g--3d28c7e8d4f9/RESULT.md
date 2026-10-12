# Normalizer rigidity and exact parameter orbits for wild cyclic genus-six curves

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). For each \(\lambda\in k\), let \(X_\lambda\) be the smooth projective curve with function field the compositum over \(k(z)\) of the Kummer extension \(x^3=z\) and the length-two Artin–Schreier–Witt extension
\[
\wp_2(Y_0,Y_1)=(z^{-1},\lambda z^{-1}),\qquad \wp_2=F-\mathrm{id}.
\]
Denote its canonical cyclic deck subgroup of order \(12\) by \(G_\lambda\). Then for every \(\lambda,\mu\in k\):

1. \(N_{\operatorname{Aut}_k(X_\lambda)}(G_\lambda)=G_\lambda\); in particular, an automorphism normalizing the displayed wild cyclic action is already a deck transformation.
2. The pairs \((X_\lambda,G_\lambda)\) and \((X_\mu,G_\mu)\), with cyclic subgroups unmarked by generators, are isomorphic if and only if
\[
\lambda^2+\lambda=\mu^2+\mu,
\]
 equivalently \(\mu=\lambda\) or \(\mu=\lambda+1\).

Equivalently, the **complete pair-isomorphism groupoid** has no arrows between parameters with different \(j\), and exactly \(12\) isomorphisms between any two parameters with equal \(j\): once one isomorphism is fixed, all others are obtained by composing with a unique deck transformation. The geometric isomorphism classes of these genus-six cyclic actions thus have the exact affine-line parameter \(j=\lambda^2+\lambda\), the quotient of the \(\lambda\)-line by its fixed-point-free translation \(\lambda\mapsto\lambda+1\). This statement concerns geometric classes, not a claim that the coarse line is a fine moduli space of curves without automorphisms.

## Assumptions and scope
All maps and automorphisms are over the fixed algebraically closed field \(k\); characteristic is exactly \(2\). The pair means a smooth projective curve together with a distinguished **subgroup** \(G\cong C_{12}\), not a chosen generator and not merely the underlying unmarked curve. The extension is interpreted as the smooth projective normalization of its affine function-field equations. The resulting curve has genus \(6\) for every \(\lambda\), including \(\lambda=0\). All the genus-six characteristic-two pairs with a cyclic subgroup of order \(12\) occur in this family by Kazemifard–Tafazolian, Theorem 5.8 [1].

## Proof
Put \(t=z^{-1}\) and \(f_\lambda=(t,\lambda t)\in W_2(k(t))\). In characteristic two, length-two Witt addition and inverse are
\[
(a,b)+(c,d)=(a+c,b+d+ac),\qquad -(a,b)=(a,b+a^2).
\]
In particular \(\wp_2(0,h)=(0,h^2+h)\). The class of \(f_\lambda\) has order exactly \(4\): its double is \(2f_\lambda=(0,t^2)\), equivalent modulo \(\wp_2(0,t)\) to the nonzero simple-pole class \((0,t)\). Two generators of the same cyclic quartic extension correspond to the Witt classes \([f]\) and \(-[f]\); the only units modulo four are \(\pm1\) [2, Proposition 2.4].

**Simple-pole lemma.** For \(A\in k\), \(At\in\{h^2+h:h\in k(t)\}\) if and only if \(A=0\). Indeed, if \(h\) is regular at \(t=\infty\), so is \(h^2+h\). If \(h\) has a pole there of order \(d>0\), its square-plus-itself has a pole of even order \(2d\), never a simple pole. Also, if \(\wp_2(u,v)=(0,Bt)\), the first coordinate gives \(u^2+u=0\) and hence \(u\in\{0,1\}\); in either case the second coordinate of \(\wp_2(u,v)\) equals \(v^2+v\). Consequently \((0,Bt)\) is a Witt coboundary exactly when \(B=0\).

**Base-coordinate rigidity.** The branch locus of \(X_\lambda\to\mathbf P^1_z\) comprises \(z=0\), with wild full inertia \(C_{12}\), and \(z=\infty\), with tame inertia \(C_3\) [1, Theorem 5.8]. Every isomorphism of two pairs, or every automorphism normalizing one \(G_\lambda\), descends to an automorphism of \(\mathbf P^1\) preserving the two points separately, necessarily \(z\mapsto cz\) for some \(c\in k^\times\). The unique order-three subgroup is characteristic in \(G_\lambda\), so the induced map preserves the cyclic quartic quotient, whose first Witt coordinate changes from \(t\) to \(c^{-1}t\). Up to the only generator choices \(\pm1\), the first coordinate is unchanged. Equality of the Artin–Schreier classes forces \((1+c^{-1})t=h^2+h\) for some \(h\in k(t)\); the simple-pole lemma forces \(c=1\).

**Normalizer.** If \(\phi\in N_{\operatorname{Aut}(X_\lambda)}(G_\lambda)\), the preceding argument shows its induced automorphism of the quotient \(X_\lambda/G_\lambda\cong\mathbf P^1_z\) is the identity. Hence \(\phi\in\operatorname{Aut}_{k(z)}k(X_\lambda)=G_\lambda\), proving the first assertion.

**Complete parameter comparison.** For an isomorphism \((X_\lambda,G_\lambda)\cong(X_\mu,G_\mu)\), the quotient coordinate is fixed by the preceding argument. The order-three and order-four subextensions are canonically determined as fixed fields of the unique subgroups of the indicated orders. The cubic equations coincide. The two cyclic quartic extensions are equivalent precisely when \([f_\lambda]=[f_\mu]\) or \([f_\lambda]=-[f_\mu]\) in \(W_2(k(t))/\wp_2 W_2(k(t))\). Direct Witt addition gives
\[
f_\lambda-f_\mu=(0,(\lambda+\mu)t),\qquad
f_\lambda+f_\mu=(0,(\lambda+\mu)t+t^2).
\]
The simple-pole lemma makes the first vector a coboundary exactly when \(\lambda+\mu=0\). For the second, add \(\wp_2(0,t)=(0,t^2+t)\); it is a coboundary exactly when \(\lambda+\mu+1=0\). Thus \(\mu=\lambda\) or \(\lambda+1\). Conversely either equality makes the quartic extensions isomorphic as unmarked cyclic covers of the same \(z\)-line, and adjoining the identical cubic extension gives an isomorphism of the original pairs. Finally,
\[
(\lambda^2+\lambda)-(\mu^2+\mu)=(\lambda+\mu)(\lambda+\mu+1),
\]
so the criterion is equivalent to equality of \(j\). Since the already proved normalizer identity gives exactly \(12\) automorphisms of each pair, an isomorphism set is either empty or a free transitive \(C_{12}\)-set of size \(12\). The invariant ring \(k[\lambda]^{\langle\lambda\mapsto\lambda+1\rangle}\) equals \(k[\lambda^2+\lambda]\): every polynomial reduces uniquely to \(A(j)+\lambda B(j)\), and invariance forces \(B=0\).

**Independent check of the defining genus.** The quartic cover has upper jumps \((1,2)\), lower jumps \((1,3)\) and local different exponent \(8\) at \(z=0\). After tame cubic base change its upper jumps become \((3,6)\), lower jumps \((3,9)\), and quartic different exponent \(18\). Transitivity with the cubic different exponent \(2\) gives full local different \(18+4\cdot2=26\) at zero. Infinity contributes four tame points of different exponent \(2\). Riemann–Hurwitz therefore yields \(2g-2=-2\cdot12+26+4\cdot2=10\), i.e. \(g=6\). The coprime cubic and quartic Galois extensions form \(C_3\times C_4\cong C_{12}\).

## Verification
The proof is symbolic and applies uniformly to every algebraically closed field of characteristic two and every parameter. The independent finite-field checker `verify.py` replays the Witt inverse, sums/differences, coboundary relation and the exact two-point orbit decomposition over \(\mathbf F_{16}\). Run `python3 verify.py` alongside this document; the observed output was `VERIFY_OK: Witt identities and eight two-point GF(16) parameter orbits`. This finite check does not prove the simple-pole lemma, universal equivalence, or normalizer theorem; those are proved above.

## Relationship to prior work
Kazemifard–Tafazolian [1, Theorem 5.8] prove the complete existence of the characteristic-two genus-six cyclic-twelve normal forms and explicitly do not establish uniqueness of their auxiliary parameter. Dang–Hippold [2, Proposition 2.4 and Section 3.3] give general Artin–Schreier–Witt equivalence and coefficient-space quotients, including the generator change used here, but do not compute the exact normalized one-parameter orbit or the normalizer of the cubic–quartic compositum. Timpanella [3] addresses the distinct range of cyclic orders at least \(2g+1\); the displayed order \(12=2g\) lies outside that stated range. The new result uses these ingredients but additionally establishes the rigidity of quotient scalings, all parameter identifications, and self-normalization for every member of this boundary family.

## Limitations
The conclusion is for pairs with a distinguished cyclic subgroup: it does not assert that \(\operatorname{Aut}(X_\lambda)=C_{12}\), nor classify isomorphism classes of curves after forgetting their cyclic subgroups. It describes geometric parameter orbits and their affine quotient, not stack representability or deformation theory over arbitrary non-algebraically-closed bases. An older equivalent normalizer theorem under other notation remains a bibliographic risk.

## References
[1] A. Kazemifard and S. Tafazolian, *Cyclic automorphisms beyond the canonical bound*, arXiv:2610.04702v1, 3 October 2026, Theorems 5.8 and 6.1, Section 5.3. https://arxiv.org/html/2610.04702v1

[2] H. Dang and M. Hippold, *The moduli space of cyclic covers in positive characteristic*, arXiv:2306.14711v3, Proposition 2.4 and Section 3.3. https://arxiv.org/pdf/2306.14711

[3] M. Timpanella, *Large cyclic automorphism groups and cyclic subgroups of index two in characteristic two*, arXiv:2609.34709v1, 28 September 2026. https://arxiv.org/abs/2609.34709
