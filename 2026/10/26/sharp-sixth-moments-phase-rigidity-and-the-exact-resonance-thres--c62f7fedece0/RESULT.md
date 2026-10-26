# Sharp sixth moments, phase rigidity, and the exact resonance threshold for two dihedral characters

## Finding

For every integer \(n\ge13\), let \(D_n\) be the dihedral group of order \(2n\), with normalized counting measure. Let \(\chi_1,\chi_2\) be the two distinct two-dimensional irreducible characters given on rotations by
\[
\chi_j(r^k)=2\cos(2\pi jk/n),\qquad
\chi_j(sr^k)=0,\quad j\in\{1,2\}.
\]
For arbitrary complex \(a,b\), put \(S=|a|^2+|b|^2\). Then
\[
\boxed{\frac1{2n}\sum_{g\in D_n}|a\chi_1(g)+b\chi_2(g)|^6
\le\left(\frac{70\sqrt{21}}3-80\right)S^3.}
\]
The constant \(K=70\sqrt{21}/3-80=26.926766215636\ldots\) is optimal. Writing \(x_*=\sqrt{21}/3-1\), every nonzero equality case is exactly
\[
\boxed{(a,b)=\lambda\bigl(\sqrt{x_*},\,\pm\sqrt{1-x_*}\bigr),
\quad\lambda\in\mathbb C\setminus\{0\}.}
\]
The following **exact global stability identity** holds for every nonzero coefficient pair, with \(x=|a|^2/S\):
\[
\boxed{\begin{aligned}
KS^3-\|a\chi_1+b\chi_2\|_{L^6(D_n)}^6
={}&15S^3(x-x_*)^2\left(1+x+\frac{2\sqrt{21}}3\right)\\
&+12S(6+x)\bigl(\operatorname{Im}(a\overline b)\bigr)^2.
\end{aligned}}
\]
Finally, the threshold is sharp: for every integer \(5\le n\le12\), both \(\chi_1\) and \(\chi_2\) are still inequivalent irreducible characters, but their sharp sixth-moment constant is **strictly larger** than \(K\). The exact constants for these eight lower orders are not claimed.

## Assumptions and scope

Here \(D_n=\langle r,s\mid r^n=s^2=e,\ srs=r^{-1}\rangle\), and integration means uniform averaging over all \(2n\) group elements, not averaging only over rotations. Coefficients are unrestricted complex numbers. The character normalization uses ordinary traces, not dimension-normalized traces. For \(n\ge5\), the characters \(\chi_1\) and \(\chi_2\) are pairwise distinct degree-two irreducibles and hence orthonormal. Consequently \(S=\|a\chi_1+b\chi_2\|_{L^2(D_n)}^2\). The strict low-order comparison concerns \(n=5,6,\ldots,12\), not \(n<5\), where the two-character description can change.

## Proof

**1. Reduction to a four-frequency Laurent polynomial.** Take \(\zeta=e^{2\pi i/n}\) and let
\[
F(z)=a(z+z^{-1})+b(z^2+z^{-2}).
\]
The two induced two-dimensional characters vanish at every reflection, so
\[
\|a\chi_1+b\chi_2\|_6^6=\frac1{2n}\sum_{k=0}^{n-1}|F(\zeta^k)|^6.
\]
Since \(|F(z)|^6\) is a Laurent polynomial with frequencies in \([-12,12]\) on the unit circle, for \(n\ge13\) its discrete average retains precisely its constant coefficient. This proves stabilization at every such order, including \(n=13\).

**2. Exact mixed moments.** With \(X(z)=z+z^{-1}\) and \(Y(z)=z^2+z^{-2}\), constant-coefficient extraction from \((z+z^{-1})^{6-j}(z^2+z^{-2})^j\) gives
\[
\frac12\int_{\mathbb T}X^{6-j}Y^j\,dm
=\begin{cases}
10,&j=0,6,\\
7,&j=2,\\
6,&j=4,\\
0,&j=1,3,5.
\end{cases}
\]
The factor \(1/2\) is the proportion of rotations inside the dihedral group. It can also be checked directly: the coefficient of \(z^0\) counts choices of signs with \((6-j)\) steps of size one and \(j\) steps of size two, divided by two.

**3. Exact complex-phase dependence.** Put \(p=|a|^2\), \(q=|b|^2\), and \(u=\operatorname{Re}(a\overline b)\). Because \(X,Y\) are real on the unit circle,
\[
|aX+bY|^2=pX^2+qY^2+2uXY.
\]
The odd mixed moments in Step 2 vanish, so expanding the cube yields the exact identity
\[
\|a\chi_1+b\chi_2\|_6^6
=10(p^3+q^3)+21p^2q+18pq^2+(84p+72q)u^2.
\]
The identity \(u^2=pq-[\operatorname{Im}(a\overline b)]^2\) shows that maximal phase alignment is necessary whenever \(a,b\ne0\), and explicitly gives the nonnegative phase defect \(12S(6+x)[\operatorname{Im}(a\overline b)]^2\).

