# Universal cubic diffusivity crossover under rapid environment regeneration

## Finding

For the one-dimensional nearest-neighbor random walk in an independent, globally regenerated random environment, write \(p\) for the probability of refreshing the entire environment after each step. Each fresh environment consists of independent site probabilities \(\omega_x\in[0,1]\) for a rightward step. Put
\[
\delta=2\mathbb E\omega_0-1,\qquad s=\operatorname{Var}(\omega_0),\qquad r=1-p.
\]
Let \(\sigma^2(p)\) denote the annealed asymptotic variance per step in the regenerative central limit theorem. **Uniformly over every law of \(\omega_0\in[0,1]\)** and every \(0\le r\le1/4\),
\[
\boxed{\sigma^2(1-r)=1-\delta^2+12\delta^2s\,r^2-8s^2r^3+R(r),\qquad |R(r)|\le86400r^4.}
\]
In particular, whenever \(\delta=0\) and \(s>0\), complete regeneration \(p=1\) is a strict one-sided **local maximum** of diffusivity. The case \(\delta\ne0\), \(s>0\), has the opposite local sign, as already implied by the positive quadratic term established by Martin and Nagel.

The expansion resolves the near-centered crossover **uniformly**, even when the environmental law changes with \(r\). Specifically, fix \(\nu>0\), \(0<\eta<2/3\), and \(s\ge\nu\). For
\[
0<r<\min\left\{\frac14,\frac{\eta\nu^2}{7200}\right\},
\]
the strict sign is
\[
\begin{aligned}
\delta^2\le(2/3-\eta)sr&\quad\Longrightarrow\quad\sigma^2(1-r)<\sigma^2(1),\\
\delta^2\ge(2/3+\eta)sr&\quad\Longrightarrow\quad\sigma^2(1-r)>\sigma^2(1).
\end{aligned}
\]
Consequently, if \(r\downarrow0\) along any family with \(s\to s_0>0\) and \(\delta/\sqrt r\to\kappa\), then
\[
\frac{\sigma^2(1-r)-\sigma^2(1)}{r^3}
\longrightarrow 12\kappa^2s_0-8s_0^2
=4s_0(3\kappa^2-2s_0).
\]
The switch occurs at the sharp scale \(\delta^2=(2/3)sr\). Neither the sign exactly on this critical line nor higher-order terms are claimed.

## Assumptions and scope

For every integer time, first choose a nearest-neighbor step at current site \(x\), right with probability \(\omega_x\), left otherwise, and **after that step** independently replace the entire field by a freshly sampled iid field with probability \(p\). All refresh decisions and fields are independent. The starting point is zero. The site-law can have atoms at zero or one; no uniform ellipticity or higher moments are assumed. The law may depend on \(r\) in the uniform inequalities. The conclusion concerns the annealed central-limit variance \(\sigma^2(p)\), not the variance of a fixed-time position or a quenched effective variance. Only \(p\ge3/4\) is needed for the explicit bound.

Let \(Z_m\) be the displacement after \(m\) steps in **one** static field with the same site law, averaged over paths and fields, and let \(v(p)\) be the annealed limiting velocity. The length \(L\) of each complete regeneration block is geometric with \(\Pr(L=m)=p(1-p)^{m-1}\). Regeneration gives iid pairs \((L,Z_L)\) and \(\mathbb E L=1/p\). Thus
\[
v(p)=p^2\sum_{m\ge1}(1-p)^{m-1}\mathbb E Z_m,
\qquad
\sigma^2(p)=p^2\sum_{m\ge1}(1-p)^{m-1}\mathbb E\!\left[(Z_m-mv(p))^2\right].
\]
These formulas agree with Martin and Nagel's equations (3.1) and (3.15). They are absolutely convergent for \(p>0\) since \(|Z_m|\le m\).

## Proof

**1. Static four-step identities.** Let \(a=\mathbb E\omega_0=(1+\delta)/2\) and \(b=\mathbb E\omega_0^2=a^2+s\). For a directed path of length \(m\), let \(R_x,L_x\) count right and left departures from site \(x\). Its annealed probability is exactly
\[
\prod_x \mathbb E\left[\omega_x^{R_x}(1-\omega_x)^{L_x}\right].
\]
Every site has at most two departures when \(m\le4\). The only required single-site factors are \(1,a,1-a,b,a-b,1-2a+b\) (respectively for zero departures, one right, one left, two right, one each, two left). Enumerating the \(2^m\) paths for \(m=1,2,3,4\) therefore yields the exact identities
\[
\begin{array}{c|c|c}
 m&\mathbb E Z_m&\mathbb E Z_m^2\\\hline
 1&\delta&1\\
 2&2\delta&2(1+\delta^2)\\
 3&\delta(3-2s)&3(1+2\delta^2)\\
 4&4\delta(1-s)&4(1+3\delta^2-2\delta^2s-2s^2).
\end{array}
\]
The supplied standalone program exactly enumerates all 30 directed histories and verifies these eight identities as exact symbolic polynomials for arbitrary \(a,b\), together with the power-series identities below. No sampling or numerical fit is involved.

