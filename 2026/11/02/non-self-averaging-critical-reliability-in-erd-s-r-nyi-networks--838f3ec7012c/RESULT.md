# Non-self-averaging critical reliability in Erdős–Rényi networks

## Finding

Fix a real number \(x\) and let \(G_n\) be the labeled simple Erdős–Rényi graph \(G(n,p_n)\), where
\[
p_n=\frac{\log n+x}{n}.
\]
For a fixed graph \(G\), write \(R_G(t)\) for the probability that its independently \(t\)-retained edge subgraph is connected (all-terminal reliability), and
\[
A(G)=\int_0^1 R_G(t)\,dt.
\]
Let \(I_n\) be the number of vertices of degree zero in \(G_n\) and \(Z_n={\bf1}_{\{I_n=0\}}\). Put
\[
\lambda=e^{-x},\qquad h_x(s)=e^{-\lambda(e^s-1)},\qquad
C_x=\int_0^\infty h_x(s)\,ds
=e^{\lambda} E_1(\lambda),
\]
where \(E_1(y)=\int_y^\infty e^{-u}du/u\) for \(y>0\).

**Theorem.** For every fixed \(S>0\),
\[
\sup_{0\le s\le S}\bigg|R_{G_n}\Big(1-\frac{s}{\log n}\Big)
-Z_nh_x(s)\bigg|\xrightarrow{\mathbb P}0.
\]
More strongly, the *random* integrated reliability satisfies
\[
\boxed{\displaystyle
\mathbb E\left[\left(\log n\,A(G_n)-C_xZ_n\right)^2\right]
\longrightarrow0.}
\]
Consequently, with \(B\) Bernoulli of success probability \(e^{-\lambda}\),
\[
\log n\,A(G_n)\ \Longrightarrow\ C_xB,
\]
and the first two limiting moments are
\[
\boxed{\displaystyle
\log n\,\mathbb EA(G_n)\longrightarrow E_1(\lambda),\qquad
(\log n)^2\operatorname{Var}(A(G_n))\longrightarrow
C_x^2e^{-\lambda}(1-e^{-\lambda}).}
\]
Conditional on \(G_n\) being connected, \(\log n\,A(G_n)\) converges in conditional \(L^2\) to \(C_x\). Thus the asymptotic positive value is deterministic on connected networks, but the unconditional distribution has a nonzero atom at zero.

At \(x=0\), the nonzero limit equals \(eE_1(1)\approx0.596347\) and has limiting probability \(e^{-1}\). The limiting annealed mean is \(E_1(1)\approx0.219384\).

## Assumptions and scope

The parameter \(x\in\mathbb R\) is fixed; \(n\to\infty\) through integers for which \(0<p_n<1\). The randomness of \(G_n\) is independent across unordered vertex pairs. Every evaluation of \(R_G(t)\) uses independent edge-retention coins conditional on the realized graph; separate replica evaluations are independent conditional on that graph. The number of vertices is fixed at \(n\), including isolated vertices. No connectivity conditioning is imposed unless explicitly stated. This is an asymptotic theorem; the displayed finite-\(n\) approximation is not claimed to have a uniform error rate in \(x\) or in the full retention interval.

## Proof

**1. Connectivity near the threshold.** For \(q_n=(\log n+a+o(1))/n\) with fixed \(a\), the number \(K_n\) of isolated vertices of \(G(n,q_n)\) converges to \(\operatorname{Poisson}(e^{-a})\). Indeed, for each fixed positive integer \(r\),
\[
\mathbb E(K_n)_r=(n)_r(1-q_n)^{r(n-r)+\binom r2}\longrightarrow e^{-ar}.
\]
Furthermore,
\[
\Pr(G(n,q_n)\text{ disconnected},\ K_n=0)=o(1).
\]
To verify the latter without assuming a stronger unproved connectivity assertion, any disconnected graph with no isolates has a connected component of size \(k\) for some \(2\le k\le n/2\). The probability that a specified \(k\)-set forms a connected component is at most \(k^{k-2}q_n^{k-1}(1-q_n)^{k(n-k)}\) by a spanning-tree union bound. Thus the sum over \(2\le k\le n/\log n\) is \(O(q_n)\): use \(\binom nk\le n^k/k!\), \(k^{k-2}/k!\le e^k\), and \((1-q_n)^{k(n-k)}\le C^k n^{-k}\). For \(n/\log n\le k\le n/2\), omit the connectivity condition and use \(\binom nk(1-q_n)^{k(n-k)}\le(C_a\log n/\sqrt n)^k\) for all sufficiently large \(n\). Both sums vanish. Therefore the probability of connectivity tends to \(e^{-e^{-a}}\).

