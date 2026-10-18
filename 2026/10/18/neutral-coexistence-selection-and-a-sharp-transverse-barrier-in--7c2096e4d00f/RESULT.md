# Neutral coexistence selection and a sharp transverse barrier in the lottery–Ricker map

## Finding
For every real \(r>0\), consider the positive-quadrant map
\[
H_r(x,y)=\left(\frac{rx}{x+y},\;y\exp(r-x-y)\right),\qquad x,y>0.
\]
Every positive forward trajectory converges to a single fixed point \((x_\infty,y_\infty)\) with \(x_\infty+y_\infty=r\), \(x_\infty>0\) and \(y_\infty\geq0\). In particular, there are no interior periodic or recurrent orbits other than fixed points. Every compactly supported invariant probability measure in the positive quadrant is supported on that fixed-point segment.

There is a sharp selection barrier when \(r>2\). If an initial point is not an eventual preimage of the fixed segment, its limit has
\[
\frac{x_\infty}{r}\geq\frac{r-2}{r-1}.
\]
The constant is the best possible infimum over such initial points. Below that threshold, the fixed segment has transversely repelling linearization. Nevertheless, a distinct one-step preimage line \(x+y=u_r\) maps onto the entire *interior* fixed segment: \(u_r\in(0,1)\) is the smaller solution of \(u\exp(r-u)=r\). In particular, a positive point can land in one step on an interior transversely repelling equilibrium.

## Assumptions and scope
The phase space is \((0,\infty)^2\), and \(r>0\) is constant. All limits concern forward iterates. The fixed segment is \(\{(x,r-x):0<x\leq r\}\). The exceptional-line and sharp-barrier statements require \(r>2\), whereas global convergence requires only \(r>0\). An *eventual preimage of the fixed segment* means an initial state for which some finite iterate satisfies \(x_n+y_n=r\). No claim is made for orbits confined to the \(y\)-axis or for the map at the origin, where its first component is undefined.

