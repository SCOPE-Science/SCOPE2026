# Exact degree-two Slepian spectrum on spherical orthants

## Finding
For every integer \(n\ge3\), put \(S^{n-1}=\{x\in\mathbb R^n:\|x\|=1\}\), equip it with probability-normalized surface measure \(\sigma\), and let \(W_n=\{x\in S^{n-1}:x_i>0\text{ for every }i\}\). Let \(\mathcal H_2^{(n)}\) be the complex space of restrictions of homogeneous harmonic quadratic polynomials. The compression \(T_n=P_{\mathcal H_2^{(n)}}1_{W_n}|_{\mathcal H_2^{(n)}}\) has **exactly the following spectral branches**, with multiplicities as stated.

Write \(s=2/\pi\), and set
\[
\begin{aligned}
T&=1+2(n-2)s+\frac{(n-2)(n-3)}2s^2,\\
a&=1+(n-4)s-(n-3)s^2,\\
b&=s\sqrt{\frac{n-2}{2}},\qquad e=(1-s)^2,\\
r_\pm&=\frac{1+a\pm\sqrt{(1-a)^2+4b^2}}2.
\end{aligned}
\]
The eigenvalues are \(2^{-n}T\) (multiplicity one), \(2^{-n}r_+\) (multiplicity \(n-1\)), \(2^{-n}r_-\) (multiplicity \(n-1\)), and, when \(n\ge4\), \(2^{-n}e\) (multiplicity \(n(n-3)/2\)). In every dimension the largest eigenvalue is uniquely \(\Lambda_n=2^{-n}T\). For \(n\ge4\) their strict order is
\[
2^{-n}T>2^{-n}r_+>2^{-n}e>2^{-n}r_-;
\]
for \(n=3\) the absent \(e\)-branch is omitted.

Consequently, **for every nonzero complex \(f\in\mathcal H_2^{(n)}\)**,
\[
\boxed{\quad\int_{W_n}|f|^2\,d\sigma\ \le\ \Lambda_n\int_{S^{n-1}}|f|^2\,d\sigma,\qquad
\Lambda_n=2^{-n}\left(1+\frac{4(n-2)}\pi+\frac{2(n-2)(n-3)}{\pi^2}\right).\quad}
\]
Equality holds precisely for nonzero complex scalar multiples of
\[
Q_n(x)=\sum_{1\le i<j\le n}x_ix_j
=\frac12\left[\left(\sum_{i=1}^n x_i\right)^2-1\right].
\]
Thus the unique maximizer is the zonal quadratic aligned with the orthant's diagonal, although the orthant is not rotationally symmetric. Writing \(P_Q\) for orthogonal projection onto the complex line spanned by \(Q_n\), the **exact sharp stability inequality** is
\[
\Lambda_n\|f\|_2^2-\int_{W_n}|f|^2\,d\sigma
\ \ge\ 2^{-n}(T-r_+)\|f-P_Qf\|_2^2.
\]
Finally the volume of the orthant is \(2^{-n}\), while
\[
\lim_{n\to\infty}\frac{\Lambda_n}{n^2 2^{-n}}=\frac{2}{\pi^2},\qquad
\lim_{n\to\infty}\frac1n\frac{\Lambda_n}{2^{-n}r_+}=\frac1{\pi-2}.
\]
Hence the best degree-two harmonic gains a **quadratic-in-dimension** factor over uniform energy allocation, whereas the largest-to-second-largest spectral ratio grows linearly.

## Assumptions and scope
All integrals are with probability-normalized spherical surface measure, and the orthant's boundary has measure zero. The frequency space consists of **degree exactly two**, not all degrees at most two; arbitrary complex coefficients are allowed. The matrix formulas apply for every integer \(n\ge3\), with no large-dimension or regularity assumption on \(f\). The statement is invariant under orthogonal coordinate changes that rotate \(W_n\).

