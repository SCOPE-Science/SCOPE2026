# Sharp zero-free radii and boundary-contact staircase for weighted harmonic Bergman kernels

## Finding

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). For every real \(\alpha>-1\), put \(p=\alpha+2>1\) and equip the complex Hilbert space of complex-valued harmonic functions with the measure
\[
 d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dA(z).
\]
Its real-valued reproducing kernel depends on \(t=z\overline w\) by
\[
 K_\alpha(z,w)=H_p(t),\qquad H_p(t)=2\operatorname{Re}(1-t)^{-p}-1.
\]
The principal branch is unambiguous because \(\operatorname{Re}(1-t)>0\) in the disk.

**Theorem (sharp inradius and boundary staircase).** For all real \(p>1\):

1. The largest centered scalar disk containing no zeros is \(|t|<\rho_p\), where
\[
 \rho_p=2^{1/p}-1.
\]
On its boundary the unique zero is \(t=-\rho_p\). Every interior zero of \(H_p\) is regular as a planar real-analytic level set.

2. For \(p>1\), define the finite integer counts
\[
 A_p=\#\left\{k\in\mathbb N:\frac{p-1}{6}<k<\frac{p-1}{4}\right\},\qquad
 D_p=\mathbf1_{\{p=6k+1\text{ for some }k\in\mathbb N\}}.
\]
Let \(E_p\) be one if \(\cos(\pi p/2)>0\), or if \(\cos(\pi p/2)=0\) and \(\sin(\pi p/2)>0\); otherwise let \(E_p=0\). Exactly
\[
 N_p^+=2A_p+D_p+E_p
\]
distinct kernel zeros occur on the open upper semicircle \(|t|=1,\operatorname{Im}t>0\), excluding the singular point \(t=1\). Exactly \(N_p^+\) lie on the lower semicircle and none at \(t=-1\). Boundary values here are the continuous extension of \(H_p\) away from \(t=1\).

3. These boundary zeros are transverse to the unit circle, except precisely for \(p=p_*=6k+1\), \(k\ge1\). At such an exponent there is one quadratic tangency on each open semicircle, exactly at \(t=e^{\pm i\pi/3}\). In the right-half-plane coordinate \(u=(1-t)^{-1}=x+iy\), the positive-imaginary tangency satisfies \(u=e^{i\pi/3}\). For \(p<p_*\) sufficiently close to \(p_*\), two transverse boundary intersections lie nearby, at
\[
 y_\pm(p)=\frac{\sqrt3}{2}\pm
 \sqrt{\frac{2\pi\sqrt3}{3p_*(p_*-1)}}\sqrt{p_*-p}
 +O(p_*-p).
\]
For \(p>p_*\) sufficiently close, no boundary intersections lie nearby. The lower-half-plane case is its reflection.

The staircase counts distinct boundary zeros, not the number of connected interior nodal arcs. It is a global boundary-intersection classification, not a claim of a complete interior topology classification.

## Assumptions and scope

The exponent \(\alpha>-1\) is arbitrary real; hence \(p>1\) is not necessarily an integer. \(dA\) denotes planar Lebesgue area, \(\mathbb N=\{1,2,\ldots\}\), and products \(t=z\overline w\) cover every scalar \(|t|<1\). A scalar zero is a vanishing of the real-valued kernel; unlike a holomorphic kernel its zeros generically form real curves. The unit-circle count concerns the scalar \(t\)-disk boundary and excludes \(t=1\), where the formula has a singularity.

## Proof

**Kernel normalization.** Orthogonality of the harmonic modes \(1,z^n,\overline z^{\,n}\) under normalized radial area measure gives
\[
 \|z^n\|^2=\frac{\Gamma(p)n!}{\Gamma(p+n)},\qquad n\ge0.
\]
Thus the normalized harmonic reproducing kernel is
\[
 1+\sum_{n\ge1}\frac{(p)_n}{n!}(t^n+\overline t^{\,n})
 =(1-t)^{-p}+(1-\overline t)^{-p}-1.
\]

**Inradius and uniqueness.** Write \(t=re^{i\theta}\) for \(0\le\theta\le\pi\), and \(\delta=\pi-\theta\). Let \(\psi(\delta)=\arg(1+r e^{i\delta})\). For \(0<r<1\),
\[
 \psi(0)=0,\quad \psi'(0)=\frac{r}{1+r},\quad
 \psi''(\delta)=-\frac{r(1-r^2)\sin\delta}{(1+2r\cos\delta+r^2)^2}<0
 \quad(0<\delta<\pi).
\]
Consequently \(0\le\psi(\delta)\le r\delta/(1+r)\). Bernoulli's inequality gives \(p(2^{1/p}-1)<1\) for \(p>1\). For \(0<r\le\rho_p=2^{1/p}-1\),
\[
 0<\theta+(p+1)\psi(\pi-\theta)<\pi\qquad(0<\theta<\pi).
\]
Direct differentiation yields
\[
 \frac{d}{d\theta}\operatorname{Re}(1-r e^{i\theta})^{-p}
 =-pr|1-r e^{i\theta}|^{-p-1}
 \sin\big(\theta+(p+1)\psi(\pi-\theta)\big)<0.
\]
The minimum on a circle of radius \(r\le\rho_p\) therefore occurs uniquely at \(t=-r\) and equals \((1+r)^{-p}\). It exceeds \(1/2\) for \(r<\rho_p\), and equals \(1/2\) at \(r=\rho_p\), proving the sharp zero-free disk and the unique first zero.

