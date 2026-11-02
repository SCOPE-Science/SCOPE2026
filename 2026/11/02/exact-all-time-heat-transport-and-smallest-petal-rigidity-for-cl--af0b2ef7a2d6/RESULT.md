# Exact all-time heat transport and smallest-petal rigidity for clique bouquets

## Finding

Let \(m\ge1\) and let \(d_1,\ldots,d_m\ge1\) be arbitrary integers. Form the finite simple clique bouquet
\[
G=K_1\vee\Bigl(\bigsqcup_{i=1}^m K_{d_i}\Bigr),
\qquad k=\sum_{i=1}^m d_i,\qquad s=\min_i d_i.
\]
The single universal vertex is \(h\); the disjoint peripheral cliques are the blades \(B_i\). Give each edge length one. Let \(L=D-A\) be the **combinatorial**, not degree-normalized, Laplacian and \(H_t=e^{-tL}\), for every real \(t\ge0\). Set
\[
a=e^{-t},\qquad b_i=e^{-(d_i+1)t},\qquad c=e^{-(k+1)t}.
\]
For the original shortest-path metric \(d_G\), the exact Wasserstein-one distance between any two distinct heat-kernel rows is
\[
W_1\bigl(H_t(x,\cdot),H_t(y,\cdot)\bigr)
=\begin{cases}
b_i,&x,y\in B_i,\\[2pt]
2a,&x\in B_i,\ y\in B_j,\ i\ne j,\\[2pt]
c+\dfrac{2(k-d_i)}{k}(a-c),&x=h,\ y\in B_i.
\end{cases}
\]
The symmetric case \(x\in B_i,y=h\) has the same value. In particular, all pair types are covered, including \(t=0\), singleton blades, and \(m=1\).

On real-valued functions modulo constants use \(\operatorname{Lip}(f)=\max_{uv\in E(G)}|f(u)-f(v)|\). Its exact, attained strong operator seminorm is
\[
\boxed{\ \|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}
=c+\frac{2(k-s)}{k}(a-c)
=\frac{2(k-s)}{k}e^{-t}-\frac{k-2s}{k}e^{-(k+1)t}.\ }
\]
For \(t>0\) with at least two blades, a hub-to-leaf edge is norming exactly when its blade is of minimum size. An attaining unit-Lipschitz input is \(f=1\) at \(h\), \(f=0\) on a chosen minimum blade, and \(f=2\) on all other blades.

**Smallest-petal rigidity.** At each time, the sharp norm depends only on \(k\) and \(s\), not on the number, sizes, or arrangement of the other blades. In particular, every clique bouquet with a singleton blade has **exactly the same full-time Lipschitz heat norm as the \(k\)-leaf star**, regardless of how the other leaves are partitioned into disjoint cliques. More generally, compared with the same \(k\)-leaf star, internal clique edges lower the exact sharp norm by
\[
\frac{2(s-1)}{k}\bigl(e^{-t}-e^{-(k+1)t}\bigr).
\]
This comparison is strict for \(t>0\) precisely when \(s>1\).

For \(m\ge2\), strict contraction at every \(t>0\) holds if and only if \(k\le2s+1\). When \(k>2s+1\), the norm initially rises, then reaches its unique positive-time peak at
\[
t_*=\frac1k\log\!\left(\frac{(k+1)(k-2s)}{2(k-s)}\right),
\qquad
\|H_{t_*}\|_{\mathrm{Lip}\to\mathrm{Lip}}
=\frac{2(k-s)}{k+1}
\left(\frac{2(k-s)}{(k+1)(k-2s)}\right)^{1/k}>1.
\]
For \(m=1\), the graph is complete and the norm is \(e^{-(k+1)t}\). The full-time profile and transport classification, rather than the previously available infinitesimal contraction threshold or the already-known star special case, are the asserted contribution.

## Assumptions and scope

