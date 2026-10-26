# Sharp robust prior-strength boundary and risk reversal for a planar Gaussian range finder

## Finding
Let \(A\in\mathbb R^{2\times2}\) have singular values \(a>b>0\), and let \(v_1\) be a leading right singular vector. Suppose a nonzero unit prior direction \(w\) is used to generate one Gaussian probe \(\omega\sim N(0,K_r)\), where
\[
K_r=I+(r^2-1)ww^{\mathsf T},\qquad r\ge1,\qquad c=|v_1^{\mathsf T}w|^2\in[0,1].
\]
Write \(y=A\omega\), \(P=yy^{\mathsf T}/\|y\|_2^2\), and \(\widehat A=PA\), the ordinary one-probe range approximation. Define the squared Frobenius risk \(\mathcal R(r,c)=\mathbb E\|A-\widehat A\|_F^2\). Then the exact risk at every finite \(r\ge1\) is
\[
\boxed{\mathcal R(r,c)=\frac{ab\bigl[ab(r^2+1)+r(a^2+b^2)\bigr]}{a^2[1+(r^2-1)c]+b^2[r^2-(r^2-1)c]+2abr}.}\tag{1}
\]
In particular, the isotropic risk is \(\mathcal R(1,c)=ab\), and for every \(r>1\),
\[
\boxed{\mathcal R(r,c)<ab\iff c>\frac{a+br}{(a+b)(r+1)}.}\tag{2}
\]
At equality the risks are equal; reversing the inequality reverses the risk comparison. Three distinct regimes result:

1. If \(c\le b/(a+b)\), no finite stronger prior improves risk over isotropic probing (and each \(r>1\) is strictly worse).
2. If \(b/(a+b)<c<1/2\), the risk is initially worse than isotropic, crosses it once at \(r_{\rm cross}=[a-(a+b)c]/[(a+b)c-b]>1\), and is better for all \(r>r_{\rm cross}\). Specifically, for \((a,b,c)=(3,1,2/5)\), the risk equals \(3\) at \(r=1\), \(525/173>3\) at \(r=2\), and \(273/97<3\) at \(r=4\).
3. If \(c\ge1/2\), every \(r>1\) improves over isotropic probing.

There is also a complete monotonicity classification. Set \(c_1=b^2/(a^2+b^2)\). If \(c\le c_1\), \(\mathcal R(r,c)\) strictly increases for \(r>1\). If \(c_1<c<1/2\), it increases up to the unique strict maximum
\[
r_{\max}=\frac{ab(1-2c)+(a^2-b^2)\sqrt{c(1-c)}}{c(a^2+b^2)-b^2}>1
\]
and strictly decreases thereafter. If \(c\ge1/2\), it strictly decreases for \(r>1\).

Finally, if a practitioner knows only an alignment certificate \(c\ge c_0\) with \(c_0\in[0,1]\), the exact worst-case design value is
\[
\boxed{\inf_{r\ge1}\ \sup_{c\in[c_0,1]}\mathcal R(r,c)
=\min\!\left\{ab,\frac{a^2b^2}{a^2c_0+b^2(1-c_0)}\right\}.}\tag{3}
\]
For \(c_0\le b/(a+b)\), the minimax optimum is achieved at \(r=1\). For \(c_0>b/(a+b)\), the strictly smaller minimax *infimum* is approached as \(r\to\infty\), but is not attained at any finite \(r\). At the equality threshold, only the isotropic finite-strength choice attains the optimum.

## Assumptions and scope
The matrix is real \(2\times2\), invertible, and has unequal positive singular values \(a>b\). One Gaussian vector is used, with covariance \(K_r\) determined independently of the realized sample. Its known prior direction is a unit vector \(w\). The projector is the orthogonal projector onto the one-dimensional range of \(y=A\omega\); \(y=0\) has zero probability. The loss is expectation of *squared Frobenius error*, not expectation of its unsquared norm. The minimax assertion minimizes worst-case risk over a certified range of squared angular alignments; it is not a claim that the singular values or alignment certificate can be computed for free.

## Proof
Choose left and right singular frames so that \(A\) acts as \(\operatorname{diag}(a,b)\), and choose the sign of \(w\) so its leading squared component is \(c\). The covariance of \(y\) is \(C=AK_rA^{\mathsf T}\). In this frame
\[
\operatorname{tr}C=a^2[1+(r^2-1)c]+b^2[r^2-(r^2-1)c],\quad\sqrt{\det C}=abr.
\]
For any positive-definite real \(2\times2\) covariance \(C\), the exact projector moment is
\[
\mathbb E\frac{yy^{\mathsf T}}{y^{\mathsf T}y}=\frac{C^{1/2}}{\operatorname{tr}C^{1/2}},\qquad y\sim N(0,C).\tag{4}
\]
To verify it, orthogonally diagonalize \(C\) with variances \(\alpha^2,\beta^2\). A standard normal vector has uniformly distributed angle; the diagonal projector entries are the angular integrals of \(\alpha^2\cos^2\theta/(\alpha^2\cos^2\theta+\beta^2\sin^2\theta)\) and its complement. Elementary integration (or the substitution \(z=\tan\theta\) over each quadrant) gives \(\alpha/(\alpha+\beta)\) and \(\beta/(\alpha+\beta)\), while the off-diagonal expectation vanishes by sign symmetry. This proves (4) including repeated eigenvalues.

