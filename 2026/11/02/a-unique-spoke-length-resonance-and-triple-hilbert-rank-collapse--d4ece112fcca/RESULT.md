# A unique spoke-length resonance and triple Hilbert-rank collapse in weighted wheel metrics

## Finding

For every integer \(n\ge4\), form a weighted wheel with rim cycle \(C_n\) of unit edges and one hub joined to every rim vertex by an edge of length \(t\in[1/2,1]\). Let \(d_t\) be the weighted shortest-path distance on all \(n+1\) vertices, and let \(\wp_n(t)\) be its supremal \(p\)-negative-type exponent.

Put
\[
 c_n=\begin{cases}1,&n\text{ even},\\ \cos(\pi/n),&n\text{ odd},\end{cases}
 \qquad b_n=\frac{2c_n}{2c_n-1},\qquad
 s_n=\frac{2+(n-3)b_n}{2n},
\]
\[
 p_n^*=\log_2\!\left(\frac{b_n}{s_n}\right),\qquad
 t_n^*=s_n^{1/p_n^*}.
\]
Then \(1/2<t_n^*<1\), \(p_n^*>1\), and \(t_n^*\) is the **unique spoke length** for which the first loss of negative type simultaneously occurs in both the radial and the least-cycle-frequency sectors. The zero-sum equality space at \((t_n^*,p_n^*)\) has dimension \(2\) for even \(n\), and dimension \(3\) for odd \(n\). Accordingly the minimum Euclidean dimension of the snowflake \(d_{t_n^*}^{p_n^*/2}\) is \(n-2\) for even \(n\) and \(n-3\) for odd \(n\), rather than the generic strict-negative-type dimension \(n\).

There is also an exact global classification. For each \(t\in[1/2,1]\), let \(p_{\mathrm{rad}}(t)>1\) be the unique solution of
\[
 2+(n-3)(2t)^p=2n t^p.
\]
For \(t>1/2\), set \(p_{\mathrm{cyc}}(t)=\log b_n/\log(2t)\), and set \(p_{\mathrm{cyc}}(1/2)=+\infty\). Then
\[
 \boxed{\wp_n(t)=\min\{p_{\mathrm{rad}}(t),p_{\mathrm{cyc}}(t)\}.}
\]
The radial exponent increases strictly with \(t\), and the cycle exponent decreases strictly with \(t\). For \(t<t_n^*\), only the radial mode is critical (endpoint equality-space dimension \(1\)); for \(t>t_n^*\), only the least cycle mode is critical (dimension \(1\) for even \(n\), \(2\) for odd \(n\)). The metric has strict \(p\)-negative type for \(0\le p<\wp_n(t)\), non-strict negative type at the endpoint, and no \(p\)-negative type above it.

An exact example is \(n=4\): \(p_4^*=2\) and \(t_4^*=1/\sqrt2\). The five weighted-wheel vertices then embed in the Euclidean plane as a unit square with its center. The first odd case, \(n=5\), has \(t_5^*\approx0.839979313649\), \(p_5^*\approx1.855205961074\), and a two-dimensional critical snowflake embedding.

## Assumptions and scope

All distances are graph-geodesic shortest-path lengths, **not** electrical resistances. The hub is a vertex in the metric space. For \(t\in[1/2,1]\), the hub-to-rim distance is \(t\), adjacent rim vertices have distance \(1\), and all other distinct rim pairs have distance \(2t\). Every rim pair has a two-spoke path of length \(2t\le2\), while a rim edge cannot be shortened below \(1\) since \(2t\ge1\).

A finite metric space has \(p\)-negative type when \(\sum_{u,v}a_u a_v d(u,v)^p\le0\) for every real vector \(a\) summing to zero; it is strict when equality requires \(a=0\). The supremal exponent is taken over all real \(p\ge0\). A Euclidean embedding of \(d^{p/2}\) exists exactly when the powered-distance matrix is conditionally negative semidefinite. At its endpoint the minimum affine embedding dimension is the rank of its centered Euclidean Gram matrix.

## Proof

