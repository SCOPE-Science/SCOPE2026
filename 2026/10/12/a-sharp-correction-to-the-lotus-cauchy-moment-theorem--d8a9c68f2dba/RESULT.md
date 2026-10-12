# A sharp correction to the LOTUS Cauchy moment theorem
## Finding
Let \(X\sim\operatorname{Cauchy}(\mu,\sigma)\) with \(\sigma>0\) and density
\[
f_X(x)=\frac{\sigma}{\pi((x-\mu)^2+\sigma^2)}.
\]
The positive-integer moment formula asserted in Theorem 3.1 of Jayakumar, Samuel, and Thomas (2026) cannot be an ordinary moment formula. For every integer \(r\ge1\),
\[
\mathbb E|X|^r=\infty,
\]
so \(\mathbb E[X^r]\) is not a finite Lebesgue expectation. In particular, the first moment does not exist and the paper's subsequent central moments about \(\mathbb E[X]\) are not defined in the usual probabilistic sense.

The proof in that paper fails before any integration: its equation (3.2) treats the Cauchy density as one-to-one. The exact inversion is
\[
x=\mu\pm\sigma\sqrt{\frac{1}{\pi\sigma f_X(x)}-1},
\]
and the plus sign alone gives \(\mu+|x-\mu|\), which equals \(x\) only on the half-line \(x\ge\mu\).

There is nevertheless a precise complex-moment statement nearby. If the principal logarithm is used to define \(x^z\) on the real line by the upper boundary value on \(( -\infty,0)\), then
\[
\mathbb E[X^z]=(\mu+i\sigma)^z
\]
holds exactly for
\[
-1<\operatorname{Re}z<1.
\]
This strip is also exactly the strip of absolute integrability. Thus the complex numbers \((\mu+i\sigma)^r\) at positive integers are values of the analytic continuation of the fractional-moment formula; they are not positive-integer Cauchy moments.

## Assumptions and scope
The expectation is the standard Lebesgue expectation of a complex-valued random variable, so existence means absolute integrability of its real and imaginary parts, equivalently \(\mathbb E|X^z|<\infty\) for the principal complex power. The scale satisfies \(\sigma>0\); no symmetry assumption beyond the Cauchy location-scale model is made.

The correction concerns the population moment statements in the cited 2026 article. It does not question its numerical computations of finite data-set sample moments, which are always finite for finite samples. It also does not claim that the fractional-moment identity itself is new: earlier work of Okamura and Otobe develops legitimate complex fractional moments for Cauchy laws. The new point assessed here is the sharp correction and interpretation of the 2026 LOTUS theorem and its proof step.

## Proof
First, as \(|x|\to\infty\),
\[
f_X(x)\sim\frac{\sigma}{\pi x^2}.
\]
Hence for every integer \(r\ge1\), the tail of \( |x|^r f_X(x)\) is comparable to \(|x|^{r-2}\), whose integral diverges. Therefore \(\mathbb E|X|^r=\infty\). For even \(r\), the raw integral diverges to \(+\infty\); for odd \(r\), its positive and negative parts are both infinite, so symmetry or a Cauchy principal value cannot turn it into a Lebesgue expectation.

Second, direct algebra gives
\[
\frac{1}{\pi\sigma f_X(x)}-1=\frac{(x-\mu)^2}{\sigma^2}.
\]
Taking the nonnegative square root therefore yields \(|x-\mu|/\sigma\), not \((x-\mu)/\sigma\). Thus a single plus branch reconstructs \(\mu+|x-\mu|\), proving that equation (3.2) in the 2026 proof fails on every \(x<\mu\).

