# Arithmetic conditioning of three-line Gaussian interference measurements

## Finding
Let \(\phi(s)=e^{-\pi s^2}\) and, for any \(\nu>0\), consider the two-tone Gaussian signal
\[
f_{a,b,\nu}(s)=a e^{2\pi i\nu s}\phi(s)+b e^{-2\pi i\nu s}\phi(s),\qquad (a,b)\in\mathbb C^2\setminus\{(0,0)\}.
\]
Use the Gaussian short-time Fourier transform
\[
V_\phi f(x,\omega)=\int_{\mathbb R}f(s)\phi(s-x)e^{-2\pi i\omega s}\,ds.
\]
For three complete frequency profiles at times \(x_0=0\), \(x_1=d\), and \(x_2=\rho d\), where \(d>0\), \(\rho>1\), and \(t=2\nu d\), removing the known diagonal exponential terms leaves three real interference measurements of the complex number \(C=a\overline b\). Their \(3\times2\) real analysis matrix is
\[
A_\rho(t)=\begin{pmatrix}1&0\\\cos(\pi t)&-\sin(\pi t)\\\cos(\pi\rho t)&-\sin(\pi\rho t)\end{pmatrix}.
\]
Its exact **squared least singular value**, the sharp linear stability constant for reconstructing the two real coordinates of \(C\), is
\[
\boxed{\lambda_\rho(t)=\frac{3-\left|1+e^{2\pi it}+e^{2\pi i\rho t}\right|}{2}}.\tag{1}
\]
It vanishes at a positive \(t\) if and only if \(\rho\) is rational and both \(t\) and \(\rho t\) are integers. Thus for irrational \(\rho\) the three-line phase measurements identify the nonzero two-tone signal up to global phase, although the linear conditioning is not uniformly positive over unbounded \(\nu\).

More precisely, for irrational \(\rho\), let \(\mu(\rho)\in[2,\infty]\) be its classical irrationality exponent:
\[
\mu(\rho)=\sup\big\{u>0:|\rho-p/q|<q^{-u}\text{ for infinitely many }(p,q)\in\mathbb Z\times\mathbb N\big\}.
\]
Then the **exact arithmetic instability exponent** is
\[
\boxed{\limsup_{t\to\infty}\frac{-\log\lambda_\rho(t)}{\log t}=2\big(\mu(\rho)-1\big).}\tag{2}
\]
For every badly approximable \(\rho\) there is a positive constant \(c_\rho\) with \(\lambda_\rho(t)\ge c_\rho(1+t)^{-2}\) for all \(t\ge1\), and this exponent is attained in order along infinitely many integer \(t\). For Liouville \(\rho\), no lower bound of the form \(c(1+t)^{-K}\), with \(c>0\) and finite \(K\), is valid for all large \(t\).

The injectivity implication itself is an instance of established irrationally spaced parallel-line phase retrieval. The claim advanced here is **the exact interference-matrix spectrum and the full irrationality-exponent law for its conditioning**, not a new general uniqueness theorem.

## Assumptions and scope
All frequencies \(\omega\in\mathbb R\) on each of the three lines are observed, without additive noise in the uniqueness statement. The two carrier frequencies are symmetric and unknown but have the same strictly positive magnitude \(\nu\); complex amplitudes are arbitrary except that they are not both zero. Singular-value stability concerns the extracted real interference data after separating the diagonal Gaussian exponential profiles, not a uniform inverse estimate in a raw spectrogram norm. The ratio \(\rho\) is a fixed real number greater than one, and all quantitative limits are as \(t=2\nu d\to\infty\).

