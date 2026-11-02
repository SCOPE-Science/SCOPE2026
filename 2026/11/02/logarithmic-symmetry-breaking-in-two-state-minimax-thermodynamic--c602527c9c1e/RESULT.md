# Logarithmic symmetry breaking in two-state minimax thermodynamic mismatch

## Finding

Consider an irreducible continuous-time Markov process with two states, labelled fast and slow, and transition rates \(a>0\) (fast to slow) and \(b>0\) (slow to fast). Let \(X_0\) be the initial state, \(X_t\) the state at time \(t>0\), and \(q=\Pr(X_0=\mathrm{slow})\). Define the worst-case minimized thermodynamic mismatch cost for the finite-time channel by
\[
\mathcal F_t=\min_{Q}\max_P\{D(P\Vert Q)-D(P_t\Vert Q_t)\}
=\max_{0\le q\le1}H_q(X_0\mid X_t),
\]
where \(P_t,Q_t\) are the Markov-evolved laws, relative entropies and entropies use natural logarithms, and the first optimization is over full-support design priors \(Q\) (the same infimum results if its boundary is admitted). The minimax identity is an established starting point, independently rederived below for this binary channel. Its unique maximizing prior is denoted by \(q_t^*\).

**Fixed unequal rates.** Suppose \(a>b>0\), put \(\Delta=a-b\), and set \(L_t=\log(1/(\Delta t))\). As \(t\downarrow0\),
\[
q_t^* L_t\longrightarrow\frac{a}{\Delta},\qquad
\boxed{\mathcal F_t=a t\bigl(L_t-\log L_t\bigr)+o(t).}
\]
Thus the optimal probability of the *slower* state is asymptotically \(a/(\Delta L_t)\), not zero at any positive observation time. The subleading correction to the cost is a negative \(a t\log\log(1/t)\) term. If \(b>a\), exchange the state labels.

**Exactly balanced rates.** If \(a=b=\kappa>0\), then for every \(t>0\)
\[
q_t^*=\frac12,\qquad
\mathcal F_t=h\!\left(\frac{1-e^{-2\kappa t}}2\right)
=\kappa t\left[\log\frac1{\kappa t}+1\right]+o(t),
\]
where \(h(z)=-z\log z-(1-z)\log(1-z)\). In particular, the fixed-imbalance logarithm-of-logarithm correction disappears at rate symmetry.

**Near-symmetry boundary layer.** Fix \(\kappa>0\), \(\eta\ge0\), let \(L_t=\log(1/(\kappa t))\), and choose varying rates
\[
a_t=\kappa+\frac{\eta}{2L_t},\qquad b_t=\kappa-\frac{\eta}{2L_t}
\]
(for sufficiently small \(t\), so both rates are positive). Then \(q_t^*\to Q_\eta\in(0,1/2]\), the unique solution of
\[
\eta=\kappa\left[2\log\frac{1-Q_\eta}{Q_\eta}
 +\frac{1-2Q_\eta}{Q_\eta(1-Q_\eta)}\right].
\]
At \(\eta=0\), \(Q_0=1/2\). Defining
\[
G_\eta=\eta\left(\frac12-Q_\eta\right)
-\kappa(1-2Q_\eta)\log\frac{1-Q_\eta}{Q_\eta},
\]
one has the sharp crossover
\[
\boxed{\mathcal F_t=\kappa t L_t+\kappa t+tG_\eta+o(t).}
\]
Moreover \(Q_\eta\sim\kappa/\eta\) as \(\eta\to\infty\). All limits above are for the stated parameter families; no uniform joint remainder for unbounded \(\eta\) is asserted.

## Assumptions and scope

The process has the conservative generator (rows indexed by initial states)
\[
K=\begin{pmatrix}-a&a\\ b&-b\end{pmatrix}.
\]
The finite-time observation is the state, not the number or direction of jumps. The design mismatch is a KL-contraction loss, not the total housekeeping entropy production; a two-state chain is reversible at stationarity. The first asymptotic has fixed strictly unequal positive rates. The near-balanced asymptotic uses rates that vary with \(t\) exactly as specified, with fixed \(\kappa,\eta\).

## Proof