For the fractional statement, write \(a=\mu+i\sigma\) and \(b=\mu-i\sigma\). Then
\[
f_X(x)=\frac{1}{2\pi i}\left(\frac{1}{x-a}-\frac{1}{x-b}\right).
\]
Fix \(z\in\mathbb C\) with \(-1<\operatorname{Re}z<1\), and use the principal branch of \(w^z\), analytic in the open upper half-plane and taking argument \(\pi\) on the negative real boundary. Integrate
\[
\frac{w^z}{2\pi i}\left(\frac{1}{w-a}-\frac{1}{w-b}\right)
\]
over an upper-half-plane contour with a large semicircle and a small indentation above the origin. The large-arc integral vanishes because \(\operatorname{Re}z<1\); the indentation vanishes because \(\operatorname{Re}z>-1\). The only enclosed pole is \(a\), with residue \(a^z/(2\pi i)\). The residue theorem therefore gives
\[
\int_{-\infty}^\infty x^z f_X(x)\,dx=a^z=(\mu+i\sigma)^z.
\]
Finally, near zero the density is positive and bounded, while in the tails it is asymptotic to a nonzero multiple of \(|x|^{-2}\). Since \(|x^z|\) differs from \(|x|^{\operatorname{Re}z}\) only by a constant factor on each half-line, absolute integrability holds if and only if \(-1<\operatorname{Re}z<1\). This proves both the identity and the sharpness of its domain.

## Verification
The contradiction with the 2026 theorem is analytic and does not rely on numerical experiments. Three independent checks support it: tail comparison gives divergence of every positive integer absolute moment; direct substitution into the Cauchy density exposes the missing sign in the inverse-density step; and a residue calculation reconstructs the complex formula only on the exact integrability strip.

At the boundary \(\operatorname{Re}z=1\), the tail behaves like \(1/|x|\); at \(\operatorname{Re}z=-1\), the origin behaves like \(1/|x|\). Both boundaries therefore diverge logarithmically. The formula \((\mu+i\sigma)^z\) is entire as a function of \(z\) after a fixed logarithm of the upper-half-plane point \(\mu+i\sigma\) is chosen, so it analytically continues beyond the strip even though the defining expectation no longer exists there.

## Relationship to prior work
Jayakumar, Samuel, and Thomas state in Theorem 3.1 that the non-central \(r\)-th Cauchy moment is \((\mu+i\sigma)^r\), list the first ten positive integer cases, and then derive zero central moments. Their own introductory discussion also notes the traditional non-convergence of Cauchy moment integrals. The exact source text was inspected through the full article, including the theorem and equation (3.2).

Okamura and Otobe study fractional non-absolute complex moments and complex power means for Cauchy distributions, with the principal complex power made explicit. Their work predates the 2026 article and shows that complex fractional moments are a legitimate separate notion. It therefore supports the distinction made here rather than the positive-integer expectation claim. The present finding does not claim priority for the fractional identity; it identifies the invalid inference in the 2026 theorem and gives the sharp ordinary-expectation domain that separates the valid fractional statement from its invalid integer extrapolation.

Nadarajah's earlier work motivates a truncated Cauchy law precisely to obtain finite moments, again consistent with the standard nonexistence of ordinary moments for the untruncated law.

## Limitations
No claim is made about Hadamard finite parts, symmetric Cauchy principal values, distributional regularizations, or alternative generalized-moment conventions; those are different functionals and must be named explicitly if used. The originality assessment is limited by the possibility that an independent correction to the 2026 article could appear under non-indexed commentary or after the search date. The fractional identity itself is treated as prior mathematical background, not as the original contribution here.

## References
1. G. S. David Sam Jayakumar, W. Samuel, and B. J. Thomas, “A critical note on moments of Cauchy distribution based on LOTUS theorem,” Journal of Statistics and Management Systems, online 8 September 2026. DOI: 10.47974/JSMS-1606.
2. K. Okamura and Y. Otobe, “Power means of random variables and characterizations of distributions via fractional calculus,” arXiv:2312.02698; Probability and Mathematical Statistics 44(1) (2024), 133–156. DOI: 10.37190/0208-4147.00175.
3. S. Nadarajah, “Making the Cauchy work,” Brazilian Journal of Probability and Statistics 25(1) (2011), 99–120. DOI: 10.1214/09-BJPS112.
