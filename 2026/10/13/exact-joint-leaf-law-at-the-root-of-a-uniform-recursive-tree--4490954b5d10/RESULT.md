# Exact joint leaf law at the root of a uniform recursive tree

## Finding
For a uniform random recursive tree on \(n\ge2\) vertices, let \(Q_n\) count children of the root that are themselves leaves and let \(L_n\) count all leaves. Write \(A_m(z)=\sum_{d=0}^{m-1}\langle m,d\rangle z^d\) for the ordinary Eulerian descent polynomial, with \(A_0(z)=1\). Then, for all complex \(u,z\),
\[
(n-1)!\,\mathbb E[u^{Q_n}z^{L_n}]
=\sum_{k=0}^{n-2}\binom{n-1}{k}(u-1)^kz^{k+1}A_{n-k-1}(z)
 +(u-1)^{n-1}z^{n-1}.
\]
In particular, for every \(n\ge3\),
\[
\operatorname{Cov}(Q_n,L_n)=\frac12,
\qquad \operatorname{Corr}(Q_n,L_n)=\sqrt{\frac3n}.
\]
Moreover,
\[
\left(Q_n,\frac{L_n-n/2}{\sqrt{n/12}}\right)
\xrightarrow{\mathrm d}(P,Z),
\qquad P\sim\operatorname{Poisson}(1),\quad Z\sim N(0,1),
\]
where \(P\) and \(Z\) are **independent**. The positive finite-size covariance and asymptotic independence are compatible because the global leaf fluctuations have order \(\sqrt n\).

## Assumptions and scope
A recursive tree has labels \(1,\ldots,n\), root \(1\), and for each \(j=2,\ldots,n\) an independently sampled parent uniformly chosen among \(1,\ldots,j-1\). Thus every one of the \((n-1)!\) increasing labeled rooted trees has equal probability. A leaf is a vertex with no children; a root leaf-child is a child of vertex \(1\) having no children. The root is not a leaf when \(n\ge2\). The Eulerian coefficient \(\langle m,d\rangle\) counts permutations of size \(m\) with \(d\) descents; for \(m=0\) use the single empty permutation. For nonnegative integers \(k\), \((a)_k=a(a-1)\cdots(a-k+1)\) is the falling factorial, with \((a)_0=1\). At \(n=2\) both leaf statistics equal one deterministically; the displayed covariance and correlation identities only assert \(n\ge3\).

## Proof
**1. The deletion property.** Fix any subset \(S\subseteq\{2,\ldots,n\}\) with \(|S|=k\). The event that every vertex in \(S\) is a leaf-child of the root forces the parent of every vertex in \(S\) to be \(1\), and forces all other vertices to avoid attaching to those in \(S\). Deleting the \(k\) specified leaves and increasing-relabeling the remaining vertices produces a recursive tree on \(n-k\) vertices. Conversely every recursive tree on those remaining labels has exactly one reconstruction that makes \(S\) a set of root leaf-children. Therefore the event has probability
\[
\frac{(n-k-1)!}{(n-1)!}=\frac1{(n-1)_k},
\]
and the remaining tree, conditional on this event, is exactly a uniformly random recursive tree of order \(n-k\). If \(0\le k\le n-2\), the remaining root is nonleaf, and reinserting the removed leaves increases total leaf count by precisely \(k\). If \(k=n-1\), the original tree must be the root-centered star with exactly \(n-1\) leaves; the one-vertex root-only tree is treated separately.

**2. Joint factorial transform.** Summing ordered choices of \(k\) distinct root leaf-children and applying the deletion property gives
\[
\mathbb E[(Q_n)_kz^{L_n}]
=\begin{cases}
 z^k\mathbb E[z^{L_{n-k}}],&0\le k\le n-2,\\
 z^{n-1},&k=n-1.
\end{cases}
\]
The identity is also valid at \(k=0\). The usual leaf-growth recurrence states that adding a new vertex increases leaf count exactly when its parent was not a leaf. This gives the Eulerian recursion for the univariate law, hence, for \(m\ge2\),
\[
\mathbb E[z^{L_m}]=\frac{zA_{m-1}(z)}{(m-1)!}.
\]
Expand \(u^{Q_n}=\sum_{k=0}^{n-1}(u-1)^k(Q_n)_k/k!\) and substitute the factorial-transform identities. Multiplication by \((n-1)!\) yields the stated exact bivariate polynomial, including its final star term.

