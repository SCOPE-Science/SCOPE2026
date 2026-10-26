# Exact beta-binomial degrees and all-size uniformity in recursively grown cographs

## Finding
Fix a join probability \(q\in(0,1)\), with \(p=1-q\). In the recursive true/false-twin cograph process defined below, let \(D_n\) be the degree of a uniformly chosen vertex and \(R_n\) the degree of the original vertex after \(n\) vertices have been grown. For every \(n\ge1\) and every integer \(0\le k\le n-1\),
\[
\Pr(D_n=k)=\binom{n-1}{k}\frac{(2q)_k(2p)_{n-1-k}}{(2)_{n-1}},\qquad
\Pr(R_n=k)=\binom{n-1}{k}\frac{(q)_k(p)_{n-1-k}}{(1)_{n-1}}.
\]
Here \((a)_j=a(a+1)\cdots(a+j-1)\) is the rising factorial, with \((a)_0=1\). Equivalently, these laws are beta-binomial with parameters \((n-1;2q,2p)\) and \((n-1;q,p)\), respectively.

At the symmetric parameter \(q=p=1/2\), the typical-vertex degree is exactly uniform on \(\{0,1,\ldots,n-1\}\), at every finite \(n\):
\[
\Pr(D_n=k)=\frac1n,\qquad \mathbb E N_n(k)=1.
\]
The second identity concerns the **expected** number \(N_n(k)\) of vertices of degree \(k\), not the number in any single realized graph.

For general \(q\),
\[
\mathbb E D_n=\mathbb E R_n=(n-1)q,\quad
\operatorname{Var}(D_n)=\frac{qp(n^2-1)}3,\quad
\operatorname{Var}(R_n)=\frac{qp n(n-1)}2.
\]
For \(n\ge2\) and \(n\to\infty\),
\[
\frac{D_n}{n-1}\Rightarrow\operatorname{Beta}(2q,2p),\qquad
\frac{R_n}{n-1}\Rightarrow\operatorname{Beta}(q,p).
\]

## Assumptions and scope
Begin with a single isolated labeled vertex. At each transition from \(n\) to \(n+1\) vertices, choose one of the existing \(n\) vertices uniformly; add one vertex with precisely the chosen parent's neighbors; then independently add the edge between parent and newcomer with probability \(q\). Thus both true and false twins are allowed. Choices at different steps are independent conditional on their past. The random choice of vertex defining \(D_n\) is uniform conditional on the realized graph and independent of the graph-generation randomness. Degrees are ordinary simple-graph degrees. The parameter \(q\) is constant across times; the boundary values \(q\in\{0,1\}\) are excluded from the stated beta-law formulation but follow as degenerate limits.

