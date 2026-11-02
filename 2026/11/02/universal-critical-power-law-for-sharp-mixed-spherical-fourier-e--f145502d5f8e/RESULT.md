# Universal critical power law for sharp mixed spherical Fourier-extension stability

## Finding

For each fixed integer \(d\ge3\), define the lower admissible exponent and Bessel order
\[
q_d=\frac{2d}{d-1},\qquad \nu=\frac d2-1.
\]
For \(q>q_d\) define the two weighted Bessel moments
\[
I_k(q)=\int_0^\infty r^{d-1}\big|r^{-\nu}J_{\nu+k}(r)\big|^q\,dr\quad(k=0,1).
\]
Let
\[
m(p)=\frac{\Gamma((p+1)/2)}{\sqrt\pi\,\Gamma((p+2)/2)},\qquad
A_d=\frac2{d-1}\left(\frac2\pi\right)^{q_d/2}m(q_d),
\]
and define the *critical adjacent-mode finite part*, as an ordinary conditionally convergent improper integral,
\[
L_d=\lim_{R\to\infty}\int_0^R r^{d-1}
\left(\left|r^{-\nu}J_\nu(r)\right|^{q_d}-
\left|r^{-\nu}J_{\nu+1}(r)\right|^{q_d}\right)dr.
\]
Then \(0<L_d<\infty\), and as the real exponent \(q=q_d+\varepsilon\) decreases to \(q_d\),
\[
\boxed{\Gamma_{d,q}=(2\pi)^d\frac{d-1}{d}L_d A_d^{-1/d}\varepsilon^{1/d}
\left(1+O_d(\varepsilon|\log\varepsilon|)\right).}
\]
Here \(\Gamma_{d,q}\) is the optimal global squared-distance stability coefficient in the radial--angular mixed spherical Fourier-extension inequality, with Fourier convention and surface measure specified below. The *relative* sharp gap satisfies the stronger expansion
\[
\boxed{\frac{\Gamma_{d,q}}{C_{d,q}^2}
=\frac{d-1}{d}\frac{L_d}{A_d}\varepsilon+O_d(\varepsilon^2).}
\]
Thus the absolute sharp stability constant decays with the **dimension-dependent universal fractional exponent** \(1/d\), even while the squared optimal extension norm diverges like \(\varepsilon^{-(d-1)/d}\). The displayed coefficients are strictly positive.

## Assumptions and scope

Let \(\sigma\) denote actual (unnormalized) surface measure on \(\mathbb S^{d-1}\), let \(P_0\) be orthogonal projection in \(L^2(\sigma)\) onto constants, and use
\[
\widehat{f\sigma}(x)=\int_{\mathbb S^{d-1}}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega),\quad
\|F\|_{q,2}=\left(\int_0^\infty\left(\int_{\mathbb S^{d-1}}|F(r\theta)|^2\,d\sigma(\theta)\right)^{q/2}r^{d-1}\,dr\right)^{1/q}.
\]
Define \(C_{d,q}=\sup_{\|f\|_2=1}\|\widehat{f\sigma}\|_{q,2}\), and \(\Gamma_{d,q}\) as the *largest* \(\Gamma\ge0\) for which
\[
C_{d,q}^2\|f\|_2^2-\|\widehat{f\sigma}\|_{q,2}^2\ge\Gamma\|f-P_0f\|_2^2
\quad\text{for all }f\in L^2(\mathbb S^{d-1},d\sigma).
\]
The statement is for each fixed \(d\ge3\) with constants in the error permitted to depend on \(d\), and for \(\varepsilon>0\) sufficiently small. It concerns neither ordinary unmixed restriction norms nor the exact critical exponent, where the input-to-mixed-norm operator is unbounded.

## Proof

