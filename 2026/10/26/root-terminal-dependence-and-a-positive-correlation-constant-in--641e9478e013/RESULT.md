# Root–terminal dependence and a positive correlation constant in the Moran forest

## Finding

For every integer \(n\ge3\), let \(R_n\) be the number of tree components and \(L_n\) the number of **terminal vertices** (vertices with no children, including isolated roots) in the stationary \(n\)-vertex Moran forest. Write \(q_n=(n-2)/(n-1)\). Then

\[
\operatorname{Cov}(R_n,L_n)=\frac{1}{2(n-1)^2}\sum_{m=1}^{n-1}m(m-1)q_n^{m-1}>0.
\]

The dependence has a finer monotone structure. In the increasing-label construction, write \(H_j\) for the event that arrival \(j\) begins a new tree, for \(2\le j\le n-1\). Conditioning on an arbitrary fixed pattern of the other root indicators, changing \(H_j\) from zero to one makes the **entire distribution** of the terminal count stochastically larger. Its unconditional conditional-mean influence is

\[
\Delta_{n,j}:=\mathbb E[L_n\mid H_j=1]-\mathbb E[L_n\mid H_j=0]
=\frac{1}{j-1}\sum_{i=1}^{j-1}q_n^{n-i-1},
\]

and \(\Delta_{n,2}<\cdots<\Delta_{n,n-1}\) whenever this index range contains at least two elements. If \(j/n\to s\in(0,1)\), then \(\Delta_{n,j}\to e^{-1}(e^s-1)/s\), a strictly increasing function of \(s\).

Despite this positive root–terminal dependence, terminal indicators at distinct vertices are **nonpositively correlated** (strictly negatively so when both can have children). The global dependence persists asymptotically:

\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(R_n,L_n)}n
=1-\frac5{2e},\qquad
\lim_{n\to\infty}\frac{\operatorname{Var}(L_n)}n
=\frac1e-\frac2{e^2},
\]

and, using the previously known root-count variance,

\[
\lim_{n\to\infty}\operatorname{Corr}(R_n,L_n)
=\frac{2e-5}{2}\sqrt{\frac6{e-2}}
=0.6308785600416852\ldots .
\]

## Assumptions and scope

The stationary Moran forest is the rooted directed forest of Bienvenu, Duchamps and Foutel-Rodier [1]. We use their exact independent-parent representation before its final uniform relabeling: for each \(j\in\{1,\ldots,n\}\), choose independently \(U_j\) uniformly in \(\{1,\ldots,n\}\setminus\{j\}\); retain a directed parent-to-child edge \(U_j\to j\) precisely when \(U_j<j\). The relabeling does not affect component counts or numbers of terminal vertices. A terminal vertex means a vertex with outdegree zero in this rooted orientation; this is **not** synonymous with undirected degree zero.

Put \(H_j=\mathbf1\{U_j>j\}\). In particular, \(H_1=1\) and \(H_n=0\) deterministically, and the other \(H_j\) are mutually independent with \(\Pr(H_j=1)=(n-j)/(n-1)\). Let \(A_i=\mathbf1\{U_j\ne i\text{ for every }j>i\}\); then \(R_n=\sum_jH_j\) and \(L_n=\sum_iA_i\). All formulas refer to the unconditional stationary forest, except where conditioning is explicitly stated.

## Proof

**Coupling and root influences.** Fix any choices of root indicators except \(H_j\). For each other arrival, choose its parent independently from the allowed set determined by its indicator. Couple the two alternatives at arrival \(j\) by choosing an earlier parent when \(H_j=0\) and a later potential parent when \(H_j=1\). Since only the earlier choice produces an edge, the second forest is obtained from the first by deleting exactly one parent-to-child edge. Removing this edge cannot turn a terminal vertex into a nonterminal one: it either increases the terminal count by one (if the parent had one child) or leaves it unchanged. All other child lists are identical. This coupling proves the claimed conditional stochastic order, for any fixed other root-indicator pattern.

Only earlier vertices can lose terminal status when \(j\) attaches. For each \(i<j\), conditional on \(H_j=1\), \(i\) is unaffected by arrival \(j\); conditional on \(H_j=0\), the parent is uniformly distributed over \(\{1,\ldots,j-1\}\). The probability that \(i\) receives no child from arrivals other than \(j\) equals \(q_n^{n-i-1}\). Thus the influence is the stated arithmetic mean of \(q_n^{n-i-1}\), over \(i<j\). As \(i\) increases these terms increase strictly, so the successive arithmetic means do likewise. For \(j/n\to s\), a Riemann sum gives \(e^{-1}(e^s-1)/s\), whose derivative is positive for \(s>0\).

**Exact covariance.** For \(i<j\), direct independence of the parent choices gives

\[
\operatorname{Cov}(H_j,A_i)
=\frac{n-j}{(n-1)^2}q_n^{n-i-1},
\]

and for \(i\ge j\) this covariance is zero. Indeed \(H_j=1\) precludes \(U_j=i\) when \(i<j\); apart from this one choice, the terminal event for \(i\) uses independent variables. Summing over \(i<j\) and reversing order yields

