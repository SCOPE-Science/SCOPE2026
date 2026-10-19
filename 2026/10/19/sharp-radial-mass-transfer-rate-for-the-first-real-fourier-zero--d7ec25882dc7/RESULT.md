# Sharp radial mass-transfer rate for the first real Fourier zero of a ball

## Finding

For each integer \(d\ge2\), let \(B\subset\mathbb R^d\) denote the unit ball, \(v_d=|B|\), and let \(\mathcal R_d(t)\) consist of all measurable rotationally invariant sets \(E\subset\mathbb R^d\) with
\[
|E|=v_d,\qquad |E\setminus B|=|B\setminus E|=t v_d.
\]
Define the first positive real Fourier-zero radius (using \(e^{-i x\cdot\xi}\) without a \(2\pi\) factor) by
\[
\kappa(E)=\inf\{s>0:\int_E e^{-isx_1}\,dx=0\}.
\]
Set \(\nu=d/2\), \(s_1=j_{\nu,1}\), \(s_2=j_{\nu,2}\), the first two positive zeros of the ordinary Bessel function \(J_\nu\). Then
\[
\boxed{\lim_{t\downarrow0}\frac{\sup_{E\in\mathcal R_d(t)}\kappa(E)-s_1}{t}
= C_d
=\frac{s_1}{d}\left[1+\left(\frac{s_1}{s_2}\right)^{\nu-1}
\frac{J_\nu'(s_2)}{|J_\nu'(s_1)|}\right].}
\]
In particular \(C_d>0\) and \(\kappa(B)=s_1\). The supremum ranges over *all* measurable radial sets satisfying the mass constraint; no boundedness, connectedness, or regularity of \(E\) is assumed.

For \(a=s_2/s_1\), the explicit two-component sets
\[
E_t=B_{(1-t)^{1/d}}\ \cup\ \{x\in\mathbb R^d:a\le |x|\le(a^d+t)^{1/d}\}
\]
are in \(\mathcal R_d(t)\) for \(0<t<1\), and attain the sharp asymptotic rate:
\[
\boxed{\kappa(E_t)=s_1+C_d t+O_d(t^2).}
\]
The result is **only the first-order sharp asymptotic**, not a classification of maximizers at a fixed positive \(t\).

## Assumptions and scope

For a finite-measure rotation-invariant set, the Fourier transform is a continuous real radial function. Its value at the origin is positive. The theorem concerns its least positive *real* zero and the symmetric-difference perturbation budget \(|E\triangle B|=2t v_d\). All radii and frequencies are in the above unscaled Fourier convention. In particular \(\nu\ge1\).

