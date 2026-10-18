# A sharp order-one transition in the Rényi entropy of stationary Markov pairs

## Finding

Let a stationary finite-state Markov chain have the refresh kernel
\[
P=rI+(1-r){\bf 1}\pi^{\mathsf T},\qquad 0<r<1,
\]
where \(\pi\) is a strictly positive probability vector on \(n\ge2\) states. Write \(Q_t(i,j)=\Pr(X_0=i,X_t=j)\), and let \(H_\alpha\) denote Rényi entropy of order \(\alpha>0\), with Shannon entropy at \(\alpha=1\).

**Entropy-phase classification.** If \(\alpha\ge1\), the sequence \(H_\alpha(Q_t)\) is strictly increasing in integer \(t\ge0\) and approaches \(2H_\alpha(\pi)\) from below. The same conclusion holds when \(0<\alpha<1\) and \(\pi\) is uniform. In contrast, for every \(0<\alpha<1\) and every nonuniform positive \(\pi\), the continuous interpolation \(H_\alpha(Q_v)\), \(0<v<1\), has exactly one interior maximum; the integer-lag sequence eventually decreases and, at all sufficiently large finite lags, strictly exceeds its independence limit \(2H_\alpha(\pi)\).

Define \(A_\alpha=\sum_i\pi_i^\alpha\) and \(B_\alpha=\sum_i\pi_i^{2\alpha-1}-A_\alpha^2\). For every fixed \(\alpha\ne1\),
\[
H_\alpha(Q_t)-2H_\alpha(\pi)
=\frac{\alpha B_\alpha}{(1-\alpha)A_\alpha^2}\,r^t+O(r^{2t}).
\]
For nonuniform \(\pi\) the coefficient is strictly positive below order one and strictly negative above it. At Shannon order,
\[
H_1(Q_t)-2H_1(\pi)=-\frac{n-1}{2}r^{2t}+O(r^{3t}),
\]
and for uniform \(\pi\) the corresponding expression at any fixed \(\alpha>0\) is \(-\alpha(n-1)r^{2t}/2+O(r^{3t})\).

Let \(v_\alpha^*\in(0,1)\) be the unique continuous maximizer for nonuniform \(\pi\) and \(0<\alpha<1\), and let \(V_\pi=\operatorname{Var}_{i\sim\pi}(\log\pi_i)>0\). As \(\alpha\uparrow1\),
\[
v_\alpha^*=\frac{(1-\alpha)V_\pi}{n-1}+O((1-\alpha)^2),\qquad
H_\alpha(Q_{v_\alpha^*})-2H_\alpha(\pi)
=\frac{(1-\alpha)^2V_\pi^2}{2(n-1)}+O((1-\alpha)^3).
\]
The corresponding real-valued peak lag is
\[
t_\alpha^*=\frac{\log v_\alpha^*}{\log r}
=\frac{\log(1/(1-\alpha))}{|\log r|}+O(1).
\]
Thus an exceptionally simple reversible, uniformly ergodic chain has monotonically decreasing absolute-regularity coefficient \(\beta(t)=(1-\sum_i\pi_i^2)r^t\), but nonmonotone lagged Rényi effective support. In particular, \(\mathcal J_\infty^{(t)}=\exp(H_{1/2}(Q_t))\) overshoots its independent-pair limit for every nonuniform \(\pi\).

## Assumptions and scope

Fix an integer \(n\ge2\), a vector \(\pi_i>0\) with \(\sum_i\pi_i=1\), and \(r\in(0,1)\). The chain begins in \(\pi\). For \(t\in\mathbb Z_{\ge0}\), the stationary pair law is \(Q_t\). The continuous interpolation is the probability law
\[
Q_v(i,j)=(1-v)\pi_i\pi_j+v\pi_i\mathbf1_{i=j},\qquad 0\le v\le1,
\]
so \(Q_t=Q_{r^t}\). The entropy of a finite probability law \(\mu\) is
\[
H_\alpha(\mu)=\frac{\log\sum_x\mu(x)^\alpha}{1-\alpha}\quad(\alpha\ne1),
\qquad H_1(\mu)=-\sum_x\mu(x)\log\mu(x).
\]
Logs are natural; \(0\log0=0\). Strict monotonicity in the statement refers to integer lags, while uniqueness of the interior peak refers to the continuous variable \(v\). No assertion concerns general reversible chains outside the specified refresh family.

