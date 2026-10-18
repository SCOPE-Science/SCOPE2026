# Two mobility conventions give sharply different capture slowdowns on stars

## Finding

Let \(K_{1,m}\) be the star with center \(o\) and \(m\ge2\) leaves. Two independent continuous-time walkers \(X,Y\) start, respectively, at one specified leaf and at \(o\). They are absorbed at their first encounter \(\tau=\inf\{t\ge0:X_t=Y_t\}\). The searcher \(X\) has mobility \(a>0\), the mobile trap \(Y\) has mobility \(b\ge0\). Consider two precisely distinguished rate conventions:

* **Edge-clock:** from every vertex, \(X\) jumps across each incident edge at rate \(a\), and \(Y\) at rate \(b\).
* **Vertex-clock:** the *total* departure rates of \(X\) and \(Y\) are \(a\) and \(b\) at every vertex, with a uniformly chosen neighbor.

Put \(x=b/a\) and \(D_m(x)=(1+x)(1+2mx+x^2)\). Their exact mean encounter times are
\[
 a\mathbb E\tau_{\mathrm E}
 =F_{\mathrm E,m}(x)
 =\frac{1+m(m+1)x+mx^2}{D_m(x)},\qquad
 a\mathbb E\tau_{\mathrm V}
 =F_{\mathrm V,m}(x)
 =\frac{1+(4m-2)x+(2m-1)x^2}{D_m(x)}.
\]
For the immobile trap \(b=0\), both means equal \(1/a\). Define
\[
 \xi_{\mathrm E}(m)=\frac{\sqrt{5m^2-2m-3}-(m+1)}2,
 \qquad \xi_{\mathrm V}(m)=\sqrt{2m-2}-1.
\]
Both thresholds are strictly positive. The mobile trap makes the expected capture time **strictly longer than the static hub trap** precisely in the following ranges:
\[
 \mathbb E\tau_{\mathrm E}>1/a\iff0<x<\xi_{\mathrm E}(m),
 \qquad
 \mathbb E\tau_{\mathrm V}>1/a\iff0<x<\xi_{\mathrm V}(m).
\]
There is equality at the respective positive threshold, and capture is faster when \(x\) is above it. Each mean as a function of \(x\ge0\) has **exactly one** global maximum, attained at a strictly positive finite value of \(x\). For the same \(a,b,m\), the two mobility conventions have the further exact comparison
\[
 a(\mathbb E\tau_{\mathrm E}-\mathbb E\tau_{\mathrm V})
 =\frac{(m-1)x(m-2-x)}{D_m(x)}.
\]
Thus for \(m>2\), the slower convention switches exactly at \(x=m-2\) (for \(x>0\)); for \(m=2\), edge-clock capture is always faster than vertex-clock capture at \(x>0\).

The **maximal delay factor** over mobile-trap rates has different sharp large-degree scaling:
\[
 \lim_{m\to\infty}\frac1m\max_{x\ge0}F_{\mathrm E,m}(x)=\frac12,
 \qquad
 \lim_{m\to\infty}\max_{x\ge0}F_{\mathrm V,m}(x)=2.
\]
The corresponding positive crossover rates scale as
\[
 \lim_{m\to\infty}\frac{\xi_{\mathrm E}(m)}m=\frac{\sqrt5-1}{2},
 \qquad
 \lim_{m\to\infty}\frac{\xi_{\mathrm V}(m)}{\sqrt m}=\sqrt2.
\]
Consequently, fixing the leaf's departure rate while enlarging the star produces unbounded optimally induced capture delay for edge-clock mobility, but a universal limiting ceiling of twice the static capture time for vertex-clock mobility.

## Assumptions and scope

The graph is the finite, simple, undirected star with \(m\ge2\) leaves, and the two walkers are labeled and independent until their first common vertex. Jumps have exponential holding times, no simultaneous jumps, and immediate absorption at contact. The initial locations are fixed at one leaf for \(X\) and at the center for \(Y\), not sampled from stationarity. The rates \(a>0\), \(b\ge0\) and the two graph-normalizations are as defined above. At \(b=0\), the trap never moves and a searcher started at a leaf hits the hub at its first jump, with mean \(1/a\). The result does not identify searcher and trap mobility with diffusivity under a spatial continuum limit.

## Proof