Introduce the normalized ball and sphere transforms
\[
b_d(s)=2^\nu\Gamma(\nu+1)\,s^{-\nu}J_\nu(s),\qquad
\phi_d(u)=2^{\nu-1}\Gamma(\nu)\,u^{1-\nu}J_{\nu-1}(u),
\]
with continuous values \(b_d(0)=\phi_d(0)=1\). Here \(b_d(s)=v_d^{-1}\int_B e^{-isx_1}\,dx\) and \(\phi_d(u)\) is the average of \(e^{-iu\theta_1}\) over the unit sphere. Write \(A_d=-b_d'(s_1)>0\) and \(\Delta_d=\phi_d(s_2)-\phi_d(s_1)>0\); the claimed coefficient equivalently equals \(\Delta_d/A_d\).

## Proof

**1. The sphere-kernel extremal values.** The radial sphere kernel obeys
\[
\phi_d''(u)+\frac{d-1}{u}\phi_d'(u)+\phi_d(u)=0,
\qquad \phi_d'(u)=-2^{\nu-1}\Gamma(\nu)u^{1-\nu}J_\nu(u).
\]
The first positive critical points of \(\phi_d\) are therefore \(s_1,s_2\). On \((0,s_1)\), \(J_\nu>0\), so \(\phi_d\) decreases; on \((s_1,s_2)\), it increases. For \(u>0\), define the mechanical energy \(H(u)=\phi_d(u)^2+\phi_d'(u)^2\). Differentiating and using the displayed ODE gives
\[
H'(u)=-\frac{2(d-1)}{u}\phi_d'(u)^2\le0.
\]
Because \(d\ge2\), the absolute values of successive nonzero extrema strictly decrease; this follows by integrating the negative derivative between distinct critical points. Standard Bessel oscillation implies there are infinitely many alternating extrema and their values tend to zero. Hence \(\phi_d(s_1)\) is its global minimum on \([0,\infty)\), while \(\phi_d(s_2)\) is its maximum on \([s_1,\infty)\). In particular, whenever \(s_1\le s<s_2\),
\[
\min_{0\le r\le1}\phi_d(sr)=\phi_d(s_1),
\qquad
\max_{r\ge1}\phi_d(sr)=\phi_d(s_2).
\]
The first identity uses the interval's inclusion of \(s_1\), and the second its inclusion of \(s_2\).

**2. A uniform upper bound for every admissible set.** Radial integration expresses the normalized Fourier transform as an average of \(\phi_d(s|x|)\) over the set. For any \(E\in\mathcal R_d(t)\), subtract the integral over the removed part \(B\setminus E\) and add that over the exterior part \(E\setminus B\). By Step 1, for every \(s_1\le s<s_2\),
\[
\frac1{v_d}\int_E e^{-isx_1}\,dx
\le b_d(s)+t\{\phi_d(s_2)-\phi_d(s_1)\}
=b_d(s)+t\Delta_d.
\]
This estimate has no error term and is uniform in \(E\), including unbounded sets. Since \(b_d(s_1)=0\), \(b_d'(s_1)=-A_d<0\), the implicit-function theorem supplies for all sufficiently small \(t\ge0\) a unique \(\sigma_t\in[s_1,s_2)\) near \(s_1\) with \(b_d(\sigma_t)+t\Delta_d=0\), and
\[
\sigma_t=s_1+\frac{\Delta_d}{A_d}t+O_d(t^2).
\]
At \(s=\sigma_t\), every admissible Fourier transform is nonpositive, whereas its value at zero equals \(v_d>0\). Continuity and the intermediate-value theorem imply \(\kappa(E)\le\sigma_t\). Thus the uniform supremum satisfies the claimed upper first-order bound.

**3. Sharp explicit mass transfer.** Let \(a=s_2/s_1>1\) and form \(E_t\) as stated. Its inner ball has volume \((1-t)v_d\), its outer shell volume \(t v_d\), and the pieces are disjoint. As \(t\downarrow0\), the two normalized perturbation integrals converge respectively to \(\phi_d(s)\) and \(\phi_d(as)\); indeed the normalized Fourier profile of \(E_t\), denoted \(g_t(s)\), satisfies on each fixed compact interval of \(s\)
\[
g_t(s)=b_d(s)+t\{\phi_d(as)-\phi_d(s)\}+O_d(t^2),
\]
with the error also holding after a fixed finite number of derivatives. At \(s=s_1\), its first variation is precisely \(\Delta_d\). The simple-zero implicit-function theorem gives a zero \(\widetilde\sigma_t=s_1+(\Delta_d/A_d)t+O_d(t^2)\). To show it is the *first* positive zero, fix a small interval around \(s_1\) on which \(b_d'\) remains negative; by uniform \(C^1\) convergence, \(g_t'\) remains negative there. On the complementary compact subinterval \([0,s_1-\varepsilon]\), \(b_d>0\) and \(g_t\to b_d\) uniformly. Thus there is no earlier zero and \(\kappa(E_t)=\widetilde\sigma_t\).

**4. The exact Bessel coefficient.** The recurrence \(J_{\nu-1}(s_i)=J_\nu'(s_i)\) at zeros of \(J_\nu\), together with \(b_d'(s_1)=2^\nu\Gamma(\nu+1)s_1^{-\nu}J_\nu'(s_1)\) and \(2\Gamma(\nu+1)=d\Gamma(\nu)\), yields
\[
\frac{\Delta_d}{A_d}
=\frac{s_1}{d}\left[1+\left(\frac{s_1}{s_2}\right)^{\nu-1}
\frac{J_\nu'(s_2)}{|J_\nu'(s_1)|}\right].
\]
Both terms inside the brackets are positive because the first and second positive Bessel zeros have derivative signs negative and positive, respectively. This completes the proof for all integer \(d\ge2\).

## Verification

A standalone numerical cross-check, `check.py`, evaluates Bessel zeros and normalized transforms, explicitly tests the volume-preserving two-shell family, and compares the computed zero displacement with the analytic \(C_d\) for dimensions \(2\) through \(7\) at two small perturbation sizes. It uses SciPy and NumPy. For \(d=2\), it returns \(s_1\approx3.831705970\), \(s_2\approx7.015586670\), \(a\approx1.830930328\) and \(C_2\approx3.343448881\). These finite-precision calculations check the formula only; the all-dimensions conclusion follows from the proof above.

## Relationship to prior work

Benguria, Levitin and Parnovski (2008/2009), *Fourier transform, null variety, and Laplacian's eigenvalues*, especially Section 9 and Theorem 2.8, **already construct nonconvex nearly radial perturbations whose first Fourier zero moves beyond that of the disk**. Thus the existence of a nonconvex counterexample or the qualitative possibility of outward improvement is expressly *not* claimed as new. Their planar construction uses radial redistribution with angular spikes; the stated theorem does not provide the sharp first-order variational constant under a fixed radial symmetric-difference budget, its attainment by a two-shell family, or the all-dimensional formula involving the first two Bessel zeros.

Gómez-Serrano, Levitin, Platt and Polterovich (2026), *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, studies fixed-volume *convex* bodies, proving counterexamples and higher-dimensional nonattainment. Its objects and optimization constraint are distinct from the present nonconvex radial infinitesimal mass-transfer problem. Classical Bessel identities and zeros, including the facts used for the sphere kernel, are standard and not asserted as new.

## Limitations

The theorem concerns measurable rotationally invariant sets and the limit of an arbitrarily small symmetric-difference budget. It does not treat convex or connected domains, finite-budget global optimizers, complex Fourier zeros, or optimal nonradial perturbations. The literature comparison supports a distinction between quantitative first-order radial optimality and earlier qualitative mass-redistribution counterexamples; it is not an exhaustive historical-priority guarantee.

## References

1. R. Benguria, M. Levitin and L. Parnovski, *Fourier transform, null variety, and Laplacian's eigenvalues*, arXiv:0801.1617, Section 9 and Theorem 2.8. https://arxiv.org/abs/0801.1617
2. J. Gómez-Serrano, M. Levitin, D. Platt and I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517, posted September 9, 2026. https://arxiv.org/abs/2609.10517
3. NIST Digital Library of Mathematical Functions, §10.21, Bessel-function zeros and interlacing. https://dlmf.nist.gov/10.21
