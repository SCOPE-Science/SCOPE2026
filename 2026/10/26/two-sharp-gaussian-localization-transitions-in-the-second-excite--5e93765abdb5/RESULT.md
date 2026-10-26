# Two sharp Gaussian-localization transitions in the second excited Fock level

## Finding
Let \(T_\tau\) be compression of multiplication by \(e^{-\tau|z|^2}\) to the third true-polyanalytic Fock space, with \(\tau>0\) and normalized Gaussian area measure. Writing \(u=(1+\tau)^{-1}\), define
\[
L_0(u)=u^3,\qquad L_1(u)=u^2(3u^2-4u+2),
\]
\[
L_k(u)=u^{k-1}\left[\binom{k}{2}(1-u)^4+2ku^2(1-u)^2+u^4\right]\quad(k\ge2).
\]
These are exactly all eigenvalues, each associated to the angular mode \(k-2\). For every \(\tau>0\), the sharp operator norm and its entire norm-attaining eigenspace obey the following exhaustive classification:

* \(0<\tau<\frac12\): norm \(L_0(u)\), unique maximizing angular mode \(-2\).
* \(\tau=\frac12\): norm \(L_0(u)=L_1(u)\), two-dimensional top eigenspace of modes \(-2,-1\).
* \(\frac12<\tau<1\): norm \(L_1(u)\), unique maximizing mode \(-1\).
* \(\tau=1\): norm \(L_1(u)=L_2(u)\), two-dimensional top eigenspace of modes \(-1,0\).
* \(\tau>1\): norm \(L_2(u)\), unique maximizing mode \(0\).

Both crossings are transverse. In particular, no angular mode with index \(k\ge3\) ever maximizes Gaussian localization, despite infinitely many available angular modes.

## Assumptions and scope
On \(\mathbb C\), use \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\), and let \(\mathcal H_{(2)}\) denote the closed span in \(L^2(d\gamma)\) of the orthonormal complex-Hermite basis \(\{\Phi_k:k\ge0\}\), with
\[
\Phi_0(z)=\bar z^2/\sqrt2,\quad
\Phi_1(z)=\bar z(|z|^2-2)/\sqrt2,
\]
\[
\Phi_k(z)=\frac{z^{k-2}}{\sqrt{2k!}}\bigl(|z|^4-2k|z|^2+k(k-1)\bigr)\quad(k\ge2).
\]
Here \(\bar z\) denotes complex conjugation, and \(P_{(2)}\) denotes the orthogonal projection onto \(\mathcal H_{(2)}\). The operator is \(T_\tau=P_{(2)}M_{e^{-\tau|z|^2}}|_{\mathcal H_{(2)}}\). All assertions quantify over every real \(\tau>0\); the boundary value \(\tau=0\) is excluded because \(T_0\) is the identity and all modes tie. Norm-attaining vectors are precisely the nonzero vectors in the indicated top eigenspace, up to normalization.

## Proof
**Radial diagonalization and exact eigenvalues.** Each \(\Phi_k\) has angular frequency \(k-2\). Since the multiplier is radial, different angular sectors are orthogonal after multiplication, and \(T_\tau\Phi_k=L_k\Phi_k\). With \(t=|z|^2\), radial integration is integration against \(e^{-t}\,dt\). Consequently,
\[
L_0=\frac12\int_0^\infty e^{-(1+\tau)t}t^2\,dt,\qquad
L_1=\frac12\int_0^\infty e^{-(1+\tau)t}t(t-2)^2\,dt,
\]
\[
L_k=\frac1{2k!}\int_0^\infty e^{-(1+\tau)t}t^{k-2}(t^2-2kt+k(k-1))^2\,dt\quad(k\ge2).
\]
The identity \(\int_0^\infty t^m e^{-st}\,dt=m!s^{-m-1}\) gives the displayed formulas. For instance, the resulting polynomial in \(u\) for \(k\ge2\) is the sum of the square-polynomial terms after exact factorial cancellation; no asymptotic approximation is used. The eigenvalues tend to zero as \(k\to\infty\) because \(0<u<1\), so the diagonal operator is compact.

