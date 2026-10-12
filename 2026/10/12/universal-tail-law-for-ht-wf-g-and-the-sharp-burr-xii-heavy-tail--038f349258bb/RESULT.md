# Universal tail law for HT-WF-G and the sharp Burr XII heavy-tail phase
## Finding
Let \(G\) be an unbounded-support baseline distribution with survival
\[
s(x)=1-G(x)\longrightarrow0,
\]
and let \(\alpha,\lambda>0\). The heavy-tailed Weibull flexible-G construction of Chipepa et al. has survival
\[
S(x)
=
\left[
\frac{e^{-A(x)}}{\lambda+(1-\lambda)e^{-A(x)}}
\right]^\lambda,
\qquad
A(x)=\left[s(x)^{-G(x)}-1\right]^\alpha.
\]
Then the generator has the universal logarithmic tail law
\[
-\log S(x)\sim \lambda\,s(x)^{-\alpha}
\qquad(x\to\infty).
\]

For the Burr XII baseline used in the paper,
\[
s(x)=(1+x^\beta)^{-k},
\qquad \beta,k>0,
\]
put
\[
\delta=\alpha\beta k.
\]
Then
\[
-\log S(x)\sim\lambda x^\delta.
\]
Consequently, using the exponential-comparison definition of heavy-tailedness adopted in the Type-I heavy-tailed-G literature,
\[
\lim_{x\to\infty}\frac{S(x)}{e^{-p x}}=\infty
\quad\text{for every }p>0,
\]
the HT-WF-BXII distribution is heavy-tailed exactly when
\[
\alpha\beta k<1.
\]
At \(\alpha\beta k=1\) it has exponential-order decay, and for \(\alpha\beta k>1\) it is lighter than every exponential.

If \(Q\) denotes its quantile function, then
\[
Q(1-q)
\sim
\left[
\frac{1}{\lambda}\log\!\left(\frac1q\right)
\right]^{1/\delta}
\qquad(q\downarrow0).
\]

For every \(\delta>0\), all positive power moments are finite. For positive exponential moments,
\[
\mathbb E e^{tX}=
\begin{cases}
\infty, & 0<\delta<1,\ t>0,\\
<\infty, & \delta=1,\ 0<t<\lambda,\\
\infty, & \delta=1,\ t>\lambda,\\
<\infty, & \delta>1,\ t>0.
\end{cases}
\]
No boundary claim at \(t=\lambda\) is needed.

For the paper's Weibull baseline
\[
s(x)=e^{-c x^\omega},
\qquad c,\omega>0,
\]
the same universal law gives
\[
-\log S(x)
\sim
\lambda e^{\alpha c x^\omega}.
\]
Thus the HT-WF-W special case is lighter than every exponential and has finite positive exponential moments of every order.

The paper's Burr XII risk simulation uses
\[
\alpha=0.2,\qquad \beta=0.3,\qquad k=0.2,
\]
so \(\alpha\beta k=0.012<1\). That displayed example is therefore inside the genuine heavy-tail phase; the correction concerns the unrestricted family-level nomenclature and parameter space, not that numerical example.

## Assumptions and scope
The baseline support is unbounded and \(s(x)\to0\). The parameters satisfy \(\alpha,\lambda>0\). The Burr XII specialization uses \(\beta,k>0\), and the Weibull specialization uses \(c,\omega>0\).

“Heavy-tailed” is used in the same strict exponential-comparison sense stated in the Type-I heavy-tailed-G precursor: the survival must dominate \(e^{-p x}\) asymptotically for every \(p>0\). This is stronger and more precise than visual tail thickness, large kurtosis, or large finite-level risk measures.

The theorem does not claim that a light asymptotic tail prevents a model from fitting a finite dataset well. Nor does it invalidate the paper's Burr XII risk table, whose displayed parameters lie in the heavy-tail phase.

## Proof
Because \(G(x)=1-s(x)\),
\[
s(x)^{-G(x)}
=
s(x)^{-(1-s(x))}
=
s(x)^{-1}\exp\!\left(s(x)\log s(x)\right).
\]
Since
\[
s\log s\longrightarrow0
\qquad(s\downarrow0),
\]
we have
\[
s(x)\left[s(x)^{-G(x)}-1\right]
=
\exp\!\left(s(x)\log s(x)\right)-s(x)
\longrightarrow1.
\]
Therefore
\[
s(x)^{-G(x)}-1\sim s(x)^{-1},
\]
and hence
\[
A(x)\sim s(x)^{-\alpha}.
\]

Now
\[
-\log S(x)
=
\lambda A(x)
+
\lambda\log\!\left(
\lambda+(1-\lambda)e^{-A(x)}
\right).
\]
As \(A(x)\to\infty\), the second term converges to the finite constant \(\lambda\log\lambda\). Thus
\[
\frac{-\log S(x)}{\lambda s(x)^{-\alpha}}\longrightarrow1,
\]
proving the universal law.

For Burr XII,
\[
s(x)^{-\alpha}
=
(1+x^\beta)^{\alpha k}
\sim x^{\alpha\beta k}=x^\delta,
\]
so
\[
-\log S(x)\sim\lambda x^\delta.
\]
For any \(p>0\),
\[
\log\frac{S(x)}{e^{-p x}}
=
p x-\lambda x^\delta(1+o(1)).
\]
If \(0<\delta<1\), this tends to \(+\infty\) for every \(p>0\). If \(\delta>1\), it tends to \(-\infty\) for every \(p>0\). If \(\delta=1\), choosing any \(p<\lambda\) makes it tend to \(-\infty\), so the heavy-tail criterion fails. This proves the sharp phase boundary.

