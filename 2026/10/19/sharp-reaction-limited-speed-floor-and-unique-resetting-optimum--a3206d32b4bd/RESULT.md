# Sharp reaction-limited speed floor and unique resetting optimum under inward drift

## Finding

Consider diffusion on the real line with generator \(D\partial_{xx}-U\partial_x\), started and independently reset to \(L>0\) at Poisson rate \(r>0\). A point trap at the origin kills at the Feynman--Kac rate \(k\delta_0\), with fixed \(D,k>0\) and inward drift speed \(U\geq0\). Write \(T_U(r)\) for the mean time to killing and \(r_*(U)\) for the optimal reset rate.

**Theorem.** For every \(D,L,k>0\) and \(U\geq0\), there is exactly one finite positive global minimizer \(r_*(U)\). Every finite \(U\) and \(r>0\) obeys the strict, parameter-independent speed floor
\[
T_U(r)>\frac{eL}{k}.
\]
The floor is sharp under increasingly strong inward drift: keeping \(D,L,k\) fixed as \(U\to\infty\),
\[
\begin{aligned}
r_*(U)&=\frac{U}{L}-\frac{k}{eL}+O_{D,L,k}(U^{-1}),\\
\min_{r>0}T_U(r)&=\frac{eL}{k}+\frac{(e-1)L+eD/k}{U}+O_{D,L,k}(U^{-2}).
\end{aligned}
\]
In addition, \(r_*(U)\) initially decreases strictly as \(U\) rises above zero, but \(r_*(U)\to\infty\) as \(U\to\infty\). Hence its dependence on inward drift speed has at least one interior minimum, for **every** finite positive reactivity \(k\). No uniqueness assertion is made about this minimum in the drift-speed variable.

## Assumptions and scope

The free motion is \(dX_t=-U\,dt+\sqrt{2D}\,dW_t\). On each reset, position returns instantly to \(L\); the bath is unaffected. The trapping functional is \(\exp[-k\int_0^t\delta_0(X_s)\,ds]\), normalized by the standard occupation-density convention corresponding to the forward term \(-k\delta_0(x)p(0,t)\). The killing event terminates the motion. Parameters \(D,L,k\) are strictly positive, \(U\geq0\), and the optimized reset rate ranges over all \(r>0\). The limit \(U\to\infty\) fixes \(D,L,k\), notably does not replace the finite-reactivity target by perfect absorption.

## Proof

**1. Killed resolvent and renewal.** Set \(a_r=\sqrt{U^2+4Dr}\). The free drift-diffusion resolvent from \(L\) to zero equals \(a_r^{-1}\exp[-(a_r-U)L/(2D)]\), and its diagonal value at the origin equals \(a_r^{-1}\). The rank-one killing resolvent therefore gives the Laplace transform of the no-reset killing-time law,
\[
q_U(r)=\frac{k}{k+a_r}\exp\!\left[-\frac{L(a_r-U)}{2D}\right].
\]
An independent exponential reset clock splits the evolution into identically distributed attempts. An attempt succeeds with probability \(q_U(r)\); its expected duration, stopped at killing or reset, is \((1-q_U(r))/r\). The renewal equation therefore yields
\[
T_U(r)=\frac{1-q_U(r)}{r q_U(r)}.
\]
This independent derivation agrees with the forward mean-time formula of the motivating article, but the optimization claims below are separate.

**2. Exact dimensionless objective and strict floor.** Introduce
\[
M=\frac{UL}{2D},\qquad \eta=\frac{2D}{kL},\qquad t=\frac{L}{2D}\left(\sqrt{U^2+4Dr}-U\right)>0.
\]
Then \(r=(D/L^2)t(2M+t)\), a strictly increasing bijection of \(t>0\) and \(r>0\), and
\[
T_U(r)=\frac{L^2}{D}F_M(t),\qquad
F_M(t)=\frac{[1+\eta(M+t)]e^t-1}{t(2M+t)}.
\]
Since \(e^t-1>0\), \((M+t)/(2M+t)\geq1/2\), and \(e^t/t\geq e\),
\[
F_M(t)>\eta\frac{M+t}{2M+t}\frac{e^t}{t}\geq\frac{\eta e}{2}.
\]
The displayed strict bound follows on multiplying by \(L^2/D\). Also \(F_M(t)\to\infty\) as \(t\downarrow0\) and as \(t\to\infty\), including \(M=0\), so a positive finite global minimizer exists.

