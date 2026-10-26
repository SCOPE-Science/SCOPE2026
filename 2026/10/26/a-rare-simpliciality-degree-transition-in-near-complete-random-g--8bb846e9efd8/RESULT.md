# A rare-simpliciality degree transition in near-complete random graphs

## Finding
Fix \(c>0\). For each sufficiently large integer \(n\), let \(G_n\sim G(n,p_n)\) on vertex set \(\{1,\ldots,n\}\), where \(p_n=1-c\log n/n\), and distinguish vertex \(v=1\). Let \(S_n\) be the event that the open neighborhood of \(v\) induces a clique (that is, \(v\) is simplicial), and let \(D_n=\deg_{G_n}(v)\). The event \(S_n\) has positive probability. Set
\[
F_c(a)=1-a+\frac c2a^2,\qquad a\in[0,1],\qquad
 a_c=\min\{1,1/c\},\qquad
 \Phi(c)=\begin{cases}c/2,&0<c\le1,\\1-1/(2c),&c>1.\end{cases}
\]
Then the following assertions hold jointly.

1. The exact, finite-size conditional mass is
\[
\Pr(D_n=d\mid S_n)=\frac{\binom{n-1}{d}\,p_n^{d(d+1)/2}(1-p_n)^{n-1-d}}
{\sum_{j=0}^{n-1}\binom{n-1}{j}\,p_n^{j(j+1)/2}(1-p_n)^{n-1-j}},\quad 0\le d\le n-1.
\]
2. The rare-event exponent is
\[
\lim_{n\to\infty}\frac{\log\Pr(S_n)}{n\log n}=-\Phi(c).
\]
3. Conditionally on \(S_n\), the laws of \(D_n/n\) obey a full large-deviation principle on \([0,1]\) with speed \(n\log n\) and good rate function \(I_c(a)=F_c(a)-\Phi(c)\). In particular, for every \(\varepsilon>0\), there exists \(\kappa(c,\varepsilon)>0\) such that, for all large \(n\),
\[
\Pr\bigl(|D_n/n-a_c|\ge\varepsilon\mid S_n\bigr)
\le n^{-\kappa(c,\varepsilon)n}.
\]
Thus \(D_n/n\to a_c\) conditionally in probability. The limiting tagged degree stays at \(1\) for \(c\le1\), but falls to \(1/c\) for \(c>1\). The rare-event exponent is continuously differentiable but not twice differentiable at \(c=1\).
4. All other vertex degrees remain asymptotically full: for every \(\varepsilon>0\),
\[
\Pr\left(\min_{u\ne v}\frac{\deg_{G_n}(u)}n<1-\varepsilon\,\middle|\,S_n\right)\longrightarrow0.
\]
Consequently the macroscopic degree deficit for \(c>1\) is localized at the distinguished vertex.

## Assumptions and scope
All graphs are simple and undirected, with independent edges; simplicial means the neighbors, excluding the distinguished vertex itself, form a complete induced subgraph. A neighborhood of size zero or one is a clique. The constant \(c\) is strictly positive and independent of \(n\); the assertions concern integers sufficiently large that \(0<p_n<1\). In the large-deviation assertion, for every closed set \(C\subseteq[0,1]\) and every relatively open set \(O\subseteq[0,1]\),
\[
\limsup_{n\to\infty}\frac1{n\log n}\log\Pr(D_n/n\in C\mid S_n)\le-\inf_{a\in C}I_c(a),
\]
\[
\liminf_{n\to\infty}\frac1{n\log n}\log\Pr(D_n/n\in O\mid S_n)\ge-\inf_{a\in O}I_c(a).
\]
The logarithm of zero is \(-\infty\), and the infimum over an empty set is \(+\infty\).

## Proof
**Exact weights.** Set \(q_n=1-p_n\). A specified collection of exactly \(d\) neighbors of \(v\) has incident-edge probability \(p_n^d q_n^{n-1-d}\). Conditional on that collection, the \(\binom d2\) edges internal to it remain independent with success probability \(p_n\). Hence the joint mass of simpliciality and root degree \(d\) is exactly
\[
w_{n,d}=\Pr(S_n,D_n=d)=\binom{n-1}{d}p_n^{d+\binom d2}q_n^{n-1-d}.
\]
Summation gives \(Z_n=\Pr(S_n)=\sum_{d=0}^{n-1}w_{n,d}\) and the stated conditional formula; \(w_{n,0}=q_n^{n-1}>0\).

**Uniform log-weight limit.** Write \(a=d/n\). Uniformly over all integers \(0\le d\le n-1\),
\[
\frac{\log w_{n,d}}{n\log n}=-F_c(d/n)+o(1).
\tag{1}
\]
Indeed \(0\le\log\binom{n-1}d\le n\log2\), while
\[
\log p_n=-c\frac{\log n}{n}+O_c\left(\frac{(\log n)^2}{n^2}\right),\qquad
\log q_n=-\log n+\log(c\log n).
\]
Using \(d(d+1)\le n^2\) and \(0\le n-1-d\le n\), the resulting normalized error is uniformly \(O_c(\log\log n/\log n+1/\log n)\), and (1) follows.