**1. Exact optimal finite-exponent reduction (published premise).** Xu [1, Theorems 1.2--1.3] proves, for every integer \(d\ge3\) and every \(q>q_d\), the strict spherical-harmonic moment ordering and the optimal identity
\[
C_{d,q}^2=(2\pi)^d I_0(q)^{2/q},\qquad
\Gamma_{d,q}=(2\pi)^d\big(I_0(q)^{2/q}-I_1(q)^{2/q}\big).
\]
This published sharp formula, rather than merely a spectral upper bound, identifies the object whose *singular critical approach* is determined here. We do not reprove global finite-exponent sharpness.

**2. First common critical residue.** The classical fixed-order Hankel expansion, with \(a=(d-1)/2\) and \(c=(2/\pi)^{1/2}\), gives, as \(r\to\infty\),
\[
r^{-\nu}J_\nu(r)=c\,r^{-a}\big(\cos\theta(r)+O_d(r^{-1})\big),\qquad
r^{-\nu}J_{\nu+1}(r)=c\,r^{-a}\big(\sin\theta(r)+O_d(r^{-1})\big),
\]
where \(\theta(r)=r-\pi\nu/2-\pi/4\) (the sign of the sine is immaterial). For \(q\) in a fixed compact interval containing \(q_d>2\), the map \(x\mapsto|x|^q\) is uniformly Lipschitz on bounded intervals. Therefore
\[
r^{d-1}|r^{-\nu}J_{\nu+k}(r)|^q
=c^q r^{-1-a\varepsilon}H_{k,q}(r)+O_d(r^{-2-a\varepsilon}),
\]
where \(H_{0,q}=|\cos\theta|^q\), \(H_{1,q}=|\sin\theta|^q\), and each is \(\pi\)-periodic with the same mean \(m(q)\). The zero-mean parts have bounded primitives, uniformly for \(q\) near \(q_d\), so their integrals against \(r^{-1-a\varepsilon}\) remain bounded by integration by parts. The integrable error is also uniformly bounded. Consequently, as \(\varepsilon\downarrow0\),
\[
I_k(q)=\frac{c^{q}m(q)}{a\varepsilon}+O_d(1)=\frac{A_d}{\varepsilon}+O_d(1),\quad k=0,1.
\]
In particular \(C_{d,q}^2=(2\pi)^d(A_d/\varepsilon)^{(d-1)/d}\big(1+O_d(\varepsilon|\log\varepsilon|)\big)\).

**3. Cancellation and existence of the critical finite part.** Subtract the two pointwise expansions before integrating. The leading periodic difference
\[
H_{0,q}(r)-H_{1,q}(r)=|\cos\theta(r)|^q-|\sin\theta(r)|^q
\]
has exactly zero mean over each period. Its integral against \(r^{-1-a\varepsilon}\) exists at \(\varepsilon=0\) by Dirichlet's test; the remaining error decays as \(r^{-2}\). This proves existence and finiteness of \(L_d\), including near the origin by the ascending Bessel series. Differentiating the mean-zero periodic integral in \(\varepsilon\) is legitimate after one integration by parts: the derivative of its decreasing weight is bounded by \(O((1+\log r)/r^2)\) uniformly near \(0\); the derivative of the periodic factor again has zero mean and bounded primitive. The Bessel remainder has an integrable logarithmic derivative. Thus
\[
I_0(q)-I_1(q)=L_d+O_d(\varepsilon).
\]
The difference has a finite limit despite the separate \(\varepsilon^{-1}\) divergences.

**4. Strictly positive critical finite part.** Xu [1, Theorem 3.9 and its proof] establishes a stronger adjacent-mode comparison for every \(q>2\): if \(\rho_n\) is the \(n\)-th positive zero of \(J_{\nu+1}\), then *each* cell integral of
\(r^{d-1}(|r^{-\nu}J_\nu|^q-|r^{-\nu}J_{\nu+1}|^q)\)
between consecutive zeros of \(J_{\nu+1}\) is strictly positive. This cell statement applies at \(q=q_d>2\), even though the two individual full moments diverge there. The conditionally convergent difference from Step 3 is the limit along the same zeros; every finite partial sum is at least the strictly positive first-cell contribution. Hence \(L_d>0\). This uses an explicit published positivity lemma and does not infer strictness merely from inequalities for \(q>q_d\).

