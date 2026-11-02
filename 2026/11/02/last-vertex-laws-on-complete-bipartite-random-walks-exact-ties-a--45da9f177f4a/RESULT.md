# Last-vertex laws on complete bipartite random walks: exact ties and a logistic imbalance window

## Finding
Let a simple random walk start from a specified vertex of part \(A\) of the complete bipartite graph \(K_{a,b}\), where \(|A|=a\ge1\) and \(|B|=b\ge1\). Stop upon first visiting all vertices. Write \(L_{a,b}\) for the probability that the last newly visited vertex belongs to \(B\), and let \(C_m\) be the number of independent uniform draws from \(m\) coupon types needed to see every type, including the first draw. Independent copies of \(C_a,C_b\) are understood.

The **exact comparison identity**, for every pair of positive integers, is
\[
L_{a,b}=\Pr(C_b\ge C_a).
\]
In particular, for balanced parts \(a=b=m\), with \(p_m(t)=\Pr(C_m=t)\),
\[
L_{m,m}=\frac12+\frac12\sum_{t=m}^{\infty}p_m(t)^2
=\frac12+\frac1{8m}+o(m^{-1})\qquad(m\to\infty).
\]
Thus the starting part loses the last-vertex race with a small but strictly positive finite-size bias. The leading coefficient is exact.

For positive integer sequences \(a_n,b_n\) such that \(a_n/n\to1\), \(b_n/n\to1\) and
\[
\frac{(b_n-a_n)\log n}{n}\longrightarrow\delta\in\mathbb R,
\]
there is a sharp **logistic imbalance window**:
\[
L_{a_n,b_n}\longrightarrow \frac{1}{1+e^{-\delta}}.
\]
The window for competition between the two vertex classes therefore has width of order \(n/\log n\); exact balance has a smaller, nonzero discrete tie correction of order \(n^{-1}\).

## Assumptions and scope
The graph is finite, simple, undirected and complete bipartite, with independent uniform choice from the neighbors at every walk step. The starting vertex is specified in \(A\); there are no self-loops or holding probabilities. Its initial visit counts as visited. The event concerns the *last newly encountered vertex*, not the vertex occupied at an arbitrary fixed time. The coupon variables in the comparison identity are independent, with geometric waiting times supported on positive integers. The asymptotic theorem holds for any sequences satisfying the displayed limits, including negative \(\delta\), but does not assert a uniform rate over unbounded parameter sets.

## Proof
**1. Independent alternating coupon streams.** The walk alternates between the two classes. On every visit to \(B\), its location is a fresh uniform choice among \(b\) vertices, independent of all previous choices; likewise each visit to \(A\) after time zero is a fresh uniform choice among \(a\) vertices. The two streams can thus be constructed independently. Let \(S_A\) be the number of post-start visits to \(A\) required to see all vertices of \(A\), and \(S_B\) the number of visits to \(B\) required to see all of \(B\). Their completion walk times are \(2S_A\) and \(2S_B-1\). Thus the last new vertex is in \(B\) precisely when \(S_B>S_A\). In a full \(a\)-type coupon collection, the first draw necessarily discovers one type, and conditional on its identity the remaining waiting time has exactly the distribution of \(S_A\). Therefore \(S_A\stackrel d=C_a-1\), while \(S_B\stackrel d=C_b\); independence survives this construction. Since these variables are integer valued, \(S_B>S_A\) is equivalent in distribution to \(C_b\ge C_a\). This proves the exact identity, including \(a=1\) or \(b=1\).

The full last-vertex distribution also follows: each particular vertex of \(B\) has probability \(L_{a,b}/b\) to be last. When \(a>1\), each vertex of \(A\) other than the starting point has probability \((1-L_{a,b})/(a-1)\), while the starting vertex has probability zero.

**2. Effective finite formula.** For any \(m\ge1\), inclusion-exclusion gives, at every integer \(t\ge0\),
\[
\Pr(C_m\le t)=\sum_{j=0}^m(-1)^j\binom mj(1-j/m)^t,
\]
with \(0^0=1\). If \(G_s\) denotes an independent geometric variable with success probability \(s/a\), then \(C_a-1\stackrel d=\sum_{s=1}^{a-1}G_s\). Consequently
\[
L_{a,b}=\sum_{j=1}^b(-1)^{j+1}\binom bj
\prod_{s=1}^{a-1}\frac{s(1-j/b)}{a-(a-s)(1-j/b)}.
\]
An empty product equals one. This is a finite rational expression for every \(a,b\).

**3. Exact balanced tie law.** Let \(C_m'\) be independent and identically distributed with \(C_m\). By exchangeability,
\[
\Pr(C_m'\ge C_m)=\frac12\bigl(1+\Pr(C_m'=C_m)\bigr)
=\frac12\bigl(1+\sum_{t=m}^\infty p_m(t)^2\bigr).
\]
The tie probability is strictly positive, so the bias is strict at every finite \(m\).

