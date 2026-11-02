# Poisson fringe defects and a sharp near-complete-reinforcement mixing window

## Finding

Let \(T_N\) be a uniformly random recursive tree on vertices \(1,\ldots,N\), rooted at \(1\), and independently delete every edge with probability \(q_N\), where \(Nq_N\to\lambda\in[0,\infty)\). Write \(C_{N,k}\) for the number of non-root components of size \(k\) after deletion, and \(D_N\) for the number of vertices outside the root component. Then the entire finite counting measure of non-root component sizes converges in law to independent Poisson counts:

\[
(C_{N,k}:k\ge1)\ \Longrightarrow\ (C_k:k\ge1),\qquad
C_k\ \text{independent},\quad C_k\sim\operatorname{Pois}\!\left(\frac{\lambda}{k(k+1)}\right).
\]

Here convergence of count sequences is in \(\ell^1(\mathbb N)\): the probability of a component beyond any large fixed size can be made uniformly small. In particular,

\[
D_N\Longrightarrow W=\sum_{k\ge1}kC_k,
\quad \mathbb E[z^W]=\exp\!\left(\lambda\frac{1-z}{z}\log(1-z)\right),\quad 0<z<1.
\]

The law of \(W\) is compound Poisson with rate \(\lambda\) and integer jump probabilities \(\pi_k=1/[k(k+1)]\). For \(\lambda>0\), its tail satisfies \(\Pr(W\ge m)\sim\lambda/m\) as \(m\to\infty\), and \(\mathbb EW=\infty\). Despite convergence in law, \(\mathbb ED_N\sim\lambda\log N\) for fixed \(\lambda>0\) when \(q_N=\lambda/N\).

Consequently, consider a step-reinforced random walk on \(\mathbb Z_2\), started at zero, with fresh steps independently uniform on \(\{0,1\}\) and each subsequent step either copied from a uniformly chosen previous step with probability \(\alpha_N=1-q_N\) or sampled afresh with probability \(q_N\). The parameter \(\alpha_N\) is held fixed throughout each \(N\)-step walk. For every odd \(N\), its terminal distribution is exactly uniform; along even \(N\),

\[
\boxed{\lim_{\substack{N\to\infty\\N\ \mathrm{even}}}
\bigl\|\mathcal L(S_N)-\operatorname{Unif}(\mathbb Z_2)\bigr\|_{\mathrm{TV}}
=\frac12\exp(-\lambda\log2)=2^{-\lambda-1}.}
\]

This gives the complete finite-intensity crossover from deterministic even-time parity at \(\lambda=0\) to arbitrarily small parity bias as \(\lambda\) grows, in the near-perfect-copying window.

## Assumptions and scope

A uniform recursive tree has independent parents \(P_j\), each uniform on \(\{1,\ldots,j-1\}\), for \(j=2,\ldots,N\). A fringe subtree consists of a vertex and all its descendants before any cuts. Edges are deleted independently of one another and of the tree. All limits take \(N\to\infty\) through positive integers, except the final mixing limit through even integers. The case \(\lambda=0\) is included for convergence and mixing. The displayed mean asymptotic requires fixed \(\lambda>0\) and exact \(q_N=\lambda/N\).

Convergence of count sequences means convergence in the metric \(\sum_{k\ge1}|x_k-y_k|\) on integer-valued summable sequences. The limit has finitely many components almost surely, because \(\sum_k\lambda/[k(k+1)]=\lambda\), although its total mass has infinite mean when \(\lambda>0\).

## Proof

**1. Exact fringe profile and concentration.** Let \(B_{N,k}\) count *non-root vertices* with an original (uncut) fringe subtree of size \(k\). For \(1\le k<N\), a direct growth calculation gives

\[
\mathbb EB_{N,k}=\frac{N}{k(k+1)}.
\]

Indeed, a fringe subtree of size \(k\) is hit by the next independent uniform parent with probability \(k/N\), while a subtree of size \(k-1\) becomes one of size \(k\) with probability \((k-1)/N\). Thus, for interior indices,

\[
\mathbb EB_{N+1,k}=\left(1-\frac{k}{N}\right)\mathbb EB_{N,k}
+\frac{k-1}{N}\mathbb EB_{N,k-1}+\mathbf1_{\{k=1\}}.
\]

The boundary term \(B_{N,N}=0\) and the initial one-vertex tree establish the formula inductively, including the highest non-root size.

