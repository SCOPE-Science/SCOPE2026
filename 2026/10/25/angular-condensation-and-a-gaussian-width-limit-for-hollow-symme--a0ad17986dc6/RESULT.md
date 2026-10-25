# Angular condensation and a Gaussian-width limit for hollow symmetric Monge simplices

## Finding
For each integer \(n\ge 3\), let \(\mathcal H_n\) be the **hollow symmetric Monge polytope**: the symmetric real \(n\times n\) matrices \(C=(c_{ij})\) satisfying \(c_{ii}=0\), \(c_{ij}\ge0\), \(\sum_{i,j}c_{ij}=1\), and
\[
 c_{ij}+c_{k\ell}\le c_{i\ell}+c_{kj}
 \quad(i<k,\ j<\ell).
\]
Use the ambient Frobenius inner product restricted to the affine hull. If \(U_n\) is uniform on the unit sphere of its direction space, write \(W_n\) for the width of \(\mathcal H_n\) in direction \(U_n\).

Let \((\xi_{ij})_{i,j\ge1}\) be independent standard normal variables, and define
\[
 Z_{a,b}=\frac{1}{ab}\sum_{i=1}^{a}\sum_{j=1}^{b}\xi_{ij},\qquad
 R=\sup_{a,b\ge1}Z_{a,b}-\inf_{a,b\ge1}Z_{a,b}.
\]
Then \(R\) is finite, positive, nonconstant and has finite moments of every positive order. There is a joint coupling of the random directions in all dimensions such that
\[
 \boxed{\quad nW_n\longrightarrow R\quad\text{almost surely.}\quad}
\]
In particular, \(nW_n\Rightarrow R\), and for every fixed real \(s>0\),
\[
 \boxed{\quad\lim_{n\to\infty}n^s\,\mathbb E[W_n^s]=\mathbb E[R^s].\quad}
\]
The limiting width law is non-Gaussian.

The vertices of \(\mathcal H_n\) are indexed by \((a,b)\in\mathbb N^2\) with \(a+b\le n\), as in Erickson--Kretschmann. In the same coupling, both the maximizing and minimizing vertex indices become **exactly constant** for all sufficiently large \(n\), almost surely. Hence the spherical normal-cone mass is tight on fixed finite sets of block indices, although the total number of vertices diverges quadratically. In particular, the probability that the maximizer is a vertex of the distinguished metric face \(a+b=n\) tends to zero.

For the smallest block \((a,b)=(1,1)\), its normalized spherical normal-cone angle \(\omega_{n,1,1}\) decreases strictly from \(\omega_{3,1,1}=1/3\) and converges to a **strictly positive** limit. Explicitly, with \(\Phi\) the standard normal distribution function and
\[
 T=\sup_{\substack{a,b\ge1\\ab\ge2}}
 \frac{\displaystyle\sum_{\substack{1\le i\le a,\ 1\le j\le b\\ (i,j)\ne(1,1)}}\xi_{ij}}{ab-1},
\]
we have the exact angular identity
\[
 \boxed{\quad\lim_{n\to\infty}\omega_{n,1,1}
 =\mathbb E[1-\Phi(T)]\in(0,1/3).\quad}
\]
Thus at least one vertex retains macroscopic spherical normal-cone mass, in contrast to the vanishing individual vertex angles of a regular simplex with an increasing number of vertices.

## Assumptions and scope
The normalization \(\sum c_{ij}=1\), symmetric zero diagonal, the Frobenius metric and the **intrinsic** spherical direction space are essential. The assertion is for all integers \(n\ge3\). No Euclidean volume or arbitrary nonsymmetric Monge polytope is covered. All limit laws refer to the stated canonical Euclidean embedding, not affine-equivalence classes.

The dimension of \(\mathcal H_n\) is \(d_n=n(n-1)/2-1\). For \(a+b\le n\), the vertex \(v_{a,b}^{(n)}\) has entries \(1/(2ab)\) on the two transposed corner rectangles \([1,a]\times[n-b+1,n]\) and \([n-b+1,n]\times[1,a]\), and zero elsewhere. This vertex description and the simplex property are established in Erickson--Kretschmann, Proposition 4.1 and Proposition 4.2, and are not claimed as new here.

