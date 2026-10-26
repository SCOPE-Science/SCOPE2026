# Sharp complete-positivity and entanglement-breaking arrival times in affine qubit semigroups

## Finding

The affine qubit semigroup studied by Diesel, Bäcker and Strunz [1] can become a completely positive trace-preserving channel at a finite positive time even when its time-independent generator is not of GKSL form. For every \(\alpha>0\) and \(|\beta|<1\), this note determines its exact complete-positivity (CP) and entanglement-breaking (EB) arrival times and establishes sharp singular laws as the stationary state approaches purity.

Let \(s=\sqrt{1-\beta^2}\), \(p_t=e^{-\alpha t}\), and \(q_t=e^{-t}\). The map is CP at a fixed time \(t>0\) **if and only if**
\[
 |p_t-q_t|\le s(1-q_t),
\]
and is EB **if and only if**
\[
 p_t+q_t\le s(1-q_t).
\]
It is CP for all times if \(|\alpha-1|\le s\). Otherwise, its first positive CP time \(t_{\mathrm{CP}}\) is the unique positive solution of equality in the first inequality, and it is non-CP strictly before that time. Its EB time \(t_{\mathrm{EB}}\) is always the unique positive solution of equality in the second inequality. In all cases with \(\alpha>0\) and \(|\beta|<1\),
\[
 0\le t_{\mathrm{CP}}<t_{\mathrm{EB}}<\infty.
\]
When the generator is non-GKSL, \(t_{\mathrm{CP}}>0\) and there is a nonempty interval in which the individual propagating map is CP but not yet EB.

For fixed \(\alpha>0\), \(\alpha\ne1\), and \(s\downarrow0\), put \(m=\min\{\alpha,1\}\). Then
\[
 t_{\mathrm{CP}}\sim t_{\mathrm{EB}}\sim \frac{\log(1/s)}{m},\qquad
 t_{\mathrm{EB}}-t_{\mathrm{CP}}\sim\frac{2}{m}s^{|\alpha-1|/m}.
\]
There is a nontrivial transition layer around \(\alpha=1\): for any fixed real \(u\ne0\), let \(L=\log(1/s)\) and \(\alpha=1+u/L\). As \(s\downarrow0\),
\[
\begin{aligned}
 t_{\mathrm{CP}}&=L+\log|1-e^{-u}|+o(1),\\
 t_{\mathrm{EB}}&=L+\log(1+e^{-u})+o(1),\\
 t_{\mathrm{EB}}-t_{\mathrm{CP}}&\longrightarrow
       \log\coth\bigl(|u|/2\bigr).
\end{aligned}
\]
At the exactly degenerate parameter \(\alpha=1\), by contrast, \(t_{\mathrm{CP}}=0\) and \(t_{\mathrm{EB}}=\log(1+2/s)\).

## Assumptions and scope

The state space consists of qubit density matrices \(\rho=(I+x\sigma_x+y\sigma_y+z\sigma_z)/2\). All maps act by complex-linear extension on \(2\times2\) matrices and preserve trace and adjoints. For \(\alpha>0\) and \(-1\le\beta\le1\), define
\[
 \Phi_t:(x,y,z)\longmapsto
   \bigl(e^{-\alpha t}x,e^{-t}y,e^{-t}z+\beta(1-e^{-t})\bigr),
 \qquad t\ge0.
\]
Composition satisfies \(\Phi_{t+u}=\Phi_t\circ\Phi_u\). The restriction \(|\beta|<1\) in the main theorem ensures a full-rank stationary state \((I+\beta\sigma_z)/2\). The results concern the complete positivity and entanglement breaking of **each individual map \(\Phi_t\)**, not complete-positive divisibility of the family or complete positivity of its generator. If a map fails to be positive at an early time, that early map must not be interpreted as a physical channel on the entire Bloch ball. The Choi normalization used below is \(J_t=(\mathrm{id}\otimes\Phi_t)(|\Omega\rangle\langle\Omega|)\) with \(|\Omega\rangle=(|00\rangle+|11\rangle)/\sqrt2\).

For boundary completeness: when \(|\beta|=1\) and \(\alpha=1\), all finite-time maps are CP but none is EB; when \(|\beta|=1\) and \(\alpha\ne1\), no strictly positive-time map is CP or EB. If the excluded value \(\alpha=0\) is admitted, \(\beta=0\) yields a CP dephasing semigroup that is never EB at a finite time, while \(\beta\ne0\) yields no strictly positive-time CP or EB maps. The identity map at time zero is CP in every case.

## Proof

