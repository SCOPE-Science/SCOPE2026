# An isolated spectral pole determines the extreme tail of Poisson-refreshed resetting

## Finding
For Brownian motion with a resetting intensity independently redrawn from an exponential law at Poisson times, the stationary spatial density has an **isolated exponential mode** strictly slower than the remaining spectrum. The exact decay exponent and positive amplitude are determined by a scalar transcendental equation. In the slow-refresh regime the isolated mode has an exponentially small weight, but it determines the mathematically strict far tail. Consequently a length inferred from the stationary mean-square displacement is not, in this model, the strict far-tail length.

Let \(D,b,\mu>0\). Define
\[
 F_b(s)=\int_0^\infty\frac{e^{-\lambda/b}}{b(s+\lambda)}\,d\lambda
       =\frac{e^{s/b}}{b}E_1(s/b),\qquad s>0,
\]
where \(E_1(u)=\int_u^\infty e^{-v}v^{-1}\,dv\). There is a unique \(s_*\in(0,\mu)\) such that \(\mu F_b(s_*)=1\). Put
\[
 a_*=\mu-s_*,\quad \kappa_*=\sqrt{a_*/D},\quad
 B_*=\frac{b s_*}{\mu a_*},\quad C_*=\frac{B_*\kappa_*}{2}.
\]
The unique stationary position density \(p\) satisfies for every real \(x\)
\[
 \boxed{\quad p(x)=C_*e^{-\kappa_*|x|}+R(x),\qquad
 0\le R(x)\le\frac{\sqrt b}{2\sqrt D}e^{-\sqrt{\mu/D}|x|}.\quad}
\]
In particular, since \(0<a_*<\mu\),
\[
 \boxed{\quad p(x)\sim\frac{b s_*}{2\mu\sqrt{D(\mu-s_*)}}
 e^{-\sqrt{(\mu-s_*)/D}|x|},\qquad |x|\to\infty.\quad}
\]

The complementary spectral density is also explicit. For \(q>\mu\), set \(u=(q-\mu)/b\) and
\[
 \rho(q)=\frac{e^{-u}/b}{
  [1+(\mu/b)e^{-u}\operatorname{Ei}(u)]^2+
  [\pi(\mu/b)e^{-u}]^2},
\]
where \(\operatorname{Ei}\) denotes the real principal-value exponential integral. Then \(\rho(q)\ge0\), \(\int_\mu^\infty\rho(q)\,dq=1-B_*\), and
\[
 R(x)=\int_\mu^\infty\frac{\sqrt q}{2\sqrt D}
                 e^{-\sqrt{q/D}|x|}\rho(q)\,dq.
\]
The isolated weight obeys \(0<B_*<1\).

Let \(\gamma_{\mathrm E}\) be Euler's constant. As \(\mu/b\downarrow0\) with \(D,b\) fixed,
\[
 s_*\sim b e^{-\gamma_{\mathrm E}-b/\mu},\quad
 a_*\sim\mu,\quad
 B_*\sim\frac{b^2}{\mu^2}e^{-\gamma_{\mathrm E}-b/\mu},\quad
 C_*\sim\frac{b^2}{2\sqrt D\,\mu^{3/2}}
                     e^{-\gamma_{\mathrm E}-b/\mu}.
\]
Thus the true asymptotic inverse decay length is \(\kappa_*\sim\sqrt{\mu/D}\), but the amplitude of that ultimate exponential is nonperturbatively small.

There is an exact comparison with the mean-square-displacement surrogate:
\[
 \operatorname{Var}(X)=\frac{2D F_b(\mu)}{1-\mu F_b(\mu)},\qquad
 a_{\mathrm{MSD}}:=\frac{2D}{\operatorname{Var}(X)}
           =\frac1{F_b(\mu)}-\mu.
\]
As \(\mu/b\downarrow0\),
\[
 a_{\mathrm{MSD}}\sim\frac b{\log(b/\mu)},\qquad
 \frac{a_{\mathrm{MSD}}}{a_*}\sim
 \frac b{\mu\log(b/\mu)}\longrightarrow\infty.
\]
Therefore, **a small-wave-number or second-moment estimate cannot determine the exact extreme spatial-tail exponent** in this model.

