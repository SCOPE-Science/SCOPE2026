# An age threshold for degree–leaf covariance in uniform recursive trees

## Finding

A uniform random recursive tree on \(n\ge3\) vertices is built by giving vertex \(t\ge2\) an independently and uniformly selected parent among \(1,\ldots,t-1\). Let \(D_i\) be the **outdegree** (number of children) of vertex \(i\); let \(Y_j=\mathbf 1\{D_j=0\}\), and let \(L=\sum_{j=1}^nY_j\) be the number of **rooted leaves**. The root is not a rooted leaf when \(n\ge2\), regardless of its ordinary undirected degree.

For every pair \(1\le i,j\le n\), put \(m=\max\{i,j\}\). The full cross-covariance matrix is
\[
\operatorname{Cov}(D_i,Y_j)=
\begin{cases}
0,&j=1,\\[2pt]
-\dfrac{j-1}{n-1}\displaystyle\sum_{t=j}^{n-1}\dfrac1t,&i=j\ge2,\\[7pt]
\dfrac{j-1}{n-1}\left(\dfrac1{m-1}-\dfrac1{n-1}\right),&i\ne j,\ j\ge2.
\end{cases}
\tag{1}
\]
The corresponding covariances with the total rooted-leaf count are
\[
\boxed{\operatorname{Cov}(D_1,L)=\frac{n-2}{2(n-1)}}
\tag{2}
\]
and, for every \(2\le i\le n\),
\[
\boxed{a_{n,i}:=\operatorname{Cov}(D_i,L)
=\frac{(n-i)(n-3)}{2(n-1)^2}
-\frac{i-1}{n-1}\sum_{t=i}^{n-1}\frac1t.}
\tag{3}
\]
The empty sum for \(i=n\) is zero.

**Sharp finite-age sign classification.** For each \(n\ge3\), \(a_{n,1}>0\), \(a_{n,n-1}<0\), and \(a_{n,n}=0\). Among nonroot ages \(2,\ldots,n-1\), the signs consist of an initial (possibly empty) positive block, at most one zero, and a nonempty negative block: in particular, if \(a_{n,i}\le0\) for some \(2\le i\le n-1\), then \(a_{n,j}<0\) for all \(i<j<n\). The last vertex has deterministic outdegree zero. For sufficiently large trees, early nonroot labels are positively associated in covariance with global rooted-leaf abundance, whereas late-but-not-last labels are negatively associated; there is no subsequent positive reversal.

For any fixed \(x\in(0,1)\), whenever \(i_n/n\to x\),
\[
\boxed{\lim_{n\to\infty}a_{n,i_n}
=f(x):=\frac{1-x}{2}+x\log x.}
\tag{4}
\]
The function \(f\) has exactly one zero in the open interval \((0,1)\), namely
\[
\boxed{\alpha=0.284668137040838\ldots,\qquad
\frac{1-\alpha}{2}+\alpha\log\alpha=0.}
\tag{5}
\]
It is positive for \(0<x<\alpha\) and negative for \(\alpha<x<1\). Let \(q_n\) be the largest **nonroot** label less than \(n\) with positive degree–leaf covariance, and set \(q_n=1\) if no such label exists (as happens for \(3\le n\le6\)). Then \(q_n/n\to\alpha\).

## Assumptions and scope

All vertices are labeled by their times of birth, \(1,\ldots,n\), and the variables \(P_t\in\{1,\ldots,t-1\}\) giving their parents are mutually independent and uniform. The degree \(D_i=\sum_{t=i+1}^n\mathbf 1\{P_t=i\}\) always means **outdegree**. A rooted leaf has outdegree zero. This differs from counting every graph-theoretic degree-one vertex, where the root can contribute an extra leaf if its outdegree is one. The theorem does not identify these two conventions. Covariance is population covariance under the uniform recursive-tree measure.

## Proof

For \(j\ge2\), vertex \(j\) survives as a rooted leaf precisely when none of the subsequent independent parent choices equals \(j\). Hence
\[
\mathbb E Y_j
=\prod_{t=j+1}^n\left(1-\frac1{t-1}\right)
=\frac{j-1}{n-1},\qquad Y_1=0.
\tag{6}
\]
Write \(A_{t,i}=\mathbf1\{P_t=i\}\). When \(t\le j\), \(A_{t,i}\) and \(Y_j\) are independent; the only relevant times for \(i\ne j\) therefore satisfy \(t>\max\{i,j\}\). At each such time, conditional on \(A_{t,i}=1\), the parent cannot equal \(j\). Removing the factor \(\Pr\{P_t\ne j\}=(t-2)/(t-1)\) from (6) gives
\[
\operatorname{Cov}(A_{t,i},Y_j)
=\frac{j-1}{(n-1)(t-1)(t-2)}.
\tag{7}
\]
By summing (7) over \(t>\max\{i,j\}\) and using
\[
\sum_{t=m+1}^n\frac1{(t-1)(t-2)}
=\frac1{m-1}-\frac1{n-1},
\]
we obtain the off-diagonal branch of (1). When \(i=j\ge2\), the product \(D_jY_j\) vanishes identically, whereas
\(\mathbb ED_j=\sum_{t=j}^{n-1}1/t\); this proves the diagonal branch. The root branch follows from \(Y_1=0\).