For each fixed \(k\), the normalized count satisfies \(B_{N,k}/N\to1/[k(k+1)]\) in probability. To verify this without requiring a special concentration theorem, represent the tree by independent parent choices and apply Efron--Stein. Replacing a single parent \(P_j\) moves the entire subtree rooted at \(j\), changing the fringe size only along the old and new ancestor chains to the root. The number of possibly affected entries in \(B_{N,k}\) is at most the sum of these chain lengths plus two. The depth of a vertex of index at most \(N\) in a uniform recursive tree has second moment \(O((\log N)^2)\), for instance by its standard independent-record-indicator representation. Summing the Efron--Stein bounds over \(j\) gives \(\operatorname{Var}(B_{N,k})=O(N\log^2N)=o(N^2)\). This proves the asserted concentration. Classical sharper fringe-count variance bounds are also known.

**2. Poisson thinning.** Conditional on the uncut tree, the numbers of deleted edges whose child has fringe size \(1,\ldots,K\) are independent binomial variables with parameters \((B_{N,k},q_N)\). Their joint probability generating function is

\[
\prod_{k=1}^K\left(1+q_N(z_k-1)\right)^{B_{N,k}}
\longrightarrow
\exp\!\left(\lambda\sum_{k=1}^K\frac{z_k-1}{k(k+1)}\right).
\]

The convergence is in probability conditionally and hence unconditionally by bounded convergence. Thus the fixed-size marked-fringe counts converge jointly to the claimed independent Poisson variables. Moreover, the expected number of cuts with original fringe size above \(K\) is

\[
q_N\sum_{k=K+1}^{N-1}\frac{N}{k(k+1)}
=q_NN\left(\frac{1}{K+1}-\frac1N\right)\le\frac{q_NN}{K+1}.
\]

Since \(q_NN\) is bounded, this uniformly excludes large-size escape of the *number* of components and yields \(\ell^1\)-convergence of the marked-fringe count sequence.

**3. Nested cuts vanish.** Two cut edges are nested if the child of one is an ancestor of the child of the other. Their expected number is at most

\[
q_N^2\sum_{j=2}^N\mathbb E\bigl[\operatorname{depth}(j)-1\bigr]
=O\!\left(q_N^2N\log N\right)=o(1).
\]

Here, the depth convention is distance from vertex \(1\); an edge is identified with its non-root endpoint. Hence with probability tending to one no two deleted edges are nested. On that event every non-root percolation component is *exactly* the original fringe subtree below its deleted incoming edge; component counts agree with marked-fringe counts, and \(D_N\) is the sum of their sizes. The preceding tail bound implies that, with arbitrarily high probability, all these sizes lie below a fixed \(K\). The asserted component spectrum and compound-Poisson weak limit follow by truncation and the continuous mapping theorem.

Summing \(\sum_{k\ge1}z^k/[k(k+1)]\) gives

\[
\sum_{k\ge1}\frac{z^k}{k(k+1)}
=1+\frac{1-z}{z}\log(1-z),
\]

which yields the generating function. Its jump tail is \(\Pr(J\ge m)=\sum_{k\ge m}1/[k(k+1)]=1/m\). A standard elementary one-large-jump argument for a fixed sum of these regularly varying positive integer variables, followed by truncation of a Poisson number of summands, gives \(\Pr(W\ge m)\sim\lambda/m\); a direct upper bound for the truncation is \(\Pr(\sum_{i=1}^rJ_i\ge m)\le r\Pr(J\ge\lceil m/r\rceil)\le r^2/(m-r)\) for \(m>r\), whose Poisson expectation is uniformly integrable. Thus \(\mathbb EW=\infty\) when \(\lambda>0\).

To see why the finite means nonetheless grow, a vertex at depth \(d\) is detached with probability \(1-(1-q_N)^d\). Uniformly bounding the second-order error by \(q_N^2d^2/2\), and using \(\sum_{j=1}^N\mathbb E\operatorname{depth}(j)=N(H_N-1)\), plus \(\sum_j\mathbb E\operatorname{depth}(j)^2=O(N\log^2N)\), gives \(\mathbb ED_N=\lambda(H_N-1)+O(\lambda^2\log^2N/N)\) when \(q_N=\lambda/N\).

**4. Exact parity representation.** The reinforced walk can be constructed from exactly this percolated recursive tree: a copied step inherits the step at its chosen parent, while each removed edge starts a new independent uniform bit. Therefore each forest component has an independent uniform bit, constant over that component. Conditionally on the forest,

