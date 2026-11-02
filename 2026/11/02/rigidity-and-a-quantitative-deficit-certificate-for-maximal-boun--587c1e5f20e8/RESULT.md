# Rigidity and a quantitative deficit certificate for maximal bounded-rationality loss on the Braess network

## Finding

The universal factor \(2\) in the excess-time bound for a directed five-edge Wheatstone (Braess) network has a rigid equality set. More precisely, for **every** positive demand \(q\), every choice of continuous nonnegative nondecreasing edge-latency functions, every Wardrop path-flow equilibrium \(f\), and every feasible path flow \(g\), define
\[
\varepsilon(g)=\max_{P:g_P>0}\left(c_P(g)-\min_{Q\in\{U,M,D\}}c_Q(g)\right),\qquad
\psi(g)=\frac{\Psi(g)-\Psi(f)}q.
\]
Then \(\psi(g)\le 2\varepsilon(g)\). There is a sharper **two-regime certificate**. When \(g_U\ge f_U\) or \(g_D\ge f_D\),
\[
\psi(g)\le\varepsilon(g).
\]
Otherwise, with \(L=\Psi(f)/q\),
\[
R(f,g)=\bigl(c_M(f)-L\bigr)+\bigl(b(f_U)-b(g_U)\bigr)+
\bigl(c(f_D)-c(g_D)\bigr)+\bigl(e(g_M)-e(f_M)\bigr)\ge0,
\]
where \(b,c,e\) denote the latency functions on the upper exit, lower entrance, and central cross edge. In this second regime,
\[
\boxed{\psi(g)\le 2\varepsilon(g)-R(f,g).}
\]
For \(\varepsilon(g)>0\), equality \(\psi(g)=2\varepsilon(g)\) holds **if and only if** all of the following conditions hold: (i) \(g=(0,q,0)\); (ii) \(f_U>0\) and \(f_D>0\); (iii) all three paths have cost \(L\) at \(f\); (iv) \(b(0)=b(f_U)\), \(c(0)=c(f_D)\), and \(e(f_M)=e(q)\); (v) the two positive outer-edge cost increments coincide,
\[
a(q)-a(q-f_D)=d(q)-d(q-f_U)=\varepsilon(g)>0.\]
In particular a positive equality case requires three specific latency plateaus; if any of \(b,c,e\) is strictly increasing, equality is impossible. The stated conditions hold for **any choice** of Wardrop reference flow whenever equality holds.

## Assumptions and scope

The directed graph has four vertices \(s,u,v,t\) and exactly five directed edges \(s\to u\), \(u\to t\), \(s\to v\), \(v\to t\), and \(u\to v\). Their continuous nonnegative nondecreasing latency functions on \([0,\infty)\) are denoted respectively by \(a,b,c,d,e\). There is a **single** source-destination commodity of mass \(q>0\). The three simple paths are \(U=(s,u,t)\), \(M=(s,u,v,t)\), \(D=(s,v,t)\); a feasible path flow is \((h_U,h_M,h_D)\in\mathbb R_{\ge0}^3\) with sum \(q\). The induced edge loads, in edge order \((a,b,c,d,e)\), are
\[
(q-h_D,\ h_U,\ h_D,\ q-h_U,\ h_M).
\]
Thus \(c_U(h)=a(q-h_D)+b(h_U)\), \(c_M(h)=a(q-h_D)+e(h_M)+d(q-h_U)\), and \(c_D(h)=c(h_D)+d(q-h_U)\). The social cost is \(\Psi(h)=\sum_P h_Pc_P(h)\). A Wardrop equilibrium means every positively used path minimizes path cost among all three paths. Such an equilibrium exists under these assumptions. All formulas apply without uniqueness of the equilibrium path-flow decomposition. No differentiability, convexity of latencies, or positive lower latency is assumed.

## Proof

**1. Wardrop baseline.** Let \(f\) be an equilibrium, and let \(L\) denote its minimum path cost. Every used path has cost \(L\), so \(\Psi(f)=qL\). At every feasible \(g\), each used path costs at most \(\min_P c_P(g)+\varepsilon(g)\), hence
\[
\Psi(g)/q\le \min_Pc_P(g)+\varepsilon(g).\tag{1}
\]
Write \(\delta_U=g_U-f_U\) and \(\delta_D=g_D-f_D\).

