# Two Dirichlet precision regimes for Boolean completion of random formal contexts

## Finding

In the symmetric Dirichlet row-density model for formal contexts, the first time the concept lattice becomes Boolean has sharply different limiting distributions depending on the prior precision. With the standard simplex-uniform choice, the completion time divided by \(m^2\log m\) converges to an inverse-exponential (Fréchet) law. With a fixed total Dirichlet precision, its logarithm divided by \(m\) converges to an exponential law. Moreover, the unconditioned mean completion time is infinite precisely at and below a sharp precision threshold.

Formally, let \(m\ge1\) be the number of attributes, let \(\beta_m>0\), and draw once a vector \(\boldsymbol\pi=(\pi_0,\ldots,\pi_m)\sim\operatorname{Dirichlet}(\beta_m/(m+1),\ldots,\beta_m/(m+1))\). Conditional on this vector, independently draw an unlimited sequence of objects: choose a row cardinality \(K\) with probabilities \(\boldsymbol\pi\), and then select uniformly one of the \(K\)-subsets of the attribute set. The vector is **held fixed for the entire sequence**. Let \(T_m\) be the minimum positive number of objects at which the concept lattice has all \(2^m\) possible intents. It is almost surely finite.

Write \(H_m=\sum_{j=1}^m1/j\). For every \(m\ge1\),

\[
\mathbb E[T_m]=\begin{cases}
\infty,&\beta_m\le m+1,\\
\displaystyle mH_m\frac{\beta_m-1}{\beta_m/(m+1)-1},&\beta_m>m+1.
\end{cases}
\]

In the *simplex-uniform regime* \(\beta_m=m+1\), for every \(x>0\),
\[
\lim_{m\to\infty}\Pr\!\left(\frac{T_m}{m^2\log m}\le x\right)=e^{-1/x}.
\]
Thus the typical completion scale is polynomial although the mean is infinite for each \(m\).

In the *fixed-precision regime* \(\beta_m=\beta>0\),
\[
\frac{\log T_m}{m}\ \xrightarrow{\,d\,}\ \operatorname{Exp}(\text{rate }\beta).
\]
Equivalently, for every \(c>0\),
\[
\lim_{m\to\infty}\Pr(T_m\le e^{cm})=1-e^{-\beta c}.
\]
The two laws describe a polynomial-to-exponential change in completion time under different natural precision scalings of the same random-context generator.

## Assumptions and scope

The model specifies **a single shared, random Dirichlet row-size distribution per context**, followed by conditionally independent, uniform-within-size object rows. It is the sequential extension of the symmetric Dirichlet construction in Felde and Hanika (2018), also treated by Felde, Hanika, and Stumme (2020). The number of objects is not pre-truncated, and repeated rows are allowed. This distinction matters: independently resampling a new Dirichlet vector for each object would produce a different law. All probability statements include the initial Dirichlet draw as well as subsequent rows. The weak limits concern integer \(m\to\infty\); the finite-mean criterion is exact at every \(m\).

## Proof

**Step 1: the Boolean-completion event.** A formal context has all \(2^m\) intents if and only if, for each attribute \(i\), it contains a row whose exact intent is the coatom \(M\setminus\{i\}\). Indeed, if all subsets are closed, then the closure of the coatom must exclude \(i\), and a row containing the coatom but missing \(i\) must be exactly that coatom. Conversely, if every coatom row occurs, for any subset \(S\subseteq M\) and every \(i\notin S\), the coatom row missing \(i\) contains \(S\) and excludes \(i\), so the closure of \(S\) equals \(S\). This standard contranominal-scale criterion is not claimed as new.

**Step 2: a beta-mixed coupon collector.** Put \(R_m=\pi_{m-1}\). Marginalization of the Dirichlet distribution gives
\[
R_m\sim\operatorname{Beta}\!\left(a_m,b_m\right),\qquad
 a_m=\frac{\beta_m}{m+1},\quad b_m=\frac{m\beta_m}{m+1}.
\]
Conditional on \(R_m=r>0\), each of the \(m\) required coatom rows has probability \(r/m\) per object; all other rows together have probability \(1-r\). The classical coupon-collector mean therefore gives \(\mathbb E[T_m\mid R_m=r]=mH_m/r\). The exact finite-time conditional distribution is
\[
\Pr(T_m\le n\mid R_m=r)=\sum_{j=0}^{m}(-1)^j\binom mj(1-jr/m)^n,
\qquad n\in\mathbb Z_{\ge0}.
\]
This also supplies a reproducible finite-time expression by integrating against the displayed beta density.

**Step 3: exact mean threshold.** For \(R\sim\operatorname{Beta}(a,b)\) with positive parameters, \(\mathbb E[1/R]=\infty\) when \(a\le1\), while for \(a>1\) it equals \((a+b-1)/(a-1)\). Substitute \(a=a_m\), \(a+b=\beta_m\), and use the nonnegative tower identity to obtain the stated exact criterion and formula. In particular, \(a_m=1\) in the standard \(\beta_m=m+1\) model, so its mean is infinite at every \(m\).

