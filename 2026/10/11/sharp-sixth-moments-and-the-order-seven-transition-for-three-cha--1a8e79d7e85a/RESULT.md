# Sharp sixth moments and the order-seven transition for three-character progressions

## Finding
Let \(G\) be a finite abelian group, let \(\gamma\) and \(\delta\) be characters of \(G\), and suppose the order \(N\) of \(\delta\) is at least \(7\). For arbitrary complex coefficients, define
\[
F(g)=\gamma(g)\bigl(c_0+c_1\delta(g)+c_2\delta(g)^2\bigr).
\]
The sharp, normalized sixth-moment inequality is
\[
\boxed{\frac1{|G|}\sum_{g\in G}|F(g)|^6
\le \frac{35(\sqrt{105}-3)}{48}
\bigl(|c_0|^2+|c_1|^2+|c_2|^2\bigr)^3.}
\]
Every nonzero equality case is exactly
\[
\boxed{(c_0,c_1,c_2)=\lambda\left(1,
\sqrt{\frac{\sqrt{105}-5}{4}}\,e^{i\theta},e^{2i\theta}\right),
\quad\lambda\in\mathbb C\setminus\{0\},\quad\theta\in\mathbb R.}
\]
The coefficient is approximately \(5.284234933512\), strictly larger than the equal-amplitude value \(47/9\). The order threshold is sharp: for every \(3\le N\le6\), this same coefficient fails for at least one three-character progression.

## Assumptions and scope
The average uses normalized counting measure \(|G|^{-1}\sum_{g\in G}\). Characters take values on the unit circle, and order refers to the order of the character in the dual group. The order requirement \(N\ge7\) ensures \(\gamma^3\delta^j\), for integer \(0\le j\le6\), are distinct characters. The coefficients may be any complex numbers, including zero, although equality for a nonzero vector forces all three to be nonzero. No restriction is placed on the remaining structure or cardinality of \(G\).

## Proof
**1. Exact cubic convolution.** Set \(P(z)=c_0+c_1z+c_2z^2\). The seven coefficients of \(P(z)^3\), in increasing degree, are
\[
\begin{aligned}
a_0&=c_0^3,&a_1&=3c_0^2c_1,&a_2&=3c_0^2c_2+3c_0c_1^2,\\
a_3&=c_1^3+6c_0c_1c_2,&a_4&=3c_0c_2^2+3c_1^2c_2,\\
a_5&=3c_1c_2^2,&a_6&=c_2^3.
\end{aligned}
\]
Since the seven characters \(\gamma^3\delta^j\) are pairwise distinct, character orthogonality gives the exact identity
\[
\frac1{|G|}\sum_{g\in G}|F(g)|^6=\sum_{j=0}^6|a_j|^2.
\]
Writing \(x=|c_0|\), \(y=|c_1|\), \(z=|c_2|\), the triangle inequality applied to each cubic coefficient shows that the right-hand side is at most the same sum formed with nonnegative \(x,y,z\). Thus it suffices first to optimize a nonnegative homogeneous sextic.

**2. Equality of endpoint moduli.** For nonnegative \(x,y,z\), put \(u=x^2+z^2\), \(w=y^2\), and \(p=xz\). Direct expansion of the seven squared cubic coefficients yields
\[
Q=u^3+9u^2w+9uw^2+w^3+(18uw+12w^2)p+(6u+18w)p^2.
\]
For fixed \(u,w\), arithmetic-geometric mean gives \(0\le p\le u/2\), and this expression is increasing in \(p\); for \(u>0\), its maximizer is uniquely \(p=u/2\). (If \(w=0\), the increase is strict for positive \(p\); the endpoint still maximizes uniquely.) Hence every nonzero global maximizer with a nonzero endpoint has \(x=z\). The remaining boundary \(x=z=0\) has normalized quotient \(1\), smaller than the asserted sharp value.

**3. One-variable sharp optimization.** Write \(x=z=a>0\), \(y=ta\), with \(t\ge0\). Then the normalized quotient is
\[
R(r)=\frac{r^3+30r^2+90r+20}{(r+2)^3},\qquad r=t^2\ge0.
\]
Its derivative factors as
\[
R'(r)=-\frac{12(2r^2+5r-10)}{(r+2)^4}.
\]
The quadratic in the numerator has exactly one nonnegative root,
\[
r_* = \frac{\sqrt{105}-5}{4}.
\]
Thus \(R\) increases to \(r_*\) and decreases thereafter. At this point,
\[
R(r_*)=\frac{35(\sqrt{105}-3)}{48}.
\]
The boundary values \(R(0)=5/2\) and \(\lim_{r\to\infty}R(r)=1\) are strictly smaller. This proves the sharp inequality and positive-modulus uniqueness.

