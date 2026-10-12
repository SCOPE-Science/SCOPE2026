# Stationary-mass polygon threshold for price-optimal continuous-time star mixing

## Finding
For a reversible continuous-time Markov chain on a star with arbitrary strictly positive stationary masses and independent positive edge prices, the optimal \(L^2(\pi)\) spectral gap, every optimal edge conductance, and its multiplicity admit a closed classification. Let \(m\ge3\), write the hub as \(0\), and let the leaves be \(1,\ldots,m\). Suppose \(\pi_i>0\) and \(\sum_{i=0}^m\pi_i=1\), and give leaf edge \(i\) price \(c_i>0\). Put
\[
 a_i=\pi_i\sqrt{c_i},\qquad S=\sum_{i=1}^m\pi_i c_i,\qquad
 \delta=\max\left\{0,\;2\max_i a_i-\sum_{i=1}^m a_i\right\},\qquad T=S-\delta^2.
\]
Then \(T>0\), the maximum spectral gap is \(\gamma^*=1/T\), and its maximizing conductance vector is unique. If \(\delta=0\),
\[
 w_i^*=\frac{\pi_i}{T}\qquad(1\le i\le m).
\]
If \(\delta>0\), there is a unique index \(j\) with \(a_j>\sum_{i\ne j}a_i\), and
\[
 w_j^*=\frac{\pi_j}{T}\left(1-\frac{\delta}{\sqrt{c_j}}\right),\qquad
 w_i^*=\frac{\pi_i}{T}\left(1+\frac{\delta}{\sqrt{c_i}}\right)\quad(i\ne j).
\]
Every optimal conductance is strictly positive. For \(\delta=0\) the optimal gap has multiplicity \(m-1\); for \(\delta>0\) it is simple. Thus stationary-mass imbalance alone can cause the transition, even when all edge prices coincide.

## Assumptions and scope
Set \(Q_{0i}=w_i/\pi_0\), \(Q_{i0}=w_i/\pi_i\), all other off-diagonal entries zero, and each diagonal entry to minus its off-diagonal row sum. Require \(w_i\ge0\) and \(\sum_i c_iw_i=1\). This is a reversible generator with prescribed stationary distribution \(\pi\). The gap \(\gamma(w)\) means the least strictly positive eigenvalue of \(-Q\) in \(L^2(\pi)\); if the graph is disconnected, define its variational gap as zero. No discrete-time transition-probability or holding-probability upper bounds are imposed. The stated optimum ranges over *every* feasible individual edge allocation, not merely symmetric allocations. The claim applies to every positive real price and mass vector and every integer \(m\ge3\).

## Proof
Let \(z_i=f(i)-f(0)\), let \(p=(\pi_1,\ldots,\pi_m)^\mathsf T\), and let \(V=\operatorname{diag}(p)-pp^\mathsf T\). Directly expanding the stationary variance shows
\[
 \operatorname{Var}_\pi(f)=z^\mathsf T Vz,\qquad
 \mathcal E_w(f,f)=\sum_i w_i z_i^2.
\]
Because \(\pi_0>0\) and every leaf mass is positive, \(V\) is positive definite. Consequently
\[
 \gamma(w)=\min_{z\ne0}\frac{z^\mathsf T\operatorname{diag}(w)z}{z^\mathsf T Vz}.
\]
For positive gap put \(x_i=w_i/\gamma(w)\). The budget implies \(\sum_i c_ix_i=1/\gamma(w)\), while the variational characterization implies \(\operatorname{diag}(x)-V\succeq0\). Conversely, any feasible \(x\) of the minimization below normalizes to a budget-one generator with gap at least the reciprocal cost. Therefore
\[
 T^*=\min_{\operatorname{diag}(x)-V\succeq0}\sum_i c_i x_i,\qquad\gamma^*=1/T^*.
\]
The semidefinite constraint automatically forces \(x_i\ge V_{ii}>0\). Strict primal feasibility holds for sufficiently large coordinates. Its dual, attained with no gap, is
\[
 \max_{Y\succeq0,\;Y_{ii}=c_i}\operatorname{tr}(VY).
\]
Represent \(Y_{ik}=\langle u_i,u_k\rangle\) for vectors \(u_i\) of prescribed lengths \(\sqrt{c_i}\). Then
\[
 \operatorname{tr}(VY)=\sum_i\pi_i\|u_i\|^2-\Big\|\sum_i\pi_i u_i\Big\|^2
 =S-\Big\|\sum_i\pi_i u_i\Big\|^2.
\]
The shortest attainable resultant of vectors of lengths \(a_i=\pi_i\sqrt{c_i}\) is exactly \(\delta=\max(0,2\max_i a_i-\sum_i a_i)\): the triangle inequality gives the lower bound, while the polygon-closing construction attains zero when the longest length does not exceed the remaining sum, and a collinear opposing configuration attains the excess otherwise. Thus strong duality gives \(T^*=S-\delta^2=T\), automatically strictly positive because the primal positive-definite variance matrix forces a positive cost.

For \(\delta=0\), set \(x_i=\pi_i\). Then
\[
 \operatorname{diag}(x)-V=pp^\mathsf T\succeq0,
\]
and the primal cost is \(S=T\). Polygon-closing vectors furnish a dual Gram matrix \(Y\) with \(\sum_i\pi_i u_i=0\), so the primal and dual objectives agree. For any *other* optimum \(x\), equality in positive-semidefinite complementary slackness implies \((\operatorname{diag}(x)-V)Y=0\), equivalently \((x_i-\pi_i)u_i=0\) for each \(i\), because \(pp^\mathsf T Y=0\). Each \(u_i\) is nonzero, so \(x_i=\pi_i\). The slack \(pp^\mathsf T\) has nullity \(m-1\).

