# A singular near-segregation layer in the two-risk epidemic threshold

## Finding

In the two-risk configuration-model epidemic-percolation kernel below, a small transmission-risk contrast \(\delta\) has a **discontinuous first-order effect at perfect assortativity**. For every fixed excess-degree factor \(\kappa>1\), high-risk share \(0<p<1\), risk split \(0\le s\le1\), and scaled segregation distance \(\tau\ge0\), let \(h=1-\tau\delta\), \(\alpha_S=(1+\delta)^s\), and \(\alpha_I=(1+\delta)^{1-s}\). Then the exact positive percolation threshold satisfies

\[
t_c(\delta,1-\tau\delta)=t_0-\frac{\delta}{\kappa-1}G_{p,q_0}(\tau)+O(\delta^2),
\qquad t_0=\log\frac{\kappa}{\kappa-1},\quad q_0=(\kappa-1)t_0,
\]
\[
G_{p,q}(\tau)=\frac{q-\tau+\sqrt{(q-\tau)^2+4pq\tau}}{2}.
\]
The \(O(\delta^2)\) assertion is for \(\delta\downarrow0\) with the displayed parameters fixed, and holds uniformly when \(\tau\) stays in a compact set. The function \(G_{p,q_0}\) decreases strictly from \(q_0\) to \(pq_0\) as \(\tau\) runs from zero to infinity. In particular the sensitivity limits do not commute:

\[
\lim_{h\uparrow1}\lim_{\delta\downarrow0}
\frac{t_c(\delta,h)-t_0}{\delta}=-p t_0,
\qquad
\lim_{\delta\downarrow0}\lim_{h\uparrow1}
\frac{t_c(\delta,h)-t_0}{\delta}=-t_0.
\]
For the source's trace-only small-transmissibility approximation, a separate corollary gives a precisely bounded, potentially twofold underestimation of the true threshold even when \(\kappa\) tends to infinity; the source's **exact** determinant equation is not challenged.

## Assumptions and scope

There are two risk classes \(L,H\), with \(0<p<1\) of individuals in class \(H\), positive susceptibility and infectivity multipliers \(\alpha_S,\alpha_I\ge1\), and assortativity \(0\le h\le1\). The row-stochastic contact-type matrix is

\[
\Pi(h)=(1-h)\begin{pmatrix}1-p&p\\1-p&p\end{pmatrix}+hI_2.
\]
For \(t=\beta/\gamma\ge0\), the two-type edge-transmission kernel and its Perron root are

