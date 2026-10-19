# Dirichlet phase clocks and random quasi-ergodic measures on reducible finite-state survivors

## Finding

**Theorem (conditional critical-class clocks and occupation laws).** Let \(Q\) be a finite nonnegative substochastic matrix and \(\pi\) a probability row vector on its transient states. Restrict attention to states reachable by a positive-weight path from \(\operatorname{supp}\pi\). Assume every strongly connected diagonal block \(A_i\) in the Frobenius decomposition of this reachable submatrix is **primitive**, with Perron root \(\lambda_i>0\), and let \(\lambda=\max_i\lambda_i\in(0,1)\). In particular all reachable states are transient. Write \(B_{ij}\) for an off-diagonal block corresponding to a possible forward transition from component \(i\) to component \(j\).

Call a component *critical* if \(\lambda_i=\lambda\). Let \(\mathcal C\) be the finite set of directed component paths \(c=(i_1,\ldots,i_h)\) that can begin in a component charged by \(\pi\), have every connecting \(B_{i_j i_{j+1}}\ne0\), and end in any component. Let \(d\ge1\) be the largest number of critical components on any path in \(\mathcal C\); let \(\mathcal C_d\) consist of the paths attaining this number.

For each critical component choose Perron vectors \(r_i>0\) and \(\ell_i>0\) satisfying
\[
A_i r_i=\lambda r_i,\qquad \ell_i^{\mathsf T}A_i=\lambda\ell_i^{\mathsf T},\qquad \ell_i^{\mathsf T}r_i=1.
\]
Set \(L_i=r_i\ell_i^{\mathsf T}\) for critical components and \(L_i=(I-A_i/\lambda)^{-1}\) for subcritical components. Define the positive weight of a maximal path \(c=(i_1,\ldots,i_h)\in\mathcal C_d\) by
\[
W(c)=\lambda^{-(h-1)}\,\pi_{i_1}L_{i_1}B_{i_1i_2}L_{i_2}\cdots B_{i_{h-1}i_h}L_{i_h}\mathbf 1_{i_h},
\qquad W=\sum_{c\in\mathcal C_d}W(c).
\]
Here \(\pi_i\) is the restriction of \(\pi\) to component \(i\), and \(\mathbf1_i\) is its all-ones column. Then the probability of survival through time \(n\) has the sharp asymptotic
\[
\boxed{\Pr_\pi(T>n)=\pi Q^n\mathbf1\sim \frac{W}{(d-1)!}\,n^{d-1}\lambda^n.}
\]
The notation \(T>n\) means that the transient-state path \(X_0,\ldots,X_n\) has survived all \(n\) transitions; the absorbing state is excluded.

Conditioned on \(T>n\), the component path converges in probability to the finite collection \(\mathcal C_d\), with
\[
\boxed{\Pr(\text{component path}=c\mid T>n)\longrightarrow W(c)/W.}
\]
Conditional on any fixed \(c\in\mathcal C_d\), enumerate its critical components in visitation order as \(\kappa_1,\ldots,\kappa_d\). If \(M_{j,n}\) is the number of time indices \(t\in\{0,\ldots,n\}\) spent in critical component \(\kappa_j\), then
\[
\boxed{(M_{1,n}/(n+1),\ldots,M_{d,n}/(n+1))\ \Longrightarrow\ (D_1,\ldots,D_d),\quad D\sim\operatorname{Dirichlet}(1,\ldots,1).}
\]
The total number of visits to subcritical components remains tight conditional on \(c\), and hence vanishes after division by \(n\). In particular, the first-entrance times into critical components \(\kappa_2,\ldots,\kappa_d\), divided by \(n\), converge jointly to the ordered values of \(d-1\) independent uniform random variables on \([0,1]\).

Let \(\eta_n=(n+1)^{-1}\sum_{t=0}^n\delta_{X_t}\). On each critical component define the probability \(\nu_i\) by \(\nu_i(s)=\ell_i(s)r_i(s)\) for \(s\) in that component and zero elsewhere. Conditionally on \(T>n\),
\[
\boxed{\eta_n\ \Longrightarrow\ \sum_{j=1}^d D_j\nu_{\kappa_j}\,,}
\]
where the component path \(c\) is first drawn with probabilities \(W(c)/W\), and independently \(D\sim\operatorname{Dirichlet}(1,\ldots,1)\). For every \(d\ge2\), conditional on \(c\), the limiting fraction in each critical component has positive variance \((d-1)/(d^2(d+1))\); consequently the conditional empirical measure does **not** converge in probability to its deterministic conditional mean.

