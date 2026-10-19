# A product-form jamming law for random dimers on complete multipartite graphs

## Finding

Fix an integer \(q\geq 3\) and positive real fractions \(a_1,\ldots,a_q\) with \(\sum_{i=1}^{q}a_i=1\). For each \(N\), let \(G_N=K_{n_1(N),\ldots,n_q(N)}\) be the complete \(q\)-partite graph with \(\sum_i n_i(N)=N\) and \(n_i(N)/N\to a_i\). Assign the edges independent atomless identically distributed priorities and accept an edge in increasing-priority order exactly when neither endpoint has previously been matched. Write \(U_N\) for the number of unmatched vertices at termination and put \(a_* = \max_i a_i\).

**Theorem.** The terminal unmatched fraction converges in probability and in mean to
\[
\frac{U_N}{N}\xrightarrow{\mathbb P}r(a_1,\ldots,a_q),\qquad
r(a_1,\ldots,a_q)=
\begin{cases}
\displaystyle a_*\prod_{j\ne i_*}\left(1-\frac{a_j}{a_*}\right),&\text{if the largest fraction occurs only at }i_*,\\[4pt]
0,&\text{if the largest fraction is tied.}
\end{cases}
\]
More precisely, the fraction of terminal unmatched vertices from part \(i_*\) tends to \(r\) when the largest fraction is unique; all other parts have vanishing terminal unmatched fraction. When the largest fraction is tied, every part has a vanishing terminal unmatched fraction.

For example, on \(K_{8m,7m,5m}\) with \(N=20m\), the limit is \(r=3/160\), despite the existence of a perfect matching for every positive integer \(m\). Thus random-priority irreversible dimer deposition can leave a positive proportion of a dense, perfectly matchable substrate unoccupied. The asymmetry requirement is sharp at the macroscopic level: equality of the two largest positive fractions makes the limiting unmatched fraction zero.

## Assumptions and scope

The number \(q\) of nonempty parts is fixed as \(N\to\infty\); each limiting fraction is strictly positive. All cross-part edges are present, all within-part edges are absent, and priorities are independent, identically distributed, and atomless. The result concerns the random-priority maximal matching, not an optimal matching or a different greedy policy that selects a random vertex first. The scaling is by the total number \(N\) of vertices, not by the number of edges. No convergence rate or central limit theorem is claimed, and regimes with \(q=q(N)\) or vanishing fractions are outside the theorem.

## Proof

**1. The exact finite-state dynamics.** Independent exponential priority clocks of mean \(N\), one per edge, induce a uniformly random edge order, equivalent to any independent continuous identically distributed edge priorities. Let \(X_i^{(N)}(t)\) be the number of still-unmatched vertices of part \(i\) by physical time \(t\). An unoccupied edge connecting parts \(i\ne j\) rings at rate \(1/N\) and permanently matches its endpoints. Conditional on the present occupancy vector, the transition that decreases \(X_i^{(N)}\) and \(X_j^{(N)}\) by one occurs at rate \(X_i^{(N)}X_j^{(N)}/N\). Other rings have no effect. The process terminates almost surely at a maximal matching, with the same law as the random-priority construction.

**2. Fixed-time stochastic-to-deterministic limit.** Put \(Y_i^{(N)}=X_i^{(N)}/N\). Its Doob decomposition is
\[
Y_i^{(N)}(t)=Y_i^{(N)}(0)-\int_0^tY_i^{(N)}(s)\sum_{j\ne i}Y_j^{(N)}(s)\,ds+M_i^{(N)}(t).
\]
For every finite \(T\), the predictable quadratic variation satisfies \(\langle M_i^{(N)}\rangle_T\le T/N\). Doob's inequality gives \(\mathbb E\sup_{t\le T}|M_i^{(N)}(t)|^2\le4T/N\). The drift is Lipschitz on the compact cube \([0,1]^q\). The Gronwall inequality therefore gives, uniformly on \([0,T]\) in probability, convergence of \(Y^{(N)}\) to the unique solution of
\[
\dot y_i(t)=-y_i(t)\sum_{j\ne i}y_j(t),\qquad y_i(0)=a_i.
\]
No independence approximation is used: the density-dependent Markov-chain rates above are exact.

