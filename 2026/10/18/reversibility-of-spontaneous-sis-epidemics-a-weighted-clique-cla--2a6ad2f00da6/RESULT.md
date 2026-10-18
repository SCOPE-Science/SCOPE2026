# Reversibility of spontaneous SIS epidemics: a weighted clique classification

## Finding

Consider a finite network of susceptible/infected sites. Site \(i\) acquires infection from outside at a positive rate \(\alpha_i\), recovers at a positive rate \(\delta_i\), and receives additional independent infection attempts from each infected site \(j\) at rate \(\beta_{j\to i}\ge0\). **The exact stationary epidemic process is time-reversible if and only if the positive transmission network is a disjoint union of complete directed components and within each component \(C\) there is a number \(\kappa_C>0\) such that**

\[
\beta_{j\to i}=\kappa_C\alpha_i\qquad (i,j\in C,\ i\ne j),
\]

with no transmissions between components. Isolated vertices are allowed, and recovery rates may vary arbitrarily. This classification permits directed, unequal transmission rates, but requires their ratios to be proportional to the *recipient's* external infection rate.

For any such network the stationary probability of the infected set \(A\subseteq V\) is

\[
\pi(A)=\frac1Z\prod_{i\in A}\frac{\alpha_i}{\delta_i}
\prod_C\prod_{h=0}^{|A\cap C|-1}(1+\kappa_C h),
\]

where empty products equal one. The normalization factor decomposes by connected component:

\[
Z=\prod_C\sum_{k=0}^{|C|}e_k\!\left(\left\{\frac{\alpha_i}{\delta_i}:i\in C\right\}\right)
\prod_{h=0}^{k-1}(1+\kappa_C h),
\]

where \(e_k\) is the elementary symmetric polynomial (with \(e_0=1\)). An isolated vertex may be assigned \(\kappa_C=0\) in these formulas. Each component normalization is computable by a quadratic-time elementary-symmetric recurrence, although there are exponentially many individual configurations.

**Uniform-network consequence.** Fix \(\alpha,\delta,\beta>0\) and an undirected simple contact graph \(G\), with external infection rate \(\alpha\), recovery rate \(\delta\), and added infection rate \(\beta\) per infected neighbor. The process is reversible exactly when \(G\) is a disjoint union of cliques. On a connected network it is reversible exactly for a complete graph. Exactly \(B_n\) of the \(2^{\binom{n}{2}}\) undirected labeled graphs on \(n\) vertices are reversible, where \(B_n\) is the Bell number.

The smallest connected nonreversible example is the three-vertex path. An elementary four-state transition cycle in that example has forward/reverse rate-product ratio

\[
\frac{(\alpha+\beta)^2}{\alpha(\alpha+2\beta)}=1+\frac{\beta^2}{\alpha(\alpha+2\beta)}>1.
\]

This obstruction occurs for *every* strictly positive \(\alpha,\beta\), not merely large transmission.

## Assumptions and scope

There are \(n\ge1\) labeled sites. A configuration is the infected subset \(A\subseteq V=\{1,\dots,n\}\). For \(i\notin A\), the jump \(A\to A\cup\{i\}\) has rate

\[
b_i(A)=\alpha_i+\sum_{j\in A}\beta_{j\to i},
\]

with \(\alpha_i>0\), \(\beta_{j\to i}\ge0\), and no self-transmission. For \(i\in A\), the jump \(A\to A\setminus\{i\}\) has rate \(\delta_i>0\), independent of other sites. All jump clocks are exponential. Since every single-site flip is possible through external infection or recovery, this finite continuous-time chain is irreducible and has a unique strictly positive stationary law. Reversible means this *exact* stationary chain satisfies detailed balance, not merely that a mean-field approximation has a stationary solution.

The stated positive components are the connected components of the undirected graph obtained from positive transmission pairs. In the reversible case the two directions on each positive pair must both be present. A component of size one carries no constraint beyond absence of external transmission edges. All conclusions quantify over all positive immigration/recovery parameters and all nonnegative directed pairwise transmission rates satisfying the stated assumptions.

## Proof

**1. Necessary square equations.** Reversibility implies that the products of rates around both orientations of every four-configuration square are equal. For distinct uninfected \(i,j\) and any infected set \(A\) disjoint from them, canceling the two recovery factors gives

\[
b_i(A)[b_j(A)+\beta_{i\to j}]
=b_j(A)[b_i(A)+\beta_{j\to i}].\tag{1}
\]

With \(A=\varnothing\), (1) becomes

\[
\alpha_i\beta_{i\to j}=\alpha_j\beta_{j\to i}.\tag{2}
\]

Because external rates are positive, one transmission direction is positive exactly when the reverse direction is positive. Define the symmetric coefficients

\[
t_{ij}:=\frac{\beta_{i\to j}}{\alpha_j}
=\frac{\beta_{j\to i}}{\alpha_i}\ge0.\tag{3}
\]

For a pair with \(t_{ij}>0\), substituting (3) in (1) and canceling positive factors gives

\[
\sum_{k\in A}t_{ki}=\sum_{k\in A}t_{kj}.\tag{4}
\]

In particular, \(A=\{k\}\) gives \(t_{ki}=t_{kj}\) for each third vertex \(k\).

**2. Necessity of weighted clique components.** Suppose \(i,j\) have a positive edge and \(k\) has a positive edge to \(i\). The singleton equation forces \(t_{kj}=t_{ki}>0\), hence \(k,j\) also have an edge. Therefore each connected component is complete. On every triangle, (4) applied successively to its three edges shows that all three coefficients coincide. Repeating across triangles shows that all \(t_{ij}\) inside any component of size at least three equal one positive constant \(\kappa_C\); for a two-vertex component its single positive coefficient already gives such a constant. Equation (3) now yields the required target-proportional transmission law. No cross-component transmission is possible by definition.

