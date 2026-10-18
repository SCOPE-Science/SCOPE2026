# A cumulative-mutation threshold for critical three-species competition

## Finding

For the cyclic, symmetric-mutation May–Leonard competition system on the neutral interaction line \(\alpha+\beta=2\), the **total accumulated mutation**, rather than its instantaneous intensity, makes an exact qualitative distinction. Let \(p_i(t)\) be the proportion of species \(i\) in the total population and let \(u=(1/3,1/3,1/3)\). For every nonuniform strictly positive initial composition and every measurable nonnegative locally integrable mutation rate \(\mu\), write \(M(t)=\int_0^t\mu(s)\,ds\). Then:

1. If \(M(\infty)=\infty\), all three species densities converge to \(1/3\); for the relative entropy \(H(t)=\frac13\sum_i\log[1/(3p_i(t))]\),
\[
H(t)\le H(0)e^{-3M(t)},\qquad
\lim_{t\to\infty}\frac{\log(H(t)/H(0))}{M(t)}=-6.
\]
2. If \(M(\infty)<\infty\) and \(\alpha\ne\beta\), the entropy converges to a **strictly positive** value \(h_\infty\). The omega-limit set of the full species-density trajectory is precisely the nontrivial closed periodic curve
\[
\left\{m\in(0,\infty)^3:\ \sum_i m_i=1,\ \frac13\sum_i\log\frac{1}{3m_i}=h_\infty\right\}.
\]
In particular, the population keeps visiting distinct nonuniform compositions at arbitrarily late times. The limit set is that of an unmutated periodic orbit; the time-dependent population itself need not be periodic.

These alternatives are exhaustive. As a sharp illustrative family, when \(\mu(t)=a(1+t)^{-q}\), with \(a,q>0\), homogenization occurs exactly for \(q\le1\), and a nontrivial periodic omega-limit occurs for \(q>1\). For \(q=1\), \(H(t)=t^{-6a+o(1)}\).

## Assumptions and scope

Take real parameters \(0<\alpha<2\), \(\beta=2-\alpha\), and \(\alpha\ne1\). Let \(m_i(0)>0\), and let \(\mu:[0,\infty)\to[0,\infty)\) be measurable and locally integrable. Consider the unique forward Carathéodory solution to the equations
\[
\begin{aligned}
\dot m_1&=m_1(1-m_1-\alpha m_2-\beta m_3)+\mu(t)(m_2+m_3-2m_1),\\
\dot m_2&=m_2(1-\beta m_1-m_2-\alpha m_3)+\mu(t)(m_1+m_3-2m_2),\\
\dot m_3&=m_3(1-\alpha m_1-\beta m_2-m_3)+\mu(t)(m_1+m_2-2m_3).
\end{aligned}
\]
The mutation term represents symmetric exchange among all three populations; neither boundedness nor monotonicity of \(\mu(t)\) is assumed. Let \(S=\sum_i m_i\), \(p_i=m_i/S\), and \(u_i=1/3\). The nonuniform-initial-composition condition means \(p(0)\ne u\). The exceptional uniform composition stays uniform for every mutation schedule and is not part of the nontrivial-curve conclusion.

## Proof

**1. Logistic population and invariant interior.** The interaction matrix is
\[
A=\begin{pmatrix}1&\alpha&\beta\\\beta&1&\alpha\\\alpha&\beta&1\end{pmatrix},
\qquad A+A^{\mathsf T}=2\mathbf1\mathbf1^{\mathsf T}.
\]
Since mutation fluxes sum to zero and \(m^{\mathsf T}Am=S^2\), the total obeys
\[
\dot S=S(1-S),\qquad
S(t)=\frac{S(0)}{S(0)+(1-S(0))e^{-t}}\longrightarrow1.
\]
The positive orthant is forward invariant: at a coordinate-zero boundary, its mutation influx is nonnegative, and on finite time intervals each positive coordinate has a Grönwall lower bound from its own loss terms. The logistic formula bounds the total and gives global existence. Normalizing gives the exact proportion system, with cyclic indices,
\[
\dot p_i=-S(t)(\alpha-1)p_i(p_{i+1}-p_{i-1})+\mu(t)(1-3p_i).
\tag{1}
\]
The indices \(i+1\) and \(i-1\) are interpreted modulo three.

**2. Exact entropy dissipation.** Define
\[
H(p)=-\frac13\sum_{i=1}^3\log(3p_i),\qquad
D(p)=\frac13\left(\sum_{i=1}^3\frac1{p_i}-9\right).
\]
The competitive part of (1) contributes zero to \(\sum_i\dot p_i/p_i\); the mutation part gives the **exact identity**
\[
\frac{d}{dt}H(p(t))=-\mu(t)D(p(t))\quad\text{a.e.}\tag{2}
\]
Both \(H\) and \(D\) are nonnegative and vanish only at \(u\). Setting \(q_i=3p_i\), and using \(q_i^{-1}-1+\log q_i\ge0\) for each positive \(q_i\), yields
\[
D(p)-3H(p)=\sum_{i=1}^3(q_i^{-1}-1+\log q_i)\ge0.\tag{3}
\]
Thus \(H(t)\le H(0)\exp[-3M(t)]\), and every trajectory remains in the compact interior entropy sublevel \(K=\{H\le H(0)\}\). For \(H(0)>0\), the ratio \(D/H\) extends continuously to \(u\): Taylor expansion with \(p_i=1/3+\delta_i\) and \(\sum_i\delta_i=0\) gives
\[
H=\frac32\sum_i\delta_i^2+O(\|\delta\|^3),\qquad
D=9\sum_i\delta_i^2+O(\|\delta\|^3),\qquad
\lim_{p\to u}\frac{D(p)}{H(p)}=6.\tag{4}
\]
Consequently, \(D/H\le C(H(0))<\infty\) on \(K\setminus\{u\}\), while (3) gives a lower bound of three. Integrating (2) yields
\[
H(0)e^{-C(H(0))M(t)}\le H(t)\le H(0)e^{-3M(t)}.\tag{5}
\]
In particular, for nonuniform initial data, \(H(t)>0\) at each finite time, and all three proportions remain strictly positive.

