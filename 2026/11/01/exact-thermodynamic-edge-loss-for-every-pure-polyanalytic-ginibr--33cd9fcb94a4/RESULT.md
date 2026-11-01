# Exact thermodynamic edge loss for every pure polyanalytic Ginibre level

## Finding

Fix an integer \(r\geq 0\). In the normalization of [1], let \(H_{j,r}\) be the orthonormal complex Hermite polynomials in \(L^2(\mathbb C,e^{-\pi|z|^2}dA(z))\), and define the finite pure-level one-point intensity by
\[
\rho_{r,N}(z)=e^{-\pi|z|^2}\sum_{j=0}^{N-1}|H_{j,r}(z,\bar z)|^2,
\qquad N=1,2,\ldots.
\]
Put \(D_N=\{z\in\mathbb C:\pi|z|^2<N\}\). Then the sharp limit exists and is strictly positive:
\[
\boxed{\lim_{N\to\infty}\frac{\|\rho_{r,N}-\mathbf1_{D_N}\|_{L^1(\mathbb C,dA)}}{\sqrt N}
=c_r,\qquad
c_{2m}=\sqrt{\frac2\pi}(4m+1)\frac{\binom{2m}{m}}{4^m},\quad
c_{2m+1}=\sqrt{\frac2\pi}(4m+2)\frac{\binom{2m}{m}}{4^m}.}
\]
Here \(m\in\mathbb N_0\). In particular \(c_0=\sqrt{2/\pi}\), \(c_1=2\sqrt{2/\pi}\), \(c_2=\frac52\sqrt{2/\pi}\) and \(c_3=3\sqrt{2/\pi}\). The exact coefficient has the high-level asymptotic \(c_r\sim (4/\pi)\sqrt r\) as \(r\to\infty\), taken **after** the fixed-level limit \(N\to\infty\).

The asymptotic yields a matching lower bound of order \(\sqrt N\) at every fixed Landau level, making the earlier known upper-order estimate quantitatively sharp.

## Assumptions and scope

Area measure \(dA\) is ordinary planar Lebesgue measure. The Gaussian weight uses \(\pi\), so the reference disk has area exactly \(N\). The degree cutoff is on the first Hermite index \(j=0,\ldots,N-1\), with the second index \(r\) fixed. The theorem applies to these **finite pure** ensembles, not a sum of several occupied Landau levels or an unrelated spectral concentration truncation. All limits in the main statement take \(N\to\infty\) with \(r\) fixed; no joint uniformity in \(r\) and \(N\) is asserted.

For nonnegative integers \(j,r\), with \(a=\min(j,r)\), \(b=\max(j,r)\), let
\[
q_{j,r}(u)=e^{-u}\frac{a!}{b!}u^{b-a}[L_a^{b-a}(u)]^2\quad (u>0),
\]
where \(L_a^{b-a}\) is a generalized Laguerre polynomial. Under the substitution \(u=\pi|z|^2\), \(q_{j,r}\) is the radial contribution of the \((j,r)\) Hermite state. The standard Laguerre orthogonality and the infinite pure-level projection identity give
\[
\int_0^\infty q_{j,r}(u)\,du=1,
\qquad \sum_{j=0}^\infty q_{j,r}(u)=1.
\]
Consequently \(0\leq\rho_{r,N}\leq1\) and \(\int\rho_{r,N}\,dA=N\).

## Proof

**1. Exact reduction to tails.** The radial coordinate \(u=\pi|z|^2\) satisfies \(dA=du\) after angular integration. Equal total masses and the pointwise bound \(0\leq\rho_{r,N}\leq1\) imply the exact identity
\[
E_{r,N}:=\|\rho_{r,N}-\mathbf1_{D_N}\|_1
=2\int_N^\infty\sum_{j=0}^{N-1}q_{j,r}(u)\,du
=2\sum_{j=0}^{N-1}\Pr(U_{j,r}>N),
\]
where \(U_{j,r}\) has density \(q_{j,r}\). This identity is valid at finite \(N\), not merely asymptotically.

