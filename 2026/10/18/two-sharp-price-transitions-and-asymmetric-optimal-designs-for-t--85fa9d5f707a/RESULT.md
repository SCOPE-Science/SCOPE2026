# Two sharp price transitions and asymmetric optimal designs for two-community fastest diffusion

## Finding

Let integers \(p\ge q\ge2\), \(N=p+q\), budget \(B>0\), and internal-edge price \(t>0\) be given. Partition the vertices of a complete graph into labeled communities \(A\) and \(C\) of sizes \(p\) and \(q\). Every cross-community edge has price \(1\), and every within-community edge has price \(t\). Choose every nonnegative, undirected edge conductance independently, with total weighted cost at most \(B\). Let \(\Lambda(p,q,t,B)\) be the maximum second-smallest weighted-Laplacian eigenvalue.

For \(p>q\), define the *two distinct prices*
\[
\tau_1=\frac{2pq}{2pq-p-q},\qquad \tau_2=\frac{2p}{p-1},\qquad 0<\tau_1<\tau_2.
\]
Then the exact optimum is
\[
\Lambda=\begin{cases}
\displaystyle\frac{BN}{pq+t[\binom p2+\binom q2]}, &0<t\le\tau_1,\\[5pt]
\displaystyle\frac{B}{q+\frac{t(p-1)(p-q)}{2p}}, &\tau_1\le t\le\tau_2,\\[5pt]
\displaystyle\frac Bp, &t\ge\tau_2.
\end{cases}
\]
At the displayed shared endpoints, adjacent formulas agree. When \(0<t<\tau_1\), the **unique global optimizer** assigns the common weight \(\Lambda/N\) to *all edges*, despite their unequal prices. When \(\tau_1<t<\tau_2\), the unique optimizer assigns cross-edge weight \(\Lambda/p\), weight \(\Lambda(p-q)/p^2\) within the larger community, and zero within the smaller. When \(t>\tau_2\), every optimizer deletes all within-community edges and has optimal value \(B/p\); the cross-edge weights need not be uniform. The uniform cross-edge assignment \(B/(pq)\) is one optimizer, but there also exist strictly positive **asymmetric** cross-edge assignments attaining the same optimum.

For \(p=q=m\ge2\), there is a single transition price \(\tau=m/(m-1)\). The unique optimum assigns weight \(\Lambda/(2m)\) to every edge for \(t<\tau\), and weight \(B/m^2\) to every cross edge with zero internal weights for \(t>\tau\). At \(t=\tau\), the entire optimal set is the one-dimensional segment of class-uniform conductances parameterized below. Thus **unequal** community sizes are exactly what permits an intermediate one-community reinforcement phase and, at high prices, asymmetric optimal designs.

At the transition \(t=\tau_1\) for \(p>q\), all optimizers form the class-uniform segment described in the proof with \(1/N\le x\le1/p\). At \(t=\tau_2\), the same construction with \(1/p\le x\le1/q\) supplies a segment of optima; it does **not** claim to enumerate every nonsymmetric optimum on that boundary.

## Assumptions and scope

The weighted graph Laplacian uses \(L_{ij}=-w_{ij}\) for \(i\ne j\) and \(L_{ii}=\sum_{j\ne i}w_{ij}\). Its eigenvalues are arranged \(0=\lambda_1\le\lambda_2\le\cdots\le\lambda_N\). Zero edge conductances are allowed. The budget is \(\sum_{i\in A,j\in C}w_{ij}+t\sum_{\{i,j\}\subset A}w_{ij}+t\sum_{\{i,j\}\subset C}w_{ij}\le B\). All admissible conductances are variables, without any a priori groupwise equality assumption. The objective is the **continuous-time diffusion/consensus rate** \(\lambda_2\), not the discrete-time second-largest eigenvalue modulus and not total effective resistance. No constraints on individual degrees are imposed.

## Proof