**1. Exact zero-sum decomposition.** Index the rim cyclically by \(j=0,\ldots,n-1\). Write a real zero-sum coefficient vector as \((y,z)\), with \(S=\sum_j y_j\) and \(z=-S\). Set \(b=(2t)^p\), \(h=t^p\), let \(A\) be the adjacency matrix of \(C_n\), and let \(J_n\) and \(I_n\) denote the all-ones and identity matrices. The rim's powered-distance matrix is exactly
\[
 R_p=b(J_n-I_n)+(1-b)A.
\]
The full quadratic form equals \(Q_p(y,z)=y^\mathsf{T}R_py-2hS^2\). Decompose \(y=S\mathbf1/n+u\), where \(\sum_j u_j=0\). Since \(R_p\mathbf1=[2+(n-3)b]\mathbf1\), the cross term vanishes and
\[
 Q_p(y,-S)=\frac{S^2}{n}\,F_n(p,t)
 -b\|u\|_2^2+(1-b)u^\mathsf{T}Au,
 \qquad F_n(p,t)=2+(n-3)b-2nh.
\]
Thus the radial sector and the rim mean-zero sector decouple exactly for **all** real \(p\ge0\).

**2. Cycle sector and multiplicity.** The adjacency eigenvalues of \(C_n\) on rim mean-zero vectors are \(2\cos(2\pi k/n)\) for \(1\le k\le n-1\). Their minimum is \(-2c_n\), where \(c_n\) is defined above; its real multiplicity is \(1\) for even \(n\) and \(2\) for odd \(n\). Because \(b\ge1\), the largest eigenvalue of the rim quadratic form is
\[
 -b+2c_n(b-1)=(2c_n-1)b-2c_n.
\]
For \(n\ge4\), \(c_n>1/2\); hence the cycle sector is nonpositive precisely when \(b\le b_n\), and it has the stated nullity exactly at \(b=b_n\). The relevant eigenvectors have zero hub coordinate and rim entries proportional to the alternating Fourier frequency (one real direction if \(n\) is even, two if odd).

