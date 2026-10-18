# Geometric strong-reset boundary layer and universal throughput in open exclusion

## Finding

Consider the finite open totally asymmetric simple exclusion process with **local** resetting to its injection site. At fixed system length, its strong-reset stationary law has an exact first-order expansion. The expansion shows a geometric accumulation of rare two-particle states, a length-independent leading throughput for every length at least three, a two-site exception, and an order-one conditional boundary correlation hidden from mean-field factorization.

Write the injection rate as \(\alpha>0\), the extraction rate as \(\beta>0\), and the reset rate as \(r>0\). The ordinary rightward hopping rate is one. Let \(\pi_r\) be the stationary law of a length-\(L\) chain, \(L\ge2\). Let \(A=(1,0,\ldots,0)\), \(B=(0,1,0,\ldots,0)\), and \(S_j\) be the state occupied precisely at sites \(1\) and \(j\), for \(2\le j\le L\). Define \(c_L=\alpha/\beta\) and, for \(2\le j<L\),

\[
c_j=\frac{\alpha(\beta+1/2)}{\beta}
\left(\frac32\right)^{L-1-j}.
\]

**Theorem.** For each fixed \(L\ge3\) and fixed positive rates, as \(r\to\infty\),

\[
\pi_r(B)=\frac1r+O(r^{-2}),\qquad
\pi_r(S_j)=\frac{c_j}{r}+O(r^{-2})\quad(2\le j\le L).
\]

Every state other than \(A,B,S_2,\ldots,S_L\) has probability \(O(r^{-2})\), and

\[
\pi_r(A)=1-\frac{1+\sum_{j=2}^{L}c_j}{r}+O(r^{-2}).
\]

For \(L=2\), the exceptional first-order law is

\[
\pi_r(0,0)=\frac{\beta}{\alpha r}+O(r^{-2}),\quad
\pi_r(B)=\frac1r+O(r^{-2}),\quad
\pi_r(S_2)=\frac{\alpha}{\beta r}+O(r^{-2}),
\]

with the remaining probability at \(A\). Let \(J_r=\beta\,\mathbb E_{\pi_r}[\eta_L]\) denote the stationary extraction throughput. Then

\[
J_r=
\begin{cases}
(\alpha+\beta)/r+O(r^{-2}),&L=2,\\
\alpha/r+O(r^{-2}),&L\ge3.
\end{cases}
\]

In particular, for every \(L\ge2\), the **exact** leading nearest-neighbour occupancy covariance is

\[
\operatorname{Cov}_{\pi_r}(\eta_1,\eta_2)=-\frac1r+O(r^{-2}).
\]

For \(L\ge3\), \(\Pr_{\pi_r}(\eta_2=1\mid\eta_1=0)\to1\), although \(\Pr_{\pi_r}(\eta_2=1)\to0\). For \(L=2\), the corresponding conditional probability tends to \(\alpha/(\alpha+\beta)\). The rare two-particle weights obey \(c_j/c_{j+1}=3/2\) for \(2\le j\le L-2\) and \(c_{L-1}/c_L=\beta+1/2\). Thus the fixed-length first-order expansion is not uniform over growing \(L\): the coefficient \(c_2\) grows geometrically in \(L\).

## Assumptions and scope

States are occupancy vectors \(\eta\in\{0,1\}^{L}\). An occupied site \(j<L\) transfers to vacant site \(j+1\) at rate one; injection fills site \(1\) at rate \(\alpha\) if empty; an occupied site \(L\) is emptied at rate \(\beta\). Independently, each occupied site \(j>1\) attempts relocation to site \(1\) at rate \(r\), but this transfer occurs only if site \(1\) is empty. A reset conserves particle number and only one particle moves at a time. These are continuous-time Markov dynamics. Positivity of \(\alpha,\beta,r\) makes the finite chain irreducible, so \(\pi_r\) exists uniquely.

All big-O constants can depend on the fixed length and the fixed positive rates. No uniform-in-length or simultaneous large-length/large-reset conclusion is asserted. The source model and rates match the open-boundary local-resetting dynamics of Pelizzola and Pretti [1].

## Proof