**1. Choi reduction.** Write \(p=p_t\), \(q=q_t\), \(c=\beta(1-q)\). Evaluating the map on the four matrix units yields the normalized Choi matrix, in computational tensor-product order,
\[
 J_t=\frac14\begin{pmatrix}
 1+c+q&0&0&p+q\\
 0&1-c-q&p-q&0\\
 0&p-q&1+c-q&0\\
 p+q&0&0&1-c+q
 \end{pmatrix}.
\]
The diagonal entries are nonnegative because \(|c|\le1-q\). There are two Hermitian \(2\times2\) blocks. Their determinant numerators are
\[
 \begin{aligned}
 D_+&=(1+q)^2-c^2-(p+q)^2,\\
 D_-&=(1-q)^2-c^2-(p-q)^2.
 \end{aligned}
\]
Since \(D_+-D_-=4q(1-p)\ge0\), positivity of the Choi matrix is equivalent to \(D_-\ge0\). Because \((1-q)^2-c^2=s^2(1-q)^2\), this is precisely the stated CP inequality. In this step the original channel is not presumed CP.

Partial transposition on the second qubit exchanges \(p+q\) with \(p-q\) between the off-diagonal blocks, leaving their diagonal entries unchanged. The smaller partial-transpose determinant is now
\[
 \widetilde D_-=(1-q)^2-c^2-(p+q)^2,
\]
while the other exceeds it by \(4q(1+p)>0\) for finite \(t>0\). Thus \(J_t\) has a positive partial transpose exactly when \(p+q\le s(1-q)\). A two-qubit density matrix is separable if and only if its partial transpose is positive. Moreover the EB inequality implies the CP inequality by \(|p-q|\le p+q\). Therefore the EB equivalence follows, without assuming complete positivity in advance.

**2. Unique arrival times.** For \(\alpha\ne1\), consider
\[
 R_\alpha(t)=\frac{|e^{-\alpha t}-e^{-t}|}{1-e^{-t}}.
\]
If \(0<\alpha<1\), this is the ratio
\[
 R_\alpha(t)=
  \frac{\int_\alpha^1e^{-vt}\,dv}{\int_0^1e^{-vt}\,dv};
\]
if \(\alpha>1\), the numerator is instead \(\int_1^\alpha e^{-vt}\,dv\). In either case the logarithmic derivative of this ratio is the mean of \(-v\) in the numerator interval minus that in \([0,1]\); it is strictly negative, since the numerator interval is strictly to the right in the relevant exponential-tilted comparison. Its boundary limits are \(\lim_{t\downarrow0}R_\alpha(t)=|\alpha-1|\) and \(\lim_{t\to\infty}R_\alpha(t)=0\), for \(\alpha>0\). For \(\alpha=1\) it vanishes identically. This proves the global CP classification and, where needed, a unique positive crossing.

Similarly,
\[
 E_\alpha(t)=\frac{e^{-\alpha t}+e^{-t}}{1-e^{-t}}
\]
is strictly decreasing, with limits \(+\infty\) and zero. It therefore crosses any \(s>0\) precisely once. At the EB crossing \(|p-q|<p+q=s(1-q)\), since both \(p,q>0\); the CP boundary must have occurred strictly earlier. This proves \(t_{\mathrm{CP}}<t_{\mathrm{EB}}\).

**3. Pure-target scaling for fixed \(\alpha\ne1\).** Let \(m=\min\{\alpha,1\}>0\) and \(L=\log(1/s)\). Both crossing equations require the slower-decaying of \(p,q\) to be asymptotic to \(s\); therefore \(t_{\mathrm{CP}},t_{\mathrm{EB}}\sim L/m\), and the other exponential is asymptotic to \(s^{\max(\alpha,1)/m}\). The two crossing equations differ only by the sign of this faster-decaying exponential. The derivative magnitude of the slower exponential at either crossing is asymptotic to \(ms\); by the mean-value theorem, the difference of crossing times is asymptotic to twice the faster exponential divided by \(ms\), namely
\[
 \frac{2}{m}s^{(\max(\alpha,1)-m)/m}
   =\frac2m s^{|\alpha-1|/m}.
\]
Corrections from the common factor \(1-q\) are smaller in the difference because its value and derivative vary continuously at the two asymptotically coinciding roots; alternatively the crossing equations may be subtracted after Taylor expansion, giving the same leading term.

**4. Critical layer.** With \(\alpha=1+u/L\) and \(u\ne0\) fixed, the two crossing times are both \(L+O(1)\). Consequently \(p/q=e^{-(\alpha-1)t}=e^{-u}(1+o(1))\), and \(1-q=1+o(1)\). Substituting into the CP and EB equalities gives respectively
\[
 q=\frac{s}{|1-e^{-u}|}(1+o(1)),\qquad
 q=\frac{s}{1+e^{-u}}(1+o(1)).
\]
Taking negative logarithms yields the stated layer formulas. The identity
\(\log[(1+e^{-u})/|1-e^{-u}|]=\log\coth(|u|/2)\)
completes the result. For \(\alpha=1\), \(p=q\) and the EB equation becomes \(2e^{-t}=s(1-e^{-t})\), hence the distinct exact boundary law.

