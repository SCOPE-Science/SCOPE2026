# Sharp branching sign transition for singleton–doubleton covariance in tree percolation

## Finding

In Bernoulli bond percolation on a finite tree, let \(I\) count singleton connected components and \(J\) count connected components consisting of precisely two vertices. The dependence between these two small-cluster counts distinguishes stars from stars whose edges are all subdivided once, at **every** edge-retention probability, not just asymptotically.

**Theorem.** Let \(p\in(0,1)\) be the common independent edge-retention probability and put \(q=1-p\). For the star \(K_{1,k}\) with \(k\ge2\) leaves,
\[
\operatorname{Cov}(I,J)=kpq^{k-1}\big((k-1)-kq-q^k\big).
\]
There is exactly one \(q_k\in(0,1)\) with \((k-1)-kq_k-q_k^k=0\); the covariance is positive precisely when \(p>1-q_k\), negative when \(p<1-q_k\), and zero at equality.

Let \(S_k\) be the tree formed from \(K_{1,k}\) by subdividing **every** edge exactly once, so that \(S_k\) has \(2k+1\) vertices. Then
\[
\operatorname{Cov}(I,J)=kp\big[-q^{2k}-q^{k+2}+p((k-1)q^{k+1}+2q^k)-q^3-q^2\big].
\]
On the path \(S_2=P_5\), this covariance is positive for \(p>2/3\), zero at \(p=2/3\), and negative for \(p<2/3\). On **every** branching member \(S_k\), \(k\ge3\), it is strictly negative for all \(p\in(0,1)\). Thus the transition at exactly three equally subdivided arms is sharp.

For example, at \(p=1/2\) the star \(K_{1,3}\) has covariance \(9/64>0\) while the corresponding once-subdivided three-arm star has covariance \(-45/128<0\).

## Assumptions and scope

All graphs are finite simple trees, including the explicit families \(K_{1,k}\) and \(S_k\). The random spanning forest is formed by retaining each original edge independently with the **same** probability \(p\in(0,1)\). A singleton is a component with exactly one vertex; a doubleton is a component with exactly two vertices, not a pair of isolated vertices and not any retained edge belonging to a larger component. Component-count variables count components once each.

For a vertex \(v\) write \(d_v\) for its original degree, and \(N(v)\) for its original neighbor set. When \(uv\) is an edge of a tree, define \(W_{uv}=(N(u)\cup N(v))\setminus\{u,v\}\). In a tree, each \(w\in W_{uv}\) is adjacent to exactly one endpoint of \(uv\).

## Proof

**1. An identity for every tree.** Write \(X_w\) for the indicator that vertex \(w\) is isolated in the retained forest, and \(Y_{uv}\) for the indicator that edge \(uv\) is retained and forms its own two-vertex component. Thus \(I=\sum_wX_w\) and \(J=\sum_{uv\in E(T)}Y_{uv}\). Independence gives
\[
\mathbb E X_w=q^{d_w},\qquad \mathbb E Y_{uv}=pq^{d_u+d_v-2}.
\]
If \(w\in\{u,v\}\), then \(X_wY_{uv}=0\), yielding covariance \(-pq^{d_u+d_v-2+d_w}\). If \(w\in W_{uv}\), conditioning on \(Y_{uv}=1\) has already forced closed the single edge from \(w\) to \(\{u,v\}\). Hence \(\Pr(X_w=1\mid Y_{uv}=1)=q^{d_w-1}\), and the covariance is \(pq^{d_u+d_v-2}\cdot pq^{d_w-1}\). For every other vertex the edge conditions are disjoint, so the indicators are independent. Summing over all vertices and original edges proves the exact finite-tree identity
\[
\boxed{\operatorname{Cov}(I,J)=\sum_{uv\in E(T)}pq^{d_u+d_v-2}\left[-q^{d_u}-q^{d_v}+\frac pq\sum_{w\in W_{uv}}q^{d_w}\right].}
\]
All exponents are nonnegative integers and \(q>0\); the formula therefore applies at every stated \(p\).

**2. The star.** The star has a hub of degree \(k\) and \(k\) degree-one leaves. For each of its \(k\) edges, the neighborhood correction consists of \(k-1\) leaves. Substitution gives
\[
\operatorname{Cov}(I,J)=kpq^{k-1}\left[-q^k-q+\frac pq(k-1)q\right]
=kpq^{k-1}\big((k-1)-kq-q^k\big).
\]
The sign-controlling factor \(f_k(q)=(k-1)-kq-q^k\) is strictly decreasing on \([0,1]\), with \(f_k(0)=k-1>0\) and \(f_k(1)=-2<0\). It consequently has exactly one zero \(q_k\), and the claimed sign classification follows.

