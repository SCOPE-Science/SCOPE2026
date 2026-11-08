# A golden-ratio covariance transition for height and leaves in two-lag Bernoulli trees

## Finding

**Theorem.** Fix \(0<p<1\) and put \(q=1-p\). Start with the rooted edge \(v_0v_1\). Independently for every integer \(n\ge 2\), attach the new vertex \(v_n\) to \(v_{n-1}\) with probability \(p\), or to \(v_{n-2}\) with probability \(q\). Let \(H_n\) be the maximum root-to-vertex distance in the tree on \(v_0,\ldots,v_n\), and let \(L_n\) count its root-oriented leaves, i.e. vertices having no children. Then

\[
\frac{1}{\sqrt n}\begin{pmatrix}H_n-n/(1+q)\\ L_n-npq\end{pmatrix}
\xrightarrow{\mathrm d} N_2(0,\Sigma(q)),
\qquad
\Sigma(q)=pq\begin{pmatrix}
(1+q)^{-3}&(q^2+q-1)(1+q)^{-2}\\
(q^2+q-1)(1+q)^{-2}&1-3pq
\end{pmatrix}.
\]

Furthermore, each entry of the covariance matrix of \((H_n,L_n)\) equals \(n\) times the corresponding entry of \(\Sigma(q)\), up to an \(O(1)\) error (whose constant may depend on \(p\)). In particular, with \(q_\star=(\sqrt5-1)/2\), the covariance is eventually strictly negative for \(q<q_\star\) and strictly positive for \(q>q_\star\). At \(q=q_\star\), the two limiting Gaussian coordinates are independent. The covariance matrix is positive definite for every \(0<q<1\), with
\[
\det \Sigma(q)=\frac{p^2q^4(1+q-q^2)}{(1+q)^4}>0.
\]

## Assumptions and scope

The attachment bits \(B_n\), \(n\ge2\), are independent with \(\Pr(B_n=1)=p\); define \(B_1=1\) deterministically. The label \(n\) designates the newest vertex, so the tree has \(n+1\) vertices and \(n\) edges. The fixed-parameter statement is for \(p\) strictly inside \((0,1)\). All limits are as integer \(n\to\infty\); no claim is made for parameter sequences approaching the endpoints.

## Proof

**1. Exact finite-tree recursions.** Write \(D_n\) for the depth of \(v_n\), with \(D_0=0,D_1=1\), and \(X_n=D_n-D_{n-1}\) for \(n\ge1\). Parent selection yields
\[
X_1=1,\qquad X_n=\begin{cases}1,&B_n=1,\\1-X_{n-1},&B_n=0.\end{cases}
\]
By induction \(X_n\in\{0,1\}\) for every \(n\). Thus depths are nondecreasing, \(H_n=D_n\), and \(H_n=1+\sum_{i=2}^nX_i\). Counting whether an attachment destroys a leaf gives the *exact* identity
\[
L_n=1+\sum_{i=2}^n\mathbf1\{B_{i-1}=1,B_i=0\}.
\]
Indeed a new attachment to the latest vertex replaces its leaf by a new leaf; attachment to the penultimate vertex adds a leaf exactly when the preceding attachment chose the latest vertex.

**2. Independent renewal blocks.** Use successive successes \(B_i=1\) as regeneration points, starting from the deterministic success \(B_1=1\). The numbers \(K\) of failures \(B_i=0\) before successive successes are independent, with \(\Pr(K=k)=pq^k\), \(k=0,1,\ldots\). A completed block lasts \(T=K+1\) arrivals. Its height-increment reward and leaf-increment reward are, respectively,
\[
R=\lfloor K/2\rfloor+1,\qquad S=\mathbf1\{K\ge1\}.
\]
The height reward follows from alternating \(0,1,0,1,\ldots\) height increments during failures, followed by an increment \(1\) at success. The leaf reward records the first failure after a success. Consequently
\[
\mathbb ET=1/p,\quad \mathbb ER=1/(1-q^2),\quad\mathbb ES=q,
\quad v=\frac{\mathbb ER}{\mathbb ET}=\frac1{1+q},
\quad \ell=\frac{\mathbb ES}{\mathbb ET}=pq.
\]
The unfinished final block has a geometrically bounded length and bounded moments of every fixed order uniformly in \(n\). Its contributions to the centered total rewards are therefore \(O_{L^r}(1)\) for every fixed finite \(r\). Standard vector renewal-reward CLT, or its proof by iid vector CLT plus the renewal law \(N(n)/n\to p\), now gives the asserted joint normal limit with covariance
\[
\Sigma=p\,\mathbb E\left[
\begin{pmatrix}R-vT\\S-\ell T\end{pmatrix}
\begin{pmatrix}R-vT&S-\ell T\end{pmatrix}
\right].
\]

