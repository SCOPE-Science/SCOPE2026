# Shape-universal covariance sign reversals for random-graph component counts

## Finding
Let \(G(n,p)\) be the simple Erdős–Rényi graph with independent edges, let \(H,K\) be arbitrary connected unlabeled graphs of distinct orders \(h,k\), and let \(C_H,C_K\) count their connected-component occurrences. For \(h+k\le n\) and \(0<p<1\), put \(\mu_H=\mathbb EC_H\) and \(\mu_K=\mathbb EC_K\). Then
\[
\operatorname{Cov}(C_H,C_K)=\mu_H\mu_K\left[\frac{(n-h)_{\underline{k}}}{(n)_{\underline{k}}}(1-p)^{-hk}-1\right]. \tag{1}
\]
Hence for any two different component sizes, the complete cross-size covariance block indexed by connected isomorphism types equals a scalar times the outer product of the corresponding mean vectors. It has rank one whenever that scalar is nonzero; at its unique zero it has rank zero.

The covariance in (1) changes sign exactly at
\[
p^*_{n;h,k}=1-\left[\frac{(n-h)_{\underline{k}}}{(n)_{\underline{k}}}\right]^{1/(hk)}\in(0,1). \tag{2}
\]
It is negative below and positive above this threshold. The threshold is strictly increasing with either size, with the other fixed, whenever both pairs satisfy the feasibility condition. In particular, fixing \(h\ne k\) as \(n\to\infty\),
\[
p^*_{n;h,k}=\frac1n+\frac{h+k-2}{2n^2}+O_{h,k}(n^{-3}). \tag{3}
\]

Write \(X_j\) for the number of components of order \(j\), regardless of shape, and set \(p=n^{-1}+\lambda n^{-2}\), with fixed real \(\lambda\). For every fixed pair \(h\ne k\),
\[
\operatorname{Cov}(X_h,X_k)\longrightarrow hk\,\tau_h(1)\tau_k(1)\left(\lambda-\frac{h+k-2}{2}\right),\quad
\tau_j(c)=\frac{j^{j-2}c^{j-1}e^{-jc}}{j!},\quad\tau_1(c)=e^{-c}. \tag{4}
\]
Thus different pairs of small component sizes reverse the sign of their cross-covariance at different offsets of order \(n^{-2}\) around the giant-component transition. At the precise critical value \(p=1/n\), these cross-covariances converge to finite, generally strictly negative constants, despite the vanishing leading-order covariance on the \(n\)-scale.

## Assumptions and scope
The number of vertices \(n\) is an integer, \(h,k\) are distinct positive integers, and \(h+k\le n\). The edge parameter satisfies \(0<p<1\). An occurrence of \(H\) is an entire connected component, not an induced but externally connected copy. For an integer \(a\ge k\), \((a)_{\underline{k}}=a(a-1)\cdots(a-k+1)\). At these parameters both means in (1) are strictly positive. Equation (4) fixes both component sizes while \(n\to\infty\); it makes no uniform claim for component sizes growing with \(n\). Internal connected graphs may be trees, unicyclic, or of greater excess. The critical finite limit in (4) concerns total size counts; larger-excess shapes contribute negligibly for fixed sizes.

## Proof
For a fixed vertex set \(S\) of size \(h\), let \(A_S\) denote the event that \(S\) spans a connected component isomorphic to \(H\). If \(a_H=h!/|\operatorname{Aut}(H)|\) and \(e(H)\) is the edge count, independence gives
\[
\Pr(A_S)=a_H p^{e(H)}(1-p)^{\binom h2-e(H)+h(n-h)},\qquad
\mu_H=\binom nh\Pr(A_S). \tag{5}
\]
Fix disjoint vertex sets \(S,T\) of sizes \(h,k\). The only edges constrained by both events, rather than independently, are the \(hk\) absent edges between \(S\) and \(T\). It follows exactly that
\[
\Pr(A_S\cap B_T)=\Pr(A_S)\Pr(B_T)(1-p)^{-hk}.
\]
Intersecting sets cannot both constitute distinct connected components. Summing over ordered disjoint \((S,T)\) gives
\[
\mathbb E(C_H C_K)=\mu_H\mu_K\frac{\binom{n-h}{k}}{\binom nk}(1-p)^{-hk},
\]
which proves (1), including the full cross-shape outer-product law. The bracket in (1) is strictly increasing in \(p\) from a negative value to infinity; solving its single root proves (2) and the exact sign classification.

