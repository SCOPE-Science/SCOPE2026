# Sharp two-edge interference barrier for the interval Helson inequality

## Finding
For the Fourier convention \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i t\xi}\,dt\), let \(\Omega=(0,1)\), \(\omega(\xi)=2\min\{\xi,1-\xi\}\), and define the optimal interval constant
\[
C_{\mathrm{int}}=\sup_{0\ne f\in L^1(\mathbb R),\ \operatorname{supp}\widehat f\subset(0,1)}
\frac{\displaystyle\int_0^1\frac{|\widehat f(\xi)|^2}{\omega(\xi)}\,d\xi}{\|f\|_1^2}.
\]
For a nonzero \(H\in L^1(\mathbb R)\) with compact positive Fourier support \(\operatorname{supp}\widehat H\subset[\delta,S]\subset(0,\infty)\), and nonnegative \(a,b\) not both zero, consider the two mirrored edge packets
\[
f_\varepsilon(t)=\varepsilon\left[aH(\varepsilon t)+b e^{2\pi it}\overline{H(\varepsilon t)}\right],
\qquad 0<\varepsilon<\frac1{2S}.
\]
Put \(Q(H)=\|H\|_1^{-2}\int_0^\infty |\widehat H(u)|^2/u\,du\), and \(M(a,b)=(2\pi)^{-1}\int_0^{2\pi}|a+be^{i\theta}|\,d\theta\). Then the exact limit is
\[
\lim_{\varepsilon\downarrow0}\frac{\displaystyle\int_0^1\frac{|\widehat f_\varepsilon(\xi)|^2}{\omega(\xi)}\,d\xi}{\|f_\varepsilon\|_1^2}
=\frac{a^2+b^2}{2M(a,b)^2}\,Q(H).
\]
The supremum of this limit over all permitted \(H,a,b\) is exactly
\[
\boxed{\frac{\pi^2}{16}=0.616850275\ldots},
\]
with optimal amplitude ratio \(a=b>0\), uniquely up to common positive scaling. In particular, the full (unrestricted) interval Helson constant obeys the rigorous bounds
\[
\boxed{\frac{\pi^2}{16}\le C_{\mathrm{int}}\le1}.
\]
**Sharpness concerns the specified two-mirrored-edge concentration model, not the unresolved unrestricted optimal interval constant.**

## Assumptions and scope
The support of a Fourier transform is its distributional support; the compact-support condition on \(H\) ensures that for small \(\varepsilon\), the two spectra are disjoint compact subsets of \(\Omega\). No smoothness, symmetry, reality, or normalization of \(H\) is assumed beyond \(L^1\) and the support condition. The coefficient convention uses \(a,b\ge0\), which is sufficient since constant phase differences do not affect the averaged limit. The case \(a=0\) or \(b=0\) is included. Everything is in one real Fourier variable and corresponds to MSC2020 42A38.

## Proof
**1. Exact weight and numerator.** For \(0<\xi<1\), \(\Omega\cap(2\xi-\Omega)\) has length \(2\min\{\xi,1-\xi\}\). Fourier scaling and reflection give
\[
\widehat f_\varepsilon(\xi)=a\widehat H(\xi/\varepsilon)
+b\overline{\widehat H((1-\xi)/\varepsilon)}.
\]
The two summands have disjoint support for \(2\varepsilon S<1\). Their weighted squared integrals each use the local boundary weight \(2\varepsilon u\), so exactly
\[
\int_0^1\frac{|\widehat f_\varepsilon(\xi)|^2}{\omega(\xi)}\,d\xi
=\frac{a^2+b^2}{2}\int_0^\infty\frac{|\widehat H(u)|^2}{u}\,du.
\]
This equality has no limiting error.

**2. Averaged \(L^1\) interference.** Substitute \(u=\varepsilon t\):
\[
\|f_\varepsilon\|_1
=\int_{\mathbb R}|aH(u)+b e^{2\pi i u/\varepsilon}\overline{H(u)}|\,du.
\]
For fixed \(u\) the integral over a complete carrier phase equals \(|H(u)|M(a,b)\) after rotating by the phase of \(H(u)\). The periodic averaging lemma, first for compactly supported continuous envelopes and then by \(L^1\)-approximation using the Lipschitz bound for absolute values, yields
\[
\|f_\varepsilon\|_1\longrightarrow M(a,b)\|H\|_1.
\]
Combining both steps proves the displayed limit.

