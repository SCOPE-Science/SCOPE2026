# Exact terminal jamming laws for two-species adsorption on complete multipartite graphs

## Finding

For the irreversible, two-species antagonistic adsorption process with repeated Poisson attempts, the entire terminal occupancy law on **every finite complete multipartite graph** is an explicit finite sum supported only on the total vertex count and the individual part sizes. This applies for every positive part-size vector and every strictly interior species probability. In the unbiased large-graph limit, the normalized occupied fraction has an explicit, generally non-degenerate mixture law; in particular, equal-sized parts exhibit macroscopic non-self-averaging. On a balanced two-part graph, the full-coverage weight has the sharper finite-size expansion \(1/2+3/(8n)+O(n^{-2})\).

Let \(G=K_{n_1,\ldots,n_r}\), where \(r\ge2\), each \(n_i\ge1\), and \(N=\sum_{i=1}^r n_i\). Fix \(0<p<1\), and put \(q=1-p\). For each part \(i\), write \(a=n_i\), \(b=N-n_i\), and define

\[
F_i^{(A)}=\sum_{j=0}^{a-1}\binom{a-1}{j}p^{a-1-j}q^j\frac{bp}{bp+j},\qquad
F_i^{(B)}=\sum_{j=0}^{a-1}\binom{a-1}{j}q^{a-1-j}p^j\frac{bq}{bq+j}.
\]

Let \(Z\) be the number of occupied vertices in the jammed state. Define

\[
w_i=\frac{n_i}{N}\left[p(1-F_i^{(A)})+q(1-F_i^{(B)})\right],\qquad
w_*=1-\sum_{i=1}^r w_i.
\]

Then the **exact law**, including collisions between equal part sizes, is

\[
\boxed{\mathcal L(Z)=w_*\delta_N+\sum_{i=1}^r w_i\delta_{n_i}.}
\]

The event with weight \(w_i\) is specifically the outcome in which exactly the vertices of part \(i\) eventually become occupied; the event with weight \(w_*\) is full coverage of all parts by a single species. No other final occupancy pattern is possible.

For a fixed \(r\), suppose \(n_i/N\to\alpha_i\in(0,1)\), where \(\sum_i\alpha_i=1\), as \(N\to\infty\). For fixed \(p\in(0,1)\), put

\[
\omega_i=\alpha_i^2pq\left[
\frac{1}{(1-\alpha_i)p+\alpha_i q}
+\frac{1}{(1-\alpha_i)q+\alpha_i p}
\right].
\]

Then

\[
\boxed{\frac{Z}{N}\ \Longrightarrow
\left(1-\sum_{i=1}^r\omega_i\right)\delta_1
+\sum_{i=1}^r\omega_i\delta_{\alpha_i}.}
\]

For equal species rates, \(p=q=1/2\), this simplifies to \(\omega_i=\alpha_i^2\). When all \(r\) parts have equal size, the limiting law is

\[
\boxed{\frac{Z}{N}\Longrightarrow
\left(1-\frac1r\right)\delta_1+\frac1r\delta_{1/r}.}
\]

In particular, the limiting occupied fraction has variance \((r-1)^3/r^4>0\), so coverage does **not** obey a law of large numbers toward a deterministic fraction in this dense-graph family.

For the special case \(G=K_{n,n}\) and \(p=q=1/2\), put

\[
F_n=2^{-(n-1)}\sum_{j=0}^{n-1}\binom{n-1}{j}\frac{n}{n+2j}.
\]

Then \(\Pr(Z=2n)=F_n\), \(\Pr(Z=n)=1-F_n\), and

\[
\boxed{F_n=\frac12+\frac{3}{8n}+O(n^{-2})}\qquad(n\to\infty).
\]

For every finite \(n\ge1\), \(F_n>1/2\); at \(n=2\), the exact probability is \(3/4\).

## Assumptions and scope

Every vertex has an independent rate-one Poisson clock. At a ring, an \(A\) particle is proposed with probability \(p\), or a \(B\) particle with probability \(q\), independently of everything else. The proposal succeeds if its vertex is vacant and has **no occupied neighbour of the opposite species**; if it fails, that vertex remains available for later attempts. Successful occupation is irreversible. The initial configuration is empty. A terminal, or jammed, configuration has no vacant vertex at which either species can be successfully placed, and \(Z\) counts occupied vertices, not permanently blocked vacant ones. This is the repeated-attempt process, not a model that gives each vertex one permanent preassigned species or only one attempt.