**2. A two-replica marked-isolate law.** Fix \(s,t\ge0\). Given \(G_n\), generate two independent thinned graphs \(G_n^{(1)}\) and \(G_n^{(2)}\) with retention probabilities \(t_{1,n}=1-s/\log n\) and \(t_{2,n}=1-t/\log n\). For one vertex \(v\),
\[
\begin{aligned}
n\Pr(v\text{ isolated in }G_n^{(1)})&\longrightarrow\lambda e^s,\\
n\Pr(v\text{ isolated in }G_n^{(2)})&\longrightarrow\lambda e^t,\\
n\Pr(v\text{ isolated in both})&=n[1-p_n(1-(1-t_{1,n})(1-t_{2,n}))]^{n-1}
\longrightarrow\lambda.
\end{aligned}
\]
The number of vertices isolated in both thinned graphs but not in the original graph tends to zero in probability, because its expectation is the difference of two expressions converging to \(\lambda\).

Partition isolated vertices by their mark: isolated in both replicas, in the first only, or in the second only. These three counts converge jointly to *independent* Poisson variables with respective means
\[
\lambda,\qquad\lambda(e^s-1),\qquad\lambda(e^t-1).
\]
Here is the necessary joint-moment justification. For any fixed \(r\) distinct named vertices and any finite assignments of required isolation events from the two replicas, all edges from these vertices to unmarked vertices are mutually independent across named vertices. Their probabilities factor into the respective one-vertex isolation probabilities, up to a relative \(1+O(r^2p_n)\) from the \(\binom r2\) edges between named vertices. Inclusion–exclusion converts required (possibly overlapping) isolation events into the three mutually exclusive marks, with joint probability equal to the product of single-vertex mark probabilities plus \(o(n^{-r})\). Multiplication by \((n)_r\) proves convergence of every mixed factorial moment to the corresponding independent Poisson factorial moments. In the zero-mean boundary cases the same statement holds with vanishing factorial moments. Poisson moment determinacy completes the argument.

A graph in the connectivity window is disconnected without isolated vertices with probability \(o(1)\), by Step 1. Applied separately to the two replicas, this also holds jointly by a union bound. Hence
\[
\Pr(G_n^{(1)}\text{ and }G_n^{(2)}\text{ connected})
\longrightarrow
\exp[-\lambda(e^s+e^t-1)].\tag{1}
\]

**3. Conditional reliability profile.** Write
\[
F_n(s)=R_{G_n}(1-s/\log n)\quad(0\le s\le\log n).
\]
A single thinning is an unconditional \(G(n,p_nt_{1,n})\) graph, and \(np_nt_{1,n}=\log n+x-s+o(1)\). Thus
\[
\mathbb E F_n(s)\longrightarrow e^{-\lambda e^s}.
\]
By conditional independence of two thinning experiments and equation (1) with \(t=s\),
\[
\mathbb E F_n(s)^2\longrightarrow e^{-\lambda(2e^s-1)}.
\]
Also, \(F_n(s)=0\) whenever the original graph has an isolated vertex, so \(Z_nF_n(s)=F_n(s)\) exactly; and \(\mathbb EZ_n\to e^{-\lambda}\) by Step 1. Expanding the square gives
\[
\mathbb E\lvert F_n(s)-Z_nh_x(s)\rvert^2\longrightarrow0
\quad\text{for each fixed }s\ge0.
\]
Both \(F_n\) and \(h_x\) are nonincreasing in \(s\), and \(h_x\) is uniformly continuous on compact intervals. A finite mesh sandwich upgrades convergence at mesh points to uniform convergence in probability on each fixed \([0,S]\). This proves the profile assertion.