By permutation symmetry of leaves, before absorption there are three orbit types: \(A\), with \(X\) at a leaf and \(Y\) at the hub; \(B\), with their positions reversed; and \(C\), with both at *distinct* leaves. Write their conditional mean residual times as \(A,B,C\), respectively. Let \(q=1\) for edge-clock mobility and \(q=1/m\) for vertex-clock mobility; at the hub, the rate per incident edge is \(aq\) for \(X\) and \(bq\) for \(Y\), while at a leaf it is \(a\) or \(b\). The first-jump equations are exactly
\[
 \begin{aligned}
 (a+mbq)A&=1+(m-1)bqC,\\
 (b+maq)B&=1+(m-1)aqC,\\
 (a+b)C&=1+aB+bA.
 \end{aligned}
\]
The omitted transition rates in the first two equations are precisely jumps landing on the other walker and hence absorbing. In the third equation, either walker's jump from its leaf reaches the hub, producing the opposite orbit type. Since the finite product chain reaches the diagonal almost surely, this Dirichlet first-step system has a unique finite solution. Indeed, with \(a>0\), from each off-diagonal pair the searching walker can follow any fixed path to the trap's current vertex while the trap makes no jump; this has strictly positive probability within bounded time, uniformly over finitely many states. Repetition gives geometric-tail absorption.

Substitute \(C=(1+aB+bA)/(a+b)\) and solve the remaining two linear equations. With \(x=b/a\), choosing \(q=1\) gives \(aA=F_{\mathrm E,m}(x)\), and choosing \(q=1/m\) gives \(aA=F_{\mathrm V,m}(x)\), as displayed in the Finding. This derivation remains valid at \(b=0\).

Subtracting the static benchmark \(1\) gives
\[
 F_{\mathrm E,m}(x)-1=
 \frac{x[(m^2-m-1)-(m+1)x-x^2]}{D_m(x)},\qquad
 F_{\mathrm V,m}(x)-1=
 \frac{x[(2m-3)-2x-x^2]}{D_m(x)}.
\]
Since both numerator brackets decrease strictly from positive values at \(x=0\), their unique positive roots are \(\xi_{\mathrm E}(m)\) and \(\xi_{\mathrm V}(m)\). Since \(D_m(x)>0\) for \(x\ge0\), this proves all strict comparison ranges and boundary equalities.

Differentiating \(F_{\mathrm E,m}\) and \(F_{\mathrm V,m}\) produces positive denominators \(D_m(x)^2\) and the respective numerator polynomials
\[
 \begin{aligned}
 P_{\mathrm E,m}(x)&=(m^2-m-1)-2(m+1)x-(2m^3+m^2+3)x^2
 -2m(m+1)x^3-mx^4,\\
 P_{\mathrm V,m}(x)&=(2m-3)-4x-(4m^2+2)x^2
 -(8m-4)x^3-(2m-1)x^4.
 \end{aligned}
\]
For every \(m\ge2\), each polynomial starts strictly positive at \(0\), is strictly decreasing for positive arguments, and tends to minus infinity. Each therefore has exactly one positive root. The respective mean initially increases and ultimately decreases to zero, so that root is the unique global maximum.

Taking the difference of the two rational forms directly gives the displayed clock-normalization comparison. To establish the limiting maximal delays without assuming the location of the maximum, note the uniform upper bounds
\[
 F_{\mathrm E,m}(x)<\frac{m+1}{2},\qquad F_{\mathrm V,m}(x)<2,
 \qquad (m\ge2,\ x\ge0).
\]
The first follows from the strictly positive polynomial identity
\[
 (m+1)D_m(x)-2[1+m(m+1)x+mx^2]
 =(m-1)+(m+1)x+(2m^2+m+1)x^2+(m+1)x^3>0.
\]
The second follows from
\[
 2D_m(x)-[1+(4m-2)x+(2m-1)x^2]
 =1+4x+(2m+3)x^2+2x^3>0.
\]
Choosing \(x=m^{-1/2}\) gives \(F_{\mathrm E,m}(x)/m\to1/2\) and \(F_{\mathrm V,m}(x)\to2\), matching these upper bounds and proving both maxima limits. Finally, taking leading terms in the two explicit positive roots proves the displayed threshold scalings.

## Verification

Run `python verify_star.py` with Python 3 and no third-party libraries. The verifier independently constructs the full labeled two-walker generator on every off-diagonal vertex pair, solves the exact rational absorbing Poisson system, and compares its result at the specified leaf–hub start with both formulas. It also checks every underlying full-generator first-step balance equation. The direct labeled generator contains \(m(m+1)\) off-diagonal states, not only the three symmetry classes used in the proof. In the delivered version, its 40 exact formula comparisons and 880 individual exact first-step checks passed, for \(2\le m\le6\), four rational mobility choices (including a static trap), and both rate conventions. Symbolic polynomial identities and sign arguments above, not the finite test range, prove the result for every integer \(m\ge2\) and real \(a>0,b\ge0\).

