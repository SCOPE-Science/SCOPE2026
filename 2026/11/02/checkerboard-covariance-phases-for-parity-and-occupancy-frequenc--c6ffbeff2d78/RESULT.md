# Checkerboard covariance phases for parity and occupancy frequencies

## Finding

Place \(N\) distinguishable balls independently and uniformly into \(B\) labeled boxes. Write \(X_i\) for the load of box \(i\), \(O_N=\sum_{i=1}^B\mathbf 1\{X_i\text{ is odd}\}\) for the number of odd-load boxes, and \(C_{N,r}=\sum_{i=1}^B\mathbf 1\{X_i=r\}\) for the number of boxes containing exactly \(r\) balls. Equivalently, \(O_N\) is the Hamming weight after \(N\) steps of the nearest-neighbor random walk on the \(B\)-cube that flips a uniformly chosen coordinate at each step, and \(C_{N,r}\) counts coordinates flipped exactly \(r\) times.

For all integers \(B\ge4\), \(N\ge2\), and \(1\le r\le N\), define
\[
 a=1-\frac2B,\qquad b=1-\frac2{B-1},\qquad
 p_{N,r}=\binom Nr B^{-r}(1-B^{-1})^{N-r}.
\]
Then the exact covariance is
\[
\boxed{\operatorname{Cov}(O_N,C_{N,r})
 =\frac{Bp_{N,r}}2\bigl[(-1)^{r+1}+Ba^N-(B-1)b^{N-r}\bigr].}
\]
Its **complete finite-size sign classification** is:

1. The covariance is strictly negative for every even \(r\ge2\).
2. The covariance is strictly positive when \(r=1\).
3. At each fixed odd \(r\ge3\), as the integer sample size \(N\) runs through \(r,r+1,\ldots\), there is exactly one negative-to-positive transition, possibly with one intervening zero value. Thus the covariance is negative before the transition and positive afterward; at most one sample size has covariance zero.
4. At fixed \(B,N\), the signs at **odd** frequencies \(r=1,3,5,\ldots\le N\) form an initial positive segment followed by a possibly empty negative segment, with at most one zero frequency in between; all even frequencies are negative.

For every fixed positive integer \(r\), if \(B\to\infty\) and \(N/B\to\lambda>0\), then
\[
\boxed{\frac{\operatorname{Cov}(O_N,C_{N,r})}{B}
\longrightarrow\frac{e^{-\lambda}\lambda^r}{2r!}
\left[(-1)^{r+1}+e^{-2\lambda}(1+2\lambda-2r)\right].}
\]
For each odd \(r\ge3\), the first sample size \(T_{B,r}\) of **strictly positive** covariance obeys
\[
\boxed{T_{B,r}=\lambda_r B+O_r(1),\qquad
 e^{2\lambda_r}+2\lambda_r+1=2r,\quad\lambda_r>0.}
\]
The critical density \(\lambda_r\) is unique. For example, \(\lambda_3\approx0.6533\), \(\lambda_5\approx0.9763\); the limiting covariance is negative at lower positive densities and positive at higher densities for odd \(r\ge3\).

## Assumptions and scope

All \(B^N\) allocations have equal probability. The finite theorem requires integer \(B\ge4\), \(N\ge2\), \(1\le r\le N\); no independence between box loads is assumed. The asymptotic statement fixes \(r\) and considers a strictly positive limiting density \(N/B\). Constants in \(O_r(1)\) may depend on \(r\) but not on \(B\). The walk representation uses non-lazy independent uniform-coordinate flips and starts at the origin.

## Proof

**Covariance identity.** By symmetry and linearity,
\[
 \operatorname{Cov}(O_N,C_{N,r})
 =B p_{N,r}\bigl(\mathbb E[O_N\mid X_1=r]-\mathbb EO_N\bigr).
\]
For a binomial variable \(Y\sim\operatorname{Bin}(m,q)\), the binomial theorem gives \(\mathbb P(Y\text{ odd})=(1-(1-2q)^m)/2\). Consequently
\[
 \mathbb EO_N=\frac B2(1-a^N).
\]
Conditional on \(X_1=r\), the remaining \(N-r\) balls are independent and uniform among the other \(B-1\) boxes; their individual loads are binomial with parameters \(N-r\) and \(1/(B-1)\). Hence
\[
 \mathbb E[O_N\mid X_1=r]
 =\mathbf1_{\{r\text{ odd}\}}+\frac{B-1}2(1-b^{N-r}).
\]
Substituting proves the boxed identity, including its exact normalization. Notice that \(p_{N,r}>0\).

**Even frequencies.** Put \(f_N=Ba^N-(B-1)b^N\). We have \(f_1=1\) and
\[
 f_{N+1}-f_N=-2(a^N-b^N)<0\qquad(N\ge1),
\]
since \(0<b<a<1\). For even \(r\ge2\), because \(b^{N-r}\ge b^N\), the bracket in the boxed covariance identity is at most \(-1+f_N<0\). This proves strict negativity.

**Singletons.** Put \(h_N=Ba^N-(B-1)b^{N-1}\). Here \(h_1=-1\), \(h_2>h_1\), and \(h_N\to0\). Moreover,
\[
 h_{N+1}-h_N=2\bigl(b^{N-1}-a^N\bigr).
\]
The quotient \(a^N/b^{N-1}=a(a/b)^{N-1}\) strictly increases in \(N\). Therefore \(h_N\) first increases, with a possible level pair at its maximum, then strictly decreases to zero. In particular \(h_N>-1\) for all \(N\ge2\), and the bracket for \(r=1\), which equals \(1+h_N\), is strictly positive.

