# Exactly two reciprocal-normal-product modes and their exponential separation from typical size

## Finding

Let \(G_1,G_2,\ldots\) be independent standard normal variables. For integers \(M,N\ge 0\) with \(M+N\ge1\), let \(X_i\) and \(Y_j\) be mutually independent centered normal variables with strictly positive standard deviations; interpret an empty product as \(1\), and set
\[
Z_{M,N}=\frac{\prod_{i=1}^M X_i}{\prod_{j=1}^N Y_j}.
\]
The normal-product ratio density has a complete modal dichotomy:

**(i)** For \(M\ge1\) and \(N\ge0\), its density is strictly decreasing on \((0,\infty)\) and strictly increasing on \(( -\infty,0)\); hence its only mode is the origin (the density at the origin may be infinite).

**(ii)** For \(M=0\) and every \(N\ge1\), its density is strictly increasing on \((0,z_N)\), strictly decreasing on \((z_N,\infty)\), and has exactly two global modes \(\pm z_N\), with a strict local minimum of value zero at the origin. Write \(s_N=\prod_{j=1}^N\sigma_{Y_j}\). The positive mode is uniquely specified by
\[
z_N=s_N^{-1}e^{-u_N},
\]
where \(u_N\) is the unique mode of the sum of \(N\) independent logarithms of standard Rayleigh variables with density \(r e^{-r^2/2}\) for \(r>0\).

**(iii)** Uniformly over all choices of the positive scale factors (because they enter only through \(s_N\)), as \(N\to\infty\),
\[
\boxed{\log(s_N z_N)=-\frac N2(\log2-\gamma_{\mathrm E})-\frac{3\zeta(3)}{\pi^2}+O(N^{-1}).}
\]
Here \(\gamma_{\mathrm E}\) is Euler's constant and \(\zeta\) is the Riemann zeta function. For unit scales, however,
\[
\frac1N\log\left|\frac1{G_1\cdots G_N}\right|\xrightarrow{\mathrm{a.s.}}\frac{\gamma_{\mathrm E}+\log2}{2}>0.
\]
Thus both density modes approach the origin exponentially even as a typical absolute observation diverges exponentially; the logarithmic separation between a sample and its positive mode is \(N\log2+o(N)\) almost surely under the natural coupling.

## Assumptions and scope

All factors are independent real zero-mean Gaussian variables with strictly positive finite variances; the density is with respect to ordinary Lebesgue measure, not the logarithmic coordinate. A mode means a global or local maximizer of this Lebesgue density. The asymptotic statement varies \(N\) with arbitrary positive denominator standard deviations and no numerator factors; the almost-sure comparison uses the first \(N\) members of one infinite iid standard-normal sequence. It makes no claim about dependent or non-Gaussian factors.

## Proof

**1. Numerator present: strict monotonicity.** When \(M\ge1\), condition on all variables except \(X_1\). Almost surely their products are nonzero, and the conditional law of \(Z_{M,N}\) is centered Gaussian with a positive random standard deviation \(A\). For each \(0<x<y\),
\[
\frac{e^{-y^2/(2A^2)}}{\sqrt{2\pi}A}<\frac{e^{-x^2/(2A^2)}}{\sqrt{2\pi}A}.
\]
The expectations are finite for every \(x>0\), since \(a^{-1}e^{-x^2/(2a^2)}\) is bounded over \(a>0\). Taking expectations proves strict decrease; symmetry supplies the negative half-line. The density limit at zero is finite when \(M=1\) and infinite when \(M\ge2\), but this fact is not needed for monotonicity.