**1. Exact binary channel and strict optimizer.** Write
\[
u_t=\frac{a}{a+b}(1-e^{-(a+b)t}),\quad
v_t=\frac{b}{a+b}(1-e^{-(a+b)t}),\quad k_t=1-u_t-v_t=e^{-(a+b)t}.
\]
Here \(u_t\) is the fast-to-slow transition probability and \(v_t\) the reverse. The slow-state probability at time \(t\) is \(z_t(q)=u_t+k_tq\). By the chain rule for Shannon entropy,
\[
\Phi_t(q):=H_q(X_0\mid X_t)
=h(q)+(1-q)h(u_t)+qh(v_t)-h(z_t(q)).\tag{1}
\]
Its derivative is
\[
\Phi_t'(q)=\log\frac{1-q}{q}-h(u_t)+h(v_t)
-k_t\log\frac{1-z_t(q)}{z_t(q)}.\tag{2}
\]
Furthermore,
\[
\Phi_t''(q)=-\frac1{q(1-q)}+\frac{k_t^2}{z_t(q)(1-z_t(q))}<0,
\]
because the law of total variance gives
\[
z_t(q)(1-z_t(q))=k_t^2q(1-q)
+(1-q)u_t(1-u_t)+qv_t(1-v_t)>k_t^2q(1-q).
\]
For every finite \(t>0\), the maximum is strictly interior (both boundary conditional entropies are zero, while any interior value is positive), hence unique and characterized by \(\Phi_t'(q_t^*)=0\).

For completeness, the minimax identity need not be taken as an unverified assumption. For a full-support prior \(Q\), let \(M(P,Q)=D(P\Vert Q)-D(P_t\Vert Q_t)\) and let \(e_i\) denote a point mass at initial state \(i\). Direct expansion gives
\[
M(P,Q)=\sum_iP_iM(e_i,Q)-H_P(X_0\mid X_t).
\]
Since conditional entropy is nonnegative, \(\sup_PM(P,Q)=\max_iM(e_i,Q)\). At the interior maximizer \(Q^*\) of conditional entropy, its partial derivatives in the unconstrained positive coordinates are equal and coincide with \(\mathcal F_t\); these derivatives are exactly \(M(e_i,Q^*)\). Hence \(\max_iM(e_i,Q^*)=\mathcal F_t\). For any other \(Q\), averaging \(M(e_i,Q)\) with weights \(Q_i^*\) gives \(\mathcal F_t+M(Q^*,Q)\ge\mathcal F_t\) by KL data processing. This proves the equality of the two optimization problems and identifies the same prior.

**2. Fixed asymmetry.** Assume \(a>b\). For a fixed \(c>0\), put \(q=c/L_t\). The entropy expansions \(h(w)=w[\log(1/w)+1]+O(w^2)\) as \(w\downarrow0\), the rate expansions \(u_t=at+O(t^2)\), \(v_t=bt+O(t^2)\), and the mean-value theorem applied in (2) yield
\[
\frac{\Phi_t'(c/L_t)}{tL_t}\longrightarrow\frac ac-\Delta.
\tag{3}
\]
For any fixed \(c_-<a/\Delta<c_+\), (3) makes the derivative positive at \(c_-/L_t\) and negative at \(c_+/L_t\) for sufficiently small \(t\). Strict concavity then gives
\[
q_t^*=\frac a{\Delta L_t}(1+o(1)).\tag{4}
\]
Uniformly for \(q\) between such two constant multiples of \(1/L_t\), a Taylor expansion of \(h(z_t(q))\) around \(q\) has remainder \(O(t^2/q)=o(t)\). In (1), using \(q\log(1/q)=o(1)\) and \(q=O(1/L_t)\), we obtain
\[
\frac{\Phi_t(q)}t=
 a\log\frac1t+a(1-\log a)
 -\Delta q\log\frac1t-a\log\frac1q+o(1).\tag{5}
\]
Substitute (4) into (5). Since \(\Delta q_t^*L_t\to a\) and \(\log(1/q_t^*)=\log L_t+\log(\Delta/a)+o(1)\), the constant terms cancel, giving \(\Phi_t(q_t^*)/t=a(L_t-\log L_t)+o(1)\). Time units cancel inside the dimensionless \(\Delta t\).

**3. Exact symmetry.** When \(a=b=\kappa\), one has \(u_t=v_t\); (1) is invariant under \(q\mapsto1-q\). By strict concavity, the unique maximum is \(q=1/2\), and its value is \(h(u_t)\). The small-argument binary-entropy expansion completes this case.

**4. Symmetry-breaking crossover.** Let \(a_t,b_t\) vary as in the finding. For every compact subinterval of \((0,1)\), Taylor expansion of (1) is uniform in \(q\), and yields
\[
\frac{\Phi_t(q)}t-\kappa L_t-\kappa
\longrightarrow g_\eta(q)
=\eta\left(\frac12-q\right)-\kappa(1-2q)\log\frac{1-q}q.\tag{6}
\]
The corresponding first-derivative convergence is also uniform on compact subsets. Direct differentiation gives
\[
g_\eta'(q)=-\eta+\kappa\left[2\log\frac{1-q}q+\frac{1-2q}{q(1-q)}\right],
\]
\[
g_\eta''(q)=-\kappa\left[\frac4{q(1-q)}+\frac{(1-2q)^2}{q^2(1-q)^2}\right]<0.
\]
As \(q\) approaches either boundary, \(g_\eta(q)\to-\infty\); its unique maximizer \(Q_\eta\) obeys the displayed equation. Choose interior points on opposite sides of \(Q_\eta\) where \(g_\eta'\) has opposite signs. Their derivatives for \(\Phi_t\) have those same signs for small \(t\), so strict concavity traps \(q_t^*\) in a fixed compact interval and forces \(q_t^*\to Q_\eta\). Equation (6) then yields the stated cost expansion. The defining equation at large \(\eta\) has dominant contribution \(\kappa/Q_\eta\), showing \(\eta Q_\eta/\kappa\to1\).

## Verification

The bundled program `verification/minimax_verifier.py` uses high-precision decimal arithmetic and separately evaluates the exact joint-distribution conditional entropy, the channel formula, strict optimizer equation, symmetric identity, fixed-gap asymptotics and near-symmetry crossover. It passed 76 deterministic checks on the bundled source. Tests are supplementary and are not substituted for Steps 1–4 of the proof.

## Relationship to prior work

Yousef, Ansbacher and Wolpert (2026), arXiv:2610.03478, establish the general finite-time identity between minimax mismatch and maximal conditional initial-state entropy, as well as the leading law \(\mathcal F_t\sim\lambda_{\max}t\log(1/t)\) for finite irreducible chains, and concentration on largest-exit-rate states. Their main text and Appendix SX were inspected for the stated input/rate/time objects. They do not state the coefficient of \(t\log\log(1/t)\), the \(1/\log(1/t)\) mass law, or the near-symmetric crossover above. The present theorem credits their general result and concerns a sharp, explicitly solvable refinement for two states.

Khouzani and Malacaria (2018), DOI:10.3390/e20090675, study robust information leakage by optimizing the *channel under constraints for a given input prior*. Their problem is distinct from maximizing posterior entropy over the initial distribution of a fixed continuous-time Markov channel; it does not cover these small-time rate-splitting formulas. Standard binary-channel calculus is not claimed as new.

## Limitations

The result concerns a two-state, time-homogeneous chain; it makes no higher-state universality claim. Fixed-rate and near-balanced expansions are pointwise in their declared parameter families. The coefficient of the leading term and the minimax representation were already known. This result does not quantify the total entropy production of a particular physical implementation or imply that an arbitrary design prior is physically realizable. Publication priority beyond the inspected literature is not independently certified.

## References

1. M. Yousef, B. Ansbacher and D. H. Wolpert, *Minimax entropy production for arbitrary processes*, arXiv:2610.03478, first publicly submitted 2026-10-02. https://arxiv.org/abs/2610.03478 ; full text https://arxiv.org/html/2610.03478 .
2. M. H. R. Khouzani and P. Malacaria, *Optimal Channel Design: A Game Theoretical Analysis*, Entropy 20 (2018), 675, DOI:10.3390/e20090675; https://pmc.ncbi.nlm.nih.gov/articles/PMC7513200/ .
