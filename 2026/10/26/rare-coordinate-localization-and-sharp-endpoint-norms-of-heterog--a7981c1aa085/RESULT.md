# Mean-preserving spreads move four-bit affine projection norms in both directions

## Finding

Let \(p=(p_1,p_2,p_3,p_4)\) with \(0<p_i\le 1/2\), and let \(P_p\) be the orthogonal projection in \(L^2(\mu_p)\) onto the constant and the four coordinate functions, where \(\mu_p=\bigotimes_i\mathrm{Bernoulli}(p_i)\). Let \(N(p)\) be its common \(L^1(\mu_p)\) and \(L^\infty(\mu_p)\) operator norm. On the fixed-mean slice \(\sum_i p_i=1\), \(N\) is **neither Schur-convex nor Schur-concave**. Specifically, both \(p^-\) and \(p^+\) below are mean-preserving spreads of \(p^0\), but
\[
\begin{array}{c|c|c}
 &p& N(p)\\ \hline
p^-&(1/6,1/6,1/3,1/3)&77/27\\
p^0&(1/4,1/4,1/4,1/4)&371/128\\
p^+&(1/8,1/8,3/8,3/8)&6213/2048
\end{array}
\qquad N(p^-)<N(p^0)<N(p^+).
\]
Thus averaging biases of the same mean can either increase or decrease the sharp endpoint amplification, even when no coordinate bias exceeds one half.

## Assumptions and scope

The coordinates are independent, the functions are real, and the measure used in both domain and range is \(\mu_p\). This is the affine orthogonal projector, including the constant, not the centered first-chaos projector or a projection chosen to minimize its norm. For vectors of equal sum, \(p\) majorizes \(q\) if the sum of the first \(k\) entries of decreasingly sorted \(p\) is at least that of decreasingly sorted \(q\), for each \(k\). Schur-convexity means that majorization can only increase the value, and Schur-concavity means that it can only decrease it.

## Proof

Apply the universal rare-vertex multiplier formula [1] with coefficient one at the constant and at the four singletons, and coefficient zero elsewhere. The resulting operator is \(P_p\), since the normalized biased coordinate characters and the constant span the affine functions. The formula gives
\[
N(p)=\mathbb E|Z|,\qquad Z=-3+\sum_{i=1}^4\frac{B_i}{p_i},
\]
where \(B_i\) are independent \(\mathrm{Bernoulli}(p_i)\). Here the rare-coordinate probabilities equal the \(p_i\) by assumption. The result also applies to real functions: the kernel is real, so choosing its signs in a maximizing row attains the same bound as over complex functions. Kernel symmetry gives equality of the two endpoint norms.

Since \(\mathbb EZ=1\), \(N(p)=1+2\mathbb E(-Z)_+\), where \(w_+=\max(w,0)\). Every success contributes at least two, so \(Z<0\) can occur only with no successes or with exactly one success. With no successes the contribution to \(\mathbb E(-Z)_+\) is \(3\prod_i(1-p_i)\). With a unique success at site \(i\) it is \((3p_i-1)_+\prod_{j\ne i}(1-p_j)\). Therefore
\[
N(p)=1+6\prod_i(1-p_i)+2\sum_i(3p_i-1)_+\prod_{j\ne i}(1-p_j).
\]
On the fixed-mean slice the product term alone is strictly maximized by the constant vector by AM–GM. When all \(p_i\le 1/3\) the correction terms vanish. Above that threshold, the correction can more than offset the product loss, as the witnesses show: at \(p^-\) the product is \(25/81\) with no correction; at \(p^0\) it is \(81/256\) with no correction; at \(p^+\) it is \(1225/4096\) and the two nonzero correction terms add \(245/1024\) to \(N\). The exact gaps are \(N(p^0)-N(p^-)=161/3456\) and \(N(p^+)-N(p^0)=277/2048\). Each unequal vector has sum one and majorizes the constant vector of that sum. The first gap violates Schur-convexity and the second violates Schur-concavity.

## Verification

The accompanying `check.py` computes the three endpoint norms by exact rational Gram-matrix inversion and evaluation of the complete kernel. This verifies the concrete witnesses independently of the rare-vertex formula; the proof above explains their direction and establishes the obstruction on the slice.

## Relationship to prior work and limitations

The general rare-vertex formula, localization, and coordinatewise monotonicity already follow from [1]. The homogeneous-bias values and their dependence on the common bias are studied in [2]. Neither calculation is claimed as a new contribution here. A mean-preserving spread changes some coordinates in each direction, so coordinatewise monotonicity alone does not settle it. The contribution here is the explicit two-sided obstruction to Schur ordering at fixed mean, with the one-success threshold that explains how the direction can reverse. No characterization of all extrema on this slice or at other means is asserted.

## References

1. [A universal rare-vertex norming law for biased Boolean Fourier multipliers](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-a-universal-rare-vertex-norming-law-for-biased-boolean-fourier-m--40f4b54b28c0), Finding and proof of the multiplier formula.
2. [Balanced bias minimizes sharp affine Fourier amplification on the Bernoulli cube](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-balanced-bias-minimizes-sharp-affine-fourier-amplification-on-th--71f416ba0fcb), Finding, homogeneous bias.
