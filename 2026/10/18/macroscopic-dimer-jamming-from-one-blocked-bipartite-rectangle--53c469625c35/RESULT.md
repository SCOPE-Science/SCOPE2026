# Macroscopic dimer jamming from one blocked bipartite rectangle

## Finding

Let \(G_n\) be a balanced bipartite graph with \(n\) labelled vertices on each side. Choose \(A_n\) on the left and \(C_n\) on the right, and remove **all** edges between \(A_n\) and \(C_n\), retaining every other left–right edge. Suppose
\[
\frac{|A_n|}{n}\longrightarrow\alpha,\qquad
\frac{|C_n|}{n}\longrightarrow\beta,
\qquad 0<\alpha,\beta<1.
\]
Place dimers by considering the remaining edges in uniformly random order, accepting an edge precisely when both endpoints are still vacant. Write \(U_n\) for the final number of vacant vertices on *either* side (the two counts are identical).

Then, both in probability and in mean,
\[
\boxed{\frac{U_n}{n}\longrightarrow r(\alpha,\beta)},
\]
where
\[
I_*(\alpha,\beta)=
\begin{cases}
\dfrac{\log(\beta/\alpha)}{\beta-\alpha},&\alpha\ne\beta,\\[5pt]
\dfrac{1}{\alpha},&\alpha=\beta,
\end{cases}
\qquad
\boxed{r(\alpha,\beta)=\alpha\exp\bigl(-(1-\beta)I_*(\alpha,\beta)\bigr).}
\]
The expression is symmetric under interchange of \(\alpha\) and \(\beta\), and is strictly positive for fixed positive parameters. Furthermore, the final vacant fractions in \(A_n\) and \(C_n\) both converge to \(r(\alpha,\beta)\), whereas the final vacant fractions in their respective complements both converge to zero. The final overall fraction of *occupied vertices* converges to \(1-r(\alpha,\beta)\).

If \(|A_n|+|C_n|\le n\), the graph has a perfect matching. Hence for \(\alpha+\beta\le1\) with that finite-size condition, irreversible random greedy deposition nevertheless leaves a **positive macroscopic vacancy fraction**. On the symmetric line \(\alpha=\beta=\theta\),
\[
\boxed{r(\theta,\theta)=\theta\exp\bigl(-(1-\theta)/\theta\bigr).}
\]
For instance, \(\theta=2/5\) gives \(r=(2/5)e^{-3/2}\approx0.08925206406\), despite the availability of a perfect matching.

## Assumptions and scope

The graph is finite, simple, balanced and bipartite. The blocked rectangle is complete: a left vertex in \(A_n\) has no allowed edge to a right vertex in \(C_n\); all other cross-edges are allowed. The sizes of the two blocked subsets may be rounded arbitrarily subject to the stated convergence. Every allowed edge has the same independent continuous priority. Accepted dimers are never removed, and adsorption continues until no admissible edge joins two vacant vertices. The limit holds for every fixed \(\alpha,\beta\in(0,1)\), including \(\alpha+\beta>1\), when no perfect matching is possible. No claim is made when one of the two parameters vanishes with \(n\).

## Proof

**1. Exact process and fluid limit.** Put \(B_n=L_n\setminus A_n\) and \(D_n=R_n\setminus C_n\). At any time let \((A,B,C,D)\) denote the numbers of currently vacant vertices in the four groups. The only admissible edge types, and their exact counts, are
\[
A\text{--}D: AD,\qquad B\text{--}C: BC,\qquad B\text{--}D: BD.
\]
Conditional on at least one such edge existing, the next accepted dimer has these three respective probabilities divided by \(AD+BC+BD\). This follows either by symmetry of remaining edge priorities or by coupling every allowed edge to an independent rate-\(1/n\) exponential clock and accepting its first ring only when both endpoints remain free. The latter clocks are equivalent in distribution to a uniformly random total priority order.

Run the exponential-clock realization in continuous time \(t\). Divide the four vacancy counts by \(n\), writing \((a_n,b_n,c_n,d_n)\). Its jump rates are exactly \(n a_n d_n\), \(n b_n c_n\), and \(n b_n d_n\), respectively, and all jumps have magnitude at most \(1/n\) in each coordinate. On every fixed time interval \([0,T]\), the density vector therefore converges uniformly in probability to the unique solution of the globally Lipschitz polynomial system
\[
\dot a=-ad,\qquad
\dot b=-b(c+d),\qquad
\dot c=-bc,\qquad
\dot d=-d(a+b)
\]
with initial data
\[
(a,b,c,d)(0)=(\alpha,1-\alpha,\beta,1-\beta).
\]
For completeness, the compensated jump-counting processes are martingales with quadratic variations bounded by a constant times \(T/n\); Doob's inequality followed by Grönwall's inequality proves the stated uniform law of large numbers. There is no finite-time singularity because the vector field is polynomial on the invariant compact state cube.

