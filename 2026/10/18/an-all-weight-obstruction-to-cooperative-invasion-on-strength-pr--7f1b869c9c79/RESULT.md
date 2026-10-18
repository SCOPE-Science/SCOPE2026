# An all-weight obstruction to cooperative invasion on strength-proportional weighted stars

## Finding
For every weighted star with at least three vertices, under strength-proportional source-first updating, cooperation is disfavored against its complementary defector invasion to first order in selection strength, for **every** strictly positive assignment of reciprocal contact weights and all positive benefit and cost values. More precisely, write \(N=m+1\), with \(m\ge2\) leaves, and use uniform placement of a single invading individual. Then
\[
\rho_C^U(\delta)-\rho_D^U(\delta)=-\delta\left[\frac{N-1}{N}c+\frac{2S}{N^2}b\right]+O(\delta^2),\qquad S>1.
\]
The exact coefficient \(S\) is expressed by neutral ancestral meeting times below. In particular, the benefit term has the adverse sign regardless of the hub's contact heterogeneity.

## Assumptions and scope
The star has center \(0\), leaves \(a\in\{1,\ldots,m\}\), and symmetric contacts \(W_{0a}=W_{a0}=w_a>0\), with all other contacts zero and \(\Lambda=\sum_a w_a\). Define \(d_i=\sum_jW_{ij}\) and \(P_{ij}=W_{ij}/d_i\). The binary variable \(n_i\) equals one for a cooperator. A cooperator pays \(c>0\), while every site receives the averaged benefit \(b\sum_jP_{ij}n_j\), so its payoff is
\[
f_i(n)=-c n_i+b(Pn)_i,\qquad b>0.
\]
At each oriented contact, site \(i\) replaces site \(j\) by its own trait at continuous-time rate \(W_{ij}\phi(\delta f_i(n))\). Assume \(\phi\) is twice continuously differentiable and strictly positive on a neighborhood of zero, and \(\phi(0)=\phi'(0)=1\). Rates are studied for sufficiently small \(\delta\ge0\). This convention is equivalent, for fixation probabilities, to selecting the reproducer globally with probability proportional to \(d_i\phi(\delta f_i)\) and then choosing the recipient using \(P_{ij}\). The two introduction experiments place one cooperator in defectors or one defector in cooperators at a uniformly random site, independently of selection strength. There is no mutation after introduction.

Let \(X_i\) denote the position of an ancestral random walker that jumps along edge \(ij\) at rate \(W_{ij}\). For \(i\ne j\) let \(T_{ij}\) be the expected first meeting time of two independently moving such walkers, \(T_{ii}=0\). Define \(A_a=T_{0a}\) and \(B_{ab}=T_{ab}\). Set
\[
S=\frac1\Lambda\left(2\sum_{a=1}^mw_a^2A_a+\sum_{a\ne b}w_aw_b(A_a+A_b-B_{ab})\right).
\]

## Proof
**Neutral martingale and perturbation.** At \(\delta=0\), reciprocal copying has symmetric directed rates, so \(M(n)=N^{-1}\sum_i n_i\) is a martingale and is the neutral cooperator-fixation probability. The connected finite chain absorbs almost surely; each mixed state has finite expected absorption time. Its generator derivative applied to \(M\) is
\[
\mathcal L'_0M(n)=\frac1N\sum_{i,j}W_{ij}f_i(n)(n_i-n_j).
\]
Let \(u_B\) and \(u_C\) be, respectively, the derivatives of average cooperator fixation for benefit-only payoff \(f=Pn\), and for unit cost-only payoff \(f=-n\). Standard finite-state differentiation of the harmonic equation gives \(u=\mathbb E_0\int_0^{\tau_{\mathrm{abs}}}\mathcal L'_0M(n_t)\,dt\). Linearity yields \(\partial_\delta\rho_C^U|_0=bu_B+cu_C\).

**Exact cost coefficient.** For cost alone, the drift derivative is
\[
\mathcal L'_0 M=-\frac1N\sum_{a=1}^m w_a(n_0-n_a)^2.
\]
At neutrality every disagreeing undirected edge makes two jumps of size \(1/N\) in \(M\), each at rate \(w_a\). Consequently the predictable quadratic-variation rate of \(M\) is \(2N^{-2}\sum_a w_a(n_0-n_a)^2\). Under any single-cooperator initial state, \(M_0=1/N\), and \(M_\infty\) is Bernoulli with success probability \(1/N\); hence the expected integrated quadratic variation is \((N-1)/N^2\). It follows exactly that
\[
u_C=-\frac{N-1}{2N}.
\]
This identity holds for every connected symmetric-copying graph, regardless of its weights.

**Ancestral pair expression for the benefit.** Write \(D=\operatorname{diag}(d_i)\), \(L=D-W\), and \(K=LP=W-WP\). Then \(\mathcal L'_{0,B}M=N^{-1}n^\top K n\) and every row of \(K\) sums to zero. Under uniformly selected single-cooperator initial data, the neutral voter duality gives \(\mathbb E[n_i(t)n_j(t)]=N^{-1}[1-\mathbb P(T_{ij}>t)]\) for distinct sites, and \(1/N\) for equal sites. Integrating the pair-survival probabilities therefore gives
\[
u_B=-\frac1{N^2}\sum_{i,j}K_{ij}T_{ij}.
\]
On the star, the nonzero off-diagonal entries are \(K_{0a}=K_{a0}=w_a\) and \(K_{ab}=-w_aw_b/\Lambda\) for distinct leaves. Rearrangement yields \(u_B=-S/N^2\).

**Strict positivity of the star obstruction.** Start two ancestral walkers at \((0,a)\). They cannot meet without at least one traversal of edge \((0,a)\), whose aggregate instantaneous crossing hazard for both walkers never exceeds \(2w_a\). The first crossing therefore stochastically dominates an exponential random variable with mean \((2w_a)^{-1}\). Since \(m\ge2\), the walker at the center has positive probability to jump first to a different leaf; on this event there is a positive interval during which the aggregate crossing hazard is strictly below \(2w_a\). Thus
\[
w_aA_a>\tfrac12.
\]
For distinct leaves, first-step conditioning on the two walkers gives the exact identity
\[
(w_a+w_b)B_{ab}=1+w_aA_b+w_bA_a.
\]
Therefore
\[
A_a+A_b-B_{ab}=\frac{w_aA_a+w_bA_b-1}{w_a+w_b}>0.
\]
Every off-diagonal summand in \(S\) is positive, and \(2\sum_aw_a^2A_a>\sum_aw_a=\Lambda\). Hence \(S>1\), proving \(u_B<-N^{-2}\) for all positive weighted stars.

**Paired invasion comparison.** Complementing a configuration transforms its original cooperator payoff by \(f_i(1-n)=(b-c)-f_i(n)\). At first order, the additive common constant \(b-c\) multiplies the neutral generator and leaves its harmonic fixation probability unchanged. The opposite sign on \(f_i(n)\) gives \(\partial_\delta\rho_D^U|_0=-\partial_\delta\rho_C^U|_0\) for the paired uniform-singleton experiments. Consequently
\[
\left.\frac{d}{d\delta}(\rho_C^U-\rho_D^U)\right|_{\delta=0}=-\frac{N-1}{N}c-\frac{2S}{N^2}b<-\frac{N-1}{N}c-\frac{2}{N^2}b<0.
\]
Finite-state smooth dependence and strict negativity imply \(\rho_C^U(\delta)<\rho_D^U(\delta)\) for all sufficiently small positive \(\delta\), with the permitted interval depending on the fixed weights and payoffs.

## Verification
The standalone \(\texttt{verify.py}\) reproduces the finite-state harmonic derivative and neutral two-walker meeting-time formula independently using exact rational Gaussian elimination. In particular, with weights \((1,2,4)\), it obtains \(u_B=-403/2192\), \(u_C=-3/8\), and \(S=403/137>1\); these satisfy \(u_B=-S/16\). The checks include four weighted stars with three to five vertices. Finite checks corroborate the infinite-family proof rather than replacing it.

## Relationship to prior work
Chowdhury's source-first weighted-network analysis [1] uses normalized parent-to-recipient copy rates proportional to \(F_iP_{ij}\). Its Section VI.2 identifies the strength-proportional alternative \(F_iW_{ij}\), finds negative benefit responses in finite examples, and states that a global all-positive-weight exclusion would require a further benefit-contraction proof. The present result supplies that proof for **all** weighted stars and additionally gives a graph-size-uniform strict coefficient bound. The same paper's negative weighted-star results in Appendix D concern the *normalized* copy rule and do not imply this result under the different neutral ancestry and reproductive values. Allen, Lippner, and Nowak [2] obtain classical weak-selection conditions on *isothermal* weighted graphs, whereas an at-least-two-leaf positive weighted star is never isothermal: its center has total strength \(\Lambda>w_a\) for every leaf. The neutral duality and martingale tools themselves are standard; the all-weight star sign and quantitative gap are the contribution.

## Limitations
Only the first derivative at neutral selection is characterized. This does not establish the sign at arbitrary finite selection strengths, on non-star topologies, with asymmetric weights, with accumulated instead of averaged payoff, with death-first updating, or with selection-dependent birth-associated mutant placement. Weak-selection intervals need not be uniform as positive weights degenerate. Independent historical-priority evaluation remains to be performed.

## References
[1] A. Chowdhury, *Protected domains and cooperative invasion on weighted networks*, arXiv:2609.10463, first public version September 9, 2026; revision v3 October 15, 2026. https://arxiv.org/html/2609.10463v3

[2] B. Allen, G. Lippner, and M. A. Nowak, *Evolutionary games on isothermal graphs*, Nature Communications 10, 5107 (2019), https://doi.org/10.1038/s41467-019-13006-7; arXiv:1903.10478.
