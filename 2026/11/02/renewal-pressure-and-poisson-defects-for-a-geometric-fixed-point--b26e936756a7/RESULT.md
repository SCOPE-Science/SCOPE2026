# Renewal pressure and Poisson defects for a geometric fixed-point potential

## Finding
Fix \(0<\theta<1\). For the binary one-sided full shift \((\Sigma,\sigma)\) with ultrametric \(d_\theta(x,y)=\theta^{\min\{j\ge0:x_j\ne y_j\}}\) for \(x\ne y\), define \(o=000\cdots\), \(H_\theta(x)=d_\theta(x,o)\), and let \(P_\beta\) and \(\mu_\beta\) be the topological pressure and equilibrium probability of \(-\beta H_\theta\), respectively, for \(\beta\ge0\). Write \(L=(1-\theta)^{-1}\), \(E_r=(1-\theta^r)/(1-\theta)\) and \(B_\beta=e^{-\beta L}\).

**Exact renewal law.** For every finite \(\beta\ge0\), \(P_\beta>0\) is the unique positive solution of
\[
\sum_{r=1}^{\infty}\exp(-\beta E_r-rP_\beta)=1.
\]
The equilibrium probability is the unique stationary renewal process whose return intervals between successive symbols \(1\) are independent with distribution
\[
q_\beta(r)=\exp(-\beta E_r-rP_\beta),\qquad r=1,2,\ldots.
\]
In particular, if \(\rho_\beta=\mu_\beta([1])\), then
\[\rho_\beta=\bigl(\sum_{r\ge1}r q_\beta(r)\bigr)^{-1}.\]

**Sharp low-temperature activation.** As \(\beta\to\infty\),
\[
\boxed{P_\beta=B_\beta\bigl(1+e^{-\beta}+e^{-\beta(1+\theta)}+o(e^{-\beta(1+\theta)})\bigr)},\qquad
\boxed{\rho_\beta\sim B_\beta}.
\]
The activation exponent is \(L\), not the instantaneous cost \(H_\theta(10\cdots)=1\). In particular, \(P_\beta>0\) at all finite inverse temperatures, although the unique maximizing probability is \(\delta_o\).

**Poisson rare-defect law.** Under stationary \(\mu_\beta\), put
\[
N_\beta=\sum_{j=0}^{\infty}x_j\,\delta_{jB_\beta}.
\]
As \(\beta\to\infty\), \(N_\beta\) converges in law, in the vague topology on locally finite counting measures over \([0,\infty)\), to the homogeneous rate-one Poisson process. Equivalently, its forward waiting time and subsequent inter-one intervals, multiplied by \(B_\beta\), converge jointly to independent mean-one exponential variables, for every fixed finite number of intervals.

## Assumptions and scope
The shift is the full one-sided shift on exactly two symbols; the metric parameter \(\theta\) is fixed strictly between zero and one, with \(\beta\to\infty\). The distance of a point to itself is zero; for any nonzero sequence, \(H_\theta(x)=\theta^k\), where \(k\) is the first index containing a one. The pressure uses the normalization \(P_\beta=\sup_\mu\{h_\mu(\sigma)-\beta\int H_\theta\,d\mu\}\). A return interval of size \(r\) from one symbol \(1\) to the next includes the first \(1\) and the following \(r-1\) zeros, but not the next \(1\). The measure \(\mu_\beta\) is stationary, rather than merely the Palm-conditioned renewal law.

## Proof
**1. Regularity and the ground state.** If two sequences agree through index \(n-1\), the difference of their distances to \(o\) is at most \(\theta^n\). Thus \(H_\theta\) is Lipschitz for the stated ultrametric, hence Hölder/Dini. Since \(H_\theta\ge0\) vanishes only at \(o\), the only probability with zero energy is \(\delta_o\).

**2. Exact energy per return.** Let \(Y=[1]\) and let \(R\) be the first return time to \(Y\). On the cylinder \([1 0^{r-1}1]\), the first \(r\) energy terms are \(1,\theta^{r-1},\theta^{r-2},\ldots,\theta\). Their sum is precisely \(E_r=1+\theta+\cdots+\theta^{r-1}\). This identity is independent of the symbols after that second \(1\). The induced return system on \(Y\) is the full shift on the countable alphabet \(r\in\{1,2,\ldots\}\).

