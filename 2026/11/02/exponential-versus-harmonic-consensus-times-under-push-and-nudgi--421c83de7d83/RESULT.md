# Exponential-versus-harmonic consensus times under push and nudging

## Finding

For the two external-influence opinion-update strategies of Van Santen, Ryckebusch and Rocha [1], complete-graph consensus time displays a sharp difference in population-size scaling. Fix \(0<\alpha\le1\), \(0<E<1\), and set \(h=\alpha E>0\), \(c=1-\alpha\). For every integer \(N\ge2\) and every initial configuration with \(i\in\{0,\ldots,N-1\}\) supporters of the externally favoured opinion \(A\), write \(T_N^{\mathrm{push}}(i)\) and \(T_N^{\mathrm{nudge}}(i)\) for the expected number of individual update attempts before all agents hold \(A\).

**Theorem.** Both rules reach unanimous \(A\) almost surely. The nudging rule satisfies the finite, uniform bounds
\[
N H_{N-i}\ \le\ T_N^{\mathrm{nudge}}(i)\ \le\ \frac{N}{\alpha E}H_{N-i},
\qquad H_b=\sum_{r=1}^b\frac1r.
\]
For the push rule, set
\[
\mathcal I_{\alpha,E}
=\int_E^1\log\!\left(\frac{x}{(1-\alpha)x+\alpha E}\right)\,dx>0.
\]
Then the following convergence holds **uniformly over every nonconsensus starting count**:
\[
\lim_{N\to\infty}\ \sup_{0\le i<N}
\left|\frac{\log T_N^{\mathrm{push}}(i)}{N}-\mathcal I_{\alpha,E}\right|=0.
\]
In particular, if the initial number of opponents is a positive fraction of \(N\), nudging takes \(\Theta(N\log N)\) individual updates in expectation, while push takes \(\exp(N\mathcal I_{\alpha,E}+o(N))\), even starting one dissenting agent short of consensus. When \(\alpha=1\), the explicit exponent is \(\mathcal I_{1,E}=\log(1/E)-1+E\).

The exact finite-\(N\) push expectation is also
\[
T_N^{\mathrm{push}}(i)
=\sum_{k=i}^{N-1}\sum_{j=0}^{k}\frac1{p_j}
\prod_{\ell=j+1}^{k}\frac{\ell}{c\ell+(N-1)h},
\qquad p_j=\frac{N-j}{N}\left(\frac{cj}{N-1}+h\right).
\]
An empty product equals one.

## Assumptions and scope