**2. The unit-coefficient regime.** If \(\delta_U<0\le\delta_D\), then \(f_U>0\). The edge loads of \(a\) and \(b\) weakly decrease from \(f\) to \(g\), so \(c_U(g)\le c_U(f)=L\). Symmetrically, if \(\delta_D<0\le\delta_U\), then \(c_D(g)\le L\). If \(\delta_U\ge0\) and \(\delta_D\ge0\) with at least one strict, then \(g_M=f_M-\delta_U-\delta_D\ge0\) entails \(f_M>0\). All three edges of \(M\) have weakly smaller loads under \(g\), hence \(c_M(g)\le c_M(f)=L\). If both differences vanish, all edge loads and costs are unchanged and a formerly used shortest path remains shortest. Therefore whenever at least one difference is nonnegative, \(\min_Pc_P(g)\le L\), and (1) gives \(\psi(g)\le\varepsilon(g)\).

**3. The quantitative deficit regime.** Suppose \(\delta_U<0\) and \(\delta_D<0\). Then \(f_U,f_D>0\), so \(c_U(f)=c_D(f)=L\), while \(c_M(f)\ge L\). Also \(g_M>f_M\), \(g_U<f_U\), and \(g_D<f_D\). Monotonicity implies that each term of
\[
R=(c_M(f)-L)+[b(f_U)-b(g_U)]+[c(f_D)-c(g_D)]+[e(g_M)-e(f_M)]
\]
is nonnegative. Direct cancellation of the \(a,d\) terms in the path costs gives the **exact identity**
\[
c_U(g)+c_D(g)=c_M(g)+L-R.\tag{2}
\]
Set \(x=\min\{c_U(g),c_D(g)\}\). Since the middle path carries positive flow at \(g\), its cost is at most \(x+\varepsilon(g)\). By (2),
\[
2x\le c_U(g)+c_D(g)=c_M(g)+L-R\le x+\varepsilon(g)+L-R,
\]
so \(\min_Pc_P(g)\le x\le L+\varepsilon(g)-R\). Inserting this bound into (1) gives \(\psi(g)\le2\varepsilon(g)-R\).

**4. Necessity of all equality conditions.** Assume \(\varepsilon(g)>0\) and \(\psi(g)=2\varepsilon(g)\). The unit-coefficient regime is impossible, so \(g_U<f_U\) and \(g_D<f_D\). The stronger bound forces \(R=0\). Equality in the chain of inequalities in step 3 forces
\[
\min_Pc_P(g)=x=L+\varepsilon(g),\qquad c_M(g)=L+2\varepsilon(g).
\]
By (2), \(c_U(g)+c_D(g)=2L+2\varepsilon(g)\), and since both outer path costs are at least the minimum \(L+\varepsilon(g)\), necessarily
\[
c_U(g)=c_D(g)=L+\varepsilon(g).
\]
Every path positively used by \(g\) must have cost \(L+2\varepsilon(g)\), because their weighted average attains the maximal permitted used cost. Since both outer costs are smaller, \(g_U=g_D=0\) and \(g_M=q\). The strict decreases from \(f\) give \(f_U,f_D>0\). The four nonnegative terms in \(R=0\) separately vanish; thus \(c_M(f)=L\), \(b(f_U)=b(0)\), \(c(f_D)=c(0)\), and \(e(f_M)=e(q)\). Together with \(c_U(f)=c_D(f)=L\), the equal outer cost changes give \(a(q)-a(q-f_D)=d(q)-d(q-f_U)=\varepsilon(g)>0\), proving necessity.

