# Exact covariance spectrum and the unique boundary fluctuation of consecutive triple-pattern counts

## Finding

Let \(N_\tau\) count consecutive triples with relative order \(\tau\) in a uniformly chosen permutation on \(n\ge4\) symbols. In coordinate order \((123,132,213,231,312,321)\), the exact finite covariance matrix \(C_n\) satisfies
\[
360 C_n=nA+B,
\]
where
\[
A=\begin{pmatrix}
46&-23&-23&7&7&-14\\
-23&28&10&-20&-2&7\\
-23&10&28&-2&-20&7\\
7&-20&-2&28&10&-23\\
7&-2&-20&10&28&-23\\
-14&7&7&-23&-23&46
\end{pmatrix}
\qquad B=\begin{pmatrix}
-74&67&67&-38&-38&16\\
67&-32&-35&40&-2&-38\\
67&-35&-32&-2&40&-38\\
-38&40&-2&-32&-35&67\\
-38&-2&40&-35&-32&67\\
16&-38&-38&67&67&-74
\end{pmatrix}.
\]
The eigenvalues, **as a multiset** (coincidences permitted), are
\[
0,\quad \frac18,\quad \frac{12n-13}{120},\quad\frac{16n-29}{120},
\quad\frac{8n-13\pm\sqrt{32n^2-224n+393}}{48}.
\]
For \(n=4\), the two displayed rational eigenvalues coincide. In particular, \(C_n\) has rank five for every \(n\ge4\).

There is exactly one non-deterministic **fixed** linear combination of these pattern counts, modulo rescaling and adding the deterministic total, whose variance stays bounded as \(n\to\infty\):
\[
W_n:=N_{132}-N_{213}+N_{231}-N_{312}
=\mathbf1\{\pi_1<\pi_2\}-\mathbf1\{\pi_{n-1}<\pi_n\}.
\]
Thus \(\mathbb P(W_n=1)=\mathbb P(W_n=-1)=1/4\), \(\mathbb P(W_n=0)=1/2\), and \(\operatorname{Var}(W_n)=1/2\) for all \(n\ge4\). The centered six-vector divided by \(\sqrt n\) converges in distribution to a centered Gaussian vector with covariance \(A/360\), which has rank four; its positive eigenvalues are
\[
\frac1{10},\quad\frac2{15},\quad \frac{2-\sqrt2}{12},\quad \frac{2+\sqrt2}{12}.
\]

## Assumptions and scope

Here \(n\) is an arbitrary integer at least four, \(\pi=(\pi_1,\ldots,\pi_n)\) is uniform among all \(n!\) permutations, and \(N_\tau=\sum_{i=1}^{n-2}\mathbf1\{\operatorname{pat}(\pi_i,\pi_{i+1},\pi_{i+2})=\tau\}\), where \(\operatorname{pat}\) records the ranks of its distinct arguments. Consequently \(\sum_\tau N_\tau=n-2\) deterministically and \(\mathbb E N_\tau=(n-2)/6\). All eigenvalues refer to the ordinary Euclidean covariance matrix in this **specified coordinate order**, not to a whitened or scaled matrix. The bounded-variance uniqueness concerns coefficient vectors independent of \(n\); it does not classify arbitrary coefficient vectors varying with \(n\).

## Proof

**Exact overlap covariance.** Represent \(\pi\) by the ranks of independent continuous uniform observations \(X_1,\ldots,X_n\). For each \(\tau\in S_3\), let \(I_i^\tau=\mathbf1\{\operatorname{pat}(X_i,X_{i+1},X_{i+2})=\tau\}\). This array is stationary and 2-dependent. For displacement \(d=1,2\), define a \(6\times6\) matrix \(V_d\) by
\[
(V_d)_{\tau,\sigma}=
\frac{\#\{q\in S_{d+3}:\operatorname{pat}(q_1,q_2,q_3)=\tau,
\operatorname{pat}(q_{d+1},q_{d+2},q_{d+3})=\sigma\}}{(d+3)!}-\frac1{36}.
\]
At displacement zero, \(V_0=\operatorname{diag}(1/6,\ldots,1/6)-\mathbf1\mathbf1^{\mathsf T}/36\). For displacement \(d\ge3\), the indicators depend on disjoint independent \(X\)'s, so their covariance vanishes. Counting ordered indicator pairs therefore gives, for all \(n\ge4\),
\[
C_n=(n-2)V_0+(n-3)(V_1+V_1^{\mathsf T})+(n-4)(V_2+V_2^{\mathsf T}).
\]
Enumerating the \(4!=24\) and \(5!=120\) possible relative orders in the definition of \(V_1\) and \(V_2\) gives exactly \(360C_n=nA+B\) with the integer matrices above. These are finite identities among rationals; the appended standalone checker performs those counts and compares every entry, rather than merely sampling.

