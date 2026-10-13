# A sharp hazard-shape boundary for the alpha-power type-II Lomax distribution

## Finding

The alpha-power type-II Lomax (APIILx) distribution of Kalt and coauthors has an **exact and exhaustive hazard-shape phase diagram**. For positive parameters \(\alpha,\theta,\lambda\), put
\[
B(\alpha)=\frac{\alpha}{1-2^{-\alpha}}-2.
\]
If \(0<\alpha\le 1\), its hazard is strictly decreasing. If \(\alpha>1\), its hazard is strictly decreasing on \((0,\infty)\) **if and only if**
\[
\boxed{\theta B(\alpha)\le 1.}
\]
If \(\alpha>1\) and \(\theta B(\alpha)>1\), the hazard increases strictly up to **one and only one positive-time maximum**, then decreases strictly thereafter. At equality, only the right derivative at the excluded origin vanishes; the hazard still decreases strictly for every positive time.

The phase boundary does not involve the scale \(\lambda\). No member of the family has a globally increasing, bathtub-shaped, or multi-peaked hazard. The unique peak is computable from a scalar monotone equation stated below. This completes the shape distinction described qualitatively by the original distribution paper; neither the general shape distinction nor the distribution itself is claimed as new.

## Assumptions and scope

Fix arbitrary \(\alpha,\theta,\lambda>0\), and let \(X\) have the continuous APIILx distribution supported on \([0,\infty)\) with CDF, for \(x\ge 0\),
\[
F(x)=\frac{[2-v(x)]^\alpha-1}{2^\alpha-1},\qquad
v(x)=\left(\frac{\lambda}{\lambda+x}\right)^\theta.
\]
Its survival function is \(S(x)=1-F(x)\), and its ordinary hazard is \(h(x)=F'(x)/S(x)\). All monotonicity assertions concern \(x>0\); one-sided derivatives at \(x=0\) are used only to state the sharp phase boundary.

Set, for \(0<t\le\log 2\),
\[
D_\alpha(t)=\frac{\alpha}{1-e^{-\alpha t}}-\frac{1}{1-e^{-t}},\qquad
K_\alpha(t)=(e^t-1)D_\alpha(t).
\]
The formula for \(K_\alpha(t)\) applies also when \(\alpha=1\), when it vanishes identically. For \(\alpha>1\), \(K_\alpha\) has the continuous extension \(K_\alpha(0)=0\).

## Proof

**1. An exact stable representation.** Differentiating the stated CDF gives
\[
f(x)=\frac{\alpha\theta}{\lambda+x}
\frac{v(x)[2-v(x)]^{\alpha-1}}{2^\alpha-1},\qquad
S(x)=\frac{2^\alpha-[2-v(x)]^\alpha}{2^\alpha-1}.
\]
Introduce the decreasing coordinate
\[
t(x)=-\log(1-v(x)/2).
\]
For \(x\ge0\), it decreases strictly from \(\log 2\) to \(0\), approaching zero only as \(x\to\infty\). Since \(v=2(1-e^{-t})\), substitution and cancellation yield
\[
\boxed{h(x)=\frac{\theta}{\lambda+x}
\frac{\alpha(e^{t(x)}-1)}{e^{\alpha t(x)}-1}.}
\]
The representation has no subtraction of nearly equal powers of \(2\) in the far tail.

**2. Exact logarithmic derivative.** Differentiating the change of coordinates gives
\[
t'(x)=-\frac{\theta(e^{t(x)}-1)}{\lambda+x}.
\]
Logarithmic differentiation of the preceding hazard formula, using the definition of \(D_\alpha\), now yields the identity
\[
\boxed{\frac{d}{dx}\log h(x)=
\frac{\theta K_\alpha(t(x))-1}{\lambda+x}.}\tag{*}
\]
The denominator is positive, so the sign is controlled exactly by the one-dimensional function in the numerator.

**3. A strict monotonicity lemma.** Fix \(t>0\). The function
\[
a\longmapsto \frac{a}{1-e^{-at}}\quad (a>0)
\]
is strictly increasing: its derivative has the sign of \(1-(1+at)e^{-at}>0\), which follows from \(e^z>1+z\) for \(z>0\). Therefore \(D_\alpha(t)\) has precisely the sign of \(\alpha-1\). In particular, \(K_\alpha(t)\le0\) for \(\alpha\le1\), strictly so for \(\alpha<1\).

For \(\alpha>1\), a second fact is crucial:
\[
D_\alpha'(t)=\frac{1}{4\sinh^2(t/2)}-
\frac{\alpha^2}{4\sinh^2(\alpha t/2)}>0.
\]
The strict inequality follows because \(z\mapsto\sinh z/z\) is strictly increasing on \((0,\infty)\), giving \(\sinh(\alpha t/2)>\alpha\sinh(t/2)\). Thus both positive factors in \(K_\alpha(t)=(e^t-1)D_\alpha(t)\) are strictly increasing for \(\alpha>1\), so \(K_\alpha\) itself is strictly increasing.

At the endpoints,
\[
\lim_{t\downarrow0}K_\alpha(t)=0,\qquad
K_\alpha(\log2)=\frac{\alpha}{1-2^{-\alpha}}-2=B(\alpha).
\]
The first limit follows from \(D_\alpha(t)\to(\alpha-1)/2\). The second follows by direct substitution. For \(\alpha>1\), \(B(\alpha)>0\).

**4. Exhaustive sign classification.** If \(\alpha\le1\), identity (*) has a strictly negative numerator for every \(x>0\). If \(\alpha>1\), then \(t(x)<\log2\) for every \(x>0\), hence
\[
0<K_\alpha(t(x))<B(\alpha),
\]
and the left side decreases strictly as \(x\) increases. If \(\theta B(\alpha)\le1\), the numerator in (*) is strictly negative at every \(x>0\). At equality, its right limit as \(x\downarrow0\) is zero, but it is negative immediately thereafter.

If \(\theta B(\alpha)>1\), the numerator tends to \(\theta B(\alpha)-1>0\) as \(x\downarrow0\), and to \(-1\) as \(x\to\infty\). Strict decrease and continuity give one and only one zero. Therefore \(h\) increases before that zero and decreases after it; the zero is its unique global maximum.

Writing \(t_*\in(0,\log2)\) for the unique solution of
\[
\theta K_\alpha(t_*)=1,
\]
its location is exactly
\[
\boxed{x_*=\lambda\left(\left[2(1-e^{-t_*})\right]^{-1/\theta}-1\right).}
\]
The threshold is sharp because both parameter regions are nonempty. Moreover, as \(x\to\infty\), the hazard representation gives \(h(x)\sim\theta/(\lambda+x)\), excluding a globally increasing hazard independently of the derivative classification.

**5. Exact parameter-boundary behavior.** The map \(\alpha\mapsto B(\alpha)\) is strictly increasing for \(\alpha>1\), by the same \(a/(1-e^{-at})\) lemma at \(t=\log2\). It rises from \(0\) to \(+\infty\) as \(\alpha\) runs from \(1\) to infinity. Thus \(\theta_\mathrm{crit}(\alpha)=1/B(\alpha)\) is continuous and strictly decreasing from infinity to zero. Equivalently, for any fixed \(\theta>0\), there is one and only one critical \(\alpha>1\): the unimodal region lies strictly above this critical value.

## Verification

The proof uses exact differentiation, the elementary exponential inequality, and the strict increase of \(\sinh z/z\), which itself follows by differentiating and observing \(z\cosh z-\sinh z>0\) for \(z>0\). No sampling or finite numerical check is used to infer infinitely quantified monotonicity.

As an exact illustration, when \(\alpha=2\), the boundary is \(\theta=3/2\). At \(\alpha=\theta=2\), write
\[
z_*=(3+\sqrt{17})/4,\qquad
t_*=\log z_*,\qquad
\frac{x_*}{\lambda}=
\left(2\left[1-z_*^{-1}\right]\right)^{-1/2}-1.
\]
For \(\lambda=1\), the peak is at \(x_*=0.06788960253492849930\ldots\); its hazard is \(1.34699989940591358088\ldots\), compared with \(h(0)=4/3\).

The numerical identity checks in `hazard_phase_checker.py` use Python's standard-library `decimal` module, test 360 interior points over multiple parameters, reproduce the exact \(\alpha=2\) boundary and peak, and examine decreasing-boundary examples. Execute `python3 hazard_phase_checker.py` in the directory containing that file. Numerical checks are cross-checks, not an infinite proof.

## Relationship to prior work

Kalt, Ben Ghorbal, Elbatal, Afify and Mahran (2026), DOI `10.3934/math.2026334`, define exactly this three-parameter CDF, PDF, survival function and hazard in their equations (2.4)–(2.7). The introduction and Figure 1 identify decreasing and unimodal hazards qualitatively, but their full-text treatment does not supply the if-and-only-if phase boundary, a proof that there is at most one interior maximum for every admissible parameter, or the exact peak equation above.

Mohsin and Kalt (2025), DOI `10.18280/mmep.120330`, introduce the more general alpha-power type-II generator and work out exponential and Weibull baselines. Its generator formula alone does not classify the Lomax-baseline hazards. Qura and coauthors (2023), DOI `10.1155/2023/6661792`, analyze a distinct four-parameter alpha-power power-Lomax model built using the exponential-in-CDF alpha-power generator, not the power-of-\(1+G\) generator here; its reported hazard shapes do not imply this threshold. The Lomax model of 1954 is the \(\alpha=1\) special case.

The novelty claimed here is **only** this complete analytic parameter classification and unique-peak determination for the 2026 APIILx model. Prior work on heavy-tail exponents and moment existence addresses different implications, not the derivative-sign threshold.

## Limitations

The theorem concerns the exact mathematical APIILx family with all three parameters strictly positive and the full infinite time domain. A hazard can appear increasing over a finite observation window while eventually decreasing; the result does not re-evaluate any empirical fit, statistical estimator, or application. The numerical illustration is not a general proof. The literature comparison does not guarantee priority against inaccessible or unindexed work; independently checking priority remains worthwhile. One secondary indexing service displays an inconsistent publication date, so the primary publisher's verified date is used in the references.

## References

1. H. G. Kalt, A. Ben Ghorbal, I. Elbatal, A. Z. Afify and H. A. Mahran, “A new alpha power type-II Lomax distribution with applications to radiation and materials sciences,” *AIMS Mathematics* **11** (2026), 8134–8167, DOI `10.3934/math.2026334`, published 27 March 2026. Complete publisher PDF: https://www.aimspress.com/aimspress-data/math/2026/3/PDF/math-11-03-334.pdf .
2. L. A. J. Mohsin and H. G. Kalt, “Alpha Power Type II-G Family: Adding a Power Parameter of Distributions,” *Mathematical Modelling of Engineering Problems* **12** (2025), 1031–1042, DOI `10.18280/mmep.120330`. Complete open-access article: https://www.iieta.org/node/19845 .
3. M. E. Qura, M. Alqawba, M. M. Al Sobhi and A. Z. Afify, “A Novel Extended Power-Lomax Distribution for Modeling Real-Life Data: Properties and Inference,” *Journal of Mathematics* (2023), article 6661792, DOI `10.1155/2023/6661792`. Open-access article: https://onlinelibrary.wiley.com/doi/10.1155/2023/6661792 .
4. K. S. Lomax, “Business Failures: Another Example of the Analysis of Failure Data,” *Journal of the American Statistical Association* **49** (1954), 847–852, DOI `10.1080/01621459.1954.10501239`.