## Proof
**1. Exact Gaussian representation.** Identify the linear space of hollow symmetric matrices with \(\mathbb R^{m_n}\), where \(m_n=n(n-1)/2\), by the orthonormal Frobenius basis \((E_{ij}+E_{ji})/\sqrt2\) for \(i<j\). For each \(n\), use the same infinite Gaussian array \((\xi_{i,k})\) by assigning coordinate \(\xi_{i,n+1-j}\) to the pair \(i<j\). This assignment is a bijection between pairs \(i<j\) and indices \(i,k\ge1\) satisfying \(i+k\le n\). It gives an isotropic Gaussian matrix \(G_n\) in the hollow symmetric space and, by the established vertex formula,
\[
 \langle G_n,v_{a,b}^{(n)}\rangle_F
 =\frac{1}{\sqrt2\,ab}\sum_{i\le a,k\le b}\xi_{i,k}
 =\frac{Z_{a,b}}{\sqrt2}.
\]
Thus its Gaussian width is exactly \(R_n/\sqrt2\), where
\[
 R_n=\max_{a+b\le n}Z_{a,b}-\min_{a+b\le n}Z_{a,b}.
\]
Projection of \(G_n\) onto the hyperplane tangent to \(\sum c_{ij}=1\) subtracts a scalar from every vertex support value, so it does not change either width or exposed vertices. Denote this projected Gaussian by \(G_n^\circ\); \(U_n=G_n^\circ/\lVert G_n^\circ\rVert_F\) is a uniform intrinsic unit direction. Consequently the following finite-dimensional identity is exact:
\[
 W_n=\frac{R_n}{\sqrt2\,\lVert G_n^\circ\rVert_F}.
\]

**2. Finite and attained Gaussian extrema.** Each \(Z_{a,b}\) is centered Gaussian of variance \(1/(ab)\). For every \(\varepsilon>0\), the Gaussian bound gives
\[
 \sum_{a,b\ge1}\Pr\{|Z_{a,b}|>\varepsilon\}
 \le2\sum_{a,b\ge1}e^{-\varepsilon^2ab/2}<\infty.
\]
By Borel--Cantelli, \(Z_{a,b}\to0\) almost surely as \(a+b\to\infty\). Along the first row the unnormalized sums \(\sum_{j\le b}\xi_{1j}\) are a Gaussian random walk; its classical law of the iterated logarithm supplies both a positive and a negative partial sum almost surely. Thus \(\sup Z_{a,b}>0\) and \(\inf Z_{a,b}<0\) almost surely. Both extrema are therefore attained at **finite** index pairs. Every difference between two distinct rectangle averages is a nondegenerate Gaussian linear form, so a countable union bound excludes ties. Hence the two infinite optimizing pairs exist and are unique almost surely. Since indices with large \(a+b\) have scores tending to zero, both unique finite optimizers must maximize/minimize every sufficiently large triangular truncation. This proves exact eventual stabilization and \(R_n\uparrow R\) almost surely.

Moreover, for \(t\ge1\),
\[
 \Pr\{\sup_{a,b}|Z_{a,b}|>t\}
 \le 2e^{-(t^2-1)/2}\sum_{a,b\ge1}e^{-ab/2}.
\]
Hence \(R\le2\sup|Z_{a,b}|\) has moments of every positive order. Since \(R\ge|\xi_{11}|\), it is unbounded and not constant. Being strictly positive, its distribution cannot be Gaussian.

**3. Spherical normalization and moments.** Enumerate the array entries in increasing order of \(i+j\). The sets \(i+j\le n\) are nested initial segments of length \(m_n\). If \(\overline\xi_n\) is their average, orthogonal projection gives
\[
 \lVert G_n^\circ\rVert_F^2
 =\sum_{i+j\le n}\xi_{ij}^2-m_n\overline\xi_n^2.
\]
The strong laws for the two sample means imply
\(\lVert G_n^\circ\rVert_F/n\to1/\sqrt2\) almost surely. Combining this with the exact identity of Step 1 and \(R_n\to R\) proves the almost-sure width limit.

For moments, Gaussian polar decomposition makes \(\lVert G_n^\circ\rVert_F\) (a chi variable with \(d_n\) degrees of freedom) independent of its direction. For all fixed \(s>0\),
\[
 \mathbb E[W_n^s]
 =\frac{\mathbb E[R_n^s]}{2^{s/2}\,\mathbb E[\chi_{d_n}^{s}]},
 \qquad
 \mathbb E[\chi_d^s]=2^{s/2}\frac{\Gamma((d+s)/2)}{\Gamma(d/2)}.
\]
Monotone convergence gives \(\mathbb E[R_n^s]\uparrow\mathbb E[R^s]\), while the gamma ratio and \(d_n\sim n^2/2\) prove the stated moment limits.