**2. Taylor coefficients.** Set \(r=1-p\), \(u(r)=v(1-r)\). The speed series and the preceding moments show, through degree three,
\[
u(r)=(1-r)^2\sum_{m\ge1}(\mathbb E Z_m)r^{m-1}
=\delta-2\delta s\,r^2+O(r^4).
\]
Indeed, the coefficients of \(r\) and \(r^3\) vanish. Substitute this series into the exact variance identity
\[
\begin{aligned}
\Sigma(r):=\sigma^2(1-r)
=(1-r)^2\sum_{m\ge1}r^{m-1}\bigl(&\mathbb E Z_m^2
-2m\,u(r)\mathbb E Z_m+m^2u(r)^2\bigr).
\end{aligned}
\]
For coefficients through \(r^3\) only \(m\le4\) enters. Expanding and collecting coefficients gives, respectively,
\[
[r^0]\Sigma=1-\delta^2,\quad [r^1]\Sigma=0,\quad
[r^2]\Sigma=12\delta^2s,\quad [r^3]\Sigma=-8s^2.
\]
The cubic coefficient is independent of the mean drift and of all site moments above order two.

**3. Universal error bound.** The following complex bounds require only \(|Z_m|\le m\). For \(|r|\le1/2\), the speed series defines a holomorphic function with
\[
|u(r)|\le |1-r|^2\sum_{m\ge1}m|r|^{m-1}
\le(3/2)^2\cdot4=9.
\]
For the variance series, bound each summand by \(m^2(1+|u(r)|)^2\). Therefore on \(|r|\le1/2\),
\[
|\Sigma(r)|\le(3/2)^2(1+9)^2\sum_{m\ge1}m^2(1/2)^{m-1}
=\frac94\cdot100\cdot12=2700.
\]
Cauchy's coefficient estimate yields \(|[r^k]\Sigma|\le2700\,2^k\) for every \(k\ge0\). Hence for real \(0\le r\le1/4\),
\[
|R(r)|\le2700\sum_{k\ge4}(2r)^k
\le\frac{2700(2r)^4}{1-2r}\le86400r^4.
\]
The bound is thus simultaneous across all site laws, including families depending on \(r\).

**4. Strict signs and sharp scaling.** At \(p=1\) the steps are iid with mean \(\delta\) and variance \(1-\delta^2\). Subtracting this baseline yields
\[
\Sigma(r)-\Sigma(0)=12sr^2\left(\delta^2-\frac23sr\right)+R(r).
\]
On either claimed side of the threshold, the first term has absolute value at least \(12\eta s^2r^3\ge12\eta\nu^2r^3\); the remainder is strictly smaller when \(r<\eta\nu^2/7200\). This establishes both inequalities. For a fixed mean-zero law with \(s>0\), divide by \(r^3\) and let \(r\downarrow0\) to get the strictly negative limit \(-8s^2\). For triangular laws substitute \(\delta/\sqrt r\to\kappa\) and \(s\to s_0\), and divide the uniform expansion by \(r^3\). Sharpness is substantive: take \(\omega_0=(1+\delta)/2\pm1/4\), each with probability \(1/2\), so \(s=1/16\); the choices \(\delta=\kappa\sqrt r\) realize every fixed finite \(\kappa\) for sufficiently small \(r\).

## Verification

Run `python verify_crossover.py` with Python 3 and SymPy installed, from the directory containing that file. The program enumerates all \(2+4+8+16=30\) directed paths, checks their exact annealed probabilities sum to one, verifies eight moment formulas, the four speed coefficients, four diffusivity coefficients and the crossover coefficient. A successful run reports 17 checked symbolic identities. The analytic convergence, universal Cauchy remainder and strict inequalities are mathematical deductions in the proof, not conclusions from the finite code checks.

## Relationship to prior work

Martin and Nagel [1] establish the regeneration representation and show that the first derivative of \(\sigma^2\) vanishes at \(p=1\), while the second derivative equals \(24\delta^2s\). Their stated strict-minimum conclusion assumes nonzero mean drift. The new claim concerns the previously degenerate zero-drift case, the universal negative cubic term, and the uniform crossover when drift is allowed to approach zero along with the nonrefresh probability. Their general power series is acknowledged as an essential starting point, and the two already known Taylor coefficients are not represented as new. Avena and den Hollander [2] and Avena, Chino, da Costa and den Hollander [3] study deterministic cooling schedules rather than the quantitative rapid **geometric** refresh crossover here.

## Limitations

No conclusion is asserted for \(p<3/4\) by the displayed uniform bound, for the exact order-four behavior on the critical crossover curve, or for static-environment diffusion at \(p=0\). The extremely conservative constant \(86400\) is not optimized. The sharpness refers to the **leading crossover scale** \(\delta^2/(sr)=2/3\), not optimality of that remainder constant. The result is annealed, one-dimensional, nearest-neighbor, and requires independent global refresh. An equivalent higher-order expansion may exist elsewhere in the random-environment literature; independent priority assessment has not been performed.

## References

[1] Raphael Martin and Jan Nagel, *Random walk in a regenerating random environment*, arXiv:2610.11919v1 (first public 8 October 2026), particularly Theorem 2.4, Lemma 3.3 and equations (3.1), (3.15). https://arxiv.org/html/2610.11919v1

[2] Luca Avena and Frank den Hollander, *Random walks in cooling random environments*, arXiv:1610.00641v2 (2016/2017), especially the model and principal limit results. https://arxiv.org/abs/1610.00641

[3] Luca Avena, Yuki Chino, Conrado da Costa and Frank den Hollander, *Random walk in cooling random environment: ergodic limits and concentration inequalities*, arXiv:1803.03295v1 (2018). https://arxiv.org/abs/1803.03295
