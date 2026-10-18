# The ten-sheeted forgetful map for cyclic-quartic genus-two covers in characteristic two

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\). For \(\lambda\in k^\times\), let \((C_\lambda,G_\lambda)\) be the smooth genus-two curve with its distinguished **unlabelled** cyclic order-four deck subgroup defined by the length-two Artin–Schreier–Witt equation
\[
(F-1)(Y_0,Y_1)=(x,\lambda x^3).
\]
Here \(F\) denotes Witt Frobenius. The parameter is complete for subgroup-marked isomorphism:
\[
(C_\lambda,G_\lambda)\simeq(C_\mu,G_\mu)\quad\Longleftrightarrow\quad\lambda=\mu.
\]
If the cyclic subgroup is forgotten, the complete geometric isomorphism invariant is
\[
J(\lambda)=\frac{(\lambda^2+\lambda+1)^5}{\lambda^6}:
\qquad C_\lambda\simeq C_\mu\quad\Longleftrightarrow\quad J(\lambda)=J(\mu).
\]
This gives a separable degree-ten map \(\mathbb P^1_\lambda\to\mathbb P^1_J\). Over each finite \(j\ne0\), precisely ten nonisomorphic subgroup-marked pairs have the same underlying curve; over \(j=0\), precisely two have the same underlying curve, each counted with multiplicity five. The zeros of \(\lambda^2+\lambda+1\) are the two exceptional parameters. Upon compactification the points \(\lambda=0,\infty\) lie over \(J=\infty\) with pole orders \(6,4\), respectively. Thus the only branch values of the compactified map are \(0\) and \(\infty\).

As a corollary, every curve in this family has exactly ten conjugacy classes of order-four cyclic subgroups when \(J\ne0\), and exactly two when \(J=0\). This subgroup-count formulation uses the exhaustiveness of the normal form in the originating classification. The familiar automorphism-group orders of \(32\) and \(160\) in the respective cases are earlier results and are **not** asserted as new.

## Assumptions and scope

All isomorphisms are geometric over \(k\). A subgroup-marked pair means a curve together with an *unlabelled* embedded subgroup \(G\cong C_4\); its generator is not part of the marking. The Witt equation denotes the smooth projective normalization. It defines a connected cover, of genus two, for every nonzero parameter by the upper-jump computation \((1,3)\) in Kazemifard–Tafazolian, Theorem 5.7. No claim is made over non-algebraically-closed fields, where roots and descent obstructions alter the isomorphism problem. The finite-value fiber count concerns \(j\in k\), not the point \(j=\infty\) of the compactification.

## Proof

**1. Uniqueness for subgroup-marked covers.** Kazemifard–Tafazolian, Theorem 5.7, shows that every characteristic-two genus-two curve with a cyclic order-four subgroup has the stated normal form, and establishes its single branch point. A pair isomorphism descends to an affine change \(x\mapsto\alpha x+\beta\) of the quotient projective line (the unique branch point is fixed). Their coefficient-reduction formulas show that a reduced Witt representative \((ax,bx^3+cx)\), with \(a,b\ne0\), has its ratio \(b/a^3\) invariant under affine substitution and removal of Witt coboundaries: the leading coefficients change to \(a\alpha\) and \(b\alpha^3\), while translation only affects lower coefficients. The sole nonidentity change of generator of \(C_4\) sends a Witt class to its negative; in characteristic two its second component changes by the square of the first, which has no effect on the reduced cubic coefficient. Consequently the value \(\lambda=b/a^3\) is invariant under every subgroup-marked isomorphism. Equal parameters give the identical presentation, proving the first equivalence.

**2. A hyperelliptic model.** Put \(u=Y_0\), so \(x=u^2+u\). In the length-two Witt addition convention of the source,
\[
(F-1)(u,Y_1)=(u^2+u,Y_1^2+Y_1+u^2+u^3).
\]
Write \(r^4=\lambda\) (unique in \(k\)) and set
\[
H=r^2u^3+r^2u^2+(1+r)u,\qquad v=Y_1+H.
\]
An exact polynomial identity then gives
\[
 v^2+v=a_\lambda u^5+b_\lambda u^3+c_\lambda u,
\quad a_\lambda=\lambda,\quad b_\lambda=\lambda+\lambda^{1/2}+1,\quad c_\lambda=1+\lambda^{1/4}.
\]
This is a genus-two Artin–Schreier model because the right-hand side has odd degree five.

**3. Classification of the unmarked quintic models.** Consider arbitrary smooth models
\[
v^2+v=au^5+bu^3+cu,\qquad v'^2+v'=a'u'^5+b'u'^3+c'u',\quad aa'\ne0.
\]
The genus-two hyperelliptic involution and its quotient are intrinsic. The unique branch point on the quotient lies at infinity, so any geometric isomorphism must have \(u'=su+t\), with \(s\ne0\), and \(v'=v+h(u)\), where \(h\) is a polynomial of degree at most two. Comparing odd powers forces \(a=a's^5\) and \(b=b's^3\). Thus \(I=b^5/a^3\) is invariant.

