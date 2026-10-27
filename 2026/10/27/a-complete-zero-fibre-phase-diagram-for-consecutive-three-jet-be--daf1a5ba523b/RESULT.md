# A complete zero-fibre phase diagram for consecutive three-jet Bergman Gram kernels

## Finding
Let \(\mathbb H=\{z\in\mathbb C:\operatorname{Im}z>0\}\). For \(u,v,b\in\mathbb R\), set \(\xi=(1,u+iv,b,0,\ldots)\) and let \(B_\xi\) be the canonical Gram kernel of the differential-evaluation functional \(f(z)+(u+iv)f'(z)+b f''(z)/2\) in \(A^2(\mathbb H)\). Define \(N(u,v,b)\) to be the number, with algebraic multiplicity, of roots \(t\) of the scalar factor of \(B_\xi\) with \(\operatorname{Im}t<0\). Each such root describes an entire nonempty fibre of pairs \((z,w)\in\mathbb H^2\) with \(1/(z-\overline w)=t\); no root of this type means that \(B_\xi\) is zero-free.

Write \(R=u^2+v^2\). The **complete count** is:

1. If \(b=0\), then \(N=2\) for \(v>0\) and \(N=0\) for \(v\le0\).
2. If \(b>0\) and \(v\ne0\), then \(N=2\). If \(b>0\) and \(v=0\), then \(N=0\) for \(u^2\ge(1+\sqrt{10/3})b\), and \(N=2\) otherwise.
3. If \(b<0\) and \(v=0\), then \(N=0\) for \(u^2\ge(\sqrt{10/3}-1)|b|\), and \(N=2\) otherwise.
4. If \(b<0\), \(v\ne0\), and \(T=5|b|/6\), then \(N=2\) for \(R<T\). For \(R=T\), \(N=0\) for \(v<0\) and \(N=2\) for \(v>0\). For \(R>T\), \(N=0\) for \(v<0\) and \(N=4\) for \(v>0\).

This is a sharp zero-free/zero-count classification for the first consecutive three-jet family with real second-derivative coefficient. The four-zero-fibre chamber and the thin zero-free discriminant strata distinguish it from two-jet behaviour.

## Assumptions and scope
The ambient Bergman space uses planar Lebesgue area measure on \(\mathbb H\), and the derivative functional has Taylor normalization \(\xi_j f^{(j)}(z)/j!\). The parameter \(b\) is real, while the first derivative coefficient \(u+iv\) is arbitrary complex. Zero fibres are counted as roots of a polynomial in the scalar \(t=1/(z-\overline w)\), not as individual pairs \((z,w)\), of which each fibre has infinitely many. Roots on the real \(t\)-axis are not attainable by pairs in \(\mathbb H^2\), and are excluded even if repeated.

## Proof
**Step 1: exact scalar polynomial.** The half-plane formula of Gehlawat–Jain–Sarkar, Theorem 4.1, equation (4.6), gives
\[
B_\xi(z,w)=-\frac{1}{\pi(z-\overline w)^2}F_\xi\!\left(\frac{1}{z-\overline w}\right),\qquad
F_\xi(t)=\sum_{m,n\ge0}\frac{(-1)^m(m+n+1)!}{m!n!}\xi_m\overline{\xi_n}\,t^{m+n}.
\]
Substitution of \(\xi=(1,u+iv,b)\), with \(R=u^2+v^2\), gives the **exact** degree-at-most-four polynomial
\[
F_\xi(t)=1-4iv t+6(b-R)t^2-24ibv t^3+30b^2t^4.
\]
Because \(z-\overline w\) ranges surjectively over the upper half-plane, its reciprocal ranges over the lower half-plane. Putting \(t=-is\) converts lower-half-plane roots into roots in \(\operatorname{Re}s>0\) of the real-coefficient polynomial
\[
P(s)=30b^2s^4+24bv s^3+6(R-b)s^2-4vs+1.
\tag{1}
\]
The leading factor outside \(F_\xi\) never vanishes.

**Step 2: the quadratic slice.** If \(b=0\) and \(R>0\), equation (1) reduces to \(6Rs^2-4vs+1\). Its discriminant is \(16v^2-24R<0\), so its conjugate pair has real part \(v/(3R)\). Thus there are two right-half-plane roots when \(v>0\), and none when \(v\le0\). For \(R=0\), \(P=1\).

**Step 3: the real-first-jet slice.** For \(b\ne0\) and \(v=0\), the polynomial in \(t\) is even:
\[
F_\xi(t)=30b^2t^4+6(b-u^2)t^2+1.
\]
All its roots are real, hence no admissible zero fibre exists, exactly when the quadratic in \(y=t^2\) has two nonnegative real roots. Since their product is positive, this occurs exactly when \(u^2-b\ge\sqrt{10/3}|b|\). At equality the real roots are repeated, but still excluded. Otherwise the even real quartic has exactly two lower-half-plane roots, counting multiplicity. The stated thresholds follow on separating \(b>0\) and \(b<0\).

**Step 4: locating all possible imaginary-axis crossings for nonreal first jets.** Assume \(b\ne0\) and \(v\ne0\). For real \(y\), equation (1) at \(s=iy\) separates into
\[
\operatorname{Im}P(iy)=y(-4v-24bv y^2),\qquad
\operatorname{Re}P(iy)=30b^2y^4-6(R-b)y^2+1.
\]
Because \(P(0)=1\), a crossing requires \(y^2=-1/(6b)>0\), so \(b<0\), and the real equation then simplifies to \(R=-5b/6=5|b|/6\). Consequently **no** roots can cross the imaginary axis in either open sign chamber for \(b>0\), or away from this exact circle for \(b<0\).

**Step 5: counts in each chamber.** For \(b>0\), connectedness of each region \(v>0\) and \(v<0\) and Step 4 make the count constant there. Approach \((u,v)=(0,0)\), where equation (1) is even with a pair of roots in each open half-plane, so \(N=2\) throughout both nonreal slices.

For \(b<0\), scaling reduces to \(b=-1\). The two open half-discs \(v>0\) and \(v<0\) with \(R<T\) are connected, and at \((u,v)=(0,0)\) the even quartic has two roots in each half-plane, so \(N=2\) below the circle. In the connected region \(v<0,R>T\), the quartic is strictly Hurwitz stable. Indeed its coefficients \((A,B,C,D,E)=(30b^2,24bv,6(R-b),-4v,1)\) are positive, and its two nontrivial Hurwitz determinants are
\[
BC-AD=24bv(6R-b)>0,\qquad
BCD-AD^2-B^2E=-96b v^2(6R+5b)>0.
\]
For \(b<0,v<0,R>T\), every root therefore has negative real part, giving \(N=0\). The identity \(P_{u,-v,b}(s)=P_{u,v,b}(-s)\) reflects roots across the imaginary axis and proves \(N=4\) for \(b<0,v>0,R>T\).

Exactly on \(R=T\), equation (1) factors as
\[
P(s)=\left(s^2-\frac1{6b}\right)\left(30b^2s^2+24bv s-6b\right).
\]
The first factor has two imaginary-axis roots; the second has both roots in the right half-plane for \(v>0\), and both in the left half-plane for \(v<0\), since its quadratic leading and constant coefficients are positive and its linear coefficient has sign opposite \(v\). The counts on the circle are therefore \(2\) and \(0\), respectively, completing the classification.

## Verification
The coefficient expansion follows directly by the nine pairs \((m,n)\in\{0,1,2\}^2\) in the primary formula. The displayed Hurwitz determinants and circle factorization are exact polynomial identities and can be verified by ordinary expansion. The Hurwitz theorem is used only under strict nondegeneracy, \(b<0,v<0,R>T\); boundary cases are covered by direct factorization. Continuity and connectedness carry counts only across regions proved to have no imaginary-axis roots. Numerical root tests are supplementary, not the proof.

## Relationship to prior work
Gehlawat–Jain–Sarkar (2026) constructed the canonical Gram kernel, supplied the general polynomial representation, and established zero-freeness for particular pure-jet and factorial-decay sequences. That representation is the starting point here, not a novel kernel construction. The classification above supplies the complete sharp three-real-parameter zero-count diagram for consecutive jets with real second coefficient, which is not stated in its examples. Related published work treats value/first-derivative two-jet phases, separated pure-jet pairs and disk-jet kernels; those results do not classify the three-jet chamber geometry or its four-zero region.

## Limitations
The second-derivative coefficient \(b\) is restricted to real values; there is no result here for arbitrary complex \(b\), for other domains, or for spaces other than the usual unweighted upper-half-plane Bergman space. Algebraic multiplicity counts parameter fibres and does not count individual zero pairs. The general finite-jet reduction to a polynomial is known, so priority concerns only the explicit sharp phase classification; an unindexed earlier classification could still exist. There has been no independent audit.

## References
Gehlawat, S., Jain, A., and Sarkar, A. *A Canonical Positive Definite Kernel Associated with the \(\xi\)-Bergman Kernel*, arXiv:2608.13193v1 (first public 2026-08-13), Theorem 4.1 and Section 4.

Routh–Hurwitz quartic stability criterion (classical; applied with its determinants written explicitly above).
