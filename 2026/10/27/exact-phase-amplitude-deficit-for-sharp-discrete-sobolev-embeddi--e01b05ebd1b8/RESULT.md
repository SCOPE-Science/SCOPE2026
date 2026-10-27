# Exact phase–amplitude deficit for sharp discrete Sobolev embeddings

## Finding
For every pair of integers \(\alpha\geq1\) and \(d\geq2\), the sharp finite-support \(\ell^1\)-to-difference-\(\ell^2\) inequality admits an exact decomposition of its squared deficit into two nonnegative quantities: a strictly weighted complete-graph energy of the coefficient phases and a squared Hilbert-energy distance to a phase-conditioned Green vector. In particular, the complex equality sequences are **exactly** the scalar multiples of the positive discrete Landau extremizer, and near-equality quantitatively forces phase alignment.

Write \(D:\mathbb C^d\to\mathbb C^{d+\alpha}\) for the zero-extended backward difference of order \(\alpha\), \(Q=D^*D\), \(G=Q^{-1}\), and \(C^2=\mathbf1^*G\mathbf1\). The entries of \(G\) are all **strictly positive**. For each \(a\in\mathbb C^d\), select \(s_j\in\mathbb T\) such that \(a_j=s_j|a_j|\) (arbitrary when \(a_j=0\)), and put \(u=\|a\|_1\), \(q=s^*Gs\), and \(E=\|Da\|_2^2\). Then
\[
\boxed{\displaystyle
 C^2E-u^2
 =E\sum_{1\le i<j\le d}G_{ij}|s_i-s_j|^2
 +q\left\|D\left(a-\frac{u}{q}Gs\right)\right\|_2^2.}
\]
The constant is the sharp published value
\[
C^2=\frac{\binom{d+2\alpha}{2\alpha+1}}{\binom{2\alpha}{\alpha}}.
\]
For nonzero \(a\), with \(m=\min_{i<j}G_{ij}>0\) and deficit \(\mathcal D=C^2E-u^2\), the phase-stability estimate is
\[
\min_{|\omega|=1}\sum_{j=1}^d|s_j-\omega|^2
\le \frac{2\mathcal D}{mdE}.
\]
Both identities hold for all real or complex input sequences; the displayed phase formulation uses complex unimodular phases and therefore also covers the real signs.

## Assumptions and scope
The integers \(\alpha,d\) are arbitrary with \(\alpha\ge1\), \(d\ge2\). Define \(a_j=0\) for all integer indices outside \(\{1,\ldots,d\}\), let \((\Delta a)_k=a_k-a_{k-1}\), and put \((Da)_k=(\Delta^\alpha a)_k\), \(1\le k\le d+\alpha\). Thus
\[
D_{kj}=\begin{cases}(-1)^{k-j}\binom\alpha{k-j},&0\le k-j\le\alpha,\\0,&\text{otherwise}.\end{cases}
\]
All matrix inverses are finite and ordinary. The inequality is homogeneous; the phase-stability estimate is asserted only when \(a\ne0\), so that \(E>0\). When a coordinate vanishes, any choice of its unimodular phase satisfies the exact identity and the estimate.

## Proof
**1. Green matrix and strict positivity.** The map \(D\) is injective: a finitely supported sequence annihilated by \(\Delta^\alpha\) is a polynomial sequence of degree below \(\alpha\), hence zero. Therefore \(Q=D^*D\) is positive definite and \(G\) exists. Vandermonde's convolution gives
\[
Q_{ij}=(-1)^{i-j}\binom{2\alpha}{\alpha+i-j},
\]
with binomial coefficients understood to vanish outside their usual range. Let \(S=\operatorname{diag}((-1)^1,\dots,(-1)^d)\). Then \(B=SQS\) has entries \(B_{ij}=\binom{2\alpha}{\alpha+i-j}\).

For clarity, we prove strict positivity of every entry of \(G\), not merely of its row sums. Regard \(B_{rc}\) as the number of lattice paths from position \(c\) at time zero to position \(r+\alpha\) at time \(2\alpha\), each step either holding position or increasing it by one. The nonintersecting-path determinant identity shows that every minor of \(B\) is nonnegative. More specifically, delete any one source indexed \(j\) and one sink indexed \(i\). Pair the remaining sources \(c_1<\cdots<c_{d-1}\) with the remaining sink indices \(r_1<\cdots<r_{d-1}\). Each displacement \(\alpha+r_k-c_k\) is one of \(\alpha-1,\alpha,\alpha+1\). A disjoint path family can be explicitly chosen as follows: all paths increase at each of the first \(\alpha-1\) time steps; at time \(\alpha\), only those with displacement at least \(\alpha\) increase; at time \(\alpha+1\), only those with displacement \(\alpha+1\) increase; they hold thereafter. Within each contiguous exceptional block, displacements are equal. At a boundary where two displacements differ, the source gap is two on precisely the potentially colliding side, so the paths remain strictly ordered at every time. Thus each deleted-row/deleted-column minor is strictly positive. Since \(\det B=\det Q>0\), Cramer's rule and \(G=SB^{-1}S\) give
\[
G_{ij}=\frac{\det B[\{1,\ldots,d\}\setminus\{j\},\{1,\ldots,d\}\setminus\{i\}]}{\det B}>0.
\]
Here the rows and columns inside the numerator are listed increasingly. This finite path argument applies also to \(\alpha=1\) and adjacent or boundary deletions.