**3. Explicit covariance.** Note \(R=T/2+\tfrac12\mathbf1\{K\text{ even}\}\). Direct geometric-series differentiation gives
\[
\mathbb ET^2=\frac{1+q}{p^2},\quad
\Pr(K\text{ even})=\frac1{1+q},\quad
\mathbb E[T\mathbf1\{K\text{ even}\}]=\frac{1+q^2}{p(1+q)^2},\quad
\mathbb E[T\mathbf1\{K\ge1\}]=\frac1p-p.
\]
Substituting these into the centered reward second moments yields
\[
\Sigma_{11}=\frac{pq}{(1+q)^3},\qquad
\Sigma_{22}=pq(1-3pq),\qquad
\Sigma_{12}=\Sigma_{21}=\frac{pq(q^2+q-1)}{(1+q)^2}.
\]
The determinant formula follows by elementary expansion. The unique zero of \(q^2+q-1\) in \((0,1)\) is \(q_\star\); its sign establishes the claimed transition and Gaussian independence at the zero.

**4. Covariance asymptotics.** The pair \((X_n,B_n)\) is a finite-state Markov chain with a common one-step reset: each new success sets the state to \((1,1)\), independently of the past, with probability \(p\). It is therefore uniformly geometrically mixing. Both increment coordinates in step 1 are bounded functions of consecutive chain states. Their centered lag covariances decrease geometrically, and the nonstationary-start errors are geometrically summable. Summing these covariances over \(n\) steps proves \(\operatorname{Cov}(H_n,L_n)=n\Sigma_{12}+O(1)\), and the analogous diagonal bounds. The same asymptotic constants follow from the renewal computation in step 3.

## Verification

The accompanying standalone `verify.py` uses exact rational path enumeration and an independent finite-state moment recursion for the actual finite trees. It checks height and leaves pathwise, matches six exact moments across 50 combinations of horizon and parameter, independently reconstructs the renewal reward covariance through truncated geometric sums, and checks finite-horizon covariance convergence and the sign boundary. Execute with `python3 verify.py`; no external packages are required. The proof of the infinite CLT and the asymptotic covariance bounds is analytic, not inferred from enumeration.

## Relationship to prior work

Tang, Wang and Wu (2026, arXiv:2607.02916, first public date 2026-07-03) define this Bernoulli two-lag tree and study its one-ended structure, trunk/branches, and collision properties of independent random walks. The inspected full publicly readable arXiv text, including its introduction, Theorems 1.1–1.2, Sections 2–3, and references, does not give a joint limit for height and leaf count or their covariance sign. Generic finite-state Markov additive and renewal-reward central limit theorems supply the probabilistic machinery, but do not themselves identify the exact tree observables, the covariance formula, or the sign-change threshold without a model-specific reduction and calculation. Related height/leaf results for uniformly attached and other recursively grown trees use distinct attachment laws and are not statements about this two-lag law.

## Limitations

There is no claim of a convergence rate, a joint local limit theorem, a limiting law at parameters tending to \(0\) or \(1\), or corresponding results for longer-memory attachment rules. The independent scientific and historical-priority audit has not been performed. More general published finite-state reward identities may implicitly subsume parts of the formula; the novelty claim concerns the explicit tree-specific covariance transition rather than the renewal CLT methodology.

## References

1. J.-s. Tang, F. Wang and X.-Y. Wu, *Infinite collisions of simple random walks on random recursive trees generated by Bernoulli sequences*, arXiv:2607.02916 (initial public posting 2026-07-03), https://arxiv.org/abs/2607.02916.
2. K. Leckey and R. Neininger, *Asymptotic Analysis of Hoppe Trees*, 2013, Journal of Applied Probability 50, 228–238, https://www.jstor.org/stable/43283456 (different weighted attachment model; background comparison).
3. *Distribution of tree parameters by martingale approach*, Combinatorics, Probability and Computing, https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/distribution-of-tree-parameters-by-martingale-approach/32DFE2BAD7DFC3309F3FAD131FEFC451 (background on Gaussian tree parameter statistics in other tree laws).