**Step 4: the simplex-uniform limit.** If \(\beta_m=m+1\), then \(R_m\sim\operatorname{Beta}(1,m)\), so \(Y_m=mR_m\) converges in distribution to a unit-rate exponential variable because, for fixed \(y\ge0\), \(\Pr(Y_m>y)=(1-y/m)^m\) for \(0\le y\le m\). Fix \(x>0\) and set \(n_m=\lfloor xm^2\log m\rfloor\). Conditional on \(Y_m=y\), the number \(Z_m\) of unseen coatom types after \(n_m\) rows has mean
\[
\mathbb E[Z_m\mid Y_m=y]
=m(1-y/m^2)^{n_m}=m^{1-xy+o(1)}
\]
for \(y\) in each fixed positive compact interval. If \(xy>1\), Markov's inequality shows \(\Pr(Z_m>0\mid y)\to0\). If \(xy<1\), the unseen-type indicators have nonpositive covariances, since \((1-2y/m^2)^{n_m}\le(1-y/m^2)^{2n_m}\). Hence \(\operatorname{Var}(Z_m\mid y)\le\mathbb E[Z_m\mid y]\), and Chebyshev's inequality shows \(\Pr(Z_m=0\mid y)\to0\). Squeezing away from \(y=1/x\) and using \(Y_m\Rightarrow\operatorname{Exp}(1)\) yields
\[
\Pr(T_m\le n_m)\to\Pr(Y>1/x)=e^{-1/x}.
\]

**Step 5: the fixed-precision logarithmic limit.** Let \(\beta_m=\beta>0\) and set \(W_m=-m^{-1}\log R_m\). Its beta density gives, for every fixed \(c>0\),
\[
\Pr(W_m>c)
=\frac{1}{B(a_m,b_m)}\int_0^{e^{-cm}}r^{a_m-1}(1-r)^{b_m-1}\,dr
\sim\frac{e^{-cma_m}}{a_mB(a_m,b_m)}\longrightarrow e^{-\beta c},
\]
since \(a_m\to0\), \(b_m\to\beta\), and \(a_mB(a_m,b_m)\to1\). Thus \(W_m\Rightarrow\operatorname{Exp}(\beta)\). The sampling delay is negligible on the logarithmic scale: for any \(\varepsilon>0\), conditional on \(R_m=r\), before \(e^{-\varepsilon m}/r\) observations there is even one coatom draw with probability at most \(e^{-\varepsilon m}\); after \(e^{\varepsilon m}/r\) observations, the union bound on missing coatom types is at most \(m\exp[-(e^{\varepsilon m}-1)/m]\). These uniform bounds prove
\[
\frac{\log T_m+\log R_m}{m}\ \xrightarrow{\mathbb P}\ 0.
\]
Slutsky's theorem completes the proof.

## Verification

The accompanying standalone standard-library checker independently enumerates every ordered row sequence for \(m\in\{1,2,3\}\) and lengths \(0\le n\le4\), with three positive rational precision choices for each \(m\). It computes all formal closure operators directly; separately detects the set of missing coatom row types; and integrates each row sequence against the full symmetric Dirichlet-multinomial law using exact rational arithmetic. It compares those sums to an independently calculated beta-mixture inclusion–exclusion expression. All 45 parameter cases and 15,159 explicitly weighted contexts pass. These finite checks corroborate normalization and the Booleanity reduction; the infinite-dimensional limiting laws are proved analytically above, not inferred from enumeration.

Run `python verify.py` from the directory containing the standalone code; it has no third-party dependencies.

## Relationship to prior work

Felde and Hanika (arXiv:1809.11160, 2018) introduced the symmetric Dirichlet context model and explicitly observed that collecting all coatom rows reduces, *conditional on coatom-category draws*, to the coupon collector; the 2020 extension by Felde, Hanika, and Stumme made the same observation and experimentally varied Dirichlet precision. Their stated results do not give the unconditioned completion-time distribution, the integrability threshold in the shared random environment, or the two precision-dependent weak limits proved here. The present result credits those model definitions and deterministic coupon observations, rather than treating them as new. Sakurai (arXiv:2101.11023, 2021) analyzes the average number of concepts under independent Bernoulli incidences rather than the frozen Dirichlet row-size mixture considered here. Classical coupon-collector concentration and beta marginals are also used as prior tools. The novel assessed statement is their joint consequence for this natural shared-environment lattice-completion problem, especially the inverse-exponential versus exponential-log scale distinction.

## Limitations

This result concerns only the **time to a full Boolean concept lattice**, not the distribution of partial concept counts or other lattice properties. The object count in the originally published generator may itself be randomly truncated; the sequential stopping time here is explicitly defined without such a cap. Nothing is asserted about independent re-draws of Dirichlet vectors between objects or nonuniform base measures. The limiting claims apply to the stated precision scalings and are not an exhaustive classification of all intermediate scalings. The novelty review could not inspect the full text of Yang et al. (2024), *Counting Formal Concepts of A Random Formal Context*; an equivalent differently phrased prior treatment of the random-environment stopping time remains a residual possibility. Publication priority has not been independently certified.

## References

1. M. Felde and T. Hanika, *Formal Context Generation using Dirichlet Distributions*, arXiv:1809.11160, first posted 2018-09-28. https://arxiv.org/abs/1809.11160.
2. M. Felde, T. Hanika and G. Stumme, *Null Models for Formal Contexts*, *Information* 11 (2020), 135, DOI:10.3390/info11030135.
3. T. Sakurai, *On formal concepts of random formal contexts*, arXiv:2101.11023 (2021); subsequently *Information Sciences* 578 (2021), 615–620.
4. L. Yang, E. C. C. Tsang, C. Zhang and J. Wu, *Counting Formal Concepts of A Random Formal Context*, ICMLC 2024, 439–445, DOI:10.1109/ICMLC63072.2024.10935090 (full-text overlap assessment unresolved).
