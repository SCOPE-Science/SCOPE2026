# Exact discounted hitting domination and optimizer phase transitions on clique windmills

## Finding

Let \(m,q\ge2\) be integers and let \(W_{m,q}=K_1\vee(\bigsqcup_{j=1}^{m}K_q)\), the graph of \(m\) complete \((q+1)\)-vertex blocks meeting in one hub. Consider simple random walk with homogeneous discount \(0<\lambda<1\). For a nonempty source set \(S\), define \(h_v(S)=\mathbb E_v[\lambda^{T_S}]\), where \(T_S\) is the first time the walk hits \(S\), and let \(\delta_{\lambda,\tau}(G)\) be the smallest \(|S|\) such that \(h_v(S)\ge\tau\) for every vertex, where \(0<\tau\le1\).

Define the strictly increasing level sequence
\[
 b_{-1}=0,\qquad
 b_s=\frac{\lambda(s+1)}{q-\lambda(q-s-1)}\quad(0\le s<q),\qquad b_q=1.
\]
There is exactly one \(r\in\{0,\ldots,q\}\) with \(b_{r-1}<\tau\le b_r\). The exact discounted hitting domination number is
\[
 \boxed{\delta_{\lambda,\tau}(W_{m,q})=1+mr.}
\]
For \(r<q\), set
\[
 u_s=\frac{\lambda(q-s)}{q-\lambda(q-s-1)},\qquad
 v_s=s+\frac{\lambda s(q-s)}{q-\lambda(q-s-1)}\quad (0\le s<q),
 \qquad(u_q,v_q)=(0,q),
\]
\[
 X_{m,q,r}=\frac{\lambda[(m-1)v_r+v_{r+1}]}{mq-\lambda[(m-1)u_r+u_{r+1}]},\qquad
 \vartheta_{m,q,r}=\frac{\lambda(X_{m,q,r}+r)}{q-\lambda(q-r-1)}.
\]
The threshold is always strictly internal: \(b_{r-1}<\vartheta_{m,q,r}<b_r\). All minimum source sets are exactly of the following types:

1. The hub together with precisely \(r\) vertices from each complete peripheral block, for every \(r\in\{0,\ldots,q\}\).
2. If \(r<q\) and \(\tau\le\vartheta_{m,q,r}\), sets omitting the hub, with \(r+1\) vertices in exactly one peripheral block and \(r\) in each other block.

Thus the number \(\mathcal N_{m,q}(\lambda,\tau)\) of minimum source sets equals
\[
 \mathcal N_{m,q}(\lambda,\tau)=
 \begin{cases}
 \binom qr^m+\mathbf1_{\{\tau\le\vartheta_{m,q,r}\}}\,m\binom q{r+1}\binom qr^{m-1},&r<q,\\
 1,&r=q.
 \end{cases}
\]
In each fixed-cardinality plateau \(b_{r-1}<\tau\le b_r\), the number and hub membership of optimal placements change at the additional, explicit threshold \(\vartheta_{m,q,r}\), while the optimal cardinality does not.

## Assumptions and scope

All graphs are finite, undirected, simple and unweighted. The \(m\) peripheral cliques are disjoint except for their common hub, and \(m,q\ge2\) throughout. The random walk chooses each neighbor uniformly. The discount is the same at every vertex and lies strictly between zero and one; the coverage threshold lies in \((0,1]\). A source is pinned at support one, so \(h_v(S)=1\) for \(v\in S\). Empty source sets are excluded. The result concerns the exact uniform-floor source placement invariant and the full census of its minimum sets, not expected hitting times without discount or a different walk kernel.

## Proof

