# A singular half-disk limit and sharp area laws for material Hopf circles

## Finding

For the cubic supercritical Hopf normal form \(\dot z=(1+i-|z|^2)z\), the transported boundaries of off-centre closed disks have **three distinct long-time geometric regimes**, separated by whether the initial circle encloses, touches, or excludes the repelling equilibrium at the origin. The critical, origin-tangent circle converges (in the co-rotating frame) to the boundary of a **filled half-disk**, including a non-obvious straight diameter contributed by a vanishingly narrow parameter boundary layer.

Let \(a\ge0\), \(R>0\), \(D_{a,R}=\{z\in\mathbb C:|z-a|\le R\}\), and let \(E_t=e^{-it}\Phi_t(D_{a,R})\), with \(\Phi_t\) the Hopf flow. Write \(A_t\) for Euclidean area and \(L_t\) for Euclidean boundary length. Set \(s=e^{2t}-1\). Then for \(t>0\) the **exact finite-time area** is
\[
A_t=\frac{\pi e^{2t}}{2s}\left(1-\frac{1+s(a^2-R^2)}{\sqrt{[1+s(a+R)^2][1+s(a-R)^2]}}\right),
\qquad A_0=\pi R^2.
\]
The Hausdorff limits of the compact sets \(E_t\), the area limits, and the boundary-length limits are:

| Initial circle | Hausdorff limit of \(E_t\) | \(\lim A_t\) | \(\lim L_t\) |
|---|---|---|---|
| \(a<R\) | closed unit disk | \(\pi\) | \(2\pi\) |
| \(a=R>0\) | closed right unit half-disk | \(\pi/2\) | \(\pi+2\) |
| \(a>R\) | unit circular arc \(\{e^{i\theta}:|\theta|\le\arcsin(R/a)\}\) | \(0\) | \(4\arcsin(R/a)\) |

Here the critical half-disk is \(\{z:|z|\le1,\ \operatorname{Re}z\ge0\}\). The boundary-length limit in the arc case counts the double traversal by the smooth, simple, shrinking-area boundaries, not the arc's geometric one-dimensional measure.

The first nonconstant area terms are sharp:
\[
\begin{aligned}
a<R:\quad&A_t=\pi+\pi\left(1-\frac{R^2}{(R^2-a^2)^2}\right)e^{-2t}+O_{a,R}(e^{-4t}),\\
a=R>0:\quad&A_t=\frac\pi2-\frac{\pi}{4a}e^{-t}+O_a(e^{-2t}),\\
a>R:\quad&A_t=\frac{\pi R^2}{(a^2-R^2)^2}e^{-2t}+O_{a,R}(e^{-4t}).
\end{aligned}
\]
The displayed leading coefficient on the interior side can vanish for special radii, but the expansion is still valid. At tangency, the convergence has the anomalously slow \(e^{-t}\) area correction, rather than the generic \(e^{-2t}\) scale.

Moreover, if \(a=R>0\) and the initial boundary is \(z(\theta)=a(1+e^{i\theta})\), then the precise material boundary layer around its origin-touching parameter satisfies, for each \(u\in\mathbb R\), locally uniformly in \(u\),
\[
\lim_{t\to\infty} e^{-it}\Phi_t\!\left(a[1+e^{i(\pi+ue^{-t})}]\right)
=-\frac{i a u}{\sqrt{1+a^2u^2}}.
\]
The right side fills the open diameter as \(u\) varies, and its closure fills the entire diameter.

## Assumptions and scope

The flow acts on the whole complex plane (equivalently \(\mathbb R^2\)); the coefficient of the cubic radial damping and of the constant rotation is normalized to one. The material region is the image of the **filled** Euclidean disk and its boundary is the image of the initial circle. Time \(t\ge0\) is physical time, and \(e^{-it}\) only removes rigid rotation; it preserves area and boundary length. The parameters \(a\ge0\) and \(R>0\) are fixed as \(t\to\infty\). All limits stated for sets use Euclidean Hausdorff distance; all areas are ordinary planar Lebesgue areas; all lengths are ordinary Euclidean arclengths of the finite-time simple closed curves.

