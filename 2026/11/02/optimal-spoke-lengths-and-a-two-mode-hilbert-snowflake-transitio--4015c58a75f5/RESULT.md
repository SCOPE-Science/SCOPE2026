# Optimal spoke lengths and a two-mode Hilbert-snowflake transition for weighted wheels

## Finding

Fix an integer \(n\ge4\). Form a metric wheel \(W_n(r)\) with rim vertices \(0,\ldots,n-1\), a hub \(h\), rim edges of length \(1\), and all \(n\) spokes of length \(r\in[1/2,1]\). Distances are shortest-path lengths. For \(p\ge0\), a finite metric has \(p\)-negative type when \(\sum_{v,w}z_vz_wd(v,w)^p\le0\) for every real vector \(z\) with \(\sum_vz_v=0\). At \(p=0\), the diagonal of the powered-distance matrix is defined to be zero.

Define
\[
 c_n=\begin{cases}1,&n\text{ even},\\\cos(\pi/n),&n\text{ odd},\end{cases}
 \qquad a_n=\frac{2c_n}{2c_n-1},\qquad
 b_n=\frac{(n-3)a_n+2}{2n}.
\]
Then \(0<b_n<1\), and the following constants are well-defined:
\[
 p_n^{\mathrm{opt}}=\log_2\frac{a_n}{b_n},\qquad
 r_n^{\mathrm{opt}}=b_n^{1/p_n^{\mathrm{opt}}}\in(1/2,1).
\]
For \(r\in[1/2,1]\), let \(p_g(n,r)\) be the unique positive solution of
\[
 (n-3)(2r)^p+2-2nr^p=0,
\]
and put
\[
 p_s(n,r)=\begin{cases}
 \infty,&r=1/2,\\
 \dfrac{\log a_n}{\log(2r)},&1/2<r\le1.
 \end{cases}
\]

**Theorem.** The supremal negative-type exponent of \(W_n(r)\) is exactly
\[
 \boxed{\wp(W_n(r))=\min\{p_g(n,r),p_s(n,r)\}.}
\]
The minimum is \(p_g(n,r)\) for \(r<r_n^{\mathrm{opt}}\), equals both thresholds at \(r=r_n^{\mathrm{opt}}\), and is \(p_s(n,r)\) for \(r>r_n^{\mathrm{opt}}\). The exponent is strictly increasing as \(r\) varies from \(1/2\) to \(r_n^{\mathrm{opt}}\), then strictly decreasing up to \(1\). In particular,
\[
 \boxed{\max_{1/2\le r\le1}\wp(W_n(r))=p_n^{\mathrm{opt}}}
\]
with a **unique maximizing spoke length** \(r=r_n^{\mathrm{opt}}\).

The metric has strict \(p\)-negative type for \(0\le p<\wp(W_n(r))\), nonstrict negative type at equality, and fails \(p\)-negative type for every larger \(p\). Let \(\kappa\) be the dimension of the zero-sum equality space at its critical exponent. Then
\[
 \kappa=\begin{cases}
 1,&r<r_n^{\mathrm{opt}},\\
 1+e_n,&r=r_n^{\mathrm{opt}},\\
 e_n,&r>r_n^{\mathrm{opt}},
 \end{cases}
 \qquad
 e_n=\begin{cases}1,&n\text{ even},\\2,&n\text{ odd}.\end{cases}
\]
For \(0<p\le\wp(W_n(r))\), the metric \(d^{p/2}\) embeds isometrically into a real Hilbert space. Its minimal affine embedding dimension is \(n\) below the threshold and \(n-\kappa\) at the threshold.

The transition has a sharp large-rim scale:
\[
 r_n^{\mathrm{opt}}=1-\frac2n+O(n^{-2}),\qquad
 p_n^{\mathrm{opt}}=1+\frac{2}{n\log2}+O(n^{-2}).
\]
For every fixed \(1/2\le r<1\), the global mode eventually controls the threshold and
\[
 \wp(W_n(r))=1+\frac{3-1/r}{n\log2}+O_r(n^{-2}).
\]
At \(r=1\) the contrast mode controls it: the exponent is exactly \(1\) for even \(n\), while for odd \(n\)
\[
 \wp(W_n(1))=1+\frac{\pi^2}{2n^2\log2}+O(n^{-4}).
\]
This identifies a narrow transition window of radial weights near \(1\) between two distinct critical equality mechanisms.

For the smallest rim, \(n=4\), the unique optimum is \(r_4^{\mathrm{opt}}=1/\sqrt2\) and \(p_4^{\mathrm{opt}}=2\). At this point the squared-distance embedding is realized by a Euclidean unit square together with its center. For \(n=5\), the optimum has \(a_5=(3+\sqrt5)/2\), \(b_5=(5+\sqrt5)/10\), and \(p_5^{\mathrm{opt}}=\log_2((5+\sqrt5)/2)\).

