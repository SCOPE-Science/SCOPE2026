# Two geometric \(7\)-rank-zero Picard curves in characteristic seven

## Finding
Let \(k=\overline{\mathbf F}_7\). Among all smooth genus-three Picard curves over \(k\) (the smooth completions of cyclic cubic covers \(y^3=f(x)\) with separable quartic \(f\)), **exactly two geometric isomorphism classes** have Jacobian \(7\)-rank zero. Representatives are
\[
 C_0:\ y^3=x^4+x,\qquad C_2:\ y^3=x^4+x+\eta,\quad \eta^3=2.
\]
Both have \(a\)-number \(2\), so neither is superspecial. More explicitly, a separable, monic, depressed quartic
\[
 C_{a,b,c}:\quad y^3=x^4+a x^2+b x+c
\]
has \(7\)-rank zero **if and only if** \(a=0\), \(b\ne0\), and
\[
 \frac{c^3}{b^4}\in\{0,2\}.
\]
For these curves, \(\operatorname{rank}(\mathcal C)=1\) on regular differentials, where \(\mathcal C\) is the Cartier operator.

## Assumptions and scope
All geometric statements are over \(k=\overline{\mathbf F}_7\). The quartic on the right is required to have four distinct roots; the smooth completion has genus three by Riemann–Hurwitz. Here *Picard curve* refers to the cyclic cubic-cover family with a separable quartic \(f\), equivalently the five-branch-point signature with four branch exponents of one type and one of the other; this is not a claim about every genus-three cyclic triple cover of every branch signature. A base-coordinate translation removes the cubic term since \(4\) is invertible in characteristic seven. The \(7\)-rank is the dimension of the etale part of the Jacobian's \(7\)-torsion, equivalently the stable rank of the Cartier operator. The \(a\)-number is \(3-\operatorname{rank}(\mathcal C)\). The two classes are *abstract geometric curve isomorphism classes*, not merely marked-cover presentation classes. No assertion about arithmetic twists, Newton polygons, or point counts is made.

## Proof
**1. Cartier matrix.** Put \(f=x^4+a x^2+b x+c\). A basis of regular differentials is
\[
 \omega_0=\frac{dx}{y^2},\qquad \omega_1=\frac{x\,dx}{y^2},\qquad \omega_2=\frac{dx}{y}.
\]
Since \(y^3=f\), in characteristic seven the identities \(y^{-2}=f^4y^{-14}\) and \(y^{-1}=f^2y^{-7}\) express the Cartier images using coefficients of \(f^4\) and \(f^2\). Using \(\mathcal C(x^m dx)=0\) unless \(m\equiv6\pmod7\), the coefficient matrix (before entrywise seventh roots) is block diagonal with a two-by-two block
\[
 M=\begin{pmatrix} U&V\\W&Z\end{pmatrix},\qquad
 \begin{aligned}
 U&=[x^6]f^4=-3a^3c-a^2b^2-2ac^2-2b^2c,\\
 V&=[x^5]f^4=-2a^2bc-3ab^3-2bc^2,\\
 W&=[x^{13}]f^4=-3b,\\
 Z&=[x^{12}]f^4=-a^2-3c,
 \end{aligned}
\]
and the one-dimensional scalar \([x^6]f^2=2a\). In the indicated basis \(\mathcal C(v)=\operatorname{diag}(M,2a)^{(1/7)}v^{(1/7)}\); the notation \((1/7)\) means entrywise seventh roots. Every displayed polynomial identity is in \(\mathbf F_7[a,b,c]\).

**2. Necessary vanishing and the two-dimensional block.** If \(a\ne0\), the one-dimensional Cartier summand is invertible, so the \(7\)-rank is at least one. Therefore a rank-zero curve must have \(a=0\). Then
\[
 M=\begin{pmatrix}-2b^2c&-2bc^2\\-3b&-3c\end{pmatrix}
 =\begin{pmatrix}-2bc\\-3\end{pmatrix}\begin{pmatrix}b&c\end{pmatrix}.
\]
If \(b=0\) and \(f\) is separable, then \(c\ne0\), and the lower-right entry \(-3c\) gives a nonzero stable rank. Thus \(b\ne0\). The displayed factorization proves that \(M\) has rank exactly one. For a rank-one semilinear operator, its stable rank is zero exactly when its square vanishes. This is equivalent to \(M^{(7)}M=0\), where \((7)\) means raising each coefficient to its seventh power. Writing \(M=vw^T\) shows
\[
 w^{(7)T}v=-2b^8c-3c^7=-c(2b^8+3c^6).
\]
Consequently, the stable rank of this block vanishes exactly when \(c=0\) or \(c^6=4b^8\) (since \(-2/3=4\) in \(\mathbf F_7\)). In the second case the invariant \(t=c^3/b^4\) satisfies \(t^2=4\), hence \(t\in\{2,5\}\).

**3. Remove the singular boundary.** For \(a=0\) the quartic discriminant is
\[
 \Delta(x^4+bx+c)=256c^3-27b^4=4c^3-6b^4=b^4(4t-6).
\]
Thus \(t=5\) is singular, while \(t=0\) and \(t=2\) are smooth. These and only these give \(7\)-rank zero. Their full Cartier matrix has rank exactly one, giving \(a\)-number \(2\).

