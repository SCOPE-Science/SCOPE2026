# Universal mass threshold for weighted variation under nonlinear heat on stars

## Finding

Let a finite star have center \(v_0\) and \(d\ge1\) leaves \(v_1,\ldots,v_d\). Assign positive vertex masses \(m_0,m_1,\ldots,m_d\), positive edge conductances \(c_1,\ldots,c_d\), and independently chosen positive edge-variation weights \(w_1,\ldots,w_d\). Fix any exponent \(1<p<\infty\). Consider the mass-weighted graph \(p\)-heat evolution
\[
 m_i\dot u_i=c_i\,|u_0-u_i|^{p-2}(u_0-u_i)\quad(1\le i\le d),\qquad
 m_0\dot u_0=\sum_{i=1}^d c_i\,|u_i-u_0|^{p-2}(u_i-u_0),
\]
where \(|z|^{p-2}z\) is defined to be zero at \(z=0\). Define \(J_w(u)=\sum_{i=1}^d w_i|u_i-u_0|\) and \(W=\sum_i w_i\).

**Exact sharp infinitesimal growth law.** If \(u(t)\) is the solution from a nonconstant initial signal, then
\[
 \sup_{u(0)\ \mathrm{nonconstant}}
 \frac{\left.\dfrac{d^+}{dt}J_w(u(t))\right|_{t=0}}
 {\displaystyle\sum_{i=1}^d c_i|u_i(0)-u_0(0)|^{p-1}}
 =\boxed{\max_{1\le i\le d}\left(\frac{W-2w_i}{m_0}-\frac{w_i}{m_i}\right)}.
\]
Each candidate in the maximum is attained by an initial signal whose only nonzero leaf-to-center difference is on its corresponding edge.

**All-time classification.** Variation is nonincreasing for every real initial signal and all times \(t\ge0\) if and only if
\[
 \boxed{\quad w_i\left(2+\frac{m_0}{m_i}\right)\ge W\quad\text{for every }1\le i\le d.\quad}
\]
Consequently, *some* strictly positive edge-variation weights make the nonlinear heat flow variation-nonincreasing if and only if
\[
 \boxed{\quad\sum_{i=1}^d\frac{1}{2+m_0/m_i}\le1.\quad}
\]
At equality, the admissible weights are unique up to common scaling and satisfy \(w_i/W=(2+m_0/m_i)^{-1}\). All three results hold for **every** \(p>1\) and **every** positive conductance assignment; neither the criterion nor the optimum coefficient depends on the exponent, and the contraction criteria do not depend on the conductances.

For \(d\) equal-mass leaves, each with mass \(m\), the existence threshold is \(m_0\ge(d-2)m\) (automatic for \(d\le2\)). In particular a six-leaf star admits nonexpansive variation gauges at central mass \(4m\) and strictly dissipative ones at central mass \(5m\), although no such gauge exists at central mass \(3m\).

## Assumptions and scope

The graph is exactly a finite simple star; \(m_0,m_i,c_i,w_i\) are strictly positive real numbers; \(p\) ranges over \((1,\infty)\). The vertex evolution uses mass-weighted divergence and edge flux \(c_i|u_i-u_0|^{p-2}(u_i-u_0)\). The edge-variation weights \(w_i\) are distinct data, not implicitly identified with the conductances. Nonexpansivity refers to variation of one solution relative to its own starting variation, not to a two-input Lipschitz estimate.

Solutions exist globally and are unique. Indeed the vector field is continuous and preserves the initial minimum and maximum; its negative is monotone in the mass-weighted Euclidean inner product, which gives uniqueness even for \(1<p<2\) when the vector field need not be locally Lipschitz at coincident vertex values. Consequently the initial-value solution is continuously differentiable in time.

## Proof

Put \(g_i=u_i-u_0\), \(\phi_p(s)=|s|^{p-2}s\), and \(S=\sum_j c_j\phi_p(g_j)\). Subtract the center equation from the leaf equations to obtain the complete edge-coordinate evolution
\[
 \dot g_i=-\frac{c_i}{m_i}\phi_p(g_i)-\frac{S}{m_0}.
\]
Because the underlying graph is a star, every vector \(g\in\mathbb R^d\) is realized by a vertex potential, so the following extremal calculation has no unmentioned cycle constraint.

For a fixed \(g\), let \(\mathcal S(g)\) consist of all vectors \(s\in[-1,1]^d\) satisfying \(s_i=\operatorname{sgn}(g_i)\) whenever \(g_i\ne0\). The directional derivative of the convex weighted absolute-value norm is its maximal subgradient pairing. Thus the upper right derivative exists and equals
\[
 D^+J_w(g)=\max_{s\in\mathcal S(g)}\sum_{j:g_j\ne0}c_j|g_j|^{p-1}
 \left[-\frac{w_j}{m_j}-\frac{s_j}{m_0}\sum_{i=1}^d w_i s_i\right].
\]
For each active index \(j\), the number \(s_j\sum_i w_i s_i\) is at least \(w_j-\sum_{i\ne j}w_i=2w_j-W\). It follows that
\[
 D^+J_w(g)\le\sum_{j=1}^dc_j|g_j|^{p-1}
 \left(\frac{W-2w_j}{m_0}-\frac{w_j}{m_j}\right)
 \le\gamma\sum_{j=1}^dc_j|g_j|^{p-1},
\]
where \(\gamma\) is the maximum coefficient in the finding. Conversely, for \(g_j=1\) and \(g_i=0\) for \(i\ne j\), the derivative of the nonzero difference is \(-c_j(1/m_j+1/m_0)\), whereas each initially zero difference acquires derivative \(-c_j/m_0\). Hence
\[
 D^+J_w(g)=c_j\left(\frac{W-2w_j}{m_0}-\frac{w_j}{m_j}\right).
\]
This gives equality in the normalized supremum for every index, proving sharpness even at the nonsmooth configurations where the derivative of absolute value matters.

