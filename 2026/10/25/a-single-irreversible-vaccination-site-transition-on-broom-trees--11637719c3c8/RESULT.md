# A single irreversible vaccination-site transition on broom trees

## Finding

For integers \(k\ge2\), \(L\ge1\), let \(B_{k,L}\) be the tree formed by adjoining \(k\) pendant leaves to one endpoint \(o\) of the path \(o,v_1,\ldots,v_L\). Protect exactly one vertex perfectly before an epidemic. Each edge between unprotected vertices independently transmits with probability \(p\in(0,1)\), and the single epidemic seed is drawn uniformly among the \(k+L\) unprotected vertices. The outbreak is the seed's component in the random open-edge subgraph. Let \(R_v(p)\) be the expected outbreak size when vertex \(v\) is protected.

**Theorem (sharp switch and asymptotic critical transmissibility).** Write \(d=L-k\). Protecting the hub \(o\) uniquely minimizes \(R_v(p)\) for every \(p\in(0,1)\) if
\[
d<2\quad\text{or}\quad 2\left\lfloor d^2/4\right\rfloor\le k(k-1).
\]
Otherwise there exists a **unique** \(p_{k,L}\in(0,1)\) such that the hub is the unique optimum below \(p_{k,L}\), ties one or two interior path vertices at \(p_{k,L}\), and is strictly suboptimal above \(p_{k,L}\). The critical values decrease strictly with \(L\) once they exist and satisfy
\[
p_{k,L}\downarrow p_k^\infty,
\]
where \(p_k^\infty\) is the unique root in \((1-1/k,1)\) of
\[
k(k-1)p(1-p)^2=2\bigl[1-k(1-p)\bigr].
\]
For every \(p\), no pendant leaf is optimal. When the hub is suboptimal, the optimal path vertices are read from an explicit unimodal one-dimensional score: set
\[
c=1-k(1-p)>0,\qquad
\theta=\frac{L-1-\log(c)/\log(p)}2.
\]
The minimum among path positions \(1\le t\le L-1\) occurs at \(t=\max\{1,\lceil\theta\rceil\}\), with the adjacent position \(t+1\) also optimal exactly when \(\theta\) is an integer in \(\{1,\ldots,L-2\}\). If the hub is optimal, this path-candidate formula need not be used. The smallest switching broom has \(k=2,L=5\), hence eight vertices; this previously known finite benchmark has critical point the unique root of \(p^3+p^2=1\) in \((0,1)\), approximately \(0.754877666\).

## Assumptions and scope

The graph is finite, simple and undirected. Vertices are labeled, but leaves attached directly to \(o\) are symmetric. Protection removes the vertex and all incident edges. There is precisely one uniformly chosen initial infection among the remaining vertices, and conditional on the seed, the infection reaches exactly its connected component after independent bond percolation. Uniform transmissibility is \(0<p<1\). The theorem is a statement about expected final size, not about infection timing or the full outbreak-size distribution. The boundary \(p=1\) is used only as a limiting comparison. The original graph has \(N=k+L+1\) vertices and the protected graph has \(N-1\).

## Proof

**1. Exact objective.** For a tree \(T\) and protected vertex \(v\), two surviving vertices \(a,b\) are connected in the open-edge graph precisely when every edge on their unique surviving path is open, an event of probability \(p^{\operatorname{dist}_{T-v}(a,b)}\). Therefore the expected outbreak size is
\[
R_v(p)=\frac1{N-1}\sum_{a,b\in V(T)\setminus\{v\}\atop a\leftrightarrow b\text{ in }T-v}p^{\operatorname{dist}_{T-v}(a,b)}.
\]
The sum is over ordered pairs and includes diagonal terms. Denote its numerator by \(S_v(p)\). If \(w\) is a pendant leaf adjacent to \(u\) and \(N\ge3\), then \(S_w(p)>S_u(p)\): each surviving pair not involving \(u,w\) connected after removing \(u\) remains connected after removing \(w\); the latter graph has additional positive connections through \(u\), including an edge from \(u\) to another vertex. Hence no leaf is optimal. It suffices to compare the hub and \(v_t\), \(1\le t\le L-1\).