To compare thresholds, take logarithms of (2):
\[
-\log(1-p^*_{n;h,k})=\frac1{hk}\sum_{a=0}^{h-1}\sum_{b=0}^{k-1}
\log\left(\frac{n-a-b}{n-a-b-1}\right). \tag{6}
\]
The summand is strictly increasing in \(a+b\). Appending a new last row or column to this rectangular average increases the average strictly, and \(1-e^{-x}\) is strictly increasing. Therefore the thresholds increase with either admissible size. A Taylor expansion of the finite products gives
\[
-\log(1-p^*_{n;h,k})=\frac1n+\frac{h+k-1}{2n^2}+O_{h,k}(n^{-3}),
\]
which implies (3).

For fixed \(j\), the expected number of size-\(j\) components is
\[
\mathbb EX_j=\binom nj q_j(p)(1-p)^{j(n-j)},\qquad
q_j(p)=\Pr(G(j,p)\text{ is connected}).
\]
In the regime \(p=c/n+O(n^{-2})\), Cayley's enumeration of trees gives \(q_j(p)=j^{j-2}p^{j-1}+O_j(p^j)\), including \(q_1(p)=1\), so \(\mathbb EX_j=n\tau_j(c)+O_j(1)\). For \(p=n^{-1}+\lambda n^{-2}\), expansion of the exact covariance bracket in (1) gives
\[
\frac{(n-h)_{\underline{k}}}{(n)_{\underline{k}}}(1-p)^{-hk}-1
=\frac{hk}{n^2}\left[\lambda-\frac{h+k-2}{2}\right]+O_{h,k,\lambda}(n^{-3}).
\]
Summing equation (1) over all connected shapes of order \(h\) and \(k\), then multiplying by the two first-moment asymptotics, yields (4). No limiting independence assumption is used.

## Verification
The included `verify_component_covariance.py` enumerates every labeled graph for \(n=3,4,5,6\) at probabilities \(1/4,1/2,3/4\), computes exact rational probabilities for component count profiles, and checks the predicted two-component moment for every co-occurring pair of different sizes. It also checks finite threshold inequalities numerically for sizes through \(n=27\). The script prints `PASS 8676 exact pair-moment and numeric threshold checks`. These finite checks are consistency evidence only: the proof above establishes the unrestricted finite-size and fixed-size limiting statements.

## Relationship to prior work
Pittel's 1990 tree census treats asymptotic jointly Gaussian tree-component-size counts for \(G(n,c/n)\) and gives a model-dependent leading covariance kernel. The leading \(n\)-order limit away from \(c=1\) is therefore background, not asserted as new. The precise **finite-\(n\) cross-shape rank-one structure, its strictly ordered all-\(p\) covariance zeros, and the nontrivial \(n^{-2}\) critical crossover constants** are the contributions evaluated here. Janson, Knuth, Łuczak and Pittel provide general component-enumeration generating functions and joint distributions for the fixed-edge critical process, which may implicitly encode some of the finite component-moment identities. Bhamidi, Budhiraja and Wang's work on barely subcritical bounded-size rules supplies a probability-classified archival reference for the phase-transition setting, not direct proof of (1)–(4).

## Limitations
These formulas concern an independent-edge \(G(n,p)\) model, distinct component sizes, and feasible size pairs. The same-size diagonal covariance includes self-pair contributions and requires a different statement. Finite numerical checks do not certify all \(n\). The exact factorial-moment identity is a classical combinatorial ingredient, and general historical generating-function frameworks may imply parts of this theorem without the specific statement. The full 1990 Pittel paper was unavailable during the comparison; its detailed covariance calculations remain a priority risk. There is no independent historical-priority certification or independent mathematical audit.

## References
1. B. Pittel, *On tree census and the giant component in sparse random graphs*, Random Structures & Algorithms 1 (1990), 311–342, doi:10.1002/rsa.3240010306.
2. S. Janson, D. E. Knuth, T. Łuczak, and B. Pittel, *The birth of the giant component*, Random Structures & Algorithms 4 (1993), 233–358; arXiv:math/9310236v1 (public 1993-10-01), https://arxiv.org/pdf/math/9310236.
3. S. Bhamidi, A. Budhiraja, and X. Wang, *Bounded-size rules: the barely subcritical regime*, arXiv:1212.5480v1 (public 2012-12-21), https://arxiv.org/pdf/1212.5480. Its arXiv manuscript lists 60C05 as a primary mathematical subject classification.
