# Critical-gap one-dimensional Fourier holography: exact fibers and singular values

## Finding

**Theorem.** Fix any integer \(n\ge1\), any known nonzero complex number \(b\), and an unknown complex vector \(a=(a_0,\ldots,a_n)\). Define
\[
F_a(z)=\sum_{j=0}^{n}a_jz^j+bz^{2n},\qquad I_a(t)=|F_a(e^{it})|^2\quad(t\in\mathbb R).
\]
The reference point at index \(2n\) is separated from the unknown support interval \(\{0,\ldots,n\}\) by exactly its diameter \(n\) in the discrete index metric. Define
\[
S(a)=\sum_{j=1}^{n-1}|a_j|^2,\qquad d(a)=\sqrt{S(a)+(|a_0|-|b|)^2}.
\]
The empty sum is zero when \(n=1\).

1. The full intensity \(I_a\) uniquely determines \(a_0,\ldots,a_{n-1}\) for *all* possible signals, even when some coefficients vanish.
2. If \(d(a)>0\), it also uniquely determines \(a_n\). This is a global uniqueness statement, not merely generic uniqueness.
3. If \(d(a)=0\), then \(a_1=\cdots=a_{n-1}=0\) and \(|a_0|=|b|>0\). Writing \(z=a_n\), the full fiber of the intensity consists of exactly the two possibly coincident tails
\[
 z\quad\text{and}\quad z^{\sharp}=\frac{b}{\overline{a_0}}\overline z.
\]
The two values coincide precisely on the real line rotated to the fixed axis of the reflection \(z\mapsto z^{\sharp}\). When different, the two full coefficient sequences are conjugate reversals, not a new kind of nontrivial Pauli partner.
4. Holding \(a_0,\ldots,a_{n-1}\) and \(b\) fixed, the data carried by the nonzero low autocorrelation lags are an affine real-linear function of the final coefficient. The two **exact** singular values of its linear part, with complex coordinates given their Euclidean real norms, are
\[
 \sigma_{\min}=\sqrt{S(a)+(|a_0|-|b|)^2},\qquad
 \sigma_{\max}=\sqrt{S(a)+(|a_0|+|b|)^2}.
\]
Thus these are the best possible lower and upper Lipschitz constants for this last-coefficient reconstruction map, after the first \(n\) coefficients have been recovered and held fixed.
5. In place of the continuous intensity, its values at the \(4n+1\) equally spaced points of the unit circle suffice for all assertions.

The reference placement is critical in a precise elementary sense: for the same finite unknown support and a reference at any integer position \(m\ge2n+1\), every coefficient is recoverable directly from isolated outer autocorrelation lags, without the exceptional reflection fiber.

## Assumptions and scope

The signal is a one-dimensional, finitely supported **complex** sequence, without positivity, nonvanishing, or genericity assumptions. Its possible unknown indices are \(0,\ldots,n\), its reference is a single known nonzero amplitude at \(2n\), and all other indices are zero. The reference and every support index are part of the model, not reconstructed. The data are ideal Fourier intensities on the circle or an exact nonaliasing grid. Singular values concern only the last-coordinate map with the earlier coefficients fixed; they are not a universal noise-amplification bound for the full nonlinear inverse map.

## Proof

Let \(f_j=a_j\) for \(0\le j\le n\), let \(f_{2n}=b\), and put all other coefficients equal to zero. The \(k\)-th Fourier coefficient of \(I_a\) in the convention \(I_a(t)=\sum_k C_k e^{ikt}\) is the autocorrelation
\[
 C_k=\sum_{j=0}^{2n-k}f_{j+k}\overline{f_j},\qquad 0\le k\le 2n,
\]
with \(C_{-k}=\overline{C_k}\). For \(0\le j<n\), the lag \(2n-j\) exceeds \(n\). Consequently the *only* contributing pair is \((2n,j)\), and
\[
 C_{2n-j}=b\overline{a_j},\qquad
 a_j=\overline{C_{2n-j}/b}.
\]
This proves the first assertion with no assumptions on the unknown coefficients.

Write \(z=a_n\). For \(1\le k<n\), the reference cannot contribute, so after subtracting the terms determined by the already recovered coefficients,
\[
 C_k-\sum_{j=0}^{n-k-1}a_{j+k}\overline{a_j}
   =z\overline{a_{n-k}}.
\]
At the unique collision lag \(n\), two contributions occur:
\[
 C_n=\overline{a_0}z+b\overline z.
\]
Hence the complete remaining nonzero-lag map is
\[
 T(z)=\bigl(\overline{a_{n-1}}z,\ldots,\overline{a_1}z,
         \overline{a_0}z+b\overline z\bigr)\in\mathbb C^n.
\]
For any \(z,w\in\mathbb C\) and \(h=z-w\), its squared difference is
\[
 \|T(z)-T(w)\|_2^2=S(a)|h|^2+|\overline{a_0}h+b\overline h|^2.
\]
As the argument of nonzero \(h\) varies, the final summand divided by \(|h|^2\) ranges exactly between \((|a_0|-|b|)^2\) and \((|a_0|+|b|)^2\). This proves both exact singular values. The lower one is positive if and only if \(d(a)>0\), proving full uniqueness in that regime.

