# Sharp deterministic-input gap and three-regime A-optimal timing for two-stage identification

## Finding

**Theorem (sharp two-stage A-optimal input-design classification).** Consider \(x_0=0\), \(x_1=b u_0+w\), with \(b\ne0\), \(\mathbb Ew=0\), \(\mathbb Ew^2=s>0\), and \(w\) independent of the time-zero input. Write \(h=b^2>0\), \(z_t=(x_t,u_t)^{\mathsf T}\), and \(\Sigma=\mathbb E(z_0z_0^{\mathsf T}+z_1z_1^{\mathsf T})\). For all \(\eta>0\) and \(\beta>s\), minimize the **nonlinear** A-optimal information criterion
\[
 F=\operatorname{tr}[(\eta I_2+\Sigma)^{-1}],\qquad \operatorname{tr}\Sigma\le\beta,
\]
over every causal policy with finite second moments, including randomized policies. Put
\[
 S_*=\operatorname{clamp}\left(\frac\beta2,\ s,\ \frac{s+h\beta}{1+h}\right),\qquad
 q_* =\frac{S_*-s}{h},\qquad
 p_*=\beta-s-(1+h)q_*.
\]
Here the clamp is the projection onto the displayed interval. The **unique optimal information matrix** is diagonal:
\[
 \boxed{\Sigma_*=\operatorname{diag}(S_*,\beta-S_*)},\qquad
 \boxed{F_*=\frac1{\eta+S_*}+\frac1{\eta+\beta-S_*}}.
\]
Every optimum has \(\mathbb Eu_0^2=q_*\), \(\mathbb Eu_1^2=p_*\), and \(\mathbb E[x_1u_1]=0\); independently randomized, zero-mean open-loop inputs attain the optimum. The unique timing regimes (with agreement at boundaries) are:

1. **Late only:** \(s<\beta\le2s\), with \(q_*=0\), \(p_*=\beta-s\).
2. **Both stages:** \(\beta>2s\), except the last regime, with \(S_*=\beta/2\), \(q_*>0\), \(p_*>0\), and \(F_*=4/(\beta+2\eta)\). When \(h\ge1\), this holds for **all** \(\beta>2s\); when \(0<h<1\), it holds for \(2s<\beta<2s/(1-h)\).
3. **Early only:** If \(0<h<1\) and \(\beta\ge2s/(1-h)\), then \(q_*=(\beta-s)/(1+h)\) and \(p_*=0\).

There is a distinct, **sharp deterministic open-loop restriction**: if both inputs are prescribed real constants, every optimal choice invests its entire budget in **one stage only**. Let \(Q=(\beta-s)/(1+h)\). Its optimal A-criterion is
\[
 \boxed{F_{\mathrm{det}}=\min\!\left\{\frac1{\eta+s}+\frac1{\eta+\beta-s},\quad
 \frac1{\eta+s+hQ}+\frac1{\eta+Q}\right\}}.
\]
The optimum is late-only when \(\beta<s(2+h)\), early-only when \(\beta>s(2+h)\), with the two pure stages tied at equality (and no mixed deterministic optimum). Hence \(F_{\mathrm{det}}>F_*\) **if and only if** \(q_*>0\) and \(p_*>0\), namely exactly in the both-stages regime. This gap does not imply that *all* deterministic state-feedback policies fail: the comparison is specifically with prescribed deterministic open-loop sequences.

For fixed \(h>1\), as \(\beta\to\infty\),
\[
 \boxed{\frac{F_{\mathrm{det}}}{F_*}\longrightarrow\frac{(1+h)^2}{4h}}.
\]
This ratio is unbounded as \(h\to\infty\). Thus neither deterministic pure-stage excitation nor any deterministic time-splitting can furnish a gain-independent multiplicative approximation to the fully causal A-optimal design criterion.

## Assumptions and scope