## Relationship to prior work

Tzou, Xie and Kolokolnikov (2014, arXiv:1410.1391, particularly their Section 3) analyze a mobile trap and a Brownian walker on a reflecting continuum interval and identify mobility thresholds. Hence **the general phenomenon that slow trap motion can impair capture is established prior work**. Their continuum-domain PDE does not supply the present finite-star formulas or the divergence-versus-ceiling classification under different degree normalizations.

Campari and Cassi (2012, DOI:10.1103/PhysRevE.86.021110) rigorously investigate two-particle recurrence and finite-collision properties of infinite branched networks; the complete four-page paper was inspected, including its finite-comb simulations and discussion of the Pascal principle. It does not solve the fixed-start finite-star continuous-time rate problem or compare edge and vertex clocks. Agliari, Blumen and Cassi (2014, arXiv:1405.5554) study first-encounter-time distributions and unexpectedly slow two-particle encounters on finite combs, mainly numerically, compared with a single immobile target. This is closely related motivation, but not the present star formulas or rate-normalization dichotomy. Agliari, Cassi, Cattivelli and Sartori (2016, arXiv:1604.05874) analytically treat unequal diffusivity and finite combs; the inspected Sections III B–D concern comb/bundled asymptotics rather than the exact finite-star degree-dependent classification here. These papers establish that moving-particle capture can behave anomalously on branched graphs; that general phenomenon is not claimed as new. Zhang, Tan and Krishnamachari (2014, arXiv:1408.2005) study two-walker meeting times on regular graphs with an averaged initial condition, rather than the nonregular star with a fixed hub–leaf start. Komarov and Winkler (2013, arXiv:1305.4559) study a *strategically controlled* cop and a random robber, not two independent mobile agents. Duan and collaborators (2019, arXiv:1912.02693) give general product-chain formulas for discrete-time meeting times, an important computational framework but not the evaluated continuous-time star threshold or sharp degree-dependent contrast here.

The first-step linear system is elementary Markov-chain machinery; the contribution claimed here is **its complete sharp two-normalization comparison and asymptotic classification for the natural nonregular star**, not the use of the first-step method itself.

## Limitations

Only stars with the specified fixed initial leaf–hub pair and independent exponential random walks are covered. The contrast depends on keeping the *leaf* departure rate fixed; it should not be extrapolated to arbitrary graph families, random starting locations, active pursuit policies, nonexponential waiting times, or spatially continuous diffusion. The mean is not a complete description of the meeting-time distribution. Although a class of adjacent generic stochastic formulations is known, exhaustive absence of prior equivalent explicit formulas has not been established. Independent validation has not been performed.

## References

1. J. C. Tzou, S. Xie and T. Kolokolnikov, *Drunken robber, tipsy cop: First passage times, mobile traps, and Hopf bifurcations*, arXiv:1410.1391 (first posted 2014-10-03), https://arxiv.org/abs/1410.1391.
2. E. Agliari, A. Blumen and D. Cassi, *Slow Encounters of Particle Pairs in Branched Structures*, arXiv:1405.5554 (first posted 2014-05-21), https://arxiv.org/abs/1405.5554.
3. R. Campari and D. Cassi, *Random collisions on branched networks: How simultaneous diffusion prevents encounters in inhomogeneous structures*, Physical Review E 86, 021110 (published 2012-08-10), https://doi.org/10.1103/PhysRevE.86.021110.
4. E. Agliari, D. Cassi, L. Cattivelli and F. Sartori, *The two-particle problem in comb-like structures*, arXiv:1604.05874 (first posted 2016-04-20), https://arxiv.org/abs/1604.05874.
5. Y. Zhang, Z. Tan and B. Krishnamachari, *On the Meeting Time for Two Random Walks on a Regular Graph*, arXiv:1408.2005 (first posted 2014-08-09), https://arxiv.org/abs/1408.2005.
6. N. Komarov and P. Winkler, *Capturing the Drunk Robber on a Graph*, arXiv:1305.4559 (first posted 2013-05-20), https://arxiv.org/abs/1305.4559.
7. X. Duan, M. George, R. Patel and F. Bullo, *Robotic Surveillance Based on the Meeting Time of Random Walks*, arXiv:1912.02693 (first posted 2019-12-04), https://arxiv.org/abs/1912.02693.