**4. Complex equality.** At the modulus optimizer all three coefficients are nonzero. Equality in the coefficientwise triangle inequalities requires, in particular, the terms \(3c_0^2c_2\) and \(3c_0c_1^2\) in \(a_2\) to have the same argument. Equivalently, \(c_1^2/(c_0c_2)\) is a positive real number. Together with \(|c_0|=|c_2|\), this is exactly the affine phase relation \(c_j=\lambda t_j e^{ij\theta}\), with \((t_0,t_1,t_2)=(1,\sqrt{r_*},1)\). Conversely this relation aligns every summand in every \(a_j\), so all the displayed equality cases attain the sharp constant.

**5. Sharpness of the order cutoff.** If \(3\le N\le6\), take the strictly positive coefficient triple \((1,\sqrt{r_*},1)\). The cubic coefficient sequence \((a_0,\ldots,a_6)\) is strictly positive. Its characters now alias whenever \(j\equiv k\pmod N\). Therefore
\[
\frac1{|G|}\sum_{g\in G}|F(g)|^6
=\sum_{r=0}^{N-1}\left|\sum_{0\le j\le6,\,j\equiv r\;(\mathrm{mod}\;N)}a_j\right|^2
>\sum_{j=0}^6a_j^2,
\]
because \(a_0\) and \(a_N\) lie in the same residue class. Dividing by the common positive coefficient \(\ell^2\)-norm to the third power gives a quotient strictly greater than the claimed order-seven constant. Every order \(3\le N\le6\) is realized by a character of a cyclic group of that order.

## Verification
Run `python checker.py` using the Python standard library. The program executes 7,636 deterministic assertions: 729 exact-integer checks of the sextic expansion, direct root-of-unity and cubic-convolution comparisons across thirteen cyclic group orders from \(7\) through \(47\), the sharp upper bound on complex coefficients, the equality construction at eleven independent phase choices per tested order, and strict cutoff failures for orders \(3\) through \(6\). The expected terminal prefix is `VERIFY_OK checks=7636`. All claims for arbitrary groups and all coefficients follow from the preceding proof; finite checks are corroboration, not a substitute for the proof.

## Relationship to prior work
Ciccone and Gonçalves, *Sharp Fourier Extension on the Circle under arithmetic constraints* (arXiv:2208.09441, first posted 2022-08-19), analyze a sharp \(L^2\)-to-\(L^6\) extension problem for a Euclidean circle with \(\mathrm{P}(3)\)-spectrum assumptions. Their Bessel-function restriction geometry is different from the finite-character triple-convolution norm treated here. González-Riquelme and Oliveira e Silva, *Sharp extension inequalities on finite fields* (arXiv:2405.16647), study full algebraic curves and surfaces rather than a chosen three-character progression. Neuwirth, *The maximum modulus of a trigonometric trinomial* (arXiv:math/0703236), determines maximum-modulus and Sidon geometry, not the sharp sixth moment relative to the coefficient square norm.

A published result titled *Even phase moments recover the normalized geometry of a three-frequency spectrum* (record 7849dda51c79) gives a collision expansion for unimodular coefficients; its hypothesis fixes all coefficient magnitudes, so its reported phase-response formula does not contain the weighted optimizer, radical sharp coefficient, or phase-amplitude equality classification here. A separate result on three consecutive characters (record b176a6018242) concerns endpoint Fourier projection norms, not this interior moment norm. A previously obtained fourth-moment classification for three characters does not determine the present sixth-moment constant or its different optimal amplitude ratio. These distinctions concern exact implications rather than title matching; alternative bibliographic formulations remain possible.

## Limitations
The theorem does not calculate the exact sharp constants for orders \(3\) through \(6\); it only establishes that each exceeds the order-seven value. The theorem does not address four or more frequencies or non-even moment exponents. The finite checks do not certify all groups, and the literature comparison does not exclude every unpublished or unindexed equivalence.

## References
1. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441v1, submitted 2022-08-19.
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, submitted 2024-05-26.
3. S. Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236, first posted 2007-03-08.
4. *Even phase moments recover the normalized geometry of a three-frequency spectrum*, published mathematical record 7849dda51c79, 2026.
5. *Exact three-frequency Fourier projection norm on every cyclic group*, published mathematical record b176a6018242, 2026.
