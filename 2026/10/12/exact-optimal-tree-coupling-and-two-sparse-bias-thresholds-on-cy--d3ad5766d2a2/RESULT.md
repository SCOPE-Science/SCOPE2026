# Exact optimal tree coupling and two sparse-bias thresholds on cycles

## Finding

For every integer \(n\ge3\), let \(C_n\) be the undirected cycle with labeled vertices \(0,\ldots,n-1\). Independently at every vertex, choose the clockwise adjacent edge with probability \(p\in[0,1]\), and the counterclockwise adjacent edge with probability \(1-p\). Denote the union of the chosen undirected edges by \(H_{n,p}\), and let \(T_n\) be a uniformly random spanning tree of \(C_n\).

For edge sets, use the **unnormalized** Hamming cost \(d(E,F)=|E\mathbin{\triangle}F|\). Its optimal mean over all couplings, the \(1\)-Wasserstein distance, is exactly
\[
W_1\bigl(\mathcal L(H_{n,p}),\mathcal L(T_n)\bigr)
=np(1-p)-1+2\bigl(p^n+(1-p)^n\bigr).
\]
The total-variation distance is exactly
\[
d_{\mathrm{TV}}\bigl(\mathcal L(H_{n,p}),\mathcal L(T_n)\bigr)
=1-n\sum_{j=1}^{n-1}p^j(1-p)^{n-j}.
\]
In particular, the uniform \(1\)-out cycle model \(p=1/2\) satisfies
\[
W_1=\frac n4-1+2^{2-n},\qquad
d_{\mathrm{TV}}=1-\frac{n(n-1)}{2^n}.
\]

The formulas give two **different sharp sparse-bias optimizers**:
\[
\lim_{n\to\infty}\min_{p\in[0,1]}W_1=\log2,
\qquad
\lim_{n\to\infty}\min_{p\in[0,1]}d_{\mathrm{TV}}=1-e^{-1}.
\]
Every sequence of exact or asymptotic minimizers of the first distance must satisfy \(n\min\{p,1-p\}\to\log2\); every sequence of exact or asymptotic minimizers of the second must satisfy \(n\min\{p,1-p\}\to1\). Here “asymptotic minimizer” means a parameter sequence whose distance differs from that dimension's minimum by \(o(1)\).

More precisely, whenever \(p_n=\lambda/n+o(1/n)\) with \(\lambda\ge0\), the number \(M_n\) of edges missing from \(H_{n,p_n}\) converges in law to \(\operatorname{Poisson}(\lambda)\), while
\[
W_1\to\lambda-1+2e^{-\lambda},\qquad
d_{\mathrm{TV}}\to1-\lambda e^{-\lambda}.
\]
The same holds near \(p_n=1\) by reflecting the cycle.

## Assumptions and scope

The graph \(C_n\) is simple and undirected; \(n\ge3\), including the triangle. The labels fix the clockwise direction. Choices made at different vertices are independent and identically distributed with common orientation bias \(p\). If both endpoints select the same undirected edge, it is included once. The random spanning tree is the cycle with one uniformly selected edge removed. The Wasserstein metric is unnormalized edge symmetric difference; no vertex or graph-isomorphism quotient is taken. All assertions include the degenerate biases \(p=0\) and \(p=1\). Statements about optimizing biases permit a different bias for each \(n\).

## Proof

**Step 1: the exact missing-edge law.** Put \(q=1-p\), and independently take \(B_i\in\{0,1\}\) with \(\Pr(B_i=1)=p\), where \(1\) means clockwise and \(0\) means counterclockwise. Index edge \(e_i=\{i,i+1\}\) modulo \(n\). Edge \(e_i\) is not chosen by either endpoint if and only if \(B_i=0\) and \(B_{i+1}=1\). Thus
\[
M_n=\sum_{i=0}^{n-1}\mathbf1\{B_i=0,B_{i+1}=1\},
\qquad \mathbb E M_n=npq.
\]
A cyclic binary word has no \(01\) transition precisely when all bits agree, so \(\Pr(M_n=0)=p^n+q^n\). A cyclic word has exactly one such transition precisely when its \(1\)'s form one nonempty proper cyclic interval. Choosing the interval length \(j\in\{1,\ldots,n-1\}\) and one of its \(n\) starting vertices gives the **exact**, disjoint count
\[
\Pr(M_n=1)=n\sum_{j=1}^{n-1}p^jq^{n-j}.
\]
The formulas remain true at \(p=0,1\).

**Step 2: sharp transport by equivariance.** Since \(H_{n,p}\) has \(n-M_n\) edges and every spanning tree \(T_n\) has \(n-1\), any coupling satisfies
\[
|E(H_{n,p})\mathbin\triangle E(T_n)|\ge |M_n-1|.
\]
To attain the bound, conditionally on the sampled \(H_{n,p}\), choose the missing tree edge uniformly from the \(M_n\) edges absent in \(H_{n,p}\) if \(M_n\ge1\); if \(M_n=0\), choose it uniformly among all \(n\) edges. The joint construction is rotation-equivariant because the input law is rotation-invariant for every homogeneous bias \(p\). Consequently, the chosen deleted edge is uniform, and its complement is a uniform spanning tree. The symmetric difference is exactly \(|M_n-1|\), including on \(M_n=0\). Therefore
\[
W_1=\mathbb E|M_n-1|=\mathbb E M_n-1+2\Pr(M_n=0),
\]
which is the stated formula, with no appeal to an unverified optimization algorithm.

