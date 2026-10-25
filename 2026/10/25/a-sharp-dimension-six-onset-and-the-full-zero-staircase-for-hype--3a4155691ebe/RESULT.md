# A sharp dimension-six onset and the full zero staircase for hyperplane-weighted ball kernels

## Finding

Let \(d\ge 1\) be an integer and \(\alpha>-1\) be real. Equip the open complex unit ball \(\mathbb B_d\subset\mathbb C^d\) with the weight \(|z_1|^2(1-\|z\|^2)^\alpha\), using ordinary Lebesgue volume, and take **only holomorphic functions on the entire ball**. Set \(s=d+\alpha+1\), \(t=z_1\overline{w_1}\), and \(u=\sum_{j=2}^{d}z_j\overline{w_j}\). The weighted reproducing kernel is
\[
K_{d,\alpha}(z,w)=\frac{\Gamma(s)}{\pi^d\Gamma(\alpha+1)}\,\frac{(1-u-t)^{-s}-(1-u)^{-s}}{t},
\]
where the quotient is continued holomorphically at \(t=0\).

Writing \(q=t/(1-u)\), all nontrivial scalar zero fibres are **exactly**
\[
q=1-\exp(2\pi i j/s),\qquad j\in\mathbb Z,\quad 0<6|j|<s.
\]
Every such zero is simple in the scalar variable \(q\), and no other zero occurs. Hence the number of distinct zero fibres is
\[
N_{d,\alpha}=2\bigl(\lceil (d+\alpha+1)/6\rceil-1\bigr).
\]
In particular, the kernel is zero-free on \(\mathbb B_d\times\mathbb B_d\) **if and only if** \(d+\alpha\le5\). At the ordinary boundary exponent \(\alpha=0\), this gives the sharp dimension-six onset: zero-free in dimensions \(1\) through \(5\), and zeros in every dimension \(d\ge6\). For \(s>6\) the first conjugate pair has scalar modulus \(2\sin(\pi/s)\).

## Assumptions and scope

The weighted space is \(A^2(\mathbb B_d,|z_1|^2(1-\|z\|^2)^\alpha)\) with the norm defined by integrating \(|f|^2\) against the stated weight, where \(f\) must extend holomorphically across the hyperplane \(\{z_1=0\}\). This convention matters: permitting meromorphic functions with poles along the hyperplane gives a different space and a different kernel. The positive powers use principal holomorphic branches in the right half-plane. When \(d=1\), define the empty sum \(u=0\). Zero fibres mean the distinct attainable values of the scalar \(q\), not the cardinality of the full analytic zero locus in two point variables.

## Proof

**1. Kernel identity.** For the conventional radial weight \((1-\|z\|^2)^\alpha\), the weighted ball Bergman kernel is
\[
K_0(z,w)=C_{d,\alpha}(1-\langle z,w\rangle)^{-s},\qquad C_{d,\alpha}=\Gamma(s)/(\pi^d\Gamma(\alpha+1)).
\]
Multiplication by \(z_1\) identifies the stated weighted space isometrically with the closed subspace of this radial Bergman space consisting of functions divisible by \(z_1\). The radial monomials are mutually orthogonal. The orthogonal complement comprises precisely the monomials independent of \(z_1\), and its reproducing kernel is \(C_{d,\alpha}(1-u)^{-s}\). Therefore the kernel of the divisible subspace is \(C_{d,\alpha}[(1-u-t)^{-s}-(1-u)^{-s}]\). Dividing by \(z_1\overline{w_1}=t\) gives the displayed weighted kernel, initially away from \(t=0\) and then by analytic continuation. Specifically,
\[
K_{d,\alpha}(z,w)\big|_{t=0}=C_{d,\alpha}s(1-u)^{-s-1}\ne0.
\]

**2. Attainable scalar domain.** Cauchy–Schwarz yields \(|u|+|t|\le\|z\|\,\|w\|<1\). Thus \(1-u\ne0\), and \(|q|=|t|/|1-u|<1\). Conversely every \(q\) with \(|q|<1\) is attained: choose \(z' = w'=0\), choose \(|z_1|=|w_1|=\sqrt{|q|}\), and choose their phases so that \(z_1\overline{w_1}=q\). Then \(u=0\) and the points lie in the ball.

