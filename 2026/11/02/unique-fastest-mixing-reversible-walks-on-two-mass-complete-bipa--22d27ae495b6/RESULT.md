# Unique fastest-mixing reversible walks on two-mass complete bipartite graphs

## Finding

For every pair of integers \(p,q\geq2\), consider the complete bipartite graph \(K_{p,q}\). The smaller of its two prescribed stationary masses is \(a\in(0,1/2]\), and the other is \(b=1-a\). The stationary distribution is uniform within each part, with probabilities \(a/p\) and \(b/q\) per vertex. The labels of the parts may be exchanged so that the smaller-mass part has \(p\) vertices.

Among **all** reversible, nonnegative, row-stochastic kernels with transitions only across bipartite edges and at self-loops, there is **exactly one** minimizer of the second-largest eigenvalue modulus (SLEM). Its total stationary cross-edge flow is

\[
T_*=\begin{cases}
a,&0<a\leq 1/3,\\
\displaystyle\frac{2ab}{1+a},&1/3\leq a\leq1/2.
\end{cases}
\]

The unique optimal kernel has stationary flow \(F_{ij}=T_*/(pq)\) on each edge from the smaller-mass to the larger-mass part. Its cross-edge transition probabilities are therefore \(P_{ij}=T_*/(aq)\) from a smaller-mass vertex and \(P_{ji}=T_*/(bp)\) in the reverse direction; the unused row probability is placed on the corresponding self-loop. Its exact optimum SLEM is

\[
\mu_* =\begin{cases}
\displaystyle\frac{1-2a}{1-a},&0<a\leq1/3,\\
\displaystyle\frac{1-a}{1+a},&1/3\leq a\leq1/2.
\end{cases}
\]

In particular, the optimum and the sharp breakpoint depend only on the **total stationary mass of each side**, not the cardinalities \(p,q\). For the simple-neighbor-proposal Metropolis--Hastings chain, the exact criterion for global SLEM optimality is \(a\leq1/3\); at larger \(a\), the Metropolis--Hastings chain is strictly suboptimal.

## Assumptions and scope

The integers \(p,q\) are at least two. All stationary masses are positive, uniform separately within the two bipartition classes, and sum to one. Kernels need not respect any vertex permutation symmetry; each of the \(pq\) cross-edge transition pairs is independently selectable subject to detailed balance, nonnegativity, row-stochasticity and support. Self-loops are permitted, and transitions inside either independent set (other than self-loops) are forbidden. SLEM is the largest absolute value of the eigenvalues on the stationary-orthogonal subspace, omitting exactly one stationary eigenvalue even for a reducible feasible kernel.

Write \(\pi_i=a/p\) in the first part and \(\pi_j=b/q\) in the second. Define edge flows \(F_{ij}=\pi_iP_{ij}=\pi_jP_{ji}\). If \(T=\sum_{i,j}F_{ij}\), then the row-capacity constraints give \(0\leq T\leq a\).

## Proof

**1. Two universal lower bounds.** Let \(D=\operatorname{diag}(\pi)\) and \(K=D^{1/2}PD^{-1/2}\). Detailed balance makes \(K\) symmetric, and \(u=\sqrt\pi\) is its unit eigenvector for eigenvalue one. Write \(u_A\) and \(u_B\) for the normalized constant vectors on the two parts. The unit vector \(v=\sqrt b\,u_A-\sqrt a\,u_B\) is orthogonal to \(u\). By the reversible Dirichlet form, its Rayleigh quotient is

\[
v^{\mathsf T}Kv=1-\frac{T}{ab}.
\]

Consequently \(\mu(P)\geq\lvert1-T/(ab)\rvert\).

Let \(W_B\) be the \((q-1)\)-dimensional subspace of vectors supported on the larger-mass part and summing to zero there. It is orthogonal to \(u\). The larger-mass diagonal block of \(K\) is \(\operatorname{diag}(1-qc_j/b)\), where \(c_j=\sum_iF_{ij}\) and \(\sum_jc_j=T\). The trace of its compression to \(W_B\), divided by \(q-1\), is exactly \(1-T/b\): subtract the one-dimensional constant-vector compression from the diagonal-block trace. Hence some unit vector in \(W_B\) has Rayleigh quotient at least \(1-T/b\), yielding

\[
\mu(P)\geq\max\left\{1-\frac Tb,\ \left|1-\frac{T}{ab}\right|\right\}.
\tag{1}
\]

This holds with *no symmetry assumption* on the edge flows.

**2. Exact attainability and minimization.** For any feasible \(T\in[0,a]\), let all \(pq\) edge flows be equal to \(T/(pq)\). The corresponding symmetric-conjugate kernel has the eigenvalues

\[
1,\qquad 1-\frac Ta\ \ (p-1\text{ times}),\qquad
1-\frac Tb\ \ (q-1\text{ times}),\qquad
1-\frac{T}{ab}.
\]

Because \(a\leq b\) and \(T\leq a\), the first nontrivial within-part eigenvalue lies between zero and \(1-T/b\). Therefore the SLEM equals the right-hand side of (1), so that bound is sharp at every \(T\).

The function \(1-T/b\) decreases strictly. Once \(T\geq ab\), the function \(T/(ab)-1\) increases strictly. They intersect at \(T=2ab/(1+a)\), which is feasible exactly when \(a\geq1/3\). For smaller \(a\), the unique optimum is the endpoint \(T=a\); otherwise, the unique optimum is the intersection. Substitution gives the announced \(T_*\) and \(\mu_*\). Values at \(a=1/3\) agree exactly.

