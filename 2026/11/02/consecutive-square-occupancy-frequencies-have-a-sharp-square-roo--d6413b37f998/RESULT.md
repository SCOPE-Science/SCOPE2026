# Consecutive-square occupancy frequencies have a sharp square-root covariance window

## Finding

Throw \(N\) distinguishable balls independently and uniformly into \(B\ge3\) labeled boxes. For each positive integer \(j\), let \(C_j\) count boxes containing exactly \(j\) balls. Fix an integer \(k\ge1\), and put
\[
r=k^2,\qquad s=(k+1)^2,\qquad a=k(k+1).
\]
For every \(N\ge r+s\), define
\[
R_B(N;r,s)=\frac{B-1}{B}\frac{(N-r)_s}{(N)_s}
\frac{(1-2/B)^{N-r-s}}{(1-1/B)^{2N-r-s}},
\]
where \((z)_s=z(z-1)\cdots(z-s+1)\) is the falling factorial. Then
\[
\operatorname{Cov}(C_r,C_s)=B^2p_rp_s\bigl(R_B(N;r,s)-1\bigr),
\quad p_j=\binom Nj B^{-j}(1-1/B)^{N-j}.
\tag{1}
\]
For each fixed \(B,r,s\), the set of \(N\ge r+s\) for which this covariance is strictly positive is an interval of integers (possibly empty). For the consecutive-square pair above, this interval is nonempty for all sufficiently large \(B\). Writing its smallest and largest members as \(N_-(B)\) and \(N_+(B)\), respectively,
\[
\boxed{N_\pm(B)=aB\pm\sqrt{aB}+O_k(1).}
\tag{2}
\]
Thus the positive-dependence window has width \(2\sqrt{aB}+O_k(1)\), although the number of balls itself is of order \(B\).

More sharply, for every fixed real \(u\) and every integer sequence \(N=N(B)\) satisfying \((N-aB)/\sqrt B\to u\),
\[
\boxed{\lim_{B\to\infty}\operatorname{Cov}(C_{k^2},C_{(k+1)^2})
=\frac{e^{-2a}a^{r+s}}{r!s!}\left(1-\frac{u^2}{a}\right).}
\tag{3}
\]
The limiting covariance is positive inside \(|u|<\sqrt a\), negative outside \(|u|>\sqrt a\), and zero at the two limiting boundaries. Equation (2), not merely the vanishing value in (3), locates the finite-sample sign changes.

The consecutive-square pairs are *exactly* the distinct positive integer frequency pairs at which the usual order-\(B\) limiting covariance has a double zero. For example, singleton and fourfold-occupied boxes have a positive covariance window centered at \(N=2B\), with endpoints \(2B\pm\sqrt{2B}+O(1)\), and at the center their covariance tends to \(4e^{-4}/3>0\).

## Assumptions and scope

All boxes have probability \(1/B\), and the number of balls \(N\) is fixed, not Poissonized. The asymptotic statements hold as \(B\to\infty\) with the square index \(k\) fixed. The exact ratio and interval property apply to every \(1\le r<s\) and every \(N\ge r+s\), not just square pairs. For \(N<r+s\), both frequency classes cannot occur together; this range is not needed for (2)–(3). No statement of stochastic association or joint distributional convergence follows from the covariance result.

## Proof

**1. Exact mixed moment.** For two distinct boxes, multinomial allocation gives
\[
\Pr\{N_1=r,N_2=s\}
=\frac{N!}{r!s!(N-r-s)!} B^{-r-s}(1-2/B)^{N-r-s}=:p_{rs}.
\]
The diagonal product of indicators for two *different* frequency classes is zero, so
\[
\mathbb E C_r=Bp_r,\quad\mathbb E C_s=Bp_s,\quad
\mathbb E(C_rC_s)=B(B-1)p_{rs}.
\]
Algebraic cancellation yields (1) and its displayed expression for \(R_B\). Both marginal probabilities are strictly positive in the stated range, so the sign is exactly that of \(R_B-1\).

**2. Exact single-interval property.** Cancelling adjacent falling factorials yields, for every \(N\ge r+s\),
\[
\frac{R_B(N+1;r,s)}{R_B(N;r,s)}
=\frac{B(B-2)}{(B-1)^2}
\left(1+\frac{rs}{(N+1-r-s)(N+1)}\right).
\tag{4}
\]
The right side decreases *strictly* with \(N\) and tends to \(B(B-2)/(B-1)^2<1\). Hence \(R_B\) is strictly log-concave as a function of integer \(N\), and the strict superlevel set \(\{N:R_B(N)>1\}\) is a contiguous integer interval. Also \(R_B(N)\to0\) as \(N\to\infty\) for fixed \(B\).

