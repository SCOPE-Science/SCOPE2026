# A sharp two-turning-point transition in run-and-tumble escape-time variance

## Finding

For the precisely specified active-particle first-passage process below, the mean exit time is strictly increasing in the bulk reversal rate, but the exit-time variance changes from having **exactly two positive stationary points** to being strictly increasing as boundary detachment is strengthened. There is one and only one positive critical boundary parameter for this change, and the two stationary points merge with a square-root law.

With dimensionless bulk reversal rate \(a>0\), excess wall-release rate \(g>0\), and dimensionless exit time \(Y\), the first two cumulants are

\[
\mathbb E Y=1+a+\frac{a}{a+g},
\]

\[
V(a,g):=\operatorname{Var}(Y)=\frac{a\big(2a^3+4a^2g+8a^2+2ag^2+12ag+9a+4g^2+6g+6\big)}{3(a+g)^2}.
\]

Define the polynomial

\[
\begin{aligned}
Q(a,g)={}&2a^4+(6g+4)a^3+(6g^2+12g)a^2\\
&+(2g^3+10g^2+6g-3)a+2g^3+3g^2+3g.
\end{aligned}
\]

There is a **unique** pair \((a_c,g_c)\in(0,\infty)^2\) with \(Q(a_c,g_c)=\partial_aQ(a_c,g_c)=0\). Numerically, \(a_c\approx0.2876511346855765\) and \(g_c\approx0.1138909239202156\). Exactly the following alternatives hold, with derivatives taken at fixed \(g\):

1. If \(0<g<g_c\), the variance has exactly two positive stationary points \(a_-(g)<a_+(g)\). It increases, then decreases, then increases, so these are a strict local maximum and a strict local minimum, respectively.
2. If \(g=g_c\), the variance is strictly increasing, with a single horizontal stationary inflection at \(a_c\).
3. If \(g>g_c\), the variance is strictly increasing and has no stationary point on \((0,\infty)\).

Moreover, as \(g\uparrow g_c\),

\[
a_\pm(g)=a_c\pm C\sqrt{g_c-g}+O(g_c-g),\qquad C=\sqrt{\frac{2\,\partial_gQ(a_c,g_c)}{\partial_{aa}Q(a_c,g_c)}}\approx1.0696933247.
\]

In all regimes, \(\partial_a\mathbb E Y=1+g/(a+g)^2>0\). Thus the fluctuation transition cannot be detected by monitoring monotonicity of mean escape time. For instance, at \(g=1/20\), the two variance extrema occur near \(a=0.0601699171\) and \(a=0.6083019433\), with respective variances approximately \(11.43184\) and \(7.31655\).

## Assumptions and scope

Fix a distance \(L>0\), speed \(v>0\), bulk direction-reversal rate \(\rho\ge0\), and a strictly positive additional wall-release rate \(\eta>0\). A particle occupies the interval \([0,L]\), and moves at deterministic velocity \(+v\) or \(-v\), reversing direction at independent rate \(\rho\) while in the interior. On reaching the left endpoint in the left-moving state, it remains immobile until an exponentially distributed time with rate \(\rho+\eta\), then resumes motion to the right. First arrival at the right endpoint absorbs it immediately. The initial state is \(X_0=0\) with rightward velocity \(+v\), **not** a symmetric-direction or spatially averaged initial distribution, and there is no initial holding time.

Set \(a=\rho L/v\), \(g=\eta L/v\), and \(Y=vT/L\), where \(T\) is the first absorption time. The theorem concerns \(g>0\) and \(a>0\). The ballistic endpoint \(a=0\) has \(Y\equiv1\) and variance zero; it is included only by continuity at fixed positive \(g\). The left endpoint cannot itself absorb the particle. No thermal diffusion or additional resetting acts in the interior. The Poisson rate \(\rho\) is a **direction-reversal** rate (not a total attempted reorientation rate that might leave direction unchanged).

## Proof

**1. First-passage transform.** In the rescaled spatial coordinate \(x\in[0,1]\), let \(u_\pm(x,s)=\mathbb E_{x,\pm}\exp(-sY)\), with \(s\ge0\), denote the transforms from the two moving states. The interior backward equations are

