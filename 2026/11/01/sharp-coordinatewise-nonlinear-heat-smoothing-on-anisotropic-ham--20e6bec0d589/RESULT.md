# Sharp coordinatewise nonlinear heat smoothing on anisotropic Hamming graphs

## Finding

For every integer \(d\ge1\), every alphabet-size vector \((q_1,\ldots,q_d)\) with \(q_i\ge2\), every conductance vector \((c_1,\ldots,c_d)\) with \(c_i>0\), and every common exponent \(1<p<\infty\), consider the nonlinear \(p\)-heat flow on the Cartesian product of cliques \(G=K_{q_1}\square\cdots\square K_{q_d}\). All vertex masses equal one, and an edge in direction \(i\) has conductance \(c_i\). Define the coordinatewise edge-Lipschitz seminorm
\[
L_i(f)=\max_{x,y\text{ adjacent in coordinate }i}|f(x)-f(y)|.
\]
Set
\[
\alpha_p=\begin{cases}1,&1<p\le2,\\2^{2-p},&p>2,\end{cases}\qquad
\kappa_i=c_i\bigl(2+(q_i-2)\alpha_p\bigr).
\]
For \(a\ge0\), \(t\ge0\), and \(\kappa>0\), define the scalar decay profile
\[
\Phi_p(t,a;\kappa)=
\begin{cases}
\bigl[\max\{0,a^{2-p}-(2-p)\kappa t\}\bigr]^{1/(2-p)},&1<p<2,\\
a e^{-\kappa t},&p=2,\\
\bigl[a^{2-p}+(p-2)\kappa t\bigr]^{-1/(p-2)},&p>2,\ a>0,\\
0,&a=0.
\end{cases}
\]
The displayed first branch also yields zero if \(a=0\). Let \(S_t\) denote the global nonlinear heat flow. Then **every** initial function \(f\) satisfies, simultaneously for all axes and all times,
\[
\boxed{L_i(S_t f)\le\Phi_p(t,L_i(f);\kappa_i)\qquad(1\le i\le d,\ t\ge0).}
\]
This is **jointly sharp**: for every prescribed vector \((a_1,\ldots,a_d)\) of nonnegative coordinatewise seminorms, there is a single initial datum \(f\) for which equality holds for **every** axis \(i\) and **every** \(t\ge0\). Consequently, the sharp bound on the ordinary edge-Lipschitz seminorm \(L(f)=\max_i L_i(f)\) is the maximum of the indicated scalar profiles.

For \(1<p<2\), all solutions reach a constant state no later than
\[
\boxed{T(f)=\max_{1\le i\le d}\frac{L_i(f)^{2-p}}{(2-p)\kappa_i},}
\]
where a zero coordinate seminorm contributes zero. This uniform time bound is sharp for every prescribed vector of initial coordinate seminorms. For a binary hypercube \(q_i=2\), \(\kappa_i=2c_i\) independently of dimension and of \(p\).

## Assumptions and scope

The vertex set is \(X=\prod_{i=1}^d\{0,\ldots,q_i-1\}\). Two distinct vertices are adjacent precisely when exactly one coordinate differs. Edges in coordinate \(i\) all have the same conductance \(c_i>0\), and each vertex has mass one. The flow is the ODE
\[
\frac{d}{dt}u(t,x)=\sum_{i=1}^d c_i\sum_{a\ne x_i}\varphi_p\bigl(u(t,x^{i\to a})-u(t,x)\bigr),
\qquad \varphi_p(s)=|s|^{p-2}s,
\]
with \(\varphi_p(0)=0\). Here \(x^{i\to a}\) means replacing only coordinate \(i\) by \(a\). No assertion is made for different nonlinear exponents on different axes, unequal conductances inside one axis, unequal vertex masses, or \(p=1\).

On this finite graph the vector field is continuous. It is the negative gradient of the convex \(C^1\) energy \(\frac1p\sum_{\{x,y\}\in E}c_{i(x,y)}|u(x)-u(y)|^p\), so monotonicity gives uniqueness and Euclidean nonexpansivity even for \(1<p<2\). A maximum principle bounds all vertex values between their initial extrema and ensures existence for all times. Hence \(S_t\) is well-defined for every real initial function.

## Proof