**Odd frequencies and the single transition.** For odd \(r\ge3\), set
\[
 s_N=1+Ba^N-(B-1)b^{N-r}\qquad(N\ge r).
\]
At \(N=r\), \(s_r=2-B+Ba^r<0\), since \(a^r<a\) and \(Ba=B-2\). Also \(s_N\to1>0\). The first difference is
\[
 s_{N+1}-s_N=2(b^{N-r}-a^N).
\]
Because \(a^N/b^{N-r}=a^r(a/b)^{N-r}\) is strictly increasing in \(N\), these differences can change sign at most once, and only from positive to negative. Thus \(s_N\) first increases and eventually decreases to the positive limit \(1\). Starting negative and ending positive, it crosses zero exactly once in the ordered discrete sense: at most one integer \(N\) has \(s_N=0\), and all later terms are positive. This proves the complete time-direction sign classification.

For the frequency-direction statement, hold \(B,N\) fixed. On odd \(r\), the bracket \(1+Ba^N-(B-1)b^{N-r}\) strictly decreases as \(r\) increases, because \(0<b<1\). Together with singleton positivity and even-frequency negativity, this proves the asserted checkerboard pattern.

**Large-box limit and critical density.** Write \(\lambda_B=N/B\). Uniformly for \(\lambda_B\) in a fixed compact interval of positive densities and fixed \(r\), the Taylor expansions
\[
 \log a=-2/B-2/B^2+O(B^{-3}),\qquad
 \log b=-2/B-4/B^2+O(B^{-3})
\]
give
\[
 Ba^N-(B-1)b^{N-r}
 =e^{-2\lambda_B}(1+2\lambda_B-2r)+O_r(B^{-1}).
\]
Also \(p_{N,r}\to e^{-\lambda}\lambda^r/r!\) whenever \(\lambda_B\to\lambda>0\). Substitution yields the covariance limit. For odd \(r\ge3\) its limiting sign factor is
\[
 F_r(\lambda)=1+e^{-2\lambda}(1+2\lambda-2r)
 =e^{-2\lambda}(e^{2\lambda}+2\lambda+1-2r).
\]
The expression \(e^{2\lambda}+2\lambda+1\) is strictly increasing from \(2\) to infinity; thus \(F_r\) has a unique positive zero \(\lambda_r\), crosses from negative to positive, and has \(F'_r(\lambda_r)>0\). The uniform error \(O_r(B^{-1})\), Taylor expansion at this simple zero, and the already proved single sign transition trap the first positive integer \(T_{B,r}\) between \(\lambda_rB\pm K_r\) for a sufficiently large constant \(K_r\). Therefore \(T_{B,r}=\lambda_rB+O_r(1)\), completing the proof.

## Verification

Run `python3 verify.py` using only the Python standard library. The program performs direct allocation enumeration (not invoking the conditional-mean proof) for small sizes; exact-rational evaluation of the closed formula for a broad finite parameter grid; deterministic sign checks; and floating-point comparisons against the large-box limit. The current run reports `VERIFY_OK 144293`, meaning 144,293 executed assertions/check increments. Analytical arguments above, not these finite tests, establish the statements for all admissible parameters. The separate `VERIFICATION.md` records check scope and boundaries.

## Relationship to prior work

Gnedin, Hansen and Pitman (2007) survey classical occupancy counts, moments and asymptotics; Barbour and Gnedin (2008) analyze joint distributions of fixed occupancy-frequency counts under general infinite-box schemes. Those frameworks provide the natural moment background and can imply portions of the large-box covariance calculation, but the inspected arguments do not supply this finite uniform-box parity-frequency checkerboard sign classification, its unique time-direction switch, or the sharp \(O_r(1)\) threshold localization. Nestoridi (2015) treats hypercube walks and mixing; the present joint dependence concerns the walk's current Hamming weight and its historical coordinate-flip frequency profile, rather than mixing times. The elementary exact conditional-mean identity is not claimed to be a new general occupancy-moment technique.

## Limitations

The result concerns only iid uniform allocations and the non-lazy nearest-neighbor hypercube walk. It makes no claim for unequal box probabilities, other dynamics, or the excluded small dimensions. The asymptotic localization holds for fixed odd frequencies; growing frequencies may have different critical regimes. Generic classical multivariate occupancy formulas may encode the covariance after algebraic extraction, and uninspected historical results could contain an equivalent finite classification; priority is not independently established.

## References

1. A. Gnedin, B. Hansen, J. Pitman, *Notes on the occupancy problem with infinitely many boxes: general asymptotics and power laws* (public preprint 24 January 2007), arXiv:math/0701718, https://arxiv.org/abs/math/0701718.
2. A. D. Barbour, A. V. Gnedin, *Small counts in the infinite occupancy scheme* (public preprint 25 September 2008), arXiv:0809.4387, https://arxiv.org/abs/0809.4387.
3. E. Nestoridi, *A non-local random walk on the hypercube* (public preprint 21 July 2015), arXiv:1507.05690, https://arxiv.org/abs/1507.05690.