**5. Degenerate endpoints.** At \(s=0\) the CP inequality requires \(p=q\), which for \(t>0\) means \(\alpha=1\); the EB inequality cannot hold at finite \(t\) because \(p+q>0\). At \(\alpha=0\), \(p=1\), and the CP inequality requires \(1-q\le s(1-q)\); this holds at positive times exactly when \(s=1\), while EB is impossible since \(1+q>s(1-q)\).

## Verification

The accompanying standalone file `verification.py` reconstructs \(J_t\) from the four independent matrix-unit images, separately computes the closed Choi matrix and partial transpose, and compares the CP and PPT inequalities against the eigenvalue tests on a grid of parameters. It also numerically solves the two threshold equations and tests both the fixed-parameter and near-critical asymptotics at high precision. Execution with NumPy, SciPy and mpmath passed 2,230 assertions. Numerical tests are consistency checks; every continuous, infinite-time and singular-limit statement is justified by the analytic argument above.

For example, for \(\alpha=3\), \(\beta=0.6\), the CP arrival time is approximately \(0.6449379916078235\), whereas the EB arrival time is approximately \(0.8989625707590763\).

## Relationship to prior work

Diesel, Bäcker and Strunz [1] introduce and analyze this two-parameter Bloch semigroup and establish the generator's GKSL region \((\alpha-1)^2+\beta^2\le1\), together with full-space positivity and restricted-positivity regions. Equation (41) of [1] supplies the map studied here; its classification of generators is not an evaluated finite-time CP/EB threshold. The present contribution is the pair of exact arrival-time criteria and the nontrivial collapse/crossover scaling of the intervening CP-but-non-EB interval.

Szczygielski and Chruściński [2] analyze general eventually entanglement-breaking evolution families, including non-GKSL settings; such general results anticipate eventual EB behavior in suitable regimes. Hanson, Rouzé and França [3] study characteristic EB times for quantum Markov semigroups, while Rahaman, Jaques and Paulsen [4] study eventual EB under iterated quantum channels. These works provide the general vocabulary and qualitative setting rather than the evaluated arrival-time formulas and singular two-parameter layer for [1]. The standard Choi and two-qubit PPT criteria used in the proof are established mathematical tools, not claimed as new. The originality of any broader generalization and literature-wide priority have not been independently determined.

## Limitations

The theorem applies to the exact algebraic qubit semigroup displayed above, not to arbitrary qubit dynamics or general Gaussian channels. During the interval in which \(\Phi_t\) is not positive or not CP, it is not a legitimate arbitrary-input quantum channel; later CP arrival does not make its underlying non-GKSL generator CP-divisible. The formulas describe maps at the elapsed times, not a physical implementation of every intermediate propagator. Uniformity is not claimed when \(u\to0\) simultaneously with the critical scaling, nor for a pure stationary state beyond the explicit endpoint classification. The results are proved mathematically but do not establish experimental feasibility or an independent literature-wide priority certificate.

## References

[1] N. Diesel, C. Bäcker, W. T. Strunz, *Gaussian and Qubit Semigroup Dynamics beyond GKSL*, arXiv:2610.20258v1 (first posted 14 October 2026), Section 4, Eq. (41), Appendices C–D. https://arxiv.org/html/2610.20258v1

[2] K. Szczygielski and D. Chruściński, *Eventually entanglement breaking divisible quantum dynamics*, Journal of Physics A: Mathematical and Theoretical **57** (2024), 495206; preprint arXiv:2407.16583. https://arxiv.org/abs/2407.16583

[3] E. Hanson, C. Rouzé and D. Stilck França, *Eventually Entanglement Breaking Markovian Dynamics: Structure and Characteristic Times*, Annales Henri Poincaré **21** (2020), 1517–1592, arXiv:1902.08173. https://arxiv.org/abs/1902.08173

[4] M. Rahaman, S. Jaques and V. Paulsen, *Eventually Entanglement Breaking Maps*, arXiv:1801.05542v2 (2018). https://arxiv.org/abs/1801.05542

[5] S. N. Filippov, A. N. Glinov and L. Leppäjärvi, *Phase Covariant Qubit Dynamics and Divisibility*, arXiv:1911.09468 (2019), for related phase-covariant channel classifications; abstract-level comparison only. https://arxiv.org/abs/1911.09468
