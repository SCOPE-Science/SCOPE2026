# Root-degree and fringe-size covariance switch sign at the square-root scale

## Finding

Consider a uniform random recursive tree \(T_n\) on labels \(\{1,\ldots,n\}\): each vertex \(j\ge2\) independently chooses a parent \(P_j\) uniformly from \(\{1,\ldots,j-1\}\). Let \(R_n\) be the number of children of root \(1\), and let \(F_{n,k}\) count nonroot vertices whose descendant subtree, including themselves, has size \(k\). For every integer \(n\ge3\) and \(2\le k<n\),
\[
\boxed{\operatorname{Cov}(R_n,F_{n,k})=\frac1k\left(1-\frac{n}{k+1}\sum_{j=n-k}^{n-1}\frac1j\right).}
\]
Define the increasing sequence and its first nonnegative-crossing rank by
\[
b_{n,k}=\frac{n}{k+1}\sum_{j=n-k}^{n-1}\frac1j,\qquad
\kappa_n=\min\{1\le k<n:b_{n,k}\ge1\}.
\]
The covariance is positive for \(1\le k<\kappa_n\), nonpositive at \(k=\kappa_n\), and strictly negative for \(\kappa_n<k<n\). The transition occurs at the same square-root scale as the marginal Poisson/normal change of fringe-size counts, but its exact position is new:
\[
\boxed{\lim_{n\to\infty}\frac{\kappa_n}{\sqrt n}=\sqrt2.}
\]
Whenever integers \(k_n/\sqrt n\to c\in(0,\infty)\),
\[
\boxed{\lim_{n\to\infty}n\operatorname{Cov}(R_n,F_{n,k_n})=c^{-2}-\tfrac12.}
\]
The formula extends to \(k=1\), where it gives the previously established covariance between the root degree and the total leaf count, \((n-2)/(2(n-1))\). That boundary case is not a novelty claim.

## Assumptions and scope

All trees are unordered, rooted at vertex \(1\), and distributed by independent uniform attachment. Fringe subtrees are descendants in this rooted tree, not arbitrary induced subgraphs. The relevant ranges are \(n\ge3\) and integers \(2\le k<n\), with \(k=1\) used only to describe the boundary. The covariance is unconditional and uses counts rather than normalized frequencies. All asymptotic assertions have \(n\to\infty\). No assumption of independence between \(R_n\) and \(F_{n,k}\) is made.

## Proof

Write \(S_v\) for the size of the descendant subtree rooted at a fixed \(v\ge2\), and write \(H_m=\sum_{j=1}^{m}j^{-1}\), \(H_0=0\). The descendants of \(v\) form a two-color Pólya urn after the arrival of \(v\): initially the subtree contains one vertex and the complement contains \(v-1\) vertices; subsequent arrivals choose the subtree in proportion to its current size. Its beta-binomial distribution yields, for \(2\le v\le n-k+1\),
\[
\Pr(S_v=k)=p_{v,k}
=\frac{(v-1)(n-k-1)!(n-v)!}
{(n-1)!(n-v-k+1)!},
\]
and the probability is zero when \(v>n-k+1\).

Crucially, condition on any fixed sequence of subtree-versus-complement attachment decisions after \(v\) that produces \(S_v=k\). Before \(v\), the expected number of attachments to the root is \(H_{v-2}\), independent of this future subtree-membership sequence. At the arrival of \(v\), its parent is the root with probability \(1/(v-1)\), independently of future membership decisions. An arriving vertex in the existing subtree cannot attach to the root. For each arriving vertex outside it, conditional on choosing the complement, its parent is uniform on the complement, which has size \(v-1+t\) for successive integers \(t=0,\ldots,n-v-k\). Thus the conditional expected number of later root attachments is
\[
\sum_{t=0}^{n-v-k}\frac1{v-1+t}=H_{n-k-1}-H_{v-2}.
\]
Since the expression is independent of the sequence of subtree-membership decisions, averaging over them gives the exact identity
\[
\mathbb E[R_n\mid S_v=k]=H_{n-k-1}+\frac1{v-1}.
\tag{1}
\]
In particular, this conditioning does not require the within-subtree shapes or the attachment positions of other vertices to be fixed.

To sum over \(v\), put \(r=k-1\), \(t=n-v\), and use the factorial-binomial identity
\[
\sum_{t=r}^{n-2}(n-1-t)\binom tr=\binom n{r+2},
\qquad
\sum_{t=r}^{n-2}\binom tr=\binom{n-1}{r+1}.
\]
Substitution in the displayed formula for \(p_{v,k}\) yields
\[
\sum_{v=2}^{n-k+1}p_{v,k}=\frac n{k(k+1)},
\qquad
\sum_{v=2}^{n-k+1}\frac{p_{v,k}}{v-1}=\frac1k.
\tag{2}
\]
As \(F_{n,k}=\sum_{v=2}^{n}\mathbf1\{S_v=k\}\), equations (1)–(2) imply
\[
\mathbb E[F_{n,k}]=\frac n{k(k+1)},\qquad
\mathbb E[R_nF_{n,k}]=\frac{nH_{n-k-1}}{k(k+1)}+\frac1k.
\]
The independent-parent construction also gives \(\mathbb E R_n=H_{n-1}\). Subtracting the product of means proves the covariance formula, using \(H_{n-1}-H_{n-k-1}=\sum_{j=n-k}^{n-1}j^{-1}\).