**Spectral diagonalization.** Introduce six mutually orthogonal directions
\[
\begin{aligned}
e&=(1,1,1,1,1,1),\\
w&=(0,1,-1,1,-1,0),\\
a&=(0,1,-1,-1,1,0),\\
b&=(2,-1,-1,-1,-1,2),\\
u&=(1,0,0,0,0,-1),\\
v&=(0,1,1,-1,-1,0).
\end{aligned}
\]
The exact integer entries of \(A,B\) give
\[
\begin{gathered}
C_ne=0,\quad C_nw=\frac18w,\quad
C_na=\frac{12n-13}{120}a,\quad C_nb=\frac{16n-29}{120}b,\\
C_nu=\frac{2n-3}{12}u-\frac{2n-7}{24}v,\qquad
C_nv=-\frac{2n-7}{12}u+\frac{4n-7}{24}v.
\end{gathered}
\]
In the \((u,v)\) basis, the remaining \(2\times2\) matrix is
\[
\begin{pmatrix}
(2n-3)/12&-(2n-7)/12\\
-(2n-7)/24&(4n-7)/24
\end{pmatrix}.
\]
Its characteristic quadratic yields the two radical eigenvalues in the statement. For \(n\ge4\), the four nonzero linear/radical eigenvalues and \(1/8\) are strictly positive (the lower radical root is positive because the matrix determinant is positive), establishing rank five. More explicitly, its determinant is \((4n^2+2n-28)/288\), which is positive for \(n\ge4\).

**Boundary and uniqueness.** Write \(R_i=\mathbf1\{X_i<X_{i+1}\}\). Every triple contributes \(R_i-R_{i+1}\) to \(I_i^{132}-I_i^{213}+I_i^{231}-I_i^{312}\), so telescoping gives \(W_n=R_1-R_{n-1}\). For \(n\ge4\), these two variables involve disjoint pairs of independent observations and are independent fair Bernoulli indicators; this proves the three-point distribution. The coefficient matrix \(A\) is positive semidefinite with nullspace exactly \(\operatorname{span}\{e,w\}\), by the asymptotic limits of the displayed eigendirections; its other four eigenvalues are strictly positive. Hence, for fixed \(c\in\mathbb R^6\), if \(c\notin\operatorname{span}\{e,w\}\), then \(\operatorname{Var}(c\cdot N)\) grows linearly and cannot remain bounded. Conversely, \(c\in\operatorname{span}\{e,w\}\) produces a deterministic term plus a fixed multiple of \(W_n\).

**Limit theorem.** The vector of six local indicator differences is a bounded stationary 2-dependent vector sequence. The multivariate central limit theorem for bounded finite-range-dependent variables, applied by Cramér–Wold, yields convergence with covariance \(\lim_{n\to\infty} C_n/n=A/360\). Its four positive eigenvalues follow by dividing the formulas above by \(n\) and taking limits. The remaining two normalized modes vanish, one identically and the other as the explicit bounded endpoint difference.

## Verification

Execute \(\texttt{python3 verify.py}\) with Python 3 and only its standard library, from the directory containing the supplied file. The checker (i) enumerates all \(24\) and \(120\) local overlapping order types, (ii) reconstructs the covariance formula and checks all six eigenvector/block identities for \(4\le n\le19\), and (iii) independently enumerates every permutation for \(4\le n\le8\), comparing all \(36\) exact-rational covariance entries and the full boundary three-point law. Expected terminating output is \(\texttt{VERIFY_OK}\). These finite checks support the explicitly reconstructed analytic proof; they do not constitute the proof of the infinite statement.

## Relationship to prior work

Elizalde's 2015 survey [1] defines and surveys consecutive permutation patterns and their enumerative and limiting properties. Hofer [2] proves one-pattern central limit results for vincular patterns, including fully consecutive occurrences; its discussion of future work explicitly identifies multivariate dependence of vincular patterns as interesting. Janson [3] gives a general treatment of constrained patterns and a univariate central limit theorem. Crucially, Remark 14.2 of [3] leaves the classification of degenerate linear combinations of constrained pattern counts as an open question, contrasting it with solved **unconstrained** cases. Our exact six-dimensional triple-pattern covariance and unique endpoint telescoping mode settle the fully consecutive length-three instance; we do **not** assert a general classification for longer or nonconsecutive patterns.

Unlike [3]'s unconstrained permutation subsequence counts, the six variables here count only **adjacent** triples. The displayed matrix is directly determined by the elementary overlap construction; the novel proposition assessed is its exact diagonalization, uniqueness of the bounded nontrivial contrast, and the four-dimensional Gaussian covariance classification, not the general overlap-counting principle.

## Limitations

Historical originality may remain incomplete: specialized older multivariate enumerations could imply the same spectral classification without using this terminology, and negative database searches do not prove priority. The result concerns uniform independent-rank permutations, one length-three consecutive-pattern family, and coefficient vectors fixed as \(n\) varies. Nothing is claimed about all lengths, nonuniform permutation laws, nonconsecutive occurrences, or arbitrary changing coefficient vectors. The distribution of the full six-vector is not claimed Gaussian at finite \(n\); its nonvanishing endpoint mode is discrete. Independent scientific audit and independent publication-priority review have not been performed.

## References

1. S. Elizalde, *A survey of consecutive patterns in permutations*, arXiv:1504.07265 (first submitted 2015-04-27), https://arxiv.org/abs/1504.07265 .
2. L. Hofer, *A Central Limit Theorem for Vincular Permutation Patterns*, arXiv:1704.00650 (first submitted 2017-04-03), https://arxiv.org/abs/1704.00650 .
3. S. Janson, *Asymptotic normality for m-dependent and constrained U-statistics, with applications to pattern matching in random strings and permutations*, arXiv:2106.09401 (first submitted 2021-06-17), https://arxiv.org/abs/2106.09401 ; especially Section 14 and Remark 14.2.
