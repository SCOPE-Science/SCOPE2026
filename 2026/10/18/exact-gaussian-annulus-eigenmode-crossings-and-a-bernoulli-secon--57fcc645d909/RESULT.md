# Exact Gaussian-annulus eigenmode crossings and a Bernoulli second-order concentration law

## Finding
Let \(\phi(t)=2^{1/4}e^{-\pi t^2}\), and let \(V_\phi\) be the short-time Fourier transform with frequency convention \(e^{-2\pi i\xi t}\). For fixed \(w>0\) and \(a\geq0\), form the phase-space annulus
\[
\Omega_{a,w}=\{(x,\xi)\in\mathbb R^2:a\leq\pi(x^2+\xi^2)\leq a+w\},
\qquad P_{a,w}=V_\phi^*\mathbf1_{\Omega_{a,w}}V_\phi.
\]
Its Euclidean area is \(w\). The operator is a positive compact contraction. Its normalized Hermite eigenfunctions \(h_n\), \(n=0,1,\ldots\), have eigenvalues
\[
\lambda_n(a,w)=\frac1{n!}\int_a^{a+w}e^{-u}u^n\,du.
\]

**Exact maximizing modes and crossings.** Put \(H(0,w)=0\) and, for \(a>0\),
\[
H(a,w)=\frac{w}{\log(1+w/a)},\qquad a_m(w)=\frac{w}{e^{w/m}-1}\quad(m=1,2,\ldots).
\]
If \(H(a,w)\) is not a positive integer, the unique top eigenmode has index \(\lfloor H(a,w)\rfloor\); if \(H(a,w)=m\in\mathbb N\), precisely the two modes \(h_{m-1}\) and \(h_m\) maximize. In particular, the unique maximizing index is \(m\) for \(a_m(w)<a<a_{m+1}(w)\), and is zero for \(0\leq a<a_1(w)\).

**Strict norm corners.** The norm \(N_w(a)=\|P_{a,w}\|\) is real-analytic between the crossing radii and is continuous but not differentiable at any \(a=a_m(w)\). Its right-minus-left first derivative there equals
\[
N_w'(a_m+)-N_w'(a_m-)
=\frac{w\,e^{-a_m}a_m^{m-1}}{(m-1)!(a_m+w)}>0.
\]
For fixed \(w\), this jump is asymptotic to \(w/(\sqrt{2\pi}\,m^{3/2})\).

**Sharp oscillatory second term.** Write \(c=a+w/2\), \(\theta=\{c\}\in[0,1)\), and \(B_2(\theta)=\theta^2-\theta+1/6\). For every fixed \(w>0\), as \(a\to\infty\), uniformly over all positions of the annulus relative to the integer Hermite levels,
\[
\boxed{
N_w(a)=\frac{w}{\sqrt{2\pi c}}
\left[1-\frac{B_2(\{c\})/2+w^2/24}{c}
+O_w(c^{-2})\right].}
\]
Accordingly the set of subsequential limits of
\(c(\sqrt{2\pi c}\,N_w(a)/w-1)\), as \(a\to\infty\), is exactly
\[
\boxed{[-w^2/24-1/12,\;-w^2/24+1/24].}
\]
Thus a single constant coefficient cannot replace the explicit periodic correction.

## Assumptions and scope
The time variable and phase-space coordinates are real; \(V_\phi f(x,\xi)=\int_\mathbb R f(t)\overline{\phi(t-x)}e^{-2\pi i\xi t}\,dt\). The window \(\phi\) and each Hermite function \(h_n\) have unit \(L^2\) norm. The annulus parameter \(w\) is an arbitrary fixed positive real number; the crossing formulas hold at every \(a\geq0\), and the asymptotic statement holds only as \(a\to\infty\) with \(w\) held fixed. The operator acts on complex \(L^2(\mathbb R)\). Every derivative of \(N_w\) is with respect to \(a\), at fixed \(w\).

## Proof
**1. Spectral reduction.** The Gaussian STFT is an isometry, and radial Gaussian localization is diagonal on the Hermite basis (or, under the Bargmann transform, on monomials). The exact Hermite spectrogram is
\[
|V_\phi h_n(x,\xi)|^2=e^{-\pi(x^2+\xi^2)}
\frac{[\pi(x^2+\xi^2)]^n}{n!}.
\]
Polar integration with \(u=\pi(x^2+\xi^2)\) gives the claimed \(\lambda_n\). Positivity and compactness follow from \(0<\lambda_n<1\), \(\lambda_n\to0\), and the complete Hermite basis.

**2. Adjacent-mode sign law.** For every integer \(n\geq0\), differentiation of \(e^{-u}u^{n+1}\) yields the exact telescoping identity
\[
\lambda_{n+1}-\lambda_n
=\frac{e^{-a}a^{n+1}-e^{-(a+w)}(a+w)^{n+1}}{(n+1)!}.
\]
For \(a>0\), its sign is the sign of \(H(a,w)-(n+1)\). At \(a=0\) every difference is negative. Thus the eigenvalue sequence strictly rises then strictly falls, with at most a two-level plateau exactly when \(H\) is integral. The map \(a\mapsto H(a,w)\) is strictly increasing from zero to infinity because \(\log(1+w/a)\) is strictly decreasing. Solving \(H(a,w)=m\) gives the displayed unique crossing \(a_m(w)\). No nonadjacent top degeneracies occur.