For every positive-definite \(2\times2\) matrix, the Cayley--Hamilton identity implies
\[
C^{1/2}=\frac{C+\sqrt{\det C}\,I}{\sqrt{\operatorname{tr}C+2\sqrt{\det C}}}.
\]
Since \(\|A-PA\|_F^2=\operatorname{tr}(AA^{\mathsf T})-\operatorname{tr}(PAA^{\mathsf T})\), substitution of (4) and the displayed square-root identity gives
\[
\mathcal R=\frac{a^2C_{22}+b^2C_{11}+(a^2+b^2)abr}{\operatorname{tr}C+2abr}.
\]
Using \(C_{11}=a^2[1+(r^2-1)c]\) and \(C_{22}=b^2[r^2-(r^2-1)c]\) yields (1).

Let \(D\) be the positive denominator of (1), and \(N\) its numerator. Exact factorization gives
\[
abD-N=ab(a-b)(r-1)\bigl[(a+b)(r+1)c-a-br\bigr].\tag{5}
\]
As \(ab(a-b)(r-1)>0\) for \(r>1\), (5) establishes (2). The threshold on its right is strictly decreasing with \(r\), tending to \(b/(a+b)\) as \(r\to\infty\) and equal to \(1/2\) as \(r\downarrow1\). This proves the three regimes and their unique crossing; the rational witness follows by substitution.

For the complete shape, write
\[
Q(r)=\bigl[c(a^2+b^2)-b^2\bigr]r^2+2ab(2c-1)r+c(a^2+b^2)-a^2.
\]
Direct differentiation gives the exact identity
\[
D^2\frac{\partial\mathcal R}{\partial r}=-ab(a-b)(a+b)Q(r).\tag{6}
\]
The discriminant of \(Q\) is \(4c(1-c)(a^2-b^2)^2\), and \(Q(1)=(a+b)^2(2c-1)\). If \(c\le c_1\), all coefficients of \(Q\) are nonpositive, with a strictly negative one, giving an increasing risk. If \(c_1<c<1/2\), the leading coefficient is positive and the constant and linear coefficients are negative, so \(Q\) has exactly one positive root greater than one, equal to the specified \(r_{\max}\). If \(c\ge1/2\), \(Q(r)>0\) for \(r>1\): at \(c=1/2\), \(Q(1)=0\) and \(Q\) is increasing beyond one; increasing \(c\) strictly increases \(Q(r)\) for positive \(r\). Formula (6) gives the asserted shapes.

For every fixed \(r>1\), the numerator of (1) is independent of \(c\) and its denominator is strictly increasing in \(c\), because \((r^2-1)(a^2-b^2)>0\). The worst certified alignment is therefore \(c=c_0\); at \(r=1\) all alignments have equal risk. The shape classification shows that an interior stationary point, if it exists, is a maximum, never a minimum. The infimum on \(r\in[1,\infty)\) must be the smaller of the endpoint value \(ab\) and
\[
\lim_{r\to\infty}\mathcal R(r,c_0)=\frac{a^2b^2}{a^2c_0+b^2(1-c_0)}.
\]
Their comparison gives precisely \(c_0>b/(a+b)\) for the anisotropic limit to be preferable, establishing (3) and the finite-attainment qualification.

## Verification
A standalone, dependency-explicit Python/SymPy script `verify.py` checks the factorization (5), derivative (6), and discriminant symbolically. It performs exact-rational comparisons across many admissible parameters, reproduces the nonmonotone witness, and independently integrates the angular one-probe projector risk at 90 parameter triples. Running `python3 verify.py` in the same directory as this document gave `PASS 1777 independent algebraic/rational/quadrature assertions`. This finite computation supports reproducibility; the all-parameter theorem is proved by the identities above, not by the tests.

## Relationship to prior work
Boullé and Townsend, *A generalization of the randomized singular value decomposition* (arXiv:2105.13052, originally public 2021-05-27), motivates nonstandard Gaussian covariance in randomized low-rank approximation and provides general bounds and experiments on tailored probing covariances. Diouane, Gürol, Di Perrotolo, and Vasseur, *A general error analysis for randomized low-rank approximation methods* (arXiv:2206.08793), gives general projection-error bounds. Halko, Martinsson, and Tropp (arXiv:0909.4061) provide the standard randomized range-finding framework. The inspected bounds do not state an exact single-probe planar risk with a misalignment-sensitive crossover or minimax prior-strength decision. The planar Gaussian projector-moment identity itself may be known independently; only its stated numerical risk and sharp robust comparison are assessed here as potentially new.

## Limitations
The result concerns only real two-dimensional, one-probe squared Frobenius risk with a rank-one covariance tilt. It makes no claim about general dimensions, oversampling, noisy matrix products, runtime, nonlinear solvers, or nonsquared residual norms. The minimax limit \(r\to\infty\) describes a degenerate deterministic probing direction; for finite \(r\) in that regime the limiting infimum is not attained. Publication priority cannot be certified by literature searches: uncatalogued equivalent special cases or general formulas implying this comparison may exist. No independent scientific audit has been carried out.

## References
- N. Boullé and A. Townsend, *A generalization of the randomized singular value decomposition*, arXiv:2105.13052, original preprint submitted 2021-05-27. https://arxiv.org/abs/2105.13052
- Y. Diouane, S. Gürol, A. Scotto Di Perrotolo, and X. Vasseur, *A general error analysis for randomized low-rank approximation methods*, arXiv:2206.08793, original preprint 2022-06-17. https://arxiv.org/abs/2206.08793
- N. Halko, P.-G. Martinsson, and J. A. Tropp, *Finding structure with randomness: probabilistic algorithms for constructing approximate matrix decompositions*, arXiv:0909.4061. https://arxiv.org/abs/0909.4061
