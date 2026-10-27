# Sharp reentrant capture-majority window for two partially absorbing Brownian targets

## Finding

Consider Brownian diffusion on the whole real line with two unequal point absorbers at \(-a\) and \(2a\), and Poisson resetting to zero. The farther right absorber can lose the eventual capture majority with no resetting, win it for intermediate resetting, and lose it again for sufficiently rapid resetting. This *reentrant capture-majority effect* occurs for some choice of near-target strength precisely when the dimensionless far-target reactivity \(B\) is greater than \(1\).

More precisely, for fixed \(B>0\) put
\[
H_B(t)=\frac{2Bt e^{-t}}{2t+B(1-e^{-t})(1+e^{-3t})}\quad(t>0),\qquad H_B(0)=\frac{B}{1+B},\qquad C(B)=\max_{t\ge0}H_B(t).
\]
For \(A>0\), reentrance means that the farther target has capture probability strictly less than \(1/2\) at zero resetting, strictly greater than \(1/2\) at some positive resetting rate, and strictly less than \(1/2\) at all sufficiently large rates. The **exact necessary and sufficient condition** is
\[
\boxed{\frac{B}{1+B}<A<C(B).}
\]
The window is nonempty if and only if \(B>1\). In particular, for \(A=11/10\) and \(B=100\), it occurs and causes at least two distinct capture-majority crossings as the reset rate increases. The statement concerns the probability of the *ultimate absorbing target*, not the mean time to absorption or the probability of merely hitting a target.

## Assumptions and scope

Fix \(D>0\), a length \(a>0\), and absorption strengths \(\kappa_L,\kappa_R>0\). The particle starts at \(0\), follows the diffusion with generator \(D\partial_{xx}\), and while alive independently resets to \(0\) at Poisson rate \(r\ge0\). At \(-a\) and \(2a\) it is killed at density rates \(\kappa_L\delta_{-a}\) and \(\kappa_R\delta_{2a}\), respectively. Equivalently, in the forward equation the loss term is \(-[\kappa_L\delta(x+a)+\kappa_R\delta(x-2a)]p(x,t)\); this specifies the local-time normalization. Resetting stops upon capture. Let \(P_L(r)\) and \(P_R(r)\) denote ultimate capture probabilities on the two respective sinks.

Set \(A=\kappa_La/D\), \(B=\kappa_Ra/D\), and \(t=a\sqrt{r/D}\). These are strictly positive except that \(t=0\) is allowed. There is no reflecting or absorbing boundary at either sink: it is *partially* absorbing and may be crossed repeatedly before killing. This result is for the specified \(1{:}2\) target-distance geometry only; it does not assert universality for arbitrary separations or non-Poisson resetting.

## Proof

**1. Eventual capture.** For \(r=0\), one-dimensional Brownian motion is recurrent and its local time at the nearer fixed site diverges almost surely. A positive exponential killing hazard on that local time gives eventual capture with probability one. For \(r>0\), each independent excursion between resets has positive probability of capture; the geometric sequence of independent attempts therefore ends in capture almost surely. Consequently \(P_L(r)+P_R(r)=1\) for every \(r\ge0\).

**2. Exact capture odds.** For \(r>0\), let \(g_r(x,y)=e^{-\sqrt{r/D}|x-y|}/(2\sqrt{Dr})\) be the resolvent of unrestricted diffusion killed by an independent exponential clock of rate \(r\). Put \(c=(2\sqrt{Dr})^{-1}\), \(q=e^{-t}\), and let \(u_L,u_R\) be the resolvent occupation densities at the two traps when the starting point is zero, before either capture or reset. The finite-rank resolvent identity gives the exact *two-equation system*
\[
\begin{pmatrix}1+\kappa_Lc&\kappa_Rcq^3\\ \kappa_Lcq^3&1+\kappa_Rc\end{pmatrix}
\begin{pmatrix}u_L\\u_R\end{pmatrix}
=c\begin{pmatrix}q\\q^2\end{pmatrix}.
\]
Its determinant is \(1+c(\kappa_L+\kappa_R)+\kappa_L\kappa_Rc^2(1-q^6)>0\), and solving shows
\[
u_L=\frac{cq[1+\kappa_Rc(1-q^4)]}{\Delta},\qquad
u_R=\frac{cq^2[1+\kappa_Lc(1-q^2)]}{\Delta}.
\]
The single-excursion capture probabilities are \(j_L=\kappa_Lu_L\), \(j_R=\kappa_Ru_R\). Geometric renewal over resets multiplies both by the same factor \((j_L+j_R)^{-1}\): \(P_i=j_i/(j_L+j_R)\). Therefore for all \(t>0\),
\[
\boxed{\frac{P_R}{P_L}=\frac{B}{A}e^{-t}\frac{2t+A(1-e^{-2t})}{2t+B(1-e^{-4t})}.}\tag{1}
\]
The finite positive limit at \(t\downarrow0\) is
\[
\boxed{\frac{P_R(0)}{P_L(0)}=\frac{B(1+A)}{A(1+2B)}.}\tag{2}
\]
This limit also follows directly from the two-sink boundary-value problem without resetting.