**2. Reciprocal denominator: an exact Rayleigh tilting identity.** Write \(Y_j=\sigma_{Y_j}G_j\) and let \(T_j=\log|G_j|\). Its density is
\[
g(t)=\sqrt{2/\pi}\,e^t\exp(-e^{2t}/2),\qquad t\in\mathbb R.
\]
With \(g_N=g^{*N}\) and \(u=-\log(s_N z)\), ordinary change of variables shows that the even reciprocal-product density for \(z>0\) is
\[
f_{Z_{0,N}}(z)=\frac{g_N(u)}{2z}=\frac{s_N}{2}\,e^u g_N(u).
\]
Now \(\operatorname E e^{T_j}=\sqrt{2/\pi}\). Multiplying \(g\) by \(e^t/\sqrt{2/\pi}\) gives exactly
\[
h(t)=e^{2t}\exp(-e^{2t}/2),
\]
the density of \(\log R\) for standard Rayleigh \(R\) with density \(r e^{-r^2/2}\). Exponential tilting commutes with independent convolution, so, with \(h_N=h^{*N}\),
\[
\boxed{f_{Z_{0,N}}(z)=\frac{s_N}{2}\left(\sqrt{\frac2\pi}\right)^N h_N(-\log(s_N z)),\quad z>0.}
\]
The log-density \(\log h(t)=2t-e^{2t}/2\) is strictly concave, and convolution preserves log-concavity. Moreover the characteristic function \(2^{it/2}\Gamma(1+it/2)\) decays exponentially, so each \(h_N\) is positive and real analytic. A nonconstant integrable positive real-analytic log-concave density cannot have a flat interval at its maximum (a linear interval would analytically continue to an everywhere linear logarithm). Hence \(h_N\) has a unique maximizer \(u_N\), and by real-analyticity, log-concavity and absence of constant intervals it increases strictly before and decreases strictly after \(u_N\). Its tails vanish at both ends. The decreasing coordinate change \(z=e^{-u}/s_N\) transfers this to the asserted two-mode shape; the value at \(z=0\) is zero by the source's origin asymptotic, or directly from the displayed identity and \(h_N(u)\to0\) as \(u\to\infty\).

For \(N=1\), \(u_1=\tfrac12\log2\) and \(z_1=(\sqrt2\,s_1)^{-1}\). For \(N=2\), the Rayleigh product density is \(rK_0(r)\); its logarithm has density \(h_2(u)=e^{2u}K_0(e^u)\). Thus \(u_2=\log t_2\), where \(t_2>0\) is the unique root of \(tK_1(t)=2K_0(t)\), giving \(t_2=1.552651255645\ldots\) and \(s_2z_2=1/t_2=0.644060\ldots\). Uniqueness follows from the preceding shape argument, not a numerical plot.

