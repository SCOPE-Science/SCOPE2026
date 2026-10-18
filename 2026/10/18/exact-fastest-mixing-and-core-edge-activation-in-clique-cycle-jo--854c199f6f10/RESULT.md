# Exact fastest mixing and core-edge activation in clique–cycle joins

## Finding

Let \(k\ge 2\) and \(m\ge4\) be integers. On the graph \(G_{k,m}=K_k\vee C_m\), minimize the second-largest eigenvalue modulus (SLEM) over **all** symmetric, entrywise nonnegative, row-stochastic matrices supported on the graph's edges and diagonal. There is no assumption that edge probabilities are constant on automorphism orbits before optimization.

Write
\[
\delta_m=2-2\cos(2\pi/m),\qquad
\Delta_m=2-2\cos\!\left(2\pi\lfloor m/2\rfloor/m\right),
\]
\[
\rho_m=\frac{\Delta_m-\delta_m}{\Delta_m+\delta_m},\qquad
\tau_m=\frac{m\rho_m}{1+\rho_m}=\frac{m(\Delta_m-\delta_m)}{2\Delta_m}.
\]
Define
\[
 a_0=\frac{1+\rho_m}{m+k(1+\rho_m)},\qquad
 a_*=\min\{1/m,a_0\},\qquad
 b_*=\frac{2(1-ka_*)}{\delta_m+\Delta_m}.
\]
The exact optimum is
\[
 \boxed{\mu_*(k,m)=\rho_m(1-ka_*)}.
\]
One globally optimal kernel assigns probability \(a_*\) to each core-to-cycle edge, probability \(b_*\) to each cycle edge, and probability
\[
 c_*=\frac{1-ma_*}{k}
\]
to each edge inside the \(k\)-vertex core clique. Its diagonal entries are then fixed by the row sums. In particular the hub/core holding probability is \((1-ma_*)/k\), and each cycle vertex holds with probability \(1-ka_*-2b_*>0\).

**Complete symmetry-invariant optimizer characterization.** All optimal kernels invariant under permutations of the core and dihedral symmetries of the cycle use exactly \(a=a_*\) and \(b=b_*\). Their common core-clique-edge probability \(c\) ranges over precisely
\[
\boxed{
\max\left\{0,\frac{1-ma_*-\mu_*}{k}\right\}
\le c\le
\min\left\{\frac{1-ma_*+\mu_*}{k},\frac{1-ma_*}{k-1}\right\}.
}
\]
There is a three-regime activation law (equalities belong to the earlier regime):

1. If \(k\le\tau_m\), all globally optimal kernels, including asymmetric ones, give zero probability to every core-clique edge and have zero holding probability at every core vertex.
2. If \(\tau_m<k\le2\tau_m\), there are globally optimal kernels both with all core-clique edges suppressed and with positive equal core-clique-edge probabilities.
3. If \(k>2\tau_m\), every globally optimal kernel assigns positive probability to at least one core-clique edge; every symmetry-invariant optimum assigns a strictly positive common probability to all of them.

As \(m\to\infty\) and \(k/m\to\alpha\ge0\) through integer pairs with \(k\ge2\), the optimal SLEM has the limit
\[
\boxed{
\lim\mu_*(k,m)=
\begin{cases}
1-\alpha,&0\le\alpha\le\tfrac12,\\[2pt]
(1+2\alpha)^{-1},&\alpha\ge\tfrac12.
\end{cases}}
\]
The boundaries for the two core-edge activation transitions scale to \(\alpha=1/2\) and \(\alpha=1\), respectively.

## Assumptions and scope

The graph join \(K_k\vee C_m\) consists of a clique of \(k\) core vertices, a disjoint cycle of \(m\) rim vertices, and every edge between the two sets. A kernel may have zero probabilities on existing edges, and self-holding is allowed. Each undirected edge has the same probability in both directions; arbitrary independent edge probabilities are initially permitted. The objective is the spectral norm of \(P-\mathbf1\mathbf1^T/(k+m)\), i.e. SLEM. All results hold exactly over the real numbers for every stated integer pair.

## Proof

**1. Symmetry reduction without a hidden restriction.** The convex feasible set and the convex objective \(\|P-\mathbf1\mathbf1^T/(k+m)\|_2\) are invariant under \(S_k\times D_m\). Averaging an arbitrary feasible kernel over that group cannot increase SLEM. Hence a globally optimal invariant kernel exists. Such a kernel has a single core-to-rim edge probability \(a\), a single rim-edge probability \(b\), and a single core-clique probability \(c\). Feasibility is exactly
\[
 a,b,c\ge0,\quad ma+(k-1)c\le1,\quad ka+2b\le1.
\]

**2. The complete eigenvalue list.** The orthogonal decomposition into the constant vector, the core-versus-rim constant contrast, the core-sum-zero space, and the nonconstant rim Fourier modes gives respectively
\[
1,\qquad 1-(k+m)a,\qquad 1-ma-kc\ \ (k-1\text{ times}),
\]
\[
1-ka-b(2-2\cos(2\pi j/m)),\qquad j=1,\ldots,m-1.
\]
The extreme nonconstant cycle Laplacian eigenvalues are \(\delta_m\) and \(\Delta_m\). Since the absolute value of a real affine function is convex, the maximum Fourier-mode modulus occurs at one of these two extremes.