## Proof

**Step 1: exact global flow and transport Jacobian.** In polar coordinates the system is \(\dot r=r(1-r^2)\), \(\dot\varphi=1\). Direct separation gives
\[
e^{-it}\Phi_t(z)=F_t(z)=\frac{e^t z}{\sqrt{1+(e^{2t}-1)|z|^2}}.
\]
Writing \(k=e^t\) and \(s=k^2-1\), its radial map \(f_t(r)=kr(1+sr^2)^{-1/2}\) has strictly positive derivative \(f_t'(r)=k(1+sr^2)^{-3/2}\), and its tangential stretch is \(f_t(r)/r=k(1+sr^2)^{-1/2}\). Thus its Jacobian is \(\det DF_t(z)=k^2(1+s|z|^2)^{-2}\), including by continuity at the origin. It is a smooth orientation-preserving embedding for every finite \(t\).

**Step 2: exact area.** Since the map is injective and orientation preserving,
\[
A_t=k^2\int_{D_{a,R}}\frac{dx\,dy}{(1+s|z|^2)^2}.
\]
Using \(\nabla\cdot[z/(1+s|z|^2)]=2/(1+s|z|^2)^2\) and the divergence theorem on the disk boundary \(z=a+Re^{i\theta}\) yields
\[
A_t=\frac{k^2 R}{2}\int_0^{2\pi}
\frac{R+a\cos\theta}{1+s(a^2+R^2+2aR\cos\theta)}\,d\theta.
\]
For \(C=1+s(a^2+R^2)\), \(B=2saR\), the classical elementary integral is \(\int_0^{2\pi}(C+B\cos\theta)^{-1}\,d\theta=2\pi/\sqrt{C^2-B^2}\), valid because \(C>|B|\). Combining it with \(\int B\cos\theta/(C+B\cos\theta)\,d\theta=2\pi-C\int(C+B\cos\theta)^{-1}\,d\theta\) proves the displayed exact formula for \(a>0,t>0\); the cases \(a=0\) and \(t=0\) follow by direct integration or continuous limits.

**Step 3: noncritical geometric and length limits.** If \(a\ne R\), the initial boundary is bounded a strictly positive distance from the origin. The radial factors \(f_t(r)\to1\) and \(f'_t(r)\to0\) uniformly on its radius range, so the images of its boundary converge in \(C^1\) parametrization to its radial projection \(z\mapsto z/|z|\). When \(a<R\), the boundary winds once around the origin and its angular total variation is \(2\pi\). Its disk contains an origin-centered disk of positive radius, hence the images of the filled disks exhaust the closed unit disk in Hausdorff distance; their lengths converge to \(2\pi\). When \(a>R\), its boundary polar angles range between \(-\beta\) and \(\beta\), where \(\beta=\arcsin(R/a)\), and traverse that interval twice. The filled image converges to the same unit circular arc; area tends to zero and boundary length tends to \(4\beta\).

**Step 4: the tangency singularity.** Assume \(a=R>0\). Parameterize its boundary on \(-\pi<\theta<\pi\) by \(z(\theta)=a(1+e^{i\theta})\). Its polar radius and angle are \(r(\theta)=2a\cos(\theta/2)\) and \(\alpha(\theta)=\theta/2\). Let \(\rho_t(\theta)=f_t(r(\theta))\). Away from the endpoints \(\pm\pi\), \(\rho_t\to1\) in \(C^1\), yielding the right semicircle of arclength \(\pi\). Each endpoint has a monotone radial transition from zero to a radius tending to one. For the length integral
\[
L_t=\int_{-\pi}^{\pi}\sqrt{[\rho_t'(\theta)]^2+[\rho_t(\theta)/2]^2}\,d\theta,
\]
use \(\sqrt{u^2+v^2}\le|u|+|v|\) and monotonicity to obtain \(L_t\le\operatorname{Var}_{[-\pi,\pi]}\rho_t+\frac12\int_{-\pi}^{\pi}\rho_t\,d\theta\to2+\pi\). For a lower bound, fix \(\delta>0\), integrate first over \([-\pi+\delta,\pi-\delta]\) to get \(\pi-\delta\), and then use \(\int|\rho_t'|\) on the two remaining endpoint intervals to get \(2\) in the limit; send \(\delta\downarrow0\). Thus \(L_t\to\pi+2\). For each polar direction \(|\alpha|<\pi/2\), the initial filled disk contains the entire radial segment \(0\le r\le2a\cos\alpha\), and its image contains the entire segment from zero to \(f_t(2a\cos\alpha)\to1\). The image lies in the right half-plane and radius at most \(f_t(2a)\to1\), proving Hausdorff convergence to the closed right half-disk. Finally, with \(\theta=\pi+u/k\), the initial point is \(-iau/k+O_{a,u}(k^{-2})\). Applying \(F_t\) and using \(s/k^2\to1\) yields the boundary-layer profile. The expansion is uniform for \(u\) in compact sets.

**Step 5: area rate transitions.** Substitute \(v=e^{-2t}\), so \(s=(1-v)/v\), in the exact area formula. If \(a\ne R\), both square-root factors have nonzero limits at \(v=0\); ordinary Taylor expansion yields the two \(O(v)\) formulae and \(O(v^2)\) remainders. If \(a=R>0\), one square-root factor vanishes at \(v=0\), and expansion in \(\sqrt v=e^{-t}\) yields \(A_t=\pi/2-\pi\sqrt v/(4a)+O(v)\). The Hausdorff/length and area limits are consistent, but neither alone implies the other.

## Verification

The accompanying `verify.py` independently integrates the boundary flux by composite Simpson quadrature and compares it to the closed area formula at sixteen parameter-time pairs; evaluates boundary length in all three regimes; tests the first area-correction terms; tests ten components of the critical boundary-layer profile; and checks sampled radial-stretch/Jacobian identities. The executable yields 78 passing finite consistency assertions using only the Python standard library. These checks do not substitute for the analytic proof of the infinite-time limits or global uniqueness of the flow.

## Relationship to prior work

Beyn, Kavousanakis and Kevrekidis (2026), *The Right Space for Dynamics: Numerics with Diffeomorphism Equivariance*, arXiv:2607.06536v1, use exactly the normalized Hopf vector field in their Section 5.1 and numerically advect the circle of radius \(0.6\) centered at \((0.6,0)\), corresponding to the singular case \(a=R=0.6\). They also discuss a circle centered at \((0.9,0)\) of radius \(0.6\), corresponding to \(a>R\). Their analysis develops coordinate-reparameterized numerical evolution and compares finite-time shape discretizations; the displayed finite-time examples do not state the exact long-time area law, the half-disk/arc classification, the limiting perimeter, or the critical diameter-generating boundary layer proved here. The scalar Hopf radial solution and angular rotation are classical and not asserted as new; the contribution concerns transported **material sets and their boundaries** and the associated three-regime singular limit. General transport-by-flows and radial logistic calculations may yield equivalent consequences; an uncatalogued prior derivation remains a priority risk.

## Limitations

The result assumes the isotropic cubic Hopf normal form and Euclidean disk initial sets with fixed \(a\) and \(R\). It does not claim equivalent shape laws for perturbations of the vector field, noncircular initial sets, nonuniform angular drift, or uniform asymptotics when \(a-R\) varies with time. The theorem gives perimeter convergence but not a full uniform asymptotic expansion for the perimeter at tangency. No claim of independent external validation or exhaustive bibliographic novelty is made.

## References

Beyn, W.-J.; Kavousanakis, M. E.; Kevrekidis, Y. G., *The Right Space for Dynamics: Numerics with Diffeomorphism Equivariance*, arXiv:2607.06536v1, first publicly submitted 7 July 2026, especially Sections 4 and 5.1. https://arxiv.org/html/2607.06536v1 .
