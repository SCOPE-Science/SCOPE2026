# D-optimal cyclic ladders with a linear-price crossover

## Finding

Let \(n\ge3\) be an integer, and put a nonnegative independent conductance on each of the \(3n\) edges of the simple prism \(G_n=C_n\mathbin{\square}K_2\). Every cycle edge has price \(P>0\), every rung has price \(Q>0\), and the total budget is \(B>0\). Among all such conductances of total price at most \(B\), the weighted spanning-tree enumerator \(\tau\) has a **unique** maximizer; its \(2n\) cycle edges have a common strictly positive conductance \(a\), and its \(n\) rungs have a common strictly positive conductance \(b\).

Write \(t=b/a\), \(d_k=1-\cos(2\pi k/n)\), and
\[
S_n(t)=\sum_{k=0}^{n-1}\frac1{t+d_k},\qquad
H_n(t)=\frac{2S_n(t)}{2n-1-tS_n(t)}.
\]
Then \(H_n\) decreases strictly and continuously from \(+\infty\) to \(0\), and the exact optimizer is
\[
H_n(t_*)=\frac QP,\qquad
 a_* = \frac B{n(2P+Qt_*)},\qquad b_*=t_*a_*.
\]
In particular, the fraction of the budget spent on rungs is exactly
\[
 f_* = \frac{Qt_*}{2P+Qt_*}=\frac{t_*S_n(t_*)}{2n-1},\qquad
\frac1{2n-1}<f_*<\frac n{2n-1}.
\]
The two inequalities are sharp limiting bounds, approached respectively as \(Q/P\to\infty\) and \(Q/P\to0\).

