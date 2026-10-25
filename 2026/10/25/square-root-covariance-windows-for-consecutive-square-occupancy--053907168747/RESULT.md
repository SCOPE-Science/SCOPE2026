# Square-root covariance windows for consecutive-square occupancy frequencies

## Finding

Throw \(n\) labeled balls independently and uniformly into \(m\) labeled boxes. Let \(X_r\) count boxes containing exactly \(r\) balls. Fix any positive integer \(a\), and set
\[
r=a^2,\qquad s=(a+1)^2,\qquad \lambda=a(a+1).
\]
For \(m\ge3\) and \(n\ge r+s\), write \(C_m(n)=\operatorname{Cov}(X_r,X_s)\).

**Critical-window theorem.** For every fixed real \(z\), and every integer sequence \(n_m\) satisfying \((n_m-\lambda m)/\sqrt m\to z\),
\[
\boxed{\displaystyle
C_m(n_m)\longrightarrow
\frac{e^{-2\lambda}\lambda^{r+s}}{r!s!}
\left(1-\frac{z^2}{\lambda}\right).}
\tag{1}
\]
In particular, at the first critical pair \((r,s)=(1,4)\), \(\lambda=2\), the limit is \(\frac43 e^{-4}(1-z^2/2)\).

For each sufficiently large \(m\), the set of integers \(n\ge r+s\) for which \(C_m(n)>0\) is a nonempty, finite, contiguous integer interval. Writing its smallest and largest members \(n_-(m)\) and \(n_+(m)\),
\[
\boxed{n_\pm(m)=\lambda m\pm\sqrt{\lambda m}+o(\sqrt m).}
\tag{2}
\]
Thus these critical pairs have a positive-covariance window with a square-root, rather than linear, width in \(m\). Formula (1) gives a signed, nonzero order-one profile inside and outside that window. It does not assign the eventual sign at \(z=\pm\sqrt\lambda\).

## Assumptions and scope

Here \(m\ge3\) and \(n\ge r+s\) are integers; \(a\ge1\) is fixed when \(m\to\infty\). All balls are independently assigned to one of the \(m\) boxes with equal probability. Only pairs of successive *square* positive loads \(r=a^2\) and \(s=(a+1)^2\) are covered. The limit in (1) is a covariance limit; it does not assert a nondegenerate limiting law for a centered random variable.

## Proof

Put \(u=(m-1)/m\) and \(v=(m-2)/m\). Specifying a box containing exactly \(r\) balls gives
\[
\mathbb E X_r=\binom nr m^{1-r}u^{n-r},\qquad
\mathbb E X_s=\binom ns m^{1-s}u^{n-s}.
\]
For distinct specified boxes, choose their disjoint sets of \(r\) and \(s\) balls and direct all remaining balls elsewhere. Since \(r\ne s\),
\[
\mathbb E[X_rX_s]
=m(m-1)\binom nr\binom{n-r}s m^{-r-s}v^{n-r-s}.
\]
Consequently the normalized coincidence ratio
\[
R_{m,n}=\frac{\mathbb E[X_rX_s]}{\mathbb EX_r\,\mathbb EX_s}
=u\frac{\binom{n-r}s}{\binom ns}\frac{v^{n-r-s}}{u^{2n-r-s}}
\tag{3}
\]
is strictly positive, and \(C_m(n)=\mathbb EX_r\mathbb EX_s(R_{m,n}-1)\). Cancellation of factorials in (3) gives
\[
\frac{R_{m,n+1}}{R_{m,n}}
=\frac{m(m-2)}{(m-1)^2}
\left(1+\frac{rs}{(n+1)(n+1-r-s)}\right).
\tag{4}
\]
The second factor strictly decreases with \(n\ge r+s\), while the first is strictly below one. Hence the positive set \(\{n:R_{m,n}>1\}\) is a contiguous interval (possibly empty). Also \(R_{m,n}\to0\) as \(n\to\infty\) at fixed \(m\), because (3) has a decaying factor \(m(m-2)/(m-1)^2<1\) raised to order \(n\). Thus any such interval is finite.

To resolve the critical scale, put \(t=n/m\). Uniformly when \(t\) lies in a fixed compact subinterval of \((0,\infty)\), while \(r,s\) are fixed, take logarithms of (3):
\[
\log R_{m,n}
=\sum_{j=0}^{s-1}\log\left(1-\frac r{n-j}\right)
+(n-r-s)\log(1-2/m)
-(2n-r-s-1)\log(1-1/m).
\tag{5}
\]
Taylor expansion, with uniform remainder since each denominator is of order \(m\), gives
\[
\log R_{m,n}=\frac{F(t)}m+\frac{G(t)}{m^2}+O(m^{-3}),
\tag{6}
\]
where
\[
F(t)=-t+(r+s-1)-\frac{rs}{t},
\qquad
G(t)=-2t+\frac{3(r+s)-1}{2}-\frac{rs(r+s-1)}{2t^2}.
\tag{7}
\]
For completeness, the first logarithmic sum in (5) equals
\[
-\frac{rs}{mt}-\frac{rs(r+s-1)}{2m^2t^2}+O(m^{-3});
\]
expanding the remaining two logarithms to cubic order gives \(\bigl[-t+(r+s-1)\bigr]/m+\bigl[-2t+(3(r+s)-1)/2\bigr]/m^2+O(m^{-3})\), confirming (6)--(7).