## Proof
**1. Full-sphere orthonormal splitting.** For a unit vector uniformly distributed on \(S^{n-1}\), the fourth moments are
\[
\mathbb E[x_i^4]=\frac3{n(n+2)},\qquad
\mathbb E[x_i^2x_j^2]=\frac1{n(n+2)}\quad(i\ne j).
\]
Put \(c_D=\sqrt{n(n+2)/2}\), \(c_E=\sqrt{n(n+2)}\). For every \(v\in\mathbb C^n\) satisfying \(\sum_i v_i=0\), write
\(D_v(x)=c_D\sum_i v_i x_i^2\); for each unordered pair \(ij\), write \(E_{ij}(x)=c_E x_ix_j\). The map \(v\mapsto D_v\) is an isometry on the standard \((n-1)\)-dimensional sum-zero subspace; the \(E_{ij}\) are orthonormal; and the diagonal and off-diagonal families are orthogonal. They form the whole traceless symmetric-matrix space \(\mathcal H_2^{(n)}\), of complex dimension \((n-1)(n+2)/2\).

**2. Orthant moments.** For nonnegative exponents \(\alpha_i\) with total \(k\), symmetry and the Dirichlet distribution of squared sphere coordinates give the exact formula
\[
\int_{W_n}\prod_i x_i^{\alpha_i}\,d\sigma
=2^{-n}\frac{\Gamma(n/2)}{\Gamma((n+k)/2)}
\prod_i\frac{\Gamma((\alpha_i+1)/2)}{\Gamma(1/2)}.
\]
For the fourth-degree moments relevant here, the full Gram matrix of the local inner product is \(2^{-n}\) times a block matrix \(M\). The diagonal block on sum-zero \(v\) is the identity. Let \(\mathcal E\) be the set of unordered coordinate pairs, and let \(R:\mathbb C^{\mathcal E}\to\mathbb C^n\) be the unsigned vertex-edge incidence map: \((Ru)_i=\sum_{j\ne i}u_{\{i,j\}}\). Let \(J\) be the all-ones matrix on edges. With \(s=2/\pi\), the edge block has entries \(1\) for equal edges, \(s\) for edges sharing one vertex, and \(s^2\) for disjoint edges. Therefore it is exactly
\[
B=(1-s)^2I+s(1-s)R^*R+s^2J.
\]
The diagonal-edge coupling is
\[
\langle D_v,E_{ij}\rangle_{W_n}
=2^{-n}\frac{s}{\sqrt2}(v_i+v_j).
\]
After factoring out \(2^{-n}\), the coupling operator is thus \((s/\sqrt2)R^*\) on sum-zero vectors. These are explicit computations from the preceding gamma identity; no numerical approximation is used.

**3. Finite-dimensional reduction.** For \(n\ge3\), \(RR^*=(n-2)I+J_n\) and \(R\) has full row rank. The edge space splits orthogonally as: the constant edge line; the image of the sum-zero coordinate subspace under \(R^*\), of dimension \(n-1\); and \(\ker R\), of dimension \(n(n-3)/2\) (zero when \(n=3\)). Both the coupling and \(B\) preserve this splitting. On constants, \(B\) acts by \(T\); on \(\ker R\), it acts by \(e=(1-s)^2\). On each of \(n-1\) mutually orthogonal pairs of one diagonal mode and the corresponding normalized edge mode, \(M\) is exactly
\[
\begin{pmatrix}1&b\\b&a\end{pmatrix},\qquad
b=s\sqrt{(n-2)/2},\quad a=1+(n-4)s-(n-3)s^2.
\]
Its two eigenvalues are \(r_\pm\). The branch dimensions add to \((n-1)(n+2)/2\), so this exhausts the complex spectrum and proves all multiplicities.

