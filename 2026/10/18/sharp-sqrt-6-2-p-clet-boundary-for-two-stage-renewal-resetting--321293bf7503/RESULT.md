# Sharp \(\sqrt{6}/2\) Péclet boundary for two-stage renewal resetting

## Finding
Let a Brownian searcher drift toward an absorbing target at zero and be restored to its starting position after i.i.d. two-stage Erlang waiting times. The sharp dimensionless drift threshold separating a unique advantageous nonzero restart rate from globally detrimental restarting is \(d_c=\sqrt6\), or \(Pe_c=\sqrt6/2\) in the conventional Péclet normalization.

For all \(v,D,L,\rho>0\), set
\[
 d=\frac{vL}{D},\qquad q=\frac{\rho L^2}{D},\qquad u=\frac{\sqrt{d^2+4q}-d}{2}>0,\qquad q=u(u+d).
\]
The exact dimensionless mean absorption time is
\[
 m_d(q):=\frac{D}{L^2}\mathbb E[T_\rho]
 =\frac{2(2u+d)(e^u-1)-u(u+d)}{u(u+d)[2u+d+u(u+d)]}.
\]

**Complete rate classification.** For each fixed \(0<d<\sqrt6\), this function decreases strictly on \((0,q_*(d))\) and increases strictly on \((q_*(d),\infty)\), where \(q_*(d)>0\) is unique, and \(m_d(q_*(d))<1/d\). For each \(d\ge\sqrt6\), it increases strictly throughout \((0,\infty)\), so positive-rate restarting cannot improve the no-reset mean \(1/d\). For \(d\uparrow\sqrt6\), the positive optimizer has the sharp boundary law
\[
 q_*(d)\sim\frac{16\sqrt6}{3(8-\sqrt6)}(\sqrt6-d).
\]
Here \(q\) uses the rate of **each** of the two exponential stages; the mean waiting time between resets is \(2/\rho\), not \(1/\rho\).

## Assumptions and scope
On the positive half-line consider \(dX_t=-v\,dt+\sqrt{2D}\,dW_t\), started at \(X_0=L>0\) and killed when first reaching zero. Both \(v\) and \(D\) are strictly positive. Independently of the particle path, each attempt has a restart clock distributed as the sum of two independent exponential waiting times with identical stage rate \(\rho>0\). When its clock rings before absorption, the process is reset instantaneously to \(L\), with fresh Brownian increments and a fresh, independent two-stage clock. Absorption terminates all attempts. Zero-reset statements mean the limit \(\rho\downarrow0\); they do not posit a finite two-stage clock of rate zero. The result is about expected absorption time, not higher moments, optimization over arbitrary clock distributions, or negative target-directed drift.

Write dimensionless time as \(s=Dt/L^2\). The dimensionless unreset hitting time \(H\) has Laplace transform \(\phi(q)=\mathbb E[e^{-qH}]=e^{-u}\), with \(u=(\sqrt{d^2+4q}-d)/2\). In particular \(\mathbb E[H]=1/d\).