**2. Exact broom scores and path differences.** Put \(H_r(p)=r+2\sum_{j=1}^{r-1}(r-j)p^j\), the ordered-pair score of a path on \(r\) vertices. Directly splitting the tree at a protected vertex gives
\[
S_o(p)=k+H_L(p),
\]
\[
S_{v_t}(p)=k+H_t(p)+H_{L-t}(p)
+2k\sum_{j=1}^t p^j+k(k-1)p^2.
\]
The \(k(k-1)p^2\) term counts ordered pairs of distinct hub leaves, and the preceding term counts their connections to the hub-side path. The path split identity
\[
H_L-H_t-H_{L-t}=
2p\frac{(1-p^t)(1-p^{L-t})}{(1-p)^2}
\]
counts the severed pairwise paths. Consequently, with \(c(p)=1-k(1-p)\),
\[
D_t(p):=S_{v_t}(p)-S_o(p)
=\frac{2p(1-p^t)(p^{L-t}-c(p))}{(1-p)^2}
+k(k-1)p^2.\tag{1}
\]
The difference between adjacent path scores is
\[
S_{v_{t+1}}-S_{v_t}=
\frac{2p}{1-p}\bigl(p^{L-t-1}-c(p)p^t\bigr),\quad 1\le t\le L-2.\tag{2}
\]
For \(p\le1-1/k\), \(c\le0\), so (1) is strictly positive and the hub is the unique optimum. For \(p>1-1/k\), \(0<c<p<1\); the sign of (2) changes at most once as \(t\) increases, from negative to positive. Solving the equality gives the stated \(\theta\), hence the explicit path minimizer. Reflection of the path contribution and strict growth of \(\sum_{j=1}^t p^j\) imply \(S_{v_t}>S_{v_{L-t}}\) whenever \(t>L/2\). It is therefore enough to consider \(1\le t\le\lfloor L/2\rfloor\).

**3. Every path competitor crosses the hub at most once.** For such \(t\), expand (1) without denominators. The coefficient of \(p^j\) in \(D_t/2\) equals
\[
a_j=k\mathbf1_{\{j\le t\}}+\binom{k}{2}\mathbf1_{\{j=2\}}-h_j,
\qquad h_j=\min\{j,t,L-t,L-j\},\quad 1\le j\le L-1,
\]
where coefficients outside this range are zero apart from the displayed \(p^2\) term. For \(j\le t\), \(h_j=j\), hence the coefficient is \(k-j+\binom{k}{2}\mathbf1_{\{j=2\}}\); for \(j>t\), it is \(-h_j+\binom{k}{2}\mathbf1_{\{j=2\}}\). When \(t=1\), the \(j=2\) coefficient is nonnegative (for \(k\ge2\)); for \(t\ge2\), the additional \(j=2\) contribution is nonnegative. Thus the list of nonzero coefficients, in increasing powers, consists of a positive initial block followed by a (possibly empty) negative block. Descartes' sign rule, applied after reversing coefficient order, gives at most one positive root; it is simple if it exists. Since \(D_t(p)>0\) near \(p=0\), a crossing within \((0,1)\) occurs exactly when \(D_t(1)<0\), and it is then strictly from positive to negative. A zero at \(p=1\) creates no interior crossing.

Taking \(p\to1\) in the finite scores yields
\[
D_t(1)=(k+t)^2+(L-t)^2-(k+L^2)
=k(k-1)+2t(t+k-L).\tag{3}
\]
For \(d=L-k\ge2\), the largest possible \(t(d-t)\) over relevant integers is \(\lfloor d^2/4\rfloor\). If \(d<2\) no positive such product is possible. Formula (3) is negative for at least one admissible path vertex precisely under the strict length inequality in the theorem. Because every path competitor either never beats the hub or begins beating it permanently at its unique root, the minimum of their crossing points is a single global critical transmissibility, with the asserted tie behavior.

**4. Strict length monotonicity and infinite-handle limit.** For a fixed \(t\), lengthening the tail from \(L\) to \(L+1\) decreases \(D_t(p)\) strictly by \(2p^{L-t+1}(1-p^t)/(1-p)\). The previously optimal interior competitor remains admissible, so the critical value strictly decreases whenever both lengths admit one.

