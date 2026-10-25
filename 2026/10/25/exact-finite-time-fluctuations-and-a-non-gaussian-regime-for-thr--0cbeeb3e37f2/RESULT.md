# Exact finite-time fluctuations and a non-Gaussian regime for three-person sampled-neighbor opinion learning

## Finding

In the synchronous Follow-the-Leader (FTL) opinion process on the three-vertex path, the degree-stationary weighted social opinion has an **exact finite-time Rademacher-product distribution**. When the two leaves have unequal intrinsic opinions, its fluctuations exhibit three distinct regimes: a non-Gaussian almost-sure random-series limit for confidence \(0<\alpha<1/2\), a logarithmically normalized Gaussian limit at \(\alpha=1/2\), and a square-root-time Gaussian limit for \(1/2<\alpha<1\). The formulas below identify the exact limiting variances and the strictly negative fourth cumulant in the first regime. The general stochastic-approximation rate transition is not claimed as new; the finding is the explicit network-observable law.

Write \(s_1,s_2,s_3\in[0,1]\) for intrinsic opinions, with \(s_1\ne s_3\), and let \(0<\alpha<1\). Define
\[
\pi=(1/4,1/2,1/4),\qquad Y_t=\pi x(t),\qquad Y_*=\pi s,\qquad c=(1-\alpha)(s_1-s_3)/4.
\]
Let \((\xi_j)_{j\ge0}\) be independent equiprobable signs. For integers \(t\ge1\) and \(j\ge1\) set
\[
 g_t=\frac{\Gamma(t+1-\alpha)}{\Gamma(t+1)},\qquad
 b_j=\frac{\Gamma(j)}{\Gamma(j+1-\alpha)}.
\]
Then the exact **equality in distribution**, and indeed an equality on the natural coupling of all rounds, is
\[
 \boxed{Y_t-Y_*=c g_t\left(b_1\xi_0+\alpha\sum_{j=2}^{t}b_j\xi_{j-1}\right).}
\]
The empty sum at \(t=1\) is zero. In particular \(\mathbb E Y_t=Y_*\),
\[
 \operatorname{Var}(Y_t)=c^2g_t^2\left(b_1^2+\alpha^2\sum_{j=2}^{t}b_j^2\right),
\]
and its characteristic function is
\[
 \mathbb E e^{iu(Y_t-Y_*)}=\cos(ucg_tb_1)\prod_{j=2}^{t}\cos(ucg_t\alpha b_j).
\]
The complete limits are:

* If \(0<\alpha<1/2\), then \(t^\alpha(Y_t-Y_*)\to Z_\alpha\) almost surely and in \(L^2\), where
\[
 Z_\alpha=c\left(b_1\xi_0+\alpha\sum_{j=2}^{\infty}b_j\xi_{j-1}\right).
\]
Its variance is \(c^2(b_1^2+\alpha^2\sum_{j\ge2}b_j^2)\), and its fourth cumulant is
\[
 \boxed{\kappa_4(Z_\alpha)=-2c^4\left(b_1^4+\alpha^4\sum_{j=2}^{\infty}b_j^4\right)<0.}
\]
Thus this limit is nondegenerate and not Gaussian.

* If \(\alpha=1/2\), then
\[
 \sqrt{\frac{t}{\log t}}(Y_t-Y_*)\ \Longrightarrow\ N(0,c^2/4),\qquad
 \lim_{t\to\infty}\frac{t}{\log t}\operatorname{Var}(Y_t)=c^2/4.
\]
Here logarithms are natural and the expressions concern \(t\ge2\).

* If \(1/2<\alpha<1\), then
\[
 \sqrt t\,(Y_t-Y_*)\ \Longrightarrow\ N\left(0,\frac{\alpha^2c^2}{2\alpha-1}\right),\qquad
 \lim_{t\to\infty}t\operatorname{Var}(Y_t)=\frac{\alpha^2c^2}{2\alpha-1}.
\]

## Assumptions and scope

The graph is the undirected path \(1-2-3\). Each round all three agents update **simultaneously**. Agents 1 and 3 have the sole neighbor 2; agent 2 independently chooses either neighbor with probability \(1/2\) in each round. Its neighbor choices are independent over rounds. The homogeneous confidence parameter \(\alpha\in(0,1)\) is the weight placed on an agent's intrinsic opinion, and all initial expressed opinions equal their intrinsic opinions: \(x_i(0)=s_i\).

