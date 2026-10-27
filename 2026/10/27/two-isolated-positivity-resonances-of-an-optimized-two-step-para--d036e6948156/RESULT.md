# Two isolated positivity resonances of an optimized two-step parareal coarse propagator

## Finding
For the **printed rational coefficients** of the optimized two-step coarse propagator O2CP in Li--Lin--Zhang--Zhou (2026), the exact-start scalar decay sequence has a complete and unusual positivity classification. Write
\[
 A(s)=\frac{0.02178-0.00047s}{1+0.56380s},\qquad
 B(s)=\frac{0.97822-0.46300s}{1+0.56380s},
\]
\[
 y_0=1,\quad y_1=e^{-s},\quad y_{n+2}=A(s)y_n+B(s)y_{n+1}\qquad(n\geq0).
\]
All quantities in the displayed rational coefficients are treated as **exact decimal rationals**, not unrounded fitted parameters. Set
\[
 s_0=\frac{48911}{23150}=2.1127861771058\ldots,\qquad
 s_1=\frac{2178}{47}=46.3404255319149\ldots.
\]
The recurrence is strictly Schur-stable for every \(s>0\), but **every** iterate is strictly positive exactly when either \(0\leq s\leq s_0\) or \(s\) is one of **two isolated positive exact-match resonances**:
\[
 s_a=3.70146585514664567\ldots,\qquad
 s_b=46.3404255319148932905944859972298\ldots.
\]
The latter lies just \(3.26426790598515\cdot10^{-16}\) below \(s_1\). They are characterized exactly, without numerical root definitions, as the two roots in \((s_0,s_1)\) of
\[
 (1+0.56380s)e^{-2s}-(0.97822-0.46300s)e^{-s}-(0.02178-0.00047s)=0.
\]
At every other \(s>s_0\), an iterate is strictly negative. For \(s\geq s_1\), the **second** computed coarse value is already negative, and
\[
 \lim_{s\to\infty}y_2=-\frac{47}{56380}=-0.000833628946434906\ldots,
\]
although the exact solution at that time tends to zero from above.

The onset of sign loss above \(s_0\) is delayed: letting \(N_-(s)\) denote the first negative index, one has
\[
 \lim_{s\downarrow s_0}(s-s_0)N_-(s)=K=1.02737350743767356\ldots,
\]
with the exact formula for \(K\) below. At either isolated resonance, \(N_-(s)\) instead diverges logarithmically as the parameter approaches the resonance through nonresonant values. These are properties of the **uncorrected exact-start scalar coarse recurrence**, not of the fully corrected parareal solution or spatial positivity of arbitrary discretizations.

