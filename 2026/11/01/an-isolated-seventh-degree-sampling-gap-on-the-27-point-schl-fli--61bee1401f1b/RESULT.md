# An isolated seventh-degree sampling gap on the 27-point Schläfli design

## Finding

Let \(X\subset S^5\) be the 27-point Schläfli spherical configuration defined explicitly below. For every integer \(k\geq0\), let \(E_k\) evaluate all (complex or real) homogeneous spherical harmonics of **exact** degree \(k\) on \(X\). Its evaluation ranks are
\[
\operatorname{rank}E_k=\begin{cases}
1&k=0,\\
6&k=1,\\
20&k=2,3,\\
26&k=4,7,\\
27&k=5,6\text{ or }k\geq8.
\end{cases}
\]
Thus degree \(5\) is the first surjective individual harmonic degree, degree \(7\) is an *isolated later failure* of surjectivity, and all degrees \(k\geq8\) are surjective. The configuration annihilates sums of exact-degree harmonics precisely in the positive degrees \(\{1,2,3,4,7\}\). In particular it has an additional harmonic-index-seven cancellation beyond its classical spherical four-design strength.

More precisely, put \(P_k(t)=C_k^{(2)}(t)/C_k^{(2)}(1)\), where \(C_k^{(2)}\) is the Gegenbauer polynomial with parameter \(2\), and write \(a_k=P_k(1/4)\), \(b_k=P_k(-1/2)\). The normalized degree-\(k\) sampling Gram matrix \(B_k=(P_k(x\cdot y))_{x,y\in X}\) has **exactly** the following eigenvalue sectors, with their indicated multiplicities (coincident numerical eigenvalues combine):
\[
\lambda_{0,k}=1+16a_k+10b_k\quad(1),\qquad
\lambda_{4,k}=1+4a_k-5b_k\quad(6),\qquad
\lambda_{-2,k}=1-2a_k+b_k\quad(20).
\]
These formulas give the full spectrum, not just the rank, at every degree.

## Assumptions and scope

All coordinates below are Euclidean and points have unit norm. Let \(e_1,\ldots,e_5\) be the standard coordinate vectors of \(\mathbb R^5\); use notation \((u,v)\in\mathbb R^5\times\mathbb R\). Define
\[
X=\{(0,1)\}
\cup\{(\epsilon\sqrt3\,e_i/2,-1/2):1\leq i\leq5,\ \epsilon\in\{-1,1\}\}
\cup\{(\sqrt3\,\epsilon/4,1/4):\epsilon\in\{-1,1\}^5,\ \epsilon_1\cdots\epsilon_5=1\}.
\]
These are \(1+10+16=27\) distinct points of \(S^5\). Their distinct-point inner products are exactly \(1/4\) and \(-1/2\). Adjacency at inner product \(1/4\) is the Schläfli graph; each point has \(16\) adjacent and \(10\) nonadjacent points. The coordinates fix the orientation and remove any ambiguity about signs, normalizations or antipodal choices.

Write \(\mathcal H_k(S^5)\) for homogeneous harmonic-polynomial restrictions of exact degree \(k\), with orthonormality under probability-normalized area measure on \(S^5\). For such an orthonormal basis \(\{Y_j\}_{j=1}^{h_k}\), the addition formula gives \(\sum_jY_j(x)\overline{Y_j(y)}=h_kP_k(x\cdot y)\), with \(h_k=\binom{k+5}{5}-\binom{k+3}{5}\). Hence \(B_k=E_kE_k^*/h_k\), and its rank equals the evaluation rank. For \(k=0\), the second binomial term is understood as zero.

## Proof

