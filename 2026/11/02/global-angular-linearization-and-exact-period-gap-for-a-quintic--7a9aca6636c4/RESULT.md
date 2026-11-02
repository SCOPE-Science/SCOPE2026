# Global angular linearization and exact period gap for a quintic two-cycle annulus

## Finding
For the Llibre–Salhi quintic vector field defined below with \(a>1\), \(b>1\), and arbitrary \(\lambda\in\mathbb R\), the open annulus between its invariant unit circle \(C\) and invariant ellipse \(\mathcal E\) possesses a global smooth angular–radial coordinate. In this coordinate the exact first return map on *every* angular section is a dilation, not merely its derivative at either boundary:
\[
\rho\longmapsto e^{-2\pi\lambda/(ab)}\rho.
\]
If \(\lambda>0\), every trajectory in the annulus tends to \(C\); if \(\lambda<0\), every such trajectory tends to \(\mathcal E\); and if \(\lambda=0\), the entire open annulus is foliated by nonconstant periodic trajectories. In original, unrescaled physical time the two boundary periods satisfy the exact identity
\[
T_C=\frac{\pi}{\sqrt{ab(a-1)(b-1)}},\qquad
T_{\mathcal E}=\frac{\pi}{\sqrt{ab(a-1)(b-1)}}-\frac{\pi}{ab},
\qquad T_C-T_{\mathcal E}=\frac{\pi}{ab}.
\]
The boundary periods are independent of \(\lambda\). These conclusions classify dynamics *inside this annulus only*; they do not assert a global classification of all trajectories in the plane.

## Assumptions and scope
Let \(x,y\in\mathbb R\), \(a,b>1\), \(\lambda\in\mathbb R\). Define
\[
S=x^2+y^2,\quad E=\frac{x^2}{a}+\frac{y^2}{b}-1,\quad
R=(1-S)[-\lambda E+2(a-b)xy],\quad
\Omega=-2ab(SE-S+1),
\]
and the autonomous polynomial system
\[
\dot x=xR-y\Omega,\qquad \dot y=yR+x\Omega.
\]
This is the compact form of the quintic polynomial field in the cited primary sources. Its unit circle \(C=\{S=1\}\) lies strictly inside its ellipse \(\mathcal E=\{E=0\}\). The domain is the **entire open annulus**
\[
\mathcal A=\{(x,y):S>1,\ E<0\}.
\]
It is forward and backward invariant. Let \(\theta\in\mathbb R\) denote a lifted polar angle, and put \(d(\theta)=\cos^2\theta/a+\sin^2\theta/b\), so that \(E=S d(\theta)-1\). The radial parameter is
\[
\rho=\frac{S(S-1)}{-E}=\frac{S(S-1)}{1-d(\theta)S}\in(0,\infty).
\]
No conclusion is asserted at \(a=1\), \(b=1\), in other parameter quadrants, or outside \(\overline{\mathcal A}\).

## Proof
**1. Invariance and positive angular speed.** Direct differentiation gives the exact polynomial identities
\[
\begin{aligned}
\dot S&=2S(S-1)[\lambda E-2(a-b)xy],\\
\dot E&=E[-2\lambda(E+1)(1-S)+4(a-b)xy(1-2S)].
\end{aligned}
\]
Hence neither \(S=1\) nor \(E=0\) is crossed; the connected open region between them is invariant. In polar coordinates, \(\dot\theta=(x\dot y-y\dot x)/S=\Omega\). Throughout the closed annulus,
\[
\dot\theta=2ab[S(1-E)-1]>0.
\]
On the inner boundary \(S=1\), the strict inequality follows from \(E<0\); on the outer boundary \(E=0\), it follows from \(S>1\). Compactness provides \(0<c\le\dot\theta\le C_0<\infty\), so angular time covers all positive and negative physical time and no equilibrium lies in the closed annulus.

**2. Global coordinate and angular-time conjugacy.** For fixed \(\theta\), we have \(0<d(\theta)<1\) and \(1<S<1/d(\theta)\). The derivative
\[
\frac{\partial \rho}{\partial S}=
\frac{2S-1-d(\theta)S^2}{[1-d(\theta)S]^2}>0.
\]
Indeed, the numerator is increasing in \(S\le1/d(\theta)\) and is already \(1-d(\theta)>0\) at \(S=1\). The coordinate \(\rho\) tends to zero at the circle and to infinity at the ellipse. Thus \((\theta\bmod 2\pi,\rho)\) is a global smooth diffeomorphism \(\mathcal A\cong S^1\times(0,\infty)\).

The displayed identities imply, by differentiating logarithms, the exact identity
\[
\frac{d}{dt}\log\rho=-\frac{\lambda}{ab}\Omega.
\]
Since \(\dot\theta=\Omega>0\), the angular-time dynamics is
\[
\frac{d}{d\theta}\log\rho=-\frac{\lambda}{ab},\qquad
\log\rho(\theta)=\log\rho(\theta_0)-\frac{\lambda}{ab}(\theta-\theta_0).
\]
After one positively oriented revolution, the exact Poincaré map is multiplication by \(e^{-2\pi\lambda/(ab)}\) in \(\rho\), globally on \((0,\infty)\). This is an **angular-time conjugacy**; physical time has not been replaced silently.

