# Logarithmic crossover and square-root unfolding of fractional-tent Fourier zeros

## Finding
For \(0<\alpha<\infty\), define the compactly supported even power tent \(f_\alpha(x)=(1-|x|)_+^\alpha\) and its real Fourier transform
\[
F_\alpha(t)=\int_{-1}^{1}f_\alpha(x)e^{-itx}\,dx=2\int_0^1(1-x)^\alpha\cos(tx)\,dx.
\]
At the critical triangular exponent \(\alpha=1\), every positive zero \(T_n=2\pi n\) has multiplicity exactly two. For each fixed positive integer \(n\), write \(\alpha=1-\varepsilon\). For all sufficiently small \(\varepsilon>0\), there are exactly two positive real zeros in the cell \((T_n-\pi,T_n+\pi)\), and they satisfy
\[
t_{n,\pm}(\varepsilon)=T_n\pm\sqrt{2C_n\varepsilon}+O_n(\varepsilon),\qquad
C_n=\gamma+\log T_n-\operatorname{Ci}(T_n)
=\int_0^{T_n}\frac{1-\cos u}{u}\,du>0.
\]
The root separation therefore opens at the square-root scale, with a coefficient \(C_n\sim\log T_n+\gamma\).

There is a distinct, nonuniform high-frequency transition. For **every** sequence of positive integers \(n_j\to\infty\) and positive real numbers \(\varepsilon_j\to0\) satisfying
\[
\varepsilon_j\log(2\pi n_j)\longrightarrow\lambda\in(0,\infty),
\]
the two and only two real zeros of \(F_{1-\varepsilon_j}\) in \((2\pi n_j-\pi,2\pi n_j+\pi)\), denoted in increasing order, obey
\[
\boxed{\quad t_{j,\pm}-2\pi n_j\longrightarrow
\pm\arccos(e^{-\lambda}).\quad}
\]
Thus at frequencies of exponential order \(\exp(\lambda/\varepsilon)\), an arbitrarily small exponent perturbation retains a nonzero limiting separation, in contrast with the fixed-frequency square-root collapse.

## Assumptions and scope
The Fourier convention is \(\widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx\). The exponent in the theorem approaches \(1\) **from below**, and the crossover parameter \(\lambda\) is finite and strictly positive. The cell endpoints are open. The result concerns real Fourier zeros, not the full complex zero set. No statement of uniform asymptotics at \(\lambda=0\), \(\lambda=\infty\), or for arbitrary fixed \(\alpha\ne1\) is inferred from the crossover limit.

## Proof
**Critical exponent and fixed-index unfolding.** Direct integration gives
\[
F_1(t)=\frac{2(1-\cos t)}{t^2},\quad t\ne0,
\qquad F_1(0)=1.
\]
Consequently its positive roots are exactly \(T_n=2\pi n\), each double, with \(F_1''(T_n)=2/T_n^2\). Differentiation under the integral sign at \(\alpha=1\) is permitted by integrable domination. Integration by parts, using \(\cos(T_n(1-u))=\cos(T_nu)\), yields
\[
\left.\partial_\alpha F_\alpha(T_n)\right|_{\alpha=1}
=2\int_0^1 u\log u\cos(T_nu)\,du
=\frac{2}{T_n^2}\left[\gamma+\log T_n-\operatorname{Ci}(T_n)\right]
=\frac{2C_n}{T_n^2}.
\]
The last identity also follows directly from the defining integral of \(\operatorname{Ci}\). Hence the real-analytic Taylor expansion at \((\alpha,t)=(1,T_n)\), with \(s=t-T_n\), is
\[
F_{1-\varepsilon}(T_n+s)
=\frac{s^2-2C_n\varepsilon}{T_n^2}
+O_n(|s|^3+\varepsilon|s|+\varepsilon^2).
\]
Writing \(s=\sqrt\varepsilon\,y\), dividing by \(\varepsilon\), and applying the implicit-function theorem at the two simple roots \(y=\pm\sqrt{2C_n}\) gives \(s=\pm\sqrt{2C_n\varepsilon}+O_n(\varepsilon)\). On the complement of a small fixed neighborhood of \(T_n\) within its cell, \(F_1\) is strictly positive, so uniform convergence on that compact set precludes additional real zeros for sufficiently small \(\varepsilon\). The strict positivity of \(C_n\) is immediate from its displayed integral, and \(\operatorname{Ci}(T_n)=O(T_n^{-2})\) follows from its oscillatory tail expansion.