Sum (1) over \(j\). For \(i=1\), only the off-diagonal terms occur and
\[
\operatorname{Cov}(D_1,L)
=\sum_{j=2}^n\frac{n-j}{(n-1)^2}
=\frac{n-2}{2(n-1)}.
\]
For \(i\ge2\), the positive contribution from \(2\le j<i\) is
\[
\frac{(i-2)(n-i)}{2(n-1)^2},
\]
whereas that from \(i<j\le n\) is
\[
\frac{(n-i-1)(n-i)}{2(n-1)^2}.
\]
Subtracting the diagonal contribution proves (3), including \(i=n\).

For \(n\ge3\), (2) is positive; (3) gives \(a_{n,n}=0\) and \(a_{n,n-1}=-1/[2(n-1)]<0\). Direct subtraction of successive instances of (3) yields
\[
\boxed{a_{n,i+2}-2a_{n,i+1}+a_{n,i}
=\frac1{i(n-1)}>0,\quad 2\le i\le n-2.}
\tag{8}
\]
Thus the sequence \((a_{n,i})_{i=2}^n\) is strictly discretely convex. Whenever \(a_{n,i}\le0\) and \(i<j<n\), strict convexity places \(a_{n,j}\) strictly below the straight chord from \((i,a_{n,i})\) to \((n,0)\), which is nonpositive. This proves the finite ordered-sign classification, including cases with no positive nonroot covariances and all equality cases without assuming equality never occurs.

Finally, for \(i_n/n\to x\in(0,1)\), the first term of (3) tends to \((1-x)/2\) and the harmonic sum satisfies
\(\sum_{t=i_n}^{n-1}1/t\to\log(1/x)\). This gives (4). Moreover \(f''(x)=1/x>0\), \(f(0+)=1/2\), \(f(1)=0\), \(f'(1)=1/2>0\), and \(f(e^{-1/2})=(1-2e^{-1/2})/2<0\). Consequently there is exactly one interior zero \(\alpha\), with the asserted sign pattern. The finite ordered-sign property, together with convergence (4) at each fixed fraction smaller or larger than \(\alpha\), implies \(q_n/n\to\alpha\) under the stated convention for an empty positive block. This proves all claims.

## Verification

Run `python verify.py` with Python 3.9 or later. The standalone program independently enumerates the \((n-1)!\) recursive trees for each \(2\le n\le9\), obtains all joint moments from parent arrays, and checks every covariance entry (1) and row sum (2)–(3) in exact rational arithmetic. For \(3\le n\le200\), it additionally checks degree-sum cancellation, all applicable second differences (8), the endpoint signs and the single-boundary implication. The observed execution completed with `VERIFY_OK 34860 exact assertions; 46233 enumerated trees`.

The independent-parent derivation and strict-convexity argument, not finite enumeration or numerical root solving, establish the general result. The printed decimal in (5) is a numerical approximation of the uniquely characterized root.

## Relationship to prior work

The published note *Equal-share covariance of root degree and leaves in a random recursive tree* establishes the root-row covariance \(\operatorname{Cov}(D_1,Y_j)=(n-j)/(n-1)^2\), together with (2) and a decomposition by root-attachment time. Those **root-only identities are prior work**, not claimed as a novelty here. Equations (1) and (3) extend to every non-root birth label, and the novel subject is the complete non-root covariance array and its globally sign-changing age threshold; neither follows as a stated result from the root-only theorem.

Saunders studies the uniform recursive-tree model within growth/deletion dynamics and treats expected root degree and expected leaves separately. Lodewijks studies the joint behavior of labeled vertex degree, depth, and distance, without the global rooted-leaf cross-covariance. Hartle and Krapivsky study leaf-degree distributions and global leaf-count laws; their graph-theoretic leaf convention may count the root, in contrast with the rooted-leaf convention specified here. These sources motivate the difference between local vertex age and a global leaf statistic. Their inspected statements do not supply (3), (8), or (5). This comparison is not a proof of historical uniqueness.

## Limitations

The theorem is specific to independent **uniform** parent choices. It does not apply without modification to weighted or preferential attachment, graph-theoretic leaves including a degree-one root, or unrooted Cayley trees. Covariance sign does not imply monotone conditional expectation, independence at zero covariance, or any general stochastic-association order. The root-row calculation is explicitly prior work. Earlier implicit moment calculations may still encompass the non-root results, and independent historical-priority review remains necessary.

## References

1. A. Saunders, *A Class of Random Recursive Tree Algorithms with Deletion*, arXiv:1906.02720, first public version 2019-06-06, https://arxiv.org/abs/1906.02720.
2. B. Lodewijks, *On joint properties of vertices with a given degree or label in the random recursive tree*, arXiv:2204.09032, first public version 2022-04-19, https://arxiv.org/abs/2204.09032.
3. H. Hartle and P. L. Krapivsky, *Statistics of leaves in growing random trees*, arXiv:2511.04085, first public version 2025-11-06, https://arxiv.org/abs/2511.04085.
4. *Equal-share covariance of root degree and leaves in a random recursive tree*, published mathematical note, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-equal-share-covariance-of-root-degree-and-leaves-in-a-random-rec--ab0acf44833f.