The social graph is the undirected complete graph without loops, and \(N\ge2\) is finite before the limit. Each discrete update selects one vertex uniformly. Its opinion is \(A\) or \(B\). The field favours \(A\), with strength \(E\in(0,1)\), and \(\alpha\in(0,1]\) is its trust weight. A selected \(B\)-agent flips to \(A\) with probability
\[
c\frac{\#\{A\text{-neighbours}\}}{N-1}+h.
\]
Under **push**, a selected \(A\)-agent flips to \(B\) with probability the fraction of \(B\)-neighbours. Under **nudging**, that flip probability is
\[
\max\left\{0,\ c\frac{\#\{B\text{-neighbours}\}}{N-1}-h\right\}.
\]
These are exactly the asymmetric and symmetric rules [1, equations (2) and (3)], specialized without approximation to a complete graph. No simultaneous updates, self-neighbours, added noise, or time rescaling are assumed. The parameters \(\alpha,E\) are held fixed as \(N\) grows. The limits exclude \(E=0\), \(E=1\), and \(\alpha=0\); those boundary regimes may have different absorbing classes or rates.

## Proof

**1. Count-chain reduction and absorption.** Let \(X_t\) be the number of \(A\)-agents. Permutation symmetry makes it a birth-death chain on \(\{0,\ldots,N\}\). For \(0\le j<N\), the upward probability, common to both strategies, is
\[
p_j=\frac{N-j}{N}\left(\frac{cj}{N-1}+h\right)>0.
\]
For push the downward probability is
\[
q_j^{\mathrm{push}}=\frac{j(N-j)}{N(N-1)},
\]
whereas for nudging it is
\[
q_j^{\mathrm{nudge}}=\frac jN\max\left\{0,\frac{c(N-j)}{N-1}-h\right\}.
\]
Both chains otherwise hold their current count, and \(N\) is absorbing. Every count below \(N\) has a positive-probability path of upward steps to \(N\); in this finite chain there is no other closed class. Thus absorption occurs almost surely with finite expectation.

**2. Exact push formula.** Abbreviate \(T_j=T_N^{\mathrm{push}}(j)\), \(T_N=0\), and \(\Delta_j=T_j-T_{j+1}\). The first-step expectation equation gives
\[
p_0\Delta_0=1,\qquad p_j\Delta_j-q_j^{\mathrm{push}}\Delta_{j-1}=1\quad(1\le j<N).
\]
Crucially, cancellation of the factor \((N-j)/N\) yields
\[
\frac{q_j^{\mathrm{push}}}{p_j}
=\frac{j}{cj+(N-1)h}.
\]
Solving the scalar recurrence exactly and using \(T_i=\sum_{k=i}^{N-1}\Delta_k\) proves the displayed finite double-product formula.

**3. The uniform exponential rate.** Write
\[
r_{N,j}=\frac{j}{cj+(N-1)h},\qquad
L_N=\sum_{j=1}^{N-1}\max\{0,\log r_{N,j}\}.
\]
The factors \(r_{N,j}\) increase in \(j\) and exceed one precisely when \(j>(N-1)E\). A Riemann-sum argument for the continuous function \(\log[x/(cx+h)]\) gives \(L_N/N\to\mathcal I_{\alpha,E}\). Since \(p_j\ge h/N\), the exact double sum has at most \(N^2\) terms, each bounded above by \((N/h)e^{L_N}\). Thus, uniformly in \(i<N\),
\[
T_N^{\mathrm{push}}(i)\le (N^3/h)e^{L_N}.
\]
For the lower bound choose \(k=N-1\) and \(j=\lfloor(N-1)E\rfloor\) in the double sum. This single summand is present in \(T_N^{\mathrm{push}}(i)\) for **every** \(i<N\). All its ratio factors are at least one; moreover \(p_j\le1\). Therefore
\[
T_N^{\mathrm{push}}(i)\ge
\exp\left(\sum_{\ell=\lfloor(N-1)E\rfloor+1}^{N-1}\log r_{N,\ell}\right).
\]
The exponent divided by \(N\) has the same Riemann-sum limit \(\mathcal I_{\alpha,E}\). These uniform sandwich bounds prove the claimed uniform logarithmic limit. Positivity follows from \(cx+h<x\) whenever \(x>E\) and \(\alpha>0\). Integrating \(\log(x/E)\) gives the stated \(\alpha=1\) expression.

**4. Nudging harmonic bounds.** Let \(V_t=N-X_t\) be the number of remaining \(B\)-agents. For \(V=N-j>0\), elementary substitution shows that, whenever the downward probability is positive, \(p_j-q_j^{\mathrm{nudge}}=h\); if it is zero, \(p_j\ge hV/N\). Hence in all cases
\[
p_j-q_j^{\mathrm{nudge}}\ge hV/N.
\]
For \(H_0=0\) and \(H_v=\sum_{r=1}^v1/r\), the expected one-step decrease of \(H_{V_t}\), conditional on \(V_t=V>0\), equals
\[
\frac{p_j}{V}-\frac{q_j^{\mathrm{nudge}}}{V+1}
\ge\frac{p_j-q_j^{\mathrm{nudge}}}{V}\ge\frac hN.
\]
Stopping at zero and summing this bounded nonnegative potential drift gives \(T_N^{\mathrm{nudge}}(i)\le N H_{N-i}/h\). Conversely each of the \(N-i\) agents initially holding \(B\) must be selected at least once before consensus. Independent uniform selections take expected time \(N H_{N-i}\) to cover those specified agents (the usual coupon-collection calculation), proving the lower bound.

## Verification

The standalone standard-library script `verify_media.py` reconstructs the complete-graph flip probabilities directly from individual binary configurations, checks rational first-step linear systems against the closed recurrence, and checks all claimed finite harmonic inequalities. On its recorded run it passed \(352\) exact hitting-time systems, \(2952\) direct configuration-to-count transition comparisons, \(1232\) harmonic bound comparisons, and numerical convergence checks for three parameter pairs, four population sizes, and two extreme starting counts. The numerical checks are not used as a proof of the uniform limit; the preceding Riemann-sum sandwich proves it for every admissible parameter pair.

Run with `python verify_media.py` using the Python standard library.

## Relationship to prior work

Van Santen, Ryckebusch and Rocha [1] introduce precisely these asymmetric push and symmetric nudging transition rates and study their population-level outcomes by finite-time network simulations. The present result treats the **exact complete-graph** count chain and identifies its long-time absorbing behavior and sharp quantitative size scaling, neither of which is stated in the inspected source.

Majmudar and collaborators [2] use a different jump-voter mechanism, with externally induced simultaneous random jumps, not the two state-dependent flip probabilities above. Bhat and Redner [3] study news-source voter models and derive linear or algebraic consensus-time growth in different rate regimes, not this paired rule comparison. Krapivsky and Redner [4] demonstrate exponential metastability in a two-class, three-person majority-rule system; that mechanism is a substantive precedent, but their rates do not imply the specific action integral and finite two-strategy bounds without a separate analysis. Standard one-dimensional birth-death hitting-time theory [6] motivates the recurrence approach and is not claimed to be new. Work on external fields in majority-rule or \(q\)-voter models [5] uses different update sampling.

## Limitations

The graph must be complete; the theorem does not establish an analogous universal law on sparse networks or for heterogeneous field strengths. The external field and trust parameters must be fixed away from the excluded boundary values when taking the population-size limit. The result concerns the **expected** absorption time, not a full concentration or quasi-stationary-distribution theorem. The exact formula and inequalities are self-contained; the originality comparison is limited by searchable accessible literature and may miss specialized prior analysis. No independent external audit has been performed.

## References

[1] N. Van Santen, J. Ryckebusch, L. E. C. Rocha, *Social clustering reinforces external influence on the majority opinion model* (first arXiv release 2024-04-03), arXiv:2404.02689, https://arxiv.org/abs/2404.02689; Physica A 648 (2024), 129929, doi:10.1016/j.physa.2024.129929.

[2] J. Majmudar, S. Krone, B. Baumgaertner, R. Tyson, *Voter Models and External Influence* (2015), arXiv:1511.04160, https://arxiv.org/abs/1511.04160.

[3] D. Bhat, S. Redner, *Polarization and Consensus by Opposing External Sources* (2019), arXiv:1910.01200, https://arxiv.org/abs/1910.01200.

[4] P. L. Krapivsky, S. Redner, *Divergence and Consensus in Majority Rule* (2021), arXiv:2103.04248, https://arxiv.org/abs/2103.04248.

[5] A. Muslim, *The external field effect on the opinion formation based on the majority rule and the q-voter models on the complete graph* (2023), arXiv:2305.06051, https://arxiv.org/abs/2305.06051.

[6] C. R. Doering, K. V. Sargsyan, L. M. Sander, *Extinction times for birth-death processes: exact results, continuum asymptotics, and the failure of the Fokker-Planck approximation* (2004), arXiv:q-bio/0401016, https://arxiv.org/abs/q-bio/0401016.