**Uniform endpoint expansion.** For \(t>0\), complex integration of a power gives the exact identity
\[
\int_0^1(1-x)^\alpha e^{itx}\,dx
=e^{it}(it)^{-\alpha-1}\gamma(\alpha+1,it),
\]
where \(\gamma(a,z)\) is the lower incomplete gamma function, with the principal branch. Substituting \(\gamma=\Gamma-\Gamma(\cdot,\cdot)\), the large-argument asymptotic expansion of the upper incomplete gamma function (DLMF §8.11(i)) gives, uniformly for \(\alpha\) in a sufficiently small fixed closed neighborhood of \(1\),
\[
\frac{F_\alpha(t)}2
=\frac{\alpha}{t^2}
+\frac{\Gamma(\alpha+1)}{t^{\alpha+1}}
\cos\!\left(t-\frac{\pi(\alpha+1)}2\right)
+O(t^{-4})\qquad(t\to+\infty).
\]
Indeed the integer inverse powers from the upper-gamma endpoint are \(-1/(it)-\alpha/(it)^2-\alpha(\alpha-1)/(it)^3-\cdots\); the even real terms begin with \(\alpha/t^2\). The same expansion can be differentiated once with respect to real \(t\) on bounded-width frequency cells, with a uniform differentiated remainder. Uniformity in the stated compact exponent range follows from the integral remainder or the locally uniform upper-gamma expansion, not from a pointwise-in-exponent big-O statement.

**Double scaling.** Put \(T_j=2\pi n_j\), \(\alpha_j=1-\varepsilon_j\), and \(t=T_j+s\) for bounded real \(s\). Multiplying the uniform expansion by \(T_j^2\) gives, uniformly in every compact interval of \(s\), and also for one derivative in \(s\),
\[
\frac{T_j^2}{2}F_{\alpha_j}(T_j+s)
\longrightarrow 1-e^\lambda\cos s.
\]
Here \(\Gamma(2-\varepsilon_j)\to1\), \((T_j+s)^{\varepsilon_j}\to e^\lambda\), and the endpoint phase equals \(s-\pi+\pi\varepsilon_j/2\). For \(\lambda>0\) the limit function has exactly two simple roots in \([-\pi,\pi]\), at \(s=\pm\arccos(e^{-\lambda})\), and is nonzero at both endpoints. Uniform convergence excludes other roots outside small disjoint neighborhoods of these roots; uniform derivative convergence and the intermediate-value theorem yield exactly one simple root inside each neighborhood. This proves the claimed two-root classification and the limiting locations for every admissible sequence.

## Verification
The accompanying `check.py` evaluates the *exact* incomplete-gamma expression at 70-decimal-digit precision, brackets the paired zeros, checks the fixed-index square-root coefficients at three indices, and tests the crossover at four exponent/frequency pairs, including indices exceeding ten billion. The accompanying `check_output.txt` records the actual execution. Finite numerical checks neither establish the uniform endpoint expansion nor certify the theorem for all sequences; the argument above supplies the infinite proof.

## Relationship to prior work
Pólya-type sine-transform zero-location results, discussed and refined by Sedletskii (2009), already give qualitative real/simple zero placement for positive increasing weights. In the present setting, integration by parts gives \(F_\alpha(t)=2\alpha t^{-1}\int_0^1(1-x)^{\alpha-1}\sin(tx)\,dx\); for \(0<\alpha<1\) that weight increases, so these prior zero results apply. Qualitative positivity for \(\alpha>1\) follows from the convexity criterion treated by Tuck (2006). The new claim is **not** the positivity threshold, the existence of zeros, or classical fixed-exponent Fourier asymptotics. It is the precisely quantified coexistence of a fixed-index square-root unfolding and a logarithmic double-scaling law for zero separation, with the explicit \(\arccos(e^{-\lambda})\) transition. DLMF §8.11 provides the standard special-function asymptotic input, not this application.

## Limitations
The leading crossover is restricted to finite positive \(\lambda\); the endpoints of its parameter range require separate uniform analyses. No globally uniform error rate for every simultaneous \(n,\varepsilon\) is asserted. Numerical calculations use finite precision and do not certify zeros away from the counted cells. Although no inspected source states the combined claim, priority cannot be guaranteed from incomplete historical coverage, especially older general literature on zeros of finite Fourier transforms. No independent review has been performed.

## References
- E. O. Tuck, “On positivity of Fourier transforms,” *Bulletin of the Australian Mathematical Society* **74** (2006), 133–138. DOI: 10.1017/S0004972700047511. Published online by Cambridge University Press on 17 April 2009.
- A. M. Sedletskii, “Localization of small zeros of sine and cosine Fourier transforms of a finite positive nondecreasing function,” *Vestnik Moskovskogo Universiteta*, Ser. 1, 2009, no. 4, 35–41. MathNet identifier vmumm887.
- NIST Digital Library of Mathematical Functions, §8.11(i), “Large \(z\), Fixed \(a\),” upper incomplete gamma expansion, equations 8.11.1–8.11.2, https://dlmf.nist.gov/8.11.
- NIST Digital Library of Mathematical Functions, Chapter 6, cosine-integral definitions, https://dlmf.nist.gov/6.