**3. Sharp large-factor modal displacement.** The cumulant-generating function of \(T=\log R\) is
\[
K(a)=\log\operatorname E e^{aT}=\tfrac a2\log2+\log\Gamma(1+a/2),\qquad a>-2.
\]
Its first three cumulants are
\[
\mu=\tfrac12(\log2-\gamma_{\mathrm E}),\qquad
v=\tfrac{\pi^2}{24},\qquad
\kappa_3=-\tfrac14\zeta(3).
\]
Let \(H_N\) be the density \(h_N\). Fourier inversion with \(\varphi(t)=2^{it/2}\Gamma(1+it/2)\) gives the density and its derivative. Since
\[
|\varphi(t)|^2=\frac{\pi|t|/2}{\sinh(\pi|t|/2)}<1\quad(t\ne0),
\]
with exponential decay at infinity, both integrals admit termwise Laplace expansion after \(t=w/\sqrt N\), uniformly for \(a\) in any fixed compact set. Expand
\[
\log\varphi(t)=i\mu t-\tfrac12vt^2+\tfrac16\kappa_3(it)^3+O(t^4).
\]
The Gaussian parity cancellations in the density and differentiated inversion yield, uniformly on bounded \(a\),
\[
H_N(N\mu+a)=\frac{1}{\sqrt{2\pi Nv}}\{1+O(N^{-1})\},
\]
\[
\frac{H_N'(N\mu+a)}{H_N(N\mu+a)}
=-\frac1{Nv}\left(a+\frac{\kappa_3}{2v}\right)+O(N^{-2}).
\]
To justify the stated error orders, split the Fourier integral into \(|t|\le N^{-2/5}\), where Taylor's formula through degree six has an integrable Gaussian-dominated remainder, and its complement, controlled by \(|\varphi(t)|<1\) away from zero and the quadratic bound near zero. Odd terms of the scaled integrands integrate to zero. All estimates are uniform in bounded \(a\); the bound for the derivative uses one additional factor \(t\). Choose fixed \(a\) on opposite sides of \(-\kappa_3/(2v)\). The displayed derivative has opposite signs for large \(N\), and strict log-concavity locates its unique root between them. Reapplying the derivative estimate at the root gives
\[
u_N=N\mu-\frac{\kappa_3}{2v}+O(N^{-1})
=N\mu+\frac{3\zeta(3)}{\pi^2}+O(N^{-1}).
\]
Substituting into \(s_Nz_N=e^{-u_N}\) proves the modal asymptotic.

**4. Typical size versus the mode.** For a standard Gaussian factor, differentiating its absolute Mellin moment at zero gives
\[
\operatorname E\log|G|=\tfrac12(\log2+\psi(1/2))=-\tfrac12(\gamma_{\mathrm E}+\log2).
\]
The variables \(\log|G_j|\) have finite first absolute moments, so the strong law gives the claimed almost-sure limit. Subtracting the logarithmic mode asymptotic leaves \(N\log2+o(N)\).

## Verification

Run `python checker.py` with the versions specified in `requirements.txt`. The checker uses the exact Fourier integral of the logarithmic Rayleigh sum, independently compares the one-factor closed form and two-factor Bessel equation, tests derivative signs and values for several factor counts, and checks the predicted large-factor displacement. It also performs a seeded Monte Carlo check of the strong-law rate. These finite computations are corroboration only: the all-\(N\) modal uniqueness and asymptotic orders follow from the analytic proof above.

## Relationship to prior work

Gaunt and Sutcliffe (2026, arXiv:2601.12997, Remark 2.10) give Meijer-G densities and state that a ratio with a numerator Gaussian factor is unimodal, while the all-denominator reciprocal case is not unimodal. They do not classify the exact number of reciprocal-product modes, derive their log-Rayleigh characterization or growing-\(N\) locations, or compare modes with almost-sure typical size. The strict monotonicity assertion in part (i) strengthens their stated univariate mode conclusion but is not presented as an independent discovery. Salo, El-Sallabi and Vainikainen (2006) supply exact Rayleigh-product densities, which permit representation of the tilted law but do not state the reciprocal-Gaussian modal-location expansion. Log-concavity under convolution and Fourier/Edgeworth expansion are standard tools; no novelty is claimed for those general tools.

## Limitations

The source 2026 paper's theorem already implies the zero-versus-nonzero modal *qualitative* separation; the contribution is an exact two-peak count and quantitative large-factor localization, not rediscovery of the distribution or its Meijer-G representation. Classical Rayleigh-product formulas and generic smooth-sum modal asymptotics substantially reduce conceptual novelty; a previously unindexed specialized mode theorem may exist. The asymptotic is in the number of denominator factors, not in sample size, and its constant assumes centered Gaussian factors. The almost-sure comparison uses unit scales, while general positive scales enter the mode formula exactly through their product. No independent audit or externally certified priority claim is made.

## References

1. R. E. Gaunt and H. L. Sutcliffe, *The distribution of the ratio of products of independent zero mean normal random variables*, arXiv:2601.12997v1 (first posted 19 January 2026); *Metrika*, DOI:10.1007/s00184-026-01045-2 (2026), Theorems 2.1, 2.6, 2.7 and Remark 2.10. https://arxiv.org/pdf/2601.12997
2. J. Salo, H. M. El-Sallabi and P. Vainikainen, *The Distribution of the Product of Independent Rayleigh Random Variables*, IEEE Transactions on Antennas and Propagation **54** (2006), 639–643, DOI:10.1109/TAP.2005.863087.
3. A. Prékopa, *Logarithmic concave measures with applications to stochastic programming*, Acta Scientiarum Mathematicarum **32** (1971), 301–316 (convolution log-concavity; standard result).