**3. Global rigidity (uniqueness without assuming symmetry).** At either optimal value \(T=T_*\), the first lower bound in (1) is an equality: \(1-T_*/b=\mu_*\). Suppose an arbitrary admissible kernel has SLEM \(\mu_*\). Every unit vector of \(W_B\) has Rayleigh quotient at most \(\mu_*\), while the mean quotient of an orthonormal basis of \(W_B\) equals \(\mu_*\). Thus every basis vector attains the top eigenvalue on \(u^\perp\). Since \(K\) is symmetric, the Rayleigh equality principle implies that *every* vector of \(W_B\) is an eigenvector with eigenvalue \(\mu_*\). The off-diagonal block of \(K\) must therefore annihilate \(W_B\). Its \(i\)-th row is proportional to \((F_{i1},\ldots,F_{iq})\), forcing each such row to be constant across \(j\).

If \(a\leq1/3\), the optimum has \(T_*=a\). Each smaller-mass row carries at most \(a/p\), so exhausting the total mass \(a\) forces every row sum to be \(a/p\). Together with rowwise constancy, \(F_{ij}=a/(pq)=T_*/(pq)\).

If \(a>1/3\), the cut-vector Rayleigh quotient also attains the negative extremal eigenvalue: \(v^{\mathsf T}Kv=-\mu_*\). The same Rayleigh equality principle makes \(v\) an eigenvector. On each smaller-mass vertex, this identity forces the total probability of leaving that vertex to be independent of its index (as \(v\), divided by \(\sqrt\pi\), takes distinct constants on the two parts). All smaller-mass row flows therefore equal \(T_*/p\). Combined with rowwise constancy across the opposite part, this again forces \(F_{ij}=T_*/(pq)\). Detailed balance and row sums uniquely determine every entry of \(P\). This proves global uniqueness.

**4. Metropolis criterion.** Under the uniform-neighbor random-walk proposal, a Metropolis--Hastings edge has stationary flow \(\min\{a,b\}/(pq)=a/(pq)\). Its total cross flow is \(T_{\mathrm{MH}}=a\). Since the optimal \(T_*\) is unique, this chain is optimal exactly when \(a\leq1/3\), and is strictly slower in SLEM for \(a>1/3\).

## Verification

The accompanying standalone `verify_bipartite.py` tests 112 exact rational characteristic-polynomial identities (with detailed balance and stochasticity), 1,800 independently perturbed asymmetric feasible flow matrices, 45 nonuniform fixed-marginal perturbations of the optimum, eight exact-rational Metropolis threshold cases, and six unconstrained-edge-flow numerical optimization cases: 1,971 test cases in total. All passed. Reproduce with `python verify_bipartite.py` after installing the packages listed in `requirements.txt`.

The proof above is analytic for all integer sizes and all real masses in the stated range; finite checking is a corroboration, not an infinity certificate. Numerical constrained optimization is supporting evidence only and is tested to a tolerance of \(10^{-4}\), because the spectral objective is nonsmooth at its minimum.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004), section 7.1 (page 685), solve the **uniform-stationary** complete-bipartite fastest-mixing problem by symmetrizing a kernel. The formulas here reduce to theirs when \(a=p/(p+q)\), but the specified two-level nonuniform stationary law and *uniqueness among all nonsymmetric feasible kernels* are not conclusions of that section. Boyd, Diaconis, Parrilo and Xiao (2009), section 5.4.2 (page 813), again give symmetric-edge block spectra for uniform stationary walks, not the global rigidity proof for nonuniform masses. Jafarizadeh (2010) studies symmetric multipartite graph patterns under uniform stationary distribution; Jafarizadeh (2020) gives general nonuniform reversible optimization for clique lifts and stars, but the inspected statements do not directly classify independent-set bipartite lifts with both parts of size at least two.

A previous exact result for reversible walks on \(K_{m,m,r}\) with two equal stationary class masses has a *partial implication*: in a range where the optimal extra interclass edge flow can vanish, its SLEM coincides with the present bipartite formula for an even-size part. That result permits a larger graph and does not claim uniqueness of all nonsymmetric optimizers on the bipartite subgraph. The new assertion here is the all-cardinality, all-mass **unique-kernel classification** and the exact necessary-and-sufficient Metropolis criterion for this fixed feasible graph.

## Limitations

The theorem assumes full bipartite connectivity, at least two vertices per part, uniform stationary probabilities *within* each part, reversibility, and allowed self-loops. It does not classify general per-vertex stationary distributions, sparse bipartite supports, nonreversible kernels, or nonasymptotic total-variation mixing time. The objective is SLEM, and uniqueness refers to kernels with labeled vertices and the stated stationary law. A broader historical statement could imply this special result; no exhaustive worldwide novelty guarantee is asserted.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, section 7.1, https://doi.org/10.1137/S0036144503423264. First published online 2004-10-29.
2. S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819, section 5.4.2, https://doi.org/10.1137/070689413; preprint https://arxiv.org/abs/0709.0955.
3. S. Jafarizadeh, *Fastest Mixing Markov Chain on Symmetric K-Partite Network* (2010), https://arxiv.org/abs/1008.2588.
4. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks 6 (2020), 88–104, https://doi.org/10.1109/TSIPN.2020.2964211; author version https://arxiv.org/abs/2501.02421.
