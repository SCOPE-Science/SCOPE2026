# Sharp fourth-moment extension and nine phase-rigid optimizers on the ternary split cone
## Finding
Let \(C=\{(x,y)\in\mathbb F_3^2:xy=0\}\), the five-point zero set of a split nondegenerate quadratic form. For any nontrivial additive character \(\psi\) of \(\mathbb F_3\), define
\[
\mathcal E_Cf(\xi)=\frac13\sum_{z\in C}f(z)\psi(\xi\cdot z),\qquad \xi\in\mathbb F_3^2.
\]
The sharp fourth-power extension inequality, using counting measure on the target and the normalized source norm, is
\[
\boxed{\sum_{\xi\in\mathbb F_3^2}|\mathcal E_Cf(\xi)|^4\le
\frac{729+33\sqrt{33}}{296}\left(\frac13\sum_{z\in C}|f(z)|^2\right)^2.}
\]
Every nonzero optimizer has the following form. Fix \(e_1=(1,0)\), \(e_2=(0,1)\), \(\omega=e^{2\pi i/3}\), and \(r_*=(\sqrt{33}-1)/4\). For some nonzero complex scalar \(\lambda\) and some \(j,k\in\{0,1,2\}\),
\[
\boxed{f(0)=\lambda r_*,\quad f(e_1)=\lambda\omega^j,\quad f(-e_1)=\lambda\omega^{-j},\quad f(e_2)=\lambda\omega^k,\quad f(-e_2)=\lambda\omega^{-k}.}
\]
Conversely all these functions attain equality. Thus there are exactly nine complex-projective optimizer classes. The center-to-arm modulus ratio is strictly greater than one; in particular, constant-modulus data are not extremal.

## Assumptions and scope
The field and entire support are fixed: \(\mathbb F_3\) and the full split cone \(C=\{0,\pm e_1,\pm e_2\}\). Every complex function on this support is permitted, including vanishing coefficients. The target measure is unnormalized counting measure and the extension kernel contains the factor \(1/3\). The statement concerns the fourth power of the extension norm, not the unsquared operator norm. All equality classifications are modulo a single nonzero complex scalar.

## Proof
**1. Exact convolution normalization.** Extend \(f\) by zero to \(G=\mathbb F_3^2\) and write \(f*f(t)=\sum_{u+v=t}f(u)f(v)\). Character orthogonality on the nine-element group gives
\[
\sum_{\xi\in G}|\mathcal E_C f(\xi)|^4=\frac19\sum_{t\in G}|f*f(t)|^2.
\]
Writing \(P=\sum_C|f|^2\), the sharp coefficient is precisely the maximum of \(\|f*f\|_2^2/P^2\) over nonzero \(f\).

**2. Remove phases without losing the equality information.** Coefficientwise convolution satisfies \(|f*f(t)|\le (|f|*|f|)(t)\), so it suffices first to optimize five nonnegative numbers. Write the center magnitude as \(c\), opposite first-axis magnitudes as \(x,y\), and opposite second-axis magnitudes as \(u,v\). The nine convolution entries have magnitudes bounded by those of
\[
\begin{array}{c|c}
\text{sum}&\text{nonnegative convolution coefficient}\\\hline
0&c^2+2xy+2uv\\
 e_1,-e_1&2cx+y^2,\ 2cy+x^2\\
 e_2,-e_2&2cu+v^2,\ 2cv+u^2\\
 \pm e_1\pm e_2&2xu,\ 2xv,\ 2yu,\ 2yv
\end{array}
\]
The squared sum of the nine right-hand entries is the exact nonnegative convolution energy \(Q\).

**3. Equalize the two entries on each axis.** Put \(h=x^2+y^2\), \(t=2xy\), \(H=u^2+v^2\), and \(T=2uv\), so \(0\le t\le h\), \(0\le T\le H\), and \(P=c^2+h+H\). Direct expansion yields
\[
Q=(c^2+t+T)^2+4c^2(h+H)+2ct\sqrt{h+t}+2cT\sqrt{H+T}
+h^2+H^2-\frac12(t^2+T^2)+4hH.
\]
Keeping \(c,h,H,T\) fixed, the derivative in \(t\), wherever the square root denominator is nonzero, is
\[
2c^2+t+2T+2c\sqrt{h+t}+\frac{ct}{\sqrt{h+t}}\ge0.
\]
The analogous derivative in \(T\) is also nonnegative. Endpoints follow by continuity. If \(c>0\) and both axis masses are positive, these derivatives are strictly positive, so maximizing requires \(t=h\) and \(T=H\), equivalently \(x=y\) and \(u=v\). The global strict case will be proved below.

**4. Balance the two axes or eliminate one.** After the equalization, write \(M=h+H\), where \(M>0\), and \(w=\sqrt{hH}/M\in[0,1/2]\). The nonnegative convolution energy becomes
\[
Q=P^2+4c^2M+2\sqrt2\,cM^{3/2}(1-w)\sqrt{1+2w}
+\frac12M^2+3M^2w^2.
\]
For fixed \(c,M\), the derivative of the \(w\)-dependent part is
\[
6Mw\left(M-\frac{\sqrt2c\sqrt M}{\sqrt{1+2w}}\right).
\]
The factor in parentheses is increasing in \(w\); hence any interior stationary point is a minimum, and a maximum occurs at \(w=0\) (one axis) or \(w=1/2\) (balanced axes). If \(M=0\), the ratio is one.

