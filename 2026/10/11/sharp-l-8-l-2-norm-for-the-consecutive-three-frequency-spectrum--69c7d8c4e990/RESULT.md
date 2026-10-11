# Sharp \(L^8/L^2\) norm for the consecutive three-frequency spectrum
## Finding
For \(F(t)=a+b e^{2\pi i t}+c e^{4\pi i t}\) on \(\mathbb T\) with normalized Haar measure, the sharp inequality \(\|F\|_8\le K_8(|a|^2+|b|^2+|c|^2)^{1/2}\) has \(K_8^8=\Psi(\tau_*)\), where \(\Psi(\tau)=(70\tau^4+560\tau^3+420\tau^2+56\tau+1)/(1+2\tau)^4\) and \(\tau_*\) is the unique positive root of \(35\tau^3-21\tau-2=0\). Equivalently, \(K_8^8\) is the unique positive root of \(1331X^3+403851X^2-4842915X-13488475=0\), numerically \(K_8^8=13.787723967226097408\ldots\) and \(K_8=1.388150559666132350\ldots\). Every nonzero extremizer, and only those extremizers, satisfies \(|a|=|c|\), \(|a|^2=\tau_*|b|^2\), and \(\arg a+\arg c-2\arg b\equiv0\pmod{2\pi}\); equivalently, up to a nonzero scalar and character modulation, it is \(\sqrt{\tau_*}+z+\sqrt{\tau_*}z^2\).

This gives the exact \(\Lambda(8)\) constant of the consecutive spectrum \(\{0,1,2\}\subset\mathbb Z\), together with all equality cases.

## Assumptions and scope
The circle \(\mathbb T=\mathbb R/\mathbb Z\) carries normalized Haar measure. The coefficients \(a,b,c\) are arbitrary complex numbers, not all zero. The norm is the usual \(L^8(\mathbb T)\) norm. No finite sampling or restriction on coefficient phases is imposed.

Put \(z=e^{2\pi i t}\). The theorem concerns the three-dimensional Fourier subspace spanned by \(1,z,z^2\). Scalar multiplication and multiplication of \(F\) by a character do not change the norm ratio.

## Proof
Write
\[
F(z)^4=\sum_{k=0}^{8}d_k z^k.
\]
Parseval gives
\[
\|F\|_8^8=\|F^4\|_2^2=\sum_{k=0}^{8}|d_k|^2.
\]
The coefficients are
\[
\begin{aligned}
d_0&=a^4, & d_1&=4a^3b,\\
d_2&=6a^2b^2+4a^3c, & d_3&=4ab^3+12a^2bc,\\
d_4&=b^4+12ab^2c+6a^2c^2, & d_5&=4b^3c+12abc^2,\\
d_6&=6b^2c^2+4ac^3, & d_7&=4bc^3,\\
d_8&=c^4.
\end{aligned}
\]
For fixed magnitudes \(|a|,|b|,|c|\), the triangle inequality applied separately to each \(d_k\) shows that the moment is maximized when all collision monomials align. If \(abc\ne0\), equality in the formula for \(d_2\) already forces
\[
\arg a+\arg c-2\arg b\equiv0\pmod{2\pi}.
\]
This condition also aligns every other collision, because two monomials contributing to the same \(d_k\) differ by an integer multiple of the elementary relation \((1,-2,1)\). Thus it suffices to maximize over positive real \(a,b,c\).

Set
\[
A=a^2+c^2,\qquad B=b^2,\qquad R=ac.
\]
Direct expansion yields the exact identity
\[
\begin{aligned}
\|F\|_8^8={}&A^4+16A^3B+36A^2B^2+16AB^3+B^4\\
&+48A^2BR+12A^2R^2+96AB^2R+96ABR^2\\
&+24B^3R+84B^2R^2+48BR^3+6R^4.
\end{aligned}
\]
For fixed \(A\) and \(B\), every coefficient of the positive powers of \(R\) is nonnegative and the derivative with respect to \(R\) is strictly positive whenever \(R>0\). Since
\[
R=ac\le\frac{a^2+c^2}{2}=\frac A2,
\]
the maximum has \(a=c\) in magnitude. Boundary faces, where one coefficient vanishes, reduce to a two-character problem and have eighth-power ratio at most
\[
2^{-4}\binom84=\frac{35}{8},
\]
strictly below the interior value obtained below. Hence every global extremizer is interior.