Let \(S_0,S_A,S_C\) denote the sums of the cross, first-group internal, and second-group internal conductances. Orthogonally decompose the mean-zero vertex space into the unit intergroup-contrast direction, the \((p-1)\)-dimensional mean-zero subspace supported in \(A\), and the \((q-1)\)-dimensional mean-zero subspace supported in \(C\). The Rayleigh quotient of the group-contrast vector, and the average Rayleigh quotients of the two internal subspaces, give **simultaneous bounds for every independent-edge design**:
\[
\lambda_2(L)\le\frac{N}{pq}S_0,\qquad
\lambda_2(L)\le\frac{S_0}{p}+\frac{2S_A}{p-1},\qquad
\lambda_2(L)\le\frac{S_0}{q}+\frac{2S_C}{q-1}.
\tag{1}
\]
The first follows by taking vertex values \(1/p\) and \(-1/q\), whose squared norm is \(N/(pq)\); each cross-edge difference is \(N/(pq)\). For the second, write \(P_A=I_A-\mathbf1_A\mathbf1_A^\mathsf T/p\). Then \(\operatorname{tr}(P_A L)=(p-1)S_0/p+2S_A\), and each Rayleigh quotient on \(\operatorname{ran}P_A\) is at least \(\lambda_2(L)\). The third is analogous.

Conversely, assign uniform conductances \(a=S_0/(pq)\) on cross edges, \(b=2S_A/[p(p-1)]\) within \(A\), and \(c=2S_C/[q(q-1)]\) within \(C\). The Laplacian has exactly the nonzero spectral branches
\[
Na\quad(r=1),\qquad qa+pb\quad(r=p-1),\qquad pa+qc\quad(r=q-1),
\]
so \((1)\) is **attained simultaneously** for all nonnegative triples of totals. Therefore the unrestricted optimization reduces *exactly* to a three-total linear program; this is an optimality certificate, not a symmetry assumption.

For a desired spectral gap \(z>0\), write \(a=zx\). From the three tightest constraints, the minimum-price choices for given \(x\) are
\[
x\ge\frac1N,\quad b=\frac z p(1-qx)_+,\quad c=\frac z q(1-px)_+,
\]
where \((u)_+=\max\{u,0\}\). The minimum budget needed for gap \(z\) is \(z\min_x F_t(x)\), where
\[
F_t(x)=pq x+\frac t2\big[(p-1)(1-qx)_++(q-1)(1-px)_+\big],
\quad \frac1N\le x\le\frac1q.
\tag{2}
\]
Larger \(x\) cannot improve the cost. If \(p>q\), the slopes of \(F_t\) on \([1/N,1/p]\) and \([1/p,1/q]\), respectively, are
\[
pq-\frac t2(2pq-p-q),\qquad pq-\frac{tq(p-1)}2.
\]
Their signs change at exactly \(\tau_1\) and \(\tau_2\). Hence the minimizing \(x\) is \(1/N\), \(1/p\), or \(1/q\) in the three strict regimes, with the stated flat intervals at equality. Substitution into \(B=zF_t(x)\) proves every displayed value and conductance formula. When \(p=q=m\), the two interior breakpoints merge, and the only slope is \(m^2-tm(m-1)\), giving \(\tau=m/(m-1)\).

To prove uniqueness in the low and intermediate open-price regimes, observe that the aggregate optimum is unique there. Both internal-subspace bounds in \((1)\) are then equalities. Since \(L-\lambda_2 I\) is positive semidefinite on mean-zero vectors, equality of the *average* Rayleigh quotient forces **every** vector supported in either community with zero community mean to be a \(\lambda_2\)-eigenvector. Its components across the partition force each cross-edge column and row to be constant, hence all cross conductances equal. Inside either community the same eigenvector condition makes the internal Laplacian scalar on its mean-zero subspace, forcing uniform internal conductances (automatic for a group of size two). This also proves uniqueness for \(p=q\) above its threshold, when the two internal bounds remain simultaneously tight. At the lower critical price for \(p>q\), both bounds remain tight throughout the optimal segment, so these are all its optima. The same applies at the balanced critical price.

