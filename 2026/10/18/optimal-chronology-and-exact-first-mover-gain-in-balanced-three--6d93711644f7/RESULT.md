# Optimal chronology and exact first-mover gain in balanced three-way opinion networks

## Finding

Consider the continuous-time three-body consensus model (3CM) of Neuhäuser and collaborators on two equal-sized groups, with reinforcing modulation \(s(z)=e^{-\kappa z}\), \(\kappa>0\). Suppose an equitable family of three-person discussions has a balanced number of local-majority discussions for each group. If the same positive amount of time is allotted to both kinds of discussion, then **activating all discussions favoring the initially higher-opinion group first is the unique schedule (up to null sets) that maximizes the eventual consensus**. Reversing the order uniquely minimizes it. This holds for arbitrary compatible incidence arrangements, not only one example of a clustered hypergraph.

The sharp consensus interval, exact maximum gain and its positive quadratic small-window law are provided below. This is a theorem for deterministic continuous-time opinions with initially homogeneous groups; it is not a claim for arbitrary initial opinions, unequal exposure budgets, or stochastic networks.

## Assumptions and scope

Let \(n\ge2\) and partition \(2n\) agents into labeled groups \(A\) and \(B\), each of size \(n\). Let \(\mathcal E_+\) consist of \(M\) *distinct* unordered three-edges, each containing two agents from \(A\) and one from \(B\). Let \(\mathcal E_-\) consist of \(M\) distinct three-edges, each containing one agent from \(A\) and two from \(B\). Assume incidence balance:

* in \(\mathcal E_+\), every \(A\) agent occurs in exactly \(2M/n\) edges and every \(B\) agent in exactly \(M/n\) edges;
* in \(\mathcal E_-\), every \(A\) agent occurs in exactly \(M/n\) edges and every \(B\) agent in exactly \(2M/n\) edges.

In particular, \(M/n\) is a positive integer. The class is nonempty for every \(n\ge2\): with indices interpreted cyclically, use
\[
\mathcal E_+=\{\{A_i,A_{i+1},B_i\}:1\le i\le n\},\qquad
\mathcal E_-=\{\{A_i,B_i,B_{i+1}\}:1\le i\le n\}.
\]
Here \(M=n\); both classes of hypergraphs are connected. Any additional intra-group hyperedges, if present, exert zero influence along the homogeneous-group trajectories considered here.

During an active snapshot \(\mathcal E\), every unordered edge \(\{i,j,k\}\) contributes to the opinion derivative at vertex \(i\) the term
\[
 e^{-\kappa|x_j-x_k|}(x_j+x_k-2x_i),
\]
and analogously at \(j,k\). Each edge contributes **once per target vertex**. This is the same per-edge normalization as the temporally extended 3CM in arXiv:2109.04985, equations (3)–(6); presentations that sum over ordered neighbor pairs without a factor \(1/2\) rescale physical time.

Initially \(x_i(0)=a_0\) for every \(i\in A\), \(x_j(0)=b_0\) for every \(j\in B\), with \(d_0=a_0-b_0>0\). Fix \(\tau>0\). For \(0\le t<2\tau\), exactly one of \(\mathcal E_+\), \(\mathcal E_-\) is active at each time; the selection may be any measurable switching schedule, with each kind active for total time \(\tau\). For \(t\ge2\tau\), activate their union permanently. Write \(C\) for the resulting common limiting opinion.

Set \(\rho=2M/n>0\), and let \(d(t)>0\) be the unique solution of
\[
\dot d=-\rho d(1+e^{-\kappa d}),\qquad d(0)=d_0.
\]
This gap is **independent of the order of the first two snapshots**. Define \(d_1=d(\tau)\), \(d_2=d(2\tau)\), and
\[
L_\kappa(z)=\frac1\kappa\log\cosh\left(\frac{\kappa z}{2}\right),\qquad
\Delta=L_\kappa(d_0)-2L_\kappa(d_1)+L_\kappa(d_2).
\]

**Exact chronology theorem.** For every permitted schedule,
\[
\frac{a_0+b_0}{2}-\Delta\ \le C\le\ \frac{a_0+b_0}{2}+\Delta,
\qquad \Delta>0.
\]
The upper endpoint occurs exactly when \(\mathcal E_+\) is active on \([0,\tau)\) and \(\mathcal E_-\) on \([\tau,2\tau)\), modulo null sets. The lower endpoint occurs exactly for the reverse order. Every other schedule with the same exposure budgets gives a strictly intermediate value. In particular, both endpoints are independent of the incidence arrangement subject to the two degree conditions.