\[
\operatorname{Cov}(R_n,L_n)
=\frac1{(n-1)^2}\sum_{i=1}^{n-2}
q_n^{n-i-1}\sum_{j=i+1}^{n-1}(n-j)
=\frac1{2(n-1)^2}\sum_{m=1}^{n-1}m(m-1)q_n^{m-1}.
\]

It is strictly positive for every \(n\ge3\). Setting \(m/n\to t\) and using \(q_n^{m-1}\to e^{-t}\) gives a Riemann-sum limit \(\frac12\int_0^1 t^2e^{-t}\,dt=1-5/(2e)\).

**Terminal covariance and variance.** Put \(r_n=(n-3)/(n-1)\). For \(i<j\), avoiding \(i\) at each arrival in \(\{i+1,\ldots,j\}\) and avoiding both \(i,j\) at arrivals after \(j\) yields

\[
\mathbb EA_i=q_n^{n-i},\qquad
\mathbb E(A_iA_j)=q_n^{j-i}r_n^{n-j}.
\]

Thus, because \(r_n\le q_n^2\), distinct terminal indicators have nonpositive covariance, with strict inequality for \(j<n\). Write their exact variance as

\[
\operatorname{Var}(L_n)
=\sum_{i=1}^n q_n^{n-i}(1-q_n^{n-i})
+2\sum_{1\le i<j\le n}
\bigl(q_n^{j-i}r_n^{n-j}-q_n^{2n-i-j}\bigr).
\]

For \(n\ge4\), \(r_n/q_n^2=1-(n-2)^{-2}\). Uniformly over \(1\le i<j\le n\), expansion gives

\[
\left(\frac{r_n}{q_n^2}\right)^{n-j}-1
=-\frac{n-j}{(n-2)^2}+O(n^{-2}).
\]

The diagonal sum divided by \(n\) tends to \(\int_0^1(e^{-t}-e^{-2t})dt=\frac12-e^{-1}+\frac12e^{-2}\). The off-diagonal sum divided by \(n\) tends to

\[
-2\int_0^1\!\int_0^u v e^{-u-v}\,dv\,du
=-\frac12+\frac2e-\frac5{2e^2}.
\]

Adding proves \(\operatorname{Var}(L_n)/n\to e^{-1}-2e^{-2}>0\). From [1, Proposition 3.1], \(\operatorname{Var}(R_n)=n(n-2)/(6(n-1))\), so \(\operatorname{Var}(R_n)/n\to1/6\). Dividing the covariance limit by the square root of these two variance limits gives the stated nonzero Pearson correlation constant.

## Verification

Run `python3 verify.py` in a directory containing the accompanying standalone checker. The checker enumerates every allowed independent-parent configuration for \(3\le n\le7\), reproduces exact means, variances, cross-covariances and conditional root influences with rational arithmetic; checks the closed identities and influence ordering for \(3\le n\le120\); and checks the numerical asymptotic constants. Exact enumeration covers 4, 27, 256, 3125, and 46656 configurations respectively. No finite computation substitutes for the analytical proof.

## Relationship to prior work

Bienvenu, Duchamps and Foutel-Rodier [1, Proposition 2.1, Proposition 3.1, Section 4] establish the independent-parent construction, the component-count moments and single-vertex degree distributions. These antecedents are used explicitly. The new assertion is the coupled terminal-count stochastic monotonicity, strictly ordered birth-time influences, exact cross-covariance, negative terminal-indicator covariances, and associated nonzero limiting Pearson correlation **for this particular stationary Moran forest**. None is asserted to be independent of the underlying published construction; instead, the proof derives them from it.

Balińska, Quintas and Szymański [2] study a *uniform random recursive forest*, a distribution distinct from [1]'s independently thinned attachment construction (as [1, Section 2.2] notes). A previously reported result on root-degree/leaf covariance for a single uniform recursive tree [3] concerns a different random object and statistic. These comparisons are substantive but do not establish absolute historical novelty.

## Limitations

The result classifies covariance and a stochastic coupling; it does not establish joint asymptotic normality, concentration, or statistical independence. Terminal vertices are outdegree-zero nodes and should not be confused with undirected isolated vertices. The separate 1994 recursive-forest paper [2] was accessible as an abstract but its full text was not established to be available for inspection; this leaves a historical-priority risk for general forest covariance identities. The full primary Moran-forest preprint [1] was inspected. Independently authored verification has not been performed.

## References

[1] François Bienvenu, Jean-Jil Duchamps, Félix Foutel-Rodier, *The Moran forest*, first public preprint 20 June 2019, arXiv:1906.08806, https://arxiv.org/pdf/1906.08806 ; journal edition *Random Structures & Algorithms* 59 (2021), 155–188, doi:10.1002/rsa.20997. Especially Sections 2.2, 3.1 and 4.1.

[2] Krystyna T. Balińska, Louis V. Quintas, Jerzy Szymański, *Random recursive forests*, *Random Structures & Algorithms* 5 (1994), 3–12, doi:10.1002/rsa.3240050103.

[3] *Equal-share covariance of root degree and leaves in a random recursive tree*, mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-equal-share-covariance-of-root-degree-and-leaves-in-a-random-rec--ab0acf44833f (summary-level comparison only).