**4. Control of the integrated tail.** Set \(L_n=\log n\) and \(q_n(s)=p_n(1-s/L_n)\). For the *annealed* thinned graph let \(M_n(s)\) be its isolate count and \(\mu_n(s)=n(1-q_n(s))^{n-1}\). The exact covariance of two distinct isolate indicators gives
\[
\frac{\operatorname{Var}M_n(s)}{\mu_n(s)^2}
\le\frac1{\mu_n(s)}+\frac{q_n(s)}{1-q_n(s)}.
\]
Uniformly for \(0\le s\le L_n\), one has \(\mu_n(s)\ge c_x e^s\) for a positive constant \(c_x\) and \(q_n(s)\le C_x' L_n/n\). Chebyshev's inequality on \(M_n(s)=0\) therefore yields
\[
\mathbb EF_n(s)\le\Pr(M_n(s)=0)
\le C_x''e^{-s}+C_x''L_n/n.
\]
For \(0\le F_n(s)\le1\), monotonicity implies \(F_n(s)F_n(t)\le F_n(\max\{s,t\})\). Consequently, for \(0\le S\le L_n\),
\[
\begin{aligned}
\mathbb E\left(\int_S^{L_n}F_n(s)\,ds\right)^2
&\le2\int_S^{L_n}(s-S)\mathbb EF_n(s)\,ds\\
&\le O_x(e^{-S})+O_x(L_n^3/n).
\end{aligned}
\]
The deterministic tail \(\int_S^\infty h_x(s)ds\) also tends to zero as \(S\to\infty\). On each fixed interval \([0,S]\), Step 3 and boundedness give \(L^2\) convergence of the integrals. Change variables \(t=1-s/L_n\) in the definition of \(A\), apply the two tail estimates, first let \(n\to\infty\) and then \(S\to\infty\). This proves
\[
\mathbb E\left|L_n A(G_n)-C_x Z_n\right|^2\to0.
\]
Finally substitute \(u=\lambda e^s\) to obtain \(C_x=e^\lambda E_1(\lambda)\). The Poisson limit of \(I_n\) proves the two-point distribution limit; the \(L^2\) estimate proves convergence of the first two moments. Connectedness and absence of isolates agree with probability tending to one, while connectivity has limiting probability \(e^{-\lambda}>0\). Conditioning on connectivity proves the stated conditional \(L^2\) limit.

## Verification

The standalone file `verify_critical_reliability.py` uses only the Python standard library. It executes 226 exact or numerical assertions: direct enumeration of all graphs on two through four labeled vertices; rationally exact all-terminal reliability integrals; the annealed percolation identity; independently computed two-thinning connectivity probabilities; closed single-vertex isolate probabilities at three large sample sizes; and two independently parametrized quadratures for \(C_x\). Run using `python3 verify_critical_reliability.py`.

Finite checks validate identities and normalizations, not an infinite-limit proof. The infinite statements rest on the spanning-tree bound, marked-isolate factorial moments, second-moment calculation, and uniform tail estimate above. No external theorem prover or independent certification is claimed.

## Relationship to prior work

Brown, Kolokolnikov and Kooij (2024) introduced an edge-deletion formulation of average all-terminal reliability and explicitly asked for the average reliability of Erdős–Rényi graphs (Open Question 2). Their article provides a general integral identity and heuristic fixed-network approximations; it does not state the present critical-window quenched limit, the conditional deterministic profile, or the two-atom area distribution. Brown, Cox and Ehrenborg (2014) introduced average reliability as a fixed-graph invariant and studied general bounds and extremal families. The classical Erdős–Rényi connectivity-window theorem already implies the *annealed first moment* once thinning and integration are combined; that consequence alone is not claimed as original. The specific new contribution is the shared-isolate, two-replica calculation yielding \(L^2\) concentration conditional on no isolated vertices and a strictly nonvanishing unconditional coefficient of variation.

## Limitations

The claims apply to simple labeled Erdős–Rényi graphs only at the connectivity window with fixed \(x\). They do not provide explicit rates, handle arbitrary degree distributions, all sparsity regimes, dependent edge failures, or vertex reliability. The law has not received independent mathematical validation. The literature comparison is best knowledge rather than a proof of historical priority: broader marked-Poisson connectivity theorems could imply pieces of the argument, and one early paper on average reliability was accessible only through its abstract. There is no assertion that the general 2024 open question is settled in every regime.

## References

1. J. I. Brown, T. Kolokolnikov and R. E. Kooij, *New approximations for network reliability*, **Networks** 84 (2024), 51–63, DOI: https://doi.org/10.1002/net.22215 (first public version of record, 2024-03-04; Sections 2–3 and 6).
2. J. I. Brown, D. Cox and R. Ehrenborg, *The average reliability of a graph*, **Discrete Applied Mathematics** 177 (2014), 19–33, DOI: https://doi.org/10.1016/j.dam.2014.05.048 (abstract and bibliographic record inspected).
3. T. Kolokolnikov, *It is better to be semi-regular when you have a low degree*, arXiv:2112.14289 (2021; version 2 HTML available), https://arxiv.org/html/2112.14289v2 (network comparison; studies a different spectral statistic).
4. P. Erdős and A. Rényi, *On random graphs I*, Publicationes Mathematicae Debrecen 6 (1959), 290–297 (classical random-graph background; the connectivity-window lemma used here is also proved above).