**3. Reduce the majority question to one scalar envelope.** Clearing strictly positive denominators in (1), and using \(1-q^4-q(1-q^2)=(1-q)(1+q^3)\), gives
\[
P_R(r)>\frac12\quad\Longleftrightarrow\quad
A<H_B(t).
\tag{3}
\]
Equation (2) gives \(P_R(0)<1/2\) exactly when \(A>B/(1+B)=H_B(0)\). Since \(H_B(t)\to0\) as \(t\to\infty\), the near target always wins for all sufficiently large \(r\). Continuity of \(H_B\) on \([0,\infty)\) and its vanishing at infinity prove that reentrance is equivalent to \(H_B(0)<A<\max_{t\ge0}H_B(t)\), as claimed. The strict inequalities yield two distinct majority crossings by the intermediate value theorem.

**4. Sharp far-reactivity threshold.** A Taylor expansion of the explicit envelope at zero gives
\[
H_B(t)=\frac{B}{1+B}+\frac{B(B-1)}{(1+B)^2}t+O_B(t^2).
\tag{4}
\]
For \(B>1\), (4) shows \(C(B)>H_B(0)\); since \(H_B(t)\to0\), the strict maximum is attained at a positive finite \(t\).

For \(0<B\le1\), we prove the *global* reverse inequality \(H_B(t)<H_B(0)\) for every \(t>0\), not just a local derivative. Write \(q=e^{-t}\in(0,1)\). After clearing positive factors it is equivalent to
\[
K(B,t):=2t[(1+B)q-1]-B(1-q)(1+q^3)<0.
\tag{5}
\]
For fixed \(t>0\), \(K\) is affine in \(B\). At \(B=0\), it equals \(2t(q-1)<0\). At \(B=1\), it equals \(2t(2q-1)-(1-q)(1+q^3)\). This is negative immediately for \(q\le1/2\). For \(1/2<q<1\), the strict elementary inequality \(t<\sinh t=(1-q^2)/(2q)\) gives
\[
2t(2q-1)<\frac{(1-q^2)(2q-1)}q
=(1-q)(1+q^3)-\frac{(1-q)(1-q^2)^2}q
<(1-q)(1+q^3).
\]
Thus \(K(1,t)<0\), and affinity proves \(K(B,t)<0\) for all \(0<B\le1\). Therefore \(C(B)=H_B(0)\) for \(B\le1\), while \(C(B)>H_B(0)\) for \(B>1\), completing the if-and-only-if proof.

**5. Strict explicit witness.** Choose \(A=11/10\), \(B=100\). At no resetting, (2) equals \(700/737<1\). At \(t=\log2\), (1) gives \(P_R>P_L\) exactly when
\[
(2B-4A)\log2>\frac98 AB,
\]
which holds because \(\log2>2/3\) (from the positive power series for \(\operatorname{arctanh}(1/3)\)), \(2B-4A=978/5\), and \((9/8)AB=495/4\): the left side is strictly greater than \(652/5>495/4\). Since the odds in (1) tend to zero as \(t\to\infty\), there are at least two crossings, one before \(t=\log2\) and another after. Their existence persists under sufficiently small changes in both positive strengths by strict continuity.