**3. Uniqueness at every inward speed.** Let \(N(t)=[1+\eta(M+t)]e^t-1\), \(B(t)=t(2M+t)\), and \(H(t)=N'(t)B(t)-N(t)B'(t)\). The derivative \(F_M'(t)\) has the sign of \(H(t)\). Its entire power series \(H(t)=\sum_{n\geq0}c_nt^n\) satisfies
\[
 c_0=-2\eta M^2,\quad c_1=-2\eta M,\quad c_2=(M-1)+\eta(M^2+M-1),
\]
and, for every integer \(n\geq2\),
\[
n!c_n=Q_n=2(1+\eta M)((n-1)M-n)+n(n-1)[1+\eta(3M+n-3)].
\]
In particular \(Q_3=4M(1+\eta M+3\eta)\geq0\), and for every integer \(n\geq2\),
\[
Q_{n+1}-Q_n=2M+2(n-1)+\eta[2M^2+2M(3n-1)+n(3n-5)]>0.
\]
Thus the coefficient sequence has exactly one change from negative to positive: for \(M>0\), \(c_0,c_1<0\), \(c_2\) has either sign, and \(c_n>0\) for all \(n\geq3\); at \(M=0\), \(c_2<0\), \(c_3=0\), and \(c_n>0\) for \(n\geq4\). Divide \(H(t)\) by the first power \(t^j\) having a positive coefficient after the negative coefficients (\(j=2,3\), or \(4\) according to the case). The resulting expression is strictly increasing on \(t>0\): each lower-degree negative term becomes a negative inverse power with positive derivative, and each higher-degree positive term is increasing. It tends to a negative value or \(-\infty\) at zero and to \(+\infty\) at infinity. Therefore \(H\) has exactly one positive simple zero; \(F_M\) decreases before it and increases afterward. This proves uniqueness and nondegeneracy of the global optimum.

**4. Strong-drift asymptotics.** Uniformly for \(t\) in compact subsets of \((0,\infty)\), as \(M\to\infty\),
\[
F_M(t)=f(t)+\frac{g(t)}M+O(M^{-2}),\qquad
f(t)=\frac{\eta e^t}{2t},\qquad
g(t)=\frac{e^t(1+\eta t/2)-1}{2t}.
\]
The strict floor in step 2 and the trial value \(t=1\), for which \(F_M(1)\to\eta e/2\), imply that every global minimizer \(t_M\) satisfies \(t_M\to1\): the coercive function \(e^t/t\) has the unique minimum \(e\) at \(t=1\). Since \(f''(1)=\eta e/2>0\), the analytic implicit function theorem applied to \(\partial_tF_M=0\) near \((t,M^{-1})=(1,0)\) yields
\[
t_M=1-\frac{1/2+1/(\eta e)}{M}+O(M^{-2}).
\]
Substitute this into \(r=(D/L^2)t(2M+t)\), and into the expansion for \(F_M(t)\) using \(g(1)=[e(1+\eta/2)-1]/2\). The claimed two expansions follow.

**5. Forced turnover in the optimal rate.** At \(U=0\), write \(r_0=r_*(0)\) and \(T_0(r)=T_{U=0}(r)\). Expansion of the resolvent-derived formula at fixed \(r\) gives
\[
T_U(r)=T_0(r)-\frac{UL}{2D}\left(T_0(r)+\frac1r\right)+O(U^2).
\]
By uniqueness and nondegeneracy from step 3, implicit differentiation of \(\partial_rT_U(r_*(U))=0\) yields
\[
\left.\frac{dr_*(U)}{dU}\right|_{U=0^+}
=-\frac{L}{2D\,r_0^2T_0''(r_0)}<0.
\]
The optimizer is continuous (indeed locally analytic) in \(U\geq0\), and step 4 shows \(r_*(U)\to\infty\). Therefore at least one interior drift speed minimizes \(r_*(U)\). This does not assert a unique turnover speed.

## Verification

Run `python check.py` alongside this file. It symbolically checks both asymptotic coefficients and the stationary-polynomial coefficient identity, compares the MFPT against an independently written killed-resolvent/restart expression, tests many distinct physical parameter sets, and tests the sharp bound at both optimized and nonoptimized rates. Finite numerical tests support algebra and normalization; the proof of uniqueness and the global strict bound use the preceding analytic identities, not numerical sampling.

## Relationship to prior work

Mazzolo (arXiv:2609.22527v1, Sections III and Appendix A.5) derives the drift-dependent forward resolvent and mean time, and illustrates nonmonotonic optimal-rate behavior numerically for one choice of physical parameters. The present theorem does **not** claim those forward formulas. It supplies all-parameter uniqueness under inward drift, a sharp global reaction-limited lower bound, two-term large-inward-drift optimization laws, and an analytic turnover-existence theorem for every finite reactivity. Whitehouse, Evans, and Majumdar (arXiv:1301.2489v1, Section 4) optimize a partially absorbing target without drift. Ray, Mondal, and Reuveni (arXiv:1811.08239v1, Sections IV and Appendix B) analyze directed drift with a **perfectly** absorbing boundary. Neither setting entails the stated finite-reactivity, strong-inward-drift optimization theorem without a further argument. The underlying restart identity and rank-one Green-function reduction are established tools, not asserted new discoveries.

## Limitations

The model is one-dimensional and uses a single fixed point trap, exact Poisson resets to the same location, spatially constant inward drift, and the stated delta-killing normalization. The strong-drift expansions hold with \(D,L,k\) fixed and are not uniform as \(k\to\infty\). There is no assertion about outward drift, multiple traps, non-Poisson resetting, or the uniqueness of the drift speed at which the optimal resetting rate attains its minimum. The present self-review are not an independent scientific audit. The finite-parameter mean formula is established prior literature; originality attaches only to the optimized inequalities/classification and their proofs.

## References

1. A. Mazzolo, *Diffusion with stochastic resetting in the presence of a delta killing trap: Drift-controlled survival regimes*, arXiv:2609.22527v1 (first posted 18 September 2026), https://arxiv.org/abs/2609.22527.
2. J. Whitehouse, M. R. Evans, and S. N. Majumdar, *Effect of Partial Absorption on Diffusion with Resetting*, arXiv:1301.2489v1 (2013), https://arxiv.org/abs/1301.2489.
3. S. Ray, D. Mondal, and S. Reuveni, *Péclet number governs transition to acceleratory restart in drift-diffusion*, arXiv:1811.08239v1 (2018), https://arxiv.org/abs/1811.08239.
