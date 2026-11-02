# Reentrant dominant-spectrum transition in finite-speed simplex flocks

## Finding
Consider the unnormalized finite-speed Cucker–Smale dynamics of Haskovec and Rodriguez Cartabia (2026) in spatial dimension \(d\ge N-1\), \(N\ge2\), with influence \(\psi_p(r)=(1+r)^{-p}\), \(p\ge0\), and propagation speed \(c>0\). At every stationary regular-simplex configuration of side length \(D>0\), its velocity linearization is exponentially stable in all disagreements. Nevertheless, the *dominant disagreement characteristic roots* undergo a sharp real-to-complex transition controlled by
\[
 q(D)=\frac{D}{c(1+D)^p},\qquad q_N=\frac{W_0((N-1)/e)}{N-1}.
\]
They are real when \(q(D)<q_N\), a double real root at equality, and a nonreal conjugate pair when \(q(D)>q_N\). The transition is not an instability or a claim that every perturbation oscillates.

When \(p>1\), put
\[
 c_{N,p}=\frac{(p-1)^{p-1}}{p^p q_N}.
\]
For \(0<c<c_{N,p}\), **exactly two** critical simplex separations \(0<D_-<1/(p-1)<D_+\) exist. The dominant disagreement roots are real for \(D<D_-\) and \(D>D_+\), but complex for \(D_-<D<D_+\). At \(c=c_{N,p}\), there is a single tangential double-root separation; at larger \(c\), there is none. For \(0\le p<1\), there is exactly one transition separation at every speed; for \(p=1\), one exists exactly when \(c<1/q_N\).

For fixed \(p>1\) and \(c>0\), both critical distances exist at all sufficiently large \(N\), and
\[
 D_-\sim c\frac{\log N}{N},\qquad
 D_+\sim\left(\frac{N}{c\log N}\right)^{1/(p-1)}.
\]
In the unattenuated case \(p=0\), with fixed \(N\) and \(D/c=\tau\to\infty\), the dominant spectral decay is qualitatively different for two agents and for three or more agents:
\[
 \operatorname{Re}\lambda_*\sim
 \begin{cases}
 -\pi^2/(2\tau^3),&N=2,\\
 -\log(N-1)/\tau,&N\ge3.
 \end{cases}
\]

## Assumptions and scope
For each \(i=1,\ldots,N\), let \(x_i(t),v_i(t)\in\mathbb R^d\) satisfy
\[
 \dot x_i(t)=v_i(t),\qquad
 \dot v_i(t)=\sum_{j\ne i}\psi_p\!\left(\left|x_j(t-\tau_{ij}(t))-x_i(t)\right|\right)
 \left(v_j(t-\tau_{ij}(t))-v_i(t)\right),
\]
where the nonnegative state-dependent delays are determined by
\[
 c\tau_{ij}(t)=|x_i(t)-x_j(t-\tau_{ij}(t))|.
\]
The sum carries no factor of \(1/(N-1)\), as in the 2026 source. A stationary simplex consists of distinct positions \(\bar x_i\) with \(|\bar x_i-\bar x_j|=D\), and velocities identically zero. Thus its propagation delays all equal \(\tau=D/c\). The subject is the spectrum of the Fréchet linearization at this stationary solution, specifically its disagreement-velocity part; all position directions and the uniform-velocity mode have neutral characteristic roots. None of the conclusions asserts nonlinear global flocking, nonlinear orbital stability, or pointwise oscillation of every perturbation. A regular simplex exists in dimension \(d\ge N-1\).

The notation \(W_0\) designates the principal Lambert function, with its upper-half-plane boundary value on the negative real cut. When its value is nonreal, the conjugate value is also a root and shares its real part. At the negative branch point \(-1/e\) the two principal real Lambert branches coincide.

## Proof
**1. Linearization despite the implicit delay.** At a stationary simplex, the velocity difference in every interaction vanishes identically. First-order changes in the distance-dependent weight therefore multiply a zero base velocity difference. First-order changes of the delay argument in \(v_j(t-\tau_{ij}(t))\) likewise multiply the time derivative of the zero base velocity and contribute nothing. The base delay is \(\tau=D/c\). Consequently, with velocity perturbation \(\eta_i\),
\[
 \dot\eta_i(t)=a\sum_{j\ne i}\eta_j(t-\tau)-(N-1)a\eta_i(t),
 \qquad a=(1+D)^{-p}>0.
\]
The accompanying position perturbation satisfies \(\dot\xi_i=\eta_i\), does not feed back into this linear velocity equation, and contributes neutral positional modes.