At \(w=0\), the function is supported on the three-point line subgroup of \(G\). Young's convolution inequality on that order-three subgroup gives \(\|f*f\|_2^2\le3P^2\). For \(w=1/2\), the four arm magnitudes equal \(a>0\). Set \(r=c/a\). The quotient is
\[
F(r)=\frac{r^4+24r^2+16r+36}{(r^2+4)^2},\qquad r\ge0.
\]
Its derivative factorizes exactly as
\[
F'(r)=-\frac{16(r+1)(2r^2+r-4)}{(r^2+4)^3}.
\]
Therefore the sole positive maximizer is \(r=r_*=(\sqrt{33}-1)/4\), and direct substitution gives \(F(r_*)=(729+33\sqrt{33})/296\). Since \(F(1)=77/25>3\), no endpoint or one-axis configuration is extremal. Thus the center is nonzero, both axes have positive mass, all four arms have equal positive magnitude, and their common modulus has the claimed ratio to the center.

**5. All phases.** Equality in \(|f*f(t)|\le (|f|*|f|)(t)\) holds for every sum fiber. Write the phases of \(f(0)\) and \(f(\pm e_i)\) as \(\theta_0,\theta_{i,+},\theta_{i,-}\) modulo \(2\pi\). The zero fiber requires
\[\theta_{i,+}+\theta_{i,-}\equiv 2\theta_0\pmod{2\pi}.\]
The \(e_i\) fiber requires
\[\theta_0+\theta_{i,+}\equiv2\theta_{i,-}\pmod{2\pi}.\]
Eliminating \(\theta_{i,-}\) gives \(3(\theta_{i,+}-\theta_0)\equiv0\pmod{2\pi}\). Therefore, modulo global phase, the values on each axis are the conjugate pair of cubic roots of unity. No further cross-axis relation arises, since each off-axis sum has one unordered pair. The independent indices \(j,k\in\mathbb Z_3\) give exactly nine classes. Each listed phase pattern is a restricted additive character, so its product phase depends only on the sum and all triangle inequalities are equalities. This completes both sharpness and the optimizer classification.

## Verification
The standalone standard-library script `artifacts/verify.py` computes all nine convolution entries and all nine Fourier outputs independently. It checks Plancherel and the sharp inequality for 2,000 deterministic random complex vectors and exactly tests the nine classified character patterns to floating-point tolerance. It separately checks the radical substitution. These finite numerical checks corroborate the exact algebraic proof above; they are not claimed to certify any inequality beyond the proved scope.

## Relationship to prior work
Iosevich, Koh, Lee, Pham and Shen, *On restriction estimates for the zero radius sphere over finite fields* (arXiv:1806.11387, initially 29 June 2018), analyze finite-field zero-radius quadratic surfaces and restriction exponent questions. Their zero-radius formulation motivates examining flat subspaces, but their main sharpness addresses exponent ranges, not the present optimal numerical fourth-moment coefficient and all complex extremizers for the five-point ternary split cone. González-Riquelme and Oliveira e Silva, *Sharp extension inequalities on finite fields* (arXiv:2405.16647, initially 26 May 2024), treat parabolae, paraboloids and four-dimensional cones; their sharp constants do not cover this two-dimensional union of intersecting lines. González-Riquelme and Ismoilov, *Maximizers of the \(L^2\to L^4\) Fourier extension inequality for cones in finite fields* (arXiv:2509.05600), concern punctured four-dimensional quadratic cones, not the two-dimensional five-point cone here.

Two related published finite-Fourier results were compared at the level of full statements: *Complete exact-support five-point Fourier spectrum on \(\mathbb F_3^2\)* counts Fourier zeros for five-point functions but does not optimize the fourth moment; *Small-field phase dichotomy for anisotropic sphere extremizers* treats different three-dimensional anisotropic spheres, and its equality families do not imply this split-plane nonconstant-amplitude optimization.

## Limitations
This theorem concerns only the smallest odd-characteristic split plane, not all odd finite fields or higher-dimensional cones. It is a self-contained exact sharp norm-and-equality calculation, not an infinite-family extension theorem. A literature search is not a uniqueness proof: earlier unindexed additive-energy or finite-frame literature may contain an equivalent case. No independent audit has been performed.

## References
1. A. Iosevich, D. Koh, S. Lee, T. Pham and C.-Y. Shen, *On restriction estimates for the zero radius sphere over finite fields*, arXiv:1806.11387v1 (2018-06-29), https://arxiv.org/abs/1806.11387.
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1 (2024-05-26), https://arxiv.org/abs/2405.16647.
3. C. González-Riquelme and T. Ismoilov, *Maximizers of the \(L^2\to L^4\) Fourier extension inequality for cones in finite fields*, arXiv:2509.05600v1 (2025-09-06), https://arxiv.org/abs/2509.05600.
4. *Complete exact-support five-point Fourier spectrum on \(\mathbb F_3^2\)*, published finite-Fourier result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-complete-exact-support-five-point-fourier-spectrum-on-f3-2--ae1a86146a92.
5. *Small-field phase dichotomy for anisotropic sphere extremizers*, published finite-Fourier result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-small-field-phase-dichotomy-for-anisotropic-sphere-extremizers--973050ba74a9.