**Minimum and partition function.** The derivative of \(F_c\) is \(ca-1\); strict convexity yields its unique minimizer \(a_c=\min\{1,1/c\}\), with minimum \(\Phi(c)\). Because the summation has exactly \(n\) nonnegative terms, (1) implies
\[
\frac{\log Z_n}{n\log n}\longrightarrow-\Phi(c).
\]
In particular \(I_c\ge0\), with equality only at \(a_c\).

**Full conditional large deviations.** From (1), the normalized log of \(w_{n,d}/Z_n\) converges uniformly on the mesh \(\{0,1/n,\ldots,(n-1)/n\}\) to \(-I_c(d/n)\). For a closed set, bounding the probability by \(n\) times its largest mass and taking convergent maximizing subsequences proves the upper bound. For a relatively open set, choose any \(a\) in it and integers \(d_n\in\{0,\ldots,n-1\}\) satisfying \(d_n/n\to a\) with \(d_n/n\) eventually inside the set (including \(a=0,1\) as boundary cases); the single-term lower bound proves the stated lower inequality. Compactness of \([0,1]\) makes \(I_c\) good. For \(\varepsilon>0\), the minimum of \(I_c\) on \(\{a:|a-a_c|\ge\varepsilon\}\) is strictly positive if that set is nonempty. The uniform approximation permits a slightly smaller positive \(\kappa\), giving the displayed exponential-concentration bound; the empty case is immediate.

**Localization.** Conditional on the precise neighbor set \(A=N(v)\) and on \(S_n\), the edges internal to \(A\) are forced present, and every other edge between vertices distinct from \(v\) remains an independent Bernoulli\((p_n)\) variable. Thus for each \(u\ne v\), its number of non-neighbors among the other \(n-2\) non-root vertices is stochastically bounded by \(B_n\sim\operatorname{Bin}(n-2,q_n)\). At most one additional non-neighbor is \(v\). Uniformly over the neighbor set \(A\), for every fixed \(\varepsilon>0\) and all large \(n\), a union bound gives
\[
\Pr\bigl(\exists u\ne v:\deg(u)<(1-\varepsilon)n\mid S_n\bigr)
\le(n-1)\Pr\bigl(B_n\ge\varepsilon n-2\bigr).
\]
Since \(\mathbb E B_n\le c\log n\), the standard binomial Chernoff estimate \(\Pr(B_n\ge t)\le(e\mathbb E B_n/t)^t\) for \(t\ge\mathbb E B_n\) makes this upper bound tend to zero. Finally, differentiating the explicit two branches of \(\Phi(c)\) proves agreement of first derivatives and the jump of second derivatives at \(c=1\).

## Verification
Run `python3 verify_simplicial.py` beside this file. The standard-library verifier exhaustively evaluates all \(33,866\) graphs on two through six labeled vertices and, for two distinct rational edge probabilities, checks each root-degree joint probability exactly against the weight formula. It also checks the direction of numerical convergence of the normalized exponent and conditional mean across three increasing values of \(n\) for five positive values of \(c\). Its observed output was `VERIFY_OK checks=70; exhaustive_graphs_n2_to_n6=33866; numeric_n=1000,10000,40000`. These finite checks do not prove any asymptotic assertion; the proof above supplies that argument.

## Relationship to prior work
Grimmett and Janson (arXiv:0712.0270, publicly posted 3 December 2007) analyze sparse \(G(n,\lambda/n)\) conditioned on *all* vertex degrees lying in a prescribed set. Their framework motivates conditioned random-graph degree laws but does not apply its stated hypotheses to a near-complete graph conditioned on one vertex's neighborhood forming a clique. Chudnovsky, Scott, Seymour and Spirkl (arXiv:2012.05287) study deterministic simplicial cliques in hereditary graph classes, rather than rare-event conditional degrees in independent-edge random graphs. Hébert-Johnson, Lokshtanov and Vigoda (arXiv:2308.09703) give counting and uniform sampling algorithms for globally chordal graphs; their distribution and objects differ from this single-vertex conditioned \(G(n,p_n)\) law. The large-deviation proof uses a standard discrete Laplace principle; the object-specific energy, marked-degree transition and localization constitute the assertion here.

## Limitations
The theorem assumes a *single distinguished simplicial vertex* and the specific logarithmic near-complete scaling \(1-p_n=c\log n/n\) with fixed \(c\). It does not establish existence probabilities for any simplicial vertex in the unconditioned graph beyond the single-vertex expectation, nor describe a graph conditioned to contain at least one such vertex. The finite computations are not substitutes for the proof. Older or more general conditioning/large-deviation results may implicitly contain this specialization; independent historical-priority review has not been performed.

## References
- G. Grimmett and S. Janson, *Random graphs with forbidden vertex degrees*, arXiv:0712.0270 (first preprint 2007-12-03), especially Sections 1–3. https://arxiv.org/abs/0712.0270
- M. Chudnovsky, A. Scott, P. Seymour and S. Spirkl, *A note on simplicial cliques*, arXiv:2012.05287 (first preprint 2020-12-09), especially Sections 1–2. https://arxiv.org/abs/2012.05287
- Ú. Hébert-Johnson, D. Lokshtanov and E. Vigoda, *Counting and Sampling Labeled Chordal Graphs in Polynomial Time*, arXiv:2308.09703 (first preprint 2023-08-18), especially introductory material and the evaporation-sequence construction. https://arxiv.org/abs/2308.09703
