# The one-correction finite-horizon minimax law for stochastic consensus on regular bipartite graphs

## Finding

Let \(G\) be a connected simple \(d\)-regular bipartite graph on \(N\ge6\) vertices, with \(d\ge2\), combinatorial Laplacian \(L=dI-A\), and spectral gap \(\mu=\lambda_2(L)\) satisfying \(0<\mu<d\). Fix any integer horizon \(r\ge3\). For each round choose a single spatially homogeneous nearest-neighbor gain \(0\le t_j\le1/d\), so that \(P_j=I-t_jL\) is individually symmetric, doubly stochastic, and entrywise nonnegative. Define the centered Euclidean contraction
\[
R(t_1,\ldots,t_r)=\left\|P_r\cdots P_1-\frac{\mathbf1\mathbf1^\mathsf T}{N}\right\|_2.
\]
Put
\[
h=\frac{\mu}{2d},\qquad \rho=1-\frac{\mu}{d},\qquad a_r=\rho^{r-1},\qquad
\boxed{B_r=\frac{a_r(1-h)}{1+h a_r}}.
\]
Then the exact global optimum over **all** such gain sequences is \(\min R=B_r\). The unique optimal multiset of gains is
\[
\boxed{\{t_1,\ldots,t_r\}=\left\{\underbrace{\frac1d,\ldots,\frac1d}_{r-1\text{ rounds}},\;\frac{1+B_r}{2d}\right\}.}
\]
Thus all but one round use the full neighbor-averaging gain \(1/d\); one correction round, at any position, prevents the bipartite \(-1\) mode from surviving. No time-varying spatial weights, memory variables, or non-stochastic intermediate matrices are allowed in this theorem.

The finite-horizon optimum is strictly smaller than the \(r\)-round contraction obtained by repeating the optimal *single* homogeneous Markov gain \(2/(2d+\mu)\), because that repeated multiset differs from the unique optimal multiset. Moreover
\[
\lim_{r\to\infty} B_r^{1/r}=1-\frac{\mu}{d},
\]
where the limit refers to **separately horizon-optimized** gain schedules, not to a single precommitted infinite schedule.

## Assumptions and scope

All graphs are finite, simple, connected, undirected, bipartite, and regular. The unweighted degree \(d\) is at least \(2\); the matrices are exact real matrices. Every round uses the **same** graph Laplacian with a common scalar gain, constrained by \(0\le t_j\le1/d\). The norm is the induced Euclidean operator norm on the subspace orthogonal to \(\mathbf1\). The assumption \(\mu<d\) excludes the complete bipartite graphs \(K_{d,d}\), where exact consensus in two steps makes long-horizon optimizers nonunique. The theorem concerns \(r\ge3\), not all graph-supported Markov chains or arbitrary polynomial filters.

## Proof

**Spectrum and admissible factors.** Regular bipartiteness gives adjacency eigenvalue pairing \(\theta\leftrightarrow-\theta\). Since \(G\) is connected, the Laplacian has eigenvalues \(0\) and \(2d\), and the remaining eigenvalues lie in \([\mu,2d-\mu]\). The assumption \(0<\mu<d\) gives \(0<h<1/2\) and \(0<\rho<1\). The diagonal of \(I-tL\) equals \(1-dt\); every edge entry is \(t\), so individual stochastic nonnegativity is exactly \(0\le t\le1/d\).

**Eliminating small gains.** If any gain \(t<1/(2d)\), replacing it by \(1/(2d)\) weakly decreases the absolute spectral factor \(|1-t\lambda|\) for every \(\lambda\in[0,2d]\). It strictly decreases the positive slow-mode factor at \(\lambda=\mu\), while all other slow-mode factors are strictly positive because \(\mu<d\). Such a gain cannot occur in a minimizer. Therefore every optimal candidate has \(t_j\in[1/(2d),1/d]\).

**Compression inequality.** Write \(b_j=2dt_j-1\in[0,1]\) and \(B=\prod_{j=1}^r b_j\). The magnitude of the \(2d\)-mode multiplier is exactly \(B\). For the slow \(\mu\)-mode put \(f(b)=1-h(1+b)\); its multiplier is \(\prod_j f(b_j)\). For any \(u,v\in[0,1]\), the exact identity
\[
f(u)f(v)-f(1)f(uv)=h(1-h)(1-u)(1-v)\ge0
\]
allows two parameters to be replaced by \(1,uv\) without increasing the slow-mode multiplier and without changing \(B\). Repeating this compression proves
\[
\prod_{j=1}^r f(b_j)\ge f(1)^{r-1}f(B)
=\rho^{r-1}(1-h-hB).
\]
Equality, because \(h(1-h)>0\) and \(f>0\), holds only if at most one \(b_j\) is smaller than \(1\).