**4. One-variable global maximum and exact gap.** For \(S>0\), let \(x=p/S\in[0,1]\). With aligned phases the normalized sixth moment is
\[
P(x)=10\bigl[x^3+(1-x)^3\bigr]+105x^2(1-x)+90x(1-x)^2
=-15x^3-45x^2+60x+10.
\]
Its derivative is \(P'(x)=-15(3x^2+6x-4)\). This quadratic has exactly one zero in \([0,1]\), namely \(x_*=\sqrt{21}/3-1\); the derivative is positive before that point and negative afterward. Therefore it is the unique global amplitude optimizer. Substitution gives \(P(x_*)=K\), and direct polynomial expansion gives the exact factorization
\[
K-P(x)=15(x-x_*)^2\left(1+x+\frac{2\sqrt{21}}3\right).
\]
Combining this with Step 3 proves the claimed deficit identity. Both terms are nonnegative. Since the first term vanishes only at \(x=x_*\) and the second only when \(\operatorname{Im}(a\overline b)=0\), the complete complex equality classification follows. If \(S=0\), both sides of the inequality vanish and the separate deficit formula need not be parameterized by \(x\).

**5. Optimality of the order threshold.** Choose the positive aligned extremal amplitudes \(a=\sqrt{x_*}\), \(b=\sqrt{1-x_*}\). Because \(F\) is then real on the unit circle, \(|F|^6=F^6\), whose Laurent coefficients are all nonnegative. For each \(5\le n\le12\), the coefficient of \(z^n\) in \(F^6\) is strictly positive: six choices of signs and step lengths in \(\{1,2\}\) sum to \(n\). Examples for \(n=5\) and \(n=12\) are \(2+1+1+1+1-1\) and \(2+2+2+2+2+2\); the intermediate integers follow by taking \(n-6\) steps of size two and the rest of size one for \(6\le n\le12\). The finite cyclic average selects both the zero coefficient and every coefficient whose index is divisible by \(n\). Thus at the same norm-one coefficient pair the sixth moment is strictly larger than the stable value \(K\). This proves the sharp threshold without asserting the lower-order optima.

## Verification

The standalone `artifacts/verify.py` enumerates Laurent coefficients, checks all seven mixed moments, tests the exact complex sixth-moment polynomial on 850 deterministic coefficient pairs and four stable orders, compares with direct dihedral-group quadrature in orders 5 through 22, and tests the exact deficit identity and positivity on 700 coefficient pairs, and verifies the radical constant and stability factorization coefficient-by-coefficient in the exact field \(\mathbb Q(\sqrt{21})\). It also checks that each order 5 through 12 contributes an additional positive Fourier coefficient. The recorded output is `artifacts/verification_output.txt`. These finite tests corroborate the identities; the analytical proof establishes them for all permitted group orders and complex coefficients.

## Relationship to prior work

The classical character-orthogonality and root-of-unity identities used in Steps 1–3 are standard. Doktorski (2020) proves broad Nikol'skii-type estimates for trigonometric polynomials and frequency supports; his statements concern scale/order estimates and do not yield this exact two-character sixth-moment constant or equality classification. Leong and Mossinghoff (2024) study the optimization of nonnegative cosine polynomials in a different number-theoretic objective; their cosine harmonics do not imply this normalized sixth-moment optimization. Related exact results for unrestricted **four consecutive** Fourier frequencies and for **two one-dimensional** Fourier characters are incomparable: the dihedral packet corresponds to the four cyclic frequencies \(\{-2,-1,1,2\}\), constrained to have two equal antipodal coefficient pairs, and its four frequencies are not consecutive. The current conclusion depends on the specific interaction of these two nonlinear irreducible characters, including its explicit global phase and amplitude defects.

## Limitations

The theorem determines the sharp constant only at orders \(n\ge13\). At orders 5 through 12 it proves strict enhancement but does not determine their exact constants or maximizers. The four-frequency character packet is not an unrestricted four-frequency Fourier synthesis space, and no claim of a general multi-character inequality is made. An equivalent formula could appear in older tables of low-degree trigonometric Nikolskii constants or finite-group character norms; priority has not been independently established.

## References

1. L. R. Ya. Doktorski, *Nikol’skii–Type Inequalities for Trigonometric Polynomials for Lorentz–Zygmund Spaces*, Journal of Function Spaces (2020), DOI: 10.1155/2020/6853723, first published 2020-02-03.
2. N. Leong and M. J. Mossinghoff, *A note on trigonometric polynomials for lower bounds of \(\zeta(s)\)*, arXiv:2404.05928 (2024-04-09).
3. Related public mathematical results on four-consecutive-frequency sixth moments and finite-order two-character even moments, identifiers `f3e238ebf219` and `22b99d88ea1a`, respectively. Their assumptions and conclusions are compared above.