The gain has the asymptotic laws, with \(q_0=e^{-\kappa d_0}\),
\[
\Delta=\frac{\rho^2}{2}d_0(1+q_0)
\big(1-q_0+\kappa d_0 q_0\big)\tau^2+O(\tau^3)
\quad(\tau\downarrow0),
\]
\[
\lim_{\tau\to\infty}\Delta=L_\kappa(d_0)
=\frac1\kappa\log\cosh\left(\frac{\kappa d_0}{2}\right)
\in(0,d_0/2).
\]
For fixed \(d_0>0\), this limiting advantage tends to \(d_0/2\) as \(\kappa\to\infty\): the first local-majority group can drive eventual consensus arbitrarily close to its own initial opinion, even when the two populations and total discussion times are exactly balanced.

## Proof

**1. Invariant two-group manifold.** Each vertex in a given group has the same incidence degree within each type of snapshot. Consequently, the set where every \(A\)-opinion equals \(a(t)\) and every \(B\)-opinion equals \(b(t)\) is invariant by uniqueness of the finite-dimensional, locally Lipschitz ODE. Put \(d=a-b\), \(m=(a+b)/2\). If \(\mathcal E_+\) is active, an \(A\)-agent receives \(-d e^{-\kappa d}\) per incident edge and a \(B\)-agent receives \(2d\); therefore
\[
\dot a=-\rho d e^{-\kappa d},\qquad \dot b=\rho d.
\]
If \(\mathcal E_-\) is active, the analogous calculation gives
\[
\dot a=-\rho d,\qquad \dot b=\rho d e^{-\kappa d}.
\]
In both cases, \(\dot d=-\rho d(1+e^{-\kappa d})\). Thus \(d\) remains strictly positive at every finite time, decreases continuously, and is independent of the switching schedule. Boundedness follows because \(a\) never increases and \(b\) never decreases while \(a>b\), so the trajectory stays in \([b_0,a_0]\).