## Assumptions and scope

The state set is finite. The substochastic matrix \(Q\) specifies transitions between transient states, with missing row mass sent to one absorbing state. The component graph is acyclic by strong-component decomposition, but the dynamics within each component may be nontrivial and need not be reversible. Every reachable diagonal block is primitive; no assumption is made that the roots of the different blocks coincide. A *reachable* component is one reachable from a positive-mass initial state. The maximal Perron root \(\lambda\) is taken on the reachable subsystem; the theorem assumes \(0<\lambda<1\), so the survival probability tends to zero. The theorem includes \(d=1\), in which the Dirichlet law means the point mass at \((1)\). No claim is made for periodic (imprimitive) blocks, countable states, or a non-absorbing critical root \(\lambda=1\).

The empirical measure is on the finite state set. Its blockwise probabilities \(\nu_i\) are the invariant distributions of the Perron-Doob transforms \(P_i(s,t)=A_i(s,t)r_i(t)/(\lambda r_i(s))\), not stationary distributions of the killed transition matrix itself. In symbolic-dynamics language, the \(\nu_i\) extend to invariant Markov measures on each critical shift component.

## Proof

**1. Exact component-path expansion.** Put \(K_i(m)=\lambda^{-m}A_i^m\) for \(m\ge0\). A trajectory with component path \(c=(i_1,\ldots,i_h)\) has precisely one intercomponent edge for each of the \(h-1\) successive moves. If \(m_j\) is the number of intracomponent transitions in component \(i_j\), then \(m_1+\cdots+m_h=n-h+1\), with each \(m_j\ge0\). Its total probability, summed over internal states, is exactly
\[
\lambda^{n-h+1}\pi_{i_1}K_{i_1}(m_1)B_{i_1i_2}K_{i_2}(m_2)\cdots B_{i_{h-1}i_h}K_{i_h}(m_h)\mathbf1_{i_h}.
\]
Every surviving trajectory has a unique such decomposition, so summing these expressions over the finitely many component paths and all nonnegative compositions is exact.

**2. Spectral splitting and finite excursions.** Primitivity supplies constants \(C>0\) and \(0<\vartheta<1\) (which may be chosen uniformly across the finitely many components) such that for every critical \(i\),
\[
K_i(m)=L_i+E_i(m),\qquad\|E_i(m)\|\le C\vartheta^m,
\]
and for every subcritical \(i\), \(\|K_i(m)\|\le C\vartheta^m\). Therefore all normalized subcritical excursions are summable and
\[
\sum_{m\ge0}K_i(m)=(I-A_i/\lambda)^{-1}=L_i.
\]
For a path having exactly \(q\ge1\) critical components, first fix all subcritical residence counts with total \(s\). The critical residence counts are then a weak composition of \(n-h+1-s\) into \(q\) parts, in number \(\binom{n-h+q-s}{q-1}\). Replacing each critical \(K_i(m)\) by \(L_i\) introduces, after summing over the compositions, an error of order \(O(n^{q-2})\) for \(q\ge2\), since
\[
\sum_{m_1+\cdots+m_q=N}\sum_{j=1}^q\vartheta^{m_j}=O((N+1)^{q-2}).
\]
For \(q=1\) the corresponding error is exponentially small for bounded subcritical residence counts. Because the subcritical residence counts have geometric tails, their total contribution may be summed termwise, and the leading term of the path is
\[
\lambda^n\frac{n^{q-1}}{(q-1)!}\,\lambda^{-(h-1)}\pi_{i_1}L_{i_1}B\cdots BL_{i_h}\mathbf1_{i_h} \,(1+o(1)).
\]
The same estimates give the appropriate upper bound for a path with no critical component, which is exponentially smaller than \(\lambda^n\). Thus the paths with exactly \(d\) critical components dominate and yield the stated survival asymptotic and path-selection weights.

**3. Joint phase-time limit.** Fix a dominating component path \(c\). The preceding estimates are uniform whenever the critical residence counts are all at least \(L\), up to errors \(O(\vartheta^L)\). The total normalized mass of compositions having a critical residence below \(L\) is \(O(L/n)\). Similarly, the normalized tail probability that a subcritical component has residence exceeding \(L\) is \(O(\vartheta^L)\), after a harmless adjustment of constants. Hence the conditional law of the critical residence vector is asymptotically that of a uniformly selected weak composition of \(n+O_{\Pr}(1)\) into \(d\) nonnegative parts. Riemann summation on the standard simplex gives the Dirichlet law with all parameters one. Normalized critical first-entry times are the cumulative sums of the preceding residence fractions, equivalent to ordered uniform spacings. All subcritical holding times are tight.