The quantile result follows by asymptotic inversion of the monotone relation
\[
-\log S(x)\sim\lambda x^\delta.
\]
Indeed, if \(q=S(Q(1-q))\), then
\[
\log(1/q)\sim\lambda Q(1-q)^\delta.
\]

For moments, the logarithmic equivalent gives eventual two-sided bounds
\[
e^{-C_2 x^\delta}
\le S(x)\le
e^{-C_1 x^\delta}
\]
for positive constants \(C_1,C_2\). The identity
\[
\mathbb E X^r
=
r\int_0^\infty x^{r-1}S(x)\,dx
\]
therefore gives finiteness for every \(r>0\).

Similarly,
\[
\mathbb E e^{tX}
=
1+t\int_0^\infty e^{t x}S(x)\,dx
\]
whenever the integral is finite. Comparing \(t x\) with \(\lambda x^\delta\) proves the stated exponential-moment regimes away from the critical point \(t=\lambda\).

For a Weibull baseline, \(s(x)=e^{-c x^\omega}\), so
\[
s(x)^{-\alpha}=e^{\alpha c x^\omega},
\]
which proves the displayed double-exponential-order logarithmic tail. Since
\[
e^{\alpha c x^\omega}/x\longrightarrow\infty,
\]
the resulting survival is lighter than \(e^{-p x}\) for every \(p>0\).

## Verification
The accompanying script evaluates the exact generated survival without replacing the generator by its asymptotic form. For several Burr XII parameter choices on all three sides of the boundary \(\alpha\beta k=1\), it verifies numerically that
\[
\frac{-\log S(x)}{\lambda x^{\alpha\beta k}}\to1.
\]
It also checks the more fundamental baseline-invariant ratio
\[
\frac{-\log S(x)}{\lambda s(x)^{-\alpha}}\to1
\]
and verifies the Weibull-baseline double-exponential logarithmic scale.

The numerical calculations are consistency checks only. The infinite-domain statements follow from the exact algebra above.

## Relationship to prior work
Chipepa et al. define the HT-WF-G construction by composing the Weibull flexible-G generator with the Type-I heavy-tailed-G transform. They call the resulting family heavy-tailed, present Weibull and Burr XII special cases, and use finite-level skewness, kurtosis, and actuarial risk measures to discuss tail flexibility. Their Burr XII section does not state the asymptotic phase boundary \(\alpha\beta k=1\), and their Weibull section does not state that the terminal tail is lighter than every exponential.

Zhao et al. define the Type-I heavy-tailed-G transform and explicitly adopt the exponential-comparison definition used here. Their transform alone preserves the leading logarithmic tail scale of its input up to a multiplicative parameter; it does not imply the new result without first analyzing the preceding Weibull flexible-G layer. In particular, the universal relation
\[
-\log S(x)\sim\lambda s(x)^{-\alpha}
\]
arises from that composition.

A 2026 Topp-Leone-heavy-tailed-G paper explicitly studies tail asymptotics for a different generator and reports a tunable tail index. That is evidence that asymptotic tail classification is a substantive property rather than a synonym for finite-level risk magnitude, but its transformation is different and does not imply the HT-WF-G formula above.

Focused searches using the target DOI, exact family names, Burr XII parameters, tail-index language, stretched-exponential aliases, and moment-generating-function aliases did not locate the universal HT-WF-G tail law or the \(\alpha\beta k=1\) boundary.

## Limitations
The universal theorem is logarithmic: it determines \(-\log S(x)\) to first asymptotic order, not a multiplicative asymptotic equivalent for \(S(x)\) itself.

At the critical Burr XII phase \(\alpha\beta k=1\), the result determines the exponential rate \(\lambda\), but no claim is made here about finiteness of the moment generating function exactly at \(t=\lambda\).

The result classifies asymptotic heaviness and does not rank finite-sample fit or finite-quantile risk measures. Slow convergence can be substantial when \(\alpha\beta k\) is very small, as in the parameter values used in the paper's risk table.

## References
1. F. Chipepa, M. M. Abdelwahab, W. Nkomo, and M. M. Hasaballah, “Oncological data applications and risk measures of the heavy-tailed Weibull flexible-G family,” AIMS Mathematics 11 (2026), 8382–8406. DOI: 10.3934/math.2026344.
2. W. Zhao, S. K. Khosa, Z. Ahmad, M. Aslam, and A. Z. Afify, “Type-I heavy tailed family with applications in medicine, engineering and insurance,” PLOS ONE 15 (2020), e0237462. DOI: 10.1371/journal.pone.0237462.
3. W. Nkomo, J. Manyemba, E. Chitombo, T. Nyakuamba, and M. Hazvinandawa, “Beyond Routine Construction: Actuarial Risk Measures, Multi Method Estimation, and Censored Survival Modeling with the Topp-Leone-Heavy Tailed G Family,” Statistics, Optimization & Information Computing (2026), online first. DOI: 10.19139/soic-2310-5070-4108.