**3. Half-line Carleman constant, including sharpness.** Every positive-frequency \(H\in L^1\) has upper-half-plane Hardy factorization \(H=UV\) with \(U,V\in H^2\) and \(\|U\|_2\|V\|_2=\|H\|_1\). On \(u>0\), \(\widehat H(u)=\int_0^u\widehat U(v)\widehat V(u-v)\,dv\). Cauchy–Schwarz with the interval of length \(u\), followed by Tonelli and Plancherel, gives
\[
\int_0^\infty\frac{|\widehat H(u)|^2}{u}\,du
\le\|U\|_2^2\|V\|_2^2=\|H\|_1^2.
\]
Thus \(Q(H)\le1\). It is sharp even under the compact positive-support restriction: \(H_0(t)=(1-2\pi it)^{-2}\) satisfies \(\widehat H_0(u)=ue^{-u}\mathbf1_{u>0}\), \(\|H_0\|_1=1/2\), and \(\int_0^\infty |\widehat H_0(u)|^2/u\,du=1/4\). Take a real smooth cutoff \(\chi\) with \(0\le\chi\le1\), \(\chi=1\) on \([-1,1]\), and \(\chi=0\) outside \([-2,2]\), and set
\[
H_R(t)=e^{2\pi i t/R}\,\mathcal F^{-1}\left[\chi(\cdot/R)\widehat H_0\right](t),\quad R\to\infty.
\]
Each \(H_R\in L^1\) has Fourier support in \([1/R,2R+1/R]\). Indeed its unmodulated factor is convolution of \(H_0\) with the \(L^1\) approximate identity \(\mathcal F^{-1}[\chi(\cdot/R)]\). Hence \(\|H_R-H_0\|_1\to0\), while dominated convergence gives \(\int_0^\infty|\widehat H_R(u)|^2/u\,du\to1/4\). Therefore \(\sup Q(H)=1\) in the admissible compact class.

**4. Exact amplitude optimization.** Write \(s=a^2+b^2>0\), \(c=2ab/s\in[0,1]\), and
\[
m(c)=\frac1{2\pi}\int_0^{2\pi}\sqrt{1+c\cos\theta}\,d\theta.
\]
Then \(M(a,b)=\sqrt{s}\,m(c)\). Pairing \(\theta\) with \(\theta+\pi\) shows that for \(0<c<1\), the derivative of \(m(c)\) is strictly negative: for every nonzero \(x\in(-1,1)\), the term \(x[(1+cx)^{-1/2}-(1-cx)^{-1/2}]\) is negative. Thus the amplitude factor \(s/(2M(a,b)^2)=1/(2m(c)^2)\) is uniquely maximized at \(c=1\), equivalent to \(a=b>0\). At this point \(M(a,a)=4a/\pi\); the factor equals \(\pi^2/16\). Together with step 3 this proves sharpness.

**5. Bounds for the full constant.** The lower bound follows from the admissible two-edge family. For the upper bound, pointwise on \(0<\xi<1\),
\[
\frac1{2\min(\xi,1-\xi)}\le\frac12\left(\frac1\xi+\frac1{1-\xi}\right).
\]
The half-line inequality in step 3 bounds \(\int_0^1|\widehat f(\xi)|^2/\xi\,d\xi\) by \(\|f\|_1^2\); apply it again to \(e^{2\pi it}\overline{f(t)}\) to bound the second term. This proves \(C_{\mathrm{int}}\le1\).

## Verification
Each critical step is analytic: spectrum separation, exact boundary weight, periodic-phase averaging, Hardy factorization, compact approximation, and one-parameter monotonicity. Independent arithmetic checkpoints are \(\|H_0\|_1=1/2\), \(\int_0^\infty ue^{-2u}\,du=1/4\), \(M(a,a)=4a/\pi\), and \(\pi^2/16>1/2\). A finite numerical check is neither required nor used to infer the all-profile sharp result. The global equality \(C_{\mathrm{int}}=\pi^2/16\) is **not** claimed.

## Relationship to prior work
Bampouras and Perfekt (arXiv:2608.19806) introduce the natural convex-domain weight and the Helson inequality, and state the classical half-line Carleman benchmark. Bampouras (arXiv:2609.10730) proves general convex-domain Helson estimates with dimension-dependent constants. The earlier Bampouras paper (arXiv:2504.05986), especially its interval discussion in Section 3, gives qualitative interval estimates. In the inspected relevant full-text sections of these papers, no exact mirrored-two-edge concentration constant or \(\pi^2/16\) interference law was found. This is a statement of the extent of inspection, not a proof of absolute novelty. The new part is the **interaction of both interval endpoints** and its sharp asymptotic amplitude law; the half-line Carleman inequality and its sharpness are classical inputs.

## Limitations
The full optimal constant \(C_{\mathrm{int}}\) is only bracketed, not determined. The sharp \(\pi^2/16\) value applies exactly to pairs of mirrored frequency packets with one common profile and fixed nonnegative amplitudes in the stated shrinking-edge limit. Different packets, more components, and interior spectral mass could produce larger ratios. The Hardy factorization is a classical theorem used as a premise; no independent external proof review has been performed. Earlier literature with the same consequence may remain unindexed.

## References
1. K. Bampouras and K.-M. Perfekt, *Boundary-Weighted Fourier Inequalities for Convex Domains*, arXiv:2608.19806, first posted 2026-08-20, Sections 1 and 4.
2. K. Bampouras, *Helson Inequality, Hankel Operators, and Weak Factorization on Paley-Wiener spaces of Convex Domains*, arXiv:2609.10730, first posted 2026-09-09, Sections 1–3.
3. K. Bampouras, *Nehari's Theorem for Schatten class Hankel operators for convex domains*, arXiv:2504.05986, first posted 2025-04-08, Section 3.
4. Classical one-dimensional Carleman inequality and Hardy-space Riesz factorization, also stated or used in references 1 and 3.
