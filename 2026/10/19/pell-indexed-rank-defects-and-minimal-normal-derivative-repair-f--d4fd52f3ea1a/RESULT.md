# Pell-indexed rank defects and minimal normal-derivative repair for equatorial spin-two sampling

## Finding
Fix an integer \(\ell\ge2\), spin \(s\in\{-2,2\}\), and \(N=2\ell+1\). Sample the degree-\(\ell\), spin-\(s\) spherical-harmonic space at the \(N\) equally spaced equatorial points \((\theta,\phi)=(\pi/2,2\pi j/N)\), for \(0\le j<N\), in the standard spherical spin frame. The point-evaluation rank is
\[
\operatorname{rank}E_{\ell,s}=2\ell+1-\mathbf1_{\ell\text{ odd}}-2\mathbf1_{\ell\in\mathcal P},
\qquad
\mathcal P=\left\{\frac{x_k-1}{2}:k\ge2,\ x_k+y_k\sqrt2=(3+2\sqrt2)^k\right\}.
\]
The first exceptional degrees in \(\mathcal P\) are \(8,49,288,1681\). At each such degree the two additional invisible azimuthal orders are \(m=\pm y_k/2\). At every odd degree the order \(m=0\) is also invisible. These are **all** the blind orders; no other values of \(\ell\ge2\) have additional nullity. In particular the rank deficiencies are \(0,1,2,3\) according as the degree is even and nonexceptional, odd and nonexceptional, even exceptional, or odd exceptional.

The full Gram spectrum and achievable sample data are given explicitly below. Moreover, if \(d=N-\operatorname{rank}E_{\ell,s}\), then **exactly \(d\) additional point measurements of the standard-frame normal derivative \(\partial_\theta f\)** suffice to recover every coefficient. This is optimal among additional complex-linear scalar measurements. Choose derivative longitudes \(\{0\}\) if the blind set is \(\{0\}\), choose \(\{0,\pi/(2M)\}\) if it is \(\{-M,M\}\), or choose \(\{0,\pi/(2M),\pi/M\}\) if it is \(\{-M,0,M\}\). No extra derivative samples are needed when \(d=0\).

## Assumptions and scope
Use the standard orthonormal spin-weighted basis \({}_sY_{\ell m}\) in area measure \(d\Omega\), with \(-\ell\le m\le\ell\). Adopt the conventional Wigner normalization
\[
{}_sY_{\ell m}(\theta,\phi)=(-1)^s\sqrt{\frac{2\ell+1}{4\pi}}\,d^\ell_{m,-s}(\theta)e^{im\phi},
\]
where any equivalent consistent Condon–Shortley convention changes column phases only. A spin frame must be chosen to compare field values at distinct points. Normal derivatives are derivatives of the coefficient function in **that same fixed frame**, not gauge-invariant covariant derivatives. Complex coefficients are unrestricted; no reality condition is imposed.

Write \(a_{\ell m,s}={}_sY_{\ell m}(\pi/2,0)\) and \(A_{jm}=a_{\ell m,s}e^{2\pi imj/N}\). Let \(q=|m|\), let \(r!!\) be the double factorial, with \((-1)!!=0!!=1\), and put \(T=\ell(\ell+1)\). For both spin signs, the exact squared column amplitudes are
\[
|a_{\ell m,s}|^2=\frac{N}{4\pi}\frac{(\ell-2)!(\ell-q)!}{(\ell+2)!(\ell+q)!}\times
\begin{cases}
(2m^2-T)^2\left[\dfrac{(\ell+q-1)!!}{(\ell-q)!!}\right]^2,&\ell+q\text{ even},\\[3pt]
4m^2\left[\dfrac{(\ell+q)!!}{(\ell-q-1)!!}\right]^2,&\ell+q\text{ odd}.
\end{cases}
\]
Thus the \(N\) eigenvalues of \(A^*A\) are exactly \(N|a_{\ell m,s}|^2\), indexed by \(-\ell\le m\le\ell\); zeros are included and multiplicities occur on both signs of \(m\). The normalization is unit-area **not** assumed: the basis uses ordinary area \(4\pi\).

## Proof
**1. Fourier diagonalization.** The longitudes form the \(N\)-point Fourier grid and the distinct integer orders \(-\ell,\ldots,\ell\) form a complete residue system modulo \(N\). Thus distinct columns of \(A\) are orthogonal and \(A^*A=N\operatorname{diag}(|a_{\ell m,s}|^2)\). If \(\widehat y_m=N^{-1}\sum_{j=0}^{N-1}y_j e^{-2\pi imj/N}\), the exact image condition is \(\widehat y_m=0\) for every blind order, and the unique minimum-norm harmonic interpolant for admissible \(y\) has coefficients \(c_m=\widehat y_m/a_{\ell m,s}\) on visible orders and \(c_m=0\) on blind orders.

