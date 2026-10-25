# A sharp Gaussian positive-definiteness dimension cutoff on Boolean Hamming cubes

## Finding
Let \(Q_d=(\mathbb Z/2\mathbb Z)^d\) carry Hamming distance \(h(x,y)\), and let \(0<q\le 1/16\). The intrinsic squared-Hamming Gaussian kernel is
\[
K_{d,q}(x,y)=q^{h(x,y)^2}=\exp[-(-\log q)h(x,y)^2].
\]
Put \(m=\lfloor q^{-1}\rfloor\) and
\[
B_d(q)=\sum_{j=0}^{d}(-1)^j\binom dj q^{j^2}.
\]
Then the entire positive-semidefiniteness classification is
\[
\begin{array}{c|c}
\text{dimension}&\text{kernel status}\\\hline
1\le d\le m&\text{strictly positive definite}\\
d=m+1&\text{positive semidefinite exactly when }B_{m+1}(q)\ge0\\
d\ge m+2&\text{not positive semidefinite}.
\end{array}
\]
At the exceptional equality \(B_{m+1}(q)=0\), the full \(2^{m+1}\)-point Gram matrix has rank \(2^{m+1}-1\), with kernel spanned by the parity Walsh character. In every dimension \(d\le m+1\), the parity Walsh character has the unique smallest Fourier eigenvalue.

Equivalently, for each fixed integer \(d\ge17\) there is a **unique** critical parameter \(q_d\in(1/d,1/(d-1))\), specified by \(B_d(q_d)=0\). For \(0<q\le1/16\), \(K_{d,q}\) is positive semidefinite if and only if \(q\le q_d\), and at equality has rank \(2^d-1\). The thresholds obey
\[
q_d=\frac1d+\frac{1}{2d^3}+O(d^{-4})\qquad(d\to\infty).
\]
For \(1\le d\le16\), every \(0<q\le1/16\) is strictly admissible.

## Assumptions and scope
The parameter \(q\) is real and restricted to \((0,1/16]\); no claim is made about the complementary weak-damping interval. Hamming distance is the number of unequal coordinates, *not* the Euclidean chordal distance. All matrix claims concern the complete vertex set of \(2^d\) binary strings, so positive definiteness means positivity of every finite Gram submatrix. Fourier eigenvalues below use the **unnormalized** character transform; multiplying every eigenvalue by \(2^{-d}\) has no effect on signs.

## Proof
Write \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) for a Walsh character with \(|S|=k\). Translation invariance gives the eigenvalue
\[
\lambda_{d,k}(q)=\sum_{j=0}^d q^{j^2}\sum_{a=\max(0,j-d+k)}^{\min(k,j)}(-1)^a\binom ka\binom{d-k}{j-a}.
\]
Its zero- and one-weight terms are \(1+(d-2k)q\). The parity eigenvalue is \(\lambda_{d,d}=B_d(q)\). Define \(R_d(q)=\sum_{j=2}^d\binom djq^{j^2}\). For \(dq\le2\), since \(j^2\ge j+2\) for \(j\ge2\),
\[
0\le R_d(q)\le q^2\big((1+q)^d-1-dq\big)
\le (e^2-3)q^2<q\quad(0<q\le1/16).
\]
The nontrivial inequality is strict because \((e^2-3)/16<1\). Thus, whenever \(dq\le2\),
\[
\lambda_{d,k}-B_d\ge2(d-k)q-2R_d>0\quad(0\le k<d).
\]
Consequently all signs are governed by the **single parity eigenvalue**.

For \(d\le m\) one has \(dq\le1\). Set \(T_j=\binom dj q^{j^2}\). For \(j\ge2\), as long as \(j<d\),
\[
\frac{T_{j+1}}{T_j}=\frac{d-j}{j+1}q^{2j+1}
\le\frac{dq}{j+1}q^{2j}<1.
\]
Hence \(T_2-T_3+T_4-\cdots>0\) when \(d\ge2\), and \(B_d=1-dq+(T_2-T_3+\cdots)>0\). The cases \(d=1\) are immediate. For \(d=m+1\), \(dq\le1+q<2\), so the parity-minimum comparison gives the asserted exact single-polynomial test and corank-one equality case. At \(d=m+2\), \(dq>1+q\), while \(dq\le1+2q<2\). Thus
\[
B_{m+2}\le1-(m+2)q+R_{m+2}<-q+R_{m+2}<0.
\]
Every larger cube contains a coordinate subcube of dimension \(m+2\), so the obstruction persists by principal-submatrix restriction.

