# Exact throughput-allocation transition in two interacting exclusion lanes

## Finding

In a pair of exchange-symmetric exclusion lanes with a product stationary law and an arbitrary nonpositive cross-lane drift, maximizing **the sum of the two signed stationary particle currents** over independently chosen lane densities undergoes an exact discontinuous allocation transition. At weak cross-inhibition, a unique balanced state optimizes throughput; beyond a sharp coupling, an empty lane and a half-filled lane are the only optimizers. The global transition lies strictly between two local-stability thresholds, producing a range of coexisting positive-throughput local optima.

Let the baseline drift be \(B>0\), let the common cross-lane parameter be \(\gamma=-cB\) with \(c\ge0\), and let the stationary Bernoulli occupancy densities \(u,v\) independently range over \([0,1]\). The established product-stationary current law gives
\[
 j_1=B u(1-u)(1-cv),\qquad j_2=B v(1-v)(1-cu).
\]
Define normalized total throughput \(J_c=(j_1+j_2)/B\). Put
\[
 q(c)=\frac{1}{1+c+\sqrt{c^2-c+1}},\qquad
 8q_*^3-16q_*^2+11q_*-2=0,\quad \frac14<q_*<\frac13,
\]
and
\[
 c_* =\frac{1-2q_*}{q_*(2-3q_*)}=1.35700320530498\ldots.
\]
Then the **complete global maximizer set** is
\[
 \operatorname{argmax}_{(u,v)\in[0,1]^2}J_c(u,v)=
 \begin{cases}
 \{(q(c),q(c))\},&0\le c<c_*,\\
 \{(q_*,q_*),(\tfrac12,0),(0,\tfrac12)\},&c=c_*,\\
 \{(\tfrac12,0),(0,\tfrac12)\},&c>c_*.
 \end{cases}
\]
In particular,
\[
 \max_{[0,1]^2}(j_1+j_2)
 =B\max\left\{2q(c)(1-q(c))(1-cq(c)),\frac14\right\}.
\]
The edge optimizer \((\frac12,0)\) becomes a strict local maximum exactly when \(c>\frac43\). The balanced positive-throughput optimizer \((q(c),q(c))\) is a strict local maximum exactly when \(0\le c<c_{\mathrm s}\), where
\[
 c_{\mathrm s}=\frac{5-\sqrt5}{2}=1.38196601125010\ldots.
\]
At each spinodal equality the corresponding branch is **not** a strict local maximum (and the balanced point at the upper spinodal is not even a non-strict local maximum). Therefore the positive-throughput balanced and edge branches are simultaneously strict local maxima throughout
\[
 \frac43<c<c_{\mathrm s},
\]
and the global switch occurs strictly inside that interval.

## Assumptions and scope

The microscopic process is an infinite or periodic two-lane nearest-neighbor exclusion process with no lane changing, for which the grand-canonical Bernoulli product laws are stationary; the two lane particle numbers are separately conserved. Conditional on the opposite lane's bond occupancy \(d\in\{0,1,2\}\), the forward-minus-backward hopping-rate difference on either lane is \(B-(cB/2)d\). Such physical nonnegative rates exist for every \(c\ge0\): take forward and backward rates \(K\pm\tfrac12[B-(cB/2)d]\), respectively, with \(K>B(1+c)/2\). The stationarity and exact flux formula are established in the cited primary literature and are assumed here, not claimed as discoveries.

The optimization compares stationary ensembles whose densities are selected independently; it does not assert that a process at fixed conserved particle numbers dynamically selects one optimizer, or that the corresponding open system has a physical first-order phase transition. Signed **total flux** is the objective, not absolute current or current per occupied particle. Density endpoints correspond to degenerate product measures and are included.

## Proof