**(1) Two-distance algebra.** Directly from the three coordinate classes in the definition, every point has norm one; distinct-point inner products lie in \(\{1/4,-1/2\}\). Let \(A\) be the \(27\)-by-\(27\) zero-diagonal matrix with \(A_{xy}=1\) precisely when \(x\cdot y=1/4\), and let \(J\) denote the all-ones matrix. Exact enumeration of the three coordinate classes (also exhaustively verified in `verify_schlaefli.py`) gives
\[
A\mathbf1=16\mathbf1,\qquad A^2=8I+2A+8J.
\]
The diagonal and off-diagonal entries respectively express the parameters \((27,16,10,8)\) of the Schläfli strongly regular graph. On \(\mathbf1^\perp\), \(A^2=8I+2A\), whose roots are \(4\) and \(-2\). Since \(\mathrm{tr}(A)=0\), the multiplicities are \(6\) for \(4\) and \(20\) for \(-2\); \(16\) has multiplicity one. This is an exact algebraic calculation, independent of floating-point eigenvalues.

**(2) Addition-kernel reduction.** For each degree \(k\), the addition theorem and the pairwise inner products give
\[
B_k=I+a_kA+b_k(J-I-A).
\]
On the three eigenspaces of \(A\), substitution yields \(\lambda_{0,k},\lambda_{4,k},\lambda_{-2,k}\) as displayed in the finding, with multiplicities \(1,6,20\). This is the complete spectrum because the three eigenspaces exhaust \(\mathbb C^{27}\). Each eigenvalue is nonnegative, as the addition theorem also realizes \(B_k\) as a positive-semidefinite Gram matrix.

**(3) Low degrees.** The normalization \(C_k^{(2)}(1)=\binom{k+3}{3}\) and the exact Gegenbauer recurrence
\[
C_0^{(2)}(t)=1,\quad C_1^{(2)}(t)=4t,\quad
kC_k^{(2)}(t)=2(k+1)tC_{k-1}^{(2)}(t)-(k+2)C_{k-2}^{(2)}(t)
\]
produce the following *rational* eigenvalue table for all \(0\leq k\leq8\):

| \(k\) | \(\lambda_{0,k}\) | \(\lambda_{4,k}\) | \(\lambda_{-2,k}\) | rank |
|---:|---:|---:|---:|---:|
| 0 | \(27\) | \(0\) | \(0\) | 1 |
| 1 | \(0\) | \(9/2\) | \(0\) | 6 |
| 2 | \(0\) | \(0\) | \(27/20\) | 20 |
| 3 | \(0\) | \(0\) | \(27/20\) | 20 |
| 4 | \(0\) | \(45/28\) | \(243/280\) | 26 |
| 5 | \(135/56\) | \(243/224\) | \(405/448\) | 27 |
| 6 | \(27/16\) | \(405/448\) | \(891/896\) | 27 |
| 7 | \(0\) | \(9/8\) | \(81/80\) | 26 |
| 8 | \(135/176\) | \(567/704\) | \(7533/7040\) | 27 |

In particular, the degree-seven failure affects **only** the one-dimensional constant-eigenvector sector.

