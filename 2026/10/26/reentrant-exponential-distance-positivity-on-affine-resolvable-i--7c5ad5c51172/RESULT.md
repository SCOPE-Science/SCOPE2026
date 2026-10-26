# Reentrant exponential-distance positivity on affine resolvable incidence graphs

## Finding
Let \(\mathcal D\) be any **existing** affine resolvable design \(\mathrm{AD}(n,\mu)\), with integers \(n\ge2\), \(\mu\ge1\), and let \(G\) be its point–block incidence graph, equipped with shortest-path distance \(d\). For any real values \(f_0,\ldots,f_4\), the real symmetric distance-radial matrix \(K_f=[f_{d(x,y)}]_{x,y\in V(G)}\) is positive semidefinite if and only if one explicit scalar and two explicit \(2\times2\) matrices below are positive semidefinite. This includes designs without point- or block-transitive automorphism groups.

Put \(k=n\mu\), \(v=nk\), and \(r=(nk-1)/(n-1)\). Define
\[
L=f_0-nf_2+(n-1)f_4,
\]
\[
B_1=\begin{pmatrix}
f_0-f_2 & \sqrt{k}(f_1-f_3)\\
\sqrt{k}(f_1-f_3)&f_0-f_4
\end{pmatrix},
\quad
B_0=\begin{pmatrix}
f_0+(v-1)f_2&\sqrt{kr}\bigl(f_1+(n-1)f_3\bigr)\\
\sqrt{kr}\bigl(f_1+(n-1)f_3\bigr)&f_0+n(r-1)f_2+(n-1)f_4
\end{pmatrix}.
\]
Then the **complete radial positivity cone** is
\[
\boxed{K_f\succeq0\iff L\ge0,\quad B_1\succeq0,\quad B_0\succeq0.}
\]
The scalar \(L\) has multiplicity \(r-1\); each eigenvalue of \(B_1\) has multiplicity \(v-1\); and each eigenvalue of \(B_0\) has multiplicity one. The decomposition determines rank and inertia at every parameter value, including singular boundaries.

For the exponential-distance family \(K_a(x,y)=e^{-a d(x,y)}\), let \(a>0\) and \(w=e^{-2a}\). Put
\[
\begin{aligned}
\beta&=-k^2n+2kn^2-kn+k-n^2,\\
\gamma&=(k-1)(n-1)^2(kn-1).
\end{aligned}
\]
The exact positivity criterion simplifies to
\[
\boxed{K_a\succeq0\iff a=0\quad\text{or}\quad
\left(a>0,\ \ 0<w\le\frac1{k-1},\ \ (n-1)+\beta w+\gamma w^2\ge0\right).}
\]

In particular, take the affine hyperplane design of \(\mathrm{AG}(3,3)\), with 27 points and 39 hyperplanes. Its incidence graph has 66 vertices. Let
\[
w_- = \frac{27-\sqrt{313}}{416},\qquad
w_+ = \frac{27+\sqrt{313}}{416}.
\]
These satisfy \(0<w_-<w_+<1/8\), and the sharp admissible set is **disconnected**:
\[
\boxed{K_a\succeq0\iff a=0\quad\text{or}\quad
0<e^{-2a}\le w_-\quad\text{or}\quad
w_+\le e^{-2a}\le\frac18.}
\]
Equivalently, the positive admissible bandwidths are
\[
\left[\tfrac12\log8,\ -\tfrac12\log w_+\right]
\ \cup\
\left[-\tfrac12\log w_-,\ \infty\right).
\]
The matrix is strictly positive definite in the interiors of these two positive intervals. The ranks at \(a=0\), \(e^{-2a}=1/8\), and \(e^{-2a}=w_\pm\) are exactly \(1\), \(40\), and \(65\), respectively. Thus increasing the bandwidth from zero may first give a valid positive-definite kernel, then an invalid indefinite matrix, then a valid positive-definite kernel again.

## Assumptions and scope
An affine resolvable design is a \(2\)-\((v,k,\lambda)\) design whose blocks partition into \(r\) parallel classes, each containing \(n\) pairwise disjoint blocks, such that every two blocks from distinct parallel classes intersect in exactly \(\mu\) points. Its standard parameters are \(v=n^2\mu\), \(k=n\mu\), \(\lambda=(n\mu-1)/(n-1)\), \(r=(n^2\mu-1)/(n-1)\), and \(b=nr=v+r-1\). The assertion concerns each design that actually exists; it makes no existence claim for arbitrary integer pairs. The incidence graph has distances \(0\) through \(4\), with point–point distance \(2\), parallel distinct block–block distance \(4\), nonparallel block–block distance \(2\), and point–block distance \(1\) or \(3\) according to incidence. Every result above uses this unweighted graph metric.

## Proof
Let \(M\) be the \(v\times b\) point–block incidence matrix, with columns ordered by parallel class. Let \(J\) denote an all-ones matrix of the dimensions dictated by its context, and put \(C=I_r\otimes J_n\). Standard counting gives
\[
MM^{\mathsf T}=kI_v+\lambda J_v,\qquad
M^{\mathsf T}M=kI_b+\mu(J_r-I_r)\otimes J_n,
\]
where \(r-\lambda=k\). The full radial kernel is
\[
K_f=\begin{pmatrix}
(f_0-f_2)I_v+f_2J_v & (f_1-f_3)M+f_3J_{v,b}\\
(f_1-f_3)M^{\mathsf T}+f_3J_{b,v}&(f_0-f_4)I_b+(f_4-f_2)C+f_2J_b
\end{pmatrix}.
\]
On the orthogonal complement of the constant point vector, \(MM^{\mathsf T}=kI\). Therefore each of the \(v-1\) orthonormal point directions pairs with its normalized incidence-image direction to give the \(2\times2\) restriction \(B_1\). For such an incidence-image direction, the sum of coefficients within every parallel class vanishes, so \(C\) acts by zero; the singular coupling coefficient is \(\sqrt{k}\).