The graph is simple, undirected and complete multipartite, so two vertices are adjacent exactly when they lie in different parts. Every part is nonempty and \(r\ge2\). The finite theorem permits unequal part sizes and arbitrary constant \(0<p<1\). At \(p=0\) or \(p=1\), only one species arrives and \(Z=N\) almost surely; those endpoints follow separately, without division by zero. The limiting theorem fixes \(r\) and keeps all limiting part proportions positive.

## Proof

**1. Classification after the first two decisive successful adsorptions.** The first accepted proposal occurs at a uniformly selected vertex, with species \(A\) with probability \(p\) and \(B\) with probability \(q\). Suppose it is an \(A\) in part \(i\). Subsequent accepted \(A\) particles in that same part do not resolve the final outcome. If a \(B\) is successfully placed at another vertex of part \(i\) before any \(A\) is successfully placed outside \(i\), then every vertex outside \(i\) has both an \(A\)- and a \(B\)-occupied neighbour. Such vertices are permanently blocked, while every remaining vertex in part \(i\) can eventually accept a particle of either type. Thus \(Z=n_i\).

Conversely, if an \(A\) is successfully placed outside \(i\) before a \(B\) is accepted inside \(i\), then at least two different parts contain an \(A\). Every still-vacant vertex is adjacent to an occupied \(A\) in a different part, and can never accept \(B\). Every vacancy can eventually accept \(A\), hence \(Z=N\). The same dichotomy holds after an initial \(B\), with the species interchanged. The decisive event occurs almost surely, since there are finitely many vertices and the remaining admissible Poisson rates are strictly positive. This proves that no other terminal occupation pattern can occur.

**2. Exact conditional probability.** Condition on the first accepted particle being an \(A\) at a particular vertex of part \(i\). The time \(\tau\) of the first proposed \(A\) at any vertex outside \(i\), measured after that first particle, is exponential with rate \(bp\), where \(b=N-n_i\). This clock is independent of all proposal streams at the \(a-1\) other vertices inside \(i\).

For any one such inside vertex, the first subsequent proposal has an exponential waiting time of rate one and has species \(B\) with probability \(q\). The probability that it accepts \(B\) before time \(t\) is \(q(1-e^{-t})\), provided no decisive event has yet occurred. Therefore, the probability that none of the \(a-1\) inside vertices produces a \(B\) before the outside clock rings at \(t\) equals \((p+qe^{-t})^{a-1}\). Averaging over \(\tau\) gives

\[
\Pr(Z=N\mid\text{first }A\text{ in part }i)
=bp\int_0^\infty e^{-bpt}(p+qe^{-t})^{a-1}\,dt.
\]

Expanding the finite binomial and integrating each exponential yields exactly \(F_i^{(A)}\). Starting instead with \(B\) gives \(F_i^{(B)}\). The first accepted vertex belongs to part \(i\) with probability \(n_i/N\), independently of the initial species. Consequently the probability of the part-\(i\)-only outcome is \(w_i\), and all remaining mass \(w_*\) belongs to full coverage. This proves the finite theorem. Equal-valued part sizes may simply be aggregated, as in the displayed probability measure.

**3. Thermodynamic mixture.** Conditioned on an initial \(A\) in part \(i\), let \(\tau_N\sim\operatorname{Exp}((N-n_i)p)\) and put \(S_N=N\tau_N\). As \(n_i/N\to\alpha_i\), \(S_N\) converges to an exponential with rate \((1-\alpha_i)p\). For fixed \(s\ge0\),

\[
(p+qe^{-s/N})^{n_i-1}\longrightarrow e^{-\alpha_i qs}.
\]

The factors lie in \([0,1]\), so bounded convergence (using a common exponential quantile coupling) yields

\[
F_i^{(A)}\longrightarrow
\frac{(1-\alpha_i)p}{(1-\alpha_i)p+\alpha_i q}.
\]

Likewise,

\[
F_i^{(B)}\longrightarrow
\frac{(1-\alpha_i)q}{(1-\alpha_i)q+\alpha_i p}.
\]

Substitution in the exact weights gives \(w_i\to\omega_i\) and \(w_*\to1-\sum_i\omega_i\). Since the finite law has at most \(r+1\) support points and these converge to \(\alpha_i\) and \(1\), weak convergence follows. At \(p=q=1/2\), both conditional full-coverage probabilities tend to \(1-\alpha_i\); therefore \(\omega_i=\alpha_i^2\). Equal proportions \(\alpha_i=1/r\) give the stated two-point mixture and variance \((r-1)^3/r^4\).

**4. Sharp balanced two-part correction.** On \(K_{n,n}\), symmetry makes the conditional full-coverage probability equal to \(F_n\) regardless of the first part and first species. The integral in step 2 becomes