**3. Radial uniqueness and monotonicity.** For \(t\in[1/2,1]\), \(F_n(0,t)=-(n+1)\) and \(F_n(1,t)=2-6t\le-1\). Moreover, \(F_n(p,t)\to n-1\) as \(p\to\infty\) if \(t=1/2\), and \(F_n(p,t)\to+\infty\) if \(t>1/2\). Its derivative with respect to \(p\) is
\[
 \partial_p F_n=(n-3)(2t)^p\log(2t)-2nt^p\log t>0,
\]
with strict positivity also at both endpoints of the length interval. Therefore there is exactly one radial zero \(p_{\mathrm{rad}}(t)>1\). At that zero, differentiating in \(t\) gives
\[
 \partial_t F_n=p t^{p-1}[(n-3)2^p-2n]=-2p/t<0,
\]
so implicit differentiation yields \(p_{\mathrm{rad}}'(t)>0\). The cycle zero is at \(p_{\mathrm{cyc}}(t)=\log b_n/\log(2t)\) for \(t>1/2\), a strictly decreasing function of \(t\), and has no finite value at \(t=1/2\).

**4. Existence, exact location and uniqueness of resonance.** The inequality \(s_n<1\) is equivalent, after rearrangement, to \(c_n>(n-1)/(n+1)\). It is immediate for even \(n\). For odd \(n\ge5\), use \(\cos(\pi/n)\ge1-\pi^2/(2n^2)>1-2/(n+1)\): the strict inequality follows from \(\pi^2<10<4n^2/(n+1)\). Also \(s_n>0\). Consequently \(p_n^*=\log_2(b_n/s_n)>1\), \(t_n^*=s_n^{1/p_n^*}<1\), and \((2t_n^*)^{p_n^*}=b_n>1\) implies \(t_n^*>1/2\). At this pair, the radial and cycle equations both hold, since \((t_n^*)^{p_n^*}=s_n\) and \((2t_n^*)^{p_n^*}=b_n\). Conversely any simultaneous zero must obey these two scalar identities, hence must be precisely this pair. Equivalently, strict increase of the radial threshold and strict decrease of the cycle threshold prevent a second crossing.

**5. Endpoint ranks and sharpness.** The decomposition shows all sectors strictly negative before their first zero, and a positive quadratic direction immediately afterward. The radial critical space is one-dimensional, while the least cycle-frequency space has the multiplicity described above. Their direct sum gives nullity \(2\) (even rim) or \(3\) (odd rim) at the unique resonance, with no other vanishing modes. Schoenberg's centered Gram criterion therefore gives the stated sharp Euclidean dimensions. For \(n=4\), \(b_4=2\), \(s_4=1/2\), so \(p_4^*=2\), \(t_4^*=1/\sqrt2\). For \(n=5\), substituting \(c_5=\cos(\pi/5)\) gives the displayed numerical values. No numerical step is needed to prove the universal statements.

## Verification

Run `python verify_weighted_wheel.py` in an environment with Python 3, NetworkX, NumPy, SymPy and SciPy. The checker independently builds weighted shortest paths, compares the exact distance structure for rational spoke lengths, and verifies the quadratic-form identity by exact rational arithmetic in 600 nonconstant coefficient configurations. It also checks first-mode transitions and centered Gram inertias on rim sizes \(4\) through \(39\). Its final line is `ALL_WEIGHTED_WHEEL_CHECKS_OK`. Those finite tests corroborate the algebraic proof; they do not establish it for infinitely many rim sizes or arbitrary real weights.

## Relationship to prior work

Li and Weston (2009) establish the general strictness and interval principles of negative type. Sánchez (2011) develops a general finite-metric powered-distance criterion and evaluates the complete-bipartite case. DeVille (2017) treats generalized distance spectra, principally of distance-regular graphs. Alhevaz, Baghipur, Ahmad and Shang (2020) give generalized distance spectra of graph joins including ordinary wheel graphs. Balaji, Bapat and Goel (2020) analyze the **ordinary**, unweighted distance matrix of wheels with an even number of vertices. Their techniques and the familiar Fourier spectrum of cycles are pertinent antecedents, not claimed new here.

Buckley and Harary (1988) study the Euclidean dimension of wheel **graphs** under the constraint that each graph edge has unit length; this is different from isometrically embedding **all pairs** of a weighted shortest-path metric.

The distinct claim here is the weighted-shortest-path **two-mode simultaneous threshold**, its unique exact spoke length, and its parity-dependent two-/three-dimensional critical kernel. The unweighted wheel boundary and general spectral machinery are antecedents, not separate novelty claims. Publicly indexed sources do not constitute an exhaustive priority search, and an equivalent derivation using general join-spectrum methods may exist.

## Limitations

The rim edges are all unit length and all spokes have one common length in \([1/2,1]\); the hub is included as a vertex. This does not classify spoke lengths outside that interval, nonuniform spokes, other hubbed graphs, resistance metrics, or arbitrary distance transformations. The proof is self-contained for the stated continuous range; numerical verification is finite. Priority in unindexed or inaccessible literature is not independently established.

## References

- F. Buckley and F. Harary, *On the Euclidean Dimension of a Wheel*, Graphs Combin. **4** (1988), 23–30, DOI:10.1007/BF01864150 (graph edge unit-distance embedding, not all-pairs isometry).
- H. Li and A. Weston, *Strict p-negative type of a metric space*, first public version 2009-01-06, arXiv:0901.0695, https://arxiv.org/abs/0901.0695 .
- S. Sánchez, *On the supremal p-negative type of a finite metric space*, first public version 2011-08-02, arXiv:1108.0451, https://arxiv.org/abs/1108.0451 .
- L. DeVille, *The generalized distance spectrum of a graph and applications*, 2017-08-07, arXiv:1708.02294, https://arxiv.org/abs/1708.02294 .
- A. Alhevaz, M. Baghipur, H. Ahmad and Y. Shang, *The Generalized Distance Spectrum of the Join of Graphs*, Symmetry **12** (2020), 169, DOI:10.3390/sym12010169 .
- R. Balaji, R. B. Bapat and S. Goel, *An inverse formula for the distance matrix of a wheel graph with even number of vertices*, arXiv:2006.02841 (2020), https://arxiv.org/abs/2006.02841 .