**Step 3: exact total variation.** A subset of the cycle's edges is a spanning tree if and only if it omits exactly one edge. By rotation symmetry, conditional on \(M_n=1\), the graph \(H_{n,p}\) is uniform over the \(n\) spanning trees. Hence its law has a mass \(\Pr(M_n=1)\) distributed exactly as \(\mathcal L(T_n)\), with all remaining mass supported off the spanning trees. Taking the sum of the smaller point masses gives
\(d_{\mathrm{TV}}=1-\Pr(M_n=1)\). Substituting Step 1 proves the second exact formula.

**Step 4: sparse Poisson scaling.** Suppose \(p_n=\lambda/n+o(1/n)\). Let \(R_n=\sum_iB_i\), a binomial random variable converging in law to \(\operatorname{Poisson}(\lambda)\). Counting a one according to whether its previous bit is zero or one gives the exact identity
\[
R_n-M_n=\sum_i\mathbf1\{B_i=B_{i-1}=1\}\ge0.
\]
Its expectation is \(np_n^2\to0\), so \(M_n-R_n\to0\) in probability and \(M_n\Rightarrow\operatorname{Poisson}(\lambda)\). In addition, \(np_n(1-p_n)\to\lambda\), \((1-p_n)^n\to e^{-\lambda}\), and \(p_n^n\to0\). The Wasserstein expression consequently tends to \(\lambda-1+2e^{-\lambda}\). The exact event probability \(\Pr(M_n=1)\) tends to \(\lambda e^{-\lambda}\), giving the total-variation limit. Reflection exchanges \(p_n\) and \(1-p_n\).

**Step 5: globally optimal bias and sharp scales.** The limiting transport function \(f(\lambda)=\lambda-1+2e^{-\lambda}\) has \(f''(\lambda)=2e^{-\lambda}>0\) and unique minimum at \(\lambda=\log2\), of value \(\log2\). For finite \(n\), choosing \(p=0\) gives transport cost \(1\); hence a minimizing sequence has \(np(1-p)-1\le1\), so \(n\min\{p,1-p\}\le4\). Extracting subsequences and using Step 4 proves both the lower bound \(\liminf\min_p W_1\ge\log2\) and the necessity of the unique limiting bias scale. Taking \(p=\log2/n\) proves the matching upper bound.

For total variation, maximize \(\Pr(M_n=1)\). If \(r=\min\{p,1-p\}\ge1/4\), Step 1 gives \(\Pr(M_n=1)\le n(n-1)(3/4)^n\to0\). If \(0\le r<1/4\), summing a geometric series bounds
\[
\Pr(M_n=1)\le \frac{nr(1-r)^n}{1-2r}
\le 2nr e^{-nr}.
\]
Therefore along any subsequence where \(nr\to\infty\), the one-missing-edge probability tends to zero. If \(nr\) stays bounded, Step 4 and reflection show that every subsequential limit is \(\lambda e^{-\lambda}\), whose unique maximum on \([0,\infty)\) is \(e^{-1}\) at \(\lambda=1\). Choosing \(p=1/n\) attains this limit. Compactness, uniqueness and the strict deficit away from this limit give both the optimal total-variation value and the asserted necessary bias scale. \(\square\)

## Verification

Run `python3 verify.py` in the directory containing this document. The standalone checker enumerates each orientation word for \(3\le n\le10\) at eleven exact-rational biases. It reconstructs the edge set, missing-edge count, explicit optimal coupling, tree marginal, and all formulae. It also checks the cyclic-run distribution by an independent combinatorial counting expression. Recorded outcome: `PASS: 1936 exact finite checks across 88 (n,p) pairs`. These finite computations check normalization and edge cases; they are not substitutes for Steps 1–5, which prove the statements for every eligible \(n,p\).

## Relationship to prior work

The motivating literature studies uniform spanning trees as determinantal processes and their relation to independent local selection. Nachmias and Peled, arXiv:2510.19563v1 (22 October 2025), prove high-degree local limits in a substantially different asymptotic setting. Mészáros and Peled, arXiv:2610.11554v1 (8 October 2026), subsequently prove a general \(O(n\log k/\sqrt{k})\) expected coupling bound at minimum degree \(k\ge2\). At \(k=2\), that bound does not determine the exact optimal cost or either bias-optimization scale. Frieze and Johansson's work on random \(k\)-out subgraphs studies connectivity rather than the present edge-law comparisons.

A general symmetry argument explains why selecting an omitted edge yields a uniform spanning tree on a transitive cycle; the new content lies in the simultaneous exact law, optimal coupling, and distinct sharp sparse-bias phase profiles. The formulas do not claim a general optimal coupling for nontransitive graphs. No claim of exhaustive priority certification is made.

## Limitations

The cycle is homogeneous and simple, the choices are independent, and the target is the **uniform** spanning-tree law. For nonuniform biases at different vertices the rotation-equivariant argument can fail to produce a uniform tree. The asymptotic statements optimize over biases depending on \(n\); they do not establish closeness of the unbiased \(1\)-out law, which instead has order-\(n\) expected edge discrepancy and total variation tending to one. No convergence rates beyond the displayed formulas, no optimal coupling for general graphs, and no independence-based audit are asserted. An equivalent result might occur in older literature on cyclic runs, transitive transport or spanning-tree couplings.

## References

1. A. Nachmias and Y. Peled, *Local limits of determinantal processes*, arXiv:2510.19563v1 (22 October 2025), https://arxiv.org/html/2510.19563v1 .
2. A. Mészáros and Y. Peled, *Product approximations for uniform spanning trees and determinantal processes*, arXiv:2610.11554v1 (8 October 2026), https://arxiv.org/html/2610.11554v1 .
3. A. Frieze and T. Johansson, *On random \(k\)-out subgraphs of large graphs*, https://www.math.cmu.edu/~af1p/Texfiles/Gkout.pdf .