Conversely, equality of \(I\) produces a scaling. If \(b,b'\ne0\), put \(A=a/a'\), \(B=b/b'\); then \(B^5=A^3\), and \(s=B^2/A\) satisfies \(s^5=A\) and \(s^3=B\). If \(b=b'=0\), take any fifth root of \(a/a'\). (An equality of \(I\) cannot pair zero and nonzero cubic coefficients.) It remains to match the linear coefficient. After the fixed scaling let
\[
P_4=a's^4t,\qquad P_2=b's^2t,\qquad P_1=a'st^4+b'st^2+c's+c.
\]
The discrepancy of the two quintics has fourth-, second-, and first-degree coefficients \(P_4,P_2,P_1\). An Artin–Schreier coboundary \(h(u)^2+h(u)\), with \(h(u)=eu^2+fu+g\), matches these coefficients if \(f=P_1\), \(e=P_2+P_1^2\), and
\[
\bigl(P_2+P_1^2\bigr)^2=P_4.
\]
The latter is a degree-sixteen polynomial equation in \(t\) with nonzero leading coefficient \((a's)^4\), hence has a solution over the algebraically closed field \(k\). Its linear coefficient is also nonzero. The remaining constant discrepancy is removable by choosing \(g\) with \(g^2+g\) equal to that constant. Therefore equality of \(I\) suffices, completing the exact unmarked classification.

**4. Degree and exceptional fibers.** For the Witt models,
\[
b_\lambda^2=\lambda^2+\lambda+1,\qquad
I(C_\lambda)^2=\frac{(\lambda^2+\lambda+1)^5}{\lambda^6}=J(\lambda).
\]
Frobenius is injective on the field, so the second displayed equivalence follows. Set \(Q(\lambda)=\lambda^2+\lambda+1\). The numerator and denominator of \(J\) are coprime, and the numerator has degree ten, establishing degree ten. In characteristic two,
\[
J'(\lambda)=\frac{Q(\lambda)^4}{\lambda^6}\ne0,
\]
so the morphism is separable. For \(j\ne0\), \(Q(\lambda)^5+j\lambda^6=0\) has degree ten and derivative \(Q(\lambda)^4\); no root can satisfy \(Q=0\), so it has ten distinct nonzero roots. For \(j=0\), the equation is \(Q^5=0\); \(Q\) has two simple nonzero roots, each of multiplicity five. Finally, \(J\) has poles of orders six at zero and four at infinity. These facts give the full asserted fiber and branch descriptions.

**5. Conjugacy classes.** The source theorem gives a Witt normal form for any pair \((C,G)\) with \(G\cong C_4\). For a fixed underlying curve \(C\), two subgroups are conjugate by an automorphism of \(C\) exactly when the two subgroup-marked pairs are isomorphic. Parts 1 and 4 therefore count those conjugacy classes by the parameter fiber.

## Verification

The accompanying `verify.py` is a dependency-free exact-arithmetic test. It verifies the Witt-to-quintic identity over the polynomial ring \(\mathbb F_2[r,u]\), independently checks the coefficient-invariant identity over \(\mathbb F_{256}\), tests explicit scalings for every finite-field parameter pair with equal nonzero invariant, and checks the degree-ten and derivative identities over \(\mathbb F_2[\lambda]\). It reports `VERIFY_OK`. This finite test does not replace the field-uniform classification proof or prove originality.

## Relationship to prior work

Kazemifard and Tafazolian, Theorem 5.7, establish the existence/exhaustiveness of the Witt normal form and its ramification; they explicitly do not assert uniqueness of \(\lambda\). Their formulas for affine reduction are used in part 1, not claimed here as new. Yamaguchi and Harashita study the general characteristic-two hyperelliptic normal form and establish automorphism orders \(32\) and \(160\) for the genus-two \(2\)-rank-zero locus. Older work on genus-two moduli and absolute invariants establishes the broad context. The distinguishing result here is the **specific rational forgetful map for this Witt family**, its marked uniqueness, degree-ten fibers, and exceptional ramification. The general isomorphism theory of characteristic-two quintic Artin–Schreier models is standard background and is not presented as a novel general classification.

## Limitations

Only subgroup-marked geometric isomorphism and underlying geometric isomorphism are addressed, not labelled-generator or arithmetic descent classifications. The numbers ten and two count conjugacy classes of order-four subgroups, not all such subgroups and not group elements. The map is a morphism after compactification, but \(\lambda=0\) and \(\lambda=\infty\) do not represent smooth genus-two covers in the specified Witt family. The automorphism orders quoted above are previously known. The originality comparison is based on accessible primary texts and searches, not a proof of universal novelty; nonindexed calculations remain possible.

## References

- A. Kazemifard and S. Tafazolian, *Cyclic automorphisms beyond the canonical bound*, arXiv:2610.04702v1 (3 October 2026), especially Theorem 5.7 and its coefficient-reduction calculation. https://arxiv.org/html/2610.04702v1
- K. Yamaguchi and S. Harashita, *Automorphism groups of hyperelliptic curves of 2-rank zero*, arXiv:2604.17901v1 (20 April 2026), Theorems 1 and 2. https://arxiv.org/html/2604.17901v1
- L. Zobernig, *Genus 2 Curves in Small Characteristic*, arXiv:2111.07270v1 (14 November 2021), Section 1.2. https://arxiv.org/html/2111.07270v1