**3. Exact elimination of two variables.** For every feasible \(a\le\min\{1/m,1/k\}\), choosing \(c=(1-ma)/k\) is feasible and sets the core-sum-zero eigenvalue to zero. For fixed \(a\), balancing the two extreme rim eigenvalues at equal and opposite values gives the unique minimax choice
\[
 b=\frac{2(1-ka)}{\delta_m+\Delta_m},\qquad
\max_{j\ne0}|\lambda_j|=\rho_m(1-ka).
\]
This \(b\) is feasible because \(\delta_m+\Delta_m>4\): for even \(m\), \(\Delta_m=4\) and \(\delta_m>0\); for odd \(m\), the sum is \(4+2(\cos(\pi/m)-\cos(2\pi/m))>4\). Thus the original three-variable problem reduces exactly to
\[
\min_{0\le a\le\min\{1/m,1/k\}}
\max\left\{\left|1-(k+m)a\right|,\rho_m(1-ka)\right\}.
\]
The first term decreases until \(a=1/(k+m)\) and then increases; the second decreases strictly throughout the feasible interval. Their positive-branch intersection is \(a_0=(1+\rho_m)/(m+k(1+\rho_m))<1/k\). Hence the unique minimizing \(a\) is \(a_*=\min\{1/m,a_0\}\). At this point the rim term equals the maximum, yielding the claimed optimum and \(b_*\). Both are unique in the invariant class.

**4. Exact core-edge interval and global activation.** With \(a=a_*\) and \(b=b_*\), the only remaining spectral requirement is \(|1-ma_*-kc|\le\mu_*\), combined with \(0\le c\le(1-ma_*)/(k-1)\). This yields the stated closed interval. The condition \(a_0\le1/m\) is exactly \(k\ge\tau_m\). In the saturated regime \(k\le\tau_m\), \(a_*=1/m\), so all invariant optimizers have \(c=0\) and core diagonal zero. Averaging any unrestricted global optimizer has this same property; nonnegativity of all averaged core edges and core diagonal entries forces each corresponding original entry to be zero.

For \(k>\tau_m\), substituting \(a_0\) gives
\[
1-ma_0-\mu_*=
\frac{k(1+\rho_m)-2m\rho_m}{m+k(1+\rho_m)}.
\]
This changes sign at \(k=2\tau_m\): hence \(c=0\) is available exactly through the intermediate regime, while beyond that every invariant optimum requires \(c>0\). If an unrestricted optimal kernel had all core-clique edges zero beyond that boundary, its symmetry-average would have \(c=0\), a contradiction.

**5. Large-size law.** The cycle Laplacian endpoints satisfy \(\delta_m\to0\) and \(\Delta_m\to4\). Consequently \(\rho_m\to1\), \(\tau_m/m\to1/2\), and \(2\tau_m/m\to1\). On the saturation branch \(\mu_*=\rho_m(1-k/m)\); on the interior branch \(\mu_*=m\rho_m/[m+k(1+\rho_m)]\). Taking \(k/m\to\alpha\) gives the two continuous pieces in the formula, including the meeting point \(\alpha=1/2\).

## Verification

The standalone program `verify.py` constructs the proposed full transition matrices and independently solves the three-orbit linear program with SciPy's linear-programming solver for \(2\le k\le11\) and \(4\le m\le40\). For matrices with at most 29 vertices it also diagonalizes the full matrix numerically. It checks phase bounds and interval feasibility, and uses exact rational arithmetic for \(m\in\{4,6\}\). An execution using NumPy and SciPy completed `VERIFY_OK 3929 checks`. These finite tests are corroboration; the proof of the unrestricted infinite-family statement is the analytic argument above.

At the fixed rim order \(m=6\), the three regimes are witnessed by \(k=2,3,6\), respectively. The optimal SLEM values are exactly \(2/5,1/3,3/13\). In the first regime every core-clique edge is suppressed; in the second suppression is optional; in the third it is impossible.

## Relationship to prior work

Boyd, Diaconis and Xiao introduced the general fastest-mixing convex optimization; Boyd, Diaconis, Parrilo and Xiao proved symmetry reduction and solved the single-hub wheel \(K_1\vee C_m\) explicitly in Section 5.4.3 of their 2007 preprint / 2009 paper. Those methods establish the framework but the wheel formula does not cover the nonuniform stationary mass on the core arising from \(k\ge2\), and it has no nontrivial core-clique edges.

Jafarizadeh's theorem on clique-lifted reversible chains supplies a general reduction from such a lift to a nonuniform-stationary base graph. It can apply to this topology, but the inspected results do not evaluate the relevant nonuniform wheel minimax problem or give the three core-edge-use thresholds or the complete optimal invariant interval. This finding addresses those explicit quantitative gaps. It is not claimed that general convexity, orbit averaging, clique lifting, or the one-hub wheel result are new.

## Limitations

Only real symmetric stochastic kernels with uniform equilibrium distribution and optional holding are considered. The formulas characterize all **invariant** optimal kernels and specific edge-support necessities for **all** optimal kernels, but do not classify every unrestricted asymmetric optimizer. They do not optimize finite-time total variation mixing, nonreversible kernels, or random walks with a prescribed nonuniform stationary distribution. Equivalent results under a different terminology or in incompletely indexed sources are possible; independent mathematical validation has not been performed.

## References

1. S. Boyd, P. Diaconis, and L. Xiao, *Fastest mixing Markov chain on a graph*, SIAM Review **46** (2004), 667–689. Author's openly accessible version: https://web.stanford.edu/~boyd/papers/fmmc.html .
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest mixing Markov chain on graphs with symmetries*, arXiv:0709.0955 (first arXiv version 6 September 2007), especially Section 5.4.3; SIAM Journal on Optimization **20** (2009), 792–819. https://arxiv.org/abs/0709.0955 .
3. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks **6** (2020), 88–104; arXiv:2501.02421 (2025 version), especially Section 3, Theorem 1. https://arxiv.org/abs/2501.02421 .