**4. The persistent corner normal cone.** The event that \((1,1)\) maximizes all rectangle averages is, after conditioning on the Gaussian coordinates other than \(\xi_{11}\), precisely \(\xi_{11}\ge T\). The coordinates defining \(T\) are independent of \(\xi_{11}\). The same summable Gaussian tail argument shows \(T<\infty\) almost surely; the first-row Gaussian walk shows \(T>0\) almost surely. Thus \(\Pr\{(1,1)\text{ wins}\}=\mathbb E[1-\Phi(T)]>0\). For the triangle \(n=3\), the corner wins precisely when \(\xi_{11}\) is the largest among \(\xi_{11},\xi_{12},\xi_{21}\), yielding \(1/3\). Increasing \(n\) adds competitors to the same Gaussian field, so \(\omega_{n,1,1}\) decreases. The decrease is strict: the new rectangle \((1,n)\) contains a fresh independent normal \(\xi_{1,n}\), which can be large enough to defeat the corner on a positive-probability event where the corner beat all older rectangles. In particular, the limiting angle lies in \((0,1/3)\).

Finally, the source characterizes the metric face by \(a+b=n\). Since the maximizing index eventually stabilizes at a fixed finite pair, it belongs to that moving boundary with probability tending to zero by dominated convergence.

## Verification
The standalone `CHECK.py` reconstructs normalized block vertices and independent Frobenius Gaussian coordinates. With a fixed pseudorandom seed it checked 576 Gaussian support identities, projection-invariant widths, and normalized spherical widths for dimensions \(3\) through \(10\), without numerical discrepancies at the displayed tolerance. It also ran 4,800 finite Gaussian-array experiments with triangle cutoff \(95\), observing a sample mean range of approximately \(1.47\) and a positive observed corner-winning frequency. These finite computations test the exact finite-dimensional reductions; they do not establish the infinite limit, uniqueness, or the positive limiting angle. The argument in the Proof supplies those statements.

To reproduce, run `python CHECK.py` with NumPy installed. No network access is required by the checker.

## Relationship to prior work
Erickson and Kretschmann (arXiv:2311.07522, first publicly submitted 2023-11-13) defined these Monge polytopes, established their vertex sets and simplex structure in Propositions 4.1--4.2, computed normalized volumes in Theorem 4.4, and described the distinguished metric face in Proposition 4.6. The present statement uses their canonical vertex coordinates but instead determines a high-dimensional **Euclidean random-width law and angular exposure localization**. The original vertex, volume, and metric-face theorems do not imply either the almost-sure stabilized Gaussian extremizers or the persistent corner solid angle without the new Gaussian analysis. A later treatment by Erickson and Jones (arXiv:2609.09508) studies normalized volume and Ehrhart enumeration for **generic nonsymmetric** Monge polytopes, not the directional widths or corner-block angles studied here. Classical Gaussian-walk oscillation, the strong law, and Gaussian tail bounds are acknowledged as standard probabilistic input.

## Limitations
No closed elementary formula is proved for the distribution or expectation of \(R\), or for the exact limiting corner angle. The finite simulation estimate is not an exact constant. The theorem does not give a rate of convergence or classify the angular probabilities of every finite block in closed form. It applies only to the stated hollow **symmetric** Monge simplex and the fixed Frobenius normalization; affine equivalence alone does not preserve spherical angles. The claim has not undergone independent mathematical audit, and an equivalent result in unindexed probabilistic or convex-geometric literature cannot be ruled out by finite literature searches.

## References
1. W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522v1 (2023-11-13), revised as arXiv:2311.07522v2 (2023-11-14), Sections 3--4, especially Propositions 4.1--4.2, Theorem 4.4 and Proposition 4.6. https://arxiv.org/abs/2311.07522
2. Classical Gaussian random-walk law of the iterated logarithm, Gaussian tail inequality, Borel--Cantelli lemma and strong law of large numbers (standard probability results used as stated above).
3. W. Q. Erickson and N. B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508v1 (2026-09-08), introduction and principal volume/Ehrhart statements. https://arxiv.org/abs/2609.09508