**4. Internal occupation law.** Fix a critical component \(i\), and define its Perron-Doob transition matrix by \(P_i(s,t)=A_i(s,t)r_i(t)/(\lambda r_i(s))\). Its invariant probability is \(\nu_i(s)=\ell_i(s)r_i(s)\). For any bounded state observable \(f\), the Perron root \(\lambda_i(u)\) of \(\operatorname{diag}(e^{uf})A_i\) is analytic for \(u\) near zero, and differentiating its eigenvalue equation gives
\[
\left.\frac{d}{du}\log\lambda_i(u)\right|_{u=0}=\sum_s\nu_i(s)f(s).
\]
The spectral gap uniformly controls the moment-generating function for a long segment with arbitrary fixed nonnegative entrance and exit weights compatible with that component. Differentiation at zero yields an expected sum of \(m\nu_i(f)+O(1)\) and variance \(O(m)\). A variance bound and Chebyshev's inequality give convergence in probability of the within-component empirical distribution to \(\nu_i\) as residence \(m\to\infty\). Because all critical fractions are strictly positive under the Dirichlet limit, each critical residence diverges in probability, while subcritical visits are tight. Combining the within-component convergence with Step 3 proves the stated random empirical-measure limit.

**5. Nonconcentration.** For the Dirichlet law with parameters all one, each coordinate has mean \(1/d\) and variance \((d-1)/(d^2(d+1))\). The critical components have disjoint state supports. For \(d\ge2\), a function identifying one of these components therefore has a limiting time average with strictly positive conditional variance. This is incompatible with convergence in probability to the deterministic quasi-ergodic expectation.

## Verification

A standalone standard-library rational-arithmetic script, `verify.py`, checks an explicit branching example without assuming the theorem. Take \(\lambda=1/4\), \(\gamma=1/8\), and the five-state substochastic matrix with diagonal \((\lambda,\lambda,\gamma,\lambda,\lambda)\) and nonzero off-diagonal entries
\[
Q_{12}=Q_{13}=Q_{25}=Q_{34}=Q_{45}=1/8.
\]
Start deterministically at state \(1\). There are two maximal critical paths, \(1\to2\to5\) and \(1\to3\to4\to5\); the second passes through subcritical state \(3\). With \(W_A=\lambda^{-2}Q_{12}Q_{25}\) and \(W_B=\lambda^{-3}Q_{13}(1-\gamma/\lambda)^{-1}Q_{34}Q_{45}\), both weights equal \(1/4\). Thus the route mixture is exactly \((1/2,1/2)\) in the limit, and
\[
\Pr(T>n)\sim\frac14n^2(1/4)^n.
\]
The conditional empirical-measure law chooses with equal probabilities between the random mixtures \(D_1\delta_1+D_2\delta_2+D_3\delta_5\) and \(D_1\delta_1+D_2\delta_4+D_3\delta_5\), with \(D\sim\operatorname{Dirichlet}(1,1,1)\). The mean is \((1/3,1/6,0,1/6,1/3)\), but the limiting conditional variance of the state-\(1\) occupation fraction is \(1/18\), not zero. The subcritical-state holding time along the detour converges to a geometric distribution on \(\{0,1,2,\ldots\}\) with masses \(2^{-(s+1)}\).

The verifier independently enumerates all surviving state paths at twelve finite horizons, checks their total weight against exact matrix powers, evaluates both maximal-route contributions, and proves the exact uniform-composition moment identities by rational enumeration. It also checks twelve powers of a genuinely two-state primitive Perron block against its spectral projector. Executing `python3 verify.py` gave:

`VERIFY_OK: 12 exact survival matrix/path comparisons; 24 maximal-route identities; 478 exact composition-moment checks; 12 non-scalar Perron-projector checks; two resolved route weights; 16 nonscalar subcritical resolvent/path comparisons`