**1. Equilibrium in a block.** If the hub has support \(x\) and exactly \(s\) of a peripheral clique's \(q\) vertices are pinned, then, for \(0\le s<q\), the other \(q-s\) vertices have a common support \(y_s(x)\). Every peripheral vertex has degree \(q\), so first-step conditioning gives
\[
 y_s(x)=\frac\lambda q\{x+s+(q-s-1)y_s(x)\}
 =\frac{\lambda(x+s)}{q-\lambda(q-s-1)}.
\]
The sum of supports in that clique is \(F_s(x)=s+(q-s)y_s(x)=u_sx+v_s\); when \(s=q\), all vertices are pinned and \(F_q=q\). For \(x\in[0,1]\) and \(s<q\), the expression \(y_s(x)\) strictly increases with \(s\), including the comparison with a fully pinned clique. This follows by taking the difference of neighboring rational expressions, whose numerator has the positive factor \(q-\lambda(q-1+x)\). In particular \(y_s(1)=b_s\). Moreover, \(b_s\) strictly increases because its continuous interpolation has positive derivative \(\lambda q(1-\lambda)/(q-\lambda(q-1)+\lambda s)^2\), and \(b_{q-1}=\lambda<1=b_q\).

**2. The hub-containing upper bound.** With the hub pinned, each clique is independent of the others and feasibility requires at least \(r\) pinned peripheral vertices in every clique: \(s<r\) leaves a vertex with support \(b_s<\tau\), while \(s=r\) suffices, or \(r=q\) pins the entire clique. This proves that hub-containing feasible sets have size at least \(1+mr\), and exactly \(\binom qr^m\) such sets attain it.

**3. The global lower bound.** Suppose the hub is not pinned. Since the hub has support \(x\le1\), every clique must still contain at least \(r\) sources by \(y_s(x)\le y_s(1)\). When \(r=q\), all \(mq\) peripheral vertices must be pinned, but then the unpinned hub has support \(\lambda<\tau\), so no hub-free feasible set exists. When \(r\ge1\) and the total source count is at most \(mr\), every clique must have exactly \(r\) sources. In that uniform configuration, all unpinned vertices, including the hub, have the same support \(x_0\); substituting into the hub and peripheral equations yields
\[
 x_0=\frac{\lambda r}{q-\lambda(q-r)}=b_{r-1}<\tau.
\]
Thus a hub-free feasible set needs at least \(mr+1\) sources. When \(r=0\), nonemptiness already gives the same lower bound of one. The construction in Step 2 proves the claimed global value in every case.

**4. The only possible hub-free optima.** Assume \(r<q\). An optimal hub-free set has \(mr+1\) sources and at least \(r\) in each clique, so precisely one clique must contain \(r+1\) sources and each remaining clique exactly \(r\). Let \(X\) denote the hub support in such a configuration. By the hub's degree \(mq\) and the block sums computed in Step 1,
\[
 X=\frac{\lambda}{mq}\bigl((m-1)(u_rX+v_r)+u_{r+1}X+v_{r+1}\bigr),
\]
whose unique solution is \(X_{m,q,r}\). The denominator is positive because the hub equation is a strict contraction: \(0\le\lambda[(m-1)u_r+u_{r+1}]/(mq)<1\). All unpinned peripheral vertices in an ordinary clique have support \(y_r(X)\); those in the exceptional clique, if any, have the larger support \(y_{r+1}(X)\). The hub itself has support \(X\).

To order these values, consider the uniform configuration with \(r\) sources in *every* clique and hub unpinned. Its hub support is \(x_0=b_{r-1}\), with \(x_0=0\) if \(r=0\). Adding one newly pinned peripheral vertex strictly increases the hub's discounted hitting potential: there is positive probability of first reaching this added vertex before any old source, and an unpinned vertex has potential strictly below one. Therefore \(X>x_0\). Since \(y_r(x_0)=x_0\) and the slope of \(y_r\) is \(\lambda/[q-\lambda(q-r-1)]\in(0,1)\), we have
\[
 b_{r-1}=x_0<y_r(X)<X<1,
 \qquad y_r(X)<y_r(1)=b_r.
\]
Thus the least support in the hub-free candidate equals \(y_r(X)=\vartheta_{m,q,r}\), and it meets the floor precisely when \(\tau\le\vartheta_{m,q,r}\). This also proves both strict threshold inequalities.

