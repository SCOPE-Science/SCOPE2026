# Balanced-sign Laplacian trace probing: an exact variance projection and zero-variance graph classification

## Finding

**Theorem (exact graph-Laplacian variance and its complete zero-variance locus).** Fix any even integer \(n\ge4\). For every symmetric array of nonnegative real edge weights \(w_{ij}=w_{ji}\ge0\) for \(1\le i<j\le n\), assign weight zero to a missing edge. Set \(d_i=\sum_{j\ne i}w_{ij}\), \(W=\sum_{i<j}w_{ij}\), and let \(L\) be the weighted Laplacian with diagonal entries \(d_i\) and off-diagonal entries \(-w_{ij}\). Draw \(s\) uniformly from the sign vectors \(\{-1,1\}^n\) having exactly \(n/2\) positive coordinates, and make one matrix-vector query to calculate

\[
T=\frac{n-1}{n}s^\top Ls.
\]

Then \(T\) is unbiased for \(\operatorname{tr}L=2W\), and its variance is **exactly**

\[
\operatorname{Var}(T)=\frac{4(n-1)}{n(n-3)}
\left[(n-2)\sum_{i<j}w_{ij}^{2}-\sum_{i=1}^{n}d_i^{2}
+\frac{2W^{2}}{n-1}\right]. \tag{1}
\]

Writing \(\mathcal A=\{(u_i+u_j)_{i<j}:u\in\mathbb R^n\}\), this also has the **sharp, nonnegative squared-distance representation**

\[
\operatorname{Var}(T)=\frac{4(n-1)(n-2)}{n(n-3)}
\min_{u\in\mathbb R^n}\sum_{i<j}(w_{ij}-u_i-u_j)^2. \tag{2}
\]

The minimizing potentials are unique and explicit:

\[
u_i=\frac{d_i-W/(n-1)}{n-2}.\tag{3}
\]

In particular, one balanced probe has **zero variance** if and only if \(w_{ij}=u_i+u_j\) on **every** unordered pair for some real vector \(u\). For any *unweighted simple graph* (all \(w_{ij}\in\{0,1\}\)), this happens **if and only if**, up to graph isomorphism, the graph is the empty graph, the complete graph, the star \(K_{1,n-1}\), or the disjoint union of \(K_{n-1}\) with one isolated vertex.

## Assumptions and scope

The dimension is even and at least four; vertex labels are fixed; the graph can be disconnected or weighted; no assumption about degree regularity is made. The zero-variance classification into four graph families is only for simple unweighted graphs. The weighted criterion (2) permits signed vertex potentials \(u\), but all off-diagonal edge weights themselves remain nonnegative. The estimator accesses the Laplacian through one exact matrix-vector application and one inner product. Equal positive/negative sign counts are part of the sampling law; the signs are **dependent**, so usual independent-Rademacher variance formulas do not apply without change.

## Proof

**1. Balanced sign moments and unbiasedness.** Exchangeability and \(\sum_i s_i=0\) almost surely give, for distinct indices,

\[
\mu:=\mathbb E(s_i s_j)=-\frac1{n-1}.
\]

For four pairwise distinct indices, use \(\mathbb E[s_i s_j s_k\sum_l s_l]=0\). The three terms where \(l\in\{i,j,k\}\) each equal \(\mu\), while the remaining \(n-3\) are equal by exchangeability. Thus

\[
\nu:=\mathbb E(s_i s_j s_k s_l)=\frac{3}{(n-1)(n-3)}.
\]

Since \(s_i^2=1\),

\[
s^\top Ls=\sum_{i<j}w_{ij}(s_i-s_j)^2
=2W-2S,\qquad S=\sum_{i<j}w_{ij}s_i s_j.
\]

Consequently \(\mathbb E S=\mu W\) and

\[
\mathbb E T=\frac{2(n-1)}n(W-\mu W)=2W=\operatorname{tr}L.
\]

**2. Pair-overlap bookkeeping.** Write \(Q=\sum_{i<j}w_{ij}^2\) and \(D_2=\sum_i d_i^2\). In the expansion of \(S^2\), identical pairs contribute \(Q\); distinct pairs of edges meeting at one vertex contribute \(2A\mu\), where \(A=(D_2-2Q)/2\); disjoint edge pairs contribute \(2B\nu\), where \(B=(W^2+Q-D_2)/2\). These identities hold with arbitrary real pair weights, hence also for the nonnegative weights here. Therefore

\[
\begin{aligned}
\operatorname{Var}(S)
&=Q+\mu(D_2-2Q)+\nu(W^2+Q-D_2)-\mu^2W^2\\
&=\frac{n}{(n-1)(n-3)}
\left[(n-2)Q-D_2+\frac{2W^2}{n-1}\right].
\end{aligned}
\]

Multiplying by \(4(n-1)^2/n^2\) gives (1), with no asymptotic approximation.

**3. Exact projection and strict zero locus.** Define the \(\binom n2\times n\) unsigned vertex-pair incidence operator \(B\), where \((Bu)_{ij}=u_i+u_j\). Its Gram matrix is

\[
B^\top B=(n-2)I+\mathbf1\mathbf1^\top,
\]

which is positive definite for \(n\ge4\). Moreover \(B^\top w=d\), with \(\sum_i d_i=2W\). The unique normal-equation solution is (3). Pythagoras for the orthogonal projection gives

