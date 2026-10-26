# Exact occupation large deviations and universal rare transitions for three-allele mutation spines

## Finding

Let \(q=(q_1,q_2,q_3)\) be any strictly positive probability vector. On the three-letter alphabet consider the no-repeat mutation chain with \(P_{ii}=0\) and \(P_{ij}=q_j/(1-q_i)\) when \(i\ne j\). Its empirical occupation vector \(L_n\) has an explicit large-deviation rate function, including the boundary of its feasible simplex. For every \(\nu\) in the triangle
\[
\mathcal T=\{\nu_i\ge0,\ \sum_i\nu_i=1,\ \max_i\nu_i\le1/2\},
\]
write \(t_{ij}(\nu)=(\nu_i+\nu_j-\nu_k)/2=1/2-\nu_k\) for distinct \(i,j,k\). The rate function is
\[
I_q(\nu)=\sum_{1\le i<j\le3} t_{ij}(\nu)\log\frac{t_{ij}(\nu)^2}{\nu_i\nu_jP_{ij}P_{ji}}
\]
on \(\mathcal T\), and \(+\infty\) outside it. A term with \(t_{ij}=0\) is defined as zero. All terms with nonzero \(t_{ij}\) have a positive denominator, including on the boundary.

The unique minimizer of the joint empirical-transition rate at prescribed \(\nu\) is the **symmetric**, zero-diagonal flow \(Q^*_{ij}=Q^*_{ji}=t_{ij}(\nu)\). Consequently, for any \(\nu\) in the relative interior of \(\mathcal T\), the empirical transition matrix of a lineage conditioned to have composition near \(\nu\) concentrates, in the iterated large-sample/small-neighborhood limit, on
\[
R^*_{ij}(\nu)=\frac{t_{ij}(\nu)}{\nu_i}\quad(i\ne j),\qquad R^*_{ii}=0.
\]
**The conditioned transition matrix is independent of the original mutation weights \(q\)**, although the exponential cost \(I_q(\nu)\) depends on them. The unique zero of the rate is the stationary composition \(\pi_i=q_i(1-q_i)/(1-\sum_jq_j^2)\).

## Assumptions and scope

The time-homogeneous Markov chain \((X_k)_{k\ge0}\) takes values in \(\{1,2,3\}\), starts from any fixed state, and uses the kernel just specified. Positivity of all \(q_i\) makes it irreducible and aperiodic (both two- and three-step returns occur). Define
\[
L_n(i)=\frac1n\sum_{k=0}^{n-1}{\bf1}_{\{X_k=i\}},\qquad
Q_n(i,j)=\frac1n\sum_{k=0}^{n-1}{\bf1}_{\{X_k=i,X_{k+1}=j\}}.
\]
A large-deviation principle (LDP) means that for every closed \(F\) and open \(G\) in the ambient probability simplex,
\[
\limsup_{n\to\infty}\frac1n\log\Pr(L_n\in F)\le-\inf_{\nu\in F}I_q(\nu),\quad
\liminf_{n\to\infty}\frac1n\log\Pr(L_n\in G)\ge-\inf_{\nu\in G}I_q(\nu).
\]
For interior \(\nu\), each \(\delta>0\) satisfies the conditional-concentration statement
\[
\lim_{\varepsilon\downarrow0}\limsup_{n\to\infty}\Pr\big(\lVert Q_n-Q^*(\nu)\rVert_\infty>\delta\ \big|\ \lVert L_n-\nu\rVert_\infty<\varepsilon\big)=0.
\]
The claimed behavior concerns the distinguished lineage's mutation types, not empirical composition of the *entire branching population* and not genealogical branching counts. It applies to the common-draw conditional-exclusion family of mutation matrices in Remark 2.2 and the Markov spine in Remark 6.1 of Blancas–Fittipaldi–Hernández-Torres (2026).

## Proof