**3. Dense-allocation expansion.** For fixed \(r,s\), write \(\lambda=N/B\) and restrict \(\lambda\) to a compact subset of \((0,\infty)\). Taylor expansion of the logarithms in (1), including the finite sum \(\sum_{j=0}^{s-1}\log(1-r/(N-j))\), gives uniformly
\[
\log R_B(N;r,s)=
-\frac{\lambda^2-(r+s-1)\lambda+rs}{\lambda B}
+\frac{H_{r,s}(\lambda)}{B^2}+O_{r,s}(B^{-3}),
\tag{5}
\]
where
\[
H_{r,s}(\lambda)=\frac{3(r+s)-1}{2}-2\lambda
-\frac{rs(r+s-1)}{2\lambda^2}.
\tag{6}
\]
The coefficient of \(B^{-1}\) vanishes to second order in \(\lambda\) precisely when the discriminant
\[
(r+s-1)^2-4rs=(s-r-1)^2-4r
\]
is zero. Since \(1\le r<s\) are integers, this means exactly \(r=k^2\) and \(s=(k+1)^2\) for an integer \(k\ge1\). With \(a=k(k+1)\), we have \(rs=a^2\), \(r+s-1=2a\), and \(H_{r,s}(a)=1\). Equation (5) therefore reads
\[
\log R_B(N;r,s)=-\frac{(\lambda-a)^2}{\lambda B}
+\frac{H_{r,s}(\lambda)}{B^2}+O_k(B^{-3}).
\tag{7}
\]

**4. Window and limiting covariance.** Let \(N=aB+u\sqrt B+o(\sqrt B)\). From (7),
\[
B^2\log R_B(N;r,s)\longrightarrow1-\frac{u^2}{a}.
\tag{8}
\]
Also \(p_r\to e^{-a}a^r/r!\) and \(p_s\to e^{-a}a^s/s!\). Since \(R_B-1\sim\log R_B\) on this scale whenever the leading constant in (8) is nonzero (and the additive convergence still holds when it is zero), multiplying equation (1) gives (3).

At \(N=r+s\) with \(r,s\) fixed, the ratio \(R_B\) tends as \(B\to\infty\) to \(r!s!/(r+s)!<1\). Near \(N=aB\), equation (8) makes the ratio greater than one for sufficiently large \(B\). At any fixed \(\lambda\ne a\) with \(N/B\to\lambda\), the first term of (7) is negative and dominates. Strict log-concavity from (4) therefore supplies precisely one bounded positive interval whose endpoints lie at the two roots of the critical profile. For \(|N-aB|\le C\sqrt B\), expansion (7) has the uniform refinement
\[
B^2\log R_B(N;r,s)
=1-\frac{(N-aB)^2}{aB}+O_{k,C}(B^{-1/2}).
\tag{9}
\]
Testing integers an appropriately large fixed distance on either side of each value \(aB\pm\sqrt{aB}\) makes the main term dominate the error; using contiguity proves (2).

## Verification

The included `verify.py` is standalone Python using only the standard library. Running `python verify.py` reproduces direct exhaustive assignment enumeration for small box systems, compares two independently factored exact covariance formulas, tests strict log-concavity at thousands of finite points, and checks critical intervals and central limits at increasing sizes. It returned `PASS: 10634 finite exact-arithmetic/asymptotic consistency assertions`. Enumeration and finite asymptotic comparisons do not establish (2)–(3) for infinitely many boxes; that is the function of the analytical proof above.

## Relationship to prior work

Gnedin, Hansen, and Pitman's 2007 occupancy survey gives marginal frequency-count moments and explicitly notes that general fixed-sample covariance formulas may be obtained by similar calculations (Section 2, around its equations (2)–(4)). Such formulas imply the raw identity (1) by specializing to equal box probabilities; that identity itself is **not claimed as new**. Barbour and Gnedin (2008/2009) study joint occupancy-frequency fluctuations and correlation structures in an infinite-frequency setting, including Poissonization and de-Poissonization. The inspected sections do not establish the consecutive-square arithmetic degeneracy, the nonvanishing second-order limit (3), or the sharp mesoscopic sign window (2) for growing numbers of equal-probability boxes.

A published exact one-switch theorem for covariance between *total occupied-box count* and a *single frequency class* concerns a sum over the other frequency classes. Neither that aggregate formula nor the fixed-bin occupied-indicator precision theorem determines the individual off-diagonal covariance in (3), so those results do not imply the square-pair window. The conclusion is a targeted statement comparison, not a claim of uniqueness across all historical literature.

## Limitations

The analysis concerns pairwise covariance for fixed positive occupancy levels and growing uniform box systems. There is no claim about nonuniform allocations, the entire covariance spectrum, or nonlinear dependence. At the limiting boundary \(|u|=\sqrt a\), the leading limit in (3) is zero; the exact sign requires the finite integer location, for which (2) gives only an \(O_k(1)\) localization. Earlier classical random-allocation texts may encode equivalent second-order expansions under different notation, and priority beyond the inspected materials remains uncertain.

## References

1. A. Gnedin, B. Hansen, and J. Pitman, “Notes on the occupancy problem with infinitely many boxes: general asymptotics and power laws,” *Probability Surveys* 4 (2007), 146–171, arXiv:math/0701718 (first public version 2007-01-24), https://arxiv.org/abs/math/0701718.
2. A. D. Barbour and A. V. Gnedin, “Small counts in the infinite occupancy scheme,” arXiv:0809.4387 (first public version 2008-09-25), https://arxiv.org/abs/0809.4387; *Electronic Journal of Probability* 14 (2009), 365–384.
3. “A one-switch covariance law for occupancy richness and frequency counts,” published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-one-switch-covariance-law-for-occupancy-richness-and-frequency--93dddb2be813 (accessed for statement comparison).
4. “Occupied-box indicators have a strictly positive precision matrix,” published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-occupied-box-indicators-have-a-strictly-positive-precision-matri--0606274d4166 (accessed for statement comparison).