**3. Finite covariance and correlation.** At \(z=1\), the factorial identities imply \(\mathbb E[(Q_n)_k]=1\) for every \(0\le k\le n-1\). Thus \(\mathbb EQ_n=1\) for \(n\ge2\), and \(\operatorname{Var}(Q_n)=1\) for \(n\ge3\). Differentiating the identity at \(k=1\) and \(z=1\), for \(n\ge3\), gives
\[
\mathbb E[Q_nL_n]=\mathbb E[L_{n-1}]+1=\frac{n+1}{2}.
\]
The Eulerian leaf law gives \(\mathbb EL_n=n/2\) and \(\operatorname{Var}(L_n)=n/12\) for \(n\ge3\). For completeness, write the Eulerian descent count as a sum of \(n-2\) adjacent comparison indicators of independent uniform observations. Each indicator has variance \(1/4\), its covariance with the adjacent indicator is \(-1/12\), and nonadjacent indicators are independent. Hence the asserted mean and variance follow. Subtracting \(\mathbb EQ_n\,\mathbb EL_n\) gives covariance \(1/2\), and dividing by the marginal standard deviations gives correlation \(\sqrt{3/n}\).

**4. Asymptotic independence.** Since the Eulerian descent indicators are bounded and 1-dependent, their standard central limit theorem gives \((L_m-m/2)/\sqrt{m/12}\xrightarrow{\mathrm d}N(0,1)\). In the bivariate factorial expansion, set \(z=\exp(it/\sqrt{n/12})\) and multiply by \(\exp(-it(n/2)/\sqrt{n/12})\). For each fixed \(k\), the factorial-transform identity and the univariate CLT show that the associated normalized term converges to \(e^{-t^2/2}(u-1)^k/k!\). For real \(0\le u\le1\), the absolute value of each term is bounded by \(1/k!\); the exceptional star term is bounded by \(1/(n-1)!\). Dominated convergence for the convergent exponential series therefore yields
\[
\lim_{n\to\infty}\mathbb E\left[u^{Q_n}\exp\!\left(it\frac{L_n-n/2}{\sqrt{n/12}}\right)\right]
=e^{u-1}e^{-t^2/2}.
\]
Uniqueness of joint probability-generating/characteristic transforms identifies the independent Poisson and Gaussian limit.

## Verification
Run `python3 verify.py` with Python 3 standard library only. The script independently enumerates all recursive-tree parent choices for \(2\le n\le9\), constructs the actual pair \((Q_n,L_n)\), computes the stated bivariate polynomial via Eulerian-number recursion, and compares every integer coefficient. It also checks all admissible factorial-moment identities for those orders and, for \(3\le n\le9\), checks the covariance and marginal leaf variance using exact rational arithmetic. The exhaustive sample contains \(46{,}233\) recursive trees across the eight orders. Passing finite checks corroborates the formula but does not prove its universal or limiting statements; those rely on the deletion and central-limit arguments above.

## Relationship to prior work
Devroye and Janson studied protected vertices and the Poisson thinning of root children that remain leaves in a continuous-time Yule recursive tree; their Section 7 treats protected-root probabilities and the number of root leaf-children at a fixed time, not the joint law with the **total** leaf count in a size-conditioned recursive tree. Mahmoud and Ward studied the global count of protected vertices through splitting and recurrences; protected-vertex count is not \(L_n\), and their moments are not the displayed two-variable polynomial. Janson's earlier degree-distribution work provides global outdegree marginals and limiting degree profiles, rather than this root-local/global-leaf joint law. The known Eulerian global-leaf law and Poisson fixed-point-type marginal for \(Q_n\) are inputs and are not individually claimed as new. The contribution here is the exact **coupled** polynomial and the finite covariance/asymptotic-independence consequences.

## Limitations
The result applies to **uniform recursive trees**, not plane-oriented increasing trees, preferential-attachment trees, or other weighted growth rules. It is an exact joint-law theorem for the specific statistics \(Q_n\) and \(L_n\), not a universal independence theorem for all root-local functionals. The finite covariance does not contradict asymptotic independence after scaling. An older comprehensive increasing-tree enumeration might encode an equivalent bivariate specialization; an exhaustive historical-priority determination is not claimed. The proof itself is self-contained apart from the standard Eulerian descent central limit theorem, which also follows from elementary bounded 1-dependent sums.

## References
1. L. Devroye and S. Janson, *Protected nodes and fringe subtrees in some random trees*, arXiv:1310.0665v1 (first publicly submitted 2 October 2013), https://arxiv.org/abs/1310.0665 . In particular, Section 7.
2. H. M. Mahmoud and M. D. Ward, *Asymptotic properties of protected nodes in random recursive trees*, Journal of Applied Probability 52 (2015), 290–297, https://the-examples-book.com/personal/mdw/_attachments/paper029.pdf . Sections 2–3.
3. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26 (2005), 69–83, https://doi.org/10.1002/rsa.20046 .
