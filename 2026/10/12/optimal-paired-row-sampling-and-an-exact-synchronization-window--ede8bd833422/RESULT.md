# Optimal paired-row sampling and an exact synchronization window in factorized Kaczmarz

## Finding

Consider the two-stage randomized Kaczmarz (RK–RK) iteration for a factored diagonal system. Keep the prescribed norm-squared sampling distribution for **each** factor, but permit correlation between the two row labels chosen in the same iteration. There exists a coupling that is componentwise optimal for **every** finite horizon and **every** right-hand side: maximize the probability that both stages select the same coordinate. More precisely, let \(\pi_{ij}=\Pr(J=i,I=j)\) have marginals \(p_i\) and \(q_i\). At every integer time \(t\geq 0\), the exact squared-error law is

\[
\mathbb E\|z_t-z_\star\|_2^2
 =\sum_{i=1}^m (z_{\star,i})^2\left[(1-p_i)^t +(p_i-\pi_{ii})\sum_{s=1}^t(1-p_i)^{s-1}(1-q_i)^{t-s}\right].
\]

For every positive integer \(t\), this expectation is simultaneously minimized, for all right-hand sides, by any coupling satisfying \(\pi_{ii}=\min(p_i,q_i)\) for each \(i\). Such a coupling always exists. The independent two-stage sampling of the original RK–RK algorithm is strictly worse for every nonzero right-hand side and each \(t\geq1\).

For the balanced family \(A=B=I_m\), \(y=\boldsymbol{1}\), and a mixture that synchronizes row labels with probability \(\theta_m\in[0,1]\) and samples them independently otherwise, the exact law is

\[
\mathbb E\|z_t-\boldsymbol{1}\|_2^2
=m\left(1-\frac1m\right)^t\left(1+(1-\theta_m)\frac tm\right).
\]

Define \(\varepsilon_m=1-\theta_m\), \(L_m=\log m\), and let \(c_m\) denote the unique real solution \(c_m\geq L_m\) of

\[
c_m-\log(1+\varepsilon_m c_m)=L_m.
\]

Uniformly over every sequence \(\theta_m\in[0,1]\) and every fixed real \(s\), with \(t_m=\lfloor m(c_m+s)\rfloor\),

\[
\mathbb E\|z_{t_m}-\boldsymbol{1}\|_2^2\longrightarrow e^{-s},
\qquad
c_m=\log m+\log\bigl(1+(1-\theta_m)\log m\bigr)+o(1).
\]

Thus the absolute mean-square threshold is at \(m\log m\) under fully synchronized sampling, at \(m(\log m+\log\log m+\log(1-\theta))+o(m)\) for any fixed \(\theta<1\), and at \(m(\log m+\log(1+\lambda))+o(m)\) when \((1-\theta_m)\log m\to\lambda\in[0,\infty)\). These statements concern **absolute squared error**, not mean per-coordinate error or a random stopping-time distribution.

## Assumptions and scope

Fix \(m\geq2\). Let \(A=\operatorname{diag}(a_1,\ldots,a_m)\) and \(B=\operatorname{diag}(b_1,\ldots,b_m)\), with every \(a_i,b_i\) real and nonzero. For any \(y\in\mathbb R^m\), the target is \(z_{\star,i}=y_i/(a_i b_i)\). Initialize both intermediate and output vectors to zero. Set

\[
p_i=\frac{a_i^2}{\sum_j a_j^2},\qquad
q_i=\frac{b_i^2}{\sum_j b_j^2}.
\]

Draw independent-in-time ordered pairs \((J_t,I_t)\), each with one fixed joint probability matrix \(\pi\) whose first and second marginals are \(p\) and \(q\). After the row \(J_t\) update to the intermediate vector \(x_t\), use that **updated** intermediate vector in the row \(I_t\) update to \(z_t\). Explicitly,

\[
x_{t,J_t}=y_{J_t}/a_{J_t},\qquad
z_{t,I_t}=x_{t,I_t}/b_{I_t},
\]

with all other coordinates unchanged. The published standard RK–RK sampler is the special case \(\pi_{ij}=p_iq_j\). The correlated samplers here retain each stage's original norm-squared marginal but are a variant of that published algorithm.

## Proof

**1. Coordinate completion.** Fix \(i\). Once row \(J=i\) is selected, the intermediate coordinate permanently equals \(y_i/a_i\). The output coordinate permanently equals its target the first time row \(I=i\) is selected **in the same iteration or later**. Before this event the output coordinate is exactly zero, even if the second-stage row was selected earlier. The probability that \(J=i\) never occurs in the first \(t\) iterations is \((1-p_i)^t\). If the first selection \(J=i\) occurs at iteration \(s\), there is a joint probability \((1-p_i)^{s-1}(p_i-\pi_{ii})\) that \(I\ne i\) then, followed by probability \((1-q_i)^{t-s}\) of seeing no \(I=i\) later. These disjoint alternatives yield the displayed exact error law. For \(t=0\), the sum is empty. For \(t\geq1\), the convolution multiplying \(p_i-\pi_{ii}\) is strictly positive, since \(0<p_i,q_i<1\).

**2. Simultaneous optimality.** Any joint distribution with marginals \(p,q\) obeys the Fréchet bound \(\pi_{ii}\leq\min(p_i,q_i)\). Write \(c_i=\min(p_i,q_i)\) and \(r=1-\sum_i c_i\). When \(r>0\), set