**3. Global annular behavior.** For \(\lambda>0\), the preceding equality gives \(\rho\to0\) as \(t\to+\infty\). Uniform continuity of the inverse radial-coordinate map on the compact closed annulus implies \(S\to1\), hence convergence in distance to \(C\). For \(\lambda<0\), \(\rho\to\infty\) and \(E\to0\), hence convergence to \(\mathcal E\). For \(\lambda=0\), each level \(\rho=\rho_0>0\) is a smooth closed graph in polar angle, and strictly positive angular speed makes it a periodic orbit. These closed orbits are nonisolated and therefore are not limit cycles.

**4. Exact physical periods.** On the circle \(S=1\),
\[
\dot\theta=2ab[1-d(\theta)];\qquad
T_C=\int_0^{2\pi}\frac{d\theta}{2ab[1-d(\theta)]}
=\frac{\pi}{\sqrt{ab(a-1)(b-1)}}.
\]
For the ellipse use \(x=\sqrt a\cos\varphi\), \(y=\sqrt b\sin\varphi\), and write \(S(\varphi)=a\cos^2\varphi+b\sin^2\varphi\). On \(E=0\), the radial component of the field vanishes in the ellipse-normal direction and
\[
\dot\varphi=\frac{x\dot y-y\dot x}{\sqrt{ab}}=2\sqrt{ab}\,S(\varphi)[S(\varphi)-1].
\]
Hence
\[
\begin{aligned}
T_{\mathcal E}&=\frac{1}{2\sqrt{ab}}
\int_0^{2\pi}\left[\frac{1}{S(\varphi)-1}-\frac{1}{S(\varphi)}\right]d\varphi\\
&=\frac{\pi}{\sqrt{ab}}
\left[\frac{1}{\sqrt{(a-1)(b-1)}}-\frac{1}{\sqrt{ab}}\right]
=T_C-\frac{\pi}{ab}.
\end{aligned}
\]
Here we used the elementary identity \(\int_0^{2\pi}d\varphi/(u\cos^2\varphi+v\sin^2\varphi)=2\pi/\sqrt{uv}\) for \(u,v>0\). All formulas hold for \(a=b>1\) as well.

## Verification
The accompanying `checks/check_annulus.py` reconstructs the two polynomial derivatives and symbolically verifies the exact logarithmic-drift identity for general nonzero symbolic parameters. It also independently integrates the original physical-time period formulas at three nontrivial parameter pairs and compares them with the closed forms at high precision. Run `python3 checks/check_annulus.py` with SymPy and mpmath installed; its saved standard output is `checks/checker_output.txt`. The global covering, strict coordinate monotonicity, and asymptotic conclusions are proven above and are not inferred from a finite test.

## Relationship to prior work
Llibre and Salhi (2019), Theorem 2(f), give an at-most-two limit-cycle result for \(a,b>1\), and explicitly exhibit the rational first integral \(S(S-1)/E\) when \(\lambda=0\). That first integral is **not claimed as new**. Cao, Chen and Tang (2026), §12.4.10, establish exactly two hyperbolic boundary cycles for nonzero \(\lambda\) and calculate their local Floquet multipliers \(e^{\mp2\pi\lambda/(ab)}\). Their published section does not establish a global dilation conjugacy on every interior transversal or the physical-time period gap. The equality of the *local* circle multiplier and the *global* conjugate return factor is a consequence of the new global calculation, not an originality claim about the multiplier itself. The result therefore strengthens an exact-count theorem with a complete annular transition from a period foliation to global selection of one boundary orbit, and a new exact comparison of two distinct boundary periods.

## Limitations
The conjugacy uses angular time; physical-time trajectories do not generally move at uniform angular speed. No assertion is made for the region inside the unit circle, outside the ellipse, or for parameter regimes where the two curves intersect. This proof does not establish quantitative global Euclidean convergence constants, sensitivity to perturbations outside the specified family, or comprehensive priority over all historical Darboux-system literature. The scientific review is not independent validation.

## References
1. C. Cao, H. Chen, Y. Tang, *New criteria for upper bounds on the number of limit cycles in Liénard systems*, arXiv:2610.30417v1, first public submission 21 October 2026; §12.4.10. https://arxiv.org/html/2610.30417v1
2. J. Llibre, T. Salhi, *The limit cycles of a class of quintic polynomial vector fields*, Topological Methods in Nonlinear Analysis 54 (2019), 141–151, DOI:10.12775/TMNA.2019.030; accessible author preprint: https://ddd.uab.cat/pub/artpub/2019/221388/topmetnonana_a2019v54n1p141.pdf