For \(p>1-1/k\), rewriting (1) gives
\[
D_t(p)=D_\infty(p)+\frac{2p}{(1-p)^2}
\bigl(p^{L-t}+c(p)p^t-p^L\bigr),
\]
\[
D_\infty(p)=\frac{p}{(1-p)^2}\Bigl(k(k-1)p(1-p)^2-2c(p)\Bigr).
\]
The correction is strictly positive. The bracket defining \(D_\infty\) has a unique zero \(p_k^\infty\in(1-1/k,1)\): under \(u=1-p\in(0,1/k)\), it becomes \(k(k-1)(1-u)u^2+2ku-2\), which is strictly increasing in \(u\), positive at \(u=1/k\), and negative at \(u=0\). Below this root, (1) is positive for every finite \(L,t\); above it, choosing \(t=\lfloor L/2\rfloor\) makes the positive correction tend to zero as \(L\to\infty\), so eventually an interior vertex beats the hub. This proves \(p_{k,L}\downarrow p_k^\infty\). For \(k=2,L=5\), (1) at \(t=1\) simplifies to \(2p(1-p^2-p^3)\); equation (2) shows this path vertex is best among all path competitors, yielding the stated benchmark. \(\square\)

## Verification

A standalone exact-rational checker is included as `verify_broom.py`. It independently enumerates every open/closed edge configuration after deleting each candidate vertex, computes connected-component sizes, and sums the squared component sizes weighted by exact rational probabilities. It compares those values against a separate distance-based implementation and the closed difference identity (1). Checked parameters: \(2\le k\le4\), \(2\le L\le7\), and \(p\in\{1/3,2/3\}\), totaling 306 deleted-vertex enumerations and 126 difference checks. It additionally tests the strict integer length criterion for \(2\le k\le5\), \(3\le L\le25\), and the \(k=2,L=5\) benchmark at six rational transmissibilities. All checks passed. These computations are corroboration; the proof of all \(k,L,p\) is analytical.

## Relationship to prior work

Hall and Siebert's publicly available 2021 preprint (published in 2023) gives exact node-state SIR/SEIR equations on rooted trees with one seed, not the sharp one-vaccine location transition on this tree family. Sartori et al. (2022) compare centrality-based vaccination heuristics across real-world networks, rather than establishing a parameter-exact criterion for which vertex is optimal. Li, Zhao and Zhang (2022) develop site-bond epidemic models and generating-function thresholds for random-network degree distributions, not a deterministic broom's optimal site. Holme (2017) considers exact node-importance expressions for graphs of at most seven vertices, whereas the smallest switching broom here has eight. The pair-connectivity identity on trees and the finite eight-vertex switching benchmark are already known and are not claimed as novel; the contribution is the explicit all-size sharp length boundary, one-way transmissibility switch, optimal interior-site rule, and infinite-handle critical law.

## Limitations

The independent-edge model is not an assertion that arbitrary continuous-time SIR systems have independent edge transmissions. The theorem optimizes only the expected final size after one perfectly protected vertex and one uniformly chosen seed. It does not treat nonuniform edge probabilities, multiple seeds, vaccination costs, multiple vaccines, general trees, or variance of outbreak size. Prior literature in unindexed network-interdiction sources might contain an equivalent tree-vaccination switching theorem; this cannot be ruled out by search alone.

## References

1. C. L. Hall and B. A. Siebert, *Exact solutions and bounds for network SIR and SEIR models using a rooted-tree approximation*, arXiv:2108.07128 (first publicly submitted 2021-08-16); *Journal of Mathematical Biology* 86, 22 (2023). https://arxiv.org/abs/2108.07128 ; https://doi.org/10.1007/s00285-022-01854-9.
2. F. Sartori et al., *A comparison of node vaccination strategies to halt SIR epidemic spreading in real-world complex networks*, *Scientific Reports* 12, 21355 (2022). https://doi.org/10.1038/s41598-022-24652-1.
3. S. Li, X. Zhao and R. Zhang, *Site-bond percolation model of epidemic spreading with vaccination in complex networks*, *Journal of Mathematical Biology* 85, 49 (2022). https://doi.org/10.1007/s00285-022-01816-1.
4. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, *Physical Review E* 96, 062305 (2017). https://doi.org/10.1103/PhysRevE.96.062305.