## Proof
**Step 1: renewal reduction and exact formula.** A two-stage Erlang clock \(R\) with stage rate \(q\) has survival probability \(\Pr(R>s)=e^{-qs}(1+qs)\). Each fresh attempt either ends at \(H<R\) or starts a new independent copy after \(R\). The renewal identity gives
\[
 m_d(q)=\frac{\mathbb E[\min(H,R)]}{\Pr(H<R)}.
\]
Since \(\phi'(q)=-\mathbb E[He^{-qH}]\), the denominator is \(\phi(q)-q\phi'(q)\). Integration of the survival function gives the numerator \(2[1-\phi(q)]/q+\phi'(q)\). Using \(\phi=e^{-u}\), \(du/dq=1/(2u+d)\), and \(q=u(u+d)\) yields
\[
 m_d(q)=\frac{2(2u+d)(e^u-1)-q}{q(2u+d+q)}.
\]
The denominator is positive. As \(u\downarrow0\), this expression tends to \(1/d\); as \(u\to\infty\), it diverges to infinity.

**Step 2: one sign change in all exponential-series coefficients.** Define
\[
 A(u,d)=2(2u+d)(e^u-1)-u(u+d),\quad
 B(u,d)=u(u+d)[2u+d+u(u+d)],\quad
 N=A_uB-AB_u.
\]
Because \(B>0\), the derivative \(\partial_u m_d=N/B^2\) has the sign of \(N\). Expansion at \(u=0\) has the **exact entire** series \(N(u,d)=\sum_{n=3}^{\infty}c_n(d)u^n\). Its first four potentially negative coefficients are
\[
\begin{aligned}
 c_3&=\frac{2d(d^2-6)}3,\\
 c_4&=\frac{7d^3+36d^2-60d-72}{12},\\
 c_5&=\frac{7d^3+75d^2+60d-180}{30},\\
 c_6&=\frac{23d^3+354d^2+960d-240}{360}.
\end{aligned}
\]
For every integer \(n\ge7\), set \(j=n-7\ge0\). Direct multiplication of \(N\)'s exponential and polynomial factors gives the coefficient identity
\[
\begin{aligned}
 n!c_n={}&4(17d^3+336d^2+1428d+840)\\
 &+2(12d^3+383d^2+2606d+3376)j\\
 &+2(d^3+69d^2+811d+1848)j^2\\
 &+4(2d^2+53d+219)j^3+2(5d+48)j^4+4j^5.
\end{aligned}
\]
Every term on this right-hand side is nonnegative, and the constant term is strictly positive, for \(d>0\) and \(j\ge0\). Thus \(c_n(d)>0\) for **every** \(n\ge7\), with no finite-enumeration assumption.

Each of the cubic numerators of \(c_6,c_5,c_4\) has exactly one positive zero by Descartes' rule of signs. Their respective roots belong to the disjoint ordered rational intervals \((0,1/4)\), \((1,6/5)\), and \((19/10,2)\); direct endpoint substitution verifies both signs. The positive root of \(c_3\) is \(\sqrt6>2\). Consequently, for every fixed \(d>0\), the ordered coefficient sequence \(c_3,c_4,c_5,\ldots\) changes sign **at most once, from negative to positive**. For \(0<d<\sqrt6\), there is precisely one such change because \(c_3<0\) and all \(c_n\) with \(n\ge7\) are positive. For \(d\ge\sqrt6\), every coefficient is nonnegative and at least one is positive.

**Step 3: global root uniqueness.** In the first regime let \(k\in\{3,4,5,6\}\) denote the last index with negative coefficient. Then
\[
 \frac{N(u,d)}{u^k}
 =\sum_{n=3}^{k}c_n(d)u^{n-k}
 +\sum_{n=k+1}^{\infty}c_n(d)u^{n-k}.
\]
All terms in the first sum are nonpositive and nondecreasing in \(u>0\), while all terms in the second are nonnegative and strictly increasing (and infinitely many are strictly positive). Hence the quotient is strictly increasing on \((0,\infty)\). It tends to a negative value or negative infinity at the left endpoint, and to positive infinity at the right endpoint. It has exactly one positive zero. Thus \(N\) changes sign once, from negative to positive, proving the unique global minimum. In the second regime, \(N(u,d)>0\) for every \(u>0\), proving strict monotonicity and the sharp equality case \(d=\sqrt6\).

**Step 4: critical linear scaling.** Expanding the exact quotient, uniformly for \(d\) near \(d_c=\sqrt6\), gives
\[
 m_d(u)=\frac1d+\frac{d^2-6}{3d^3}u^2
 +\frac{8-\sqrt6}{2(\sqrt6)^4}u^3
 +O(|d-\sqrt6|u^3+u^4).
\]
The positive stationary point \(u_*(d)\) approaches zero when \(d\uparrow\sqrt6\): otherwise continuity and positivity of \(N\) at the critical parameter contradict its defining equation (and its high-\(u\) exponential dominance precludes escape to infinity). Balancing the first two nonzero terms of the derivative yields
\[
 u_*(d)\sim\frac{16}{3(8-\sqrt6)}(\sqrt6-d).
\]
Finally \(q_*(d)=u_*(d)[u_*(d)+d]\), giving the asserted coefficient \(16\sqrt6/[3(8-\sqrt6)]\).

## Verification
The standalone script `verify.py` evaluates the identities and checks the all-index coefficient decomposition symbolically using SymPy. It checks cubic-root brackets with exact rational arithmetic, the critical expansion, and the exact mean formula against independent integration of the inverse-Gaussian first-passage density and survival function. An additional numerical root check supports the optimizer behavior for representative drifts. Execute `python verify.py` with Python, SymPy, SciPy and mpmath. The executable checks are supplemental: the infinite root count and the threshold follow from the coefficient sign proof above, not numerical sampling.

## Relationship to prior work
Ray, Mondal and Reuveni (arXiv:1811.08239, originally posted in 2018) establish the sharp \(Pe=1\) transition and unique Poisson-rate optimization for the same drift-diffusion first-passage geometry. Their waiting times are exponential, whereas every restart interval here is explicitly the **sum of two independent exponentials**. The new threshold differs for that reason.

Pal and Reuveni (arXiv:1607.06048, originally posted in 2016) derive the general mean-first-passage renewal formula used in Step 1, including nonexponential restart. That general reduction does not itself provide the particular Erlang-two global sign and minimizer classification proved in Steps 2–4.

Linn and Lawley (arXiv:2302.05409, first posted February 10, 2023) explicitly consider gamma-two restart clocks, principally for frequent-restart limits of **driftless** diffusion and other search mechanisms. Their limiting distribution and moment results do not imply the finite-rate optimizer for positive drift or the all-rate critical curve here.

The motivation is the simplest nonmemoryless renewal clock admitting a finite-state Markov representation. The difference between \(Pe=1\) and \(Pe=\sqrt6/2\) quantifies how clock shape modifies the boundary between beneficial and detrimental restart.

## Limitations
The result assumes positive drift toward the target, homogeneous diffusion, an absorbing point target, instantaneous restoration to exactly the initial point, i.i.d. Erlang-two waiting times with **two equal stage rates**, full clock renewal, and no time cost for reset. No claim is made for general gamma shape, deterministic restarts, other geometries, drift away from the target, higher first-passage moments, or noisy rate estimation. The theorem specializes established renewal machinery; equivalently derived formulas outside the primary sources examined remain a priority risk, and independent scholarly priority assessment has not been performed.

## References
1. S. Ray, D. Mondal, and S. Reuveni, *Péclet number governs transition to acceleratory restart in drift-diffusion*, arXiv:1811.08239 (first public version November 20, 2018), https://arxiv.org/html/1811.08239v4.
2. S. Linn and S. D. Lawley, *First passage times under frequent stochastic resetting*, arXiv:2302.05409 (first public version February 10, 2023), https://arxiv.org/abs/2302.05409.
3. A. Pal and S. Reuveni, *First Passage Under Restart*, arXiv:1607.06048 (first public version July 20, 2016), https://arxiv.org/abs/1607.06048.
