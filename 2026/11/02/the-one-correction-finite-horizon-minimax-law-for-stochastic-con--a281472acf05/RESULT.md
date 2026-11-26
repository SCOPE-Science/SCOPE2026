# The one-correction finite-horizon minimax law for stochastic consensus on regular bipartite graphs

## Finding

Let \(G\) be a connected simple undirected \(d\)-regular bipartite graph on \(N\ge6\) vertices with \(d\ge2\), and let its combinatorial Laplacian \(L=dI-A\) have gap \(0<\mu=\lambda_2(L)<d\). In each of \(r\ge3\) rounds use a single spatially homogeneous gain \(t_j\in[0,1/d]\), so \(P_j=I-t_jL\) is individually symmetric, doubly stochastic, and entrywise nonnegative. Define
\[
R(t_1,\ldots,t_r)=\left\|P_r\cdots P_1-\frac{\mathbf1\mathbf1^{\mathsf T}}{N}\right\|_2,
\qquad h=\frac{\mu}{2d},\qquad \rho=1-\frac{\mu}{d},\qquad a_r=\rho^{r-1}.
\]
Then the exact minimum over all such schedules is
\[
B_r=\frac{a_r(1-h)}{1+h a_r},
\]
and the unique optimal multiset consists of \(r-1\) gains equal to \(1/d\) and one equal to \((1+B_r)/(2d)\). The correction can be used at any position. This schedule strictly improves on repeating the best single gain \(2/(2d+\mu)\). The horizon-optimized factors satisfy \(\lim_{r\to\infty}B_r^{1/r}=\rho\).

## Assumptions and scope

Every round uses the same unweighted Laplacian; changing spatial weights, adding memory, or allowing nonstochastic intermediate steps is outside the theorem. The norm is the induced Euclidean norm on the complement of constants. The assumption \(\mu<d\) excludes complete bipartite graphs \(K_{d,d}\): their nonzero Laplacian eigenvalues are \(d,2d\), so two admissible rounds can yield exact consensus and destroy long-horizon uniqueness. The asymptotic rate concerns separately optimized horizons, not a single precommitted infinite sequence.

## Proof

**Spectrum and norm.** Bipartiteness gives adjacency eigenvalue pairing \(\theta\leftrightarrow-\theta\); connected regularity makes \(0\) and \(2d\) simple Laplacian eigenvalues. Every other eigenvalue lies in \([\mu,2d-\mu]\). The diagonal entries of \(P_j\) are \(1-dt_j\) and its edge entries are \(t_j\), giving exactly the stated stochastic gain interval. The centered operator norm is the maximum absolute multiplier \(\left|\prod_j(1-t_j\lambda)\right|\) over nonzero Laplacian eigenvalues.

**Small gains.** Every gain obeys \(1-\mu t_j\ge\rho>0\). If one is strictly less than \(1/(2d)\), its slow-mode multiplier is strictly greater than \(1-h\), so the full schedule has
\[
R\ge \prod_j(1-\mu t_j) > a_r(1-h) > B_r.
\]
This is a strict comparison for the norm itself; merely improving the slow mode would not suffice when another mode attains the maximum.

**Compression.** For the remaining schedules write \(b_j=2dt_j-1\in[0,1]\), \(B=\prod_j b_j\), and \(f(b)=1-h(1+b)>0\). The \(2d\)-mode has magnitude \(B\); the \(\mu\)-mode has positive multiplier \(\prod_j f(b_j)\). The exact identity
\[
f(u)f(v)-f(1)f(uv)=h(1-h)(1-u)(1-v)\ge0
\]
replaces \((u,v)\) by \((1,uv)\) without changing \(B\) and without increasing the slow-mode multiplier. Repeated application gives \(\prod_j f(b_j)\ge f(1)^{r-1}f(B)=a_r(1-h-hB)\). If at least two original \(b_j<1\), compressing those two first is strict and the other multipliers remain positive. Conversely, if at most one is below one, the displayed product is an equality.