**2. The exact orthogonal decomposition.** Pick phases \(s_j\) as stated. The Green-vector \(v=Gs\) satisfies \(Qv=s\) and
\[
\langle Da,Dv\rangle=\langle a,s\rangle=u,
\qquad \|Dv\|_2^2=s^*Gs=q>0.
\]
Consequently, by the Pythagorean identity for orthogonal projection onto the span of \(Dv\),
\[
qE-u^2=q\left\|D\left(a-\frac{u}{q}v\right)\right\|_2^2.
\]
All the matrix entries of \(G\) are real and symmetric. Since the coordinates of \(s\) have modulus one,
\[
C^2-q=\mathbf1^*G\mathbf1-s^*Gs
=\sum_{i<j}G_{ij}|s_i-s_j|^2.
\]
Adding \((C^2-q)E\) to the preceding Pythagorean identity gives the claimed decomposition. Its right-hand side is nonnegative. Strict positivity of the off-diagonal entries also shows that equality for nonzero \(a\) forces all \(s_j=\omega\) and \(a=(u/C^2)\omega G\mathbf1\). Conversely every complex scalar multiple of \(G\mathbf1\) gives equality, since \(G\mathbf1\) has strictly positive coordinates.

**3. Identification with the sharp constant and Landau extremizer.** The cited sharp discrete Sobolev theorem proves the displayed binomial constant and exhibits a positive sequence sampled from the discrete Landau polynomial. The proved equality characterization, combined with that explicit equality example, shows that the positive vector \(G\mathbf1\) is proportional to those samples. In particular the decomposition contains no unknown new sharp constant and applies in all dimensions and orders covered by the published inequality.

**4. Quantitative phase control.** Let \(m=\min_{i<j}G_{ij}>0\). The first nonnegative term in the deficit yields \(\mathcal D\ge mE\sum_{i<j}|s_i-s_j|^2\). If \(R=|\sum_j s_j|\), then
\[
\sum_{i<j}|s_i-s_j|^2=d^2-R^2,
\qquad \min_{|\omega|=1}\sum_j|s_j-\omega|^2=2(d-R).
\]
Since \(d+R\ge d\), the required estimate follows. The bound is explicit from the \(d\)-by-\(d\) matrix \(G\); its coefficient is not claimed optimal.

## Verification
The supplementary script `verify.py`, using only Python's standard library, forms \(D\), inverts \(Q\) in exact rational arithmetic, checks every entry of \(G\) is strictly positive, confirms the exact binomial value of \(C^2\), and tests the complex deficit identity on deterministic finite samples. Tested all \(1\le\alpha\le5\), \(2\le d\le9\), with 16 phase/amplitude samples per pair (640 samples total); all checks passed. A separate direct finite enumeration verified the nonintersecting-path schedule for \(1\le\alpha\le7\), \(2\le d\le9\), and every deleted row/column pair. These computations are finite checks only; the proof above establishes the general result.

## Relationship to prior work
Hindov, Nitzan, Olsen and Rydhe (arXiv:2610.19010v1, first publicly available October 13, 2026), Theorem 1 and Section 4, establish the optimal constant and construct an equality sequence from discrete Landau polynomials. Their results do not state the all-complex two-term deficit identity, the strictly positive inverse-Gram kernel as a phase-interaction graph, or the phase-stability estimate. The present decomposition is a quantitative rigidity refinement rather than another computation of the sharp constant. Its finite-dimensional Hilbert projection step is classical; the nonstandard input is the simultaneous strictly positive Green-kernel structure across all difference orders. Related discrete Dirichlet interpolation and infinite-lattice Sobolev stability results have different domains and functionals and do not directly imply the stated identity. Historical priority of the underlying total-positivity argument or an equivalent unstated remainder formula cannot be excluded.

## Limitations
The theorem is for zero-extended integer-order finite differences and the \(\ell^1\)-to-\(\ell^2\) endpoint. It does not assert a sharp phase-stability coefficient or an analogous identity for arbitrary weighted stencils, fractional differences, or higher-dimensional domains. A finite verification is not an infinite proof. Novelty is assessed against accessible published literature, not certified exhaustively.

## References
1. R. Hindov, S. Nitzan, J.-F. Olsen, and E. Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1 (October 13, 2026), https://arxiv.org/html/2610.19010v1.
2. K. Fan, O. Taussky, and J. Todd, *Discrete analogs of inequalities of Wirtinger*, Monatshefte für Mathematik 59 (1955), 73–90; background on the second-order discrete inequality.
3. B. Lindström, *On the vector representations of induced matroids*, Bulletin of the London Mathematical Society 5 (1973), 85–90; nonintersecting-path determinant method.
