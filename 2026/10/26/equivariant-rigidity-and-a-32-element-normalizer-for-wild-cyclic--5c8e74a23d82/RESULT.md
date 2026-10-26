# Equivariant rigidity and a 32-element normalizer for wild cyclic-quartic genus-two covers

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). For every \(\lambda\in k^\times\), let \(C_\lambda\) be the smooth projective curve with function field defined by the length-two Artin–Schreier–Witt extension
\[
\wp_2(y_0,y_1)=(x,\lambda x^3),\qquad \wp_2=F-1,
\]
and let \(G_\lambda\cong\mathbb Z/4\mathbb Z\) denote the deck group. The pair \((C_\lambda,G_\lambda)\) is marked by a **subgroup**, not by a choice of generator.

**Theorem.** For \(\lambda,\mu\in k^\times\), the marked pairs \((C_\lambda,G_\lambda)\) and \((C_\mu,G_\mu)\) are isomorphic if and only if \(\lambda=\mu\). Further, for every \(\lambda\ne0\), with geometric normalizer and centralizer taken inside \(\operatorname{Aut}_k(C_\lambda)\),
\[
|N(G_\lambda)|=32,\qquad |C(G_\lambda)|=16,\qquad
N(G_\lambda)/G_\lambda\cong(\mathbb Z/2\mathbb Z)^3.
\]
The conjugation character \(N(G_\lambda)\to\operatorname{Aut}(G_\lambda)\cong\mathbb Z/2\mathbb Z\) is surjective. In particular, \(\lambda\) is a complete **equivariant** isomorphism parameter for the cyclic-order-four normal forms in the classification of Kazemifard–Tafazolian.

## Assumptions and scope
The result concerns geometric isomorphisms of pairs, i.e. a curve isomorphism carrying the specified order-four subgroup onto the specified subgroup. It does not classify the curves after **forgetting** the subgroup. All orders refer to abstract groups of geometric automorphisms, not automorphism group schemes.

The quotient \(C_\lambda/G_\lambda\cong\mathbb P^1_k\) has a unique branch point, at \(x=\infty\), with upper jumps \(1\) and \(3\). For the cyclic-order-four extension, the corresponding lower jumps are \(1,5\), giving different exponent \(3(2)+1(4)=10\). Riemann–Hurwitz yields \(2g(C_\lambda)-2=-8+10=2\), hence \(g(C_\lambda)=2\). The base curve and upper jumps also follow from the cited classification.

## Proof
We use the Witt addition convention, in characteristic two,
\[
(a,b)+(c,d)=(a+c,b+d+ac),\quad -(a,b)=(a,b+a^2).
\]
Two representatives give the same cyclic-order-four cover with the same generator if they differ by a length-two Witt coboundary \(\wp_2(h_0,h_1)\); changing the generator acts by the only other unit, namely inversion.

**1. Base transformations.** Any isomorphism of the marked pairs descends to the two projective-line quotients. The unique branch point must be fixed, so the induced rational coordinate change is \(x\mapsto\alpha x+\beta\), with \(\alpha\ne0\). The first Witt-coordinate class must be the class of \(x\), regardless of whether the deck generator is inverted. Thus \((\alpha+1)x+\beta=h_0^2+h_0\) for some \(h_0\in k(x)\). A rational Artin–Schreier coboundary with a pole has even pole order. Hence a degree-one polynomial cannot be such a coboundary: necessarily \(\alpha=1\). As \(k\) is algebraically closed, constants are Artin–Schreier coboundaries.

**2. Rigidity of the cubic coefficient.** Having fixed \(\alpha=1\), the first-coordinate correcting cochain \(h_0\) is constant, since \(h_0^2+h_0\) is constant. Witt addition of a constant correction to a first coordinate of degree one changes the second coordinate only by a polynomial of degree at most one, besides constants. The remaining correction \(h_1^2+h_1\) cannot have finite poles if it relates two polynomial second-coordinate representatives, so \(h_1\in k[x]\). Moreover, \(\deg h_1\ge2\) would introduce a term of degree \(2\deg h_1\ge4\), impossible between cubic representatives. Thus \(\deg h_1\le1\), changing only quadratic and lower coefficients. Inverting the generator also changes the second coordinate only by \(x^2\). It follows that the coefficient of \(x^3\) is invariant, proving \(\lambda=\mu\). The converse follows from the identical normal form.