**3. Variational pressure and uniqueness.** Fix \(\beta\ge0\). Since \(e^{-\beta E_r}\to e^{-\beta L}>0\), the strictly decreasing function \(p\mapsto\sum_{r\ge1}e^{-\beta E_r-rp}\) ranges from infinity to zero on \((0,\infty)\). It has exactly one root \(P_\beta>0\); define \(q_\beta(r)\) by the root formula. Because \(q_\beta(r)\le e^{-rP_\beta}\), its mean \(m_\beta=\sum r q_\beta(r)\) is finite. The stationary renewal probability with iid inter-one gaps \(q_\beta\) therefore exists.

For any ergodic invariant probability different from \(\delta_o\), the induced return measure on \(Y\) has a gap marginal \(p_r\) and finite mean \(m\). Kac's and Abramov's induced identities yield \(h_\mu=h_{\rm ind}/m\) and \(\int H_\theta\,d\mu=(\sum p_r E_r)/m\). The induced entropy satisfies \(h_{\rm ind}\le-\sum p_r\log p_r\), with equality only for iid gaps (interpreting the inequality by finite truncations when necessary). The Kullback–Leibler inequality for \(p\) against \(q_\beta\) gives
\[
-\sum_r p_r\log p_r-\beta\sum_r p_rE_r
=P_\beta m-D_{\rm KL}(p\Vert q_\beta)\le P_\beta m.
\]
The stationary iid-gap renewal attains equality, and equality requires the exact marginal \(p=q_\beta\) and independence. The competing measure \(\delta_o\) has pressure zero, strictly below \(P_\beta\). Ergodic decomposition establishes global uniqueness.

**4. Sharp expansion.** Put \(B=e^{-\beta L}\), \(a_r=e^{-\beta E_r}\), and \(\Delta_r=a_r-B\ge0\). The renewal equation becomes
\[
1=\frac{B}{e^{P_\beta}-1}+D_\beta(P_\beta),\qquad
D_\beta(p)=\sum_{r\ge1}\Delta_r e^{-rp}.
\]
For \(r\ge3\), since \(E_r\ge E_3=1+\theta+\theta^2\),
\[
0\le \Delta_r=e^{-\beta E_r}\bigl(1-e^{-\beta\theta^r/(1-\theta)}\bigr)
\le\frac{\beta\theta^r}{1-\theta}e^{-\beta E_3}.
\]
Consequently, uniformly for fixed \(\theta\),
\[
D_\beta(0)=e^{-\beta}+e^{-\beta(1+\theta)}-2B
+O_\theta\bigl(\beta e^{-\beta(1+\theta+\theta^2)}\bigr)
=e^{-\beta}+e^{-\beta(1+\theta)}+o(e^{-\beta(1+\theta)}),
\]
and \(\sum_r r\Delta_r=O_\theta(e^{-\beta})\). The exact equation first yields \(P_\beta\sim B\). It follows that \(D_\beta(P_\beta)=D_\beta(0)+O(P_\beta e^{-\beta})\), and
\[
\frac{P_\beta}{B}=
\frac{P_\beta}{e^{P_\beta}-1}\,
\frac{1}{1-D_\beta(P_\beta)}
=1+D_\beta(0)+O(D_\beta(0)^2+B+B e^{-\beta}).
\]
Because \(L>1+\theta\) and \(2>1+\theta\), these remainders are \(o(e^{-\beta(1+\theta)})\). This proves the pressure expansion.

**5. Stationary intensity.** Differentiating the geometric series gives
\[
m_\beta=\sum_{r\ge1}r q_\beta(r)
=\frac{B e^{-P_\beta}}{(1-e^{-P_\beta})^2}
+\sum_{r\ge1}r\Delta_r e^{-rP_\beta}
\sim\frac{B}{P_\beta^2}\sim\frac1B.
\]
The renewal-reward identity \(\rho_\beta=1/m_\beta\) gives \(\rho_\beta/B\to1\).