**1. Fast transitions and reduced chain.** Write the row generator as \(Q_r=rR+S\). Partition states into \(C=\{\eta:\eta_1=1\}\cup\{0\}\) and \(F=\{\eta:\eta_1=0,\sum_{j\ge2}\eta_j\ge1\}\). Fast resetting is absent in \(C\). In \(F\), if \(k\) sites are occupied, the \(R\)-chain jumps at rate \(k\) directly into \(C\), with each occupied site equally likely to be returned to site \(1\). Hence \(R_{FF}=-D\), where \(D\) is diagonal with the strictly positive occupation numbers \(k\).

Writing stationary row masses as \((x_r,y_r)\) on \((C,F)\), the \(F\)-balance gives

\[
y_r=x_rS_{CF}(rD-S_{FF})^{-1}.
\]

The inverse admits a convergent series in \(1/r\) for sufficiently large \(r\). Eliminating \(y_r\) gives an effective chain on \(C\) whose leading generator is

\[
\bar Q=S_{CC}+S_{CF}D^{-1}R_{FC}.
\]

The second term means: after a slow transition from \(C\) into \(F\), immediately apply one uniformly selected available reset. An empty state enters \(A\) by injection. In a state in \(C\) with additional particles, the reduced transitions never increase the number of particles away from site \(1\); rightward hops and eventual extraction provide a path of positive rates to decrease that number. Repeating gives access to \(A\). Therefore \(A\) is the sole closed class of \(\bar Q\), and \(x_r\to\delta_A\). The block equation also implies \(y_r=O(r^{-1})\). Because the finite effective generator is analytic in \(1/r\) and has a simple stationary eigenvalue, all stationary components admit integer-power asymptotic expansions.

**2. Fast-state coefficient.** The only slow departure from \(A\) is its unit-rate hop to \(B\). Since \(B\) contains exactly one particle, the leading term of the fast-state block formula is

\[
y_r=\frac1r\delta_B+O(r^{-2}).
\]

Thus \(\pi_r(B)=r^{-1}+O(r^{-2})\); every other state of \(F\) contributes only at order \(r^{-2}\) or smaller.

**3. Effective first-order source and one-extra-particle dynamics.** On visiting \(B\), a slow event occurring before its fast return to \(A\) has probability of order \(r^{-1}\). Injection at rate \(\alpha\) creates \(S_2\). When \(L\ge3\), the other possible slow event, hopping from site \(2\) to site \(3\), still leaves a one-particle state in \(F\) that rapidly resets to \(A\): it does not create a new long-lived state. The reduced first-order source is therefore a transfer \(A\to S_2\) at coefficient \(\alpha\). At \(L=2\), extraction from \(B\) at rate \(\beta\) additionally gives a first-order transfer \(A\to0\).

For \(L\ge3\), restricting the leading reduced dynamics to \(S_j\) states gives the following transitions. At \(j=2\), the additional particle hops forward at unit rate. At \(j\ge3\), that particle also hops forward at unit rate if \(j<L\), and the particle at site \(1\) can hop into site \(2\) at rate one. The resulting two particles in \(F\) reset with equal probability: resetting the site-2 particle restores \(S_j\), while resetting the other particle yields \(S_2\). Hence there is an **effective transfer \(S_j\to S_2\) at rate \(1/2\)**. At \(j=L\), extraction at rate \(\beta\) returns the system to \(A\). Configurations with two or more additional particles receive no first-order source, and their reduced dynamics only decreases their additional-particle count; their first-order masses are zero.

Let \(c_j\) denote the first-order stationary mass of \(S_j\). Conservation of the added-particle flux in this reduced chain gives

\[
\beta c_L=\alpha.
\]

The remaining stationarity equations are

\[
c_{j-1}=\frac32c_j\quad(3\le j<L),\qquad
c_{L-1}=(\beta+1/2)c_L,
\]

and the site-2 equation is \(c_2=\alpha+\frac12\sum_{j=3}^{L}c_j\). The displayed explicit coefficients satisfy all of these equations and are uniquely determined. Normalization yields the formula for \(\pi_r(A)\).

When \(L=2\), the reduced first-order flux \(A\to0\) has coefficient \(\beta\), the empty state leaves for \(A\) at rate \(\alpha\), and \(S_2\) leaves for \(A\) at rate \(\beta\). The first-order coefficients are \(\beta/\alpha\) at the empty state and \(\alpha/\beta\) at \(S_2\), establishing the exception.