For fixed \(d\ge17\), the proven classification shows strict positivity at \(q=1/d\) and failure at \(q=1/(d-1)\). On that interval \(q\le1/16\) and \(dq\le2\). Differentiating the parity polynomial and bounding the non-linear terms gives
\[
\frac{1}{d}\left|B'_d(q)+d\right|
\le q^2\left((1+q)^{d-1}+(d-1)q(1+q)^{d-2}-1\right)
\le q^2(3e^2-1)<1.
\]
Here \(j^2-1\ge j+1\) for \(j\ge2\) bounds the differentiated tail. Thus \(B_d'(q)<0\), proving the unique threshold \(q_d\). Above \(1/(d-1)\) the dimension cutoff already implies failure; below \(1/d\) it implies strict positivity. Finally, at \(q=1/d\),
\[
B_d(1/d)=\binom d2d^{-4}+O(d^{-6})
=\frac1{2d^2}-\frac1{2d^3}+O(d^{-6}).
\]
The derivative satisfies \(B_d'(q)=-d+O(d^{-1})\) uniformly for \(q=1/d+O(d^{-3})\). The previous bracket yields \(q_d-1/d=O(d^{-3})\), and the mean-value theorem gives the stated expansion.

## Verification
The standalone `check.py` reconstructs every Walsh eigenvalue both from Krawtchouk coefficients and from direct vertex-by-vertex character summation in small cubes, using rational arithmetic. It also tests minimum-eigenvalue ordering in dimensions close to the dimension cutoff and brackets four unique critical roots with 70-digit working precision. Its exact and high-precision tests are supplements to the uniform inequalities above and do not claim exhaustive enumeration of unbounded dimensions.

## Relationship to prior work
Harrow–Kolla–Schulman (arXiv:1209.4148, first publicly available 2012-09-19) provide the classical Walsh/Krawtchouk harmonic framework for Hamming spheres, but investigate spherical maximal operators rather than the positive-definiteness threshold for \(q^{h^2}\). Feragen–Lauze–Hauberg (arXiv:1411.0296, first public 2014-11-02) analyze when intrinsic Gaussian kernels remain positive definite across geodesic spaces; their all-bandwidth geometric restrictions do not give a finite binary-cube cutoff or the parity eigenvalue. Jayasumana and coauthors (arXiv:1412.0265, first public 2014-11-30) give a general metric-space Gaussian positive-definiteness framework, not the present discrete sharp threshold. This finding supplies a quantitative finite-dimensional boundary that those statements do not directly imply.

## Limitations
The phase diagram is proved only for \(0<q\le1/16\), equivalent to damping \(-\log q\ge\log16\). The formula does not assert a closed elementary form for the roots \(q_d\); it specifies each uniquely by a finite polynomial. No independent external mathematical audit or exhaustive publication search has been performed. Published literature may contain an equivalent characterization under another formulation.

## References
1. A. W. Harrow, A. Kolla, L. J. Schulman, *Dimension-free L2 maximal inequality for spherical means in the hypercube*, arXiv:1209.4148 (first public 2012-09-19); *Theory of Computing* **10** (2014), 55–75. https://arxiv.org/abs/1209.4148
2. A. Feragen, F. Lauze, S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296 (first public 2014-11-02). https://arxiv.org/abs/1411.0296
3. S. Jayasumana, R. Hartley, M. Salzmann, H. Li, M. Harandi, *Kernel Methods on Riemannian Manifolds with Gaussian RBF Kernels*, arXiv:1412.0265 (first public 2014-11-30). https://arxiv.org/abs/1412.0265