If \(d(a)=0\), then all middle coefficients vanish and \(|a_0|=|b|>0\). The only remaining nonzero-lag equation is \(\overline{a_0}z+b\overline z=C_n\). In addition, the zero lag fixes \(|z|\), because
\[
 C_0=|a_0|^2+|z|^2+|b|^2.
\]
Put \(\eta=b/\overline{a_0}\), so \(|\eta|=1\), and choose \(\rho\) on the unit circle with \(\rho^2=\eta\). Substituting \(z=\rho u\) changes the nonzero-lag equation into a known nonzero factor times \(2\operatorname{Re}u\), while \(C_0\) fixes \(|u|\). A vertical line meets the corresponding circle in precisely \(u\) and \(\overline u\), possibly coinciding. Returning to \(z\), these are \(z\) and \(\eta\overline z\). Both produce identical autocorrelations at every lag, so the description is exact. The full sequence \((a_0,0,\ldots,0,z,0,\ldots,0,b)\) is transformed to its conjugate reversal multiplied by \(a_0/\overline b\), which equals \(b/\overline{a_0}\) in the balanced case. This verifies the stated classical nature of the ambiguity.

The polynomial \(I_a\) has Fourier degrees between \(-2n\) and \(2n\). Discrete Fourier inversion on any \(4n+1\) equispaced points therefore recovers all \(C_k\) without aliasing. Finally, if the reference is at \(m\ge2n+1\), then \(m-j>n\) for every \(0\le j\le n\), so \(C_{m-j}=b\overline{a_j}\) recovers all coefficients. The theorem follows.

## Verification

The accompanying standard-library-only script `verification/check.py` numerically exercises all algebraic lag identities, the nonaliasing-grid inversion, the two real singular values, and the complete balanced reflection pair. It passed 2,185 random parameter cases across dimensions \(1\le n\le23\). These computations are independent cross-checks; the quantified conclusions for every \(n\) and all complex parameters are proved above and do not rely on sampling.

## Relationship to prior work

Novikov and Xu (2026) construct Fourier-phase-retrieval ambiguities with a known background when its support separation is below the unknown support diameter; they also recall a known uniqueness guarantee beyond the diameter. The theorem here addresses a sharply defined discrete single-point-reference model **at equality**. It classifies all fibers and the exact residual stability, rather than merely giving an existence or generic result.

Barmherzig, Sun, Li, Lane and Candès (2019) develop referenced deconvolution and pinhole-reference reconstruction in a two-dimensional block layout where cross-correlations can be isolated. Their reconstruction formula does not furnish the present one-dimensional edge-collision classification. Crimmins and Fienup (1983) prove essential generic uniqueness under strictly separated autocorrelation supports, not the touching critical case. Bendory, Beinert and Eldar (2017) review general one-dimensional zero flipping and partial coefficient information, but the reviewed generic statements do not imply the universal fiber bound and singular-value formula here.

## Limitations

The conclusion does not cover arbitrary multispike backgrounds, multidimensional supports, other reference offsets below the threshold, or unknown reference amplitude. The nontrivial obstruction at exact critical separation is only the classical conjugate-reversal symmetry. The finite-grid sample count is sufficient, not claimed minimal. Stability is conditional on exact recovery of the lower-index coefficients and uses nonzero-lag Euclidean data; it is not a uniform end-to-end noisy intensity-recovery theorem. No independent mathematical validation is claimed.

## References

1. R. G. Novikov and T. Xu, *On Phase Retrieval for Continuous and Discrete Fourier Transforms*, arXiv:2604.25662v1 (April 28, 2026), Introduction and Theorems 1–4, https://arxiv.org/abs/2604.25662.
2. D. A. Barmherzig, J. Sun, P.-N. Li, T. J. Lane and E. J. Candès, *Holographic Phase Retrieval and Reference Design*, arXiv:1901.06453, §§2.2–2.4, https://arxiv.org/abs/1901.06453.
3. T. R. Crimmins and J. R. Fienup, *Uniqueness of Phase Retrieval for Functions with Sufficiently Disconnected Support*, J. Opt. Soc. Am. **73** (1983), 218–221, https://doi.org/10.1364/JOSA.73.000218.
4. T. Bendory, R. Beinert and Y. C. Eldar, *Fourier Phase Retrieval: Uniqueness and Algorithms*, arXiv:1705.09590, §§3.1–3.2, https://arxiv.org/abs/1705.09590.