**4. Throughput, covariance, and conditioned occupancy.** For \(L\ge3\), only \(S_L\) contributes at first order to occupation at the last site, so \(J_r=\beta c_L/r+O(r^{-2})=\alpha/r+O(r^{-2})\). At \(L=2\), both \(B\) and \(S_2\) occupy the exit site, giving \((\alpha+\beta)/r+O(r^{-2})\). All lengths satisfy \(\Pr(\eta_1=0,\eta_2=1)=r^{-1}+O(r^{-2})\), while \(\Pr(\eta_1=0)=O(r^{-1})\) and \(\Pr(\eta_2=1)=O(r^{-1})\). The identity

\[
\operatorname{Cov}(\eta_1,\eta_2)
=-\Pr(\eta_1=0,\eta_2=1)
+\Pr(\eta_1=0)\Pr(\eta_2=1)
\]

gives the universal covariance. For \(L\ge3\), only \(B\) accounts for the first-order vacancy of site \(1\), yielding the stated conditional limit; for \(L=2\), the first-order empty state supplies an additional vacancy mass \(\beta/\alpha\). This completes the proof.

## Verification

The supplied `check.py` builds the exact continuous-time generator from the elementary jump rules, solves the finite stationary equations over rational numbers, and independently compares every first-order configuration coefficient and the current and covariance limits for lengths \(2\) through \(5\) at several positive rational boundary rates and reset rates. It also checks the all-length reduced flux recurrences for lengths \(3\) through \(30\). Running `python check.py` passed 1,734 exact rational assertions. These finite calculations corroborate, but are not substitutes for, the proof for all fixed \(L\).

## Relationship to prior work

Pelizzola and Pretti [1] define precisely the local-reset open TASEP and study density phases using mean-field closure and Monte Carlo simulations. They discuss strong resetting chiefly when length becomes large and the product of resetting rate and length diverges. The present theorem instead takes reset rate to infinity **at fixed arbitrary finite length** and determines the entire first nonzero stationary measure, not just a mean-field density profile. In particular, the exact negative site-1/site-2 covariance is of order \(1/r\), the same as the site's rare marginal occupancy, so independent-site factorization is asymptotically invalid near the resetting boundary.

The interacting-resetting review [2] covers periodic local-reset exclusion and open systems with global resets, which are not equivalent to this fixed-length open local-reset problem. Bhatia and Gupta [3] discuss a related resource-constrained open-reset TASEP with mean-field and simulation techniques, rather than an unrestricted-reservoir finite-state theorem. Standard finite Markov-chain perturbation theory supplies the mathematical method, not these model-dependent numerical coefficients.

## Limitations

The expansion is pointwise in each fixed length; its geometric coefficient grows with length, making a uniform simultaneous length/reset limit unsupported. The theorem does not prove the large-length hydrodynamic phase diagram, all-order corrections, or global monotonicity of throughput in resetting rate. The known generator and general perturbation machinery may allow an equivalent result to be implicit in an unlocated prior analysis; independent priority assessment is still needed.

## References

[1] A. Pelizzola and M. Pretti, *Totally asymmetric simple exclusion process with local resetting and open boundary conditions*, Journal of Physics A: Mathematical and Theoretical **55** (2022), 454001. DOI: https://doi.org/10.1088/1751-8121/ac9d72 ; manuscript and model: https://arxiv.org/abs/2402.13698 ; public university manuscript: https://iris.polito.it/retrieve/handle/11583/2973072/0aca9b1c-1ce8-4ec1-b321-a4706a476ab9/Testo_rev.pdf .

[2] A. Nagar and S. Gupta, *Stochastic resetting in interacting particle systems: A review*, Journal of Physics A: Mathematical and Theoretical **56** (2023), 283001. https://arxiv.org/abs/2305.16955 .

[3] N. Bhatia and A. K. Gupta, *Totally asymmetric simple exclusion process with local resetting in a resource-constrained environment*, Physical Review E **109** (2024), 024109. https://doi.org/10.1103/PhysRevE.109.024109 .