**5. Census.** The hub-containing minimum sets choose \(r\) from each clique, giving \(\binom qr^m\). A hub-free minimum set, when feasible, chooses its unique exceptional clique in \(m\) ways, chooses \(r+1\) of its \(q\) vertices, and chooses \(r\) in each other clique. Their count is \(m\binom q{r+1}\binom qr^{m-1}\), with disjoint cases. For \(r=q\), the only minimum set is the entire vertex set. This proves the formula and exhausts all cases.

## Verification

The independent program `verify.py` builds the windmill adjacency matrix, solves the pinned discounted equilibrium equations by exact rational Gaussian elimination for **every nonempty source subset**, and compares the smallest feasible cardinality, the complete optimizer count, and the count of hub-free optimizers to the formulas above. It tests \((m,q)=(2,2),(3,2),(2,3),(3,3),(2,4)\), discounts \(\lambda\in\{1/2,4/5\}\), and a total of 132 threshold cases including all algebraic transition points and intervals between them. It prints `TOTAL_EXACT_OK 132` upon success. These finite tests corroborate rather than establish the universal quantified theorem, which follows from Steps 1–5.

As a sharp example, take \(m=2\), \(q=4\), and \(\lambda=4/5\). On \(1/2<\tau\le2/3\), exactly three sources are necessary. There are 64 optimum placements for \(1/2<\tau\le9/17\), but only 16 for \(9/17<\tau\le2/3\); the 48 hub-free optima cease to be feasible at the exact internal threshold \(9/17\).

## Relationship to prior work

Allagan, Pereyra and Massey (arXiv:2609.31535v1, first public September 25, 2026) introduced discounted hitting domination and derived structural results for spiders, stars and complete graphs, plus general algorithmic formulations. The present graph consists of cliques sharing a hub; for \(q\ge2\) it is neither a spider nor a complete graph. The precise two-level optimizer phase diagram and source-set census here are not stated in that paper. The definition of the random-walk quantity, its Markov interpretation and general equilibrium existence are credited to that work; no new definition of discounted hitting support is claimed.

Guo et al. (2024) study evaluation and ranking queries for *group hitting probability* with a fixed starting vertex, not minimization of target-set cardinality subject to a simultaneous floor on all vertices. A separately available exact result for complete bipartite graphs concerns a different graph class; other results on windmill graphs address different invariants, including dissociation. None of these checked statements implies the cardinality **and** optimizer classification above. Searches covered the equivalent descriptions “windmill,” “friendship” and “clique bouquet,” together with “pinned source placement,” “group hitting probability” and “discounted hitting domination.”

## Limitations

The result requires equal clique sizes, unweighted simple random walk, and homogeneous scalar discount. Heterogeneous block sizes, weighted/directed kernels, and arbitrary block graphs are not covered. Only the numerical examples use finite exhaustive computation; the universal statement depends on the displayed analytic proof. Novelty comparisons cannot exclude unpublished or unindexed results using different terminology, and no independent external audit has been performed.

## References

1. J. D. Allagan, K. Pereyra and W. A. Massey, “Discounted Hitting Domination on Graphs with Submodularity, Complexity and Exact Algorithms,” arXiv:2609.31535v1 (first public September 25, 2026), https://arxiv.org/pdf/2609.31535v1 .
2. Q. Guo, D. Lin, S. Wang, R. C.-W. Wong and W. Lin, “Efficient Algorithms for Group Hitting Probability Queries on Large Graphs,” *IEEE Transactions on Knowledge and Data Engineering* 36 (2024), 2995–3008, DOI:10.1109/TKDE.2023.3349164, https://www.cse.ust.hk/~raywong/paper/tkde24-GroupHittingProb.pdf .