**3. The exact zero equation.** Factoring out \((1-u)^{-s}\), a nonzero kernel value at \(q\ne0\) is a nonvanishing factor times \(((1-q)^{-s}-1)/q\). Since \(|q|<1\), \(1-q\) belongs to the open right half-plane and its principal logarithm has imaginary part strictly between \(-\pi/2\) and \(\pi/2\). Thus \((1-q)^{-s}=1\) holds precisely when
\[
\operatorname{Log}(1-q)=2\pi i j/s,\qquad j\in\mathbb Z,\quad |j|<s/4.
\]
At \(j=0\) one obtains \(q=0\), but the removable quotient there equals \(s\), not zero. For \(j\ne0\), the candidate is \(q_j=1-\exp(2\pi i j/s)\). In the allowed principal-log range, \(|q_j|=2\sin(\pi |j|/s)\). It is strictly smaller than \(1\) exactly when \(|j|<s/6\); equality is attained only on the excluded unit-circle boundary. The allowed indices are therefore exactly \(0<6|j|<s\). They produce pairwise distinct points because the principal arguments have absolute value less than \(\pi/3\). Differentiation of \((1-q)^{-s}-1\) gives \(s(1-q)^{-s-1}\ne0\) at each root, proving simplicity.

**4. Threshold and count.** The number of positive integers strictly smaller than \(s/6\) is \(\lceil s/6\rceil-1\). Pairing each with its negative gives the formula for \(N_{d,\alpha}\). This vanishes if and only if \(s\le6\), proving the exact zero-free criterion. At \(s=6m\) a would-be new pair lies on \(|q|=1\), hence does not enter until \(s>6m\). Finally the closest scalar roots correspond to \(j=\pm1\), whose modulus is \(2\sin(\pi/s)\), for \(s>6\).

## Verification

The kernel identity can be checked independently by the radial monomial expansion
\[
K_0(z,w)=C_{d,\alpha}\sum_{k\ge0}\frac{(s)_k}{k!}(u+t)^k
\]
and deleting the terms with zero power of \(t\). The removable value at \(q=0\) is \(s\), not a zero. Boundary cases \(s=6\) and \(s=12\) give \(N=0\) and \(N=2\), respectively. For \(s=7\), the two roots have modulus \(2\sin(\pi/7)<1\); for \(s=13\), the four roots correspond to \(j=\pm1,\pm2\). These checks are illustrative; the preceding logarithmic argument, not finite testing, proves the classification for all parameters.

## Relationship to prior work

Jacobson's 2013 work supplies a planar decomposition of Bergman kernels weighted by a holomorphic factor vanishing at a point (Theorem 4), which motivates the divisibility/projection method, but its inspected statements and zero-set discussion do not give this complex-ball dimension-and-weight phase diagram or the scalar root staircase. Boas's Lu Qi-Keng survey treats a different disk weight, namely the Euclidean boundary-distance power \((1-|z|)^\beta\), and obtains a different threshold. Ghiloufi and Snoun treat kernels on punctured disk-type spaces, where meromorphic holomorphicity conventions matter. The result here concerns full-ball holomorphic spaces with a hyperplane-vanishing weight and supplies the exact all-dimensional criterion, scalar zero locations, multiplicities, and entry thresholds. Literature coverage is bounded; this is not a claim that all possible prior equivalent formulations have been excluded.

## Limitations

The statement counts scalar zero fibres rather than irreducible components or geometric multiplicities in the full two-point zero locus. It covers one coordinate hyperplane factor \(|z_1|^2\) and real radial boundary exponent \(\alpha>-1\), not arbitrary hyperplane configurations or higher powers. The proof does not establish a stability theorem for perturbed weights. Historical priority is subject to the possibility of equivalent, unindexed or inaccessible work. No independent audit or external certification is claimed.

## References

1. R. Jacobson, *Weighted Bergman Kernel Functions Associated to Meromorphic Functions*, arXiv:1309.4800v1, first public version 2013-09-18, https://arxiv.org/abs/1309.4800.
2. H. P. Boas, *Lu Qi-Keng's problem*, Journal of the Korean Mathematical Society **37** (2000), 253–267, https://haroldpboas.gitlab.io/preprints/zeroes-survey.pdf, especially Section 7.
3. A. Ghiloufi and M. Snoun, *Zeros of new Bergman kernels*, arXiv:2009.04307v1 (2020), https://arxiv.org/html/2009.04307v1.