If every coefficient is nonpositive, the displayed bound makes the upper right time derivative of \(J_w(u(t))\) nonpositive for every initial state and every subsequent time; continuity and the elementary Dini monotonicity principle show that \(J_w(u(t))\le J_w(u(0))\) for all \(t\ge0\). If any coefficient is positive, its one-edge initial state has a strictly positive right derivative; hence variation increases for all sufficiently small positive times. Rearranging the coefficients gives the stated \(d\) inequalities.

Finally normalize \(\alpha_i=w_i/W>0\). The inequalities are exactly \(\alpha_i\ge(2+m_0/m_i)^{-1}\). Such positive \(\alpha_i\) can sum to one precisely when the sum of these lower bounds is at most one. If equality holds there is a single normalized choice; otherwise distribute the positive slack among the indices. If leaf masses all equal \(m\), the condition becomes \(d/(2+m_0/m)\le1\), or \(m_0\ge(d-2)m\). No step depends on \(p\), except that \(|g_i|^{p-1}\) is positive for an active index and vanishes for a zero index.

## Verification

The included standalone `verify.py` uses exact rational arithmetic to check the directional-derivative upper bound for 26,460 nonconstant integer difference profiles, attainability on 15,120 isolated-edge profiles, and the sharp feasibility certificates on 1,260 positive mass profiles. It additionally checks 5,320 fractional-exponent profiles (including exponents between one and two), 15,000 explicit small-step nonlinear-flow inequalities, and the six-leaf critical-mass example. Invoke with `python verify.py` from the extracted package. The analytical proof above, not the sampled tests, establishes the universal quantifiers.

## Relationship to prior work

Hua and Mugnolo's *Time regularity and long-time behavior of parabolic p-Laplace equations on infinite graphs* (arXiv:1410.1584v1, October 6, 2014) treats weighted vertex measures, edge conductances, nonlinear well-posedness and contractions in vertex \(\ell^q\) spaces; its introductory equations and nonlinear semigroup results do not directly yield the sharp edge-weighted \(\ell^1\) variation generator or the mass threshold above. Keller and Mugnolo's *General Cheeger inequalities for p-Laplacians on graphs* (arXiv:1509.06062v1, September 20, 2015) studies weighted graph \(p\)-energy and spectral/Cheeger estimates, not this variation-dissipativity classification. Mugnolo's *Parabolic theory of the discrete p-Laplace operator* (arXiv:1207.1996v1, July 9, 2012) treats nonlinear semigroup well-posedness, positivity, comparisons and invariance, but not an independently weighted edge-variation star mass threshold. Xin, Mu and Liu's 2011 study of discrete \(p\)-Laplacian diffusion with absorption establishes an initial-boundary-value framework, comparison and extinction/positivity assertions rather than the present all-mass star criterion. Earlier linear heat-flow results on stars or trees with counting measure do not imply the nonlinear all-exponent statement with independent vertex masses; the mass mechanism here permits arbitrarily many leaves when the central mass increases.

## Limitations

This is a one-input total-variation result on finite stars; it does not give a two-input variation Lipschitz constant, a classification for trees with multiple branching centers or graphs with cycles, or a uniform exponential decay rate for nonlinear exponents. The normalized infinitesimal coefficient controls the initial variation derivative relative to a nonlinear flux magnitude, not relative to variation itself. A comprehensive identification of possible implicit formulations in older dissipativity or nonlinear-semigroup literature would require broader independent literature review. There has been no independent scientific audit.

## References

1. B. Hua and D. Mugnolo, *Time regularity and long-time behavior of parabolic p-Laplace equations on infinite graphs*, arXiv:1410.1584v1 (2014-10-06), https://arxiv.org/abs/1410.1584.
2. M. Keller and D. Mugnolo, *General Cheeger inequalities for p-Laplacians on graphs*, arXiv:1509.06062v1 (2015-09-20), https://arxiv.org/abs/1509.06062.
3. Q. Xin, C. Mu, and D. Liu, *Extinction and positivity of the solutions for a p-Laplacian equation with absorption on graphs*, Journal of Applied Mathematics (2011), article 937079, first published 2011-09-19, https://doi.org/10.1155/2011/937079.
4. D. Mugnolo, *Parabolic theory of the discrete p-Laplace operator*, arXiv:1207.1996v1 (2012-07-09), https://arxiv.org/abs/1207.1996.
5. Y. van Gennip, N. Guillen, B. Osting and A. L. Bertozzi, *Mean curvature, threshold dynamics, and phase field theory on finite graphs*, Milan J. Math. 82 (2014), 3–65, https://doi.org/10.1007/s00032-014-0216-8.