In precise FTL notation, if \(J_i(k)\) is agent \(i\)'s sampled neighbor at round \(k\), then, for all integers \(t\ge1\),
\[
 x_i(t)=\alpha s_i+\frac{1-\alpha}{t}\sum_{k=0}^{t-1}x_{J_i(k)}(k).
\]
This is exactly the sample-average FTL update of Fotakis–Kandiros–Kontonis–Skoulakis, with uniform path-edge weights and intrinsic weights chosen to realize the common \(\alpha\). The stochastic matrix of neighbor sampling is
\[
 P=\begin{pmatrix}0&1&0\\1/2&0&1/2\\0&1&0\end{pmatrix},\qquad \pi P=\pi.
\]
The deterministic Friedkin–Johnsen equilibrium \(x^*\) solves \(x^*=\alpha s+(1-\alpha)Px^*\); hence \(\pi x^*=\pi s=Y_*\). The result concerns this particular degree-stationary projection, not the complete vector's distribution. The strict inequality \(s_1\ne s_3\) ensures nonzero sampling noise.

## Proof

**Step 1 (a deterministic leaf difference).** Every leaf always samples agent 2. For all \(t\ge1\), the FTL formula therefore gives
\[
 x_1(t)-x_3(t)=\alpha(s_1-s_3).
\]
At time zero the corresponding difference is \(s_1-s_3\). This is the special structural property that makes the random central sampling additive with deterministic amplitude.

**Step 2 (exact scalar recursion).** The FTL formula can equivalently be written
\[
 x(t)=\left(1-\frac1t\right)x(t-1)+\frac1t\left[\alpha s+(1-\alpha)X(t-1)\right],
\]
where \(X_i(t-1)=x_{J_i(t-1)}(t-1)\). Write the central agent's choice as the independent fair sign \(\xi_{t-1}=1\) for leaf 1 and \(-1\) for leaf 3. Multiplication by the stationary row vector \(\pi\) yields, for \(E_t=Y_t-Y_*\),
\[
 E_0=0,\quad E_1=c\xi_0,\quad
 E_t=\left(1-\frac\alpha t\right)E_{t-1}+\frac{\alpha c}{t}\xi_{t-1}\quad(t\ge2).
\]
The first impulse differs because the initial leaf difference is not yet attenuated by \(\alpha\). Independence holds because fresh central sampling is independent of all earlier choices.

**Step 3 (solving the recursion).** The product identity
\[
 \prod_{k=j+1}^{t}\left(1-\frac\alpha k\right)
 =\frac{\Gamma(t+1-\alpha)\Gamma(j+1)}{\Gamma(t+1)\Gamma(j+1-\alpha)}
 =\frac{j g_t\Gamma(j)}{\Gamma(j+1-\alpha)}
\]
shows that an impulse applied at time \(j\) with factor \(1/j\) has final coefficient \(g_t b_j\). Summing the first impulse \(c\) and subsequent impulses \(\alpha c\) gives the boxed identity in the finding. By independence, the characteristic function is a cosine product and the variance is the sum of squared coefficients, exactly as stated.

**Step 4 (the subcritical random series).** Gamma-ratio asymptotics give \(t^\alpha g_t\to1\) and \(b_j\sim j^{\alpha-1}\). If \(0<\alpha<1/2\), then \(\sum_{j\ge2} b_j^2<\infty\). The independent centered series therefore converges almost surely and in \(L^2\) by the martingale convergence theorem. Multiplying its partial sums by \(t^\alpha g_t\to1\) proves the asserted limit. The fourth cumulant of a fair sign with coefficient \(u\) is \(-2u^4\). As \(\sum b_j^4<\infty\), fourth moments of the partial sums converge to those of the limit (e.g. by the standard fourth-moment formula and convergence of both square and fourth-power sums). Hence the displayed strictly negative cumulant is exact, and rules out a Gaussian law.

**Step 5 (critical and supercritical Gaussian limits).** For \(\alpha\ge1/2\), the squared coefficient sum of the Rademacher series diverges, but the largest unscaled individual coefficient remains bounded because \(b_j\sim j^{\alpha-1}\), \(\alpha<1\). Thus the maximal normalized summand tends to zero, giving the Lindeberg condition. The independent triangular-array central limit theorem applies. More precisely, at \(\alpha=1/2\), \(\sum_{j=2}^{t}b_j^2\sim\log t\), whereas if \(\alpha>1/2\), \(\sum_{j=2}^{t}b_j^2\sim t^{2\alpha-1}/(2\alpha-1)\). Combining these expressions with \(g_t\sim t^{-\alpha}\) gives the exact two limiting variances and normalizing factors. The single initial impulse makes no asymptotic contribution in either regime.