**3. Cusp calculation.** At \(a=a_m(w)\) put \(b=a+w\). Equality of consecutive eigenvalues gives \(e^{-a}a^m=e^{-b}b^m=:K\). Differentiating their difference with respect to \(a\) and using this equality gives
\[
\frac{d}{da}(\lambda_m-\lambda_{m-1})
=\frac{K}{m!}\,m\left(\frac1a-\frac1b\right)
=\frac{w e^{-a}a^{m-1}}{(m-1)!b}>0.
\]
The leading eigenvalue therefore switches transversely from \(m-1\) to \(m\), producing the displayed one-sided derivative jump. The expansion \(a_m=m-w/2+O_w(m^{-1})\) and Stirling's formula give the stated jump asymptotic.

**4. Uniform two-term expansion.** Put \(c=a+w/2\) and \(s=u-c\), so \(|s|\leq w/2\). The logarithmic mean satisfies
\[
H(a,w)=\frac{w}{\log((c+w/2)/(c-w/2))}
=c-\frac{w^2}{12c}+O_w(c^{-3}).
\]
For a maximizing integer \(n\), this ensures \(d=n-c\) remains bounded. Stirling's formula with uniform Taylor remainders for bounded \(d,s\) gives
\[
\frac{e^{-(c+s)}(c+s)^n}{n!}
=\frac1{\sqrt{2\pi c}}
\left[1-\frac{(d-s)^2+d+1/6}{2c}+O_w(c^{-2})\right].
\]
Integrating over \(-w/2\leq s\leq w/2\) gives
\[
\lambda_n(a,w)=\frac{w}{\sqrt{2\pi c}}
\left[1-\frac{d^2+d+1/6+w^2/12}{2c}+O_w(c^{-2})\right].
\]
Usually the maximizing index is \(\lfloor c\rfloor\), so \(d=-\theta\). The only other possibility for sufficiently large \(c\) is \(n=\lfloor c\rfloor-1\), which occurs only when \(0\leq\theta=O_w(c^{-1})\). In that exceptional case, replacing \(d=-1-\theta\) by \(d=-\theta\) changes \(d^2+d\) by \(2\theta=O_w(c^{-1})\), absorbed in the displayed uniform \(O_w(c^{-2})\) relative error. Thus \(d^2+d+1/6\) can uniformly be replaced by \(B_2(\theta)\), proving the boxed expansion, including exact mode crossings.

**5. Attainment of the oscillatory range.** The continuous periodic profile \(-B_2(\theta)/2-w^2/24\) ranges from \(-1/12-w^2/24\) to \(1/24-w^2/24\). For any chosen \(\theta\in[0,1)\), take \(c_j=j+\theta\) and \(a_j=c_j-w/2\), which is eventually positive. The uniform remainder tends to zero, producing every point of that interval as a subsequential limit, while excluding all others.

## Verification
The standalone `checker.py` evaluates the incomplete-gamma eigenvalues independently of the boundary difference formula, verifies the neighboring-mode sign law on a diverse deterministic parameter grid, tests every claimed two-mode crossing in multiple bandwidths, checks the derivative-jump identity against finite and analytic differences, and compares the oscillatory asymptotic coefficient over increasingly distant annuli. It runs with Python 3 and `mpmath` and prints assertion counts. The infinite-dimensional statements, the exact uniqueness of all crossings, and the uniform asymptotic error rest on the analytic arguments above, not on finite computation.

## Relationship to prior work
Daubechies (1988) established Gaussian phase-space localization, Hermite diagonalization, and incomplete-gamma disk spectra. Abreu and Dörfler (first publicly posted 2012-02-27) explicitly explain that unions of concentric annuli preserve Hermite eigenfunctions; their principal theorem is inverse geometric rigidity. Knutsen (2019 preprint; 2020 open-access article), Section 3.1, considers precisely Gaussian localization on area-one rings and proves a leading operator-norm estimate with an \(O(R^{-3})\) error. The present statement does not claim the gamma eigenvalue formula or Hermite diagonalization as new. Its proposed increment is the exact crossing set and cusp amplitudes for every positive area, and the radius-dependent coefficient resolving that previously undetermined error order. An equivalent expansion obtained elsewhere from Poisson local limit theory remains a publication-priority risk.

## Limitations
This is an exact mathematical result for a Gaussian analysis window, concentric single annuli, and fixed area parameter in the asymptotic regime. It does not characterize nonradial masks, non-Gaussian windows, unions of several annuli, or regimes where \(w\) grows with \(a\). No claim of independent verification or priority certification is made. The possible existence of implicit equivalent results in classical special-function and Poisson asymptotics literature remains an originality risk.

## References
1. I. Daubechies, *Time-frequency localization operators: A geometric phase space approach*, IEEE Transactions on Information Theory **34** (1988), 605–612. DOI: 10.1109/18.9761. Author-hosted full text: https://sites.math.duke.edu/~ingrid/publications/ieee34-1988.pdf
2. L. D. Abreu and M. Dörfler, *An Inverse Problem for Localization Operators*, arXiv:1202.5841, first submitted 2012-02-27. https://arxiv.org/abs/1202.5841
3. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets I*, arXiv:1907.00848 (2019), Journal of Fourier Analysis and Applications **26** (2020), article 47, Section 3.1. DOI: 10.1007/s00041-020-09751-9. https://link.springer.com/article/10.1007/s00041-020-09751-9