\[
\mathbb E[(-1)^{S_N}\mid T_N,\text{cuts}]
=\prod_{\text{components }A}\frac{1+(-1)^{|A|}}2
=\mathbf1_{\{\text{every component size is even}\}}.
\]

For odd \(N\) at least one size must be odd, so the terminal bit is exactly uniform. For even \(N\), the root component size has the same parity as the sum of the non-root component sizes; hence all component sizes are even precisely when there are no odd-sized non-root components. The component-count limit and the large-size-count tail bound imply

\[
\Pr(\text{all component sizes even})\longrightarrow
\prod_{\substack{k\ge1\\k\,\mathrm{odd}}}\exp\!\left(-\frac{\lambda}{k(k+1)}\right)
=\exp(-\lambda\log2),
\]

since \(\sum_{k\ge1,\,k\mathrm{\ odd}}1/[k(k+1)]=\log2\). On \(\mathbb Z_2\), total variation from uniform is half the absolute parity character; the mixing formula follows.

## Verification

The standalone Python 3 script `verification/check.py` uses exact rational arithmetic and no external packages. It enumerates all increasing parent arrays for tree orders \(2\) through \(7\), checking the exact fringe expectations. It separately compares the direct reinforced-step Markov recursion for the parity character with an independent exhaustive percolated-forest calculation for orders \(2\) through \(6\) and three deletion probabilities at each size, including exact uniformity at odd orders. Run `python verification/check.py`; the observed output in `verification/check_output.txt` reports 63 passing assertions. These calculations check finite identities but do not establish infinite convergence or priority.

## Relationship to prior work

Peres and Qin (arXiv:2604.07207, first submitted April 8, 2026) introduced the finite-group step-reinforced walk framework and its random-recursive-forest representation. Their companion (arXiv:2604.07227, submitted April 8, 2026) proves for the uniform-bit walk exact parity uniformity at odd times and exponential **bounds** on even-time parity bias at fixed reinforcement. Those bounds permit, but do not determine, the present joint limit with \(N(1-\alpha_N)\to\lambda\). The sharp coefficient \(\log2\), its Poisson defect interpretation, and the corresponding near-perfect-copying crossover are not stated there.

The classical fringe-subtree law for uniform recursive trees, including exact mean and variance control, is available in Seelbach Benkner and Wagner (2022), Lemma 3, and earlier work of Fuchs (2008). These inputs are not claimed as new. Baur (arXiv:1407.2508) treats percolation parameters approaching one, but its large-cluster scaling theorem requires the expected number of cuts to diverge, excluding the present finite-intensity regime. The Poisson fringe lemma above draws on the known profile plus sparse independent marking; the assessed mathematical contribution is the complete resulting component-deficit law together with the exact reinforced-walk mixing window.

## Limitations

The main asymptotics require independent uniform recursive-tree parent choices and independent edge deletion with \(Nq_N\to\lambda<\infty\). The walk conclusion uses independent uniform fresh steps on \(\mathbb Z_2\), not arbitrary groups or biased fresh-step laws. No quantitative convergence rate in \(N\) is claimed. Previously developed general Poisson-thinning and random-tree results might provide alternate derivations; the historical originality assessment requires independent confirmation. The finite checker is not an infinite-size proof.

## References

1. Y. Peres and S. Qin, *Mixing times of step-reinforced random walks* (2026), arXiv:2604.07207; https://arxiv.org/abs/2604.07207 (first public April 8, 2026).
2. Y. Peres and S. Qin, *Transition probabilities of step-reinforced random walks* (2026), arXiv:2604.07227; https://arxiv.org/abs/2604.07227 (first public April 8, 2026).
3. L. Seelbach Benkner and S. Wagner, *Distinct Fringe Subtrees in Random Trees*, Algorithmica 84 (2022), Lemma 3; https://doi.org/10.1007/s00453-022-01013-y.
4. M. Fuchs, *Subtree Sizes in Recursive Trees and Binary Search Trees: Berry–Esseen Bounds and Poisson Approximations*, Combinatorics, Probability and Computing 17 (2008), 661–680; https://doi.org/10.1017/S0963548308009243 (bibliographic identifier to be independently checked).
5. E. Baur, *Percolation on random recursive trees*, arXiv:1407.2508 (2014); https://arxiv.org/abs/1407.2508.