For \(\delta>0\), let \(j\) be the unique longest length. Choose the dual Gram vector in one dimension as \(u_j=\sqrt{c_j}\) and \(u_i=-\sqrt{c_i}\) for \(i\ne j\). Then \(p^\mathsf T u=\delta\). Set
\[
 x_j=\pi_j\left(1-\frac{\delta}{\sqrt{c_j}}\right),\qquad
 x_i=\pi_i\left(1+\frac{\delta}{\sqrt{c_i}}\right)\quad(i\ne j).
\]
These values are strictly positive since \(0<\delta<\pi_j\sqrt{c_j}<\sqrt{c_j}\), and a direct multiplication gives \((\operatorname{diag}(x)-V)u=0\). To show positive semidefiniteness (not just a zero eigenvalue), write the slack as \(D+pp^\mathsf T\), with
\[
 D_{jj}=-\frac{\pi_j\delta}{\sqrt{c_j}},\qquad
 D_{ii}=\frac{\pi_i\delta}{\sqrt{c_i}}>0\quad(i\ne j).
\]
The principal block away from \(j\) is positive definite. Its Schur complement at \(j\) equals
\[
 -\frac{\pi_j\delta}{\sqrt{c_j}}+
 \frac{\pi_j^2}{1+\sum_{i\ne j}\pi_i\sqrt{c_i}/\delta}=0,
\]
using \(\pi_j\sqrt{c_j}=\delta+\sum_{i\ne j}\pi_i\sqrt{c_i}\). Hence the full slack is positive semidefinite of rank \(m-1\). Its objective cost is
\[
 \sum_i c_i x_i=S-\delta\big(\pi_j\sqrt{c_j}-\sum_{i\ne j}\pi_i\sqrt{c_i}\big)=S-\delta^2=T,
\]
so it is optimal. Finally, at every optimum complementary slackness with the rank-one dual \(uu^\mathsf T\) forces \((\operatorname{diag}(x)-V)u=0\), which determines every \(x_i\) uniquely, as all \(u_i\ne0\). The slack has nullity one. Normalization \(w_i=x_i/T\) proves the formulas, uniqueness and multiplicities, including the transition boundary.

## Verification
The accompanying `verify.py` uses exact rational arithmetic when \(\sqrt{c_i}\) is rational. It checks every principal minor of the candidate semidefinite slack, exact budget and rank deficiency, and compares the resulting analytic spectral gap to the computed minimum generalized eigenvalue. Running `python verify.py` produced:

`VERIFY_OK 321 exact budget/PSD/duality cases, 114 imbalanced, numerical generalized eigenvalue checks`

This comprises 320 seeded instances with three through six leaves plus a deliberate mass-imbalance example. The universal proof above does not depend on the finite tests. In particular, a numerical eigenvalue comparison is not a proof of global optimality.

With \(\pi_0=1/5\), \(\pi_1=7/10\), \(\pi_2=\pi_3=1/20\), and all prices one, the exact result is \(\delta=3/5\), \(T=11/25\), \(\gamma^*=25/11\), and \((w_1^*,w_2^*,w_3^*)=(7/11,2/11,2/11)\). By contrast, equal leaf masses with the same hub mass and prices lie in the polygon regime with equal optimal conductances.

## Relationship to prior work
Göring, Helmberg and Wappler (2005) derive the primal-dual spectral optimization and graph-embedding framework for unweighted vertex variance and a unit total edge-weight budget; that framework underlies the semidefinite method here but does not give the arbitrary stationary-mass, arbitrary edge-price star classification. Boyd, Diaconis and Xiao (2004) treat the fastest discrete-time mixing chain, including reversible stationary-distribution variants, under discrete-time transition constraints and a different objective. Jafarizadeh (2020) gives a star formula for the *discrete-time* reversible fastest-mixing problem with arbitrary equilibrium masses, but without independent conductance purchase prices; it is not the continuous-time budgeted polygon formula above. The present result specializes to familiar equal-mass priced-star optimization and to three-vertex birth-death chains, without claiming those subcases as new.

## Limitations
The theorem does not optimize discrete-time second-largest-eigenvalue modulus, allow zero stationary masses, or include extra constraints on individual rates. It establishes global uniqueness under the stated linear budget only. The closed formula is a specialization of a general semidefinite variational principle; an equivalent formulation in older specialized literature cannot be excluded by source search alone. The historical unweighted-star theory and generalized path results should not be misattributed to this finding. No independent audit has been performed.

## References
1. F. Göring, C. Helmberg, M. Wappler, *Embedded in the Shadow of the Separator*, public preprint September 2, 2005. https://optimization-online.org/2005/09/1202/ ; full text https://optimization-online.org/wp-content/uploads/2005/09/1202.pdf .
2. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46(4), 667–689 (2004), https://web.stanford.edu/~boyd/papers/fmmc.html .
3. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), https://web.stanford.edu/~boyd/papers/pdf/fmmc_sym.pdf .
4. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks 6, 88–104 (2020), doi:10.1109/TSIPN.2020.2964211 ; https://arxiv.org/abs/2501.02421 (subsequently uploaded preprint).
