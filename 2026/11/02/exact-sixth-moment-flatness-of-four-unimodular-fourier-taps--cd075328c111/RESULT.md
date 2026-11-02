# Exact sixth-moment flatness of four unimodular Fourier taps

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) carry probability Haar measure. For every coefficient vector \(a=(a_0,a_1,a_2,a_3)\) with \(|a_j|=1\), set
\[
 P_a(e^{it})=\sum_{j=0}^3a_j e^{ijt},\qquad
 M_6(a)=\frac1{2\pi}\int_0^{2\pi}|P_a(e^{it})|^6\,dt.
\]
The **sharp minimum**, attained by and only by the families described below, is
\[
\boxed{\quad M_6(a)\ge 616-\frac{148}{3}\sqrt{111}
 =96.24108152593155\ldots.\quad}
\]
Write \(c_*=2-\sqrt{111}/6\) and \(\theta_*=\arccos c_*\in(0,\pi/2)\). Equality holds precisely for coefficient vectors of
\[
\boxed{\quad P_a(z)=\lambda\bigl[1-w\zeta z-w\zeta^2z^2+\zeta^3z^3\bigr],
\qquad w=e^{i\theta_*}\ \text{or}\ w=e^{-i\theta_*},
\quad |\lambda|=|\zeta|=1.\quad}
\]
In particular, the exact minimum within the binary coefficient alphabet \(a_j\in\{-1,1\}\) is \(112\), strictly larger than the unrestricted-phase optimum. No finite root-of-unity phase alphabet can attain the unrestricted optimum (although such alphabets can approximate it).

There is a strict **fourth/sixth-moment tradeoff** even at this shortest nontrivial four-tap aperture: the family \((1,-e^{i\theta},-e^{i\theta},1)\) has fourth moment \(19\) when \(\cos\theta=1/4\), but its sixth moment is then \(385/4=96.25\), strictly above the sharp sixth-moment minimum. The sixth-moment minimizer has fourth moment strictly above \(19\).

## Assumptions and scope
The support is exactly the four consecutive frequencies \(\{0,1,2,3\}\subset\mathbb Z\); the ambient group is the continuous circle, not a sampled finite grid. Each coefficient has modulus exactly one. Integrals use normalized Haar measure, so \(\|P_a\|_2^2=4\); the displayed numbers are *sixth powers* of \(L^6\) norms, not sixth roots. The phase-alphabet claim concerns finite groups of complex roots of unity (and, more generally, any finite set of roots of unity), not arbitrary finite sets of algebraic phases. No statement is made about fifth or higher-degree apertures.

## Proof
**1. Exact Fourier moment.** Multiplying all coefficients by a common unit scalar and rotating the argument \(z\mapsto\zeta z\), one can normalize \(a_0=a_3=1\); indeed a cube root of \(a_0/a_3\) makes both endpoints equal after dividing by \(a_0\). Write \(a_1=e^{i\alpha}\), \(a_2=e^{i\beta}\), where \(\alpha,\beta\in\mathbb R\).

By Fourier orthogonality, \(M_6(a)\) equals the sum of the squared moduli of the ten coefficients of \((1+e^{i\alpha}z+e^{i\beta}z^2+z^3)^3\). Expanding those coefficients and collecting Fourier modes in \((\alpha,\beta)\) gives the exact identity
\[
\begin{aligned}
M_6={}&256+6(\cos3\alpha+\cos3\beta)\\
&+84(\cos(\alpha-2\beta)+\cos(2\alpha-\beta))
+144\cos(\alpha+\beta).
\end{aligned}
\tag{1}
\]
The coefficients in (1) can be checked by elementary multinomial expansion, without numerical integration: the nonzero Laurent coefficients are \(256\) at bidegree \((0,0)\), \(3\) at each of \(\pm(3,0)\) and \(\pm(0,3)\), \(42\) at each of \(\pm(1,-2)\) and \(\pm(2,-1)\), and \(72\) at \(\pm(1,1)\).

**2. Two independent real variables.** Put \(m=(\alpha+\beta)/2\), \(d=(\alpha-\beta)/2\), \(x=\cos m\), and \(y=\cos(3d)\). Sum-to-product identities, including \(\cos3m=4x^3-3x\), transform (1) exactly into
\[
\boxed{\quad M_6=112+288x^2+12x(4x^2+11)y.\quad}\tag{2}
\]
Every \(x\in[-1,1]\) and \(y\in[-1,1]\) occurs: choose independently \(m\) and \(d\), then set \(\alpha=m+d\), \(\beta=m-d\). The coefficient of \(y\) in (2) has the sign of \(x\) because \(4x^2+11>0\). Thus, for \(t=|x|\in[0,1]\), minimization over \(y\) gives exactly
\[
\phi(t)=112+288t^2-48t^3-132t.
\]
This reduction is exact, including all boundary choices, not an ansatz restricting coefficient symmetries.

