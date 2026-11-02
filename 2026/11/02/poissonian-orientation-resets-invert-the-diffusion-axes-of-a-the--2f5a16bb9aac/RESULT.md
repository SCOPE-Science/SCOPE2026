# Poissonian orientation resets invert the diffusion axes of a thermally coupled colloid

## Finding

For a passive planar Brownian colloid whose body-frame translational and rotational thermal noises are coupled, resetting **only its orientation** to zero at independent Poisson times creates an exact drift and a nontrivial centered diffusion tensor. The tensor is given below for *every* symmetric positive-definite body mobility. In the natural subfamily with isotropic translational noise after conditioning on angular noise, its major diffusion axis reverses at one universal reset rate, and its longitudinal diffusion enhancement has a different, exactly optimal reset rate.

Write \(\rho=\lambda/D_r\), where \(\lambda>0\) is the orientation-reset rate and \(D_r>0\) the rotational diffusivity. Let \(\Theta=k_BT>0\), and write the symmetric positive-definite body mobility in blocks as
\[
\mu=\begin{pmatrix}K&h\\h^{\mathsf T}&m\end{pmatrix},\qquad K=K^{\mathsf T}\in\mathbb R^{2\times2},\quad h\in\mathbb R^2,\quad m>0.
\]
Define the positive-definite conditional translational diffusivity, rotational diffusivity, and coupling displacement vector by
\[
E=\Theta(K-hh^{\mathsf T}/m),\quad D_r=\Theta m,\quad a=-Jh/m,\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Put
\[
f_\parallel(\rho)=\frac{\rho(2\rho^2+2\rho+3)}{(\rho+1)^3(\rho+4)},\qquad
f_\perp(\rho)=\frac{\rho}{\rho+4}.
\]
For the continuous spatial position \(X_t\in\mathbb R^2\), with angle reset to zero and position unchanged at each reset, the long-time velocity and effective diffusion tensor exist and equal
\[
\boxed{v=\lim_{t\to\infty}\frac{\mathbb E X_t}{t}=-\frac{D_r\rho}{1+\rho}a,}
\]
\[
\boxed{\begin{aligned}
D_{\rm eff}&=\lim_{t\to\infty}\frac{\operatorname{Cov}(X_t)}{2t}\\
&=\frac{\operatorname{tr}E}{2}I_2+\frac{\rho}{\rho+4}\left(E-\frac{\operatorname{tr}E}{2}I_2\right)\\
&\quad+D_r\left[f_\perp(\rho)|a|^2I_2+\big(f_\parallel(\rho)-f_\perp(\rho)\big)aa^{\mathsf T}\right].
\end{aligned}}
\]
Moreover, \((X_t-vt)/\sqrt t\) converges in distribution to the centered two-dimensional Gaussian with covariance \(2D_{\rm eff}\). These assertions hold for all \(\lambda>0\) and all positive-definite \(\mu\), without any small-coupling approximation.

In particular, choose \(E=D_0I_2\), \(D_0>0\), and \(a=(c,0)\) with \(c\ne0\); these conditions are realized by \(h=(0,mc)\) and \(K=D_0 I_2/\Theta+hh^{\mathsf T}/m\). Then
\[
D_{\rm eff}=\operatorname{diag}\big(D_0+c^2D_r f_\parallel(\rho),\ D_0+c^2D_r f_\perp(\rho)\big).
\]
The longitudinal enhancement is **strictly increasing** on \((0,2)\), **strictly decreasing** on \((2,\infty)\), and reaches its unique maximum \(5c^2D_r/27\) at \(\lambda=2D_r\). The transverse enhancement increases strictly to \(c^2D_r\). The major diffusion axis switches from longitudinal to transverse at the unique positive root
\[
\boxed{\rho_\star^3+\rho_\star^2+\rho_\star-2=0,\qquad \rho_\star=0.810535713766\ldots.}
\]
At this single positive rate the centered diffusion tensor is isotropic even though \(h\ne0\), and at all other positive rates it is anisotropic. The two limiting tensors are
\[
\lim_{\lambda\downarrow0}D_{\rm eff}=\tfrac12\operatorname{tr}(E)I_2,\qquad
\lim_{\lambda\to\infty}D_{\rm eff}=\Theta K.
\]

## Assumptions and scope

The system is force-free and planar, with homogeneous constant body mobility \(\mu\succ0\) and equilibrium noise strength \(\Theta>0\). Orientation is a circle-valued angle and the reference angle is zero. The driving translational and angular Wiener noises are independent after Schur-factor decomposition. Each reset occurs at rate \(\lambda>0\), independently of all noises, instantaneously setting the orientation to zero while **leaving \(X_t\) exactly unchanged**. No spatial reset, finite reset duration, external torque, active propulsion, or interparticle interaction is assumed. Both the starting position and angle can be deterministic; the stated long-time quantities do not depend on the former. The angle is initialized at zero for convenience.

## Proof

**1. Exact stochastic factorization.** In the laboratory frame use \(R_\phi=\big(\begin{smallmatrix}\cos\phi&-\sin\phi\\\sin\phi&\cos\phi\end{smallmatrix}\big)\). Positive definiteness implies \(E\succ0\). A constant orthogonal change of the thermal driving noises yields the equivalent between-reset Stratonovich system
\[
d\phi_t=\sqrt{2D_r}\,dW_t,\qquad
dX_t=\sqrt2 R_{\phi_t}E^{1/2}\,dB_t+R_{\phi_t}(h/m)\circ d\phi_t,
\]
where \(B\) is planar Brownian motion independent of \(W\). The first integral is also Itô because its driver is independent of the angular driver. Since \(Ja=h/m\), the angular integral on any **continuous** excursion starting at \(\phi=0\) is \((R_\phi-I_2)a\). The angular jump at a reset is expressly excluded from this integral because the physical position does not jump.

**2. Independent excursions.** Let \(S\) be an exponential variable of rate \(\lambda\), independent of all Wiener processes, and let \(\phi_s=\sqrt{2D_r}W_s\) until \(S\). The displacement during one full excursion is
\[
Y=(R_{\phi_S}-I_2)a+\sqrt2\int_0^S R_{\phi_s}E^{1/2}\,dB_s.
\]
Successive pairs \((Y,S)\) are i.i.d. with moments of every finite order. Since \(\mathbb E e^{ik\phi_S}=\lambda/(\lambda+k^2D_r)\) for every integer \(k\),
\[
\mathbb E Y=-\frac{a}{1+\rho},\qquad \mathbb ES=\frac1{\lambda},\qquad
v=\frac{\mathbb E Y}{\mathbb ES}=-\frac{D_r\rho}{1+\rho}a.
\]

**3. Regenerative covariance.** With \(Z=Y-vS\), one has \(\mathbb EZ=0\). The renewal-reward central limit theorem gives asymptotic covariance-growth tensor \(\mathbb E[ZZ^{\mathsf T}]/\mathbb ES\). Its use is justified directly: the number of complete excursions is a renewal process with finite exponential moments of lengths, while the unfinished excursion has a uniformly bounded second moment, being bounded in its angular part and having a Gaussian translational contribution over an exponentially distributed age. Thus the incomplete-excursion term vanishes after division by \(\sqrt t\); Cauchy–Schwarz gives the covariance-rate limit as well.

The translational Wiener integral has zero conditional mean given \((W,S)\). Hence it has zero cross-covariance with \((R_{\phi_S}-I_2)a-vS\). Let \(C_1=\rho/(\rho+1)\) and \(C_2=\rho/(\rho+4)\). With \(G=(R_{\phi_S}-I_2)a\), the required angular excursion moments are
\[
\begin{aligned}
\mathbb E[GG^{\mathsf T}]&=\tfrac12(1-C_2)|a|^2I_2+(1+C_2-2C_1)aa^{\mathsf T},\\
\mathbb E[SG]&=\left(\frac{\rho}{D_r(\rho+1)^2}-\frac1{D_r\rho}\right)a,\\
\mathbb E[S^2]&=\frac2{D_r^2\rho^2}.
\end{aligned}
\]
Expanding \(\mathbb E[(G-vS)(G-vS)^{\mathsf T}]\), dividing by \(2\mathbb ES\), and simplifying yields exactly
\[
D_r\big[f_\perp(\rho)|a|^2I_2+(f_\parallel(\rho)-f_\perp(\rho))aa^{\mathsf T}\big].
\]

For the translational component, \(\mathbb E[R_{\phi_s}ER_{\phi_s}^{\mathsf T}]=\tfrac12\operatorname{tr}E\,I_2+e^{-4D_rs}(E-\tfrac12\operatorname{tr}E\,I_2)\). Integration against \(\Pr(S>s)=e^{-\lambda s}\) and division by \(\mathbb ES=1/\lambda\) produces
\[
\frac{\operatorname{tr}E}{2}I_2+\frac{\rho}{\rho+4}\left(E-\frac{\operatorname{tr}E}{2}I_2\right),
\]
completing the full formula and the Gaussian limit.

**4. Exact extremizers and axis inversion.** For \(E=D_0I_2\), \(a=(c,0)\), the formula is diagonal. Differentiation and exact factorization give
\[
\frac{d f_\parallel}{d\rho}=-\frac{(\rho-2)(2\rho^3+4\rho^2-\rho+6)}{(\rho+1)^4(\rho+4)^2},\quad
\frac{d f_\perp}{d\rho}=\frac4{(\rho+4)^2}>0.
\]
The cubic factor in the first derivative is positive for every \(\rho>0\): for \(0<\rho\le1\), \(6-\rho>0\), while for \(\rho\ge1\), \(4\rho^2-\rho>0\). Thus the only critical point of \(f_\parallel\) is its strict global maximum at \(\rho=2\). The signed diffusion eigenvalue gap is
\[
f_\parallel(\rho)-f_\perp(\rho)
=\frac{\rho(2-\rho-\rho^2-\rho^3)}{(\rho+1)^3(\rho+4)}.
\]
The polynomial \(\rho^3+\rho^2+\rho-2\) has positive derivative \(3\rho^2+2\rho+1\), starts negative and tends to infinity; hence it has exactly one positive root and the claimed axis switch. Finally, the two stated tensor limits follow from \(f_\parallel(0)=f_\perp(0)=0\), \(f_\parallel(\infty)=0\), \(f_\perp(\infty)=1\), and \(D_r(|a|^2I_2-aa^{\mathsf T})=\Theta hh^{\mathsf T}/m\).

## Verification

Run `python3 VERIFY.py` using Python 3's standard library. The program independently reconstructs excursion moments from exponential-time harmonic transforms for hundreds of rational rates, checks the generic matrix formula using rational arithmetic, verifies root brackets and extremal identities, and compares with independently simulated full renewal excursions. It also simulates anisotropic Brownian paths directly to test non-diagonal covariances. Numerical simulations are finite tests, not a substitute for the analytical central limit and uniqueness proofs.

## Relationship to prior work

Cleuren and Eichhorn, *Sorting by Resetting* (2026, arXiv:2603.19430), introduce the hydrodynamically coupled colloid and derive mean transport under **periodic** orientation resets. The model and its mean drift mechanism are prior work. Their discussion identifies second-moment transport and random reset protocols as further directions. The present claim concerns the fully centered **Poisson-clock** diffusion tensor and the exact reversal and optimum, not the existence of a sorting drift.

Chaki, Olsen, and Löwen, *Anisotropic Brownian particles under resetting* (2024, arXiv:2406.17550), derive the long-time diffusion tensor for **Poisson orientation resets** in a body-frame model with *independent* rotational and translational noises. In their notation there are three mobilities, with no translation–rotation covariance block. Setting \(h=0\) in our formula recovers their rate-dependent tensor, so that subcase is explicitly not claimed as new. Their model and formulas do not contain the \(aa^{\mathsf T}\) term driving axis inversion. Related anisotropic active-Brownian orientation-resetting results (Ghosh, Mandal, and Chaki, arXiv:2501.05149) involve self-propulsion and a different stochastic coupling mechanism. General renewal methods for hidden-coordinate resets are well established (Olsen and Löwen, arXiv:2401.12685). The precise all-mobility coupling term and its sharp symmetric-Schur phase diagram are the assessed contribution.

## Limitations

The result is mathematical and assumes instantaneous spatially non-displacing orientation resets, a strictly positive-definite *constant* body mobility, Markovian Brownian thermal noise, and no active driving. The isotropic-Schur axis switch requires \(c\ne0\); it is not asserted for arbitrary anisotropic \(E\). At zero reset rate the behavior is a limit, not a statement involving a positive-frequency reset point. The finite numerical checks neither certify the infinite-time asymptotics nor prove publication priority. Work on more general resetting and hidden-coordinate processes may offer a broader formulation; definitive human publication-priority review has not been performed.

## References

1. B. Cleuren and R. Eichhorn, *Sorting by Resetting* (2026), arXiv:2603.19430, first submitted March 19, 2026. https://arxiv.org/abs/2603.19430
2. S. Chaki, K. S. Olsen, and H. Löwen, *Anisotropic Brownian particles under resetting* (2024), arXiv:2406.17550; later *Dynamics of a single anisotropic particle under various resetting protocols*, J. Phys.: Condens. Matter 37, 115101 (2025). https://arxiv.org/abs/2406.17550
3. A. Ghosh, S. Mandal, and S. Chaki, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149 (2025); Phys. Rev. E 113, 014142 (2026). https://arxiv.org/abs/2501.05149
4. K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685 (2024). https://arxiv.org/abs/2401.12685