**5. Sufficiency and attainability.** Conversely, assume (i)–(v), including that \(f\) is Wardrop. The flatness of \(b,c,e\), all-three-path tie at \(f\), and the common outer increments imply \(c_U(g)=c_D(g)=L+\varepsilon\) and \(c_M(g)=L+2\varepsilon\) for \(g=(0,q,0)\), where \(\varepsilon>0\) is that increment. The exact regret is \(\varepsilon(g)=\varepsilon\), while \(\Psi(g)/q=L+2\varepsilon\), so equality follows. To realize the conditions with a positive central component even at \(f\), set \(q=1\), \(f=(2/5,1/5,2/5)\), \(g=(0,1,0)\), \(b=c\equiv1/2\), \(e\equiv0\), and for any \(\theta>0\) set
\[
a(x)=d(x)=1/2+(5\theta/2)\max\{0,x-3/5\}.
\]
The three path costs at \(f\) are \(1\), whereas at \(g\) they are \(1+\theta,1+2\theta,1+\theta\). Thus \(\psi(g)=2\theta=2\varepsilon(g)\), proving sharpness. This example respects nonnegativity and continuity.

## Verification

Run the standalone pure-Python checker with `python verify_braess.py`. It enumerates active sets of rational affine-latency Wardrop equations exactly, tests the two regime inequalities and the equality implications on rational path flows, and separately verifies explicit piecewise-linear sharpness families including nonzero center-path flow at \(f\). Its reported finite counts are 600 affine models, 85,800 path-flow comparisons, and 12 rational sharpness instances. The algebraic proof above, not these finite checks, establishes the infinite claim.

## Relationship to prior work

Massicot and Langbort (2024, arXiv:2406.00295, §3.2 and Appendix A) defined the same additive regret and welfare metrics, displayed a Wheatstone cost instance with coefficient \(2\), and asserted the coefficient for every flow **within that specified instance**. Their Theorem 8 provides topology-dependent asymptotic constants and instance-dependent global constants without identifying the universal sharp constant or its full equality set for arbitrary Wheatstone latencies. Accordingly, the **new contribution here is the nonnegative quantitative deficit \(R\) and the necessary-and-sufficient classification of every positive sharp case**; the published witness and general boundedness principles are not claimed as new. Nikolova and Stier-Moses (2014, arXiv:1411.0059, §4–5) prove a factor \(2\) in a different, multiplicative price-of-risk-aversion model with risk coefficients controlled relative to latency; their alternating-path proof is relevant background, but it does not state this plateau characterization or the \(R\) certificate for additive satisficing regret. Takalloo and Kwon (2019, arXiv:1911.07914) investigate multiplicative price of satisficing. Di et al. (2014) investigate the Braess paradox under bounded rationality, but its complete publisher text was not accessible for a decisive priority check; this remains a publication-priority risk.

## Limitations

The graph must have exactly the specified direction on the central edge and a single source-destination commodity; the proof does not cover arbitrary five-edge orientations, multicommodity networks, stochastic latencies, or atomic traffic. The equality classification concerns strictly positive regret; zero regret merely recovers an equilibrium with zero excess. Latency plateaus are necessary for positive-regret *attainment*; the theorem does not quantify how closely strictly increasing latency families may approach the bound. The theorem is an analytic result, not an independent external audit. Priority in the inaccessible 2014 specialized literature remains uncertain.

## References

1. O. Massicot and C. Langbort, *On Network Congestion Reduction Using Public Signals Under Boundedly Rational User Equilibria (Full Version)*, arXiv:2406.00295, v1 posted 2024-06-01; https://arxiv.org/html/2406.00295v2, particularly §3.2 and Appendix A.
2. E. Nikolova and N. E. Stier-Moses, *The Burden of Risk Aversion in Mean-Risk Selfish Routing*, arXiv:1411.0059, §4–5; https://arxiv.org/abs/1411.0059.
3. M. Takalloo and C. Kwon, *On the Price of Satisficing in Network User Equilibria*, arXiv:1911.07914, posted 2019-11-18; https://arxiv.org/html/1911.07914v1.
4. X. Di, X. He, X. Guo, and H. X. Liu, *Braess paradox under the boundedly rational user equilibria*, *Transportation Research Part B* 67 (2014), 86–108, https://doi.org/10.1016/j.trb.2014.04.005 (abstract accessible, full text not obtained).
