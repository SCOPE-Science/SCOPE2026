# Component–degree covariance signs and terminal contrast in the Moran forest

## Finding
Consider the stationary Moran forest on \(n\ge 2\) vertices. Let \(K_n\) count its tree components, \(H_{n,r}\) count vertices of **total undirected degree** exactly \(r\), and \(Z_n\) count vertices with no outgoing edges (including isolated vertices). These are label-invariant statistics.

For \(n\ge3\), write \(m=n-1\), \(a=(m-1)/m\), and
\[
b_{k,s}=\begin{cases}\binom{k}{s}m^{-s}a^{k-s},&0\le s\le k,\\0,&\text{otherwise.}\end{cases}
\]
For every integer \(0\le r\le n-1\), the exact finite-size component/degree-count covariance is
\[
\boxed{\operatorname{Cov}(K_n,H_{n,r})=
\sum_{k=1}^{m}\frac{k}{m^3}\left[
\left((m-k)(m-1)+\frac{k(k-1)}2\right)(b_{k-1,r}-b_{k-1,r-1})
+\frac{(m-k)(k+1)}2(b_{k-1,r-1}-b_{k-1,r-2})\right].}
\]
Its **complete sign diagram** is
\[
\begin{array}{c|c}
\text{class}&\operatorname{Cov}(K_n,H_{n,r})\\\hline
r=0&>0\\
r=1&=0\text{ if }n=3;\ <0\text{ if }n\ge4\\
2\le r\le n-1&<0
\end{array}
\]
For \(n=2\), the component count is constant and all covariances are zero. Outside the degree range \(0\le r\le n-1\), \(H_{n,r}=0\). The degree-one covariance has the useful factorization
\[
\boxed{\operatorname{Cov}(K_n,H_{n,1})=-\sum_{k=1}^{m-2}
\frac{k(m-k)(m-k-1)(2m-k-1)}{2m^4}
\left(1-\frac1m\right)^{k-2}.}
\]
This empty sum is zero for \(n=3\), and every summand is positive inside the outer minus sign for \(n\ge4\).

In contrast, the zero-outdegree statistic obeys
\[
\boxed{\operatorname{Cov}(K_n,Z_n)=
\sum_{k=2}^{m}\frac{k(k-1)}{2m^2}\left(1-\frac1m\right)^{k-1}>0\qquad(n\ge3).}
\]
For \(n=2\) this covariance is zero. Thus increased component count is associated with **fewer undirected degree-one vertices**, but **more zero-outdegree terminal vertices**.

Finally, the dependencies are of linear order with distinct nonzero limits:
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(K_n,H_{n,1})}{n}=4-\frac{11}{e}<0,\qquad
\lim_{n\to\infty}\frac{\operatorname{Cov}(K_n,Z_n)}{n}=1-\frac{5}{2e}>0.}
\]

## Assumptions and scope
At each step of the finite-state Moran-forest chain, choose an ordered pair \((u,v)\) of distinct vertices uniformly, disconnect \(v\) from its previous neighbors and connect \(u\) to \(v\). The stationary distribution is the Moran forest. All statements concern this model, not the uniform law on increasing recursive forests.

Proposition 2.1 of Bienvenu–Duchamps–Foutel-Rodier supplies an equivalent sampler up to an independent uniform relabeling: for every \(j\in\{1,\ldots,n\}\), choose \(U_j\) independently and uniformly from \(\{1,\ldots,n\}\setminus\{j\}\), and insert the directed edge \(U_j\to j\) precisely when \(U_j<j\). The statistics in the theorem are invariant under that relabeling. Outdegree counts children and indegree indicates a parent; a zero-outdegree vertex may be an isolate, so \(Z_n\) is not the same statistic as \(H_{n,1}\).

## Proof
Let \(B_j=\mathbf1_{\{U_j>j\}}\) and \(C_j=\sum_{\ell=j+1}^n\mathbf1_{\{U_\ell=j\}}\). Put \(k=n-j\) and \(m=n-1\). Independence of the parent choices yields
\[
B_j\sim\operatorname{Ber}(k/m),\qquad
C_j\sim\operatorname{Bin}(k,1/m),\qquad B_j\perp C_j.
\]
The number of components and the total degree of position \(j\) are respectively
\[
K_n=\sum_{j=1}^n B_j,\qquad D_j=(1-B_j)+C_j,\qquad H_{n,r}=\sum_{j=1}^n\mathbf1_{\{D_j=r\}}.
\]
The first equality uses the fact that every component has exactly one vertex with no parent.

Fix \(j\) and write \(k=n-j\). The term involving \(B_j\) itself is
\[
\operatorname{Cov}(B_j,\mathbf1_{\{D_j=r\}})=
\frac{k(m-k)}{m^2}(b_{k,r}-b_{k,r-1}).
\]
For \(\ell<j\), \(B_\ell\) depends only on \(U_\ell\), and is independent of \(D_j\). If \(\ell>j\), the mutually exclusive events \(U_\ell>\ell\) and \(U_\ell=j\) yield
\[
\operatorname{Cov}(B_\ell,\mathbf1_{\{D_j=r\}})=
\frac{n-\ell}{m^2}\left[
\frac{k}{m}(b_{k-1,r}-b_{k-1,r-1})
+\frac{m-k}{m}(b_{k-1,r-1}-b_{k-1,r-2})\right].
\]
Indeed, conditioning on \(B_\ell=1\) forces the \(\ell\)-th contribution to \(C_j\) to vanish, whereas unconditionally that contribution is Bernoulli with success probability \(1/m\). Summing over \(\ell>j\), use \(\sum_{\ell=j+1}^n(n-\ell)=k(k-1)/2\). Finally apply
\[
b_{k,s}=\left(1-\frac1m\right)b_{k-1,s}+\frac1m b_{k-1,s-1}.
\]
The resulting contributions, collected by \(k\), are exactly the boxed finite-size formula.

