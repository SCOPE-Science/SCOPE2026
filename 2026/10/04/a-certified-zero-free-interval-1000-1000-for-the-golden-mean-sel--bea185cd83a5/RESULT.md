# A certified zero-free interval \([-1000,1000]\) for the golden-mean self-similar Fourier transform
## Finding
Let \(p=(\sqrt5-1)/2\), let \(f_1(x)=x/2\) and \(f_2(x)=(x+2)/4\), and let \(\mu\) be the self-similar probability measure satisfying
\[
\mu(E)=p\,\mu(f_1^{-1}(E))+p^2\,\mu(f_2^{-1}(E)).
\]
With Fourier transform
\[
F(\xi)=\int e^{-2\pi i\xi x}\,d\mu(x),
\]
one has
\[
F(\xi)\neq0\qquad\text{for every real }|\xi|\le1000.
\]
This is a finite-range statement only; it does not assert that \(F\) is zero-free on all of \(\mathbb R\).

## Assumptions and scope
The normalization and functional equation are those of Mao--Wu, arXiv:2609.04701v1. Since \(p+p^2=1\), their recursion is
\[
F(\xi)=pF(\xi/2)+p^2e^{-\pi i\xi}F(\xi/4).
\]
The attractor lies in \([0,2/3]\), so for real \(t\),
\[
|F(t)-1|\le \frac{4\pi}{3}|t|.
\]
The computation below uses depth \(N=42\) and outward interval arithmetic at 30 decimal digits.

## Proof
Set
\[
V(\xi)=\binom{F(\xi)}{F(\xi/2)},\qquad
M(\xi)=\begin{pmatrix}p&p^2e^{-\pi i\xi}\\1&0\end{pmatrix}.
\]
Then
\[
V(\xi)=M(\xi)M(\xi/2)\cdots M(\xi/2^{N-1})V(\xi/2^N).
\]
Define the depth-\(N\) approximation by replacing the terminal vector with \((1,1)^T\):
\[
V_N(\xi)=M(\xi)M(\xi/2)\cdots M(\xi/2^{N-1})\binom11,
\]
and let \(F_N\) be its first component. In the max norm on \(\mathbb C^2\), every matrix satisfies
\[
\|M(\xi)\|_\infty=\max\{p+p^2,1\}=1.
\]
Because \(\operatorname{supp}\mu\subset[0,2/3]\),
\[
|F(t)-1|\le\int 2\pi |t|x\,d\mu(x)\le \frac{4\pi}{3}|t|.
\]
Consequently, for \(|\xi|\le1000\),
\[
|F(\xi)-F_N(\xi)|\le \frac{4\pi}{3}\frac{1000}{2^{42}}
<\frac{88}{21}\frac{1000}{2^{42}}.
\]
The verifier covers \([0,1000]\) by an adaptive finite family of closed intervals. On each interval it evaluates the complete matrix product for \(F_N\) with outward interval arithmetic. An interval is accepted only when either its real-part enclosure or its imaginary-part enclosure stays farther from zero than the analytic tail bound above. Therefore the tail disk around the enclosure cannot contain zero. The finite cover proves \(F(\xi)\neq0\) on \([0,1000]\). Since \(\mu\) is real and positive, \(F(-\xi)=\overline{F(\xi)}\), yielding the claim on \([-1000,1000]\).

## Verification
Running `verify_zero_free.py` with mpmath 1.3.0 gives

`VERIFY_OK R=1000 depth=42 leaves=10908 splits=908 tail_upper=9.52803973285924693e-10 min_margin_lower=2.15110083984447931e-07 min_width=1.95312500011368684e-04 max_bisection_depth=9 mpmath=1.3.0 iv_dps=30`

The positive `min_margin` is the smallest coordinate-separation margin after subtracting the analytic truncation radius. The computation is exhaustive over the stated finite interval, not a point sample.

## Relationship to prior work
Mao--Wu prove analytically that \(F\) has no real zeros on \([-1.08,1.08]\). They also report a numerical scan with no detected real zeros on \([-10^7,10^7]\), while explicitly stating that this numerical work is not a formal proof and that a rigorous computer-assisted verification is left for future investigation. The present result converts the subrange \([-1000,1000]\) into a rigorous interval certificate. It does not supersede their much broader numerical evidence, and it does not settle global zero-freeness or spectrality.

Targeted searches for the exact maps, weights, Fourier recursion, zero-free property, Riccati formulation, and computer-assisted verification found no earlier rigorous statement covering \([-1000,1000]\) for this measure. Classical spectral Cantor-measure results concern different, homogeneous convolution structures and do not imply this finite zero-free interval.

## Limitations
The claim is only the finite cutoff \(|\xi|\le1000\). No assertion is made for \(|\xi|>1000\), for global non-spectrality, or for other non-homogeneous self-similar measures. The computational part depends on the outward-enclosure semantics of mpmath 1.3.0 interval arithmetic; an independent implementation has not been checked here. The analytic tail estimate is deliberately coarse but sufficient because the certified minimum separation exceeds the tail radius by more than two orders of magnitude.

## References
1. Yi-Qiu Mao and Zhi-Yi Wu, *On the spectrality of the non-homogeneous golden-mean self-similar measure*, arXiv:2609.04701v1, 4 September 2026.
2. I. Łaba and Y. Wang, *On spectral Cantor measures*, Journal of Functional Analysis 193 (2002), 409--420, for homogeneous spectral Cantor-measure background.