**2. Exact schedule representation.** Let \(u(t)=1\) for an \(\mathcal E_+\) snapshot and \(u(t)=-1\) for an \(\mathcal E_-\) snapshot. Then
\[
\dot m=u(t)w(t),\quad
w(t)=\\frac{\\rho}{2} d(t)(1-e^{-\kappa d(t)}).
\]
For \(z>0\), \(d[z(1-e^{-\kappa z})]/dz=1-e^{-\kappa z}+\kappa z e^{-\kappa z}>0\). Since \(d'(t)<0\), \(w(t)>0\) is strictly decreasing on \([0,2\tau]\). Therefore
\[
m(2\tau)=m(0)+\int_0^{2\tau}u(t)w(t)\,dt.
\]
The subset where \(u=1\) has Lebesgue measure \(\tau\). For a strictly decreasing positive function \(w\), the integral of \(w\) over any measurable subset of measure \(\tau\) is at most its integral over \([0,\tau]\), with equality only if the subset agrees with that initial interval almost everywhere. (Exchange any later positive-measure selected subset with an equally sized earlier unselected subset.) Its minimum is attained, uniquely almost everywhere, over \([\tau,2\tau]\). This proves the sharp chronological order and its strict uniqueness.

**3. Closed gain formula.** Direct differentiation yields
\[
L_\kappa'(d)=\frac12\tanh\left(\frac{\kappa d}{2}\right)
=\frac12\frac{1-e^{-\kappa d}}{1+e^{-\kappa d}},
\quad \frac{d}{dt}L_\kappa(d(t))=-w(t).
\]
Hence, under \(\mathcal E_+\) the quantity \(m+L_\kappa(d)\) is constant, while under \(\mathcal E_-\) the quantity \(m-L_\kappa(d)\) is constant. Following the maximizing two-stage order gives
\[
m(2\tau)-m(0)=
[L_\kappa(d_0)-L_\kappa(d_1)]
-[L_\kappa(d_1)-L_\kappa(d_2)]=\Delta.
\]
The reverse order gives \(-\Delta\).

**4. Persistence of the mean after the two snapshots.** With the union \(\mathcal E_+\cup\mathcal E_-\) active, every \(A\)-agent has derivative \(-\rho d(1+e^{-\kappa d})\) and every \(B\)-agent has the opposite derivative. Thus \(\dot m=0\) and \(\dot d=-2\rho d(1+e^{-\kappa d})\), giving \(d\to0\) exponentially and \(C=m(2\tau)\). This also shows why the result concerns *ultimate* consensus rather than just a finite-time average.

**5. Strictness and boundary laws.** Because \(w\) strictly decreases, \(\Delta=\int_0^\tau w(t)dt-\int_\tau^{2\tau}w(t)dt>0\). Differentiating once more gives
\[
-w'(0)=\frac{\rho^2}{2}d_0(1+q_0)
\big(1-q_0+\kappa d_0q_0\big)>0.
\]
Taylor expansion of the two consecutive window integrals proves the \(O(\tau^3)\) remainder and displayed quadratic coefficient. The gap ODE implies \(d(t)\to0\); taking \(\tau\to\infty\) in the exact formula proves the limit. Finally \(0<\log\cosh x<x\) for every \(x>0\) and \(\log\cosh x=x-\log 2+o(1)\) as \(x\to\infty\), giving the stated bounds and strong-reinforcement limit.

## Verification

Run `python check.py` with Python 3.9 or newer. The standard-library-only checker constructs the full (not pre-reduced) vertex ODE on explicit cyclic hypergraphs with \(n=2,3,5\), confirms incidence balances, integrates all target-vertex equations independently, and compares A-first, B-first and interleaved time schedules to the scalar theorem. It tests four positive reinforcement intensities and two positive window lengths, then integrates the all-on terminal phase. It also checks the positive small-window coefficient at three shorter durations.

The checker passed 24 independent parameter/topology cases and their terminal comparisons. For \(n=3\), \(\kappa=2\), \(\rho=2\), \(a_0=1\), \(b_0=0\), \(\tau=0.6\), it gives
\[
d_1\approx0.187006621995,\quad d_2\approx0.020033334112,
\quad\Delta\approx0.199605980357,
\]
so A-first consensus is approximately \(0.699605980357\) and B-first approximately \(0.300394019643\); alternating four equal half-windows yields approximately \(0.624928685298\), strictly inside the sharp interval. These are independent numerical diagnostics; the theorem for all \(n\), all compatible hypergraphs, and all admissible measurable schedules is justified by the proof above, not by finite tests.

## Relationship to prior work

Neuhäuser, Schaub, Mellor and Lambiotte (arXiv:2004.00901; first public version 2 April 2020) introduce the deterministic exponential three-body opinion model and demonstrate majority/minority effects. Neuhäuser, Lambiotte and Schaub (arXiv:2109.04985; first public version 10 September 2021), especially Sections 3.1 and 5.1–5.3, investigate nonlinear temporal hypergraphs and show first-mover advantage through simulations of randomly placed clustered connections. The **qualitative phenomenon and model are prior results**, not claimed here. The additional results here are a closed, topology-independent chronological optimization theorem over *every* measurable schedule with fixed equal exposure budgets, its exactly computable sharp consensus endpoints and strict small-window gain.

The 2021 chapter arXiv:2105.01369 surveys deterministic multibody opinion shifts and clustered structures, but does not state this sharp chronological scheduling law. Shang (2023, doi:10.1093/comnet/cnad009) analyzes a different **discrete-time stochastic** temporal model and proves consensus and moment criteria rather than this continuous-time optimal order. Shang (2022, doi:10.1098/rspa.2021.0564) treats conservation and consensus for another multi-body model; its abstract and available metadata were examined, but not its full manuscript. Priority against further less-indexed studies of exact switched consensus remains a residual risk, and no independent priority certification is asserted.

## Limitations

The reduction relies crucially on initially uniform opinions inside each group and equitable incidence in each snapshot. Arbitrary heterogeneous opinions may destroy the two-dimensional invariant manifold. The chronology optimization also requires equal positive exposure rates, one snapshot at a time, an exact budget of \(\tau\) for each, and a subsequent simultaneous balanced phase. It does not extend automatically to unequal groups, imperfect discussion activation, noise, infinite networks, or simultaneous overlap during the controlled interval. The selection parameter \(\kappa\) and per-edge time normalization must be held fixed in schedule comparisons. At \(\kappa=0\) the strict advantage vanishes because the dynamics are linear; it is not included in the strict theorem. The strongest statements have been checked analytically within the stated scope but have not received independent scientific audit.

## References

1. L. Neuhäuser, M. T. Schaub, A. Mellor and R. Lambiotte, *Opinion Dynamics with Multi-Body Interactions*, arXiv:2004.00901v1 (2 April 2020), https://arxiv.org/html/2004.00901v1.
2. L. Neuhäuser, R. Lambiotte and M. T. Schaub, *Consensus dynamics on temporal hypergraphs*, arXiv:2109.04985v1 (10 September 2021), *Physical Review E* 104 (2021) 064305, https://arxiv.org/html/2109.04985v1.
3. L. Neuhäuser, R. Lambiotte and M. T. Schaub, *Consensus Dynamics and Opinion Formation on Hypergraphs*, arXiv:2105.01369 (initial version 4 May 2021), https://arxiv.org/html/2105.01369v2.
4. Y. Shang, *Non-linear consensus dynamics on temporal hypergraphs with random noisy higher-order interactions*, *Journal of Complex Networks* 11 (2023) cnad009, https://doi.org/10.1093/comnet/cnad009.
5. Y. Shang, *A system model of three-body interactions in complex networks: Consensus and conservation*, *Proceedings of the Royal Society A* 478 (2022) 20210564, https://doi.org/10.1098/rspa.2021.0564.