## Verification

A standard-library Python checker, `check.py`, reconstructs the independent two-by-two resolvent linear solve and compares it against formula (1) at 175 parameter combinations, tests representative subcritical and supercritical envelopes, and brackets two zero-odds-difference roots for the explicit witness. Execute `python3 check.py`; its console output is not a proof for continuously many parameters. The proof of the global \(B\le1\) inequality is analytic (step 4), while direct manipulation of (1) establishes every asserted strict equivalence. The endpoint \(r=0\) follows from the stated explicit continuous limit and recurrence.

## Relationship to prior work

Whitehouse–Evans–Majumdar, arXiv:1301.2489 (first posted 2013-01-11), treats Poisson resetting with **one** partially absorbing delta target, establishing the single-target model but no competitive two-target majority criterion. Giuggioli–Gupta–Chase, arXiv:1901.03033, is particularly close: Sec. 3 and Appendix B contain a general two-defect resolvent for partially absorbing sites, and Sec. 5 gives exact splitting probabilities for **two perfectly absorbing** targets. Its two-defect propagator already implies the *forward* ratio (1) after specializing the locations and extracting the two capture fluxes; that ratio alone is **not** claimed as original. The contribution here is the sharp necessary-and-sufficient *reentrant majority classification* (3)–(5), including the global far-reactivity threshold \(B=1\), the exact open parameter window, and a certified two-crossing witness. These do not occur as stated or proved in the inspected sections of that paper; the result is nevertheless a nontrivial further consequence of its broader general model.

Schumm–Bressloff, arXiv:2104.09372, Sec. 5, gives multi-target renewing flux and splitting formulae for **spatially extended** partially absorbing targets in two dimensions. Bressloff–Schumm, arXiv:2110.06895, analyzes small finite targets in two/three dimensions and reset-controlled targeting. These frameworks motivate competing reaction channels but do not establish the stated one-dimensional delta-sink iff threshold. Pal–Prasad, arXiv:1812.03009, studies two **perfectly absorbing** endpoints; this comparison was made from abstract and bibliographic content only, not full article text. Pal and collaborators, arXiv:2502.09127, discuss general conditional-selectivity criteria under resetting, not this sharp two-local-time-sink parameter boundary. Distinctive search terms and statements were also checked against indexed mathematical research records; no equivalent classification was identified. A failed search is not a proof of novelty.

## Limitations

The geometry is fixed at distances \(a\) and \(2a\) on opposite sides of the reset point; the threshold \(B>1\) is not asserted for different distance ratios, spatially extended targets, state-dependent resetting, or asymmetric diffusion. The theorem establishes *at least* two capture-majority crossings in the reentrant regime, not an exact count of crossings, nor monotonicity of the envelope for \(B>1\). The phase boundary \(C(B)\) is defined exactly by a one-variable maximum, not by an elementary closed form. Priority cannot be conclusively established from the finite literature checked; especially, generic two-defect resolvents predating this calculation supply the forward data and specialized unlocated treatments may exist. Numerical checks are illustrative rather than substitutes for infinite-domain proofs.

## References

1. J. Whitehouse, M. R. Evans, and S. N. Majumdar, *Effect of Partial Absorption on Diffusion with Resetting*, arXiv:1301.2489 (initial public posting 2013-01-11), https://arxiv.org/abs/1301.2489.
2. L. Giuggioli, S. Gupta, and M. Chase, *Comparison of two models of tethered motion*, arXiv:1901.03033, https://arxiv.org/abs/1901.03033.
3. R. D. Schumm and P. C. Bressloff, *Search processes with stochastic resetting and partially absorbing targets*, arXiv:2104.09372, https://arxiv.org/abs/2104.09372.
4. P. C. Bressloff and R. D. Schumm, *The narrow capture problem with partially absorbing targets and stochastic resetting*, arXiv:2110.06895, https://arxiv.org/abs/2110.06895.
5. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009, https://arxiv.org/abs/1812.03009.
6. A. Pal and collaborators, *Universal criterion for selective outcomes under stochastic resetting*, arXiv:2502.09127, https://arxiv.org/abs/2502.09127.