For fixed \(P,Q>0\), as \(n\to\infty\), the unique ratio converges to the positive constant
\[
 t_\infty=\frac{2}{3Q}\left(P-2Q+\sqrt{(P-2Q)^2+3P^2}\right).
\]
More surprisingly, when rung prices instead grow as \(Q_n=\kappa n\) for fixed \(\kappa>0\) and fixed \(P>0\), a different scale appears:
\[
 n^2t_*\longrightarrow u_{P,\kappa},\qquad
 \frac{\coth\sqrt{u_{P,\kappa}/2}}{\sqrt{2u_{P,\kappa}}}=\frac\kappa P.
\]
The displayed equation has exactly one positive solution. In this regime, \(a_*\sim B/(2Pn)\), \(b_*\sim Bu_{P,\kappa}/(2Pn^3)\), and \(f_*\sim\kappa u_{P,\kappa}/(2Pn)\). With \(g(u)=\coth\sqrt{u/2}/\sqrt{2u}\), a more precise expansion is
\[
 t_*=\frac{u_{P,\kappa}}{n^2}+\frac{v_{P,\kappa}}{n^3}+O(n^{-4}),\quad
 v_{P,\kappa}=-\frac{g(u_{P,\kappa})[1+u_{P,\kappa}g(u_{P,\kappa})]}{2g'(u_{P,\kappa})}>0.
\]
All asymptotics hold for fixed displayed positive parameters; the remainder constants may depend on them.

## Assumptions and scope

The prism has vertex set \(\{(j,\varepsilon):j\in\mathbb Z/n\mathbb Z,\ \varepsilon\in\{0,1\}\}\), two cyclic edge orbits \((j,\varepsilon)\leftrightarrow(j+1,\varepsilon)\), and one rung orbit \((j,0)\leftrightarrow(j,1)\). All edge conductances are individually free and nonnegative. The objective is the sum, over all spanning trees, of the product of their constituent edge conductances. A disconnected allocation has \(\tau=0\). This is determinant-based network design, not an optimization of effective-resistance sums or the algebraic connectivity. The range \(n\ge3\) ensures a simple connected underlying graph.

## Proof

**1. Global symmetry and uniqueness without assuming it.** For an edge-weight vector \(w\), let \(L_0(w)\) be a fixed reduced weighted Laplacian of order \(2n-1\). The matrix-tree theorem gives \(\tau(w)=\det L_0(w)\). On connected nonnegative allocations, the reduced matrix is positive definite and \(\log\det\) is strictly concave in \(w\): distinct vectors define distinct grounded matrices, because every off-diagonal entry determines the weight of its edge (and the grounded vertex's incident weights follow from the diagonal entries). The total-price feasible set is compact. It contains connected positive allocations, so an optimum has positive determinant. Strict concavity makes it unique. All graph automorphisms preserve both budget and determinant, and hence fix that unique optimizer. Rotations and exchange of the two rings act transitively on each edge type, showing that cycle conductances equal \(a\ge0\) and rung conductances equal \(b\ge0\). If either equals zero the network disconnects, so both are strictly positive. Scaling all weights by a common factor raises \(\tau\) to degree \(2n-1\); consequently the full budget is used: \(n(2Pa+Qb)=B\).

**2. Exact weighted tree polynomial and stationarity.** For constant \(a,b\), symmetric and antisymmetric Fourier modes along the two rings give Laplacian eigenvalues \(2ad_k\) and \(2ad_k+2b\), respectively. Only the symmetric mode with \(k=0\) vanishes. The matrix-tree product and the Chebyshev identity yield
\[
 \tau_n(a,b)=\frac1{2n}\prod_{k=1}^{n-1}2ad_k\prod_{k=0}^{n-1}(2ad_k+2b)
 =n a^{2n-1}\big[T_n(1+b/a)-1\big],
\]
where \(T_n(\cos\theta)=\cos(n\theta)\). Its unweighted specialization is known; the optimization is the subject here. Set \(t=b/a\) and substitute \(a=B/[n(2P+Qt)]\). Differentiating the logarithm of the determinant along this positive ray gives
\[
 \frac{d}{dt}\log\tau_n=
 S_n(t)-\frac{(2n-1)Q}{2P+Qt},\qquad
 S_n(t)=\frac{T_n'(1+t)}{T_n(1+t)-1}.
\]
(The last equality follows from the product over \(k\), including multiplicities.) Stationarity is equivalent to \(H_n(t)=Q/P\).

**3. Strict monotonicity and allocation thresholds.** Since each \(d_k\ge0\), the denominator \(2n-1-tS_n(t)\) is strictly positive: \(1<tS_n(t)<n\) for \(t>0\). Differentiation gives
\[
 H_n'(t)=\frac{2[(2n-1)S_n'(t)+S_n(t)^2]}{[2n-1-tS_n(t)]^2}<0,
 \quad S_n'(t)=-\sum_{k=0}^{n-1}(t+d_k)^{-2}.
\]
Cauchy--Schwarz gives \(S_n(t)^2\le n\sum_k(t+d_k)^{-2}\), and \(n<2n-1\). As \(t\downarrow0\), \(S_n(t)\sim1/t\) and \(H_n(t)\sim1/[(n-1)t]\); as \(t\to\infty\), \(S_n(t)\sim n/t\) and \(H_n(t)\sim2n/[(n-1)t]\). Therefore the stationarity equation has exactly one positive solution, necessarily the global maximizer already shown unique. The budget fraction identity follows by multiplying the stationarity equation by \(t\). Since \(tS_n(t)=1+\sum_{k=1}^{n-1}t/(t+d_k)\) is strictly increasing between \(1\) and \(n\), both sharp bounds and their price-limit orientation follow. In particular \(t_*\sim P/[(n-1)Q]\) as \(Q/P\to\infty\) and \(t_*\sim2nP/[(n-1)Q]\) as \(Q/P\to0\), with \(n\) fixed.

**4. Closed spectral resolvent and fixed-price limit.** The cycle resolvent sum has the exact finite identity
\[
 S_n(t)=\frac{n}{\sqrt{t(t+2)}}\coth\!\left(\frac n2\operatorname{arcosh}(1+t)\right).
\]
Indeed the positive Fourier eigenvalue denominators factor with the two roots of the quadratic recurrence associated to \(t+1-\cos\theta\); summing their geometric images around the cycle gives the displayed hyperbolic expression. Equivalently it follows by logarithmically differentiating \(T_n(1+t)-1=\cosh[n\operatorname{arcosh}(1+t)]-1\). For each fixed \(t>0\), \(S_n(t)/n\to1/\sqrt{t(t+2)}\) exponentially. Therefore
\[
 H_n(t)\to \frac{2}{2\sqrt{t(t+2)}-t}.
\]
These functions decrease from infinity to zero; monotone-root bracketing puts their unique roots in a common compact positive interval and yields convergence. Solving the limiting stationarity equation and retaining the positive root gives the formula for \(t_\infty\) above.

**5. The linearly priced crossover and correction.** Fix \(Q_n=\kappa n\). The stationarity equation gives
\[
 \frac{S_n(t_*)}{n^2}=\frac{\kappa}{2P}\left(2-\frac{1+t_*S_n(t_*)}{n}\right),
\]
so, using \(1<tS_n(t)<n\), its left-hand side stays between positive constants. The resolvent formula implies \(n^{-2}S_n(u/n^2)\to g(u)=\coth\sqrt{u/2}/\sqrt{2u}\), uniformly with an \(O(n^{-2})\) error for \(u\) in compact positive intervals. Since \(g\) is strictly decreasing from infinity to zero, comparison at two fixed values of \(u\) brackets \(n^2t_*\) and proves convergence to the unique \(u\) satisfying \(g(u)=\kappa/P\). Substitute \(t_*=u/n^2+v/n^3\) into the stationarity equation, using the uniform analytic resolvent expansion and \(g'(u)<0\). At relative order \(1/n\), the equation is
\[
 2v g'(u)+g(u)[1+u g(u)]=0.
\]
The implicit function theorem, with uniformly controlled derivatives near \(u\), gives the stated \(O(n^{-4})\) remainder and the positive correction \(v\). The asymptotic conductance and spend expressions then follow directly from the budget formula.

## Verification

The standalone standard-library Python script `verify_prism.py` reproduces exact rational matrix-tree determinants using Bareiss elimination, compares the Chebyshev expression on multiple graph sizes, checks the cycle resolvent and derivative ordering numerically, samples thousands of independently weighted feasible competitor graphs, and checks both extreme-price budgets and the linearly priced scaling regime. Running `python3 verify_prism.py` completed **23,668 checks** with no asserted failure. Finite tests corroborate the calculation but do not establish the infinite-parameter claims; those are proved by the symbolic arguments above.

## Relationship to prior work

The unweighted prism spanning-tree count is classical (Boesch--Bogdanowicz, 1987; Jagers, 1988), and the Chebyshev product recovers it as a specialization; this count is explicitly **not** claimed as original. The general use of log-determinants and weighted spanning-tree counts as graph-design criteria is developed, among other places, by Khosoussi et al. (arXiv:1604.01116v1, first publicly posted 2016-04-05), which emphasizes graph edge-selection and relaxations rather than the complete independent-conductance price optimization here. Sun--Wang--Zhang (2016) enumerate trees in prism-related families by combinatorial recurrences but do not supply the stated allocation and large-price crossover. A previously published finite-ladder determinantal-kernel result addresses a different graph with boundaries and not the cyclic price-constrained global optimum. Claims of priority are limited to the exact all-price allocation, spend-fraction law and linear-price scaling, not generic matrix-tree optimization or the unweighted enumeration.

## Limitations

Only prisms with \(n\ge3\), nonnegative edge conductances, two constant positive price classes and a total linear budget are covered. The finite optimal ratio is characterized implicitly by a unique scalar root rather than a uniform radical formula. The spectral asymptotics assume fixed \(P,\kappa,B>0\), and they do not describe arbitrary simultaneous scaling of all prices. A closely related early unweighted-prism paper was identifiable but its complete text could not be materially checked; an unlocated specialist result deriving the same priced-optimization theorem remains a priority risk. No claim is made about effective-resistance design, arbitrary graph topologies, stability of algorithms or independent verification of the mathematical proof.

## References

1. Khosoussi, Sukhatme, Huang and Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116v1 (first public posting 2016-04-05). https://arxiv.org/abs/1604.01116 .
2. Sun, Wang and Zhang, *Counting Spanning Trees in Prism and Anti-prism Graphs*, Journal of Applied Analysis and Computation (2016), DOI:10.11948/2016006. https://www.jaac-online.com/data/article/jaac/preview/pdf/20160106.pdf .
3. Boesch and Bogdanowicz, *The number of spanning trees in a prism*, International Journal of Computer Mathematics (1987), DOI:10.1080/00207168708803568.
4. Jagers, *A Note on the Number of Spanning Trees in a Prism Graph*, International Journal of Computer Mathematics (1988), DOI:10.1080/00207168808803639.