**Boundary of random sampling.** A connected loopless graph with one or two vertices gives every vertex at most one neighbor, so the neighbor-selection step produces no randomness. The three-vertex path is therefore the smallest connected simple graph that permits the nontrivial sampled-neighbor fluctuations examined here.

## Verification

`verify.py` uses only the Python standard library and rational arithmetic. It independently enumerates **every** sequence of the central agent's neighbor choices through eight rounds for nine combinations of rational confidences and intrinsic-opinion vectors. It evolves the original three-agent FTL recurrence, compares the resulting weighted mean with a separately constructed exact impulse expansion, checks the deterministic leaf-difference identity and bounds on expressed opinions, and compares the enumerated mean and variance with the exact coefficient formulas. Execution completed with **13,916 exact-rational assertions passed**.

As a hand-check, take \(\alpha=1/2\), \((s_1,s_2,s_3)=(0,1/2,1)\), and \(t=2\). Then \(c=-1/8\) and
\[
 Y_2-Y_*=-\frac3{32}\xi_0-\frac1{32}\xi_1,
 \qquad \operatorname{Var}(Y_2)=\frac5{512}.
\]
The finite enumeration is a check, not a proof of the infinite-series, central-limit, or almost-sure statements, which follow analytically from Steps 4–5.

## Relationship to prior work

Fotakis, Kandiros, Kontonis, and Skoulakis introduced and analyzed sampled-neighbor no-regret FTL opinion learning in their 2018 conference publication (expanded in their 2023 open-access journal paper). Their main FTL result bounds the expected maximum error of the complete opinion vector by a logarithmically corrected inverse power of time. Their displayed FTL rule coincides with the update used here, but the reported theorem does not identify an exact finite-time law for \(\pi x(t)\), its exact variance, or a model-specific non-Gaussian limit with a fourth-cumulant certificate.

Renlund (2011) gives a general stochastic-approximation central limit theorem and a slower non-normal-scaling regime. It anticipates the **general half-exponent division**, so that division by itself is not claimed as novel. The specific exact Rademacher coefficients, distributional identity, asymptotic constants, and explicit non-normal law for this anchored opinion observable require identifying the three-path's leaf-difference invariant and are not stated in that general theorem. Earlier limited-interaction opinion models use distinct update rules. The literature and mathematical-database comparisons were not an exhaustive proof of publication priority.

## Limitations

This is a theorem for a homogeneous-confidence, three-vertex path with independent uniform central sampling and a degree-weighted **scalar** opinion observable. It does not assert that individual agent opinions or the full opinion vector obey the same limiting law or that a corresponding formula holds on arbitrary graphs, with heterogeneous confidences, correlated sampling, or other update rules. For \(s_1=s_3\), the sampling noise vanishes and the displayed nondegenerate limits do not apply. Existing general stochastic-approximation results already predict some scaling regimes. The publication-priority comparison is not exhaustive.

## References

1. D. Fotakis, V. Kandiros, V. Kontonis, S. Skoulakis, *Opinion Dynamics with Limited Information*, Web and Internet Economics (WINE), first online 21 November 2018, pp. 282–296, DOI: 10.1007/978-3-030-04612-5_19; https://link.springer.com/chapter/10.1007/978-3-030-04612-5_19 .
2. D. Fotakis, V. Kandiros, V. Kontonis, S. Skoulakis, *Opinion Dynamics with Limited Information*, Algorithmica 85 (2023), pp. 3855–3888, DOI: 10.1007/s00453-023-01157-5; https://link.springer.com/article/10.1007/s00453-023-01157-5 .
3. H. Renlund, *Limit theorems for stochastic approximation algorithms*, arXiv:1102.4741, first posted 23 February 2011, https://arxiv.org/abs/1102.4741 .
4. D. Fotakis, D. Palyvos-Giannas, S. Skoulakis, *Opinion Dynamics with Local Interactions*, IJCAI (2016), pp. 279–285, https://mlanthology.org/ijcai/2016/fotakis2016ijcai-opinion/ .