For \(p>q\) and \(t>\tau_2\), the optimizing totals are uniquely \(S_0=B\), \(S_A=S_C=0\), but only the larger-community internal-subspace bound is tight. To exhibit asymmetric optimizers, assign the cross-edge weight \(u_j>0\) to every edge incident with a particular vertex \(j\) of the smaller community, independently of the vertex in the larger community, where \(\sum_{j=1}^q u_j=B/p\). The larger-community mean-zero subspace has eigenvalue \(B/p\). For the uniform choice \(u_j=B/(pq)\), the other positive eigenvalues are \(B/q\) (multiplicity \(q-1\)) and \(BN/(pq)\), both **strictly larger** than \(B/p\) because \(p>q\). Eigenvalue continuity gives a neighborhood of positive, nonuniform \((u_j)\) with all remaining eigenvalues greater than \(B/p\). These give genuinely asymmetric global optima. For instance, at \(p,q,B)=(3,2,1)\), the unequal column weights \(u_1=11/60\) and \(u_2=9/60\) give \(\lambda_2=1/3\) at every \(t>3\): the two remaining positive eigenvalues are roots of \(x^2-4(u_1+u_2)x+15u_1u_2=0\), and their smaller root exceeds \(1/3\) because \(5u_1u_2>(u_1+u_2)^2\). This proves the claimed loss of uniqueness, without asserting that this subfamily enumerates all high-price optimizers.

## Verification

Run `python verify.py` with Python 3.10+ and NumPy 1.24+. It checks the phase formulas for all integers \(2\le q\le p\le8\), rational budgets and prices on both sides of and at the thresholds, exact budget and spectral-branch identities, direct full weighted-Laplacian eigenvalues, and randomly chosen *independently weighted* feasible graphs against the three Rayleigh upper certificates. It also checks an explicit unequal-column optimum on five vertices, using the exact sufficient quadratic inequality for that example. A local replay produced **3,055 successful assertions**. The proof of the theorem is analytic; the finite checks are not presented as exhaustive or as infinite-dimensional certification.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis (2006) introduced continuous-time fastest-mixing optimization under weighted rate budgets and its semidefinite/geometric duality. Their general framework covers the optimization formulation but does not itself state the two-price, two-community classification, exact critical prices, or high-price asymmetric optimal family. Jafarizadeh (2015) supplies explicit unpriced continuous-time spectral-gap designs for several other network topologies, including complete graphs and two complete graphs sharing vertices. The present model is a **complete graph with two price classes**, rather than two cliques sharing vertices. Later work on maximizing algebraic connectivity across interconnected network layers optimizes their interlayer rates with fixed intralayer Laplacians; it does not optimize all three conductance classes against a shared price budget. The general spectral framework and symmetry principles are acknowledged; the claimed contribution is their sharp parametric specialization and unrestricted-optimum structure.

## Limitations

The topology is the complete two-block graph, not an arbitrary sparse community network. The budget is linear in conductance, the Markov process is symmetric and continuous time, and the groupwise edge prices are homogeneous within each class. For unequal groups at the upper threshold, only an explicit symmetric segment (and not a complete list of nonsymmetric optimizers) is described. Other equivalent specializations in literature not indexed by the searches remain possible. No independent scientific audit has been performed.

## References

1. J. Sun, S. Boyd, L. Xiao, P. Diaconis. *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*. SIAM Review 48 (2006), 681–699; DOI: 10.1137/S0036144504443821. First public electronic publication: 2006-11-02. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. S. Jafarizadeh. *Optimizing the Convergence Rate of the Continuous Time Quantum Consensus*. arXiv:1509.05823, initial version 2015-09-18. Full text: https://arxiv.org/pdf/1509.05823.
3. *The art of interconnections: Achieving maximum algebraic connectivity in multilayer networks*. Network Science, 2024. Full text: https://www.cambridge.org/core/journals/network-science/article/art-of-interconnections-achieving-maximum-algebraic-connectivity-in-multilayer-networks/67B428A634B2BF0741AFD0B350F8AB4E.