**1. A scalar convexity inequality.** For \(0\le s\le1\), write \(h_p(s)=s^{p-1}+(1-s)^{p-1}\). If \(1<p<2\), \(h_p\) is concave and has minimum \(1\) at its endpoints. If \(p=2\), it equals \(1\). If \(p>2\), it is convex with minimum \(2^{2-p}\) at \(s=1/2\). Thus \(h_p(s)\ge\alpha_p\), including the boundary cases.

**2. Exact directional derivative estimate.** Fix time \(t\) with \(\ell=L_i(u(t))>0\), and choose any active direction-\(i\) edge \((x,y)\), ordered so that \(u(x)-u(y)=\ell\). Let \(z\) run through the other \(q_i-2\) vertices of the complete fiber containing \(x,y\). Since each pair in this fiber is an edge of direction \(i\), the maximality of \(\ell\) gives \(u(y)\le u(z)\le u(x)\). The direct edge \(x\leftrightarrow y\) contributes \(-2c_i\ell^{p-1}\) to \(\dot u(x)-\dot u(y)\). For any other \(z\), with \(s=(u(z)-u(y))/\ell\in[0,1]\), the contribution is exactly
\[
 c_i[\varphi_p(u(z)-u(x))-\varphi_p(u(z)-u(y))]
 =-c_i\ell^{p-1}h_p(s)\le-c_i\alpha_p\ell^{p-1}.
\]
The entire direction-\(i\) contribution is therefore at most \(-\kappa_i\ell^{p-1}\).

For a different coordinate \(j\ne i\), pair a neighbor \(x'\) of \(x\) obtained by changing coordinate \(j\) with the corresponding neighbor \(y'\) of \(y\) obtained by the same change. The vertices \(x',y'\) are adjacent in direction \(i\); hence \(u(x')-u(y')\le\ell=u(x)-u(y)\). Rearranging yields
\[
 u(x')-u(x)\le u(y')-u(y).
\]
Because \(\varphi_p\) is increasing and both matched edges have conductance \(c_j\), their contribution to \(\dot u(x)-\dot u(y)\) is nonpositive. Summing all coordinates gives \(\dot u(x)-\dot u(y)\le-\kappa_i\ell^{p-1}\).

The maximum of finitely many differentiable edge differences has right upper Dini derivative no greater than the maximum of the active derivatives. Thus, whenever \(L_i(u(t))>0\),
\[
 D^+L_i(u(t))\le-\kappa_iL_i(u(t))^{p-1}.
\]
If \(L_i=0\), the function is invariant under all permutations of coordinate \(i\). Such permutations are graph automorphisms preserving the conductances; uniqueness of the flow preserves this invariance. Therefore \(L_i\) remains zero once it reaches zero.

**3. Integrate the differential inequality.** For \(1<p<2\), applying the comparison principle to \(L_i^{2-p}\) until it vanishes gives \(L_i(t)^{2-p}\le\max\{0,L_i(0)^{2-p}-(2-p)\kappa_i t\}\). For \(p=2\), Grönwall's inequality yields \(L_i(t)\le L_i(0)e^{-\kappa_i t}\). For \(p>2\), differentiating \(L_i^{2-p}\) where positive and using its nonincreasing property yields \(L_i(t)^{2-p}\ge L_i(0)^{2-p}+(p-2)\kappa_i t\). These are exactly the three branches of \(\Phi_p\). At an axis with initial seminorm zero, the bound follows from invariance.

**4. Simultaneous all-time sharpness.** Fix any \(a_i\ge0\) independently. If \(a_i=0\), take a constant function of coordinate \(i\). Otherwise, on the alphabet of coordinate \(i\), use the following profile:

