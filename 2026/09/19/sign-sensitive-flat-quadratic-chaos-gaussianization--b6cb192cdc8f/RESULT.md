# Sign-sensitive sharp Gaussianization of flat quadratic-chaos maxima

## Statement

Let `p -> infinity`, let `m=m_p -> infinity`, and let `s_1,...,s_m in {+1,-1}` be deterministic signs. Put

\[
\rho_m=\frac1m\sum_{r=1}^m s_r,
\qquad
Q_{m,j}=\frac1{\sqrt{2m}}\sum_{r=1}^m s_r\,(Z_{jr}^2-1),
\quad 1\le j\le p,
\]

where all `Z_{jr}` are independent standard Gaussian variables, and define

\[
M_{p,m}=\max_{j\le p}Q_{m,j}.
\]

Every coordinate has variance one. Every sign pattern has the same fourth-order effective rank

\[
r_4=\frac{(\sum_r a_r^2)^2}{\sum_r a_r^4}=m,
\qquad a_r=\frac{s_r}{\sqrt{2m}},
\]

and the same fourth cumulant `12/m`, but its third cumulant is

\[
\kappa_3(Q_{m,j})=\frac{2\sqrt2\,\rho_m}{\sqrt m}.
\]

Let `L=log p`, let `b_p=Phi^{-1}(1-1/p)`, and write

\[
x_p(y)=b_p+\frac{y}{b_p}.
\]

The following uniform extreme-tail expansion holds for each fixed bounded set of `y` whenever

\[
\frac{m}{L^{5/3}}\longrightarrow\infty:
\]

\[
\boxed{
\log\frac{\mathbb P\{Q_{m,1}>x_p(y)\}}{\bar\Phi(x_p(y))}
=
\frac{\sqrt2\,\rho_m}{3\sqrt m}\,x_p(y)^3
+
\left(\frac12-\rho_m^2\right)\frac{x_p(y)^4}{m}
+o(1).
}
\tag{1}
\]

Consequently, if

\[
\alpha_p:=\rho_m\frac{L^{3/2}}{\sqrt m}\to\alpha\in\mathbb R,
\qquad
\beta_p:=\frac{L^2}{m}\to\beta\in[0,\infty),
\]

then

\[
\boxed{
 b_p(M_{p,m}-b_p)\Rightarrow G+a,
 \qquad
 a=\frac43\alpha+2\beta,
}
\tag{2}
\]

where `G` is standard Gumbel with distribution function

\[
\Lambda(y)=\exp(-e^{-y}).
\]

If `M_p^G=max_{j<=p}G_j` for independent standard Gaussians, then the Kolmogorov distance has the explicit critical-window limit

\[
\boxed{
 d_K(M_{p,m},M_p^G)
 \longrightarrow
 D(|a|),
 \qquad
 D(c)=(1-e^{-c})\exp\!\left[-\frac{c}{e^c-1}\right],
}
\tag{3}
\]

with `D(0)=0` by continuity.

## Two sharp flat-spectrum benchmarks

### Positive flat spectrum

If all signs are positive, then

\[
Q_m^+=\frac{\chi_m^2-m}{\sqrt{2m}},
\qquad r_4=m.
\]

If

\[
\frac{L^{3/2}}{\sqrt m}\to\tau\in[0,\infty),
\]

then

\[
\boxed{
 b_p(M_{p,m}^+-b_p)\Rightarrow G+\frac43\tau,
}
\tag{4}
\]

and

\[
\boxed{
 d_K(M_{p,m}^+,M_p^G)\to D(4\tau/3).
}
\tag{5}
\]

Thus `m >> (log p)^3` is the sharp Gaussianization order for the independent positive-flat benchmark. The exponent `3` itself is consistent with classical Cramer theory and with the sharp centered-chi-square moderate-deviation example already identified by Fang--Koike; the new content here is the exact extreme-value critical window and its use as an effective-rank benchmark.

### Balanced signed flat spectrum

For even `m`, take `m/2` plus signs and `m/2` minus signs. Then

\[
Q_m^{\pm}
=
\frac{\chi_{m/2}^2-\widetilde\chi_{m/2}^2}{\sqrt{2m}},
\qquad r_4=m,
\]

with independent chi-squares and exactly zero third cumulant. If

\[
\frac{L^2}{m}\to\tau\in[0,\infty),
\]

then

\[
\boxed{
 b_p(M_{p,m}^{\pm}-b_p)\Rightarrow G+2\tau,
}
\tag{6}
\]

and

\[
\boxed{
 d_K(M_{p,m}^{\pm},M_p^G)\to D(2\tau).
}
\tag{7}
\]

Hence the balanced family Gaussianizes already at the sharp order `m >> (log p)^2`.

## Effective rank is not a sharp one-parameter phase coordinate

