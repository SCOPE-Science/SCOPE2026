# Logarithmic frequency-splitting curvature of the nonharmonic Dirichlet sum

## Finding

For every **even integer** \(N\ge 2\), put
\[
P_{N,\varepsilon}(t)=\sum_{k=0}^{N-1}e^{ikt}+e^{i(N+\varepsilon)t},\qquad
\mathcal L_N(\varepsilon)=\int_{-\pi}^{\pi}|P_{N,\varepsilon}(t)|\,dt.
\]
There is a finite real number \(A_N=\mathcal L'_N(0)\) such that, as a real nonzero \(\varepsilon\to0\),
\[
\mathcal L_N(\varepsilon)=\mathcal L_N(0)+A_N\varepsilon+
 C_N\varepsilon^2\log\frac1{|\varepsilon|}+O_N(\varepsilon^2),
\]
where the **exact strictly positive coefficient** is
\[
C_N=\frac{16\pi^2}{(N+1)^3}\sum_{j=1}^{N/2} j^2
\sin\!\frac{\pi j}{N+1}\,\cos^2\!\frac{\pi j}{N+1}>0.
\]
Moreover the coefficients converge, along even \(N\to\infty\), to the explicit universal constant
\[
\lim_{N\to\infty\atop N\,\mathrm{even}}C_N
=\frac{32(3\pi-7)}{27\pi}=0.914762425734477\ldots.
\]
In particular \(\mathcal L_N\) has a first derivative but **no finite second derivative** at its equally spaced frequency vector: its positive symmetric second difference divided by \(\varepsilon^2\) grows like \(2C_N\log(1/|\varepsilon|)\).

## Assumptions and scope

The integration interval is the fixed unnormalized interval \([-\pi,\pi]\); all coefficients of the \(N+1\) exponential terms are exactly one. The integer \(N\) is even and fixed as \(\varepsilon\to0\); the \(O_N\) remainder is not asserted uniform in simultaneous \(N\)-\(\varepsilon\) limits. The displaced frequency is the upper endpoint \(N+\varepsilon\), not an arbitrary coefficient deformation. The coefficient limit is a *subsequent* \(N\to\infty\) limit. For small \(|\varepsilon|\) the frequencies remain distinct. No minimizing property among frequency sets is assumed or claimed.

## Proof

**1. Real Dirichlet baseline and all its zeros.** At \(\varepsilon=0\),
\[
P_{N,0}(t)=e^{iNt/2}D_N(t),\qquad
D_N(t)=\frac{\sin((N+1)t/2)}{\sin(t/2)},
\]
with the removable definition \(D_N(0)=N+1\). For even \(N\), \(D_N\) is nonzero at both integration endpoints and has exactly \(N\) simple interior zeros
\[
t_j=\frac{2\pi j}{N+1},\qquad j=\pm1,\ldots,\pm N/2.
\]
Their slopes satisfy
\[
|D_N'(t_j)|=\frac{N+1}{2|\sin(\pi j/(N+1))|}.
\]
The real baseline removes all possible complex-phase ambiguity at the zeros.

**2. Exact transverse velocities.** Multiply by the unimodular gauge \(e^{-iNt/2}\). The gauged family is
\[
G_N(t,\varepsilon)=D_N(t)+e^{iNt/2}(e^{i\varepsilon t}-1),
\]
so \(G_N(t,0)=D_N(t)\) is real, and
\[
\partial_\varepsilon G_N(t,0)
=-t\sin(Nt/2)+it\cos(Nt/2).
\]
The imaginary displacement transverse to the baseline real zero at \(t_j\) is therefore
\[
b_j=t_j\cos(Nt_j/2)=(-1)^jt_j\cos\frac{\pi j}{N+1}.
\]
In particular, every \(b_j\ne0\) for even \(N\). As the zero set has measure zero and the derivative of the modulus away from it is bounded by \(|t|\), dominated convergence gives
\[
A_N=-\int_{-\pi}^{\pi}
 t\sin(Nt/2)\operatorname{sgn}(D_N(t))\,dt.
\]
This establishes the existence and the displayed value of the first derivative.

**3. Local modulus lemma, including the error.** Let \(G(t,s)\) be smooth and complex-valued on a real neighborhood of \((t_0,0)\), real-valued at \(s=0\), with \(G(t_0,0)=0\), \(a=\partial_tG(t_0,0)\ne0\), and \(b=\operatorname{Im}\partial_sG(t_0,0)\ne0\). For any smooth cutoff \(\chi\) supported sufficiently close to \(t_0\),
\[
\int\chi(t)|G(t,s)|\,dt
=B_0+B_1s+\frac{\chi(t_0)b^2}{|a|}
 s^2\log\frac1{|s|}+O(s^2).
\]
To verify the coefficient and remainder, use \(u=\operatorname{Re}G(t,s)\), a smooth local coordinate by the inverse-function theorem. Then \(\operatorname{Im}G(t(u,s),s)=s h(u,s)\), with \(h(0,0)=b\). The integral becomes
\[
\int W(u,s)\sqrt{u^2+s^2h(u,s)^2}\,du,
\qquad W(0,0)=\frac{\chi(t_0)}{|a|},
\]
for a smooth compactly supported density \(W\). The integral of \(W(u,s)|u|\) has an ordinary Taylor expansion. Because \(h(u,s)=b+O(|u|+|s|)\) and \(W(u,s)=W(0,0)+O(|u|+|s|)\), the difference between its modulus defect and
\[
W(0,0)\int_{-\delta}^{\delta}
\bigl(\sqrt{u^2+b^2s^2}-|u|\bigr)\,du
\]
is \(O(s^2)\): the pointwise defect is bounded by a constant times \(s^2/(|u|+|s|)\), while the variation of \(h^2\) and of \(W\) supplies an additional \(O(|u|+|s|)\) factor. Finally direct integration (or evaluation at \(u=\delta\)) gives
\[
\int_{-\delta}^{\delta}
\bigl(\sqrt{u^2+b^2s^2}-|u|\bigr)\,du
=b^2s^2\log\frac1{|s|}+O(s^2).
\]
This proves the lemma with an actual bounded quadratic remainder, rather than just a leading-order heuristic.

**4. Summation over the complete zero set.** Choose disjoint smooth cutoffs at the \(N\) simple zeros, plus a complementary cutoff on which \(|D_N|\) stays bounded away from zero. The latter contribution has an ordinary second-order Taylor expansion. By the lemma the logarithmic coefficient is precisely
\[
\sum_{j=\pm1}^{\pm N/2}\frac{b_j^2}{|D_N'(t_j)|}
=\frac{16\pi^2}{(N+1)^3}
\sum_{j=1}^{N/2}j^2\sin\frac{\pi j}{N+1}
\cos^2\frac{\pi j}{N+1}.
\]
Each summand is strictly positive. All local remainder constants can depend on fixed \(N\), and there are finitely many cutoffs, giving the asserted \(O_N(\varepsilon^2)\). The symmetric second difference is \(2C_N\varepsilon^2\log(1/|\varepsilon|)+O_N(\varepsilon^2)\), which excludes a finite second derivative.

**5. Large-degree coefficient.** Replacing \(u\) by \(j/(N+1)\) expresses the coefficient as a Riemann sum,
\[
C_N=16\pi^2\frac1{N+1}\sum_{j=1}^{N/2}
\left(\frac{j}{N+1}\right)^2
\sin\frac{\pi j}{N+1}\cos^2\frac{\pi j}{N+1}.
\]
The integrand is continuous on \([0,1/2]\). Thus its limit is
\[
16\pi^2\int_0^{1/2}u^2\sin(\pi u)\cos^2(\pi u)\,du
=16\pi^2\frac{2(3\pi-7)}{27\pi^3}
=\frac{32(3\pi-7)}{27\pi}.
\]
Integration by parts, using \(\sin(\pi u)\cos^2(\pi u)=-\tfrac1{3\pi}\partial_u\cos^3(\pi u)\) and \(\cos^3v=(3\cos v+\cos3v)/4\), supplies the exact integral.

## Verification

The standalone \(check.py\) independently evaluates the finite sum, the closed-form Riemann integral and symmetric numerical second differences. For the latter it uses quadrature separated at the *exact* baseline zeros to resolve the narrow modulus layers. For each tested even \(N\), the slope of \(\bigl(\mathcal L_N(\varepsilon)+\mathcal L_N(-\varepsilon)-2\mathcal L_N(0)\bigr)/(2\varepsilon^2)\) against \(\log(1/\varepsilon)\) agrees with the analytical \(C_N\) within the stated numerical tolerance. These are finite checks, not an exhaustive or infinite proof; the lemma and exact identities above are the proof.

## Relationship to prior work

Jaming, Kellay and Saba, *The Littlewood problem and non-harmonic Fourier series* (first arXiv posting 2023-03-20), prove quantitative lower \(L^1\)-bounds for general real-frequency exponential sums and distinguish short and long integration intervals. Their Theorem 1.1 gives lower bounds or asymptotic Besicovitch norms, not this fixed-interval second variation at the consecutive integer spectrum. The Jaming–Saba survey (2023) includes the classical Dirichlet-kernel \(L^1\)-asymptotic and extensions of nonharmonic norm inequalities, but not this explicit frequency-displacement logarithm. Our result does **not** improve the universal Littlewood lower bound or resolve its extremal-frequency problem. Generic local \(\sqrt{u^2+s^2}\) calculus explains the type of logarithm; the new quantitative content asserted here is the complete Dirichlet-zero coefficient for every even degree and its nontrivial positive limiting value.

## Limitations

The result is local in a single frequency-displacement parameter; it treats even \(N\) to avoid baseline zeros on the integration boundary and does not assert any formula for odd degrees. The \(O_N\) control is not simultaneous in degree and perturbation. General frequency-vector Hessians, minimizers among arbitrary real spectra, and finite-noise estimates are not claimed. Historical-priority risk remains for unindexed local frequency-sensitivity calculations or general modulus-integral singularity results. Independent validation has not been performed.

## References

- P. Jaming, K. Kellay and C. Saba, *The Littlewood problem and non-harmonic Fourier series*, arXiv:2303.10919 (first submitted 2023-03-20), https://arxiv.org/abs/2303.10919.
- P. Jaming and C. Saba, *From Ingham to Nazarov's inequality: a survey on some trigonometric inequalities*, arXiv:2311.17714 (first submitted 2023-11-29), https://arxiv.org/abs/2311.17714.
- A. Zygmund, *Trigonometric Series*, Cambridge University Press, 1959; classical reference for Dirichlet-kernel integrals.