The horizon is exactly two scored state-input observations, at times zero and one; the state equation beyond \(x_1\) does not affect these observations. Inputs may depend causally on available states and independent internal randomness, and are square-integrable. The disturbance need not be Gaussian; its centering, variance, and independence from \(u_0\) suffice. The source's weights are specialized to identity design and energy matrices and isotropic positive regularization \(\eta I_2\). The budget is on expected **state plus input** energy, not merely input energy. The deterministic comparison means both controls are fixed real numbers before observing the disturbance, not policies of the form \(u_1=\phi(x_1)\).

## Proof

**1. Exact moment description.** For every admissible policy put \(q=\mathbb Eu_0^2\ge0\), \(p=\mathbb Eu_1^2\ge0\), and \(c=\mathbb E[x_1u_1]\). The state equation and independence yield
\[
 \Sigma=\begin{pmatrix}s+hq&c\\c&q+p\end{pmatrix},\qquad
 c^2\le(s+hq)p,\qquad s+(1+h)q+p\le\beta.
\]
The inequality for \(c\) is Cauchy--Schwarz. Conversely, every pair \(q,p\ge0\) satisfying the budget can be realized with \(c=0\) by choosing independent centered inputs of those variances, also independent of the noise. No distributional assumption beyond finite second moments is needed.

**2. The causal/global optimum.** An exact inverse of a symmetric \(2\times2\) matrix gives
\[
 F(q,p,c)=\frac{2\eta+s+(1+h)q+p}{(\eta+s+hq)(\eta+q+p)-c^2}\ \ge\
 \frac1{\eta+s+hq}+\frac1{\eta+q+p}.
\]
Equality holds **exactly when** \(c=0\). For fixed \(q,p\), replacing \(u_1\) with a centered independent variable of equal second moment sets \(c=0\) without altering the budget. Moreover, with \(c=0\), increasing \(p\) strictly decreases the second reciprocal, so optimality forces \(s+(1+h)q+p=\beta\). Consequently the problem reduces exactly to
\[
 \min_{\,s\le S\le(s+h\beta)/(1+h)}
 \left(\frac1{\eta+S}+\frac1{\eta+\beta-S}\right),\qquad S=s+hq.
\]
The displayed function is strictly convex and symmetric about \(\beta/2\); its derivative is \(-1/(\eta+S)^2+1/(\eta+\beta-S)^2\). Therefore the unique optimal \(S\) is the clipped center \(S_*\), giving the claimed optimal covariance, moments, and value. Comparing the center with the interval endpoints gives the three timing regimes: \(\beta/2\le s\) exactly when \(\beta\le2s\); and \(\beta/2\ge(s+h\beta)/(1+h)\) is possible exactly when \(h<1\) and \(\beta\ge2s/(1-h)\).

**3. Deterministic open-loop criterion.** For prescribed real numbers \(u_0,u_1\), set \(q=u_0^2\), \(p=u_1^2\). Then \(c=b u_0u_1\) and \(c^2=hqp\). Thus
\[
 F_{\mathrm{open}}(q,p)=\frac{2\eta+s+(1+h)q+p}{(\eta+s+hq)(\eta+q+p)-hqp}.
\]
At fixed \(q\), the right-hand side is fractional-linear in \(p\), with a derivative of constant sign. Any optimum can therefore take either \(p=0\) or the maximum allowed \(p=\beta-s-(1+h)q\). Among cases \(p=0\), increasing \(q\) strictly reduces both reciprocals, so only the endpoint \(q=Q\) can be optimal. For the full-budget branch, the numerator is fixed at \(2\eta+\beta\), and its denominator simplifies **exactly** to
\[
 D(q)=(\eta+s)(\eta+\beta-s)+h q(q-s),\qquad 0\le q\le Q.
\]
Since \(D\) is strictly convex in \(q\), its maximum on this interval occurs only at \(q=0\) or \(q=Q\). Hence optimal fixed inputs never split energy between stages. The denominator difference is \(D(Q)-D(0)=hQ(Q-s)\), so the pure-stage switch occurs at \(Q=s\), or \(\beta=s(2+h)\); the end points tie there. The two endpoint reciprocal expressions are precisely the claimed formula.