**6. Poisson limit, including the initial waiting time.** Under the Palm law conditional on a one at index zero, the subsequent gap \(R\) has law \(q_\beta\). For every fixed \(t\ge0\) and \(n=\lfloor t/B\rfloor\),
\[
\Pr(R>n)=\frac{B e^{-(n+1)P_\beta}}{1-e^{-P_\beta}}
+\sum_{r>n}\Delta_r e^{-rP_\beta}\longrightarrow e^{-t},
\]
since \(P_\beta/B\to1\), \(B/(1-e^{-P_\beta})\to1\), and the remainder is bounded by \(D_\beta(0)\to0\). Similarly, the geometric term dominates \(B^2\mathbb E[R^2]\to2\), and the \(\Delta_r\) contribution is negligible. Thus \(BR\) converges to an exponential distribution with convergent first two moments.

Under the stationary (unconditioned) renewal law, the interval straddling index zero has the size-biased gap distribution, and the location of the origin within that interval is uniform on its integer sites. Consequently, the scaled forward wait converges to an exponential distribution: this also follows from the stationary excess-tail formula \(\Pr(W>n)=m_\beta^{-1}\sum_{r>n}(r-n)q_\beta(r)\), up to the irrelevant one-site endpoint convention. Subsequent gaps are independent of that initial wait and iid with law \(q_\beta\). Joint convergence of the first finitely many scaled arrival times to independent exponential increments implies vague convergence of the point process to a unit-rate Poisson process. Tightness on bounded windows follows from \(\mathbb E N_\beta([0,t])\le(t/B+1)\rho_\beta\to t\) for \(t>0\). This completes the proof.

## Verification
The accompanying `verify.py` checks the exact finite-return energy formula for multiple geometric parameters and lengths, evaluates the positive pressure root by a scaled geometric-tail expression, and checks its residual and the first two correction ratios at several finite inverse temperatures. The symbolic limit reasoning, iid-gap equilibrium identification, and stationary Poisson limit are proved above; no finite computation is treated as an infinite proof.

## Relationship to prior work
Jiang, Li and Sun, *Typical periodic optimization and freezing phase transition: Dini potentials and beyond* (arXiv:2610.31327v1, first public October 22, 2026), prove general non-freezing and logarithmic-rate statements for Dini potentials on expanding systems. Those statements do not imply a particular pressure prefactor, its second correction, an exact Palm renewal distribution, or a stationary rare-event point-process limit. The present potential is a simple natural geometric-distance specialization addressing these quantitative questions.

Bissacot, Garibaldi and Thieullen, *Zero-temperature phase diagram for double-well type potentials in the summable variation class* (arXiv:1512.08071), develop different two-well thermodynamics with exactly two minimizing fixed points. Here there is only one energy-minimizing fixed point, and neither a two-well selection diagram nor a pressure barrier comparison automatically yields the stated formulas. General renewal and rare-event techniques are classical and are used without novelty claims; see also Chazottes and Ugalde on hitting and recurrence times for fixed Gibbs sources. The specific combined exact laws were not located among the compared published statements.

## Limitations
Only the full two-symbol shift with the stated geometric distance potential is classified. The rare-event theorem takes fixed \(\theta\in(0,1)\) and \(\beta\to\infty\); it does not assert a uniform limit as \(\theta\to0\) or \(\theta\to1\). The Poisson convergence is in distribution, not total variation of point processes. The discovery of a more general historic renewal theorem subsuming these exact pressure and point-process laws remains a residual priority risk; independent audit has not been performed.

## References
1. Y. Jiang, Z. Li, Y. Sun, *Typical periodic optimization and freezing phase transition: Dini potentials and beyond*, arXiv:2610.31327v1 (October 22, 2026), https://arxiv.org/html/2610.31327v1.
2. R. Bissacot, E. Garibaldi, P. Thieullen, *Zero-temperature phase diagram for double-well type potentials in the summable variation class*, arXiv:1512.08071, https://arxiv.org/abs/1512.08071.
3. J.-R. Chazottes, E. Ugalde, *Entropy estimation and fluctuations of hitting and recurrence times for Gibbsian sources*, arXiv:math/0401093, https://arxiv.org/abs/math/0401093.