\[
\frac n2\int_0^\infty e^{-nt/2}
\left(\frac{1+e^{-t}}2\right)^{n-1}\,dt,
\]

and finite binomial expansion gives the stated sum. Equivalently, if \(J\sim\operatorname{Bin}(n-1,1/2)\), then \(F_n=\mathbb E[n/(n+2J)]\). For \(n\ge2\), strict Jensen convexity yields

\[
F_n\ge\frac{n}{n+2\mathbb EJ}
=\frac n{2n-1}>\frac12.
\]

The \(n=1\) case is \(F_1=1\). For a quantitative expansion set \(Y=2J-(n-1)\) and \(d=2n-1\). Then \(\mathbb EY=\mathbb EY^3=0\), \(\mathbb EY^2=n-1\), \(\mathbb EY^4=3(n-1)^2-2(n-1)\), and \(d+Y\ge n\). The exact identity

\[
\frac1{d+Y}=\frac1d-\frac Y{d^2}+\frac{Y^2}{d^3}
-\frac{Y^3}{d^4}+\frac{Y^4}{d^4(d+Y)}
\]

therefore implies

\[
F_n=\frac n{2n-1}+\frac{n(n-1)}{(2n-1)^3}+O(n^{-2})
=\frac12+\frac{3}{8n}+O(n^{-2}).
\]

Indeed the remainder is bounded in absolute value by \(\mathbb E[Y^4]/d^4=O(n^{-2})\). This proves the asymptotic expansion with a justified error bound.

## Verification

The accompanying standard-library-only `check_jamming.py` computes the terminal occupancy distribution by **independent exact-rational Markov recursion on successful species-specific vertex arrivals**, not by reusing the integral proof. It compares that distribution to the finite formula for every unordered positive part-size partition of totals \(2\) through \(8\), across five rational species probabilities \(1/4,1/3,1/2,2/3,3/4\). It also verifies the binomial identity for \(K_{n,n}\) for \(1\le n\le150\). Reproduction: `python3 check_jamming.py`. A successful run reports 290 exact Markov-chain comparisons and 1,169 assertions. These finite checks support the algebra and boundary conditions; the claims for every graph order and the asymptotics are proved above independently of computation.

## Relationship to prior work

Martins, Dickman and Ziff introduced and studied the same **repeated-attempt two-species exclusion dynamics** on one- and two-dimensional lattices; their 2022 open preprint (arXiv:2211.04622) analyzes jamming coverage and percolation, including exact low-concentration coefficients. The present result concerns all finite complete multipartite graphs with generally growing degree, a different geometry and a complete terminal probability law. It does not claim their process or their one-dimensional results as new.

Dhara, van Leeuwaarden and Mukherjee (2016) analyze threshold, multi-frequency and greedy frequency-allocation RSA variants on sparse Erdős–Rényi random graphs; these are not the repeated two-species antagonistic Poisson model with the complete-multipartite geometry. Krivelevich, Mészáros, Michaeli and Shikhelman (2023 prepublication; 2024 journal) study the one-species, single-pass random greedy maximal independent set, which likewise has a different success rule. The equilibrium Widom–Rowlinson partition function does not by itself specify a history-dependent jammed-state distribution. Classical stochastic adsorption and exponential-race techniques supply background but, in the inspected sources, did not yield the displayed multi-partite terminal weights or the \(3/(8n)\) correction. Definitive priority requires a broader independent literature review.

## Limitations

The exact law assumes independent per-site Poisson attempt streams with replacement, two antagonistic species, no desorption, complete multipartite adjacency and a fixed species probability. It does not apply to a one-shot random vertex order with permanently fixed colors, to finite-duration adsorption, or to general dense graphs with missing cross-edges. The weak limit requires a fixed number of parts and positive limiting proportions. The sharp \(3/(8n)\) coefficient is derived only for the balanced, equal-species-rate bipartite case. There is no independent mathematical audit or certified historical uniqueness.

## References

1. P. H. L. Martins, R. Dickman and R. M. Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions*, first public preprint 2022-11-09, https://arxiv.org/abs/2211.04622 (journal DOI: https://doi.org/10.1103/PhysRevE.107.024104).
2. S. Dhara, J. S. H. van Leeuwaarden and D. Mukherjee, *Generalized Random Sequential Adsorption on Erdős–Rényi Random Graphs*, 2016, https://doi.org/10.1007/s10955-016-1583-z.
3. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, https://doi.org/10.1002/rsa.21200.
4. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401, https://doi.org/10.1137/0402034.