**1. Stationary law and detailed balance.** Let \(Z=1-\sum_iq_i^2=\sum_iq_i(1-q_i)>0\). Then \(\pi_i=q_i(1-q_i)/Z\) sums to one and \(\pi_iP_{ij}=q_iq_j/Z=\pi_jP_{ji}\). Thus \(P\) is reversible, irreducible and aperiodic.

**2. The underlying empirical-flow LDP.** The standard finite-state Markov method of types yields a joint LDP for \((L_n,Q_n)\) with good rate
\[
J(\nu,Q)=\sum_{i\ne j}Q_{ij}\log\frac{Q_{ij}}{\nu_iP_{ij}},
\]
when \(Q_{ii}=0\), \(Q_{ij}\ge0\), and both its row sums and column sums equal \(\nu\), and \(+\infty\) otherwise. Terms \(Q_{ij}=0\) vanish. Here \(0\log(0/0)\) is zero on unused rows. This follows by decomposing paths according to integer directed-edge counts: the logarithmic number of paths with a balanced limiting flow \(Q\) is \(-n\sum_{i,j}Q_{ij}\log(Q_{ij}/\nu_i)+o(n)\). The upper bound comes from multinomial choices of destinations at each state. The lower bound uses integer approximations by connected Eulerian directed multigraphs (every strictly positive flow has these approximants), Stirling's formula, and then approximates boundary flows by positive feasible ones; the finite initial/final path imbalance changes counts by at most one and does not affect speed \(n\). Equivalently this is the discrete-time level-2.5 LDP of Monthus (2021, Section III.4, equation (48)). Contracting over \(Q\) yields \(I_q(\nu)=\min_Q J(\nu,Q)\).

**3. Sharp feasible domain.** Since all diagonal flow entries vanish and the total sum is one, any balanced feasible flow satisfies \(\nu_i=\sum_{j\ne i}Q_{ij}\le\sum_{j\ne i}\nu_j=1-\nu_i\). Hence \(\max_i\nu_i\le1/2\). Conversely, for any \(\nu\) satisfying these three inequalities, \(t_{ij}=(\nu_i+\nu_j-\nu_k)/2\ge0\) gives a nonnegative symmetric matrix with row/column sums \(\nu\), establishing feasibility and the exact triangle (including its edges and vertices).

**4. Uniqueness of the symmetric minimizing flow.** Write \(Q^\top\) for transpose. By detailed balance and both-marginal constraints,
\[
J(\nu,Q^\top)=J(\nu,Q):
\]
the difference in logarithmic reference weights reduces to \(\sum_{i,j}Q_{ij}(\log\pi_i-\log\pi_j)=0\). Because \(x\mapsto x\log x\) is strictly convex, \(J(\nu,(Q+Q^\top)/2)\le J(\nu,Q)\), strictly unless \(Q=Q^\top\) on its support. Therefore every minimizer is symmetric. On three vertices any symmetric zero-diagonal matrix with row sums \(\nu\) is uniquely determined by the three linear equations and has entries \(t_{12},t_{13},t_{23}\) above. Existence holds by compactness and lower semicontinuity; hence \(Q^*\) is the unique minimizer even on the boundary.

**5. Explicit rate and its minimum.** Substituting the unique minimizer into \(J\) and pairing the two orientations of each edge gives the displayed formula. The rate is continuous on the closed triangle: the entropy expression \(\sum_{ij}Q^*_{ij}\log Q^*_{ij}-\sum_i\nu_i\log\nu_i-\sum_{ij}Q^*_{ij}\log P_{ij}\) uses only continuous \(x\log x\) terms. The rate is nonnegative because each row contributes a weighted KL divergence. Equality forces the transition rows to agree with \(P\), so \(\nu P=\nu\), and irreducibility gives the unique \(\nu=\pi\). The explicit formula and domain constitute a good LDP on the compact simplex.