The orthogonal complement in block space to the image of \(M^{\mathsf T}\) consists precisely of vectors constant within each parallel class whose \(r\) class-constants sum to zero. Its dimension is \(b-v=r-1\). On this subspace, \(C\) acts as multiplication by \(n\), and \(J_b\) vanishes. The eigenvalue of \(K_f\) is exactly \(L\).

The remaining two-dimensional subspace is spanned by the normalized all-one vectors in point space and block space. The cross-incidence singular value is \(\sqrt{kr}\), and direct row sums produce \(B_0\). These orthogonal invariant subspaces exhaust \(2+2(v-1)+(r-1)=v+b\) dimensions. Hence the three displayed semidefinite tests are individually necessary and jointly sufficient, with precisely the claimed multiplicities.

Set \(z=e^{-a}\) and \(w=z^2\) for \(a>0\). Direct substitution into the blocks yields
\[
L=(1-w)\bigl(1-(n-1)w\bigr),\qquad
\det B_1=(1-w)^2\bigl(1-(k-1)w\bigr).
\]
Both diagonal entries of \(B_1\) are strictly positive when \(0<w<1\); thus \(B_1\succeq0\) exactly when \(w\le1/(k-1)\). Since \(k=n\mu\ge n\), that bound also forces \(L\ge0\). The top-left diagonal entry of \(B_0\) is \(1+(v-1)w>0\), so its positivity is equivalent to nonnegative determinant. Simplifying its determinant using \(r=(nk-1)/(n-1)\) gives
\[
\det B_0=\frac{1-w}{n-1}\bigl((n-1)+\beta w+\gamma w^2\bigr),
\]
with the explicit \(\beta,\gamma\) above. This proves the general exponential criterion. At \(a=0\), all entries are one, so \(K_0=J_{v+b}\) has rank one.

For \(\mathrm{AG}(3,3)\), insert \(n=3\), \(\mu=3\), \(k=9\), \(v=27\), \(r=13\). The determinant factors specialize to
\[
\det B_0=(1-w)(1-54w+416w^2),\quad
\det B_1=(1-w)^2(1-8w),\quad
L=(1-w)(1-2w).
\]
The quadratic has the distinct roots \(w_-,w_+\) above. Both lie strictly between zero and \(1/8\), and the quadratic is nonnegative exactly outside their open interval. Consequently the admissible \(w\) set and its two positive-bandwidth components follow. At \(w=w_\pm\) only \(B_0\) loses one eigenvalue; at \(w=1/8\) exactly one eigenvalue in each of the \(v-1=26\) copies of \(B_1\) vanishes. No other sector vanishes at these points. The endpoint ranks are therefore \(65\) and \(66-26=40\), as stated.

## Verification
The standalone Python 3 file `affine_distance_kernel_verifier.py` uses SymPy and NumPy. Running `python affine_distance_kernel_verifier.py` verifies exact symbolic determinant factorizations, the radical root ordering and zeros, and direct finite-instance diagnostics of all distance classes, spectral multiplicities and boundary ranks. The examples are affine point–hyperplane incidence structures over \(\mathbb F_2^2\), \(\mathbb F_2^3\), \(\mathbb F_3^2\), and \(\mathbb F_3^3\). These finite computations check implementation, while the proof above establishes the assertions for all existing affine resolvable designs.

## Relationship to prior work
Ma's 2016 preprint *The distance signatures of the incidence graphs of affine resolvable designs* establishes the distance-matrix inertia and supplies the affine-design incidence identities. It does not classify positive semidefiniteness for arbitrary five-parameter radial kernels, nor identify the disconnected bandwidth intervals. The generalized-distance spectral method of DeVille (2017) addresses distance-regular graphs and their Cartesian products; the present incidence graphs are biregular (their point degree \(r\) and block degree \(k\) differ). Furthermore their distance-class matrices do not generally commute: on the \(B_1\) sector the distance-one and distance-two matrices restrict to \(\begin{pmatrix}0&\sqrt{k}\\\sqrt{k}&0\end{pmatrix}\) and \(\begin{pmatrix}-1&0\\0&0\end{pmatrix}\), respectively. Thus neither the distance-regular method nor the commuting-distance-matrix criterion in DeVille directly supplies this classification. The proof here uses the exact affine-design incidence decomposition rather than an automorphism-transitive hypothesis.

## Limitations
The result assumes an existing finite affine resolvable design. It neither classifies existence of designs for given \((n,\mu)\) nor describes non-distance-radial kernels. It classifies real symmetric positive semidefinite matrices but not the determinants or condition numbers throughout the entire cone. Literature comparisons are bounded: an equivalent older association-scheme or coherent-configuration specialization may exist.

## References
1. J. Ma, *The distance signatures of the incidence graphs of affine resolvable designs*, arXiv:1604.08922, first posted 2016-04-29, https://arxiv.org/abs/1604.08922.
2. L. DeVille, *The generalized distance spectrum of a graph and applications*, arXiv:1708.02294, first posted 2017-08-07, https://arxiv.org/abs/1708.02294.
3. D. Clark, D. Jungnickel and V. D. Tonchev, *Exponential bounds on the number of designs with affine parameters*, Journal of Combinatorial Designs **18** (2010), 475–487, DOI: 10.1002/jcd.20256.