Thus \(R\ge\max\{B,a_r(1-h-hB)\}\). This bound has a unique minimum at the intersection of the strictly increasing and strictly decreasing affine functions, namely \(B=B_r\in(0,1)\).

**Attainment and uniqueness.** Take \(r-1\) full gains and one correction as stated. Both endpoint eigenmodes \(\mu,2d\) have magnitude \(B_r\). For \(\lambda\in[\mu,2d-\mu]\) the full-gain factors give \(|1-\lambda/d|^{r-1}\le a_r\). The correction factor \(1-(1+B_r)\lambda/(2d)\), when nonnegative, is at most \(1-h(1+B_r)\), so the product magnitude is at most \(a_r[1-h(1+B_r)]=B_r\). When negative its magnitude is at most \(B_r\), as \(\lambda\le2d\), and multiplication by the full-gain factors cannot increase it. Equality of the norm with \(B_r\) forces \(B=B_r\) and equality in the compression bound. Thus there is exactly one \(b_j<1\) and it equals \(B_r\). Commutativity makes ordering immaterial.

For one round, convexity in \(\lambda\) shows that the worst mode is among \(\mu,2d\). On \([0,1/(2d)]\) the first dominates and decreases; on \([1/(2d),1/d]\) its decreasing value and the increasing magnitude of the second intersect at \(2/(2d+\mu)\). Repetition cannot be an optimal multiset for \(r\ge3\) because this gain lies strictly below \(1/d\) and all repetitions are equal. Finally the explicit formula implies the rate limit since \(a_r=\rho^{r-1}\) and \(0<\rho<1\).

## Verification

The accompanying `verify.py` gives exact rational checks of the compression identity, endpoint formula, small-graph Laplacian spectra and stochastic matrix products. Run it with Python 3.9 or later; the expected terminal line is `ALL_CHECKS_PASSED 326741`. The proof, not the finite samples, establishes the all-graph and all-horizon statements. For illustration \(B_3=3/17\) on the six-cycle (gains \(1/2,1/2,5/17\)); on the three-cube \(B_3=1/14\) (gains \(1/3,1/3,5/28\)).

## Relationship to prior work and limitations

Apers–Sarlette optimize polynomial filters without imposing entrywise Markov positivity at each stage. Boyd–Diaconis–Xiao optimize one transition kernel; Hendrickx–Shi–Johansson prove finite-time reachability allowing much more general spatial weights. The indexed stagewise-safe Richardson result gives a sharp interval-robust two-stage frontier and general-stage bounds, not this exact all-horizon finite-graph minimax. A same-day indexed odd-cycle result also uses a two-round homogeneous Markov schedule, but odd cycles are not bipartite and its horizon is two. An indexed November 22 bipartite-chain result gives an overlapping two-round law for a restricted range of the gap, outside the asserted horizon. The contribution here is the exact factor and unique scalar-gain multiset for every \(r\ge3\) in the stated bipartite regular regime. These comparisons do not settle historical priority.

The theorem does not optimize unrestricted graph-supported kernels and makes no assertion about changing topology, floating-point errors, noise, or convergence at intermediate times.

## References

1. S. Apers and A. Sarlette, *Accelerating Consensus by Spectral Clustering and Polynomial Filters*, https://arxiv.org/abs/1503.01269.
2. J. M. Hendrickx, G. Shi and K. H. Johansson, *Finite-time consensus using stochastic matrices with positive diagonals*, https://arxiv.org/abs/1302.6668.
3. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, https://web.stanford.edu/~boyd/papers/fmmc.html.
4. [*Sharp stagewise-safe Richardson frontier and a no-acceleration barrier*](https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-stagewise-safe-two-step-richardson-frontier--31fff666d705).
5. [*Sharp two-round stochastic consensus on odd cycles*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-two-round-stochastic-consensus-on-odd-cycles--b2b600a3fbfd).
6. [*A spectral-gap exception to interval-optimal two-round stochastic consensus on bipartite chains*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-spectral-gap-exception-to-interval-optimal-two-round-stochasti--276d97e49c41).