For \(1<p\le2\), assign value \(a_i\) to exactly one symbol and zero to the remaining \(q_i-1\) symbols. By symmetry the high–low gap \(g_i(t)\) evolves through \(g_i'=-c_iq_i g_i^{p-1}=-\kappa_i g_i^{p-1}\), since \(\alpha_p=1\).

For \(p>2\), assign values \(+a_i/2\) and \(-a_i/2\) to two symbols, and zero to any other symbols. The middle symbols remain at zero, the extreme values remain opposites, and their gap evolves through
\[
 g_i'=-c_i\bigl[2+(q_i-2)2^{2-p}\bigr]g_i^{p-1}=-\kappa_i g_i^{p-1}.
\]
This works also when \(q_i=2\), with no middle symbols.

Let \(f_i(t,\cdot)\) be these one-clique solutions and set \(u(t,x)=\sum_{i=1}^d f_i(t,x_i)\). Each edge change in direction \(i\) involves only \(f_i\), so the nonlinear vector field decomposes exactly and \(u(t,\cdot)\) solves the full product flow. For every \(i,t\), its direction-\(i\) seminorm equals \(g_i(t)=\Phi_p(t,a_i;\kappa_i)\). In particular a single constructed initial function simultaneously attains all directional estimates at all times, proving joint sharpness.

**5. Consensus.** If \(1<p<2\), each coordinate seminorm vanishes by its indicated time. Once all directions have vanishing edge differences, connectedness of the product forces the function to be constant. The separable extremizers from Step 4 attain the last vanishing time \(T(f)\), establishing optimality of the formula for every initial vector \((a_i)\).

## Verification

The standalone script `verify_hamming_pheat.py` uses only the Python standard library. Run it with `python verify_hamming_pheat.py` from the directory containing this document. It reconstructs the Cartesian adjacency and vector field independently, checks the active-edge derivative bound in exact rational arithmetic for \(p=2,3,4\), and verifies simultaneous extremizers with exact fractions. It also checks scalar profiles and finite extinction numerically for additional real exponents and independently integrates sample nonlinear systems by a fourth-order Runge–Kutta method. The observed output is:

```text
EXACT_DIRECTIONAL_DINI_INEQUALITIES_OK 2265
EXACT_SIMULTANEOUS_EXTREMIZERS_OK 54
SCALAR_FLOW_AND_EXTINCTION_DIAGNOSTICS_OK
NONLINEAR_FLOW_ENVELOPES_OK 80
ALL_HAMMING_PHEAT_TESTS_OK
```

These are finite reproducibility checks; the all-parameter theorem follows from the five analytical steps above, not from finite sampling.

## Relationship to prior work

Mugnolo's 2012 preprint develops existence, nonlinear semigroup contraction in vertex-function spaces, comparison and graph symmetry for discrete \(p\)-heat. Hua–Mugnolo (2014) studies time regularity and extinction, especially on infinite graphs. Those results supply the correct framework but do not evaluate the **directionwise edge-Lipschitz** decay coefficient for anisotropically weighted Hamming products or its simultaneous sharp all-time extremizers. Lin–Liu–Yang (2015 preprint, 2016 online) establishes a gradient-form inequality for positive functions involving the **linear Laplacian**, not the present sharp nonlinear directional time-decay inequality. Abatangelo–Dragomir (2008) develops discrete-time **linear** heat kernels on binary Hamming graphs. That linear case and the familiar \(p=2\) product heat behavior are acknowledged as antecedents, not claimed as independent novelties.

These distinctions concern mathematical implications: general \(\ell^q\) nonexpansivity does not yield decay of the *edge* seminorm with optimal coefficient, and a linear heat-kernel representation does not supply the nonlinear \(p\ne2\) exponent-dependent profile. Earlier related product results for total variation and edge projection norms concern different functionals and therefore do not imply the theorem above. The principal scientific novelty claim is the nonlinear, axiswise, weighted, jointly sharp all-time classification.

## Limitations

The graph must be a finite Cartesian product of complete graphs, with a common nonlinear exponent, equal vertex masses, and conductance constant within each coordinate direction. Neither arbitrary graph products nor within-axis heterogeneous weights are covered. The result concerns an individual solution's directional differences, not the Lipschitz distance between *two* solutions. It does not address infinite products, \(p=1\), or \(p=\infty\). Searches cannot rule out equivalent unindexed prior work, and no independent external audit is claimed.

## References

1. D. Mugnolo, *Parabolic theory of the discrete p-Laplace operator*, arXiv:1207.1996, publicly submitted 9 July 2012, https://arxiv.org/abs/1207.1996 .
2. B. Hua and D. Mugnolo, *Time regularity and long-time behavior of parabolic p-Laplace equations on infinite graphs*, arXiv:1410.1584, submitted 6 October 2014, https://arxiv.org/html/1410.1584v1 .
3. Y. Lin, S. Liu and Y. Yang, *A gradient estimate for positive functions on graphs*, arXiv:1509.07981, submitted 26 September 2015, https://arxiv.org/abs/1509.07981 .
4. V. Abatangelo and S. Dragomir, *Discrete Heat Equation Morphisms*, Interdisciplinary Information Sciences 14 (2008), 225–244, https://doi.org/10.4036/iis.2008.225 .