**3. Infinite cumulative mutation.** If \(M(t)\to\infty\), the upper estimate in (5) forces \(H(t)\to0\) and hence \(p(t)\to u\). The logistic convergence gives \(m_i(t)\to1/3\). By (4), \(D(p(t))/H(p(t))\to6\). Since
\[
\log\frac{H(t)}{H(0)}=-\int_0^t\mu(s)\frac{D(p(s))}{H(p(s))}\,ds,
\]
dividing by the diverging \(M(t)\) and applying weighted Cesàro convergence proves the displayed sharp logarithmic exponent \(-6\), even for intermittent mutation pulses.

**4. Finite cumulative mutation.** If \(M(\infty)<\infty\), monotonicity of \(H\) and the lower estimate (5) give \(H(t)\to h_\infty>0\). The compactness of \(K\) makes the omega-limit set nonempty, and every accumulation point lies on the level \(H=h_\infty\). Strict convexity of \(H\) on the open two-simplex and its divergence on the boundary imply that this positive level is a smooth, simple, closed curve surrounding \(u\).

Let \(F_i(p)=-(\alpha-1)p_i(p_{i+1}-p_{i-1})\). It is tangent to every entropy level and, because \(\alpha\ne1\), has no zero in the interior except \(u\). Hence its restriction to \(H=h_\infty\) is a nowhere-vanishing tangent field: the entire level is one periodic orbit of \(\dot p=F(p)\).

It remains to establish that this **entire** periodic orbit is the omega-limit, rather than just some subset. For any sequence \(t_j\to\infty\) with \(p(t_j)\to q\), equation (1), \(S(t_j+s)\to1\) uniformly for bounded \(s\), and
\[
\int_{t_j}^{t_j+T}\mu(s)\,ds\longrightarrow0\qquad(T<\infty)
\]
show via integral equations and Grönwall's inequality that \(p(t_j+\cdot)\) converges uniformly on \([0,T]\) to the unmutated solution \(\varphi_{\cdot}(q)\). Therefore each \(\varphi_s(q)\) lies in the omega-limit set. As the positive forward orbit of \(q\) traverses the entire entropy level, that level is contained in the omega-limit set. The reverse inclusion was proved above. Finally \(S(t)\to1\) identifies the omega-limit set for the original densities \(m(t)\) with precisely the displayed curve.

**5. Power-law boundary.** For \(\mu(t)=a(1+t)^{-q}\), its total integral diverges precisely when \(q\le1\). At \(q=1\), \(M(t)=a\log(1+t)\), so the logarithmic exponent gives \(\log H(t)=-6a\log(1+t)+o(\log t)\); this is the claimed asymptotic logarithmic power law.

## Verification

The standalone `verify.py` checks the exact logistic reduction and entropy derivative using rational arithmetic across 35 parameter triples; verifies the entropy-dissipation inequality at 99 rational compositions; checks the limit of \(D/H\) near the uniform composition; and integrates original, unnormalized three-species equations under three power-law mutation schedules, confirming the displayed finite-time inequalities. Run `python3 verify.py` from the directory containing this document. The analytical proof, not finite testing, establishes the infinite-time alternatives and the omega-limit statement.

## Relationship to prior work

Jaramillo, Mrad and Stepien introduced and analyzed the May–Leonard model with **constant** global mutation, including its equilibrium and Hopf structure; their preprint first appeared on 9 October 2022. The classical unperturbed neutral cycles were known much earlier. Toupo and Strogatz analyzed constant-rate replicator–mutator rock–paper–scissors dynamics. Boone and Piliouras described the periodic orbits and KL conservation of the zero-sum replicator. None of these cited works states the cumulative-budget dichotomy for arbitrary measurable time-dependent global mutation rates, its sharp KL decay exponent, or its full finite-budget omega-limit conclusion. The known constant-rate stabilization, when restricted to the neutral interaction line, is a special case of the infinite-budget alternative; it is not claimed as new. The new statement is the **two-sided all-schedule classification** and sharp rate on that line.

## Limitations

The theorem requires exactly symmetric three-way mutation and exactly the critical interaction line. It does not extend as stated to asymmetric exchange, other ecological parameter regimes, spatially structured or stochastic models, or data with species initially absent. For finite mutation budgets it identifies the entire asymptotic orbit but does **not** assert a limiting phase shift relative to a fixed periodic solution. The logarithmic exponent \(-6\) is measured against cumulative mutation exposure, not physical time. Novelty relative to general nonautonomous replicator or perturbation theorems cannot be certified by a finite literature search.

## References

- G. Jaramillo, L. Mrad and T. L. Stepien, *Dynamics of a linearly-perturbed May–Leonard competition model*, arXiv:2210.04342v1, first posted 2022-10-09. https://arxiv.org/abs/2210.04342 (especially Section III, Eq. (6), and stability discussion).
- N. Toupo and S. H. Strogatz, *Nonlinear dynamics of the rock-paper-scissors game with mutations*, arXiv:1502.03370v1 (2015). https://arxiv.org/abs/1502.03370 (especially Sections III–V).
- V. Boone and G. Piliouras, *From Darwin to Poincaré and von Neumann: Recurrence and Cycles in Evolutionary and Algorithmic Game Theory*, arXiv:1910.01334v1 (2019). https://arxiv.org/abs/1910.01334 (three-strategy zero-sum periodicity and KL invariant).