**3. Sufficiency and exact stationary measure.** Conversely, suppose the transmission network has the stated form. For uninfected \(i\in C\), write \(k=|A\cap C|\). Its infection rate is exactly \(\alpha_i(1+\kappa_C k)\). Let \(w(A)\) be the unnormalized product displayed in the finding. Then

\[
\frac{w(A\cup\{i\})}{w(A)}
=\frac{\alpha_i}{\delta_i}(1+\kappa_C k)
=\frac{q(A,A\cup\{i\})}{q(A\cup\{i\},A)}.
\]

Every allowed jump consequently satisfies detailed balance with \(\pi=w/Z\). Irreducibility establishes that this is the unique stationary distribution. Summing by the infected counts of separate components gives the stated partition function; the elementary symmetric polynomials evaluate its componentwise sums.

**4. Uniform specialization and sharp witness.** If all transmission edges have the same positive rate \(\beta\) and all immigration rates equal \(\alpha\), condition (3) reads \(t_{ij}=\beta/\alpha\) on edges. The characterization is therefore equivalent to the graph being a disjoint union of cliques, in bijection with set partitions, which gives \(B_n\). Every graph on at most two vertices is a clique union. On the path \(k-i-j\), start with just \(k\) infected. Adding \(i\) then \(j\) has infection-rate product \((\alpha+\beta)^2\), while adding \(j\) then \(i\) has product \(\alpha(\alpha+2\beta)\). The two recovery factors are identical and cancel. Their strictly unequal ratio violates reversibility and proves the sharp three-vertex cutoff. A non-clique connected graph always contains an induced three-vertex path (take the first three vertices of a shortest path between nonadjacent vertices), so this obstruction generalizes to every non-clique component.

## Verification

The standalone `verification.py` performs exact rational-arithmetic checks; execute `python verification.py` from the directory containing the script. The one-line JSON output must be byte-identical to `certificate.json`. It checks all \(1{,}099\) labeled undirected simple graphs on one through five sites, finding exactly \(75\) reversible clique unions and \(1{,}024\) nonreversible cases. It explicitly tests \(18{,}801\) four-state square comparisons, including checks stopped at the first violation. This census supports but is not needed for the unrestricted structural proof. It separately validates a six-site heterogeneous directed weighted clique construction, all \(192\) oriented state-edge detailed-balance equations, all \(240\) square equations, an unbalanced two-vertex obstruction, and the three-vertex path ratio \(25/16\) at \(\alpha=2,\beta=3\).

## Relationship to prior work

The spontaneous-infection SIS/contact process itself is classical; no priority is claimed for that stochastic model, for Kolmogorov's reversibility criterion, or for the complete-graph stationary formula. Van Mieghem and Cator (2012) analyze the model with nodal self-infection and derive its complete-graph stationary behavior. Foxall (2014) treats general heterogeneous spontaneous and contact rates, irreducibility, convergence, and approximate occupancy equations. Zhang and Moura's publicly posted 2015 preprint distinguishes the linearly additive extended contact process from their *exponentially scaled* SIS model, which has a reversible closed-form stationary distribution on any undirected graph. Their result does **not** imply that the additive-rate contact process has detailed balance on all graphs: the rates define different chains. Its full preprint text addresses approximation, not the necessary-and-sufficient weighted clique classification here.

The new statement concerns the exact topology-and-rate boundary between reversible and nonreversible **additive** epidemic mechanisms, extends beyond equal parameters to arbitrary strictly positive nodal immigration and recovery and directed transmission, and gives an exact partition function throughout the reversible class. Its classical ingredients are acknowledged; the conjunction of complete weighted classification, exact stationary weights, and sharp local cycle obstruction is the object of the contribution.

## Limitations

Reversibility is stronger than existence of stationarity. All graphs under the positive-rate assumptions have a unique stationary law even when they are *nonreversible*. The theorem does not claim an impossibility of calculating that law by other methods, nor quantify its entropy production. The conclusions may fail for zero external infection rates, non-exponential holding times, state-dependent recovery, or nonlinear/saturating infection rates. A mathematically equivalent earlier formulation in interacting-particle-system or epidemic literature remains a bibliographic risk. The full technical text of Van Mieghem–Cator (2012) was not available for inspection; its accessible abstract establishes complete-graph analysis but is insufficient to rule out every result in the paper.

## References

- Van Mieghem, P., and Cator, E. (2012). *Epidemics in networks with nodal self-infection and the epidemic threshold*. Physical Review E 86, 016116. DOI: 10.1103/PhysRevE.86.016116. First published July 30, 2012.
- Foxall, E. (2014). *Convergence and monotonicity for a model of spontaneous infection and transmission*. Advances in Applied Probability 46, 560–584. DOI: 10.1239/aap/1401369707. Accessible full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/94BC4FB52AA8A9D55BD0B50886E796B0/S0001867800007217a.pdf/div-class-title-convergence-and-monotonicity-for-a-model-of-spontaneous-infection-and-transmission-div.pdf.
- Zhang, J., and Moura, J. M. F. (2015 preprint; 2017 journal publication). *Contact process with exogenous infection and the scaled SIS process*. arXiv:1507.00396; DOI: 10.1093/comnet/cnx003. First publicly submitted July 1, 2015. Full preprint text posted by an author: https://www.researchgate.net/publication/279632927_Contact_Process_with_Exogenous_Infection_and_the_Scaled_SIS_Process.
- Puha, A. L. (1999). *A reversible nearest particle system on the homogeneous tree*. Journal of Theoretical Probability 12, 217–254. DOI: 10.1023/A:1021709013569. Modifies recovery behavior and does not use the strictly constant recovery mechanism assumed here.