**Endpoint minimax lower bound.** The two eigenmodes \(\mu\) and \(2d\) thus give
\[
R(t_1,\ldots,t_r)\ge \max\left\{a_r(1-h-hB),\ B\right\}.
\]
The first affine function decreases in \(B\), while the second increases. Their unique intersection lies in \((0,1)\) and equals \(B_r=a_r(1-h)/(1+h a_r)\). Hence \(R\ge B_r\) for every admissible sequence.

**Attainment at all spectral modes.** Take \(r-1\) gains equal to \(1/d\) and the last equal to \(t_*=(1+B_r)/(2d)\). The multiplier at an arbitrary nonzero Laplacian eigenvalue \(\lambda\) is
\[
\left(1-\frac{\lambda}{d}\right)^{r-1}
\left(1-\frac{(1+B_r)\lambda}{2d}\right).
\]
At \(\lambda=\mu\) its magnitude is \(a_r(1-h-hB_r)=B_r\); at \(\lambda=2d\) it is also \(B_r\). For every other \(\lambda\in[\mu,2d-\mu]\), the first factor has magnitude at most \(\rho^{r-1}=a_r\). If the correction factor is nonnegative, it is at most \(1-h(1+B_r)\), hence the product magnitude is at most \(B_r\). If the correction factor is negative, its magnitude is at most \(B_r\) since \(\lambda\le2d\), and multiplication by \(a_r\le1\) preserves that bound. Thus no unexamined eigenmode exceeds \(B_r\), completing attainment.

**Uniqueness.** Equality in the endpoint lower bound forces \(B=B_r\), and equality in the strict compression identity forces all but at most one \(b_j\) to equal \(1\). Therefore the multiset of gains stated above is the only optimizer; permutations give the same commuting matrix product. The repeated one-gain schedule is different for \(r\ge3\), giving strict improvement. The asymptotic limit follows directly from \(a_r=\rho^{r-1}\).

## Verification

The included dependency-free `verify.py` runs exact rational tests of the compression identity and endpoint formulas, compares against rational gain grids, reconstructs Laplacian characteristic polynomials for four small graphs, and computes exact stochastic transition products. It completed **326741 checks**. Families include even cycles, Boolean hypercubes, balanced complete bipartite graphs (the excluded degeneracy as a boundary test), and crown graphs. These finite checks do not prove the graph-uniform claim; the preceding analytic argument does.

Two exact illustrative values: on the six-cycle \(d=2,\mu=1,r=3\), the minimum is \(B_3=3/17\), with gains \(\{1/2,1/2,5/17\}\). On the three-cube \(d=3,\mu=2,r=3\), the minimum is \(B_3=1/14\), with gains \(\{1/3,1/3,5/28\}\).

## Relationship to prior work

Apers and Sarlette's 2015 polynomial-filter paper formulates gain-factor products and gives a general unconstrained **two-stage** optimizer and graph-weight preconditioning; it explicitly drops entrywise Markov positivity. Those results do not give the present all-horizon exact minimax with individually stochastic stages. The published stagewise-safe Richardson result establishes an exact **two-step** interval-robust frontier and an asymptotic complexity sandwich for arbitrary stage counts. Its lower bound from the smallest eigenvalue does not imply this finite-graph sharp factor or the unique \(r\)-stage correction multiset for \(r\ge3\). The present proof uses the additional bipartite spectral reflection and a strict multiplicative compression inequality. The two-step phenomenon, complete-bipartite exact-consensus case, and general existence of finite-time consensus are not claimed as original.

Hendrickx, Shi, and Johansson's general finite-time consensus construction permits heterogeneous graph-supported stochastic matrices and solves reachability/existence, not the scalar, finite-horizon spectral minimax. Boyd, Diaconis, and Xiao optimize one homogeneous Markov transition kernel rather than an arbitrary fixed horizon of independently chosen scalar gains.

## Limitations

The theorem does not optimize unrestricted graph-supported stochastic matrices, nonregular or nonbipartite networks, robustness to changing topology, noise, floating-point errors, convergence between rounds, or a single infinite gain schedule. Reaching exact consensus in two rounds on \(K_{d,d}\) destroys uniqueness, so that boundary family is deliberately outside the main claim. The literature comparison is supported by identified available texts and indexed records, not an exhaustive proof that no prior equivalent theorem exists. Independent mathematical validation has not been performed.

## References

1. S. Apers and A. Sarlette, *Accelerating Consensus by Spectral Clustering and Polynomial Filters*, arXiv:1503.01269v1, publicly posted 2015-03-04. https://arxiv.org/abs/1503.01269
2. J. M. Hendrickx, G. Shi, and K. H. Johansson, *Finite-time consensus using stochastic matrices with positive diagonals*, arXiv:1302.6668. https://arxiv.org/abs/1302.6668
3. S. Boyd, P. Diaconis, and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. https://web.stanford.edu/~boyd/papers/fmmc.html
4. *Sharp stagewise-safe Richardson frontier and a no-acceleration barrier*, published mathematical research record (2026). https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-stagewise-safe-two-step-richardson-frontier--31fff666d705