**3. Explicit translation obstruction.** Pulling back the representative by \(x\mapsto x+\beta\) and correcting its first Witt coordinate by the constant class \(\beta\) gives, up to a removable constant second coordinate,
\[
(x,\lambda x^3+\lambda\beta x^2+(\lambda\beta^2+\beta)x).
\]
The extra linear term \(\beta x\) is the Witt cross term; omitting it would give an incorrect normalizer count. Let \(s\in k\) be the unique square root satisfying \(s^2=\lambda\beta\). Addition of the coboundary \(\wp_2(0,sx)=(0,s^2x^2+sx)\) removes the quadratic term. Thus the translated cover is represented by
\[
(x,\lambda x^3+T_\lambda(\beta)x),\qquad
T_\lambda(\beta)=\lambda\beta^2+\beta+s,\quad s^2=\lambda\beta.
\]
On the other hand, the inverse of \((x,\lambda x^3)\) is \((x,\lambda x^3+x^2)\), which is cohomologous, by \(\wp_2(0,x)=(0,x^2+x)\), to \((x,\lambda x^3+x)\). By the degree argument in step 2, two normalized representatives with fixed cubic coefficient and linear coefficients differing by \(c\) are cohomologous precisely when \(c=0\): if \(h_1=a x+b\), its quadratic coefficient is \(a^2\), so preserving the absent quadratic term forces \(a=0\). Therefore the base translation \(\beta\) lifts to a normalizing automorphism exactly when \(T_\lambda(\beta)\in\{0,1\}\), and it centralizes the deck group exactly when \(T_\lambda(\beta)=0\).

**4. Counting the normalizer.** Substitute \(\beta=s^2/\lambda\). Then
\[
T_\lambda(\beta)=\lambda^{-1}\bigl(s^4+s^2+\lambda s\bigr).
\]
The additive polynomial \(Q_\lambda(s)=s^4+s^2+\lambda s\) has formal derivative \(\lambda\ne0\). Consequently each equation \(Q_\lambda(s)=0\) and \(Q_\lambda(s)=\lambda\) has exactly four distinct roots in \(k\), and the root sets are disjoint. There are exactly eight allowed base translations, four of which centralize \(G_\lambda\). Every liftable base automorphism has exactly four lifts, a torsor for the order-four deck group. It follows that \(|N(G_\lambda)|=8\cdot4=32\) and \(|C(G_\lambda)|=4\cdot4=16\). The eight allowed \(s\) satisfy \(Q_\lambda(s)\in\lambda\mathbb F_2\); they form a three-dimensional \(\mathbb F_2\)-vector space. The map \(s\mapsto s^2/\lambda\) is additive and injective. The quotient normalizer is therefore \((\mathbb Z/2)^3\), and the four solutions of \(Q_\lambda(s)=\lambda\) produce automorphisms that invert \(G_\lambda\).

## Verification
The standalone script `verify.py` operates in \(\mathbb F_{2^{12}}\) using the irreducible polynomial \(z^{12}+z^3+1\). It exhaustively checks the Witt-translation polynomial identity for every base coordinate in this field, for \(\lambda=1\) and the two nontrivial cube roots of unity. It also finds four roots for each of the two additive equations and tests the eight-element translation space. These are finite exact checks of critical formulas, not substitutes for the algebraic-closure and pole-order arguments in the proof. Run with `python verify.py` (Python standard library only).

## Relationship to prior work
Kazemifard–Tafazolian (arXiv:2610.04702v1, Theorem 5.7) establish the length-two Artin–Schreier–Witt normal form for this wild boundary case, explicitly without asserting uniqueness of \(\lambda\). The present statement concerns the previously unspecified equivalence relation **for a curve together with its cyclic subgroup** and computes that subgroup's normalizer.

Cardona–Nart–Pujolàs (arXiv:math/0210105v1) classify characteristic-two genus-two curves and their full automorphism structures after forgetting a distinguished cyclic subgroup. That broader unmarked classification does not itself identify the isomorphism relation between the Witt representatives **as marked pairs**. The normalizer calculation is consistent with their order-\(32\) and order-\(160\) automorphism cases; no new claim about the full automorphism group is made here.

## Limitations
No assertion is made that distinct \(\lambda\) produce nonisomorphic unmarked curves. No complete classification of conjugacy classes of all cyclic-order-four subgroups inside the full automorphism group is supplied. Group-scheme infinitesimal automorphisms, automorphisms over non-algebraically-closed fields, and the degenerate parameter \(\lambda=0\) are outside the claim. Historical priority for equivalent marked formulations in older literature is not independently settled.

## References
- A. Kazemifard and S. Tafazolian, *Cyclic automorphisms beyond the canonical bound* (2026), arXiv:2610.04702v1, https://arxiv.org/abs/2610.04702 .
- G. Cardona, E. Nart and J. Pujolàs, *Curves of genus two over fields of even characteristic* (2002 preprint; journal version 2005), arXiv:math/0210105v1, https://arxiv.org/abs/math/0210105 .