**3. Global critical point and equality.** Differentiation yields
\[
\phi'(t)=-12(12t^2-48t+11),\qquad
\phi''(t)=576-288t>0\quad(0\le t\le1).
\]
The quadratic has precisely one root in \([0,1]\), namely \(c_*=2-\sqrt{111}/6\), and \(\phi\) is strictly convex on this interval. Substitution gives \(\phi(c_*)=616-148\sqrt{111}/3\). Equality in the first minimization step requires \(|\cos m|=c_*\) and \(\cos3d=-\operatorname{sgn}(\cos m)\); in particular \(\alpha-\beta\in(2\pi/3)\mathbb Z\), so \(a_1/a_2\) is a cube root of unity. Rotating \(z\) by an appropriate cube root of unity preserves the normalized endpoints and makes the inner coefficients equal. Then (2) forces them to equal \(-e^{i\theta_*}\) or \(-e^{-i\theta_*}\). Undoing the endpoint normalization proves exactly the stated \(\lambda,\zeta\) families, and direct substitution proves that every member attains equality.

**4. Binary and finite-phase obstruction.** Normalize the binary constant coefficient to \(1\) and enumerate the remaining three signs. The eight possibilities have sixth moments only in \(\{112,220,580\}\), and \(112\) occurs. For the finite-alphabet claim, the coefficient ratio \(a_1a_2/(a_0a_3)\), invariant under common scalar and linear-phase rotations, equals \(e^{2i\theta_*}\) or \(e^{-2i\theta_*}\) at equality. If all four coefficients were roots of unity, that ratio would be a root of unity, hence so would \(e^{i\theta_*}\). Then \(2\cos\theta_*=4-\sqrt{111}/3\) would be an algebraic integer. But its irreducible polynomial over \(\mathbb Q\) is \(3X^2-24X+11\): the discriminant \(444\) is nonsquare and the primitive polynomial is nonmonic. This is impossible. Continuity and density of roots of unity in the circle give arbitrary approximation with sufficiently fine phase alphabets.

**5. Relation to fourth-moment minima.** For \(a=(1,-e^{i\theta},-e^{i\theta},1)\), write \(t=\cos\theta\). Its three positive-lag autocorrelations have moduli \(|1-2t|\), \(2t\), and \(1\). Fourier orthogonality then gives
\[
M_4(a)=16+2\bigl((1-2t)^2+4t^2+1\bigr)=20-8t+16t^2.
\]
The unique minimizer in this family is \(t=1/4\), where \(M_4=19\) and equation (2) gives \(M_6=385/4\). The sixth optimum has \(t=c_*\ne1/4\), hence its fourth moment is strictly larger than \(19\). The known global four-tap fourth-moment minimum is \(19\); the comparison does not claim the fourth-moment theorem as new.

## Verification
Run `python artifacts/verify.py` from the package root. The self-contained standard-library script independently constructs the Laurent coefficient table of the cubic polynomial, verifies (1) and (2) against direct complex coefficient convolution on a two-dimensional angular grid, tests the exact extremal value and its equality examples, exhausts the eight binary sign patterns, and checks the fourth/sixth tradeoff. The script's finite tests are supplementary; the exact algebraic identities and convexity argument above prove the universal statement.

## Relationship to prior work
Balister, Bollobás, Morris, Sahasrabudhe and Tiba (2019 preprint, 2020 publication) establish long binary Littlewood polynomial flatness in the uniform norm. Their theorem concerns arbitrarily large degree and existence of bounded upper and lower envelopes, not a degree-three, continuous-phase sixth-moment minimum or its full minimizer set. Schmidt (2013) relates unimodular polynomial fourth moments to correlation energy and studies asymptotic flatness, not the sixth-moment minimum at length four. Sankuru and Babu (2020) optimize integrated sidelobe level with iterative algorithms for unimodular sequences; their explicit objective is a fourth-moment autocorrelation quantity, rather than the present sixth moment. The published four-point phase-only fourth-moment support classification gives a different exact invariant (fourth rather than sixth moment), while a published sharp sixth-moment *maximum* for arbitrary four-term coefficients does not bound the present *minimum* from below. Those distinct results are acknowledged rather than duplicated.

## Limitations
The result is an exact, finite-support extremal fact, not an assertion of asymptotic optimality, downstream communication performance, or a theorem for arbitrary supports and exponents. It gives no quantitative optimal sixth moment for each finite phase alphabet separately. The binary count is finite and elementary; the algebraic obstruction to *all* finite root-of-unity alphabets is proved separately. Historical priority is not certified: older unindexed short-sequence tables or alternative moment-parametrization results could possibly contain an equivalent formula. Independent review has not been performed.

## References
1. P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe and M. Tiba, *Flat Littlewood Polynomials Exist*, arXiv:1907.09464v1, first posted 2019-07-22; *Annals of Mathematics* 192 (2020), 977–1004; doi:10.4007/annals.2020.192.3.6. Published primary MSC 42A05.
2. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1, first posted 2013-02-12; *Journal of Fourier Analysis and Applications* 19 (2013), 457–466.
3. *Sharp sixth-moment Fourier norm via four-term even-moment symmetrization*, published mathematical finding (2026); exact maximum, unlike the minimum here. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moment-fourier-norm-via-four-term-even-moment-symmet--f3e238ebf219 .
4. S. P. Sankuru and P. Babu, *Designing unimodular sequence with good auto-correlation properties via Block Majorization-Minimization method*, arXiv:2001.06267v1, first posted 2020-01-17.
5. *Four-point support geometry quantizes the phase-only fourth Fourier moment*, published mathematical finding (2026); exact fourth moment, unlike the sixth moment here. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-four-point-support-geometry-quantizes-the-phase-only-fourth-four--2b7f859e0b5c .