## Assumptions and scope

The graph is finite, has exactly one hub, has an integer rim size \(n\ge4\), has all rim edges of length one, and has uniform real spoke length \(1/2\le r\le1\). The specified interval guarantees that every pair of distinct rim vertices has distance \(1\) if adjacent on the cycle and \(2r\) otherwise; every hub-rim distance is \(r\). Ties at \(r=1/2\) and \(r=1\) are allowed. The range \(n=3\), nonuniform spoke lengths, and spoke lengths outside this interval are excluded. The exponent \(p\) is an arbitrary nonnegative real number; no upper bound on \(p\) is assumed in the proof.

## Proof

**1. Exact distance reduction.** Write \(a=(2r)^p\), \(b=r^p\), and let \(A\) be the adjacency matrix of the rim cycle \(C_n\). The rim-rim powered distance block is
\[
 D_{\mathrm{rim}}^{(p)}=a(J-I)+(1-a)A.
\]
Given any zero-mass real vector, write its rim coordinates \(x=(x_0,\ldots,x_{n-1})\), its hub coordinate \(y=-\sum_jx_j\), and decompose \(x=\bar x\mathbf1+u\), where \(\sum_ju_j=0\). As \(A\mathbf1=2\mathbf1\), direct expansion gives the **exact identity**
\[
 \begin{aligned}
 Q_p(x,y)&=\sum_{v,w}z_vz_wd(v,w)^p\\
 &=n\bigl[(n-3)a+2-2nb\bigr]\bar x^2
       -a\|u\|_2^2+(1-a)\langle u,Au\rangle.
 \end{aligned}
\]
The global and oscillatory subspaces are independent in this quadratic form, and they span the complete \(n\)-dimensional zero-mass subspace.

**2. The only two obstructions.** The cycle adjacency eigenvalues on the orthogonal complement of constants are \(2\cos(2\pi k/n)\), \(1\le k<n\). Since \(a\ge1\), the largest eigenvalue of the oscillatory quadratic form is
\[
 -a+2(a-1)c_n=(2c_n-1)a-2c_n.
\]
It is nonpositive precisely when \(a\le a_n\). This is automatic for all \(p\ge0\) if \(r=1/2\); otherwise it holds exactly for \(p\le p_s(n,r)\). The global coefficient is
\[
 g_{n,r}(p)=(n-3)(2r)^p+2-2nr^p.
\]
It satisfies \(g_{n,r}(0)=-n-1<0\) and
\[
 g_{n,r}'(p)
 =(n-3)\log(2r)(2r)^p-2n\log r\,r^p>0
\]
throughout the allowed spoke-length interval. Its limit is positive (infinite for \(r>1/2\)), so it has one positive root \(p_g(n,r)\). The decomposition establishes both necessity and sufficiency of the two inequalities. It also proves strictness below the smaller root, the critical equality vectors, and failure above it; in particular there is no unverified possibility of reentrant negative type.

**3. A unique transition and optimum.** For \(n\) even, \(c_n=1\). For odd \(n\ge5\), the elementary inequality \(\cos(\pi/n)>(n-1)/(n+1)\) gives \(a_n<2(n-1)/(n-3)\). The same conclusion is immediate for even \(n\). Thus \(0<b_n<1\). For \(r>1/2\), substitute the spectral threshold \(p_s\) into the global coefficient:
\[
 g_{n,r}(p_s)=2n\left(b_n-r^{p_s}\right).
\]
The function
\[
 r\longmapsto r^{p_s(n,r)}
 =\exp\left(\frac{\log a_n\,\log r}{\log(2r)}\right)
\]
is strictly increasing from \(0\) at the lower endpoint to \(1\) at \(r=1\): the derivative of \(\log r/\log(2r)\) is \((\log2)/(r\log^2(2r))>0\). Therefore precisely one spoke length makes the two thresholds equal. Solving \((2r)^p=a_n\) and \(r^p=b_n\) yields
\[
 p=p_n^{\mathrm{opt}}=\log_2(a_n/b_n),\qquad
 r=r_n^{\mathrm{opt}}=b_n^{1/p_n^{\mathrm{opt}}}.
\]
This length lies strictly between \(1/2\) and \(1\), since \(0<b_n<1<a_n\).

For the global root, implicit differentiation at \(g_{n,r}(p_g)=0\) gives
\[
 \frac{\partial g_{n,r}}{\partial r}(p_g)=-\frac{2p_g}{r}<0,
 \qquad
 \frac{\partial p_g}{\partial r}
 =\frac{2p_g}{r\,\partial_pg_{n,r}(p_g)}>0.
\]
Conversely \(p_s(n,r)=\log a_n/\log(2r)\) strictly decreases for \(r>1/2\). Their lower envelope consequently has the asserted unique maximum and the two branches.

