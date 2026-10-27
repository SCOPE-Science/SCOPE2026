# Finite-band obstruction and sharp approximation for the periodic Hilbert transform's weak-\(L^\infty\) norm

## Finding

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) carry normalized Lebesgue measure \(dm=d\theta/(2\pi)\). Let \(\mathcal H\) be the periodic Hilbert transform with Fourier multiplier \(-i\,\operatorname{sgn}(n)\) for \(n\ne0\) and multiplier \(0\) at \(n=0\). For a measurable real function \(g\), define
\[
\|g\|_{W(\mathbb T)}=\sup_{0<t\le1}\bigl(g^{**}(t)-g^*(t)\bigr),
\qquad
g^{**}(t)=\frac1t\int_0^t g^*(s)\,ds,
\]
where \(g^*\) is the decreasing rearrangement of \(|g|\).

For each integer \(N\ge0\), let \(\mathcal P_N\) be the real trigonometric polynomials of degree at most \(N\), and set
\[
C_N=\sup_{0\ne f\in\mathcal P_N}
\frac{\|\mathcal H f\|_{W(\mathbb T)}}{\|f\|_{L^\infty(\mathbb T)}}.
\]
Then
\[
0\le C_N<1\quad\text{for every finite }N,\qquad
C_N\le C_{N+1},\qquad
\lim_{N\to\infty}C_N=1.
\]
Thus no finite Fourier band attains the sharp global weak-\(L^\infty\) operator constant, but finite-band polynomials approach that constant as their degree increases.

## Assumptions and scope

The claim is for real-valued trigonometric polynomials on the circle, with the normalized measure and Hilbert-transform convention specified above. Constants are annihilated by \(\mathcal H\). The weak-\(L^\infty\) quantity is the rearrangement seminorm \(W\) used in the cited sharp inequality; it is not the usual weak-\(L^\infty\) expression, which coincides with \(L^\infty\).

No explicit formula or asymptotic rate for \(1-C_N\) is claimed. No finite-band analogue on the real line is asserted.

## Proof

Write \(g=\mathcal H f\), \(M=\|g\|_\infty\), and, for \(0\le\lambda<M\), define
\[
D_f(\lambda)=m\{|g|>\lambda\},\qquad
E_f(\lambda)=\int_{\mathbb T}(|g|-\lambda)_+\,dm,\qquad
\Psi_f(\lambda)=\frac{E_f(\lambda)}{D_f(\lambda)}.
\]
For a nonconstant trigonometric polynomial, \(g\) is a nonzero trigonometric polynomial. Hence \(D_f(\lambda)>0\) for \(\lambda<M\), and each level set \(\{|g|=\lambda\}\) has measure zero. The rearrangement definition therefore gives
\[
\|\mathcal H f\|_{W(\mathbb T)}=\sup_{0\le\lambda<M}\Psi_f(\lambda).
\]

The sharp global inequality of Osękowski is proved from the superharmonic majorant \(\mathcal U^{(1)}_\lambda\) of \(\mathcal V^{(1)}_\lambda\). Its boundary functions satisfy
\[
\mathcal V^{(1)}_\lambda(x,y)=(|y|-\lambda)_+-\mathbf1_{\{|y|>\lambda\}}.
\]
The explicit formula for the majorant gives, whenever \(-1<x<1\) and \(y>0\),
\[
U^{(1)}(x,y)-V^{(1)}(x,y)
=\frac2\pi\left[\arctan(A-B)+\arctan(A+B)\right]>0,
\]
where \(A=e^{-\pi y/2}/\cos(\pi x/2)>0\) and \(B=\tan(\pi x/2)\). For fixed \(B\), the function
\[
S(A)=\arctan(A-B)+\arctan(A+B)
\]
satisfies \(S(0)=0\) and
\[
S'(A)=\frac{1}{1+(A-B)^2}+\frac{1}{1+(A+B)^2}>0.
\]
Thus \(S(A)>0\) for \(A>0\).