**2. Modes and strict spectral damping.** On the uniform-agent subspace the scalar characteristic equation is
\[
 \lambda=(N-1)a(e^{-\lambda\tau}-1).
\]
It has a simple root at zero and no other root with nonnegative real part: if \(\operatorname{Re}\lambda\ge0\), the equality \(|\lambda+(N-1)a|=(N-1)a e^{-\operatorname{Re}\lambda\tau}\) forces \(\lambda=0\). The derivative of its characteristic function at zero equals \(1+(N-1)a\tau>0\).

On the \((N-1)d\)-dimensional disagreement-velocity space, each scalar component satisfies
\[
 \dot w(t)=-(N-1)a\,w(t)-a\,w(t-\tau),
\]
with characteristic function
\[
 F(\lambda)=\lambda+(N-1)a+a e^{-\lambda\tau}.
\]
No disagreement characteristic root has nonnegative real part. Indeed, for such a root, \(|\lambda+(N-1)a|\ge (N-1)a\), whereas the other side has modulus at most \(a\). For \(N>2\) this is impossible; for \(N=2\), equality would force \(\lambda=0\), but \(F(0)=2a>0\).

**3. Exact leading roots.** Set \(q=a\tau\), \(A=(N-1)a\). Solving the characteristic equation yields all roots
\[
 \lambda_k=-A+\tau^{-1}W_k(-q e^{(N-1)q}),\qquad k\in\mathbb Z.
\]
The principal Lambert branch (and its conjugate when on the cut) has the largest real part. For completeness, if \(z=-K<0\), then \(w e^w=-K\) with \(w=x+iy\) and \(y>0\) requires \(\sin y>0\), \(x=-y\cot y\), and \(K=e^x\sqrt{x^2+y^2}\). The principal complex solution has \(0<y<\pi\) and \(x>-1\); all nonprincipal complex solutions have \(y>2\pi\). For any \(y>2\pi\), the function \(x\mapsto e^x\sqrt{x^2+y^2}\) is strictly increasing on \([-1,\infty)\), and at fixed \(x\) it increases with \(y\). Thus no nonprincipal complex solution can have real part as large as the principal one. When \(K\le1/e\), the principal solution is the larger real solution in \([-1,0)\), and the same comparison excludes other complex roots. This proves the leading-root assertion, including equality of the conjugate pair.

