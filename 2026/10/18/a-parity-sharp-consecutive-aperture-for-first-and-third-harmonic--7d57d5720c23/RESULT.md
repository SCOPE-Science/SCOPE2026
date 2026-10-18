# A parity-sharp consecutive aperture for first-and-third-harmonic quadrature

## Finding
Let \(N\ge4\) be an integer, and set \(\omega_N=e^{2\pi i/N}\). For \(0\le D<N\), a positive cyclic quadrature on the frequency window \(\{0,\ldots,D\}\) means nonnegative weights \(w_j\), not all zero, satisfying
\[
\sum_{j=0}^{D}w_j\omega_N^{j}=0,
\qquad
\sum_{j=0}^{D}w_j\omega_N^{3j}=0.
\]
Equivalently, after normalizing \(\sum_jw_j=1\), it integrates exactly the Haar mean of every function in the translation-invariant, real five-dimensional space
\[
\operatorname{span}_{\mathbb R}\{1,\cos\theta,\sin\theta,\cos3\theta,\sin3\theta\}.
\]
The least feasible endpoint \(D_*(N)\) is exactly
\[
\boxed{D_*(N)=\begin{cases}N/2,&N\text{ even},\\(N+3)/2,&N\text{ odd}.\end{cases}}
\]
The minimum is attained by positive weights on at most six distinct nodes, with strictly positive weights at both endpoints. The equivalent sharp arc length is \(2\pi D_*(N)/N\). The theorem holds for every \(N\ge4\), not only asymptotically. (At \(N=3\), the third harmonic is constant on the grid, so no such quadrature exists.)

## Assumptions and scope
All weights are real and nonnegative; zero weights on permitted nodes are allowed. The aperture is consecutive in the cyclic grid, but it may begin at any grid position: rotation multiplies the two moment sums by unimodular factors, so its feasibility depends only on \(D\). No node outside the window is allowed. Every statement uses the normalized Haar measure on the full unit circle as the reference integral. The exactness space contains the first and third harmonics, **not the second harmonic**; consequently this is sparse-harmonic quadrature, and it is not claimed to be Parseval sampling for the three spatial sites \(\{0,1,3\}\).

## Proof
**Semicircle lower bound.** Put \(\theta_j=2\pi j/N\), and center the candidate arc by \(\phi=\pi D/N\). If \(D<N/2\), all angles \(\theta_j-\phi\) lie strictly between \(-\pi/2\) and \(\pi/2\), so
\(\sum_jw_j\cos(\theta_j-\phi)>0\) for any nonzero nonnegative weights. This contradicts the vanishing first harmonic. Hence \(D\ge\lceil N/2\rceil\).

If \(N\) is even, choose \(D=N/2\) and put weight \(1/2\) at each of \(j=0,D\). The two phases are antipodal. Every odd Fourier harmonic, in particular the first and third, cancels. Thus the even case is sharp.

**Odd-grid extra obstruction.** Let \(N=2q+1\ge5\). The semicircle bound leaves \(D=q+1=(N+1)/2\) as the only remaining candidate below the proposed threshold. For that \(D\) and \(\phi=\pi D/N\), define
\[
x_j=\cos(\theta_j-\phi),\qquad a=\sin\frac{\pi}{2N},\qquad b=\sin\frac{3\pi}{2N}.
\]
The two endpoint cosines equal \(-a\). Every interior cosine is at least \(b>a>0\). Vanishing of the first and third complex Fourier moments implies that the centered real moments of \(x\) and \(4x^3-3x\) vanish. In particular \(\sum_jw_jx_j=\sum_jw_jx_j^3=0\), whence
\[
\sum_{j=0}^D w_j\,x_j(x_j^2-a^2)=0.
\]
But \(x_j(x_j^2-a^2)=0\) at the two endpoints, and it is strictly positive at every interior node. Therefore all interior weights must vanish. The first moment would then be \(-a\sum_jw_j<0\), a contradiction. The odd aperture is thus at least \(q+2=(N+3)/2\). This is an explicit dual-sign certificate, rather than a numerical infeasibility claim.