**4. Geometric isomorphism classes.** With a smooth monic depressed quartic, an isomorphism preserving the distinguished cyclic triple cover has the form \(x\mapsto\alpha x\), \(y\mapsto\gamma y\), where \(\gamma^3=\alpha^4\); its coefficients transform as \((a,b,c)\mapsto(\alpha^2a,\alpha^3b,\alpha^4c)\) or inversely depending on the direction of the isomorphism. The ratio \(t=c^3/b^4\) is unchanged. Over \(k\), scaling normalizes any nonzero \(b\) to \(1\). When \(t=2\), the three choices of \(\eta\) with \(\eta^3=2\) are related by the remaining cubic-root scalings. Thus \(t=0\) and \(t=2\) each yield one marked-cover isomorphism class and they differ.

The only Picard curves having more than one distinguished cyclic triple-cover subgroup are the *special* Picard curves, geometrically isomorphic to \(y^3=x^4-1\) (Bouw–Koutsianas–Sijsling–Wewers, Lemma 1.17). In characteristic seven this special curve has stable Cartier rank one, as is also immediate from the displayed matrix with \(a=b=0,c=-1\). Hence both rank-zero curves are nonspecial. Lemma 1.21 of the same work shows that any abstract isomorphism between two nonspecial Picard curves respects their distinguished cyclic-cover subgroup and has the affine form already considered. The two marked classes are therefore also precisely two abstract geometric isomorphism classes. This completes the proof.

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. It expands the powers of the universal quartic in the polynomial ring \(\mathbf F_7[x,a,b,c]\) and matches all five coefficients in the Cartier matrix. It independently constructs \(\mathbf F_{7^3}=\mathbf F_7[u]/(u^3-2)\), confirms irreducibility of \(u^3-2\), evaluates the twisted Cartier-square condition, and exhausts all \(343\) values of \(c\) for the normalized slice \(a=0,b=1\). Precisely four such \(c\)-values give smooth rank-zero models, with cube values \(0\) (one model) and \(2\) (three models); the three additional rank-zero candidates having \(c^3=5\) are singular. The finite-field check corroborates the symbolic proof; it is not used to infer the geometric universal quantifier.

## Relationship to prior work
The motivating 2023 preprint of Nourozi and Rahmati (arXiv:2306.07823, v1 dated June 13, 2023) supplies a general Picard Cartier-matrix framework; its Theorem 3.1 states a uniform \(a\)-number claim for \(p\equiv1\pmod3\) and nonzero constant coefficient. The explicit smooth curve \(C_2\) above has nonzero constant coefficient but \(a=2\), so the present exact calculation gives a counterexample to that general nonvanishing assertion. Equation (3.2) of their preprint is consistent with the coefficient formula used here; the nonvanishing inference in the theorem's proof is not generally valid.

Kazemifard and Tafazolian (2015) determine Newton polygons for the special families \(y^3=x^4-x\) and \(y^3=x^4-1\). The first is geometrically isomorphic to \(C_0\); its rank-zero behavior is **known**, not claimed as new. Their two-family classification does not give the exhaustive Picard rank-zero classification or the second class \(C_2\). Bouw, Koutsianas, Sijsling, and Wewers (2019 preprint, published 2020) give normal forms and abstract isomorphism criteria, which are used here; their work does not derive the characteristic-seven rank-zero stratum. Ozman, Pries, and Weir (2022) treat general \(p\)-rank strata of cyclic covers but not this explicit two-point classification. The contribution is the complete genus-three Picard \(7\)-rank-zero isomorphism classification, rather than a new Cartier-method formula or rediscovery of the familiar \(C_0\).

## Limitations
The theorem does not classify intermediate \(7\)-ranks, Newton polygons, twists, or rational models. The calculation is over an algebraic closure, so a parameter rational over \(\mathbf F_7\) need not admit the normalized representative over \(\mathbf F_7\). The older Kazemifard–Tafazolian article's publisher PDF could not be accessed during the comparison; the available detailed primary-page text identifies its scope as the two indicated families. Unindexed equivalent characteristic-seven classifications remain a bibliographic possibility. Independent validation has not been performed.

## References
1. V. Nourozi and F. Rahmati, *The Rank of the Cartier Operator on Picard Curves*, arXiv:2306.07823 (first submitted June 13, 2023), particularly §3 and Theorem 3.1: https://arxiv.org/pdf/2306.07823.
2. I. I. Bouw, A. Koutsianas, J. Sijsling, S. Wewers, *Conductor and Discriminant of Picard Curves*, arXiv:1902.09624 (February 25, 2019), especially Lemmas 1.3, 1.17, 1.21: https://arxiv.org/pdf/1902.09624.
3. A. Kazemifard and S. Tafazolian, *A Note on Some Picard Curves over Finite Fields*, Finite Fields and Their Applications **34** (2015), 107–122, DOI:10.1016/j.ffa.2014.12.002.
4. E. Ozman, R. Pries, C. Weir, *The Boundary of the p-Rank 0 Stratum of the Moduli Space of Cyclic Covers of the Projective Line*, Nagoya Mathematical Journal (2022), §7.2, https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/boundary-of-the-prank-0-stratum-of-the-moduli-space-of-cyclic-covers-of-the-projective-line/02D5FFF8FB89AC671E0F637D48BB1613.