**5. Extract the fractional exponent and relative law.** For positive \(x=I_0(q)\) and \(y=I_1(q)=x-L_d+O_d(\varepsilon)\), Taylor's theorem at relative separation \((x-y)/x=O_d(\varepsilon)\) gives
\[
x^{2/q}-y^{2/q}=\frac2q\big(L_d+O_d(\varepsilon)\big)
 x^{2/q-1}\big(1+O_d(\varepsilon)\big).
\]
Since \(2/q_d=(d-1)/d\) and \(x=A_d/\varepsilon+O_d(1)\),
\[
x^{2/q-1}=A_d^{-1/d}\varepsilon^{1/d}
\big(1+O_d(\varepsilon|\log\varepsilon|)\big).
\]
This gives the stated optimal \(\Gamma_{d,q}\) asymptotic. Dividing by \(C_{d,q}^2\) instead yields
\[
1-\left(1-\frac{I_0(q)-I_1(q)}{I_0(q)}\right)^{2/q}
=\frac{d-1}{d}\frac{L_d}{A_d}\varepsilon+O_d(\varepsilon^2),
\]
with no logarithmic loss at that order. Both expressions remain exact sharp-coefficient conclusions by Step 1. \(\square\)

## Verification

The supplementary program `verify_critical_collapse.py` (NumPy/SciPy) rechecks the residue normalization, the gamma-function period mean, positivity of numerically integrated critical modal differences in dimensions three and four, and near-endpoint scaling across six parameter instances. It reports, illustratively, \(L_3\approx0.176150\) and \(L_4\approx0.143480\). Finite quadrature does not certify the improper integral, its positivity for every dimension, or the infinite-dimensional sharp constant; Steps 1--5 are the proof of those claims. The program approximates common infinite tails by their leading mean term, so its printed finite-parameter values are supplementary and not rigorous enclosures.

## Relationship to prior work

Carneiro--Oliveira e Silva--Sousa [2] reduced sharp mixed spherical restriction to Bessel moments. Ciccone--Sousa [3] improved available ranges of modal optimality. Xu [1] settled the exact modal ordering and globally sharp stability coefficient throughout the admissible exponent range and proved a finite-cutoff adjacent-mode positivity lemma even outside that range. Those results provide critical inputs but neither [1] nor [2] nor [3] states the *dimension-dependent exact singular asymptotic of the sharp stability coefficient* or the renormalized relative slope found here. The vanishing critical-endpoint law is logically distinct from asymptotic behavior at large exponents: near \(q_d\), both leading modal moments diverge and their common pole must be canceled before extracting the sharp gap. Searches for equivalent Bessel finite-part and critical-exponent formulations are documented in the associated review.

## Limitations

The fractional law applies to the radial--angular mixed norm and each fixed integer \(d\ge3\), not to the usual unmixed Fourier extension problem, and it supplies a conditional-integral representation rather than an elementary closed form for \(L_d\). The exact norm at the critical exponent is infinite; no endpoint stability inequality is asserted there. The proof relies on Xu's full sharpness theorem and finite-cell positivity statement; it proves the distinct singular asymptotic but not those premises anew. An equivalent unpublished or unindexed asymptotic treatment remains a residual originality risk. Independent mathematical audit has not been performed.

## References

[1] Zewei Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648, version 1 publicly posted 2026-10-14, Theorems 1.2--1.3 and 3.9, Sections 2--4. https://arxiv.org/abs/2610.19648

[2] Emanuel Carneiro, Diogo Oliveira e Silva and Mateus Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365 (first posted 2017-10-28), *Advances in Mathematics* 341 (2019), 583--608. https://arxiv.org/abs/1710.10365

[3] Valentina Ciccone and Mateus Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere*, arXiv:2312.07309 (2023); *Journal of Fourier Analysis and Applications* 31 (2025), article 70; DOI: 10.1007/s00041-025-10201-7. https://doi.org/10.1007/s00041-025-10201-7
