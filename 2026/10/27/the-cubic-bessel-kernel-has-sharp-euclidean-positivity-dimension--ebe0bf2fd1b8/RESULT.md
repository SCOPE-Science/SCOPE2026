# The cubic Bessel kernel has sharp Euclidean positivity dimension two

## Finding

Let \(J_0\) be the Bessel function of the first kind of order zero, and let \(\Phi_d\) denote the continuous radial functions \(f:[0,\infty)\to\mathbb R\) for which \((x,y)\mapsto f(\|x-y\|_2)\) is positive semidefinite on every finite subset of \(\mathbb R^d\). For every \(a>0\),

\[
\boxed{\quad r\longmapsto J_0(ar)^3\in\Phi_2\setminus\Phi_3.\quad}
\]

In particular, the three-step planar random-walk characteristic function cannot serve as an isotropic covariance in any Euclidean dimension at least three. The nonmembership provides an exact counterexample to the power-dimension prediction in Remark 4.4 of Golinskii--Malamud--Oridoroga's 2015 preprint (arXiv:1502.07179v1), which at \(n=2\) and \(k=3\) predicts inclusion in \(\Phi_4\). The cited prediction is a conjecture, not a theorem.

## Assumptions and scope

The exponent is exactly three; the scale \(a\) is any positive real number. The Bessel function is normalized by \(J_0(0)=1\), and the Euclidean norm is used in every dimension. Positive semidefiniteness refers to all finite Gram matrices, not to a finite numerical test. No claim is made about other odd powers or unequal scaling parameters.

For a nonnegative integer \(k\), define the three-step planar-walk moment

\[
A_k=\sum_{i+j+h=k}\left(\frac{k!}{i!j!h!}\right)^2.
\]

Define \(m_k=A_k(\tfrac32)_k/k!\), where \((z)_k\) is the rising factorial. These are the *necessary* even radial moments of any hypothetical Schoenberg representing measure in dimension three, not moments of a measure assumed to exist.

## Proof

**1. Positivity in dimension two.** The normalized uniform measure on the unit circle has characteristic function \(x\mapsto J_0(\|x\|_2)\). Therefore \(J_0(a\|x\|_2)^3\) is the characteristic function of the sum of three independent, uniformly oriented planar vectors of length \(a\). By Bochner's theorem, it is positive semidefinite on \(\mathbb R^2\).

**2. Necessary moments of a hypothetical dimension-three representation.** It suffices to set \(a=1\). If \(J_0(r)^3\) belonged to \(\Phi_3\), Schoenberg's representation would give a probability measure \(\nu\) on \([0,\infty)\) satisfying

\[
J_0(r)^3=\int_0^\infty \frac{\sin(rt)}{rt}\,\nu(dt),
\]

with the quotient interpreted as one when its argument vanishes. All moments used below would be finite: the left side is analytic at zero, and the standard nonnegative finite-difference argument for characteristic functions implies finiteness of the corresponding even moments. Alternatively, represent the right side as the characteristic function of a spherically symmetric vector and apply this argument to one coordinate.

The absolutely convergent Taylor expansions are

\[
J_0(r)^3=\sum_{k\ge0}\frac{(-1)^k A_k}{4^k(k!)^2}r^{2k},\qquad
\frac{\sin(rt)}{rt}=\sum_{k\ge0}\frac{(-1)^k t^{2k}}{(2k+1)!}r^{2k}.
\]

Matching coefficients, with the moment finiteness just justified, yields

\[
\int_0^\infty t^{2k}\,\nu(dt)
=\frac{(2k+1)!}{4^k(k!)^2}A_k
=\frac{(\frac32)_k}{k!}A_k=m_k.
\]

Consequently the matrix \(H=(m_{i+j})_{0\le i,j\le6}\) must be positive semidefinite: for every real polynomial \(p\) of degree at most six, \(\int p(t^2)^2\nu(dt)\ge0\).

**3. Exact obstruction.** The finite multinomial formula above gives the exact rational determinant

\[
\boxed{\det H=
-\frac{59778222499952939497463042623250744763}{302231454903657293676544}<0.}
\]

This contradicts the positive-semidefinite moment condition. The exact-arithmetic standalone checker verifies this determinant and, independently, an explicit integer-coefficient degree-six polynomial with strictly negative putative squared integral. It also verifies a shorter dimension-four certificate:

\[
\det\bigl[((i+j+1)A_{i+j})\bigr]_{0\le i,j\le3}=-27756,
\]

where the dimension-four hypothetical radial moments are \((k+1)A_k\). In particular, for \(q(x)=7x^3-132x^2+747x-1146\), the hypothetical squared integral in dimension four would equal \(-10794\).

**4. All positive scales and higher dimensions.** If the scaled function were positive semidefinite on \(\mathbb R^3\) for any \(a>0\), coordinate dilation would yield the unscaled function there, a contradiction. Restriction to a three-dimensional linear subspace excludes every higher Euclidean dimension. This proves the claimed sharp cutoff.

## Verification

The adjacent `check_certificate.py` is a complete Python 3 standard-library-only checker. Run it with `python3 check_certificate.py`. It recomputes all three-step moment integers, the required rational moment sequences, the seven-by-seven determinant, an explicit negative squared-polynomial certificate in dimension three, and independent four-by-four / cubic-polynomial checks in dimension four. No floating-point computations or external datasets are required. The proof of positivity in dimension two is analytic; the exact finite determinant is a *necessary-condition obstruction* valid for the infinite-domain claim, not an enumeration of sample points.

## Relationship to prior work

Golinskii, Malamud and Oridoroga [1], Theorem 4.3, prove that the square of the order-two Schoenberg kernel, \(J_0(r)^2\), extends to positive definiteness in dimension three. Schur multiplication then also admits the fourth power in dimension three. Their Remark 4.4 proposes a general formula for powers of Schoenberg kernels, but explicitly states that an analogue for third and higher powers is unavailable. The present cubic nonextension contradicts its predicted dimension-four inclusion while establishing the sharper obstruction already in dimension three.

Borwein, Nuyens, Straub and Wan [2], Proposition 1, give the planar random-walk even moments \(A_k\) as sums of squared multinomial coefficients. These moments are used here as established input, but their work studies planar walk densities and moments, not the failed dimension-three Schoenberg moment condition. The novelty asserted here is solely the sharp nonextension and its exact finite moment certificate, not the formula for \(A_k\) or the positive-definiteness of the planar characteristic function.

## Limitations

The proof does not construct explicit locations of a finite negative Gram matrix in \(\mathbb R^3\); existence follows from the failure of positive definiteness. No classification of fifth or higher odd powers, or of unequal-step products, is obtained. The comparison establishes that the 2015 preprint's conjectural inclusion is false at this parameter, but does not assert that the conjecture remained unchanged in every later version. Literature searching was bounded, and an equivalent earlier treatment under other terminology remains possible. No independent mathematical audit has been performed.

## References

[1] L. Golinskii, M. Malamud, L. Oridoroga, *Radial positive definite functions and Schoenberg matrices with negative eigenvalues*, arXiv:1502.07179v1 (public preprint 25 February 2015), especially Theorem 4.3 and Remark 4.4. https://arxiv.org/abs/1502.07179

[2] J. M. Borwein, D. Nuyens, A. Straub, J. Wan, *Some Arithmetic Properties of Short Random Walk Integrals*, author-hosted preprint, especially Proposition 1 and equations (11)--(14). https://arminstraub.com/downloads/pub/walks.pdf ; author bibliography https://arminstraub.com/pub/walks

[3] I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522--536; classical radial representation theorem, as recalled in [1].