For the sign classification, write \(S_k=\sum_{j=n-k}^{n-1}j^{-1}\). Whenever \(1\le k\le n-2\),
\[
 b_{n,k+1}-b_{n,k}
=\frac{n}{(k+1)(k+2)}\left(\frac{k+1}{n-k-1}-S_k\right)>0,
\]
because \(S_k\le k/(n-k)<(k+1)/(n-k-1)\). Furthermore \(b_{n,1}=n/[2(n-1)]<1\) for \(n\ge3\), whereas \(b_{n,n-1}=H_{n-1}>1\). Hence the crossing rank \(\kappa_n\) exists, and the exact covariance formula gives the stated signs and possible zero at the crossing.

Finally, uniformly when \(k=O(\sqrt n)\) with \(k\ge1\), expanding \(1/(n-j)\) gives
\[
\sum_{j=1}^{k}\frac1{n-j}=\frac kn+\frac{k(k+1)}{2n^2}+O\!\left(\frac{k^3}{n^3}\right),
\]
and therefore
\[
 b_{n,k}=\frac{k}{k+1}+\frac{k}{2n}+O\!\left(\frac{k^2}{n^2}\right),
\qquad
\operatorname{Cov}(R_n,F_{n,k})
=\frac1{k(k+1)}-\frac1{2n}+O\!\left(\frac{k}{n^2}\right).
\]
If \(k_n/\sqrt n\to c\in(0,\infty)\), multiplying the covariance identity by \(n\) gives \(c^{-2}-1/2\). For every fixed \(\varepsilon\in(0,\sqrt2)\), the two sequences \(k=\lfloor(\sqrt2-\varepsilon)\sqrt n\rfloor\) and \(k=\lceil(\sqrt2+\varepsilon)\sqrt n\rceil\) lie respectively below and at-or-above the unique crossing for all sufficiently large \(n\). Squeezing and letting \(\varepsilon\downarrow0\) proves \(\kappa_n/\sqrt n\to\sqrt2\).

## Verification

The standalone Python 3 script `CHECK.py` uses exact fractions and enumerates all \((n-1)!\) recursive-tree parent sequences for \(2\le n\le9\). It compares the per-vertex subtree-size distribution, the conditional expected root degree, fringe-size marginal means, mixed covariances, and the deterministic profile-sum identity with their predicted rational values. It additionally checks monotonicity and crossing behavior for all \(3\le n\le500\), and evaluates larger ranks as numerical diagnostics. A successful run reports `CHECK_OK` and totals 46,233 enumerated trees, 412 enumeration identities, and 376,239 further rational comparisons. The finite checker is reproducibility evidence, not a substitute for the all-size proof above.

## Relationship to prior work

Feng, Mahmoud and Panholzer (2008) analyzed the distribution of the marginal fringe-size count across a square-root normal-to-Poisson transition. Holmgren and Janson (2014), Theorem 1.4 and Remark 1.6, give exact marginal fringe-size expectations and the same asymptotic boundary; Theorems 1.13–1.15 give covariance statements between two aggregate fringe-count functionals, while Section 8.1 counts degrees over all vertices. Those assertions do not specify the covariance of a distinguished root's degree with the fringe-size profile. Devroye and Janson (2013) analyze protected nodes and fringe tree distributions, without that distinguished-root mixed moment in the inspected relevant sections. The single-size \(k=1\) root-degree/leaf covariance is already established and not a novelty claim here.

The main difference is the exact mixed root-versus-fringe profile for all \(k\ge2\), including a sign transition and a limiting covariance that locate the dependence crossover at \(\sqrt{2n}\), not merely the marginal normal/Poisson crossover at order \(\sqrt n\).

## Limitations

Only uniform random recursive trees are covered; neither binary search trees nor nonuniform attachment rules are covered. An equivalent mixed moment might be implicit in older multivariate generating functions, especially the earlier subtree-variation literature whose complete article text was not accessible during this comparison; absolute bibliographic uniqueness is not established. The theorem gives a covariance profile, not a joint limit distribution or a conditional independence statement. The boundary case \(k=1\) is not claimed as new, and exact enumeration is not a proof for arbitrary sizes.

## References

- Q. Feng, H. M. Mahmoud, A. Panholzer, *Phase Changes in Subtree Varieties in Random Recursive and Binary Search Trees*, SIAM Journal on Discrete Mathematics **22** (2008), 160–184, DOI: `10.1137/060653950` (online 15 February 2008).
- L. Devroye, S. Janson, *Protected nodes and fringe subtrees in some random trees*, arXiv:`1310.0665v1` (2 October 2013).
- C. Holmgren, S. Janson, *Limit Laws for Functions of Fringe trees for Binary Search Trees and Recursive Trees*, arXiv:`1406.6883v1` (26 June 2014), primary MSC 60C05; especially Theorems 1.4 and 1.13–1.15 and Section 8.1.