Write \(a=c>0\) after phase alignment, and put
\[
\tau=\frac{a^2}{b^2}>0.
\]
Homogeneity reduces the eighth power of the norm ratio to
\[
\Psi(\tau)=\frac{70\tau^4+560\tau^3+420\tau^2+56\tau+1}{(1+2\tau)^4}.
\]
Differentiation gives the exact factorization
\[
\Psi'(\tau)=-\frac{24(35\tau^3-21\tau-2)}{(1+2\tau)^5}.
\]
The cubic \(h(\tau)=35\tau^3-21\tau-2\) decreases on \((0,1/\sqrt5)\), is negative at its unique positive critical point, and then increases to \(+\infty\). It therefore has exactly one positive zero \(\tau_*\), and the displayed derivative changes sign from positive to negative there. Thus \(\tau_*\) is the unique global maximizer.

Eliminating \(\tau_*\) from \(h(\tau_*)=0\) and \(X=\Psi(\tau_*)\) gives
\[
1331X^3+403851X^2-4842915X-13488475=0.
\]
This cubic has exactly one positive root, which is \(K_8^8\). The equality conditions accumulated above give the stated complete extremizer family.

## Verification
The accompanying `verify.py` uses exact integer polynomial arithmetic to reconstruct the coefficients of \(F^4\), verify the \((A,B,R)\) moment identity, verify the derivative factorization and the elimination polynomial, isolate the unique positive root of \(35\tau^3-21\tau-2\), and check the numerical values. Deterministic numerical samples are included only as stress tests; the proof of the theorem is the exact analytic argument above.

A successful replay prints a line beginning `VERIFY_OK` and reports approximations to \(\tau_*\), \(K_8^8\), and \(K_8\).

## Relationship to prior work
Michels develops the classical \(\Lambda(p)\)-set framework and the optimal \(L^p/L^2\) constant for character sets, but the inspected result is structural and asymptotic rather than an evaluation of this finite three-character \(p=8\) constant. Neuwirth studies the same consecutive three-frequency geometry through the Sidon, or \(L^\infty\), extremal problem and obtains its exact Sidon constant; that endpoint does not determine the \(L^8/L^2\) optimization here.

A published published-finding corpus finding on even moments of unimodular three-frequency sums determines the first moment at which phase becomes visible and its phase response when all coefficient magnitudes are fixed. The present theorem instead optimizes over arbitrary coefficient magnitudes and finds the unique nontrivial magnitude ratio \(\tau_*\), so that phase-only result does not imply this sharp operator norm or its equality cases.

## Limitations
The theorem is specific to the consecutive three-frequency spectrum and to the eighth moment. It does not give a general closed formula for arbitrary three-point spectra or arbitrary even exponents. The originality comparison cannot exclude an older equivalent formula hidden under substantially different notation; no such formula was found in the inspected sources or targeted database searches.

## References
1. Carsten Michels, *\(\Lambda(p)\)-sets and the limit order of operator ideals*, arXiv:math/9904176v1, first public April 30, 1999.
2. Stefan Neuwirth, *The Sidon constant of sets with three elements*, arXiv:math/0102145v1, first public February 19, 2001.
3. published-finding corpus, *Even phase moments recover the normalized geometry of a three-frequency spectrum*, identifier `2026/10/4/SCOPE-even-phase-moments-recover-the-normalized-geometry-of-a-three-fr--7849dda51c79`.