## Proof
Condition on the current graph, and fix an existing vertex of degree \(k\). The newcomer is adjacent to this vertex if its chosen parent is one of that vertex's \(k\) neighbors, or if the parent is the vertex itself and the extra parent-child edge is added. These disjoint cases give
\[
\Pr(\text{the fixed vertex's degree increases}\mid G_n)=\frac{k+q}{n}.
\]
For the original vertex, therefore, if \(r_n(k)=\Pr(R_n=k)\), with terms outside \(0,\ldots,n-1\) interpreted as zero,
\[
r_{n+1}(k)=\left(1-\frac{k+q}{n}\right)r_n(k)
+\frac{k-1+q}{n}r_n(k-1),\qquad r_1(0)=1.
\]
This is the Pólya-urn count transition with initial positive weights \(q\) and \(p\), whose mass function is the claimed beta-binomial law for \(R_n\).

For a uniform vertex, let \(N_n(k)\) be the number of *existing* degree-\(k\) vertices. The preceding conditional increment rule implies that existing vertices contribute an expected
\[
\left(1-\frac{k+q}{n}\right)N_n(k)
+\frac{k-1+q}{n}N_n(k-1)
\]
vertices of degree \(k\) at the next step. The new vertex has degree equal to its uniformly chosen parent's previous degree, plus an independent Bernoulli\((q)\) variable. Its conditional probability of degree \(k\) is therefore
\[
\frac{p N_n(k)+qN_n(k-1)}n.
\]
Adding these quantities and taking expectations gives the exact count recurrence
\[
\mathbb E N_{n+1}(k)=\frac{n+1-k-2q}{n}\,\mathbb E N_n(k)
+\frac{k-1+2q}{n}\,\mathbb E N_n(k-1).
\]
Because \(h_n(k)=\mathbb E N_n(k)/n=\Pr(D_n=k)\), division by \(n+1\) yields
\[
h_{n+1}(k)=\frac{n+1-k-2q}{n+1}h_n(k)
+\frac{k-1+2q}{n+1}h_n(k-1),\qquad h_1(0)=1.
\]
For arbitrary positive \(a,b\), define
\[
B_m(k;a,b)=\binom mk\frac{(a)_k(b)_{m-k}}{(a+b)_m}.
\]
Direct cancellation of neighboring rising factorials proves
\[
B_{m+1}(k;a,b)=\frac{m-k+b}{m+a+b}B_m(k;a,b)
+\frac{k-1+a}{m+a+b}B_m(k-1;a,b).
\]
Putting \(m=n-1\), first with \((a,b)=(q,p)\) and then with \((a,b)=(2q,2p)\), matches the two recurrences and initial conditions. This proves both mass functions by induction, including every boundary degree.

At \(q=p=1/2\), the two parameters of the uniform-vertex beta-binomial law are both \(1\), and \(\binom{n-1}{k}(1)_k(1)_{n-1-k}/(2)_{n-1}=1/n\). The mean and variance identities follow from the standard beta-binomial moments, or directly from their beta-mixture representation. For a positive beta-binomial law, draw \(X\sim\operatorname{Beta}(a,b)\), then draw \(Y_m\mid X\sim\operatorname{Bin}(m,X)\). Its mass function is \(B_m(k;a,b)\); conditional binomial concentration shows \(Y_m/m\Rightarrow X\), proving the two weak limits. For \(n\ge3\), the original-vertex variance exceeds the typical-vertex variance by \(qp(n-1)(n-2)/6\).

## Verification
Run `python verify_degrees.py` using Python 3 and its standard library. The checker enumerates every reachable labeled graph state for sample sizes \(1\) through \(6\) and five rational join probabilities \(1/7,1/3,1/2,3/5,6/7\), using exact rational state probabilities. For each size it independently evaluates the sampled-vertex and original-vertex degree histograms. It also verifies the two distribution recurrences symbolically over exact fractions through size \(45\). The supplied program completed successfully and reported 10,821 assertions. The all-size theorem follows from the mathematical induction above, not from bounded enumeration.

## Relationship to prior work
Féray and Rivera-Lopez, *The permuton limit of random recursive separable permutations* (first public June 7, 2023, arXiv:2306.04278), define precisely this recursive cograph growth process, derive its graphon limit, and give an exact general finite labeled-graph probability formula. **Neither the underlying model nor that comprehensive graph probability formula is claimed as new.** The additional result here is a compact, closed marginal distribution for the degree of a uniform vertex and the founder, with a non-obvious doubling of beta parameters, finite-size all-degree uniformity at symmetry, and the contrasting beta weak limits. These statements are in principle summable from the earlier all-graph law, but that general law does not present the closed degree distributions or their paired age comparison.

Bassino and collaborators, *Random cographs: Brownian graphon limit and asymptotic degree distribution* (arXiv:1907.08517), prove an asymptotically uniform degree law for **uniform random labeled or unlabeled cographs**. That is a different distribution on cographs from this recursively generated model, and it gives neither exact finite-size uniformity for the latter nor the beta shape for biased twin joining. The agreement of uniform limits at the symmetric parameter is therefore a comparison of models, not an implication of the earlier theorem.

## Limitations
These are annealed one-vertex degree laws; they do not assert that every realized graph has all possible degrees or that its empirical degree distribution converges to a deterministic beta distribution. They do not establish joint degree distributions or a limit for the empirical measure. Exact labeled-graph probabilities were known previously, so originality concerns the collapsed marginal identities, not the existence of a finite expression in principle. Other broader duplication-model identities could imply the marginal results and remain a historical-priority risk. An independent mathematical audit has not been performed.

## References
1. V. Féray and K. Rivera-Lopez, *The permuton limit of random recursive separable permutations*, arXiv:2306.04278, initial public version June 7, 2023. https://arxiv.org/abs/2306.04278
2. F. Bassino, M. Bouvel, V. Féray, L. Gerin, M. Maazoun, and A. Pierrot, *Random cographs: Brownian graphon limit and asymptotic degree distribution*, arXiv:1907.08517, initial public version July 19, 2019. https://arxiv.org/abs/1907.08517