**2. Closed-form solution up to jamming.** Conservation of left–right vacancy balance gives
\[
k(t):=a(t)+b(t)=c(t)+d(t).
\]
Set \(B_0=1-\alpha\), \(D_0=1-\beta\), and
\[
h(t)=\exp\left(-\int_0^t k(s)\,ds\right),\qquad
I(t)=\int_0^t h(s)\,ds.
\]
Solving each scalar equation gives
\[
b(t)=B_0h(t),\quad d(t)=D_0h(t),\quad
a(t)=\alpha e^{-D_0I(t)},\quad
c(t)=\beta e^{-B_0I(t)}.
\]
Using \(a+b=c+d\) yields, when \(\alpha\ne\beta\),
\[
h=\frac{\beta e^{-(1-\alpha)I}-\alpha e^{-(1-\beta)I}}{\beta-\alpha}
=e^{-(1-\alpha)I}\frac{\beta-\alpha e^{(\beta-\alpha)I}}{\beta-\alpha}.
\]
When \(\alpha=\beta=\theta\), its continuous limit is
\[
h=e^{-(1-\theta)I}(1-\theta I).
\]
In either case, the right-hand side is strictly positive for \(0\le I<I_*\), zero at \(I=I_*\), and has no earlier zero. Since \(\dot I=h\), \(I(t)\) is increasing and bounded above by \(I_*\). If its limit were below \(I_*\), its derivative would remain bounded away from zero, a contradiction. Thus \(I(t)\uparrow I_*\), \(h(t)\downarrow0\), and
\[
(a,b,c,d)(t)\longrightarrow(r,0,r,0).
\]
The equality of the two remaining nonzero coordinates also follows from the explicit identity
\(\alpha e^{-(1-\beta)I_*}=\beta e^{-(1-\alpha)I_*}\). This proves both the stated formula and its symmetry.

**3. Passing from a finite time to the final jam.** Let \(K_n(t)=(A_n(t)+B_n(t))/n\) be the left-side vacant fraction, and let \(K_n(\infty)=U_n/n\). Every admissible edge touches at least one vertex in \(B_n\cup D_n\). Consequently, on **every finite sample path**, every future accepted dimer after time \(T\) consumes at least one of the currently vacant vertices in these two groups, so
\[
0\le K_n(T)-K_n(\infty)\le b_n(T)+d_n(T).
\]
For fixed \(T\), the fluid limit gives \(K_n(T)\to k(T)\) and \(b_n(T)+d_n(T)\to b(T)+d(T)\) in probability. Letting first \(n\to\infty\) and then \(T\to\infty\) squeezes \(K_n(\infty)\) to \(r\) in probability. The same argument gives the final classwise vacancy fractions. Since all fractions are bounded by one, convergence also holds in mean.

**4. Feasibility is not jamming.** If \(|A_n|+|C_n|\le n\), first match every vertex of \(A_n\) to a distinct vertex of \(D_n\), which is possible because \(|A_n|\le|D_n|\). The remaining vertices on the right are all adjacent to every remaining vertex on the left (all in \(B_n\)), so this extends to a perfect matching. The already proved positive value of \(r\) shows that the random greedy mechanism nevertheless fails to realize perfect coverage by an extensive amount.

## Verification

The standalone Python 3 program `verify.py` gives an independent exact-rational recurrence for the finite four-group vacancy chain. For a graph with two vertices on each side and one forbidden pair, direct enumeration of all six allowed-edge priority orders yields terminal left-side vacancy probabilities \(2/3\) for zero vacancies and \(1/3\) for one vacancy, agreeing with the recurrence. With \(n=4\), \(|A_n|=|C_n|=2\), the exact distribution is
\[
\Pr(U_n=0)=\frac{22}{63},\quad
\Pr(U_n=1)=\frac{184}{315},\quad
\Pr(U_n=2)=\frac1{15}.
\]
The program also checks numerous exact normalization and left–right symmetry identities and deterministic-seed simulations for three positive parameter pairs with \(n=2000\). The latter agree with the theoretical values to within the stated finite Monte Carlo tolerance. These checks support, but do not replace, the infinite-size martingale and tail argument.

Run with `python verify.py`; no third-party packages, external data or network access are needed.

## Relationship to prior work

Random sequential adsorption on graphs is classical; the edge-exclusion setting appears in Pippenger's 1989 study and the broad physical framework in Evans's 1993 review. Dyer and Frieze (1991) analyzed random greedy matching on fixed graphs, particularly worst-case behavior and sparse classes. Mastin and Jaillet (2013) derived differential-equation asymptotics for **online vertex-arrival** greedy matching on independently generated bipartite random graphs. That input distribution and arrival mechanism are different from uniform edge-priority adsorption on this deterministic graph with a macroscopic forbidden rectangle. Arnosti (2021) compared greedy algorithms on random-edge-set models rather than determining this fixed-substrate explicit jamming fraction. The present result is the closed-form limit for this specific dense two-class substrate and the demonstration of extensive kinetic loss despite a perfect matching.

## Limitations

This is a law of large numbers for fixed positive blocked-subset fractions, not a finite-size rate, central limit theorem, or double-scaling statement when a blocked fraction tends to zero. The initial graph has a perfectly homogeneous allowed-edge rate; heterogeneous rates and independently random forbidden edges are not included. It describes random edge-priority kinetic outcomes, not equilibrium dimer ensembles. A complete full-text comparison with the 1991 Dyer–Frieze paper was unavailable; although its accessible abstract emphasizes different graph families and worst-case guarantees, an unrecognized closely related worked example remains an originality risk.

## References

1. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401. DOI: 10.1137/0402034.
2. M. Dyer and A. Frieze, *Randomized Greedy Matching*, Random Structures & Algorithms 2 (1991), 29–45. DOI: 10.1002/rsa.3240020104.
3. J. W. Evans, *Random and Cooperative Sequential Adsorption*, Reviews of Modern Physics 65 (1993), 1281. DOI: 10.1103/RevModPhys.65.1281.
4. A. Mastin and P. Jaillet, *Greedy Online Bipartite Matching on Random Graphs*, first arXiv version, 9 July 2013, arXiv:1307.2536v1, https://arxiv.org/abs/1307.2536.
5. N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, Stochastic Systems 12 (2022), 133–150; first publicly available 2021. DOI: 10.1287/stsy.2021.0082.