Define \(s=x+y\), \(f=x/s\), and \(\Phi(t)=t-1-\log t\) for \(t>0\). Put \(Q=x/y^{1/r}\). Exact one-step identities are
\[
\begin{aligned}
s'-r&=(1-f)\big(s\exp(r-s)-r\big),\\
\log\frac{Q'}Q&=\Phi(s/r)\geq0.
\end{aligned}
\]
The second identity is strict unless \(s=r\), and yields the exact composition-selection formula
\[
Q_n=Q_0\exp\left(\sum_{j=0}^{n-1}\Phi(s_j/r)\right).
\]
The weighted Lyapunov identity underlying this formula is already present, in an equivalent reciprocal power, in the motivating 2011 primary article; novelty is not asserted for this identity alone.

## Proof
**(1) Compactness and separation from the singular origin.** For every \(n\geq1\),
\[
0<x_n\leq r,\qquad 0<y_n\leq\exp(r-1),
\]
because \(u\exp(r-u)\leq\exp(r-1)\) for \(u>0\). Hence \(s_n\leq M=r+\exp(r-1)\). Let \(\delta=r/2\) and
\[
m=\min_{\delta\leq u\leq M}u\exp(r-u)>0,
\qquad c=\min\{s_1,\delta,m\}>0.
\]
If \(s\leq\delta\), both \(r>s\) and \(s\exp(r-s)>s\), so \(s'=fr+(1-f)s\exp(r-s)>s\). If \(s\geq\delta\), then \(s'\geq\min\{r,m\}=m\), since the minimizing interval includes \(r\). By induction \(c\leq s_n\leq M\) for all \(n\geq1\).

**(2) Monotone composition selection.** Direct substitution gives
\[
\frac{Q'}Q=\frac r s\exp\left(\frac{s-r}{r}\right)
=\exp\Phi(s/r).
\]
Thus \(Q_n\) is nondecreasing. If it has a finite limit \(Q_\infty\in(0,\infty)\), logarithmic increments tend to zero. Strict convexity of \(\Phi\), together with \(s_n\in[c,M]\), implies \(s_n\to r\). For each \(s>0\), the map \(x\mapsto x/(s-x)^{1/r}\) is strictly increasing from zero to infinity as \(x\) ranges over \((0,s)\). Therefore \(s_n\to r\) and \(Q_n\to Q_\infty\) force convergence to a unique point with both coordinates positive and sum \(r\).

If instead \(Q_n\to\infty\), boundedness of \(x_n\) gives \(y_n\to0\). Because \(s_n\geq c\), eventually \(x_n\geq c/2\), and hence
\[
x_{n+1}=\frac{r}{1+y_n/x_n}\longrightarrow r.
\]
Consequently \((x_n,y_n)\to(r,0)\). This proves global pointwise convergence. It also excludes nontrivial interior periodic orbits. For a compactly supported invariant probability \(\mu\) in the positive quadrant, \(\log Q\) is bounded on its support; stationarity gives
\[
0=\int(\log Q\circ H_r-\log Q)\,d\mu
=\int\Phi((x+y)/r)\,d\mu.
\]
The nonnegative integrand vanishes only on \(x+y=r\), so \(\mu\) is supported there. Recurrence outside the segment is ruled out by strict growth of \(Q\) and compact orbit limits.

**(3) Transverse spectrum and the lower barrier.** At a fixed point \((rf,r(1-f))\), where \(0<f<1\), differentiation yields
\[
DH_r=\begin{pmatrix}
1-f&-f\\
-r(1-f)&1-r(1-f)
\end{pmatrix};
\qquad\operatorname{spec}(DH_r)=\{1,(1-r)(1-f)\}.
\]
When \(r>2\), the transverse multiplier has modulus greater than one exactly for \(f<(r-2)/(r-1)\). If a positive orbit never lands on the fixed line, then \(s_n-r\ne0\), and the exact mass-deviation identity gives
\[
\frac{s_{n+1}-r}{s_n-r}
=(1-f_n)\frac{s_n\exp(r-s_n)-r}{s_n-r}
\longrightarrow(1-f_\infty)(1-r)
\]
provided the limiting point is interior. If \(f_\infty<(r-2)/(r-1)\), the absolute value of the limit exceeds one, contradicting \(s_n-r\to0\). A boundary limit has \(f_\infty=1\) and already satisfies the inequality.

**(4) Sharpness.** Fix any \(f_*\) strictly between \((r-2)/(r-1)\) and \(1\). At \((rf_*,r(1-f_*))\), the mass-deviation quotient in (3) has absolute value less than one. By continuity, choose a narrow strip \(|f-f_*|<\eta\), \(|s-r|<\eta\) in which \(|s'-r|\leq k|s-r|\) with some \(k<1\). Inside the strip, \(\Phi(s/r)\leq C(s-r)^2\), so a trajectory starting at \(s_0=r+\varepsilon\), \(f_0=f_*\), for sufficiently small nonzero \(\varepsilon\), has total logarithmic \(Q\)-drift at most \(C\varepsilon^2/(1-k^2)\). The smooth, locally invertible coordinate transformation \((s,f)\mapsto(s,\log Q)\) then keeps \(f\) in the strip by a standard induction: \(|f_n-f_*|\leq C'(\lvert\varepsilon\rvert+\varepsilon^2/(1-k^2))<\eta\). Shrink the strip to exclude every zero of \(s\exp(r-s)-r\) other than \(s=r\). Then \(s_n-r\ne0\) for all \(n\), while the terminal composition approaches \(f_*\) as \(\varepsilon\to0\). Taking \(f_*\downarrow(r-2)/(r-1)\) proves optimality of the bound as an infimum.

**(5) Exceptional preimages.** The fixed-point line is \(s=r\), and the mass identity shows that its full one-step preimage in the positive quadrant is precisely the collection of solutions of \(s\exp(r-s)=r\). For \(r>2\), the function \(s\exp(r-s)\) increases on \((0,1)\), decreases on \((1,\infty)\), and takes its unique maximum \(\exp(r-1)>r\) at \(1\). Hence its level \(r\) has exactly the two roots \(u_r\in(0,1)\) and \(r\). At any point of \(s=u_r\),
\[
H_r(fu_r,(1-f)u_r)=(rf,r(1-f)),\qquad0<f<1.
\]
This proves that even transversely repelling interior points of the segment can be reached in one step from strictly positive states. The endpoint \((r,0)\) cannot be reached in one step from a strictly positive state.

## Verification
The accompanying `VERIFY.py` checks the symbolic mass identity, the fixed-line Jacobian spectrum, the weighted-ratio identity and finite sample trajectories for several parameter values. The general convergence and sharpness claims follow from the inequalities and compactness arguments above, not from numerical enumeration.

## Relationship to prior work
Kang and Smith introduced the same lottery–Ricker map and proved global exclusion for \(r_1>r_2\), as well as persistence and period-two phenomena for \(r_1<r_2\). Their 2011 preprint gives the exact weighted monomial Lyapunov quotient from which the neutral monotonicity identity follows immediately, so that algebraic identity is not independently new. The present result targets the omitted equality regime \(r_1=r_2=r\): pointwise convergence for every strictly positive start, a sharp transverse selection threshold for non-landing points, and the exceptional preimage that permits direct access to the repelling segment. The closest related preimage study was bibliographically located but its full content could not be inspected; the overlap risk is explicit.

## Limitations
This result concerns a deterministic map with equal parameters and strictly positive initial states. It does not classify boundary-axis Ricker orbits, perturbations away from equality, or stochastic variants. The threshold is an infimum for non-eventually-landing trajectories; no assertion is made that the endpoint is attained by such a trajectory. A 2011 related preimage article remains a bibliographic originality risk. The algebraic verification script does not constitute a complete computer-assisted proof.

## References
1. Yun Kang and Hal Smith, *Global Dynamics of a Discrete Two-species Lottery-Ricker Competition Model*, arXiv:1102.2286v1 (first public version 2011-02-11), https://arxiv.org/html/1102.2286v1 ; published in *Journal of Biological Dynamics* 6 (2012), 358–376, doi:10.1080/17513758.2011.586064.
2. Yun Kang, *Pre-images of invariant sets of a discrete-time two-species competition model*, *Journal of Difference Equations and Applications* 18 (2012), 1709–1733 (published online 2011), doi:10.1080/10236198.2011.591390. Full text not accessible during this comparison; no exclusion of overlap is inferred from the abstract alone.