**2. Exact first two moments.** Multiplication by \(u\) in the orthogonal Laguerre basis is tridiagonal. Its diagonal coefficient is \(2a+(b-a)+1=j+r+1\), and the squares of adjacent off-diagonal coefficients add to \((a+1)(b+1)+ab\). Therefore
\[
\mathbb E U_{j,r}=j+r+1,
\qquad \operatorname{Var}(U_{j,r})=2jr+j+r+1.
\]
Both identities hold for all \(j,r\ge0\), including \(j<r\). In particular, for fixed \(r\) and \(0\le j<N\), the variance is at most \((2r+1)N+r+1\).

**3. A single-state Hermite edge law.** For \(j\ge r\), the finite Laguerre coefficient formula is equivalently
\[
L_r^{j-r}(u)=[t^r](1+t)^j e^{-ut}.
\]
Put \(u=j+s\sqrt j\) and \(t=x/\sqrt j\). Uniformly for \(s\) in compact real intervals and \(x\) on a fixed complex circle,
\[
(1+x/\sqrt j)^j e^{-(j+s\sqrt j)x/\sqrt j}
\longrightarrow e^{-x^2/2-sx}.
\]
Taking the \(r\)-th coefficient by Cauchy's formula proves
\[
j^{-r/2}L_r^{j-r}(j+s\sqrt j)
\longrightarrow\frac{(-1)^r}{r!}\operatorname{He}_r(s),
\]
where \(\operatorname{He}_r\) denotes the probabilists' Hermite polynomial, defined by
\(e^{sx-x^2/2}=\sum_{r\ge0}\operatorname{He}_r(s)x^r/r!\).
The local Poisson/Stirling estimate gives
\[
\sqrt j\,e^{-(j+s\sqrt j)}\frac{(j+s\sqrt j)^j}{j!}
\longrightarrow\frac{e^{-s^2/2}}{\sqrt{2\pi}}.
\]
Combining the identities in the explicit Laguerre density yields, locally uniformly in \(s\),
\[
\sqrt j\,q_{j,r}(j+s\sqrt j)
\longrightarrow f_r(s):=
\frac{e^{-s^2/2}}{\sqrt{2\pi}\,r!}\operatorname{He}_r(s)^2.
\]
The exact variance bound makes the centered-scaled laws tight, hence the pointwise density convergence gives weak convergence of \((U_{j,r}-j)/\sqrt j\) to the probability density \(f_r\). The latter is continuous and even.