**3. Equal-arm once-subdivided stars.** In \(S_k\), the center has degree \(k\), the \(k\) intermediate vertices degree \(2\), and the \(k\) leaves degree \(1\). Each center-to-intermediate edge contributes
\[
pq^k\left[-q^k-q^2+\frac pq\big((k-1)q^2+q\big)\right],
\]
and each intermediate-to-leaf edge contributes
\[
pq\left[-q^2-q+\frac pq q^k\right]
\]
to the boxed identity. There are \(k\) edges of each type. Adding and using \(p=1-q\) gives the displayed formula \(\operatorname{Cov}(I,J)=kpB_k(q)\), with
\[
B_k(q)=-q^{2k}-q^{k+2}+(1-q)\big((k-1)q^{k+1}+2q^k\big)-q^3-q^2.
\]
For \(k=2\), direct factorization yields \(B_2(q)=-q^2(1+q)(3q-1)\). Since \(kp>0\) and \(q\in(0,1)\), this proves the exact \(p=2/3\) sign transition.

For all \(k\ge3\), division by \(q^2>0\) yields
\[
\frac{B_k(q)}{q^2}=-1-q-q^k-q^{2k-2}+2q^{k-2}(1-q)+(k-1)q^{k-1}(1-q).
\]
Since \(q^{k-2}\le q\), \(2q(1-q)\le 1/2\), and
\[
(k-1)q^{k-1}(1-q)\le \left(\frac{k-1}{k}\right)^k<e^{-1},
\]
we have \(B_k(q)/q^2<-1+1/2+e^{-1}<0\). This proves strict negativity for every integer \(k\ge3\) and every real \(0<q<1\), completing the theorem.

## Verification

The accompanying `verify_cluster_cov.py` uses only the Python standard library and exact rational arithmetic. It independently enumerates every retained-edge configuration of every labeled tree with \(2\le n\le6\), using all Prüfer words, for retention probabilities \(1/3\) and \(1/2\) (2,882 tests). It separately tests both families at four rational probabilities through \(k=7\), with full configuration enumeration through \(k=6\) for the once-subdivided family, and checks a larger finite sign grid. Output ends in `VERIFY_OK`. These are finite checks; the proof in the preceding section is uniform in \(p\), \(k\), and finite trees for the local formula.

## Relationship to prior work

Berzunza and Holmgren, *The asymptotic distribution of cluster sizes for supercritical percolation on random split trees* (arXiv:2003.12018, first public version 2020-03-26), examine asymptotic largest-cluster sizes in a random-tree percolation regime; the present theorem concerns **joint small-cluster count dependence** on two **deterministic** tree families with fixed \(p\). Allard, Hébert-Dufresne, Young, and Dubé, *General and exact approach to percolation on random graphs* (arXiv:1509.01207, 2015), give a general method for rooted **component-size distributions** on finite random graphs. Their finite-graph recurrence supplies related marginal probabilities, but its stated results are not a sign theorem for covariance of **two global component counts**, nor a classification for subdivided stars. Exhaustive edge-state computation is of course possible for any fixed tree; the contribution here is a finite closed form and a sharp **all-parameter** branching sign boundary, not the ability to enumerate states.

## Limitations

No claim is made about all possible trees having a common covariance sign, about nonuniform bond probabilities, about clusters of size three or more, or about uniqueness relative to uninspected historical publications. The expressions are for exactly the stated families (plus the general local identity). Broad graph-component enumeration theory could permit independent derivation, so priority remains subject to further literature verification. The rational finite checks are not substituted for the unrestricted proof.

## References

1. G. Berzunza and C. Holmgren, *The asymptotic distribution of cluster sizes for supercritical percolation on random split trees*, arXiv:2003.12018 (first posted 2020-03-26), https://arxiv.org/abs/2003.12018.
2. A. Allard, L. Hébert-Dufresne, J.-G. Young, and L. J. Dubé, *General and exact approach to percolation on random graphs*, arXiv:1509.01207 (first posted 2015-09-03), https://arxiv.org/abs/1509.01207.