**(4) No further rank loss.** Set \(t=\cos\theta\), \(-1<t<1\), and use the Chebyshev polynomial \(U_{k+1}(\cos\theta)=\sin((k+2)\theta)/\sin\theta\). The derivative identity \(C_k^{(2)}(t)=U_{k+1}'(t)/2\) gives
\[
|P_k(t)|\leq\frac{3}{(k+1)(k+2)(1-t^2)^{3/2}}.
\]
Indeed, differentiating the sine quotient gives a numerator bounded by \(|t|+(k+2)\sin\theta\leq k+3\), and division by \(2\binom{k+3}{3}\sin^3\theta\) yields the displayed bound. The strict rational comparisons \((16/15)^3<(10/9)^2\) and \((4/3)^3<(8/5)^2\) imply
\[
16|a_k|+10|b_k|
<\frac{3[16(10/9)+10(8/5)]}{(k+1)(k+2)}
=\frac{304}{3(k+1)(k+2)}.
\]
For every integer \(k\geq9\), this is at most \(304/330<1\). Each of the three eigenvalues differs from \(1\) by at most \(16|a_k|+10|b_k|\), hence **all three are strictly positive** for every \(k\geq9\). Combined with the exact table, this proves the all-degree ranks and the two distinct surjectivity thresholds.

**(5) Exact harmonic-index cancellations.** For \(k\geq1\), the addition theorem gives
\[
\lambda_{0,k}=\frac{1}{27h_k}\sum_{j=1}^{h_k}\left|\sum_{x\in X}Y_j(x)\right|^2.
\]
Thus the sum of *every* degree-\(k\) spherical harmonic over \(X\) vanishes exactly when \(\lambda_{0,k}=0\). The table and the strict high-degree bound show that the positive harmonic-index set is precisely \(\{1,2,3,4,7\}\).

## Verification

Run `python3 verify_schlaefli.py`. The standalone Python-3 standard-library script constructs all 27 points in a rational coordinate model (the first five coordinate axes represent an extra factor \(\sqrt3\)), checks all 729 exact inner products, checks all 729 entries of the strongly regular matrix identity, recursively computes normalized Gegenbauer values, verifies all three rational eigenvalues at degrees zero through eight, and independently performs exact rational row reduction of all nine full Gram matrices to check the claimed ranks. It finally checks the two rational inequalities used in the infinite-degree analytic estimate. The observed terminal marker is `SCHLAEFLI_ALL_DEGREE_CERTIFICATE_OK 27 points, 9 exact ranks`.

The checker verifies only the finite algebraic steps and the displayed rational envelopes; the displayed Chebyshev derivative argument is the proof for arbitrarily large harmonic degrees. It is not inferred from any finite computational range.

## Relationship to prior work

The Schläfli configuration is a known tight spherical four-design, and the inner products and their multiplicities have been determined in classical design theory; in particular, Boyvalenkov (1995) proves its uniqueness and the two-distance distribution. The addition-kernel formalism and harmonic-index design concept are standard, as in Bannai–Okuda–Tagami (2013) and Zhu–Bannai–Bannai–Kim–Yu (2015). Those results imply the familiar cancellations at degrees one through four, but the inspected material does not state the exact *all-degree* evaluation ranks, the isolated degree-seven rank loss, or the eventual full-rank threshold. The present claim is an explicit classification in this already-known configuration, not a new construction of the points or a new general addition formula.

The associated \(E_6\) invariant-theory degrees \(2,5,6,8,9,12\) are consistent with the missing seventh-degree invariant. That group-theoretic observation by itself neither determines the full degree-seven sampling rank nor certifies surjectivity at all higher degrees. Other all-degree sampling results for larger exceptional configurations do not imply the rank of the nonantipodal 27-point configuration, since both the point set and the ambient zonal Gegenbauer parameter differ.

## Limitations

The result concerns ordinary scalar spherical harmonics on the explicitly normalized 27-point configuration; it does not claim optimal numerical conditioning, weighted interpolation, or other polytopes. The rank and spectral conclusions have a complete exact proof, but an older equivalent rank calculation in exceptional association-scheme or cubature literature cannot be categorically excluded by the bounded source inspection. No independent mathematical audit has been performed.

## References

- Peter Boyvalenkov, *Computing distance distributions of spherical designs*, Linear Algebra and its Applications **226–228** (1995), 277–286, DOI `10.1016/0024-3795(95)00153-I`. Theorems 3.2 and 4.1 treat tight four-design distance distributions and the Schläfli configuration.
- Eiichi Bannai, Takayuki Okuda and Makoto Tagami, *Spherical designs of harmonic index t*, arXiv:`1308.5101v1` (first posted 2013-08-23), subsequently Journal of Approximation Theory **195** (2015), 1–18.
- Yan Zhu, Eiichi Bannai, Etsuko Bannai, Kyoung-Tark Kim and Wei-Hsuan Yu, *More on spherical designs of harmonic index t*, arXiv:`1507.05373` (first posted 2015-07-20), including the Gegenbauer addition-kernel setup and harmonic-index definitions.
- E. W. Weisstein, *Schläfli Graph*, MathWorld, for the graph's classical strongly regular parameters and adjacency spectrum (background reference).