\[
\pi^{\max}_{ij}=c_i\boldsymbol{1}_{\{i=j\}}
 +\frac{(p_i-c_i)(q_j-c_j)}r.
\]

When \(r=0\), set \(\pi^{\max}_{ij}=c_i\boldsymbol{1}_{\{i=j\}}\). The specified table has marginals \(p,q\) because the leftover row and column masses each total \(r\); its additional diagonal mass is zero because for every \(i\) either \(p_i-c_i=0\) or \(q_i-c_i=0\). Hence \(\pi^{\max}_{ii}=c_i\) simultaneously. The formula from step 1 is strictly decreasing in each diagonal mass at every positive \(t\) whenever \(z_{\star,i}\ne0\), proving the optimality for every right-hand side and time. Under independent sampling, \(p_iq_i<\min(p_i,q_i)\) for all \(i\), proving strict improvement for every nonzero \(y\).

**3. Exact balanced law.** In the balanced case \(p_i=q_i=1/m\). A synchronous/independent mixture gives

\[
\pi_{ii}=\frac{\theta_m}{m}+\frac{1-\theta_m}{m^2},\qquad
p_i-\pi_{ii}=\frac{(1-\theta_m)(m-1)}{m^2}.
\]

The finite convolution has exactly \(t\) identical terms, each equal to \((1-1/m)^{t-1}\). Substituting and summing over \(m\) target coordinates gives the stated identity for every nonnegative integer \(t\).

**4. Uniform transition window.** The function \(F_m(c)=c-\log(1+\varepsilon_m c)\) is strictly increasing for \(c\geq L_m\), since \(F_m'(c)=1-\varepsilon_m/(1+\varepsilon_m c)>0\). It satisfies \(F_m(L_m)\leq L_m\) and diverges as \(c\to\infty\), so the root exists uniquely. The root equation implies

\[
c_m-L_m=\log(1+\varepsilon_m c_m).
\]

Uniformly in \(\varepsilon_m\in[0,1]\), this difference is \(O(\log L_m)\): indeed it is at most \(\log(1+c_m)\), and the root lies below \(L_m+2\log(1+L_m)\) for all sufficiently large \(m\). Therefore

\[
0\leq c_m-L_m-\log(1+\varepsilon_m L_m)
=\log\!\left(1+\frac{\varepsilon_m(c_m-L_m)}{1+\varepsilon_m L_m}\right)
\leq\frac{c_m-L_m}{L_m}\longrightarrow0
\]

uniformly, where the upper bound follows from \(\varepsilon_m/(1+\varepsilon_m L_m)\leq1/L_m\).

For \(t_m=\lfloor m(c_m+s)\rfloor\), the expansion \(\log(1-1/m)=-1/m+O(m^{-2})\) is uniform and \(c_m=O(\log m+\log\log m)\). The exact balanced identity and the root equation now give

\[
\mathbb E\|z_{t_m}-\boldsymbol{1}\|_2^2
=e^{-s}\left(1+\frac{\varepsilon_m s}{1+\varepsilon_m c_m}\right)+o(1)
=e^{-s}+o(1),
\]

uniformly in the mixture parameter. The asserted regimes follow by substituting the uniform center expansion; for fixed \(\theta<1\), \(\log(1+(1-\theta)\log m)=\log\log m+\log(1-\theta)+o(1)\).

## Verification

The standalone Python 3 script `verify.py` reconstructs the two successive source updates with exact rational arithmetic and exhaustively enumerates every row-pair path in several small diagonal systems. It checks the componentwise formula under independent, maximal, and intermediate couplings, verifies both joint marginals and strict dominance, and tests the balanced identity over multiple dimensions, horizons, and mixture parameters. The verification also computes the finite-dimensional transition location and checks its analytically derived first-order finite-size correction. Run with `python3 verify.py`; no third-party packages are needed. The finite checks corroborate, but do not replace, the all-dimensions proof above.

## Relationship to prior work

Ma, Needell, and Ramdas introduce the interlaced RK–RK updates and obtain convergence bounds for independently sampled factor rows [1]. Du analyzes regularized variants and recovers RK–RK as a special case [2]. Those results supply the iteration being studied; their analyzed bounds do not give the coupling-dependent exact coordinate error or the all-horizon optimal joint law proved here. The diagonal construction uses the classical Fréchet bound for couplings as a proof tool; that bound itself is not claimed as new. The additional \(\log\log m\) absolute mean-square delay is specific to independent two-stage completion and does not assert a new general coupon-collector theorem.

## Limitations

The optimality holds **only** for nonzero real diagonal factors, zero initialization, one fixed i.i.d.-in-time pair coupling, and preservation of the original row-sampling marginals. It does not claim superiority for general nonorthogonal matrices, nonzero initialization, adaptive sampling, other loss functions, or wall-clock performance. The absolute squared-error transition is not an almost-sure stopping-time theorem. The literature comparison cannot rule out equivalent arguments in unindexed publications.

## References

[1] Anna Ma, Deanna Needell, and Aaditya Ramdas. *Iterative methods for solving factorized linear systems*. arXiv:1701.07453, first posted 25 January 2017. https://arxiv.org/abs/1701.07453 . See Section 4, Algorithm 1 and the convergence results.

[2] Kui Du. *Regularized randomized iterative algorithms for factorized linear systems*. arXiv:2204.10722, first posted 22 April 2022. https://arxiv.org/abs/2204.10722 . See Section 3 and Algorithm 4.