For \(r=0\), the second bracket is zero and the first difference is \(b_{k-1,0}>0\); its coefficient is nonnegative, and the \(k=m\) coefficient is strictly positive when \(m\ge2\). This proves strict positivity.

For \(r\ge2\), the binomial mass \(b_{k-1,s}\) is nonincreasing in \(s\ge0\), because its consecutive ratio for \(1\le s\le k-1\) is \((k-s)/(s(m-1))\le1\); zero values beyond the support preserve this monotonicity. Both bracketed differences are therefore nonpositive, and the \(k=m\) term is strictly negative whenever \(2\le r\le m\). This proves negativity.

For \(r=1\), substitute \(b_{k-1,0}=a^{k-1}\) and \(b_{k-1,1}=(k-1)a^{k-2}/m\) into the coefficient of the \(k\)-th summand. Direct multiplication gives the **termwise factorization**
\[
\frac{k}{m^3}\left[\left((m-k)(m-1)+\frac{k(k-1)}2\right)(b_{k-1,1}-b_{k-1,0})
+\frac{(m-k)(k+1)}2b_{k-1,0}\right]
=-\frac{k(m-k)(m-k-1)(2m-k-1)}{2m^4}a^{k-2}.
\]
The terms with \(k=m-1,m\) vanish; all remaining terms are strictly negative if \(m\ge3\), and no such term exists if \(m=2\).

For terminal vertices, \(\mathbf1_{\{C_j=0\}}\) is independent of \(B_\ell\) for \(\ell\le j\). For \(\ell>j\) the same disjointness gives
\[
\operatorname{Cov}(B_\ell,\mathbf1_{\{C_j=0\}})
=\frac{n-\ell}{m^2}\left(1-\frac1m\right)^{k-1}.
\]
The sum over \(j\) and \(\ell>j\) proves the stated \(Z_n\) formula. Its terms are nonnegative and the \(k=2\) term is positive.

Set \(x=k/m\). The elementary uniform convergence \((1-1/m)^{k-O(1)}\to e^{-x}\) along \(k/m\to x\in[0,1]\), with bounded polynomial factors, turns the two exact sums into Riemann integrals. In order, the limiting constants are
\[
-\frac12\int_0^1x(1-x)^2(2-x)e^{-x}\,dx=4-\frac{11}{e},\qquad
\frac12\int_0^1x^2e^{-x}\,dx=1-\frac{5}{2e}.
\]
These integrals are evaluated by elementary integration by parts. This concludes the proof.

## Verification
The accompanying standard-library-only `verify.py` independently enumerates all \((n-1)^{n-1}\) choices of parent candidates for each \(2\le n\le8\), directly constructs every forest and computes the empirical exact-rational covariances. It checks all degree classes and terminal counts against the derived formulas, checks the degree-one factorization and sign diagram for \(3\le n\le70\), and tests numerical convergence at four larger sizes. The verifier reports 2,614 successful assertions and `VERIFY_OK`. This finite check is corroborative; the preceding identities and Riemann-sum argument prove the statements for every admissible \(n\) and the limit.

## Relationship to prior work
Bienvenu, Duchamps and Foutel-Rodier (2019 preprint, 2021 journal) introduce the stationary Moran forest and establish its uniform-attachment sampler (Proposition 2.1), its **marginal** component count (Section 3), and its **marginal** degree law (Section 4). Their marginal results and the sampling representation are used with attribution here. Neither the component-count/degree-histogram covariance matrix row nor the degree-one/terminal sign contrast is stated there. Unlike their marginal formulas, the joint claims require contributions from the shared independent attachment choices.

Balińska, Quintas and Szymański (1994) study *uniform random recursive forests*. As explicitly distinguished by Bienvenu and coauthors in Section 2.2, the Moran-forest sampler does not give the uniform distribution on recursive forests, so results on that distinct probability law cannot be transferred without a measure comparison. Published work on ordinary recursive-tree root degree and leaf count also concerns a different law, not the stationary Moran forest.

## Limitations
The claim concerns finite-size covariance and two first-order asymptotic covariances, not independence, monotone regression, negative association, or full joint limit laws. The proof requires only the proved sampler and finite calculations; the computational checker does not certify the infinite theorem by enumeration. Historical-priority uncertainty remains: a broader joint-moment identity in less visible prior work may imply some formulas. The complete 1994 paper was not available for full-text inspection, although its published abstract and the primary Moran-forest comparison establish a distinct forest model. This is a self-review; no independent audit has been conducted.

## References
1. F. Bienvenu, J.-J. Duchamps, and F. Foutel-Rodier, *The Moran forest*. arXiv:1906.08806, first submitted 20 June 2019; Random Structures & Algorithms **59** (2021), 155–188. https://arxiv.org/abs/1906.08806 .
2. K. T. Balińska, L. V. Quintas, and J. Szymański, *Random recursive forests*. Random Structures & Algorithms **5** (1994), 3–12. https://doi.org/10.1002/rsa.3240050103 .