**Interior regularity.** The Möbius coordinate \(u=(1-t)^{-1}\) maps \(\mathbb D\) onto \(\{\operatorname{Re}u>1/2\}\). There \(H_p=2\operatorname{Re}u^p-1\). Since the complex derivative \(pu^{p-1}\) never vanishes in the right half-plane, the real level set \(H_p=0\) is smooth with nonvanishing gradient, including the first radial zero.

**Boundary count.** On \(|t|=1\), \(t\ne1\), write \(u=1/2+iy=\frac{e^{i\varphi}}{2\cos\varphi}\) for \(-\pi/2<\varphi<\pi/2\). Its upper side corresponds to \(0<\varphi<\pi/2\). Boundary zeros satisfy
\[
 F_p(\varphi):=\frac{\cos(p\varphi)}{\cos^p\varphi}=2^{p-1}.
\]
The key exact derivative identity is
\[
 F_p'(\varphi)=-\frac{p\sin((p-1)\varphi)}{\cos^{p+1}\varphi}.
\]
All its critical points are \(\varphi_j=j\pi/(p-1)\) inside \((0,\pi/2)\). At odd indices \(j\), \(F_p(\varphi_j)=-\cos^{-(p-1)}\varphi_j<0\), a strict minimum. At even indices \(j=2k\), \(F_p(\varphi_{2k})=\cos^{-(p-1)}\varphi_{2k}>0\), a strict maximum. Such a maximum exceeds the target \(2^{p-1}\) exactly when
\[
 \frac{p-1}{6}<k<\frac{p-1}{4},
\]
and equals it precisely when \(p=6k+1\). Hence each strict superlevel maximum creates exactly two simple crossings, and the equality case exactly one tangent contact. Initial value \(F_p(0)=1<2^{p-1}\). At the remaining endpoint, \(F_p(\varphi)\to+\infty\) exactly in the case encoded by \(E_p=1\): when \(\cos(p\pi/2)>0\), or at a zero of that cosine if \(\sin(p\pi/2)>0\). Otherwise its endpoint limit is \(-\infty\). (For an odd integer \(p\), the leading endpoint term has sign \(\sin(p\pi/2)\) and order \((\pi/2-\varphi)^{1-p}\).) Thus the terminal monotonic interval contributes precisely \(E_p\) additional crossings. This proves \(N_p^+=2A_p+D_p+E_p\). Reflection gives the lower-side count, and at \(t=-1\), \(u=1/2\), so \(\operatorname{Re}u^p<1/2\), excluding a zero there.

**Rigidity and square-root splitting.** Define \(B(p,x,y)=\operatorname{Re}(x+iy)^p-1/2\); a boundary tangency on \(x=1/2\) satisfies \(B=B_y=0\). Writing \(u=R e^{i\varphi}\), the derivative condition implies \((p-1)\varphi=j\pi\). Positivity of \(B+1/2\) forces even \(j\), and then
\[
 \operatorname{Re}u^p=R^p\cos\varphi
 =2^{-p}\cos^{-(p-1)}\varphi=\frac12
\]
forces \(|\varphi|=\pi/3\). Therefore \(p=6k+1\) for an integer \(k\ge1\), and the tangencies are exactly \(u=e^{\pm i\pi/3}\), equivalently \(t=e^{\pm i\pi/3}\). At the positive tangency,
\[
 B_p=-\frac{\pi\sqrt3}{6},\quad B_y=0,\quad
 B_{yy}=-\frac{p_*(p_*-1)}{2},\quad B_x=p_*>0.
\]
The nonzero second derivative proves quadratic contact with the boundary line \(x=1/2\), and the nonzero parameter derivative gives the stated square-root splitting by Taylor expansion and the implicit function theorem. Local zero curves lie on the interior side of the tangency at the critical exponent.

## Verification

The accompanying standalone script `checks/boundary_phase_check.py` recomputes the endpoint and extremum count for specified exponents, compares it against independently located boundary roots, tests 150 deterministic noninteger exponents, checks the sharp inradius by direct circle samples, and checks the local square-root law near exponent \(p=7\). A numerical root census is not used in the infinite-parameter proof. The script uses Python, NumPy, and SciPy; pinned minimum dependency names are provided in `requirements.txt`.

## Relationship to prior work

Engliš (arXiv:1601.03716v1, 2016) gives general weighted harmonic Bergman kernel formulas and high-power asymptotics, including the weight \((1-|z|^2)^\alpha\). The present theorem concerns the exact global zero-radius and complete scalar boundary-intersection behavior for this standard disk family, not kernel asymptotics. Zeytuncu (arXiv:1009.2806v1, 2010) constructs zeros for weighted **holomorphic** Bergman kernels under radial perturbations; these are different Hilbert spaces and kernels. Other radial analytic-kernel zero classifications do not imply the real-harmonic boundary-level-set staircase. The underlying power kernel and the Möbius half-plane map are classical, and are not asserted novel by themselves.

## Limitations

This result counts boundary intersections and establishes local contact transitions, but does not classify global connected components, nodal-arc lengths, or the distribution of intersections for all fixed interior radii beyond the sharp first radius. The proof concerns the disk and power weights, not arbitrary weights or higher-dimensional balls. Priority against older harmonic-kernel studies not found in the accessible literature remains a risk; no independent specialist audit has been performed.

## References

1. M. Engliš, *High-power asymptotics of some weighted harmonic Bergman kernels*, arXiv:1601.03716v1, publicly posted 2016-01-14, https://arxiv.org/abs/1601.03716.
2. Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, arXiv:1009.2806v1, posted 2010-09-14, https://arxiv.org/abs/1009.2806 (holomorphic comparison only).