**4. Ordering, optimizer, and stability.** Since \(0<s<1\), \(r_+\le\max\{1,a\}+b\). But
\[
T-1=2(n-2)s+\frac{(n-2)(n-3)}2s^2>b,
\quad
T-a=ns+\frac{n(n-3)}2s^2>b
\]
for every \(n\ge3\). Thus \(T>r_+\); also \(r_+\ge1>(1-s)^2=e\). To order the remaining branches observe
\[
\det\left(\begin{pmatrix}1&b\\b&a\end{pmatrix}-eI\right)
=\frac{(n-2)s^2}{2}\,(2s^2-6s+3)<0.
\]
The last sign follows from \(s=2/\pi\) and \(3<\pi<22/7<2+2\sqrt3/3\). Therefore \(r_-<e<r_+\). The constant edge eigenvector corresponds to \(Q_n\), giving the unique top eigenspace and the sharp inequality. The spectral theorem gives the stability inequality; it is sharp because an \(r_+\)-eigenvector realizes equality in the associated gap estimate.

**5. Asymptotics.** The explicit polynomial \(T\) has leading term \(2n^2/\pi^2\). Since \(a=ns(1-s)+O(1)\), \(b^2=ns^2/2+O(1)\), and \(s(1-s)>0\), the upper eigenvalue satisfies \(r_+=ns(1-s)+O(1)\). The displayed two limits follow.

## Verification
The accompanying `verify_orthant.py` independently builds local Gram matrices from gamma-integrated monomials, without inserting the displayed spectral formula into their entries. In dimensions \(3\) through \(10\), it compares their full numerical spectra, dimensions, and traces with the theorem. For \(n=3\), a separate two-dimensional Gauss-Legendre quadrature over the spherical octant provides an independent surface-integral check. Symbolic algebra independently verifies the trace decomposition and two polynomial ordering identities. Run `python verify_orthant.py` with Python 3, NumPy and SymPy installed. The archived `verification_output.txt` records one successful execution. These finite checks are diagnostic; the universal assertion follows from the analytic gamma and incidence-matrix derivation above.

## Relationship to prior work
The spherical spatial-spectral (Slepian) concentration eigenproblem and general-region concentration matrices are established in Simons–Dahlen–Wieczorek (2006), Bates–Khalid–Kennedy (2016/2017), and Michel–Plattner–Seibert (2021). The first two authors' sphere results and the 2017 colatitude-longitude formulation cover the **procedure** of forming and diagonalizing concentration matrices for arbitrary two-sphere patches, including an octant, but their inspected formulations do not state this all-dimensional orthant quadratic spectrum, its one-dimensional zonal optimizer, or its sharp gap and asymptotic enhancement. The 2021 paper develops scalar/vector/tensor Slepian constructions and cap commuting operators rather than an orthant formula. The present result uses familiar finite-dimensional spectral machinery; the asserted contribution is the explicit family-wide classification and extremal geometry, not invention of Slepian concentration or the matrix reduction itself.

## Limitations
The theorem is limited to exact harmonic degree two and equal-threshold coordinate orthants. It gives no formula for arbitrary polyhedral cones or higher harmonic degrees. Prior matrix formulations can compute special low-dimensional examples numerically; the claim is an explicit universal formula, equality rigidity, and sharp gap, not uniqueness of the underlying technique. An equivalent all-dimensional formula in unindexed older literature cannot be ruled out by bibliographic searches. The computation script does not independently prove the all-dimension theorem or certify bibliographic novelty.

## References
1. V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650, first posted 2021-03-26; especially Sections 3.1–3.3 and 5.
2. A. P. Bates, Z. Khalid, R. A. Kennedy, *Slepian Spatial-Spectral Concentration Problem on the Sphere: Analytical Formulation for Limited Colatitude-Longitude Spatial Region*, arXiv:1608.03031 (2016), IEEE Transactions on Signal Processing **65** (2017), 1527–1537; DOI 10.1109/TSP.2016.2646668, especially Sections III–V.
3. A. Aslam, Z. Khalid, *Spatial-Slepian Transform on the Sphere*, arXiv:2010.07266, first posted 2020-10-14; especially Section II-D.
4. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral Concentration on a Sphere*, SIAM Review **48** (2006), 504–536; DOI 10.1137/S0036144504445765.