## Proof

Set \(E={\bf1}\pi^{\mathsf T}\). Since \(E^2=E\), \(P^t=r^tI+(1-r^t)E\); consequently \(Q_t=Q_{r^t}\). Detailed balance follows from \(\pi_iP_{ij}=r\pi_i\mathbf1_{i=j}+(1-r)\pi_i\pi_j\), and all transition entries are positive. Define \(\Delta_{ij}=\pi_i(\mathbf1_{i=j}-\pi_j)\), and for \(0<v<1\) put \(S_\alpha(v)=\sum_{i,j}Q_v(i,j)^\alpha\). Then \(Q_v=\pi\otimes\pi+v\Delta\), and for \(\alpha\ne1\)
\[
S'_\alpha(v)=\alpha\sum_{i,j}\Delta_{ij}Q_v(i,j)^{\alpha-1},\qquad
S''_\alpha(v)=\alpha(\alpha-1)\sum_{i,j}\Delta_{ij}^2Q_v(i,j)^{\alpha-2}.
\]
The final sum is strictly positive, since \(n\ge2\) and all \(\pi_i>0\). Direct summation at the independence endpoint gives
\[
S_\alpha(0)=A_\alpha^2,\qquad S'_\alpha(0)=\alpha B_\alpha.
\]
Cauchy–Schwarz applied to \(A_\alpha=\sum_i\pi_i^{\alpha-1/2}\sqrt{\pi_i}\) yields \(B_\alpha\ge0\), with equality for \(\alpha\ne1\) exactly when \(\pi\) is uniform.

For \(\alpha>1\), strict convexity of \(S_\alpha\) and \(S'_\alpha(0)\ge0\) imply \(S'_\alpha(v)>0\) for every \(v>0\); because \(1/(1-\alpha)<0\), \(H_\alpha(Q_v)\) strictly decreases in \(v\). If \(0<\alpha<1\) and \(\pi\) is uniform, strict concavity together with \(S'_\alpha(0)=0\) gives the same decrease. If \(0<\alpha<1\) and \(\pi\) is nonuniform, strict concavity and \(S'_\alpha(0)>0\) hold, while
\[
\lim_{v\uparrow1}S'_\alpha(v)=-\infty.
\]
Indeed every off-diagonal summand has negative \(\Delta_{ij}\), and its magnitude diverges like \((1-v)^{\alpha-1}\); diagonal summands remain bounded. Thus exactly one zero \(v_\alpha^*\in(0,1)\) exists, with \(S_\alpha\) strictly increasing before and strictly decreasing after it. Since \(1/(1-\alpha)>0\), the same is true of entropy. Furthermore \(H_\alpha(Q_v)>H_\alpha(Q_0)=2H_\alpha(\pi)\) for all sufficiently small positive \(v\). Replacing \(v\) by \(r^t\) proves the claimed eventual overshoot and decrease. Since the real-lag curve is unimodal, its largest integer-lag value is attained at one of the two integers adjacent to \(t_\alpha^*\) (with endpoint clipping if necessary).

At \(\alpha=1\), both marginals of \(Q_v\) are \(\pi\). Accordingly
\[
H_1(Q_v)=2H_1(\pi)-D(Q_v\Vert\pi\otimes\pi),
\]
where the divergence has derivative zero at \(v=0\) and strictly positive second derivative \(\sum_{i,j}\Delta_{ij}^2/Q_v(i,j)\) for \(v\in[0,1)\). Hence the divergence increases strictly in \(v>0\), proving the Shannon statement.

