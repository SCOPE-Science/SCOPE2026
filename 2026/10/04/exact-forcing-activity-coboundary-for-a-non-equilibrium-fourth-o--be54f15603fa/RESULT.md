# Exact forcing–activity coboundary for a non-equilibrium fourth-order flow
## Finding
Consider the autonomous flow
\[
\dot x=y,\qquad \dot y=z,\qquad \dot z=w,\qquad
\dot w=-aw+bx^2-cy^2+exy+fxz+g,
\]
with real parameters \(a,b,c,e,f,g\). Define
\[
\Phi(x,y,z,w)=w+az-\frac e2x^2-fxy.
\]
Along every classical trajectory,
\[
\frac{d}{dt}\Phi=b x^2-(c+f)y^2+g. 
\]
Consequently, every bounded forward trajectory satisfies
\[
 b\,\frac1T\int_0^T x(t)^2\,dt-(c+f)\,\frac1T\int_0^T y(t)^2\,dt+g\longrightarrow0. 
\]
Every compactly supported invariant probability measure \(\mu\) satisfies the exact stationary law
\[
 b\int x^2\,d\mu-(c+f)\int y^2\,d\mu+g=0. 
\]
Two direct consequences are structural. If \(b\ge0\), \(c+f\le0\), and \(g>0\), then no bounded forward trajectory exists. If \(b\ge0\), \(c+f>0\), and \(g>0\), then every bounded forward trajectory obeys
\[
\liminf_{T\to\infty}\frac1T\int_0^T y(t)^2\,dt\ge\frac{g}{c+f}. 
\]
For the published chaotic parameter values \(b=0.7\), \(c=0.19\), \(f=1.79\), and \(g=1.15\), interpreted as the exact displayed decimals, (3) becomes
\[
\int y^2\,d\mu=\frac{35}{99}\int x^2\,d\mu+\frac{115}{198},
\]
so every compact invariant measure has \(\int y^2\,d\mu\ge115/198\). Equivalently, any convergent long-time root-mean-square value of \(y\) is at least \(\sqrt{115/198}\approx0.762107656967\).

## Assumptions and scope
The differential equation is the four-dimensional system printed in Jahanshahi et al. (2019). The coboundary identity (1) is algebraic and needs only a classical solution. Statement (2) assumes that \(x,y,z,w\) remain bounded for all forward time. Statement (3) assumes a compactly supported invariant probability measure of this flow; compact support makes all polynomial observables used here integrable. No ergodicity assumption is needed. The sign obstruction uses \(g>0\) exactly as stated. The numerical specialization uses the displayed decimal parameter values as exact rational numbers.

## Proof
Differentiate \(\Phi\) along the vector field:
\[
\begin{aligned}
\dot\Phi
&=\dot w+a\dot z-e x\dot x-f(\dot x\,y+x\dot y)\\
&=(-aw+bx^2-cy^2+exy+fxz+g)+aw-exy-f(y^2+xz)\\
&=b x^2-(c+f)y^2+g.
\end{aligned}
\]
This proves (1). Integrating from \(0\) to \(T\) gives
\[
\frac{\Phi(T)-\Phi(0)}{T}
=b\frac1T\int_0^T x(t)^2\,dt-(c+f)\frac1T\int_0^T y(t)^2\,dt+g.
\]
If the trajectory is bounded, then \(\Phi\) is bounded, so the left side tends to zero; this proves (2).

For an invariant probability measure \(\mu\), integrate the time-integrated form of (1) over initial conditions. Invariance makes \(\int \Phi\circ\varphi_T\,d\mu=\int\Phi\,d\mu\), while Fubini and invariance make the time average of the right-hand side equal its \(\mu\)-integral. Thus (3) follows.

If \(b\ge0\), \(c+f\le0\), and \(g>0\), then (1) yields \(\dot\Phi\ge g\). Hence \(\Phi(t)\ge\Phi(0)+gt\), contradicting boundedness of a bounded state trajectory. This proves the no-bounded-trajectory statement. If instead \(b\ge0\), \(c+f>0\), and \(g>0\), rearranging (2) and using nonnegativity of the mean of \(x^2\) proves (4).

At the displayed chaotic parameters, \(b=7/10\), \(c+f=99/50\), and \(g=23/20\). Solving (3) for \(\int y^2d\mu\) gives the stated coefficients \(35/99\) and \(115/198\).

## Verification
The accompanying `verify.py` performs an exact formal polynomial check of the Lie-derivative identity with independent indeterminates for the four state variables and six parameters, and checks the displayed rational specialization. Running it from the packaged path prints `VERIFY_OK`. The proof itself is symbolic and does not rely on numerical trajectory integration, finite enumeration, or a Lyapunov-exponent computation.

## Relationship to prior work
Jahanshahi et al. introduce the same flow, classify its equilibria, and numerically study bifurcation diagrams, Lyapunov exponents, entropy, and control. Their Section 2 supplies the vector field and the parameter set used above, but does not state the coboundary (1), the stationary law (3), or the sign obstruction. Ren et al. study a different no-equilibrium four-dimensional hyperjerk with a different fourth equation and focus on equilibria, bifurcations, Lyapunov exponents, fractional-order variants, delay, and circuit realization. Semantic literature searches for this system together with time-average, mean-square, invariant-measure, balance-law, and coboundary terminology did not locate a statement implying (1)–(4). Related exact balance-law results for other flows do not imply this system-specific identity.

## Limitations
The result constrains bounded recurrent dynamics but does not prove existence of an attractor, chaos, ergodicity, uniqueness of an invariant measure, or convergence of individual time averages. The lower bound (4) is a one-sided constraint and does not determine the full invariant statistics. The originality check cannot exclude an unindexed or differently phrased prior derivation; this remains a residual literature risk.

## References
1. H. Jahanshahi, M. Shahriari-Kahkeshi, R. Alcaraz, X. Wang, V. P. Singh, V.-T. Pham, “Entropy Analysis and Neural Network-Based Adaptive Control of a Non-Equilibrium Four-Dimensional Chaotic System with Hidden Attractors,” *Entropy* 21 (2019), 156. DOI: 10.3390/e21020156. Published 2019-02-07.
2. S. Ren, S. Panahi, K. Rajagopal, A. Akgul, V.-T. Pham, S. Jafari, “A New Chaotic Flow with Hidden Attractor: The First Hyperjerk System with No Equilibrium,” *Zeitschrift für Naturforschung A* 73 (2018), 239–249. DOI: 10.1515/zna-2017-0409.
3. C. Wang et al., “Synchronization of a Non-Equilibrium Four-Dimensional Chaotic System Using a Disturbance-Observer-Based Adaptive Terminal Sliding Mode Control Method,” *Entropy* 22 (2020), 271. DOI: 10.3390/e22030271.