## Assumptions and scope
The environment \((\lambda_t)\) is stationary and independent of Brownian increments. At the jump times of a Poisson process of rate \(\mu\), \(\lambda_t\) is replaced by an independent sample from \(f_b(\lambda)=b^{-1}e^{-\lambda/b}\) for \(\lambda>0\). Between such jumps the rate is constant. Conditional on the entire environmental path, the particle resets to zero at the times of an inhomogeneous Poisson process with hazard \(\lambda_t\). A reset does not alter the environmental rate. Between resets the particle has generator \(D\partial_{xx}\). All parameters are fixed and strictly positive for the spatial-tail limit; the slow-refresh limit is taken separately after identifying the fixed-parameter tail.

## Proof
**1. Reset-free-age representation.** For a stationary environmental history, the probability of no reset in an interval of length \(t\) is
\[
 S(t)=\mathbb E\left[\exp\left(-\int_0^t\lambda_u\,du\right)\right].
\]
Since the Cox reset point process is stationary, the backward age \(A\) from a stationary observation time to the latest reset obeys \(\mathbb P(A>t)=S(t)\). Conditional on \(A=t\), the Brownian displacement has the centered heat kernel \(g_t(x)=(4\pi Dt)^{-1/2}\exp[-x^2/(4Dt)]\). Hence
\[
 p(x)=\int_0^\infty[-S'(t)]g_t(x)\,dt.
\]
There are almost surely resets arbitrarily far in both time directions: the rate process is stationary ergodic with positive mean \(b\), so its accumulated integrated hazard diverges. This also supplies the stationary construction and uniqueness of the position marginal.

**2. Positive self-adjoint representation.** On \(\mathcal H=L^2(f_b(\lambda)\,d\lambda)\), let \(P h=\int h(\lambda)f_b(\lambda)\,d\lambda\), a rank-one orthogonal projection onto constants. Set
\[
 H h=(\lambda+\mu)h-\mu Ph.
\]
The stationary refresh generator is \(\mu(P-I)\); the Feynman--Kac formula gives \(S(t)=\langle1,e^{-tH}1\rangle\). The self-adjoint operator is nonnegative, since
\[
 \langle h,Hh\rangle=\int\lambda|h|^2f_b\,d\lambda
                 +\mu(\|h\|^2-|\langle1,h\rangle|^2).
\]
Its essential spectrum is \([\mu,\infty)\), because \(H\) is a rank-one bounded perturbation of multiplication by \(\lambda+\mu\).

**3. Exactly one isolated eigenvalue.** Define \(M_2(s)=\int(s+\lambda)^{-2}f_b(\lambda)\,d\lambda\). An eigenvector below \(\mu\) must be proportional to \(h_s(\lambda)=(s+\lambda)^{-1}\) and satisfy \(\mu F_b(s)=1\), with eigenvalue \(\mu-s\). The function \(F_b\) decreases strictly from infinity at zero to zero at infinity, and \(\mu F_b(\mu)<1\), so precisely one solution \(s_*\in(0,\mu)\) exists. Its eigenvalue \(a_*\) is positive and simple. The spectral mass of the constant vector at this eigenvalue is
\[
 B_* =\frac{|\langle1,h_{s_*}\rangle|^2}{\|h_{s_*}\|^2}
      =\frac1{\mu^2M_2(s_*)}.
\]
Differentiating \(F_b(s)=e^{s/b}E_1(s/b)/b\) gives
\[
 M_2(s)=\frac1{bs}-\frac{F_b(s)}b.
\]
At \(s=s_*\), this yields \(B_*=bs_*/[\mu(\mu-s_*)]\). The constant vector has a nontrivial projection onto the continuum because the constant function is not an eigenvector of \(H\); therefore \(0<B_*<1\).

**4. Exact positive spectral mixture and tail.** The spectral theorem gives a probability measure \(\sigma\) supported on \(\{a_*\}\cup[\mu,\infty)\) such that
\[
 S(t)=\int_0^\infty e^{-qt}\sigma(dq),\qquad
 \sigma(\{a_*\})=B_*,\qquad
 \int q\,\sigma(dq)=\langle1,H1\rangle=b.
\]
Differentiating and inserting in the heat-kernel mixture is legitimate by positivity. The elementary Laplace integral
\[
 \int_0^\infty q e^{-qt}g_t(x)\,dt
     =\frac12\sqrt{q/D}\,e^{-\sqrt{q/D}|x|}
\]
proves the claimed atom-plus-remainder representation. For the remainder, all rates satisfy \(q\ge\mu\) and Cauchy--Schwarz gives
\[
 \int_{[\mu,\infty)}\sqrt q\,\sigma(dq)
 \le\left(\int q\,\sigma(dq)\right)^{1/2}=\sqrt b.
\]
Thus the displayed uniform remainder bound follows. Since \(a_*<\mu\), dividing the remainder by the isolated exponential and sending \(|x|\to\infty\) proves the strict asymptotic equivalent with positive coefficient.

**5. Explicit continuum.** The scalar resolvent is
\[
 \langle1,(z+H)^{-1}1\rangle
     =\frac{F_b(\mu+z)}{1-\mu F_b(\mu+z)}.
\]
For \(q=\mu+a\), \(a>0\), its upper boundary value involves
\[
 F_b(-a+i0)=-\frac{e^{-a/b}}b\operatorname{Ei}(a/b)
                  -i\pi\frac{e^{-a/b}}b.
\]
Stieltjes inversion yields precisely \(\rho(q)\) above. This explicitly separates the isolated eigenvalue from the continuous spectral band and proves the integral representation of \(R\).

**6. Slow-refresh asymptotics and variance.** As \(s\downarrow0\),
\[
 bF_b(s)=-\log(s/b)-\gamma_{\mathrm E}
            +O((s/b)|\log(s/b)|).
\]
Using \(\mu F_b(s_*)=1\) shows \(s_*\sim b e^{-\gamma_{\mathrm E}-b/\mu}\). Substitution in the exact formulas proves the three remaining isolated-mode asymptotics. The no-reset survival transform at zero is
\[
 \int_0^\infty S(t)\,dt=\frac{F_b(\mu)}{1-\mu F_b(\mu)}.
\]
The stationary Brownian variance is \(2D\mathbb E[A]=2D\int S\), giving its exact formula. The small-\(\mu\) expansion of \(F_b(\mu)\) gives the variance-based asymptotic and the divergent ratio to the true spectral exponent.

## Verification
The independent Python program `verify_tail.py` performs numerical Stieltjes inversion of the spectral measure and compares it with the Fourier transform obtained directly from the stationary renewal formula. For \(b=D=1\) and \(\mu=0.5,1,3\), it checks spectral normalization, the mean-square displacement, and characteristic functions at three nonzero frequencies each, as well as the disappearance of the continuum relative to the isolated mode with increasing distance. It also checks the nonperturbative small-refresh equation at four smaller refresh rates using arbitrary-precision arithmetic. These computations are independent consistency checks, not an infinite-dimensional proof.

## Relationship to prior work
Arutkin and Reuveni, *Diffusion with doubly stochastic resetting*, arXiv:2509.25365v1 (first posted 2025-09-29), introduced exactly this Poisson-refreshed environment and derived the stationary Fourier transform in their equations (23) and (24). Those formulas and their model are prior work. The cited article argues for a far-field exponential length inferred from small-wave-number behavior; the present theorem distinguishes that second-moment surrogate from the strict spatial tail by isolating the pole of its already known exact transform, and determines its exponentially small residue.

Rose, Touchette, Lesanovsky and Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298v2 (2018), describe the spectral shift for **constant**, state-independent resetting rate and the ordinary Brownian exponential stationary law. That result is not an analysis of an independently evolving random Cox intensity. The general spectral theorem, rank-one perturbation principles, and Stieltjes inversion used here are standard tools, not claimed as new.

## Limitations
The spatial asymptotic is pointwise in each fixed \(\mu>0\); it is not uniform as \(\mu\downarrow0\). The limiting coefficient is exponentially small, so the strict far tail can be difficult to resolve in finite samples. The theorem treats exponential refresh-rate draws, independent homogeneous Poisson refreshes, resetting to a fixed origin, and one-dimensional Brownian diffusion. It does not establish the corresponding tail for arbitrary intensity laws, non-Poisson refresh intervals, or spatially heterogeneous resetting. The exact stationary Fourier transform and general rank-one spectral methods predate this deduction. An inaccessible supplementary derivation and other unpublished or unlocated analyses remain originality risks; no claim of independent certification is made.

## References
1. M. Arutkin and S. Reuveni, *Diffusion with doubly stochastic resetting*, arXiv:2509.25365v1, first submitted 2025-09-29; https://arxiv.org/abs/2509.25365 . Equations (11), (23), (24) and discussion of inferred far-tail length.
2. D. C. Rose, H. Touchette, I. Lesanovsky, and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298v2 (2018); https://arxiv.org/html/1806.01298v2 . Constant-rate spectral comparison.