Taylor expansion at \(v=0\) gives \(H_\alpha(Q_v)=2H_\alpha(\pi)+\alpha B_\alpha v/((1-\alpha)A_\alpha^2)+O(v^2)\). Also
\[
\sum_{i,j}\frac{\Delta_{ij}^2}{\pi_i\pi_j}=n-1,
\]
so the Shannon expansion is \(-(n-1)v^2/2+O(v^3)\). If \(\pi\) is uniform, the same identity in \(S''_\alpha(0)\), along with \(S'_\alpha(0)=0\), yields \(-\alpha(n-1)v^2/2+O(v^3)\) for every fixed \(\alpha\ne1\); continuity supplies \(\alpha=1\). Substitution \(v=r^t\) proves the finite-lag expansions.

For the near-Shannon transition write \(\eta=1-\alpha\downarrow0\). Expanding the finite sums of strictly positive numbers gives
\[
B_{1-\eta}=\eta^2V_\pi+O(\eta^3),\qquad
\left.\partial_v H_{1-\eta}(Q_v)\right|_{v=0}=\eta V_\pi+O(\eta^2),
\]
and \(\partial_v^2H_{1-\eta}(Q_v)|_{v=0}=-(n-1)+O(\eta)\). These derivatives extend smoothly to \((\eta,v)=(0,0)\). Because the latter second derivative is nonzero, the implicit-function theorem applied to the equation \(\partial_vH_{1-\eta}(Q_v)=0\) gives \(v_\alpha^*=\eta V_\pi/(n-1)+O(\eta^2)\). Evaluating the Taylor series there gives the quadratic overshoot coefficient. Taking \(\log v_\alpha^*/\log r\) gives the peak-lag asymptotic.

Finally,
\[
\beta(t)=\tfrac12\sum_{i,j}|Q_t(i,j)-\pi_i\pi_j|
=\tfrac12r^t\sum_{i,j}|\Delta_{ij}|
=\left(1-\sum_i\pi_i^2\right)r^t.
\]
For \(\alpha=1/2\), \(\exp(H_{1/2}(Q_t))=(\sum_{ij}\sqrt{Q_t(i,j)})^2\), establishing the effective-support interpretation.

## Verification

The bundled `verify.py` uses exact rational matrix powers to check the identity \(Q_t=Q_{r^t}\) for random positive stationary laws on two through five states, compares finite-lag entropy profiles at several orders, numerically solves the unique critical-point equation, and checks all three asymptotic expansions. It completed 654 finite tests without error. These checks support the algebra but are not substitutes for the analytic proof above.

For illustration, take \(\pi=(9/10,1/10)\), \(r=7/10\), and \(\alpha=1/2\). The unique continuous maximizer is approximately \(v^*=0.1745116896701\), corresponding to real lag \(t^*=4.894550569747\); the largest integer-lag effective support occurs at \(t=5\):
\[
\mathcal J_\infty^{(5)}\approx2.605443373946
>2.56=\lim_{t\to\infty}\mathcal J_\infty^{(t)}.
\]
The absolute-regularity coefficient nevertheless equals \(0.18(0.7)^t\) and strictly decreases.

## Relationship to prior work

Judd and Esposito (2026, arXiv:2610.10860v1, Sections 1 and 3–6) define the stationary lag-pair law and its effective-support quantity \(\mathcal J_\infty^{(s)}\) in the context of average-mixing-time estimation. They study converse bounds and specifically take an envelope over time lags. Wolfer and Alquier (2024 preprint, 2026 revision, arXiv:2402.10506v5, Sections 3.1, 4.1 and 4.4) introduce the same Rényi-related entropic factor for estimation and analyze two-state \(\beta\)-mixing, but do not derive the monotonicity classification or near-Shannon transition above. General Rényi entropic inequalities (Linden, Mosonyi and Winter, arXiv:1212.0248) establish that classical Rényi entropy lacks Shannon-like universal linear relations; such general feasibility results do not supply the stated reversible Markov family, unique maximum, sharp lag asymptotics or critical scaling. The present claim is a specific exact analysis, not a claim that Rényi non-subadditivity is new.

## Limitations

The classification holds only for finite positive stationary vectors and kernels of the specified refresh form. The overshoot is a property of **ordinary joint Rényi entropy** and does not contradict monotonicity of a Rényi *divergence* to stationarity. No assertion is made for arbitrary reversible or nonreversible kernels, for negative eigenvalues, or for the maximum over every restricted mixing-time window. Integer sampling may select either of the two lags surrounding the continuous peak. The literature comparison is necessarily bounded; unindexed equivalent special cases remain possible.

## References

1. N. A. Judd and A. R. Esposito, *On the Impossibility of Estimating the Average Mixing Time*, arXiv:2610.10860v1 (first posted 2026-10-07), https://arxiv.org/html/2610.10860v1.
2. G. Wolfer and P. Alquier, *Optimistic Estimation of Convergence in Markov Chains with the Average-Mixing Time*, arXiv:2402.10506v5, https://arxiv.org/html/2402.10506v5.
3. N. Linden, M. Mosonyi and A. Winter, *The structure of Rényi entropic inequalities*, arXiv:1212.0248, https://arxiv.org/abs/1212.0248.