**3. Exact product parametrization.** Let \(g(0)=0\) and
\[
\dot g(t)=F(g(t)),\qquad F(z)=\prod_{j=1}^q(1-a_jz).
\]
For \(0\le z<a_*^{-1}\), set \(f_i(z)=a_i\prod_{j\ne i}(1-a_jz)\). Direct differentiation gives
\[
F(z)f_i'(z)=-f_i(z)\sum_{j\ne i}f_j(z).
\]
Hence \(y_i(t)=f_i(g(t))\) solves the initial-value problem. The scalar solution is increasing and cannot leave \([0,a_*^{-1}]\); its limit is \(a_*^{-1}\), because \(F(z)>0\) strictly below that endpoint. Thus
\[
\lim_{t\to\infty}y_i(t)
=a_i\prod_{j\ne i}\left(1-\frac{a_j}{a_*}\right).
\]
The limit is nonzero precisely when \(i\) is the unique maximizer of the fractions. In that case its value is the claimed \(r\); otherwise all limiting coordinates vanish.

**4. Passing from fixed time to complete jamming.** Fix any part index \(h\), and define the current minority count \(B_N(T)=\sum_{i\ne h}X_i^{(N)}(T)\). Every subsequently accepted edge has at least one endpoint outside part \(h\), because there are no edges within a part. Consequently there can be at most \(B_N(T)\) further accepted edges. Deterministically,
\[
0\le\sum_i X_i^{(N)}(T)-U_N\le2B_N(T).
\]
Choose \(h\) with \(a_h=a_*\). The fixed-time convergence and Step 3 imply \(\lim_{T\to\infty}\sum_{i\ne h}y_i(T)=0\), regardless of whether the maximum is tied. First take \(N\to\infty\) for fixed \(T\), then \(T\to\infty\). The displayed inequality implies \(U_N/N\to r\) in probability. It also bounds the change in every class, establishing the classwise assertion. Because \(0\le U_N/N\le1\), convergence in mean follows by bounded convergence in probability.

**5. A perfectly matchable example.** For \(K_{8m,7m,5m}\), a perfect matching can pair \(5m\) vertices from the first and second parts, \(3m\) from the first and third, and \(2m\) from the second and third. Yet the theorem yields
\[
\frac{U_{20m}}{20m}\xrightarrow{\mathbb P}
\frac25\left(1-\frac{7}{8}\right)\left(1-\frac58\right)=\frac3{160}>0.
\]

## Verification

The standalone standard-library program `verify.py` compares exact rational dynamic-programming laws with independent exhaustive priority-order enumeration on four small complete multipartite graphs; checks the product-parametrization differential identity at rational parameters for three, four, and five parts; verifies its endpoint behavior; and performs a seeded finite-size consistency simulation. Running `python verify.py` produced a PASS message for 37 exact identities/checks plus the seeded simulation. For \((a_1,a_2,a_3)=(2/5,7/20,1/4)\), the predicted density is exactly \(3/160\), and the recorded \(N=2000\) sample mean from 48 trials was \(0.01979167\). Simulations are not used to infer the infinite-size limit: Steps 1–4 constitute the analytical proof.

## Relationship to prior work

Deloubrière, Hilhorst, and Täuber study spatial multi-species mutual-annihilation systems and discuss equal-density mean-field kinetics and the qualitative fate of unequal initial concentrations. The finite complete multipartite random-priority matching process, its exact product terminal fraction, and the fixed-time-to-terminal stochastic justification above are distinct statements. Gamarnik and Goldberg analyze random greedy matching on bounded-degree regular/high-girth graphs, not the dense, nonregular multipartite graph sequence in this theorem. Existing results on one fixed/dilute third part of a tripartite graph do not imply the fixed positive-fraction, uniquely largest-part regime or the all-\(q\) product expression. Absence of an exact match in the targeted sources or research index does not prove universal novelty.

## Limitations

The theorem provides only a law of large numbers for fixed \(q\) and positive limiting class fractions. It neither describes finite-size fluctuations near equal-largest-part ties nor extends automatically to nonuniform edge priorities, within-part reactions, spatial diffusion, or growing numbers of classes. The product-form dynamics are algebraically close to familiar mean-field mutual-annihilation equations; specialized earlier analyses of their unequal-density solutions could reduce the novelty of the explicit formula. The originality comparison remains subject to this literature risk and to inaccessible portions of older greedy-matching work.

## References

1. O. Deloubrière, H. Hilhorst, and U. C. Täuber, *Multi-Species Pair Annihilation Reactions*, arXiv:cond-mat/0209471, first posted 19 September 2002, https://arxiv.org/abs/cond-mat/0209471.
2. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277, first posted 8 July 2008; author manuscript https://people.orie.cornell.edu/dag369/ftp/Goldberg_Gamarnik_CPC2009.pdf.
3. J. Aronson, M. Dyer, A. Frieze, and S. Suen, *Randomized greedy matching. II*, Random Structures & Algorithms **6** (1995), 55–73, DOI:10.1002/rsa.3240060107. Its sampled-vertex-first rule differs from the edge-priority rule considered here.