\[
F(t)=\begin{pmatrix}
\pi_{LL}(1-e^{-t})&\pi_{LH}(1-e^{-\alpha_I t})\\
\pi_{HL}(1-e^{-\alpha_S t})&\pi_{HH}(1-e^{-\alpha_S\alpha_I t})
\end{pmatrix},\qquad R(t)=\rho(F(t)).
\]
Here \(\kappa=g_1'(1)>1\) is the finite excess-degree mean of the configuration-model degree distribution. Define \(t_c\) as the unique \(t>0\) satisfying \(\kappa R(t)=1\); this is the percolation onset criterion from the cited model, including at \(h=1\) where onset means a giant component in at least one of the two positive-proportion groups. The theorem concerns this mathematical percolation criterion, not epidemic prevalence in a finite population. The perturbative law fixes \(s\in[0,1]\) and writes \(\alpha_S=(1+\delta)^s\), \(\alpha_I=(1+\delta)^{1-s}\).

## Proof

**Existence and uniqueness.** Every entry of \(F(t)\) is nondecreasing in \(t\); all nonzero entries increase strictly. For \(h<1\) the matrix is positive for \(t>0\), and Perron monotonicity makes \(R(t)\) strictly increasing. At \(h=1\) it is diagonal and its maximum diagonal entry also strictly increases. It ranges from zero to one, because \(F(\infty)=\Pi(h)\). Since \(\kappa>1\), the threshold is uniquely defined.

**Degenerate near-segregation perturbation.** Put \(f(t)=1-e^{-t}\) and \(q(t)=t e^{-t}/f(t)\). For fixed \(\tau\), \(h=1-\tau\delta\) and \(\alpha_S\alpha_I=1+\delta\), entrywise Taylor expansion yields

\[
F(t)=f(t)\left[I_2+\delta K_{p,q(t)}(\tau)+O(\delta^2)\right],\quad
K_{p,q}(\tau)=\begin{pmatrix}-\tau p&\tau p\\
\tau(1-p)&q-\tau(1-p)\end{pmatrix}.
\]
The off-diagonal transmission-rate perturbations have no first-order effect because the off-diagonal contact weights are already \(O(\delta)\); hence the leading law is independent of the risk split \(s\). The characteristic polynomial of \(K\) is \(\lambda^2-(q-\tau)\lambda-pq\tau\). Its simple largest eigenvalue is \(G_{p,q}(\tau)\), also at \(\tau=0\) since \(q>0\). Thus

\[
R(t)=f(t)\bigl(1+\delta G_{p,q(t)}(\tau)+O(\delta^2)\bigr).
\]
At \(\delta=0\) the critical value is \(t_0\), with \(f(t_0)=1/\kappa\), \(\kappa f'(t_0)=\kappa-1\) and \(q(t_0)=q_0\). Substitution into \(\kappa R(t_c)=1\) yields the asserted threshold shift. On compact \(\tau\)-sets the simple eigenvalue is separated from the other eigenvalue at each fixed parameter tuple, justifying the uniform Taylor bound.

**Monotone crossover and noncommuting sensitivities.** The positive eigenvalue solves \(G^2-(q-\tau)G-pq\tau=0\). It satisfies \(G(0)=q\), \(G(\tau)>pq\) for every finite \(\tau\), and

\[
G'(\tau)=\frac{pq-G(\tau)}{2G(\tau)+\tau-q}<0.
\]
Dividing its quadratic by \(\tau\) as \(\tau\to\infty\) gives \(G(\tau)\to pq\). For every fixed \(h<1\), \(\Pi(h)\) has simple unit Perron eigenvalue with left stationary vector \((1-p,p)\) and right eigenvector \((1,1)\). First-order perturbation in \(\delta\), using \(\alpha_S'(0)=s\), \(\alpha_I'(0)=1-s\), gives the scalar coefficient

\[
(1-p)\pi_{LH}(1-s)+p\pi_{HL}s+p\pi_{HH}=p.
\]
Therefore \(R(t)=f(t)+\delta p t e^{-t}+O(\delta^2)\), so \(\lim_{\delta\downarrow0}(t_c(\delta,h)-t_0)/\delta=-pt_0\), independently of fixed \(h<1\). At \(h=1\), \(F(t)\) is diagonal, and its higher-risk entry gives exactly \(t_c(\delta,1)=t_0/(1+\delta)\). Taking limits in the stated orders proves the mismatch because \(p<1\).

**The trace-only threshold bias.** For fixed \(p,h,\alpha_S,\alpha_I\), put \(\alpha=\alpha_S\alpha_I\), \(\theta=\pi_{LL}+\alpha\pi_{HH}\). The low-transmissibility coefficient matrix is

\[
B=\begin{pmatrix}\pi_{LL}&\alpha_I\pi_{LH}\\\alpha_S\pi_{HL}&\alpha\pi_{HH}\end{pmatrix},
\qquad\det B=\alpha h,
\qquad r=\rho(B)=\frac{\theta+\sqrt{\theta^2-4\alpha h}}2.
\]
The product identity \(\det\Pi=h\) proves the determinant formula. Taylor expansion \(F(t)=tB+O(t^2)\) gives \(t_c\sim1/(\kappa r)\) as \(\kappa\to\infty\). Dropping the quadratic determinant term instead gives the source's displayed trace-only expression \(t_{\rm tr}=1/(\kappa\theta)\). Since \(B\) has positive trace and nonnegative determinant, its two eigenvalues are nonnegative, giving

\[
1\le \lim_{\kappa\to\infty}\frac{t_c}{t_{\rm tr}}=\frac{\theta}{r}\le2,
\]
with strict left inequality for \(h>0\). The factor \(2\) is attained in the neutral fully segregated case \(\alpha_S=\alpha_I=1\), \(h=1\), where \(B=I_2\); the bound is sharp also when approaching that case from \(\alpha>1\). Under neutral risk for any \(h\), \(F(t)=f(t)\Pi(h)\) and the exact threshold is \(t_0\), independently of homophily. Thus the trace-only formula is not uniformly accurate in \(\kappa\) at positive homophily, although the original exact equation remains valid.

## Verification

The included standalone program `verify_threshold.py` uses only the Python standard library. It directly constructs the finite-transmissibility \(2\times2\) Jacobian, computes its Perron root from the characteristic polynomial, and bisects the *exact* onset equation without replacing finite edge-transmission probabilities by their linear approximations. It checks 405 base parameter sets at multiple network excess degrees, exact rational determinant identities, neutral cases, small-risk/strong-segregation crossover predictions, and fixed-h sensitivity limits. The program prints the number of successful numerical/rational assertions; its finite-grid comparisons are not a proof of the quantified asymptotic statements. Run `python verify_threshold.py` from the directory containing this document.

## Relationship to prior work

Mazza et al. (2026) introduce the two-risk HeSIR network construction, its \(\Pi(h)\), the exact determinant threshold (main Eq. (3), Appendix Eq. (A4)), and the trace-only small-\(t\) expression (main Eq. (4), Appendix Eq. (A5)). Their full preprint presents the threshold equation and numerical comparisons, not the singular \(1-h\asymp\delta\) window, noncommuting near-neutral sensitivities, or the sharp twofold bound on the trace-only approximation in the degree-asymptotic regime. The theorem retains their exact onset criterion and derives a parameter-space boundary-layer law from it. General two-group SIR reproduction-number and positive-matrix spectral-radius methods predate the paper; no novelty is claimed for those tools. The first confirmed public appearance of the primary paper was the journal issue on 2026-01-08, preceding its arXiv upload on 2026-01-29.

## Limitations

The theorem applies to the idealized configuration-model bond-percolation criterion, fixed \(\kappa>1\), and precisely specified small risk contrasts. Its crossover asymptotics are uniform for bounded \(\tau\), not claimed uniformly over all growing \(\tau\). The trace-only bound concerns \(\kappa\to\infty\) with risk parameters fixed and should not be confused with the fixed-\(\kappa\) boundary layer. Generalization to finite-size networks, evolving behavior, degree-correlated risk types, and nonlinear epidemic trajectories is not established. The fully reviewed preprint is dated later than the journal's initial public issue; possible intervening textual differences and unindexed equivalent perturbation analyses remain residual literature risks.

## References

1. Fabio Mazza, Gabriele Ricci, Francesca Colaiori, Stefano Guarino, Sandro Meloni, and Fabio Saracco, *Impact of behavioral heterogeneity on epidemic outcome and its mapping into effective network topologies*, Physical Review E **113**, 014306 (published January 8, 2026), DOI: 10.1103/xps9-qqvp. Open preprint: https://arxiv.org/abs/2601.21743 (submitted January 29, 2026), inspected main §II and Appendix A.
2. P. Magal, O. Seydi, and G. F. Webb, *Final Size of an Epidemic for a Two-Group SIR Model* (2016), background on two-group epidemic threshold analysis; this work is not asserted to cover or not cover the present singular scaling without full-text comparison.