\[
\begin{aligned}
\min_u\|w-Bu\|_2^2
&=Q-d^\top u\\
&=\frac{(n-2)Q-D_2+2W^2/(n-1)}{n-2}.
\end{aligned}
\]

Substitution yields (2). Its positive prefactor proves that zero variance is equivalent to \(w\in\mathcal A\), not just that this condition is sufficient.

**4. Rigidity for simple graphs.** Suppose every pair weight belongs to \(\{0,1\}\) and has additive form \(w_{ij}=u_i+u_j\). If all \(u_i\) are equal, every edge weight is the same, yielding the empty or complete graph. Otherwise choose indices \(i,j\) with \(u_i>u_j\). For every \(k\notin\{i,j\}\),

\[
w_{ik}-w_{jk}=u_i-u_j>0.
\]

Since both weights lie in \(\{0,1\}\), this forces \(w_{ik}=1\), \(w_{jk}=0\), and \(u_i-u_j=1\). Every other \(u_k\) must equal a common value \(c\), so \(u_i=1-c\), \(u_j=-c\). As \(n\ge4\), there exist distinct \(k,l\) outside \(\{i,j\}\), giving \(2c=w_{kl}\in\{0,1\}\). Thus \(c=0\) or \(c=1/2\). In the first case, \(i\) is joined to all other vertices and no other edges occur: a star. In the second case, \(j\) is isolated and all other vertices form a clique. Conversely all four graph families admit such an additive potential vector: \(u\equiv0\) for empty; \(u\equiv1/2\) for complete; one potential equal to \(1\) and all others \(0\) for a star; one potential \(-1/2\) and all others \(1/2\) for a clique plus an isolate. This proves necessity and sufficiency for every even \(n\ge4\).

## Verification

The standalone `verify.py` is pure Python standard library and compares the variance formulas to **exact rational enumeration** of the entire balanced sign distribution. It checks 600 deterministic pseudo-random nonnegative integer-weighted graphs over dimensions \(4,6,8,10\), 200 additive weighted examples, and the full finite sets of \(2^6\) simple four-vertex and \(2^{15}\) simple six-vertex graphs. It also checks projection orthogonality, mean normalization, uniqueness consequences, and the identified four families. The extracted script completed with 3,434 exact assertions. These checks are finite diagnostic evidence; the preceding algebra proves the statement for all admissible dimensions and weights.

For a star \(K_{1,n-1}\), the balanced estimator is deterministic despite the ordinary independent-Rademacher Hutchinson estimator having one-query variance \(4(n-1)\). This follows from the exact variance identities: for independent fair signs the cross terms have zero covariance and the variance is \(4\sum_{i<j}w_{ij}^2\). No general stochastic dominance is asserted for arbitrary graphs.

## Relationship to prior work

The matrix-free trace-estimation motivation and independent-sign baseline are in Meyer, Musco, Musco and Woodruff (2020), whose Hutch++ method uses independent random signs and randomized low-rank correction. Persson, Cortinovis and Kressner (2021) study improved low-rank-corrected trace estimators using independent Gaussian probes. These do not state the balanced-slice degree-based variance identity or the complete zero-variance graph families in the inspected methods and theoretical statements.

Filmus and Mossel (2015) develop the general harmonic-polynomial and orthogonality theory of the fixed-Hamming-weight Boolean slice; in particular, their Theorem 3.10 supplies a powerful representation-theoretic route to second moments of harmonically projected degree-two functions. Such general slice orthogonality is **prior art** and is not claimed as new here. The present theorem supplies the explicit graph-Laplacian trace normalization, the exact weighted edge-distance identity, and the complete \(\{0,1\}\)-graph zero-variance rigidity classification. The proof directly verifies the specialization instead of assuming a new general theory of the slice. Publication priority for this precise combination has not been exhaustively established.

## Limitations

When all weighted edges are supplied explicitly, the Laplacian trace is trivially \(2\sum_{i<j}w_{ij}\) and there is no algorithmic need for this estimator. The relevance is specifically **implicit matrix-vector access**, controlled probe-design comparisons, or structural variance benchmarks. An exact one-query result for these graph Laplacians says nothing about the trace of matrix functions such as an inverse or exponential. The method requires exactly balanced signs, an even number of vertices, noiseless products, and the stated weighted Laplacian model. It does not claim universal improvement over independent probes, or optimal query complexity for arbitrary PSD matrices. The cited slice-harmonic representation theory may permit alternate derivations; further specialized earlier results remain a publication-priority risk. Independent scientific assessment has not been performed.

## References

1. R. A. Meyer, C. Musco, C. Musco, D. P. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, first posted 19 October 2020, [arXiv:2010.09649](https://arxiv.org/abs/2010.09649).
2. D. Persson, A. Cortinovis, D. Kressner, *Improved variants of the Hutch++ algorithm for trace estimation*, first posted 22 September 2021, [arXiv:2109.10659](https://arxiv.org/abs/2109.10659).
3. Y. Filmus, E. Mossel, *Harmonicity and Invariance on Slices of the Boolean Cube*, first posted 9 July 2015, [arXiv:1507.02713](https://arxiv.org/abs/1507.02713), especially Section 3.2 and Theorem 3.10.