**Odd-grid positive construction.** Set \(D=q+2\), \(\phi=\pi D/N\), and
\[
a=\sin\frac{\pi}{2N},\quad b=\sin\frac{3\pi}{2N},\quad c=\sin\frac{5\pi}{2N}.
\]
For every odd \(N\ge5\), \(0<a<b<c\le1\). The symmetric node pairs \(\{0,D\}\), \(\{1,D-1\}\), and \(\{2,D-2\}\) have centered cosine values \(-b\), \(a\), and \(c\), respectively. For \(N=5\), the final pair consists of the same central node twice; its two contributions are combined.

Assign aggregate masses to the positive \(a\)-pair, positive \(c\)-pair, and negative \(-b\)-pair in the respective proportions
\[
A=c(c^2-b^2),\qquad B=a(b^2-a^2),\qquad C=\frac{ac(c^2-a^2)}{b}.
\]
All three are strictly positive. A direct factorization yields
\[
Aa+Bc=Cb,\qquad Aa^3+Bc^3=Cb^3.
\]
Normalize by \(T=A+B+C\) and split each aggregate mass evenly between its two indices, combining the central contributions when they coincide. Symmetry about \(\phi\) makes all centered sine moments of frequencies one and three vanish. The two displayed equations make the centered first and third cosine moments vanish, because \(\cos3t=4\cos^3t-3\cos t\). Rotating the two zero complex moments back by the factors \(e^{i\phi}\) and \(e^{3i\phi}\) preserves zero. Consequently this construction is an exact positive quadrature supported on at most six nodes, with both endpoints receiving \(C/(2T)>0\). The lower bound proves its aperture is minimal.

## Verification
The standalone standard-library script `verify.py` checks the displayed weights, normalization, endpoint occupation, vanishing first and third complex moments, and the strict odd-case dual-certificate sign for every \(4\le N\le1000\). It also tests the construction's two cancellation identities using exact rational arithmetic with three distinct sets of test parameters. A verified execution returned:

`VERIFY_OK 997 cyclic orders, 1994 complex moments, 6 exact rational cancellation identities`

Finite numerical checks are supplementary. The proof above establishes all stated integer ranges analytically.

## Relationship to prior work
Positive trigonometric quadrature on the unit circle has classical general descriptions, notably Peherstorfer's 2010 work. The more recent literature on positive trigonometric quadrature and covering radius, including Kunis (first public appearance August 12, 2026), studies full-degree exactness and geometric dispersion, rather than a fixed **missing-even-harmonic** exactness space with a sharply minimal consecutive cyclic window. An's October 8, 2026 work treats whole regular-grid designs and their geometric interpretation, rather than restricted-window reweighting.

Other close Fourier problems quantify the number of frequencies needed to sample three consecutive spatial sites, or the minimum aperture when the **first and second** moments vanish. Neither implies a classification for the first and third moments: the exactness subspaces are different, and the present odd/even apertures differ quantitatively. Published finite-group extremal problems for trigonometric polynomials supported on \(\{0,\pm1,\pm3\}\) constrain polynomial positivity across the whole grid or maximize an associated Fourier coefficient; these are different objectives and do not state the present consecutive-aperture existence threshold. The lower bound here uses a sign-certificate only on a moving consecutive arc, while the construction provides the matching positive weights. No claim of historical uniqueness is made beyond the comparisons documented in the accompanying scientific review.

## Limitations
The result concerns exactly the first two **odd** harmonics \(1\) and \(3\). It does not cover all harmonics through degree three, all pairs of odd harmonics, arbitrary nonconsecutive node sets, minimum node counts, or robustness to perturbing nodes. The stated proof is an analytic deduction for this structured harmonic pair; limited indexing of old cyclic quadrature literature leaves residual historical-priority uncertainty. No independent scientific audit has been performed.

## References
1. S. Kunis, *Positive quadrature and mobile sampling of multivariate trigonometric polynomials*, arXiv:2608.11915, first version August 12, 2026, https://arxiv.org/abs/2608.11915.
2. F. Peherstorfer, *Positive trigonometric Quadrature Formulas and quadrature on the unit circle*, arXiv:1001.2451v1, January 14, 2010, https://arxiv.org/html/1001.2451v1.
3. C. An, *Gauss–Chebyshev Quadrature, S¹-Designs, and the Planar Minkowski Inverse Problem*, arXiv:2610.11814v1, October 8, 2026, https://arxiv.org/html/2610.11814v1.