**4. Exact separation and asymptotic sharpness.** Every globally optimal policy must realize the unique optimal diagonal information matrix. If \(q_*,p_*>0\), every prescribed nonzero pair has \(c^2=hq_*p_*>0\), so it cannot realize the required zero off-diagonal; the deterministic optimum is strictly worse by compactness and the preceding strict endpoint comparison. Conversely, if either moment is zero, the corresponding pure deterministic choice attains the causal optimum; this proves the exact gap criterion. For \(h>1\) and \(\beta\to\infty\), the causal optimum has \(S_*=\beta/2\), so \(F_*\sim4/\beta\). The deterministic switch eventually chooses \(q=Q\), so its two diagonal information eigenvalues are asymptotic to \(h\beta/(1+h)\) and \(\beta/(1+h)\), yielding \(F_{\mathrm{det}}\sim(1+h)^2/(h\beta)\). Dividing proves the asymptotic gap, which grows without bound with \(h\).

## Verification

An entirely exact-rational witness sets \(b=2\), \(s=1\), \(\eta=1\), and \(\beta=3\). The optimal independently randomized open-loop energies are \(q_*=1/8\), \(p_*=11/8\), giving \(\Sigma_*=\operatorname{diag}(3/2,3/2)\) and \(F_*=4/5\). Every prescribed deterministic open-loop pair has \(F\ge5/6\), attained by late-only control, yielding the exact positive gap \(1/30\). Run `python3 check.py` in the same directory; it verifies the witness and the sharp formulas in reproducible exact-rational parameter grids. The universal result is proved by the four steps above, not by these finite computations.

## Relationship to prior work

Bencherki, Lee, Matni, and Rantzer [1] introduce the general *nonlinear* trace-of-inverse covariance objective with arbitrary causal policies, establish convexity of feasible covariance sets, and propose a Frank--Wolfe method whose *linear* oracle is solved by Riccati steps. Their original formulation and Appendix 8.1 imply the moment-feasibility setting used here, but the inspected Sections 2--4 and Appendix do not state this exact two-stage nonlinear optimum, the three timing regimes, the fixed-input pure-stage theorem, or the unbounded gain-dependent comparison. The classical A-optimal inverse-information balancing principle is not asserted to be new: the contribution is its exact causal-versus-deterministic realization in this dynamical, state-plus-input-budget setting. Earlier work on time-domain experimental design [2], and adaptive A-optimal design [3], discusses different general designs and does not establish this displayed phase law in the material reviewed. An earlier exact two-step treatment of the *linearized* Riccati oracle does not imply the nonlinear criterion's optimal covariance or the fixed-input gap; the two optimization problems have different objectives. Bibliographic searches and the inspected materials cannot rule out every prior equivalent special case.

## Limitations

The theorem concerns a two-observation, scalar, exact-arithmetic, isotropically weighted inverse-covariance design with known dynamics. It is not a general multi-stage design rule, a theorem about empirical finite-sample Fisher information, or a guarantee under input-only budgets. The deterministic comparison excludes adaptive state-feedback and independent randomization; appropriately chosen deterministic nonlinear feedback may also attain the same covariance for some noise laws. General A-optimal diagonal information balancing is standard, and independent bibliographic validation of the exact dynamical comparison has not been performed.

## References

[1] F. Bencherki, B. Lee, N. Matni, and A. Rantzer, *Optimal input design via Frank--Wolfe*, arXiv:2609.08751v1, first posted 2026-09-08, Sections 2--4 and Appendix 8.1, https://arxiv.org/abs/2609.08751 . Accessible full-text transcription: https://documents.live/documents/display/Optimal-input-design-via-Frank-Wolfe .

[2] I. R. Manchester, *Input Design for System Identification via Convex Relaxation*, arXiv:1009.5614 (2010), https://arxiv.org/abs/1009.5614 . Abstract-level comparison only.

[3] C. Fohring and R. Haber, *Adaptive A-Optimal Experimental Design for Linear Dynamical Systems* (2016), bibliographic abstract inspected; see https://scholar.google.com/scholar?q=Adaptive+A-Optimal+Experimental+Design+for+Linear+Dynamical+Systems .