## Proof
**1. Exact profile reduction.** Completing the square gives
\[
V_\phi f_{a,b,\nu}(x,\omega)=\frac{e^{-\pi i x\omega}}{\sqrt2}
 e^{-\frac\pi2(x^2+\omega^2+\nu^2)}
 \left(a e^{\pi\nu\omega+\pi i\nu x}+b e^{-\pi\nu\omega-\pi i\nu x}\right).
\]
Consequently, writing \(I_x(\omega)=|V_\phi f(x,\omega)|^2\),
\[
2e^{\pi(x^2+\omega^2)}I_x(\omega)
=e^{-\pi\nu^2}\left(|a|^2e^{2\pi\nu\omega}+|b|^2e^{-2\pi\nu\omega}+2\operatorname{Re}(Ce^{2\pi i\nu x})\right).\tag{3}
\]
The coefficients of the distinct real exponentials in (3) are unique. In particular, a nonzero signal's single entire profile identifies \(\nu\) and the two amplitude magnitudes, including the cases in which one amplitude vanishes. From any such profile the constant term can therefore be extracted exactly. At \(x=0,d,\rho d\), these terms are respectively \(\operatorname{Re}C\), \(\operatorname{Re}(Ce^{\pi it})\), and \(\operatorname{Re}(Ce^{\pi i\rho t})\), yielding \(A_\rho(t)\) when \(C\) is written in its real and imaginary coordinates. Once \(C\) and \(|a|,|b|\) are known, \((a,b)\) is determined up to a common unimodular factor. A vanishing amplitude requires no relative-phase inversion.

**2. The spectrum and the exact resonance set.** The real row vectors of \(A_\rho(t)\) have unit norm and angles \(0,-\pi t,-\pi\rho t\). Using the elementary double-angle formulas, the two eigenvalues of its Gram matrix are
\[
\lambda_\pm=\frac{3\pm|1+e^{2\pi it}+e^{2\pi i\rho t}|}{2}.
\]
The three unit complex numbers have modulus-three sum precisely when they coincide. Hence \(\lambda_- =0\) precisely when \(t,\rho t\in\mathbb Z\). A positive simultaneous integer solution exists precisely for rational \(\rho\).

**3. Uniform comparison with simultaneous near-resonance.** Put \(\|u\|_{\mathbb R/\mathbb Z}=\min_{k\in\mathbb Z}|u-k|\). With \(S=1+e^{2\pi it}+e^{2\pi i\rho t}\), the elementary identity
\[
9-|S|^2=4\left(\sin^2\pi t+\sin^2\pi\rho t+\sin^2\pi(\rho-1)t\right)
\]
gives
\[
\lambda_\rho(t)=\frac{2\big(\sin^2\pi t+\sin^2\pi\rho t+\sin^2\pi(\rho-1)t\big)}{3+|S|}.
\]
As \(3\le3+|S|\le6\), \(2\|u\|_{\mathbb R/\mathbb Z}\le|\sin\pi u|\le\pi\|u\|_{\mathbb R/\mathbb Z}\), and \(|\sin\pi(u-v)|^2\le2(|\sin\pi u|^2+|\sin\pi v|^2)\), it follows for every \(t\in\mathbb R\) that
\[
\frac43\left(\|t\|_{\mathbb R/\mathbb Z}^2+\|\rho t\|_{\mathbb R/\mathbb Z}^2\right)
\le\lambda_\rho(t)\le
2\pi^2\left(\|t\|_{\mathbb R/\mathbb Z}^2+\|\rho t\|_{\mathbb R/\mathbb Z}^2\right).\tag{4}
\]