**No higher angular mode can dominate.** Put \(r=(1-u)/u>0\). For every integer \(k\ge2\), direct subtraction yields
\[
L_{k+1}-L_k=-u^{k+3}(1-u)Q_k(r),\qquad
Q_k(r)=\binom{k}{2}r^4-kr^3+2kr^2-2r+1.
\]
At \(k=2\),
\[
Q_2(r)=(r^2-r+1)^2+r^2>0.
\]
For larger indices,
\[
Q_k(r)=Q_2(r)+(k-2)r^2\left(\frac{k+1}{2}r^2-r+2\right)>0.
\]
Indeed, \(\frac{k+1}{2}r^2-r+2\) has positive leading coefficient and negative discriminant \(1-4(k+1)<0\). Thus \(L_{k+1}<L_k\) for all \(k\ge2\) and all \(u\in(0,1)\); only indices \(0,1,2\) need comparison.

**The exact two crossings.** Direct factorizations are
\[
L_1-L_0=u^2(u-1)(3u-2),
\qquad
L_2-L_1=u(u-1)(2u-1)(3u^2-3u+1).
\]
The factor \(3u^2-3u+1=3(u-\frac12)^2+\frac14\) is strictly positive. Therefore \(L_1=L_0\) only at \(u=2/3\) (equivalently \(\tau=1/2\)) and \(L_2=L_1\) only at \(u=1/2\) (equivalently \(\tau=1\)). Their simple factors give transversality. Sign inspection establishes the strict top-eigenvalue ordering in each open interval. At \(u=2/3\), \(L_2<L_1=L_0\); at \(u=1/2\), \(L_0<L_1=L_2\). The strict tail ordering excludes all further top degeneracies, and angular orthogonality gives the complete equality spaces.

## Verification
The accompanying standalone Python checker uses exact rational arithmetic. It recomputes all displayed eigenvalues from the factorial moment integrals for indices \(0\le k\le20\) and eight rational \(u\)-values, checks normalization at zero damping, confirms the adjacent-difference formulas and positive \(Q_k\) at rational parameters, and verifies optimal sectors at six damping levels. Its finite checks support the symbolic proof but are not substitutes for the all-parameter inequalities established above. Run `python3 verify_gaussian.py` from the extracted directory.

## Relationship to prior work
Abreu, Gröchenig, and Romero study polyanalytic Landau levels and radial *disk* localization, providing the complex-Hermite framework and spectral setting. Gaussian damping is a different localization symbol: this result classifies its operator norm and the complete maximizing eigenspace for every damping strength, and establishes exactly two transverse top-mode transitions. General Toeplitz quantization and compactness results do not imply the explicit inequality excluding every higher mode. Unlike sharp radial-disk spectra, the Gaussian family has a uniform three-mode upper envelope.

## Limitations
This theorem is restricted to the second excited (third true-polyanalytic) Fock level and the centered Gaussian radial multiplier. It makes no assertion for all polyanalytic levels, arbitrary radial masks, anisotropic multipliers, or perturbations of the Gaussian profile. Priority against every historical special-case computation is not independently certified. No external independent audit has been performed.

## References
1. L. D. Abreu, K. Gröchenig, and J. L. Romero, *Harmonic Analysis in Phase Space and Finite Weyl–Heisenberg Ensembles*, arXiv:1704.03042 (first public version April 10, 2017), especially the radial localization and polyanalytic spectral discussion; https://arxiv.org/abs/1704.03042 .
2. R. Fulsche and R. Hagger, *Toeplitz operators on polyanalytic Fock spaces*, arXiv:2308.11292 (2023); https://arxiv.org/abs/2308.11292 .
