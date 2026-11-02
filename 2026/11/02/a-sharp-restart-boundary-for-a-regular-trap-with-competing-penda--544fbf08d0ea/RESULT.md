# A sharp restart boundary for a regular trap with competing pendant targets

## Finding
Let \(H\) be any simple \(d\)-regular graph on \(m\ge2\) vertices, with \(0\le d\le m-1\) and \(md\) even. Join a new apex \(o\) to all vertices of \(H\) and attach \(L\ge1\) pendant leaves to \(o\). Mark one leaf \(t\) as the target. A discrete-time simple random walk starts at \(o\); independently at every step, with probability \(r\in[0,1)\) it returns to \(o\) (consuming a step), and otherwise chooses an ordinary uniform neighbor. Let \(T\) be the first hitting time of \(t\).

**Complete finite law and topology invariance.** Put
\[
p=\frac{1-r}{m+L},\quad v=\frac{m(1-r)}{m+L},\quad w=\frac{(L-1)(1-r)}{m+L},\quad q=r+\frac{1-r}{d+1}.
\]
For \(0\le z<1\), the probability-generating function is
\[
\mathbb E[z^T]=\frac{zp\,[1-z(1-q)]}{(1-zr-z^2w)[1-z(1-q)]-z^2vq}.
\]
Thus the *entire first-passage law*, not merely its mean, is unchanged by replacing \(H\) with any other \(d\)-regular graph of the same order (even a disconnected one). For fixed \(m,L,r<1\), the law is nondecreasing in stochastic order with \(d\). Its mean is exactly
\[
F_{m,d,L}(r)=\frac{m+L}{1-r}+\frac{m(d+1)}{1+dr}+L-1.
\]

**Sharp restart threshold and unique optimizer.** Zero resetting is the unique mean-optimal choice if and only if
\[
md(d+1)\le m+L.
\]
Otherwise the unique global minimizer is
\[
r_* = \frac{\kappa-1}{\kappa+d},\qquad
\kappa=\sqrt{\frac{md(d+1)}{m+L}}>1,
\]
and its minimum equals
\[
F_{m,d,L}(r_*)=\left(\sqrt{\frac{(m+L)d}{d+1}}+\sqrt m\right)^2+L-1.
\]
In particular the exact transition, for each feasible positive \(d\), is \(L=m[d(d+1)-1]\). At equality, the minimum is still uniquely at \(r=0\). When \(d=0\), resetting never helps.

**Universal rare-target limit.** For any sequence of such graphs with \(m\to\infty\), \(d\to\infty\), and \(L/m\to\lambda\in[0,\infty)\), the optimal restart probabilities and optimally controlled hitting times satisfy
\[
r_*\longrightarrow\frac{1}{1+\sqrt{1+\lambda}},\qquad
\frac{T}{m}\ \Longrightarrow\ \operatorname{Exp}\!\left(\frac{1}{C_\lambda}\right),\qquad
\frac{\mathbb ET}{m}\longrightarrow C_\lambda=2\sqrt{1+\lambda}\,(1+\sqrt{1+\lambda}).
\]
Here \(\operatorname{Exp}(1/C_\lambda)\) has mean \(C_\lambda\). Without restarting, \(\mathbb ET=m(d+2)+2L-1\). Hence the ratio of the no-restart and optimal means diverges when \(d\to\infty\), uniformly in the internal topology of the regular core.

## Assumptions and scope
The graph is finite, simple and undirected. The core may be disconnected because adding \(o\) makes the whole graph connected. Only one of the \(L\) pendant vertices is absorbing; all other pendant vertices are ordinary decoy leaves. Resetting occurs *before* a proposed ordinary move, and a reset consumes one unit of time, including resets already at \(o\). The target is not reset to before its first visit. All distributional statements concern a walk initially at \(o\), not an arbitrary source; parameters and the restart probability are deterministic. The limiting graphs can be any sequence satisfying the integer feasibility constraints; no graph expansion or mixing assumption is needed.

## Proof
**(1) Exact reduction.** There are three nonabsorbing classes: the apex \(o\), the core \(H\), and the \(L-1\) decoy leaves. At every core vertex the probability of returning to \(o\) in the next step is \(q=r+(1-r)/(d+1)\), independent of its location and the adjacency pattern in \(H\). A decoy leaf returns to \(o\) with probability one in the next step. From \(o\), the transition probabilities to the target, core, decoys and \(o\) are respectively \(p,v,w,r\). Thus the partition is strongly lumpable up to absorption.

Let \(A(z),B(z),D(z)\) denote the generating functions of the remaining time to hit the target when starting at \(o\), a core vertex, and a decoy leaf. First-step conditioning gives
\[
B(z)=zqA(z)+z(1-q)B(z),\quad D(z)=zA(z),\quad
A(z)=z\{p+rA(z)+vB(z)+wD(z)\}.
\]
Eliminating \(B,D\) gives the displayed rational probability-generating function. The reduction is exact for every \(H\) in the stated class; the poles are not invoked to prove any claimed asymptotic.