**4. Uniformly controlled Riemann sum.** Write \(j=N-1-k\). For a fixed \(M>0\), with \(0\le k\le M\sqrt N\), the indices \(j\) tend uniformly to infinity and the standardized threshold \((N-j)/\sqrt j\) tends uniformly to \(k/\sqrt N\). Weak convergence to a continuous distribution implies uniform convergence of distribution functions, so
\[
\frac1{\sqrt N}\sum_{0\le k\le M\sqrt N}\Pr(U_{N-1-k,r}>N)
\longrightarrow\int_0^M\Pr(Y_r>s)\,ds,
\]
where \(Y_r\) has density \(f_r\). For the omitted indices \(k>M\sqrt N\), choose \(M\ge2\) and then \(N\) sufficiently large that \(N-\mathbb EU_{j,r}=k-r\ge k/2\). Chebyshev's inequality and the variance bound imply
\[
\frac1{\sqrt N}\sum_{k>M\sqrt N}\Pr(U_{N-1-k,r}>N)
\le\frac{C_r}{\sqrt N}\sum_{k>M\sqrt N}\frac{N}{k^2}
\le\frac{C'_r}{M}.
\]
Thus the omitted tail vanishes as \(M\to\infty\), and the tail integral identity gives
\[
\lim_{N\to\infty}\frac{E_{r,N}}{\sqrt N}
=2\int_0^\infty\Pr(Y_r>s)\,ds
=\mathbb E|Y_r|.
\]
The last equality uses the evenness of \(f_r\). This proves positivity and the sharp \(\sqrt N\) scale for every fixed \(r\).

**5. Exact evaluation of the constants.** Mehler's diagonal identity for probabilists' Hermite polynomials, valid for \(0\le t<1\), is
\[
\sum_{r=0}^\infty\frac{\operatorname{He}_r(s)^2}{r!}t^r
=\frac1{\sqrt{1-t^2}}\exp\left(\frac{ts^2}{1+t}\right).
\]
Multiplication by \(|s|e^{-s^2/2}/\sqrt{2\pi}\), followed by Tonelli's theorem and an elementary Gaussian integral, yields
\[
\sum_{r=0}^\infty c_rt^r
=\sqrt{\frac2\pi}\frac{(1+t)^2}{(1-t^2)^{3/2}}.
\]
Extracting even and odd coefficients gives precisely the two stated binomial formulas. Stirling's approximation for the central binomial coefficient gives \(c_r\sim4\sqrt r/\pi\) as \(r\to\infty\).

## Verification

The standalone `check.py` tests the first nine exact coefficients of the Mehler generating function, six Hermite absolute-moment integrals, thirty-five Laguerre-density normalizations, and four levels of finite-\(N\) intensity errors against the predicted limits. It passed 58 checks using SciPy and SymPy. For instance the normalized finite errors at \(N=256\) are approximately \(0.797625,1.595250,1.994062,2.391836\) for \(r=0,1,2,3\), compared with \(0.797885,1.595769,1.994711,2.393654\). Numerical tests do not establish the infinite-\(N\) claim: the proof is the moment/tightness/edge/Riemann-sum argument above.

## Relationship to prior work

Abreu, Gröchenig and Romero [1, Theorem 1.2] proved an \(O_r(\sqrt N)\) upper bound for these exact finite pure-level intensities and explicitly described sharpness at positive levels as expected, rather than proved. Their exact complex Hermite normalization, definition of the finite ensemble, and Laguerre-based radial law [1, Theorem 1.8] are used here. The contribution is the matching positive asymptotic constant **for every fixed level** and its closed binomial form.

Haimi and Hedenmalm [2] studied local and edge limits of polyanalytic ensembles, including full-level kernels; Haimi and Wennman [3] investigated central limit theorems for linear statistics, including pure levels. Their constructions are important antecedents. Neither of the inspected texts states the global, absolute \(L^1\) leading constant for the finite pure cutoffs above. Sharp perimeter bounds for **spectrally selected Weyl–Heisenberg ensembles** do not automatically give this constant for the **Hermite-index selected** finite pure ensembles, as [1] distinguishes the two operators.

## Limitations

The theorem is for fixed \(r\) and the specific disk/degree cutoff. No general-domain perimeter constant, joint limit with growing \(r\), point-process fluctuation theorem, or exact finite-\(N\) closed form is asserted. The literature-comparison conclusion is provisional: local edge expansions, radial Kostlan-type identities, or stronger unpublished results may indirectly imply the constant. No independent mathematical audit has been performed.

## References

[1] L. D. Abreu, K. Gröchenig and J. L. Romero, *Harmonic analysis in phase space and finite Weyl–Heisenberg ensembles*, arXiv:1704.03042, first publicly posted 2017-04-10, especially §1.2, Theorems 1.2 and 1.8, and §5.

[2] A. Haimi and H. Hedenmalm, *The polyanalytic Ginibre ensembles*, arXiv:1106.2975, first publicly posted 2011-06-15, especially the polyanalytic kernel and edge-limit sections.

[3] A. Haimi and A. Wennman, *A Central Limit Theorem for Fluctuations in Polyanalytic Ginibre Ensembles*, arXiv:1612.07974, first publicly posted 2016-12-23, especially §2 and the pure-level linear-statistics results.