Normalize \(\|f\|_\infty=1\). Since \(f\) is nonconstant, \(|f|<1\) except at finitely many points. For every \(\lambda<M\), the set \(\{|g|>\lambda,\ |f|<1\}\) has positive measure. On that set the majorant strictly exceeds the boundary function. The superharmonic mean-value argument from the cited proof yields
\[
E_f(\lambda)-D_f(\lambda)
=\int_{\mathbb T}\mathcal V^{(1)}_\lambda(f,g)\,dm
<
\int_{\mathbb T}\mathcal U^{(1)}_\lambda(f,g)\,dm
\le0.
\]
Consequently \(\Psi_f(\lambda)<1\) for every \(\lambda<M\). The function \(\Psi_f\) is continuous on \([0,M)\), and \(\Psi_f(\lambda)\le M-\lambda\), so it extends continuously by \(0\) at \(M\). Its maximum on \([0,M]\) is strictly below \(1\). This proves \(\|\mathcal H f\|_{W(\mathbb T)}<\|f\|_\infty\) for every nonconstant trigonometric polynomial; constants have ratio zero.

For fixed \(N\), the unit sphere of \(\mathcal P_N\) in the uniform norm is compact. The Hilbert transform is continuous on this finite-dimensional space, and the \(W\)-quantity is continuous under uniform convergence: if \(\|g-h\|_\infty\le\varepsilon\), then \(|g^*(t)-h^*(t)|\le\varepsilon\) and \(|g^{**}(t)-h^{**}(t)|\le\varepsilon\), hence \(|\|g\|_W-\|h\|_W|\le2\varepsilon\). Thus the supremum defining \(C_N\) is attained. Since every member of the unit sphere has ratio strictly below \(1\), compactness gives \(C_N<1\). The inclusions \(\mathcal P_N\subset\mathcal P_{N+1}\) imply \(C_N\le C_{N+1}\).

Finally, Osękowski's sharpness construction gives bounded real boundary data with a level ratio arbitrarily close to \(1\). If the level initially chosen has a level-set atom, move the level slightly upward: the superlevel measure and positive-part integral converge from the right, and a regular level (one with zero-measure level set) can be chosen with an equally large ratio. Poisson smoothing \(f_r=P_r*f\) preserves the \(L^\infty\) bound and satisfies \(\mathcal H f_r=P_r*(\mathcal H f)\). As \(r\uparrow1\), the transforms converge in \(L^1\) and in measure; at the chosen regular level, both the superlevel measure and the positive-part integral converge, so the corresponding \(\Psi_{f_r}(\lambda)\) approaches \(\Psi_f(\lambda)\). For fixed \(r<1\), the Fourier series of \(f_r\) and its Hilbert transform converge uniformly under truncation. The \(W\)-quantity is continuous under this uniform convergence, so a finite trigonometric polynomial achieves a ratio arbitrarily close to \(1\). Therefore \(\sup_{N\ge0} C_N=1\); monotonicity and \(C_N\le1\) give \(\lim_{N\to\infty}C_N=1\).

## Verification

The strict finite-band bound follows from the explicit positive majorant gap, the rearrangement identity, and compactness of a finite-dimensional unit sphere. The limiting assertion uses the source's sharpness construction followed by Poisson smoothing and uniform Fourier truncation. No numerical experiment or finite enumeration is used as proof.

The proof establishes a qualitative gap \(C_N<1\) for each fixed \(N\), but gives neither an explicit value of \(C_N\) nor a rate for \(1-C_N\). The approximation argument concerns the periodic circle only.

## Relationship to prior work

Osękowski proved \(\|\mathcal H f\|_{W(\mathbb T)}\le\|f\|_\infty\) and proved sharpness of the global constant by a conformal-map construction. The finite-band statement adds two conclusions not stated there: strict inequality for every finite-degree real trigonometric polynomial and convergence of the restricted constants \(C_N\) to the global sharp value. The strict part uses the strict form of the paper's explicit majorant gap on \(|x|<1\), then compactness; the limit part makes the sharpness witness finite-band by Poisson smoothing and Fourier truncation.

Searches of the mathematical claim database returned nearby work on cyclic Hilbert-transform endpoint norms and harmonic Hardy extremizers, but those concern discrete operators or different rearrangement quantities. No direct match for the sequence \(C_N\) or its strict finite-band gap was found in the bounded searches performed. This is not a proof that no unindexed result exists.

## Limitations

The theorem does not give a quantitative lower bound for \(1-C_N\), an explicit extremizer for any \(C_N\), or a classification of all sequences approaching \(1\). The novelty search was bounded to the cited primary paper and the retrieved mathematical-claim records. Independent audit has not been performed.

## References

A. Osękowski, “A Sharp Weak-Type \((\infty,\infty)\) Inequality for the Hilbert Transform,” *Complex Analysis and Operator Theory* **10** (2016), 1133–1143. First published online 25 March 2015. DOI: 10.1007/s11785-015-0454-y.