**(2) Mean and stochastic comparison.** First-step mean equations are \(E_H=E_o+1/q\), \(E_D=E_o+1\) and \(E_o=1+rE_o+vE_H+wE_D\). Solving yields \(E_o=(1+v/q+w)/p\), which simplifies to \(F_{m,d,L}(r)\). For the stochastic comparison, construct successive visits to \(o\) using the same independent source choice (target, reset, core, or decoy) for two permissible core degrees. When the core is entered, couple its sojourn durations as geometric variables with parameters \(q(d)=r+(1-r)/(d+1)\). Since \(q(d)\) decreases with \(d\), inverse-uniform coupling orders all such durations. The time to the common first target choice, and hence its law, is ordered. This proves all-deadline dominance without comparing internal core edges.

**(3) Global optimality.** Direct differentiation gives
\[
F'(r)=\frac{m+L}{(1-r)^2}-\frac{md(d+1)}{(1+dr)^2},\quad
F''(r)=\frac{2(m+L)}{(1-r)^3}+\frac{2md^2(d+1)}{(1+dr)^3}>0.
\]
The function tends to infinity as \(r\uparrow1\); its right derivative at zero has sign \(m+L-md(d+1)\). Strict convexity therefore establishes the exact boundary and uniqueness, including equality. When this derivative is negative, solving \(F'(r_*)=0\) gives the stated \(r_*\). Set \(x=1-r\) and \(c=d/(d+1)\); minimizing \((m+L)/x+m/(1-cx)\) by the equality case of \(a/y+b/(1-y)\ge(\sqrt a+\sqrt b)^2\) gives the minimum. The case \(d=0\) is immediate.

**(4) Limit at the optimal restart.** Let \(a=\sqrt{1+\lambda}\). Since \(d,m\to\infty\), the exact optimizer converges to \(r_\lambda=1/(1+a)\), while \(p_m\sim 1/[ma(1+a)]\) and \(q_m\to r_\lambda>0\). At successive visits to \(o\), the next step hits the marked leaf with independent probability \(p_m\). Thus the number of trials \(N_m\) through the successful one is geometric with parameter \(p_m\), giving \(N_m/m\Rightarrow\operatorname{Exp}(1/[a(1+a)])\).

Given a failed trial, its length is one step for a reset, two for a decoy visit, or one plus an independent geometric return time of parameter \(q_m\) after a core entry. Failed trials are independent and identically distributed; their conditional mean is
\[
\mu_m=\frac{r_m+2w_m+v_m(1+q_m^{-1})}{1-p_m}
=\frac{1-p_m+w_m+v_m/q_m}{1-p_m}\longrightarrow2.
\]
Their second moments are uniformly bounded because \(q_m\) is bounded away from zero. Conditional variance estimates therefore show that their total duration, divided by \(N_m\), converges in probability to two; the final successful trial has duration one. Consequently \(T/m\Rightarrow\operatorname{Exp}(1/[2a(1+a)])\). Independently, substituting the optimizer into the exact mean yields \(\mathbb ET/m\to2a(1+a)=C_\lambda\), proving the stated moment claim. At \(r=0\), the exact mean from (2) is \(m(d+2)+2L-1\), completing the comparison.

## Verification
Run `python checker.py` using Python 3's standard library. The checker constructs multiple explicit regular cores, solves full vertex-state first-passage equations with exact fractions, compares 10 exact first-passage probabilities with the three-class recursion, and compares independently computed full-matrix generating functions with the closed expression at two rational arguments. It also tests global optima, the exact boundary, and the proposed asymptotic constants. All 5,247 assertions passed for the packaged checker. These finite tests corroborate the proof; they do not prove the infinite family or the weak limit.

## Relationship to prior work
The general discrete-time resetting model and spectral mean-first-passage formulas occur in Riascos, Boyer, Herringer and Mateos (2019/2020); the full-model mean formula here is not represented as a new general restart identity. Riascos, Boyer and Mateos (2021) give a general criterion for when restart improves a first-passage mean and discuss rings and Cayley trees. Zelenkovski and colleagues (2023) analyze centrality-based resets on lollipops, barbells and trees, primarily through global mean first-passage time. The present claim is the *joint finite topology-invariant law, closed integer restart boundary, unique optimal rate and topology-independent exponential rare-target crossover* for the specified regular-core/pendant-target class. Those specific results are not stated in the compared material. The general Markov/renewal framework is prior work and provides a possible alternative derivation of parts of the finite formulas.

## Limitations
The regularity of \(H\) is essential for the exact three-class lumpability; arbitrary irregular cores are not covered. The exponential limit requires both core order and degree to diverge and the pendant-to-core ratio to converge to a finite number. The result does not optimize other reset protocols, arbitrary reset locations, or hitting different target types. The full priority of this specific classification is not independently established; general resetting identities may yield overlapping corollaries after algebraic specialization.

## References
1. A. P. Riascos, D. Boyer, P. Herringer and J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568 (first posted 2019-10-29), https://arxiv.org/abs/1910.13568.
2. A. P. Riascos, D. Boyer and J. L. Mateos, *Discrete-time random walks and Lévy flights on arbitrary networks: when resetting becomes advantageous?*, arXiv:2110.15437 (first posted 2021-10-28), https://arxiv.org/abs/2110.15437.
3. K. Zelenkovski et al., *Random Walks on Networks with Centrality-Based Stochastic Resetting*, *Entropy* 25 (2023), 293, https://doi.org/10.3390/e25020293.