The graph is finite, simple, connected and unweighted, with exactly one common hub and with clique blades intersecting only in that hub. The semigroup uses counting vertex measure and the combinatorial generator \(L=D-A\), giving unit jump rate on each edge. \(W_1\) uses the unweighted shortest-path distance, and the Lipschitz seminorm is over all real functions modulo constants. All formulas hold for every integer \(m\ge1\), every strictly positive integer blade profile, and every real \(t\ge0\), without asymptotic restrictions.

## Proof

**Spectral decomposition.** Write \(e_v\) for coordinate vectors and \(\mathbf1_B=\sum_{v\in B}e_v\). The following orthogonal subspaces exhaust \(\mathbb R^{k+1}\): constants, of eigenvalue zero; the one-dimensional span of \(e_h-k^{-1}\mathbf1_{V\setminus\{h\}}\), of eigenvalue \(k+1\); the peripheral vectors constant on each blade, zero at the hub and of peripheral sum zero, of eigenvalue one; and the within-blade mean-zero subspace on \(B_i\), of eigenvalue \(d_i+1\). These follow directly by applying \(L\) at the hub and each peripheral vertex. The dimensions sum to \(k+1\), including the possible zero-dimensional spaces.

**Hub-to-blade transport.** Fix \(u\in B_i\), write \(d=d_i\) and \(b=e^{-(d+1)t}\). Since the heat matrix is symmetric, the signed difference of its hub row and \(u\) row is
\[
H_t(e_h-e_u)=
 c\left(e_h-\frac1k\mathbf1_{V\setminus\{h\}}\right)
+a\left(\frac1k\mathbf1_{V\setminus\{h\}}-\frac1d\mathbf1_{B_i}\right)
+b\left(\frac1d\mathbf1_{B_i}-e_u\right).
\]
Its coordinate at \(h\) is \(c>0\); at each vertex outside \(B_i\cup\{h\}\) it is \((a-c)/k\ge0\); at each vertex of \(B_i\setminus\{u\}\) it is
\[
\frac{a-c}{k}-\frac{a-b}{d}
=a\left(\frac{1-e^{-kt}}{k}-\frac{1-e^{-dt}}{d}\right)\le0,
\]
and at \(u\) the last expression decreases by \(b\). The inequality follows because \(x\mapsto(1-e^{-xt})/x\) is nonincreasing on positive \(x\), and \(d\le k\). Thus all positive mass is at the hub and outside the chosen blade, while all negative mass is inside it.

Every unit of positive mass at the hub must travel distance one to the deficit blade; every positive unit on any other blade must travel distance two to it. Therefore the explicitly feasible transport cost is
\[
c+2\frac{k-d}{k}(a-c).
\]
It is optimal: the potential taking values \(1\) at \(h\), \(0\) on \(B_i\), and \(2\) on all other blades is globally one-Lipschitz and attains precisely this dual value. This proves the hub-to-blade formula without hidden sign assumptions.

**Two peripheral vertices.** For distinct \(u,v\in B_i\), the difference \(e_u-e_v\) is a within-blade eigenvector of eigenvalue \(d_i+1\). Consequently the heat-row difference is \(b_i(e_u-e_v)\), whose optimal transport cost is \(b_i\), as \(u\) and \(v\) are adjacent. If \(u\in B_i\) and \(v\in B_j\) with \(i\ne j\), the signed row difference is
\[
a\left(\frac{\mathbf1_{B_i}}{d_i}-\frac{\mathbf1_{B_j}}{d_j}\right)
+b_i\left(e_u-\frac{\mathbf1_{B_i}}{d_i}\right)
-b_j\left(e_v-\frac{\mathbf1_{B_j}}{d_j}\right).
\]
Every coordinate in \(B_i\) is nonnegative and every coordinate in \(B_j\) is nonpositive because \(a\ge b_i,b_j\). The total positive mass is \(a\), and all distances between these blades are two. Transporting that mass across costs \(2a\); the one-Lipschitz potential equal to \(1\) on \(B_i\), \(-1\) on \(B_j\), and zero elsewhere attains the same dual value.