**6. Conditioned transitions.** At fixed interior composition \(\nu\), all \(t_{ij}>0\), and the feasible flow set is compact. For every \(\delta>0\), strict uniqueness supplies a positive gap between \(\min J(\nu,\cdot)\) and the minimum over \(\lVert Q-Q^*(\nu)\rVert_\infty\ge\delta\). Compactness and continuity extend this gap to a sufficiently small neighborhood of \(\nu\). Combining the joint LDP upper bound and its occupation lower bound shows the conditional probability in the statement decays exponentially in \(n\). Dividing the flow by its row marginals proves the formula for the empirical transition kernel. Its independence of \(q\) is explicit.

## Verification

At \(q_i=1/3\), the stationary composition is \(\pi=(1/3,1/3,1/3)\) and \(I_q(\pi)=0\). At the vertex \(\nu=(1/2,1/2,0)\), the only admissible limiting flow alternates between the first two states and
\[
I_q(1/2,1/2,0)=\tfrac12\log\frac1{P_{12}P_{21}};
\]
in particular this equals \(\log2\) for uniform weights, matching the elementary probability \(2^{1-n}\) of alternating on two specified types to exponential order when starting in one of them. The accompanying standalone program verifies row/column balance, detailed balance, the rate formula, its stationary zero and strict cost increase from nonzero circulations over seeded cases. These finite calculations do not constitute the infinite-horizon LDP proof.

## Relationship to prior work

Blancas, Fittipaldi and Hernández-Torres (arXiv:2610.20896v1, Remark 2.2) explicitly propose the common-draw conditional-exclusion mutation kernel, and Remark 6.1 identifies it as the type transition law along the size-biased spine. They do not derive the empirical occupation rate surface or its rare-event conditional transition law. Monthus (arXiv:2101.09045v3, Section III.4) supplies the general **uncontracted**, level-2.5 flow-entropy rate for discrete Markov chains, from which this investigation starts; it does not evaluate the entropy contraction on a three-allele exclusion triangle or identify the universal rare-event kernel. The new mathematical work is the exact feasibility triangle and the unique reversible entropy minimization that eliminates all residual flow degrees of freedom; the general Markov LDP itself is not new. The 1976 paper of Wei Shen Hsia studies occupation-time distributions for a three-state process with no diagonal transition; its abstract is a close historical precursor, but its full text was not accessible for detailed comparison.

## Limitations

The rate is a large-time exponential limit, not a finite-time probability formula or a prefactor asymptotic. The explicit three-state formula does not automatically extend to four or more types, where symmetric balanced flows are not uniquely fixed by their marginals. For a boundary composition the rate formula remains valid, but the displayed conditional-transition statement is intentionally restricted to interior compositions. The result concerns spine types under the specified mutation transition kernel, not unconditioned population type-frequency large deviations. A historical three-state occupation-time article could contain additional overlapping asymptotics; the accessible abstract does not resolve this risk.

## References

1. A. Blancas, M. C. Fittipaldi and S. Hernández-Torres, *The Q-process for the general mother-dependent multitype branching process*, arXiv:2610.20896v1 (submitted 2026-10-14), Remark 2.2 and Remark 6.1. https://arxiv.org/html/2610.20896v1
2. C. Monthus, *Inference of Markov models from trajectories via Large Deviations at Level 2.5 with applications to random walks in disordered media*, arXiv:2101.09045v3 (2021), Section III.4, equation (48). https://arxiv.org/html/2101.09045v3
3. L. Daures, *Large deviations for possibly reducible Markov chains on discrete state spaces*, arXiv:2507.11166v2 (2026), general Markov occupation LDP framework. https://arxiv.org/html/2507.11166v2
4. W. S. Hsia, *The joint probability density function of the occupation time of a three-state problem*, J. Applied Probability 13 (1976), 57–64, DOI 10.2307/3212665 (abstract consulted; full text unavailable). https://doi.org/10.2307/3212665