**2. Equatorial spin-two factors.** Set \(Y_{\ell m}=R_{\ell m}(\theta)e^{im\phi}\), including the usual scalar normalization. The two spin-raising applications and the scalar spherical-harmonic equation give, at the equator,
\[
{}_{2}Y_{\ell m}(\pi/2,\phi)=\sqrt{\frac{(\ell-2)!}{(\ell+2)!}}\left[(2m^2-T)R_{\ell m}(\pi/2)-2mR'_{\ell m}(\pi/2)\right]e^{im\phi}.
\]
The lowering identity gives the same zero set and squared moduli for spin \(-2\). The associated Legendre parity law implies \(R'_{\ell m}(\pi/2)=0\) and \(R_{\ell m}(\pi/2)\ne0\) when \(\ell+|m|\) is even; for odd parity, \(R_{\ell m}(\pi/2)=0\) and \(R'_{\ell m}(\pi/2)\ne0\). Inserting the standard associated-Legendre values and derivatives at zero produces precisely the displayed double-factorial spectrum. Therefore a blind order is either \(m=0\) with odd \(\ell\), or a nonzero order of even parity satisfying \(2m^2=T\). This exhaustive dichotomy proves no accidental cancellations remain.

**3. All integer resonances.** For positive \(M=|m|\), the equation \(2M^2=\ell(\ell+1)\) is equivalent to
\[
(2\ell+1)^2-2(2M)^2=1.
\]
All strictly positive integer solutions of this Pell equation are \((x_k,y_k)\), where \(x_k+y_k\sqrt2=(3+2\sqrt2)^k\), \(k\ge1\). The solution \(k=1\) has \(\ell=1\) and is excluded; \(k\ge2\) gives every other resonance. Recurrence modulo four gives \(x_k+y_k\equiv1\pmod4\); hence \(\ell+M=(x_k+y_k-1)/2\) is even, so every Pell solution belongs to the parity branch in which the factor can vanish. Also \(1\le M\le\ell\) because \(M^2=\ell(\ell+1)/2\le\ell^2\) for \(\ell\ge1\). The resonance therefore contributes exactly the two orders \(\pm M\), independently of the odd-degree order zero. No further possibilities exist.

**4. Minimal pointwise repair.** For each order, \(u_m(\theta)=d^\ell_{m,-s}(\theta)\) solves the smooth second-order equation
\[
u_m''+\cot\theta\,u_m'+\left[T-\frac{m^2+s^2+2ms\cos\theta}{\sin^2\theta}\right]u_m=0
\quad\text{for }0<\theta<\pi.
\]
A nonzero solution cannot have both \(u_m(\pi/2)=0\) and \(u_m'(\pi/2)=0\), by uniqueness for this regular initial-value problem. Hence every blind order has nonzero equatorial normal-derivative amplitude \(b_m=\partial_\theta{}_sY_{\ell m}(\pi/2,0)\). First reconstruct all visible coefficients by a discrete Fourier transform of the original \(N\) samples. Subtract their known contributions from the specified derivative readings. The remaining equations are \(z_j=\sum_{m\in B}b_mc_m e^{im\phi_j}\). For a single blind order, the coefficient is immediate. For \(B=\{\pm M\}\), the two specified phases \(e^{iM\phi}\) are \(1,i\), yielding a nonsingular two-by-two matrix. For \(B=\{-M,0,M\}\), the three phases \(1,i,-1\) yield a nonsingular Laurent–Vandermonde matrix. The repair uses exactly \(|B|=d\) derivative point readings. Fewer than \(d\) arbitrary additional complex-linear scalar measurements cannot injectively distinguish the \(d\)-dimensional old kernel by the rank-nullity theorem.

## Verification
Run `python3 verify_spin2.py` with a standard Python interpreter. The file independently computes rational squares of Wigner small-\(d\) entries at \(\pi/2\) from the finite factorial sum and from the displayed spin-raising / Legendre expression, checks Wigner-column unitarity, and compares zero sets with the Pell/parity classification. It performs \(3717\) exact comparisons for \(\ell=2,\ldots,60\), the \(59\) exact column-sum checks, and the first eight Pell pairs (with degree one excluded from the stated theorem). All tests passed. The unrestricted theorem follows from the symbolic steps above, not from the finite test range.

## Relationship to prior work
Wiaux–Jacques–Vandergheynst (2005), especially equations (14)–(15), already derives the general spin-\(\pm2\) to scalar-harmonic identity. In particular, its formula explicitly contains the factor \(2m^2-\ell(\ell+1)\). **That coefficient identity is not claimed as new.** Huffenberger–Wandelt (2010) uses Wigner matrices at \(\pi/2\) for full-sphere spin transforms. Elahi and collaborators (2018) use multiple iso-latitude rings in an optimal-dimensionality spin sampling theorem. These results supply the analytic and numerical context but do not state the complete **one-equatorial-ring**, **all-degree Pell nullity**, **explicit exact finite Fourier image**, or **minimal sparse normal-derivative repair** classification established here. The theorem therefore refines explicit prior pointwise identities; readers should not mistake it for a newly derived spin-harmonic formula.

## Limitations
This theorem addresses one exactly equatorial ring, one fixed harmonic degree, and spin \(\pm2\). It does not assert stable recovery under noise: derivative amplification may be severe. The normal derivatives depend on the stated spin gauge. General pointwise spin formulas in prior literature can be specialized to obtain the displayed coefficients, so priority of the sharper global Pell-and-repair classification remains a residual bibliographic risk. An accessible search index exposed the exact equatorial coefficient formula in a Southampton thesis, but the underlying linked full text could not be inspected. Independent validation and external review have not been performed.

## References
1. Y. Wiaux, L. Jacques and P. Vandergheynst, *Fast spin ±2 spherical harmonics transforms and application in cosmology*, arXiv:astro-ph/0508514, first available 2005-08-24, equations (14)–(15). https://arxiv.org/abs/astro-ph/0508514
2. K. M. Huffenberger and B. D. Wandelt, *Fast and Exact Spin-s Spherical Harmonic Transforms*, arXiv:1007.3514 (2010), especially section 2. https://arxiv.org/abs/1007.3514
3. U. Elahi et al., *An Optimal-Dimensionality Sampling for Spin-s Functions on the Sphere*, arXiv:1809.01321 (2018). https://arxiv.org/abs/1809.01321
4. Standard associated Legendre parity and the classical Pell-unit parametrization are used in their usual forms.