**1. Global reduction without symmetry assumptions.** Abbreviate \(s=u+v\) and \(p=uv\). Direct expansion gives the exact identity
\[
 J_c(u,v)=s-s^2+p\,[2-c(2-s)].
\]
For fixed \(s\in[0,2]\), the feasible product interval is
\[
 \max(0,s-1)\le p\le s^2/4.
\]
The upper endpoint is achieved only by \(u=v=s/2\); the lower is achieved by a density on the boundary of \([0,1]^2\). Since \(J_c\) is affine in \(p\), a global maximum lies on the diagonal or square boundary. On the empty-lane edges, the maximum is \(1/4\), attained only at \((1/2,0)\) and \((0,1/2)\). On a full-lane edge, the total current is \((1-c)v(1-v)\le1/4\), and cannot match the global value except potentially at \(c=0\), where the diagonal has current \(1/2\).

**2. Balanced branch.** On \(u=v=q\), set \(F_c(q)=2q(1-q)(1-cq)\). Its stationary equation is
\[
 \tfrac12F_c'(q)=1-2(1+c)q+3cq^2=0.
\]
The first root is \(q(c)=[1+c+\sqrt{c^2-c+1}]^{-1}\), with \(q(0)=1/2\). It is the unique global diagonal maximizer: the derivative starts positive at zero; the second root, when inside \([0,1]\), is a local minimum; and the diagonal endpoints have zero current, strictly below the positive value at \(q(c)\). The balanced optimal value \(M(c)=F_c(q(c))\) is strictly decreasing, because \(M'(c)=-2q(c)^2(1-q(c))<0\) (with the corresponding one-sided derivative at zero). Also \(M(0)=1/2\) and \(M(c)\to0\) as \(c\to\infty\). Hence exactly one \(c_*\) satisfies \(M(c_*)=1/4\). Eliminating \(c=(1-2q)/[q(2-3q)]\) from that equality gives \(8q^3-16q^2+11q-2=0\). Its derivative \(24q^2-32q+11\) is positive for every real \(q\), as its discriminant is negative and its leading coefficient is positive, and the polynomial changes sign between \(1/4\) and \(1/3\). This proves the exact root and all three comparisons.

**3. Exhaustion of global maximizers.** The fixed-sum reduction could admit extra off-diagonal maximizers only on a flat fiber \(2-c(2-s)=0\). For \(0<c\le1\), no such interior fiber exists. If \(1<c<2\), its sum is \(s=2-2/c\in(0,1)\), and its common current is \(s(1-s)\le1/4\), with equality possible only at \(c=4/3\). But at \(c=4/3\) the diagonal witness \(u=v=2/7\) gives \(J=260/1029>1/4\). If \(c\ge2\), the flat sum is at least one and \(s-s^2\le0\); it likewise cannot maximize the positive current. Thus only the specified balanced and half-filled-empty pairs can globally maximize. The preceding strict comparisons prove their exact multiplicities.

**4. The lower and upper spinodals.** At \((u,v)=(1/2,0)\), the inward derivative is \(\partial_vJ_c=1-3c/4\); tangential curvature is \(\partial_{uu}J_c=-2\). Therefore it is a strict local maximum for \(c>4/3\), and is not a local maximum below. At equality, the feasible path \(u=1/2-2v/3\) obeys
\[
 J_{4/3}(1/2-2v/3,v)-1/4=v^2/9-8v^3/27>0
\]
for all sufficiently small \(v>0\), so equality is not a maximum either. By symmetry this holds at the other edge.

At the balanced critical point the Hessian eigenvalues in the parallel and antisymmetric directions are
\[
 \lambda_+=-2(1+c-3cq(c))<0,
 \qquad \lambda_-=-2[1-c(1-q(c))].
\]
The second vanishes exactly at \(q=(5-\sqrt5)/10\) and \(c=c_{\mathrm s}=(5-\sqrt5)/2\). The balanced point is a strict local maximum below and a saddle above this value. At equality, write \(u=q+h+\delta\), \(v=q+h-\delta\). Since \(\lambda_-=0\), its exact expansion around the balanced critical point has the form
\[
 J_c(q+h+\delta,q+h-\delta)-J_c(q,q)
 =-A h^2+2c(-h)\delta^2+O(|h|^3),
 \quad A=2(1+c-3cq)>0.
\]
Choosing \(h=-(c/A)\delta^2\) makes the leading change \((c^2/A)\delta^4>0\). Hence the upper-spinodal balanced point is not a local maximum. Finally \(c_*>4/3\) follows from \(J_{4/3}(2/7,2/7)=260/1029>1/4\), and \(c_*<c_{\mathrm s}\) follows from \(M(c_{\mathrm s})=(\sqrt5-1)/5<1/4\), by strict monotonicity.

## Verification

`verify.py` uses only the Python standard library. Run `python verify.py` in the directory containing the extracted standalone script. It checks the exact \((s,p)\) polynomial identity over rational grids and both positive and negative interactions, the cubic bracket and threshold ordering, the two local-stability diagnostics, and numerical global-current domination for 12,000 random density pairs at each of 15 chosen coupling strengths. The number of passing assertions and computed constants are printed. These finite checks are supporting diagnostics; the preceding fixed-sum reduction, cubic monotonicity and Hessian/path calculations prove the statements for all parameters and densities.

## Relationship to prior work

The current-density law, the admissibility of arbitrary signed cross-lane couplings, and Bernoulli product stationarity are **prior results** of Popkov (2026); the same two-lane cubic current already appears in Popkov, Schmidt and Schütz (2014/2015) and in Schütz's 2017 lecture notes. Nothing about that current polynomial or stationary invariant measures is claimed as new. The literature on multilane flux extrema and flux-phase diagrams includes Evans, Kafri, Sugden and Tailleur (2011), Curatolo and collaborators (2016), and Amir, Bahadoran, Busani and Saada (2025). Those studies concern different dynamics and criteria (notably transverse lane switching, fixed total density/relaxation manifolds or open-system boundary selection). The claim here is restricted to the **complete unconstrained two-density optimizer of the exact cross-inhibited Bernoulli current**, including the two distinct local-instability thresholds and the exhaustive global optimizer sets. A broader optimization result not located in the inspected sources could still imply this classification.

## Limitations

The optimization is at the grand-canonical stationary flux level; it does not prove finite-size dynamical mixing, hysteresis, boundary-driven phase selection, experimental realizability, or stability of the density selection under a dynamical controller. It assumes two equal baseline drifts and identical cross-couplings; asymmetric baseline drifts, more than two lanes, and different objectives may behave differently. The positive-throughput local stability statements do not classify every zero-current local extremum elsewhere in the density square. Prior general flux theory and the pre-existing exact current formula create a residual originality risk; no independent validation has been performed.

## References

1. V. Popkov, *Multilane Asymmetric Exclusion Process with stationary Bernoulli measure* (2026), arXiv:2605.06949v1, https://arxiv.org/abs/2605.06949 .
2. V. Popkov, J. Schmidt and G. M. Schütz, *Universality classes in two-component driven diffusive systems* (2014/2015), arXiv:1410.8026, https://arxiv.org/abs/1410.8026 .
3. G. M. Schütz, *Fluctuations in Stochastic Interacting Particle Systems*, lecture notes (2017), Section 4.1, https://indico.math.cnrs.fr/event/852/attachments/1972/2137/Schutz_LectureNotes.pdf .
4. M. R. Evans, Y. Kafri, K. Sugden and J. Tailleur, *Phase diagram of two-lane driven diffusive systems* (2011), arXiv:1103.4677, https://arxiv.org/abs/1103.4677 .
5. M. Curatolo and collaborators, *Multilane Driven Diffusive Systems* (2015/2016), arXiv:1510.04150, https://arxiv.org/abs/1510.04150 .
6. G. Amir, C. Bahadoran, O. Busani and E. Saada, *Hydrodynamics and relaxation limit for multilane exclusion process and related hyperbolic systems* (2025), arXiv:2501.19355, https://arxiv.org/abs/2501.19355 .