**4. Exact instability exponent.** Suppose \(\rho\) is irrational and let \(q\) be the nearest integer to \(t\ge2\), and \(p\) the nearest integer to \(\rho t\). Then \(q\asymp t\) and
\[
|q\rho-p|\le |\rho|\|t\|_{\mathbb R/\mathbb Z}+\|\rho t\|_{\mathbb R/\mathbb Z}.
\]
For every \(\epsilon>0\) and every sufficiently large integer \(q\), the definition of the irrationality exponent implies \(|\rho-p/q|\ge q^{-\mu(\rho)-\epsilon}\) for all integers \(p\), if \(\mu(\rho)<\infty\). Thus (4) yields \(\lambda_\rho(t)\ge c_{\rho,\epsilon}t^{-2(\mu(\rho)-1+\epsilon)}\) for all large \(t\). Conversely, infinitely many fractions \(p/q\) satisfy \(|\rho-p/q|<q^{-\mu(\rho)+\epsilon}\); for \(t=q\), (4) yields \(\lambda_\rho(q)\le2\pi^2 q^{-2(\mu(\rho)-1-\epsilon)}\). If \(\mu(\rho)=\infty\), the latter inequality holds with an arbitrarily large exponent. Letting \(\epsilon\downarrow0\) proves (2) in both cases.

For badly approximable \(\rho\), \(|\rho-p/q|\ge c/q^2\) for all integer \(p,q>0\), so the first half of the argument gives a uniform \(t^{-2}\) lower bound for \(t\ge1\). Standard continued-fraction convergents have \(|\rho-p/q|<q^{-2}\) infinitely often, proving the reverse order along integer \(t=q\). Liouville's defining approximation property gives arbitrarily high inverse-power decay along an unbounded sequence, excluding every fixed polynomial lower bound.

## Verification
The attached standalone \(\texttt{checker.py}\) independently recomputes the eigenvalues from the real Gram matrix, checks the trigonometric bounds on many nonresonant parameters, tests the exact rational-resonance obstruction, checks reconstruction of a complex interference value, tests the golden-ratio convergent decay, and compares the closed STFT with direct numerical Gaussian integration. These checks passed; the universal and asymptotic assertions are established by the proof above, not by sampling.

## Relationship to prior work
Wellershoff (arXiv:2202.03733, first posted 2022-02-08) characterizes phaseless ambiguity on parallel lines and establishes the general irrational-three-line uniqueness mechanism. Liehr (2024, DOI 10.1112/blms.13134) proves a stronger whole-function characterization through arithmetic-progression containment. These results **already cover** the qualitative irrationality criterion here, and it is not claimed to be original. Alaifari, Bartolucci, Steinerberger, and Wellershoff (arXiv:2205.07013) study sampling versus stability using infinite-dimensional Gabor estimates, and Grohs, Liehr, and Rathmair (arXiv:2308.00385) study Fock-space Liouville uniqueness sets. The exact two-tone interference Gram eigenvalues (1), uniform comparison (4), and equality of its worst-frequency conditioning exponent with twice the irrationality-exponent defect (2) are the distinct quantitative assertions. This comparison is based on inspected accessible texts; equivalent phase-design estimates in other literatures remain a priority risk.

## Limitations
The method uses entire one-dimensional frequency profiles on three time slices. It assumes a symmetric two-tone Gaussian model, and the singular value governs extraction of the interference moment rather than a raw, noise-normalized inversion of all continuous spectrogram data. Full-function uniqueness for irrationally spaced lines is prior art. Neither a general sparse-multitone analogue nor a uniform stability bound across arbitrary signal classes is claimed. Novelty remains best-knowledge rather than independently established.

## References
- M. Wellershoff, *Phase retrieval of entire functions and its implications for Gabor phase retrieval*, arXiv:2202.03733 (first submitted 2022-02-08); subsequently J. Funct. Anal. 286 (2024), 110403.
- L. Liehr, *Arithmetic progressions and holomorphic phase retrieval*, Bull. Lond. Math. Soc. 56 (2024), 3316–3330, DOI:10.1112/blms.13134.
- R. Alaifari, F. Bartolucci, S. Steinerberger, and M. Wellershoff, *On the connection between uniqueness from samples and stability in Gabor phase retrieval*, arXiv:2205.07013 (2022).
- P. Grohs, L. Liehr, and M. Rathmair, *Phase retrieval in Fock space and perturbation of Liouville sets*, arXiv:2308.00385 (first submitted 2023-08-01).