For consecutive squares, \(r+s-1=2\lambda\) and \(rs=\lambda^2\). Thus
\[
F(t)=-\frac{(t-\lambda)^2}{t},\qquad G(\lambda)=1.
\]
If \((n_m-\lambda m)/\sqrt m\to z\), then \(t_m=\lambda+z/\sqrt m+o(m^{-1/2})\), so
\[
m^2\log R_{m,n_m}\to1-\frac{z^2}{\lambda},
\qquad
m^2(R_{m,n_m}-1)\to1-\frac{z^2}{\lambda}.
\tag{8}
\]
The moment formulas yield
\[
\frac{\mathbb EX_r\,\mathbb EX_s}{m^2}
\longrightarrow\frac{e^{-2\lambda}\lambda^{r+s}}{r!s!}.
\]
Combining this with (8) proves (1).

Taking \(z=0\) in (1) shows that the positive-covariance interval is eventually nonempty. For each \(\varepsilon\in(0,\sqrt\lambda)\), the limit has positive sign at \(z=\pm(\sqrt\lambda-\varepsilon)\) and negative sign at \(z=\pm(\sqrt\lambda+\varepsilon)\). The exact one-interval property from (4) therefore traps its two endpoints between those corresponding scaled positions. Letting \(\varepsilon\downarrow0\) proves (2). \(\square\)

## Verification

The accompanying `verify_occupancy_boundary.py` independently enumerates all allocations for small pairs of parameters and checks the moment and covariance formulas using exact rational arithmetic. It then checks the exact two-load event identities and one-step ratio for four successive-square pairs over a bounded parameter grid, and independently checks the second-order limits with 65-digit arithmetic. The recorded output is `PASS 3242 finite exact/high-precision checks`. These computations corroborate finite instances and scaling approximations; the unbounded claims follow from (3)--(8).

## Relationship to prior work

The original occupancy-frequency statistics and their joint dependence have a long history. Eaton, Godbole and Sinclair (2008), in their full preprint, treat exact-occupancy counts and multivariate Poisson approximation in the sparse regime \(n/m\to0\), not the present dense scaling \(n/m\to\lambda\). Barbour and Gnedin (2008) analyze multivariate normal approximation and limiting covariance structures for infinitely many heterogeneous boxes, not the equal-box, fixed-load critical window (1). Kahn and Neiman (2010) analyze negative dependence in competing urns under distinct monotonicity conditions; such results do not determine the sign of two exact-load frequency counts.

An earlier finite uniform pair-frequency analysis supplies the general normalized-ratio log-concavity and the leading covariance limit for fixed \(r,s\). Its first-order limit *vanishes* at every consecutive-square pair: \((r+s-1)^2=4rs\). Neither strict log-concavity nor that zero leading limit implies the sign, the order-one amplitude, or the square-root endpoint scale in (1)--(2). The contribution here is the next-order, uniformly controlled critical expansion and its all-pairs endpoint consequence, not the classical counting identity or generic first-order log-concavity.

## Limitations

The result concerns independent equal-probability allocations and fixed positive integer \(a\); it does not establish uniformity as \(a\to\infty\). It does not classify equality or finite-size zero covariance at the window boundaries, and the limit at \(z=\pm\sqrt\lambda\) is zero without determining smaller-order signs. An exact general finite formula for the normalized ratio is classical in spirit, and older occupancy sources may contain implicit expansions: priority remains provisional. There is no independent mathematical audit.

## References

1. J. Eaton, A. Godbole and B. Sinclair, “Competition between Discrete Random Variables, with Applications to Occupancy Problems,” arXiv:0806.1007v1, first submitted 2008-06-05; subsequently *J. Statistical Planning and Inference* 140 (2010), 2204–2212.
2. A. D. Barbour and A. V. Gnedin, “Small counts in the infinite occupancy scheme,” arXiv:0809.4387v1, submitted 2008-09-25; *Electronic Journal of Probability* 14 (2009), 365–384.
3. J. Kahn and M. Neiman, “Conditional negative association for competing urns,” arXiv:1001.0610v1, submitted 2010-01-05.