A double real characteristic root occurs exactly when the Lambert argument is \(-1/e\); hence
\[
 q e^{(N-1)q}=e^{-1},\qquad q=q_N.
\]
At equality \(\lambda=-A-1/\tau\), \(F(\lambda)=F'(\lambda)=0\), and \(F''(\lambda)=\tau>0\); the multiplicity is exactly two per scalar disagreement component. Below the branch point the dominant roots are distinct real roots, and beyond it they are a conjugate pair.

**4. Geometric phase diagram.** Because \(q(D)=D/[c(1+D)^p]\),
\[
 q'(D)=\frac{1+(1-p)D}{c(1+D)^{p+1}}.
\]
For \(p<1\), this is positive and \(q(D)\to\infty\), giving one crossing. At \(p=1\), the range is \((0,1/c)\), so it crosses \(q_N\) at a finite \(D\) iff \(c<1/q_N\). For \(p>1\), there is a unique maximum at \(D_*=1/(p-1)\), with \(q(D_*)=(p-1)^{p-1}/(c p^p)\); comparison with \(q_N\) gives zero, one tangent, or two crossing distances exactly as claimed. For the generic two-crossing case the strict inequalities define open real–complex–real regimes.

**5. Large-population and remote-separation limits.** Standard asymptotics \(W_0(t)\sim\log t\) imply \(q_N\sim\log N/N\). When \(p>1\) and \(N\to\infty\), the smaller and larger roots of \(D/(1+D)^p=cq_N\) respectively satisfy \(D_-\sim cq_N\) and \(D_+^{1-p}\sim cq_N\), giving the two stated formulas. For \(p=0\) put \(\tau=D/c\), so \(a=1\). If \(N\ge3\), the characteristic equation gives \(e^{-\lambda_*\tau}=-(N-1)-\lambda_*\); choosing the principal conjugate pair yields \(\lambda_*\tau\to-\log(N-1)\pm i\pi\). If \(N=2\), inserting \(\lambda_*=i\pi/\tau-i\pi/\tau^2+(i\pi-\pi^2/2)/\tau^3+O(\tau^{-4})\) into \(F(\lambda_*)=0\) yields \(\operatorname{Re}\lambda_*=-\pi^2/(2\tau^3)+O(\tau^{-4})\). The expansions pertain to the spectral envelope, not a guaranteed asymptotic of every initial history.

## Verification
The accompanying `verify.py` checks the Lambert-branch ordering across selected \(N\) and \(q\), the double-root identity, the two-separation regimes for two positive exponent choices, the large-delay rates, and the asymptotic two-distance formulas at growing agent counts. It uses `mpmath` at 60 decimal digits. All checks completed successfully. These finite evaluations are evidence of arithmetic consistency, not substitutes for the proof of the universal quantifiers.

For reproducibility, run `python verify.py` in a Python installation with `mpmath`. The proof is self-contained apart from standard facts about the principal Lambert function and Taylor asymptotics of exponentials and \(W_0\).

## Relationship to prior work
Haskovec and Rodriguez Cartabia (2026, arXiv:2610.33170) introduce the unnormalized finite-signal-speed equations and study their nonlinear flocking using Doppler-inspired Lyapunov functionals; they do not give the spectral regime diagram for stationary regular-simplex flocks. Haskovec (2021, arXiv:2112.12806) establishes well-posedness, flocking and the mean-field limit of an earlier normalized variant, not the present phase diagram. Haskovec and Markou (2018, arXiv:1810.01084) study the *different* fixed reaction-delay model and its sharp nonoscillatory condition for a scalar negative-feedback equation. Moradian and Kia (2018, arXiv:1812.04030) analyze the general Lambert-\(W\) method and delay-accelerated convergence for systems with purely delayed linear feedback; this is acknowledged as a methodological antecedent. The present results concern a geometric light-cone delay, a mixture of instantaneous and retarded damping, the doubled distance threshold under integrable attenuation, and its population-size scaling. The formulas follow from classical spectral tools once the physical system is linearized, so claims of priority are restricted to the combined model-specific phase classification, not to Lambert-function methods.

## Limitations
The result is a classification of characteristic exponents about resting simplex configurations, not a nonlinear bifurcation of actual periodic solutions. A nonreal leading pair indicates oscillatory *generic linearized asymptotic modes*; specially prepared histories may avoid them, and transient signs need not alternate. At the double-root separations, solutions can contain polynomially weighted exponential terms. The full linearized system retains neutral position and common-velocity modes; it is not exponentially stable as a whole. For \(p>1\), the influence is integrable, and the source's fat-tail global-flocking theorem does not apply. Spatial dimension must satisfy \(d\ge N-1\); the large-\(N\) limit is not at fixed physical dimension. Results should not be extended to differently normalized original variants without rescaling. Historical-priority comparison against all specialized delay-network literature is not exhaustive.

## References
1. J. Haskovec and M. Rodriguez Cartabia, *Flocking with finite communication speed: a Doppler-inspired Lyapunov approach*, arXiv:2610.33170 (first public 2026-10-23), https://arxiv.org/html/2610.33170v1.
2. J. Haskovec, *Cucker-Smale model with finite speed of information propagation: well-posedness, flocking and mean-field limit*, arXiv:2112.12806 (2021), https://arxiv.org/abs/2112.12806.
3. J. Haskovec and I. Markou, *Asymptotic flocking in the Cucker-Smale model with reaction-type delays in the non-oscillatory regime*, arXiv:1810.01084 (2018), https://arxiv.org/abs/1810.01084.
4. H. Moradian and S. S. Kia, *On the Positive Effect of Delay on the Rate of Convergence of a Class of Linear Time-Delayed Systems*, arXiv:1812.04030 (2018), https://arxiv.org/abs/1812.04030.
5. R. M. Corless et al., *On the Lambert W Function*, Adv. Comput. Math. 5 (1996), 329–359, https://doi.org/10.1007/BF02124750.