The two flat families above have the same variance, the same fourth cumulant `12/m`, and exactly the same effective rank `r_4=m`. Nevertheless their simultaneous Gaussianization thresholds differ by one full power of `log p`.

A direct same-rank separation is obtained by taking an even integer sequence

\[
m_p\asymp (\log p)^{5/2}.
\]

For the balanced signed family, (1) gives a vanishing tail correction because

\[
\frac{L^2}{m_p}\to0,
\]

so

\[
d_K(M_{p,m_p}^{\pm},M_p^G)\to0.
\]

For the positive family, (1) at `y=0` gives

\[
\log\frac{\mathbb P\{Q_{m_p}^+>b_p\}}{\bar\Phi(b_p)}
\sim \frac43 L^{1/4}\to\infty.
\]

Since `p*barPhi(b_p)=1`, it follows that

\[
\mathbb P\{M_{p,m_p}^+\le b_p\}\to0,
\]

whereas

\[
\mathbb P\{M_p^G\le b_p\}=(1-1/p)^p\to e^{-1}.
\]

Therefore

\[
\boxed{
\liminf_{p\to\infty}d_K(M_{p,m_p}^+,M_p^G)\ge e^{-1},
\qquad
 d_K(M_{p,m_p}^{\pm},M_p^G)\to0.
}
\tag{8}
\]

This shows that fourth-order effective rank alone cannot be a sharp universal phase coordinate for signed quadratic-chaos maxima. The sign imbalance, equivalently the third cumulant at flat spectrum, is an additional leading-order parameter.

## Proof

### 1. Exact cumulant generating function

Let `m_+` and `m_-` be the numbers of positive and negative signs, so that

\[
\rho_m=(m_+-m_-)/m.
\]

The cumulant generating function `K_m(t)=log E exp(t Q_{m,1})` is exactly

\[
\begin{aligned}
K_m(t)
={}&-\rho_m\sqrt{\frac m2}\,t
-\frac{m_+}{2}\log\left(1-\sqrt{\frac2m}\,t\right)\\
&-\frac{m_-}{2}\log\left(1+\sqrt{\frac2m}\,t\right).
\end{aligned}
\tag{9}
\]

The linear term cancels in the Taylor expansion. Uniformly for `|t|=o(sqrt(m))`,

\[
K_m(t)
=
\frac{t^2}{2}
+\frac{\sqrt2\rho_m}{3\sqrt m}t^3
+\frac{t^4}{2m}
+O\left(\frac{|t|^5}{m^{3/2}}+\frac{|t|^6}{m^2}\right).
\tag{10}
\]

This also gives

\[
\kappa_3=\frac{2\sqrt2\rho_m}{\sqrt m},
\qquad
\kappa_4=\frac{12}{m}.
\]

### 2. Saddlepoint expansion

Let `t_x` solve `K_m'(t_x)=x`, and let

\[
I_m(x)=t_xx-K_m(t_x).
\]

In the range `x=O(sqrt(L))`, `m/L^{5/3}->infinity`, expansion of the inverse saddlepoint equation gives

\[
\frac{x^2}{2}-I_m(x)
=
\frac{\sqrt2\rho_m}{3\sqrt m}x^3
+
\left(\frac12-\rho_m^2\right)\frac{x^4}{m}
+o(1).
\tag{11}
\]

For completeness, the quartic coefficient contains the square of the cubic term: if

\[
K(t)=t^2/2+A t^3+B t^4+\cdots,
\]

then

\[
I(x)=x^2/2-Ax^3+(9A^2/2-B)x^4+\cdots.
\]

Here `A=sqrt(2) rho_m/(3 sqrt(m))` and `B=1/(2m)`.

Exponential tilting at `t_x`, followed by Berry--Esseen under the tilted law, gives the standard saddlepoint prefactor

\[
\mathbb P\{Q_{m,1}>x\}
=
\frac{e^{-I_m(x)}}{t_x\sqrt{2\pi K_m''(t_x)}}(1+o(1)).
\tag{12}
\]

Indeed the tilt seen by each elementary centered chi-square summand is `O(t_x/sqrt(m))=o(1)`, the tilted third absolute moments stay uniformly bounded, and the Berry--Esseen error is `O(m^{-1/2})=o(t_x^{-1})`. Also

\[
t_x\sqrt{K_m''(t_x)}/x\to1.
\]

Normal Mills asymptotics therefore turn (11)--(12) into (1).

### 3. Extreme-value transfer

For fixed `y`, Gaussian extreme-value theory gives

\[
p\,\bar\Phi(x_p(y))\to e^{-y}.
\]

Under the finite critical-window assumptions,

\[
\rho_m^2\frac{L^2}{m}
=
\frac{\alpha_p^2}{L}\to0,
\]

and `b_p/sqrt(2L)->1`. Substitution into (1) yields