\[
\frac{d}{dx}\begin{pmatrix}u_+\\u_-\end{pmatrix}
=\begin{pmatrix}s+a&-a\\a&-(s+a)\end{pmatrix}
\begin{pmatrix}u_+\\u_-\end{pmatrix}.
\]

A right-moving particle at \(x=1\) is immediately absorbed, hence \(u_+(1,s)=1\). From the left-moving state at \(x=0\), exponential holding followed by rightward release gives \(u_-(0,s)=(a+g)u_+(0,s)/(a+g+s)\). These are precisely the two incoming-state boundary conditions required by the first-order backward system. Its matrix squares to \(s(s+2a)I\). Writing \(z=\sqrt{s(s+2a)}\), the transform of the exit time from the prescribed initial state is therefore

\[
F(s)=\mathbb E e^{-sY}=\left[\cosh z+\frac{s(s+2a+g)}{s+a+g}\,\frac{\sinh z}{z}\right]^{-1},
\]

where the quotient \(\sinh z/z\) takes its entire-function value \(1\) at \(z=0\). These functions are analytic in \(s\) near zero. All moments used below are finite: from any state on the compact interval, there is a uniformly positive probability of right-boundary absorption within some bounded time, since \(g>0\) allows departure from the left wall and a no-reversal rightward traversal has positive probability (the case \(a=0\) is deterministic from the prescribed initial state). Repeated trials give an exponential tail.

**2. Moments.** Expand the square bracket as \(1+d_1s+d_2s^2+O(s^3)\). Differentiation at zero gives \(\mathbb E Y=d_1\) and \(\operatorname{Var}(Y)=d_1^2-2d_2\). Direct exact expansion yields the displayed mean and variance formulas. An independent derivation through backward equations for the first two moments is specified in the accompanying checker, and establishes the same expressions without using the displayed transform.

**3. Reduction to a strictly convex polynomial.** Exact differentiation and simplification give

\[
\partial_aV(a,g)=\frac{2Q(a,g)}{3(a+g)^3},\qquad
\partial_a\mathbb E Y=1+\frac{g}{(a+g)^2}.
\]

For all \(a\ge0\), \(g>0\),

\[
\partial_{aa}Q=24a^2+(36g+24)a+12g^2+24g>0,
\]

\[
\partial_gQ=6a^3+(12g+12)a^2+(6g^2+20g+6)a+6g^2+6g+3\ge3.
\]

Consequently \(Q(\cdot,g)\) is strictly convex on \([0,\infty)\), and, for fixed \(a\ge0\), \(Q(a,g)\) increases at least at rate \(3\) with \(g\). Also \(Q(0,g)=2g^3+3g^2+3g>0\), while \(Q(a,g)\to\infty\) as \(a\to\infty\).

**4. Unique threshold and exact stationary-point count.** Define \(h(g)=\min_{a\ge0}Q(a,g)\) for \(g\ge0\). Its minimum is attained, and \(h\) is continuous because the quartic is coercive uniformly in \(g\) over compact parameter intervals. For \(g_2>g_1\ge0\), the preceding derivative bound gives \(h(g_2)\ge h(g_1)+3(g_2-g_1)\), so \(h\) is strictly increasing. At \(g=0\), \(Q(a,0)=a(2a^3+4a^2-3)\), which is negative at \(a=1/4\); thus \(h(0)<0\). At \(g=1\), every coefficient of \(Q(a,1)\) is strictly positive, hence \(h(1)>0\). There exists exactly one \(g_c\in(0,1)\) such that \(h(g_c)=0\).

Since \(Q(0,g_c)>0\), the unique minimizing point \(a_c\) is positive; strict convexity forces \(\partial_aQ(a_c,g_c)=0\) and gives uniqueness of the positive double-root pair. If \(0<g<g_c\), the positive value at zero, negative minimum, and positive large-\(a\) limit force precisely two distinct positive roots. If \(g>g_c\), the polynomial is everywhere positive. At \(g=g_c\), strict convexity makes its unique zero a double zero. Applying the derivative identity establishes each monotonicity regime for \(V\). Although the derivative vanishes at one point for \(g=g_c\), it is positive elsewhere, so \(V\) is strictly increasing across the entire domain.