## Assumptions and scope
The scalar test equation is \(u'=-\lambda u\) with \(\lambda>0\); \(s=\lambda\tau\) is the dimensionless two-step coarse parameter. The starting data \(y_0=1\), \(y_1=e^{-s}\) are exact half-step data. This favorable exact starter is chosen deliberately to isolate the effect of the coarse recurrence. The source initializes its complete parareal implementation separately; no identity with that startup is asserted. For \(s=0\), every iterate equals one. Throughout, the printed five-decimal O2CP coefficients are mathematical data in their own right; no conclusion is claimed for hidden unrounded coefficients.

## Proof
**Stability and sign boundary.** Let \(a=0.02178\), \(b=0.00047\), \(c=0.97822\), \(d=0.46300\), and \(e=0.56380\). The characteristic polynomial is \(z^2-B(s)z-A(s)\). The three real quadratic Schur inequalities are
\[
1-B-A=\frac{(e+b+d)s}{1+es}>0,\quad
1+B-A=\frac{2-2a+(e+b-d)s}{1+es}>0,\quad
1+A=\frac{1+a+(e-b)s}{1+es}>0
\]
for \(s>0\). For \(0\leq s\leq s_0=c/d<s_1=a/b\), both coefficients \(A\) and \(B\) are nonnegative, so induction from \(y_0,y_1>0\) proves positivity (at \(s=0\) the sequence is constant). For \(s\geq s_1\), both coefficients are nonpositive and \(B<0\), giving \(y_2=A+B e^{-s}<0\).

For \(s_0<s<s_1\), \(A>0>B\). The characteristic roots are the positive number \(p\) and negative number \(-q\), where
\[
 p=\frac{B+\sqrt{B^2+4A}}2,\qquad
 q=\frac{\sqrt{B^2+4A}-B}2>p>0.
\]
Writing \(u=e^{-s}\), the **exact** solution of the recurrence is
\[
 y_n=\frac{u+q}{p+q}p^n+\frac{p-u}{p+q}(-q)^n.
\]
When \(u=p\), the negative-root coefficient vanishes and every iterate equals \(p^n>0\). Otherwise, the dominant negative root forces an eventually negative **even** index if \(u>p\), and an eventually negative **odd** index if \(u<p\). This proves the exhaustive positivity criterion. In the nonresonant interval, the first negative index is exactly the smallest even integer strictly greater than
\[
 \frac{\log((u+q)/(u-p))}{\log(q/p)}
\]
when \(u>p\), or the smallest odd integer strictly greater than
\[
 \frac{\log((u+q)/(p-u))}{\log(q/p)}
\]
when \(u<p\). The inequalities are strict, so exact zero values are not mistaken for negative ones. The positivity classification does not assert a uniform lower bound away from zero.

**Exactly two resonances.** The matching equation \(u=p\) on \((s_0,s_1)\) is equivalent to the stated exponential polynomial \(F(s)=0\), because the positive root is the unique positive solution of \(z^2-Bz-A=0\). For this interval, rewrite
\[
 F(s)=(1+es)e^{-2s}+(ds-c)e^{-s}-a+bs.
\]
Direct differentiation yields
\[
 F'=(e-2-2es)e^{-2s}+(d+c-ds)e^{-s}+b,
\]
\[
 F''=(4+4es-4e)e^{-2s}+(ds-c-2d)e^{-s}.
\]
The function \(H=e^sF''=4(1+e(s-1))e^{-s}+ds-c-2d\) obeys
\[
 H''(s)=4(1+e(s-3))e^{-s}>0\quad(s\geq s_0),
\]
since \(s_0>2\) and \(0<e<1\). Moreover \(H(s_0)<0<H(s_0+2)\); convexity therefore gives exactly one zero of \(H\) to the right of \(s_0\), so \(F'\) first decreases and then increases. The strict signs \(F'(s_0)>0\), \(F'(7/2)<0\), \(F'(s_1)>0\) imply one local maximum and one local minimum of \(F\) on \((s_0,s_1)\). Finally, \(F(s_0)>0\), \(F(7/2)>0\), \(F(4)<0\), \(F(46)<0\), and \(F(s_1)>0\), proving one root in \((7/2,4)\) and exactly one root in \((46,s_1)\), with no others. Each root is simple, being on a strictly monotone branch. All decisive exponential signs follow from elementary Taylor upper/lower bounds; exact rational interval checks are implemented in `check.py`.

**Delayed first sign loss.** At \(s=s_0\), let \(P=\sqrt{A(s_0)}\) and \(u_0=e^{-s_0}>P\) (the last inequality is certified by the same explicit exponential bounds). As \(s\downarrow s_0\),
\[
 \log(q/p)=\frac{d}{(1+es_0)P}(s-s_0)+O((s-s_0)^2).
\]
The even-index sign criterion and bounded rounding to the nearest even index imply
\[
 K=\frac{P(1+es_0)}d\log\frac{u_0+P}{u_0-P}.
\]
Near either simple resonance \(s_r\), the coefficient \((p-u)/(p+q)\) vanishes linearly, while \(\log(q/p)\) is strictly positive, so the same exact first-negative-index formulas give
\[
 N_-(s)=\frac{\log(1/|s-s_r|)}{\log(q(s_r)/p(s_r))}+O(1)
\]
on either nonresonant side. Finally \(y_2=A+B e^{-s}\to-b/e\) as claimed.

## Verification
Run `python check.py` from the extracted package. It checks the exact rational stability identities, 2,557 direct-vs-closed recurrence/first-sign comparisons, high-precision critical values, and eleven **rigorous rational Taylor-interval sign inequalities** used to count the resonances and establish the onset constant. The exact interval checker uses positive Taylor series for \(e^t\), a geometric remainder bound, and inversion to enclose \(e^{-t}\). Numerical iteration by itself is not the proof of the infinite positivity classification; the proof is the characteristic-root decomposition plus the convexity and Sturm-free derivative count above. `check_output.txt` records a successful execution of the included program.

## Relationship to prior work
Li, Lin, Zhang and Zhou, arXiv:2605.11979v2, Section 3.1, equations (3.1)--(3.3), and Section 3.5, equation (3.20), introduce and optimize the two-step coarse recurrence; Proposition 6 studies A-stability. Their objective contains the exact exponential-matching residual, but the inspected sections do not classify the full nonnegative trajectory, its two isolated matching resonances, or first-sign-loss delays. Earlier linear-multistep positivity research by Hundsdorfer, Ruuth and Spiteri treats general monotonicity and admissible starting procedures, not these printed O2CP rational functions or the all-time exact-start scalar resonance set. A published note on BDF2 delayed sign loss treats complex-root oscillation with a square-root delay exponent; general real-root-dominance arguments are also classical and not claimed as new. Neither establishes this O2CP exact-match root count and positivity set.

## Limitations
The result is intentionally scalar and uses the **uncorrected** two-step coarse recurrence with exact exponential starting data. It does not show nonpositivity of the final converged parareal solution, nor a coordinatewise maximum-principle failure for all spatial PDE discretizations. The last resonance is narrower than binary64 resolution relative to its location; its numeric digits require high-precision evaluation and are not a robust floating-point tuning recommendation. Changes to the rational coefficients, including replacing the printed decimals with unpublished higher-precision optimization coefficients, may move or remove the exceptional resonances. General linear-recurrence/monotonicity theory substantially overlaps the proof technique; a hidden equivalent formula remains a priority risk. No independent audit has been performed.

## References
1. G. Li, Q. Lin, K. Zhang, Z. Zhou, *Optimized Two-Step Coarse Propagators in Parareal Algorithms*, first posted May 12, 2026, arXiv:2605.11979v1; equations and analysis inspected in v2 (May 17, 2026). https://arxiv.org/abs/2605.11979
2. W. Hundsdorfer, S. J. Ruuth, R. J. Spiteri, *Monotonicity-Preserving Linear Multistep Methods*, CWI Report MAS-R0210 (2002), https://ir.cwi.nl/pub/4231/04231D.pdf ; SIAM Journal on Numerical Analysis 41 (2003), 605--623, DOI:10.1137/S0036142902406326.
3. *Exact delayed sign loss just beyond BDF2's positivity boundary*, publicly accessible mathematical research note, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-delayed-sign-loss-just-beyond-bdf2-s-positivity-boundary--cf66315c5a14.