\[
\log\frac{\mathbb P\{Q_{m,1}>x_p(y)\}}{\bar\Phi(x_p(y))}
\to
\frac43\alpha+2\beta=a.
\]

Thus

\[
p\,\mathbb P\{Q_{m,1}>x_p(y)\}\to e^{a-y},
\]

and independence across coordinates gives

\[
\mathbb P\{b_p(M_{p,m}-b_p)\le y\}
\to
\exp(-e^{a-y})=\Lambda(y-a).
\]

This proves (2).

Since the same normalization sends the Gaussian maximum to `Lambda(y)` and both limiting distribution functions are continuous, Polya's theorem yields uniform convergence of both cdfs. The Kolmogorov distance therefore converges to

\[
\sup_y|\Lambda(y-a)-\Lambda(y)|.
\]

For `c=|a|>0`, writing `u=e^{-y}` reduces this to maximizing

\[
e^{-u}-e^{-e^c u}.
\]

The maximizer is `u=c/(e^c-1)`, giving (3).

The positive and balanced specializations follow by substituting `rho_m=1` and `rho_m=0`. The separation (8) follows from the same tail expansion with `m_p asymp L^{5/2}`.

## Relation to recent and classical literature

Cai and Hu (2026) study maxima of high-dimensional canonical order-two U-statistics through signed Gaussian quadratic-chaos targets. Their Theorem 3.1 gives a general comparison term of order `r_{4,min}^{-1/6} log p`, so `r_{4,min}/log^6 p -> infinity` is sufficient for the ordinary-Gaussian endpoint; their Figure 1 explicitly describes that curve as schematic rather than sharp. The present result gives exact independent flat-spectrum benchmarks and shows that a sharp transition cannot in general be indexed by `r_4` alone.

The exponents `3` and `2` are not claimed as generic new moderate-deviation exponents. Classical Cramer--Petrov theory already explains why a nonzero third cumulant limits relative Gaussian tails at `x=o(m^{1/6})`, while cancellation of the third cumulant exposes the quartic correction at `x=o(m^{1/4})`. Fang and Koike (2023), in their Wiener-chaos moderate-deviation discussion, explicitly use the positive flat centered-chi-square chaos and note sharpness of the `m^{1/6}` range. Chernozhukov, Chetverikov and Koike (2023) likewise identify `log^3 d/n` as the sharp high-dimensional skewed scale and show a `log^2 d/n` improvement in a smooth zero-skewness regime.

The originality claim here is narrower: the explicit sign-imbalance expansion (1) on the Gaussian extreme scale, the critical Gumbel translations and exact Kolmogorov limits (2)--(7), and the same-`r_4`, same-fourth-cumulant separation (8) for quadratic-chaos maxima.

## Limitations

- The coordinates are independent; this is a sharp benchmark and obstruction, not a general dependent-chaos theorem.
- The spectrum is flat in magnitude. Unequal eigenvalues require additional spectral power sums beyond the two terms used here.
- Formula (1) is stated in the regime `m/(log p)^{5/3}->infinity`, which is sufficient to control the displayed Cramer-series remainder; more extreme sparse-rank regimes are not analyzed.
- The result concerns the Gaussian-chaos target itself, not the separate finite-sample approximation from a U-statistic to that target.
- Generic `log^3` and zero-skew `log^2` high-dimensional CLT phenomena are prior art; only the quadratic-chaos critical-window and effective-rank statements above are claimed as new to the best of our knowledge.

## Reproducibility

`artifacts/verify_flat_chaos.py` evaluates exact chi-square tails for the positive family, exact Bessel-density tails for the balanced variance-gamma family, and the closed Kolmogorov gap `D(a)`. `artifacts/verification_output.txt` records the output. The numerical calculations support the analytic tail corrections but are not used as proof.

## References

1. Leheng Cai and Qirui Hu, *Approximation Theorems for High-Dimensional Canonical U-Statistics: Gaussian Chaos and Phase Transition*, arXiv:2609.20529v1 (2026). https://arxiv.org/abs/2609.20529v1
2. Xiao Fang and Yuta Koike, *From p-Wasserstein Bounds to Moderate Deviations*, Electronic Journal of Probability 28 (2023), DOI 10.1214/23-EJP976. https://arxiv.org/abs/2205.13307
3. Victor Chernozhukov, Denis Chetverikov and Yuta Koike, *Nearly optimal central limit theorem and bootstrap approximations in high dimensions*, Annals of Applied Probability 33 (2023), DOI 10.1214/22-AAP1870. https://arxiv.org/abs/2012.09513
4. Matthias Schulte and Christoph Thäle, *Cumulants on Wiener chaos: moderate deviations and the fourth moment theorem*, Bernoulli 22 (2016). https://arxiv.org/abs/1410.7964