**Global sharp norm.** Finite-metric Kantorovich duality gives \(\|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}=\max_{xy\in E(G)}W_1(H_t(x,\cdot),H_t(y,\cdot))\). For \(m\ge2\), the smallest blade satisfies \(s\le k/2\); its hub-edge transport is at least \(a\), whereas within-blade edge transports \(b_i\) are at most \(a\). The hub-edge expression decreases with \(d_i\) for \(t>0\), so its maximum is attained precisely on minimum blades, with the stated potential. When \(m=1\), all edge differences decay by \(e^{-(k+1)t}\); the same formula follows. At \(t=0\) every case returns distance or norm one as required.

**Time behavior.** Differentiating the two-exponential norm yields
\[
\left.\frac{d}{dt}\|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}\right|_{t=0}=k-2s-1.
\]
For \(m\ge2\), the positive fast exponential coefficient in the derivative can cross the slower negative one at most once. It crosses at a positive time precisely when \(k>2s+1\), giving the stated \(t_*\) and peak. In the complementary range the profile decreases strictly for all \(t>0\), including the zero-derivative boundary. The star comparison follows by subtracting the displayed formula with \(s=1\).

## Verification

The standalone `verify.py` builds the graph Laplacian and its complete rational spectral projectors and checks the exact heat matrix at \(t=\log 2\) and \(t=\log 3\). For **every ordered positive-integer composition** of \(k=1,\ldots,8\), it checks the projection identities, spectral eigenvalue equations, symmetry and stochasticity, then independently maximizes the Kantorovich dual objective over all integral anchored one-Lipschitz potentials. Integrality follows from total unimodularity of the graph's difference-constraint matrix. The checker compares this optimization to all claimed pair transports and the edge-operator norm: **255 profiles, 510 exact-rational heat instances, 14,846 pairwise dual comparisons**. Running `python verify.py` prints `CERTIFICATE_OK` on success.

The infinite-family proof above is analytic and does not extrapolate from the finite checker; the checker is a replayable cross-check of the spectral decomposition, transport constraints and boundaries.

## Relationship to prior work

Ollivier introduced Wasserstein contraction as a curvature observable for Markov chains; Jost and Liu developed graph-curvature bounds related to triangles, using a degree-normalized walk. Münch and Wojciechowski established equivalences between curvature bounds and exponential Lipschitz semigroup estimates on general graphs. These establish the framework but do **not** provide the exact arbitrary-time pairwise transport profile of the clique bouquets above. Jost, Mulas and Zhang analyze spectral gaps of normalized Laplacians on petal and book graphs; their homogeneous petal case has overlapping graph objects but a different invariant and generator.

The infinitesimal edge-total-variation contraction threshold for clique bouquets is already available and happens to agree numerically with the transition here; it is not a new assertion. The complete-bipartite star special case of the Lipschitz norm is likewise previously available. Neither one yields the full pairwise Wasserstein formulas or the all-time invariance under repartition of nonminimal blades. No covering exact transport law was identified in targeted mathematical-record and primary-literature searches; unindexed equivalent calculations remain possible.

## Limitations

Only one-hub unions of complete unweighted peripheral blocks, the combinatorial graph Laplacian, the original graph distance and \(W_1\) are covered. Weighted edges, degree normalization, arbitrary multi-hub block graphs, and \(W_p\) for other exponents are not covered. This is a mathematical proof and replayable self-review, not independent scientific validation or a guarantee of publication priority.

## References

1. Y. Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886, first public version 2007-01-30. https://arxiv.org/abs/math/0701886
2. J. Jost and S. Liu, *Ollivier's Ricci curvature, local clustering and curvature dimension inequalities on graphs*, arXiv:1103.4037, 2011. https://arxiv.org/abs/1103.4037
3. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875, 2017. https://arxiv.org/abs/1712.00875
4. J. Jost, R. Mulas and D. Zhang, *Petals and books: The largest Laplacian spectral gap from 1*, Journal of Graph Theory (2023), DOI 10.1002/jgt.22999. https://doi.org/10.1002/jgt.22999