**4. Equality spaces and embedding dimension.** When the global coefficient vanishes, its zero-mass equality vector is \((1,\ldots,1,-n)\). When the oscillatory coefficient vanishes, its zero-mass equality vectors have hub coordinate zero and rim entries in the minimum-eigenvalue eigenspace of \(C_n\). For even \(n\) this is the one-dimensional alternating vector \(((-1)^j)_j\). For odd \(n\) it is the two-dimensional real span of \(\cos(2\pi k j/n)\) and \(\sin(2\pi k j/n)\) with \(k=(n-1)/2\). These spaces have disjoint support decomposition and add at the transition.

For a finite metric, the centered powered-distance Gram matrix is \(-\tfrac12 H D^{(p)}H\), where \(H\) is orthogonal projection onto zero-mass vectors. By the elementary distance-Gram correspondence (Schoenberg's criterion), its positive-semidefiniteness characterizes Hilbert embeddings of \(d^{p/2}\), and its rank is the minimum affine dimension. Its dimension is therefore \(n-\kappa\) at the endpoint and \(n\) below it.

**5. Large-rim expansions.** For even \(n\), \(a_n=2\). For odd \(n\), Taylor's theorem yields \(a_n=2+\pi^2n^{-2}+O(n^{-4})\). In both cases \(b_n=1-2n^{-1}+O(n^{-2})\). Substitution into the explicit formulas proves the transition-weight and optimal-exponent expansions. For fixed \(r<1\), \(p_s(n,r)\) tends to a number strictly greater than one (or is infinite at \(r=1/2\)), whereas the global root tends to one. Writing \(p=1+\delta\) in \(g_{n,r}(p)=0\) and applying Taylor's theorem gives
\[
 0=2nr(\log2)\delta+2-6r+O_r(n\delta^2+|\delta|),
\]
so \(\delta=(3-1/r)/(n\log2)+O_r(n^{-2})\). At \(r=1\), the oscillatory expression directly gives the asserted parity-dependent expansion.

## Verification

The self-contained `verify.py` reconstructs shortest-path distances by Floyd–Warshall independently of the reduced formula, builds a zero-sum orthonormal basis, and checks the complete powered-distance spectra for all \(4\le n\le16\) at six radial weights per size, including the exact transition weight. It also tests arbitrary zero-mass vectors against the quadratic-form identity, the predicted critical nullity, both sides of each exponent threshold, and large-rim expansions. The completed replay returned `PASS` with 10,362 assertions. See `VERIFICATION.md` for reproducibility details. This finite test suite corroborates but does not prove the all-size statements; the proof is the algebraic argument above.

## Relationship to prior work

Obata's *Quadratic Embedding Constants of Wheel Graphs* (2017, Theorem 1.1) determines the ordinary unweighted \(p=1\) wheel quadratic embedding constant, including its odd/even parity split. Lou, Obata and Huang's *Quadratic Embedding Constants of Graph Joins* (arXiv:2001.06752, submitted 2020; Example 3.6) reproduces that unweighted result through the adjacency spectrum of graph joins. These supply the motivating spectral setting but **do not state the variable spoke-length, variable exponent, or optimal radial phase diagram** proved here. Robertson's *Negative type and bi-lipschitz embeddings into Hilbert space* (arXiv:2309.16070, 2023) gives the general \(p\)-negative type/Hilbert framework and works out bipartite and Hamming examples, not weighted metric wheels. The present assertion is a direct new explicit classification in the metric-embedding setting, not a claim to have discovered the existing Fourier or Schoenberg criteria.

## Limitations

The class is restricted to uniform spokes in \([1/2,1]\) and at least four rim vertices. When spokes are shorter, the shortest-path rim distances change form; when longer, multiple rim separation scales appear, so the two-parameter distance reduction no longer applies. No claim is made for arbitrary wheel weights, graph-independent embedding bounds, nonlinear Banach targets, or distorted embeddings. Previously published spectral identities and their immediate unweighted \(p=1\) corollaries are not claimed as new. Novelty is qualified by the possibility of an earlier equivalent weighted wheel calculation under alternative metric terminology.

## References

1. N. Obata, *Quadratic Embedding Constants of Wheel Graphs*, Interdisciplinary Information Sciences 23 (2017), 171–174, DOI: `10.4036/iis.2017.S.02`. Full text: https://www.jstage.jst.go.jp/article/iis/23/2/23_2017.S.02/_pdf (Theorem 1.1 and Section 4).
2. Z. Lou, N. Obata and Q. Huang, *Quadratic Embedding Constants of Graph Joins*, arXiv:2001.06752v1, first posted 2020-01-19; revised 2022. https://arxiv.org/html/2001.06752v2 (Section 3, especially Example 3.6).
3. G. Robertson, *Negative type and bi-lipschitz embeddings into Hilbert space*, arXiv:2309.16070v1, first posted 2023-09-27. https://arxiv.org/abs/2309.16070 (Sections 1 and 4).
4. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536 (foundational distance-Gram criterion).