A separate six-state family tests a *genuinely two-state subcritical communicating class*, rather than merely a scalar detour. Four singleton critical blocks have diagonal transition probability \(1/4\). The two-state subcritical block is
\[
A_{\mathrm{sub}}=\frac1{32}\begin{pmatrix}3&1\\1&3\end{pmatrix},\qquad
(I-4A_{\mathrm{sub}})^{-1}=\begin{pmatrix}5/3&1/3\\1/3&5/3\end{pmatrix}.
\]
For the graph with edges \(1\to2\), \(1\to3\), \(2\to6\), \(4\to5\), and \(5\to6\), each of weight \(1/8\), and the extra internal bidirectional subcritical edges defined by \(A_{\mathrm{sub}}\), the two maximal routes have respective weights \(1/4\) and \(1/24\). The verifier independently checks eight survivor horizons against exact matrix powers and exact nonscalar-resolvent path sums.

These finite checks do not substitute for the spectral and Riemann-sum arguments proving the universal limit.

## Relationship to prior work

Van Doorn and Pollett, *Quasi-Stationary Distributions for Reducible Absorbing Markov Chains in Discrete Time* (2009), determine quasi-stationary distributions and **one-time terminal conditional laws** in reducible finite-state chains. They do not give the random conditional occupation or joint multitransition law stated above.

Colonius and Rasmussen, *Quasi-ergodic limits for finite absorbing Markov chains* (arXiv:2005.12738v1, 2020), analyze maximal communicating-class paths and calculate conditional **expectations of empirical time averages**, including polynomial survival factors. Their Theorem 3.14, Corollary 3.17, and Theorem 3.20 establish deterministic mean limits; their Proposition 3.7 supplies a related weighted-composition asymptotic. Those tools are directly relevant and credited here. An expectation limit alone does not determine a Dirichlet law, positive limiting occupation variance, or joint transition times. The result here proves the full distributional statement and additionally allows **arbitrary primitive nonscalar subcritical blocks** via matrix resolvents, beyond the scalar subcritical-block hypothesis in their Assumption 3.13.

Champagnat and Villemonais, *Quasi-stationary distributions in reducible state spaces* (arXiv:2201.10151, 2022), derive semigroup powers and polynomial convergence parameters for reducible processes, including matrix-valued components, but their Theorem 4.1 and surrounding estimates concern terminal conditional distributions and quasi-stationary limits rather than the joint empirical-measure distribution or Dirichlet transition clocks.

Dietz and Sethuraman, *Occupation Laws for Some Time-Nonhomogeneous Markov Chains* (2007), give Dirichlet laws in a different, time-inhomogeneous nonabsorbing setting. The present finite **time-homogeneous**, absorbing, conditioned process has a different mechanism. The uniform-simplex asymptotic is a natural extension of classical finite-state Perron and weak-composition methods, not an assertion that these analytic ingredients themselves are new.

## Limitations

The theorem assumes finite state space and primitive strongly connected diagonal blocks. Periodic blocks can introduce subsequential and lattice effects and are not addressed. The power \(n^{d-1}\) and the uniform-simplex law need not hold when the maximal Perron root has other algebraic degeneracies outside these hypotheses. The finding does not provide a central limit theorem within critical components or a universal convergence rate. Prior work's weighted-composition arguments are close; an unnoticed treatment of their full distributional consequences would affect historical priority. No independent scholarly audit or historical-priority certification has been performed.

## References

1. E. A. van Doorn and P. K. Pollett, *Quasi-Stationary Distributions for Reducible Absorbing Markov Chains in Discrete Time*, Markov Processes and Related Fields **15** (2009), 191–204. https://www.researchgate.net/publication/43511271_Quasi-Stationary_Distributions_for_Reducible_Absorbing_Markov_Chains_in_Discrete_Time . Public journal date recorded as 2009-08-03 at https://portal.mardi4nfdi.de/wiki/Quasi-stationary_distributions_for_reducible_absorbing_Markov_chains_in_discrete_time . An earlier report is identified as November 2008 without an independently verified exact public day.
2. F. Colonius and M. Rasmussen, *Quasi-ergodic limits for finite absorbing Markov chains*, arXiv:2005.12738v1 (2020-05-26), especially Proposition 3.7 and Theorems 3.14 and 3.20. https://arxiv.org/html/2005.12738v1 .
3. N. Champagnat and D. Villemonais, *Quasi-stationary distributions in reducible state spaces*, arXiv:2201.10151v1 (2022-01-25), especially Sections 1 and 4 and Theorem 4.1. https://arxiv.org/abs/2201.10151 .
4. Z. Dietz and S. Sethuraman, *Occupation Laws for Some Time-Nonhomogeneous Markov Chains*, Electronic Journal of Probability **12** (2007), 661–683. https://doi.org/10.1214/EJP.v12-413 .