**5. Critical coalescence.** The derivatives \(\partial_{aa}Q(a_c,g_c)>0\) and \(\partial_gQ(a_c,g_c)>0\) guarantee a nondegenerate quadratic tangency. Taylor expansion of \(Q\) around \((a_c,g_c)\), followed by the implicit-function theorem with square-root parameter \(\sqrt{g_c-g}\), gives the stated two-root expansion and its positive constant \(C\). The decimal values are merely approximations to the unique exactly characterized solutions; no numerical root finding is used to prove their existence or uniqueness.

## Verification

Run `python verify.py` with Python 3 and SymPy. The standalone checker reconstructs the mean and variance in two algebraically independent ways: (i) differentiation of the Laplace-transform denominator at the origin, and (ii) first- and second-moment backward ODEs with the correct exponential waiting-time boundary moments. It also verifies the displayed derivative polynomial and its convexity/parameter derivatives symbolically, checks the opposite-sign regime witnesses exactly, and computes illustrative roots numerically. Numerical roots are corroboration, not an infinite-domain proof; the positivity, convexity, and uniqueness arguments above cover all admissible parameters.

## Relationship to prior work

The 2014 run-and-tumble literature supplies the active-persistence setting. Angelani, Di Leonardo and Paoluzzi (2014; author-provided arXiv copy 2015) derive the **mean** first-passage time for directed injection and nonsticky reflection; their full equations include the absorbing-right/reflecting-left geometry but not the present wall-release fluctuation phase. Angelani (2023) develops **generic boundary** rules, gives the general Laplace exit-time distribution, and specializes calculated results to mean exit times; that more general forward formulation implicitly determines higher moments, so neither the boundary transform principle nor the general ability to compute moments is claimed as new. Angelani (2024) considers the same kind of enhanced wall-release rate and proves a sharp **mean-optimal tumbling threshold** for centrally injected and initially orientation-averaged walkers. By contrast, here injection is rightward directly at the left wall, the mean is strictly monotone, and the theorem concerns the number and coalescence of **variance** extrema. Mercado-Vásquez and Boyer (2021) obtain nonmonotonic relative first-hitting fluctuations for a stochastically switching **target** with reflective outer boundaries; their state space, boundary mechanism, normalization and optimization parameters differ. The contribution asserted here is only the sharp, parameter-complete two-extrema variance theorem and square-root merger for the specified entrance-wall injection problem.

## Limitations

The stationary-point criterion applies to variance of the dimensionaless exit time, not to the coefficient of variation, higher moments, or distributions from other initial states; changing the observable or initial condition can change its phase diagram. The boundary release rate is constrained to equal the bulk reversal rate plus a fixed positive excess, and the theorem neither covers negative excess nor a left-wall absorption channel. Because the generic-boundary first-passage transform was already available in prior literature, priority is limited to the new sharp global optimization/classification rather than the underlying forward-law machinery. Broad bibliographic coverage cannot exclude implicit earlier derivations in specialized work or unpublished calculations. No independent external scientific audit has occurred.

## References

1. M. Paoluzzi, R. Di Leonardo and L. Angelani, “Run-and-tumble particles in speckle fields,” 2014, arXiv:1401.6944, original public submission 27 January 2014, https://arxiv.org/abs/1401.6944.
2. L. Angelani, R. Di Leonardo and M. Paoluzzi, “First-passage time of run-and-tumble particles,” *European Physical Journal E* **37** (2014) 59, DOI:10.1140/epje/i2014-14059-4; accessible author copy arXiv:1506.08046, https://arxiv.org/pdf/1506.08046.
3. L. Angelani, “One-dimensional run-and-tumble motions with generic boundary conditions,” *Journal of Physics A* **56** (2023) 455003, DOI:10.1088/1751-8121/ad009e, https://iris.cnr.it/retrieve/e1d78abe-8685-4eff-936b-9bcad8ad4c0f/prod_489129-doc_203607.pdf.
4. L. Angelani, “Optimal escapes in active matter,” *European Physical Journal E* **47** (2024) 9, DOI:10.1140/epje/s10189-023-00402-7, https://link.springer.com/article/10.1140/epje/s10189-023-00402-7.
5. G. Mercado-Vásquez and D. Boyer, “First hitting times between a run-and-tumble particle and a stochastically-gated target,” arXiv:2102.11787 (2021), https://arxiv.org/pdf/2102.11787.