**4. Sharp tie coefficient.** After \(k\) draws on \(m\) coupons, write \(U_{m,k}\) for the number of unseen types. Completion on the next draw requires exactly one unseen type, followed by that type, giving the exact local identity
\[
p_m(k+1)=m^{-1}\Pr(U_{m,k}=1),\qquad mp_m(k+1)\le1.
\]
For each fixed real \(x\), at \(k_m=\lfloor m\log m+mx\rfloor\), the factorial moments satisfy
\[
\mathbb E[(U_{m,k_m})_r]=(m)_r(1-r/m)^{k_m}\longrightarrow e^{-rx}
\]
for every fixed nonnegative integer \(r\), hence \(U_{m,k_m}\) converges to a Poisson variable of mean \(e^{-x}\). Therefore
\[
mp_m(k_m+1)\longrightarrow g(x):=e^{-x}\exp(-e^{-x}).
\]
The same factorial-moment argument shows \((C_m-m\log m)/m\Rightarrow G\), where \(G\) is the standard Gumbel distribution, \(\Pr(G\le x)=\exp(-e^{-x})\). The local convergence is uniform when \(x\) ranges over a compact interval: otherwise a violating sequence has a convergent subsequence of its \(x\)-parameters, contradicting the same factorial-moment limit. Combined with tightness and \(0\le mp_m(t)\le1\), it follows that
\[
m\sum_t p_m(t)^2=\mathbb E[mp_m(C_m)]\longrightarrow \mathbb E[g(G)]
=\int_{-\infty}^{\infty}g(x)^2\,dx
=\int_0^\infty u e^{-2u}\,du=\frac14.
\]
Here the final integral uses \(u=e^{-x}\). Substitution into Step 3 proves \(L_{m,m}=1/2+1/(8m)+o(m^{-1})\).

**5. Logistic boundary.** Independent standard coupon limits imply
\[
\left(\frac{C_{a_n}-a_n\log a_n}{a_n},\frac{C_{b_n}-b_n\log b_n}{b_n}\right)
\Rightarrow(G_A,G_B),
\]
with independent standard Gumbels. Since \(a_n/n,b_n/n\to1\) and \((b_n-a_n)\log n/n\to\delta\), the mean-value theorem gives \((b_n\log b_n-a_n\log a_n)/n\to\delta\). Therefore \((C_{b_n}-C_{a_n})/n\Rightarrow\delta+G_B-G_A\). This limit has a continuous distribution, so the distinction between \(\ge0\) and \(>0\) disappears. Finally independent standard Gumbels have logistic difference: \(\Pr(G_B-G_A\ge-\delta)=1/(1+e^{-\delta})\). Combining with Step 1 proves the stated window.

## Verification
Run `python3 check.py` using Python 3 and only the standard library. The checker implements an **independent exact Markov-state recursion** on the two visited-class counts and compares it to the rational coupon generating-function identity over all \(1\le a,b\le8\). It also checks boundary cases, separately computes balanced tie probabilities from occupancy chains, and performs approximate finite-size diagnostics for the \(1/(8m)\) coefficient and logistic transition. The package checker produced `PASS 158 exact and numerical assertions`. These are finite corroborations; the unbounded statements are proved analytically in Steps 4–5.

## Relationship to prior work
Lovász and Winkler (1993) characterized graphs whose last new vertex is uniform. Buchanan, Horn and Rombach (2022 preprint, later 2023 publication) extended the characterization to directed graphs. Their short original preprint is concerned with a graph-wide uniformity characterization, not this specific size-sensitive full law, balanced tie coefficient or logistic part-imbalance window. The Gumbel limit for a uniform coupon collector is classical. Ilienko (2026) obtains logistic differences of *different collection levels in the same extended coupon process*; this demonstrates the generality of Gumbel differences, but its variables and centering are not the two independent, unequal-size streams here. We claim neither novelty of the Gumbel or logistic distributions nor novelty of the general cover-tour characterization. The proposed contribution is the conjunction of the exact cover-tour comparison identity, sharp balanced lattice correction and graph-specific critical-size window. Relevant general probability results can be used to rederive the asymptotic steps.

## Limitations
The result applies only to simple random walks on complete bipartite graphs from a specified side. The logistic law is a weak limit, not a quantitative error estimate; the \(o(m^{-1})\) term is not given an explicit bound. The published 1993 original paper could not be read in full during literature checking; prior coverage of a special bipartite case is a residual priority risk. No independent mathematical assessment has been performed. The exact finite formula does not by itself establish a universal statement for other bipartite graphs.

## References
1. C. Buchanan, P. Horn, P. Rombach, *On the Last New Vertex Visited by a Random Walk in a Directed Graph*, arXiv:2209.08079, first submitted 16 September 2022, https://arxiv.org/abs/2209.08079 (full four-page preprint inspected).
2. L. Lovász, P. Winkler, *A note on the last new vertex visited by a random walk*, Journal of Graph Theory 17 (1993), 593–596, https://doi.org/10.1002/jgt.3190170505 (abstract and bibliographic record inspected; full text inaccessible).
3. A. Ilienko, *Limit theorems in the extended coupon collector’s problem*, VMSTA (2026), https://doi.org/10.15559/26-VMSTA306 (Theorem 3 and Corollary 1 inspected).
4. J. C. Saunders, *The number of K-tons in the coupon collector problem*, Journal of Applied Probability 60 (2023), 723–736, https://doi.org/10.1017/jpr.2022.94 (abstract and classification inspected; distinct stopping statistic).
