# Exact all-order Gamma-memory bifurcation geometry in a cognitive-map PDE

## Statement

Consider the cognitive-map reaction-diffusion model of Liang, Wang and Zhang at its normalized positive homogeneous equilibrium
\[
u_*=1,\qquad a_*=\theta=\frac{h(1)}{\mu+\beta},
\]
and replace the two temporal kernels treated explicitly there by the full integer-order Gamma family
\[
g_k(t)=\frac{t^k e^{-t/\tau}}{\tau^{k+1}k!},\qquad k=0,1,2,\ldots.
\]
Assume \(f'(1)<0\), \(M:=\mu+\beta>0\), and
\[
\rho:=h'(1)-\beta\theta\ne0.
\]

For every nonzero Neumann Laplacian eigenvalue \(\lambda>0\), define
\[
X=d_1\lambda-f'(1)>0,\qquad
B=d_1\lambda+\tau^{-1}>0,\qquad
C=\frac{d_2\rho\lambda}{\tau^{k+1}}.
\]
Then the complete characteristic polynomial of that spatial mode is
\[
\boxed{P_k(z)=(z+X)(z+M)(z+B)^{k+1}+C.}
\]

This factorization gives the entire imaginary-axis crossing geometry for every integer Gamma order.

Define
\[
\Phi_k(\omega)=
\arctan\frac{\omega}{X}
+\arctan\frac{\omega}{M}
+(k+1)\arctan\frac{\omega}{B},
\]
and
\[
R_k(\omega)=
\sqrt{X^2+\omega^2}\,
\sqrt{M^2+\omega^2}\,
(B^2+\omega^2)^{(k+1)/2}.
\]
For \(\omega>0\), \(\Phi_k\) and \(R_k\) are strictly increasing, with
\[
\Phi_k(0)=0,\qquad
\lim_{\omega\to\infty}\Phi_k(\omega)=\frac{(k+3)\pi}2.
\]

Hence:

1. **Positive-\(C\) crossings.** There is exactly one conjugate imaginary pair for every phase level
   \[
   \Phi_k(\omega)=(2j+1)\pi
   \]
   lying below \((k+3)\pi/2\), and its threshold is
   \[
   C=+R_k(\omega).
   \]
   The number of such thresholds is
   \[
   \boxed{N_+(k)=\left\lceil\frac{k+1}4\right\rceil}.
   \]

2. **Negative-\(C\) oscillatory crossings.** There is exactly one conjugate imaginary pair for every phase level
   \[
   \Phi_k(\omega)=2j\pi,\qquad j\ge1,
   \]
   lying below \((k+3)\pi/2, and its threshold is
   \[
   C=-R_k(\omega).
   \]
   Their number is
   \[
   \boxed{N_-(k)=\left\lfloor\frac{k+2}4\right\rfloor}.
   \]

3. **Stationary crossing.** There is exactly one zero-eigenvalue threshold,
   \[
   \boxed{C_S=-XMB^{k+1}}.
   \]

4. **Transversality.** Every nonzero imaginary crossing above is simple and transversal.

5. **Exact primary modal stability interval.** Starting from \(C=0\), where every root is in the open left half-plane, the first loss of stability on the negative side is always the stationary crossing \(C_S\), while the first loss on the positive side is the \(j=0\) Hopf crossing. Thus the modal block is Hurwitz exactly for
   \[
   \boxed{-XMB^{k+1}<C<C_{H,+}^{(0)}},
   \]
   where \(C_{H,+}^{(0)}=R_k(\omega_0)\) and \(\Phi_k(\omega_0)=\pi\).

The spatially homogeneous mode \(\lambda=0\) has no such oscillatory crossing: under \(f'(1)<0\) and \(M>0\), its spectrum consists only of the negative kinetic eigenvalues together with the repeated memory eigenvalue \(-1/\tau\). Thus every Hopf crossing described here is spatially inhomogeneous.

For generic parameter values in which only one spatial mode crosses at a time and the standard nonlinear nondegeneracy hypotheses hold, each modal oscillatory crossing gives a Hopf bifurcation of the full PDE. The spectral statements above themselves do not require that additional nonlinear hypothesis.

## Derivation

For an integer Gamma order \(k\), introduce \(k+1\) memory stages \(v_0,\ldots,v_k\), with \(v_0\) the field entering the advective flux:
\[
\begin{aligned}
u_t&=d_1\Delta u+d_2\nabla\!\cdot(u\nabla v_0)+f(u),\\
(v_j)_t&=d_1\Delta v_j+\tau^{-1}(v_{j+1}-v_j),
&&0\le j<k,\\
(v_k)_t&=d_1\Delta v_k+\tau^{-1}(a-v_k),\\
a_t&=h(u)-(\mu+\beta u)a .
\end{aligned}
\]
This is the usual Erlang linear-chain representation, here combined with the heat-semigroup spatial kernel used in the source model. The \(k=0\) and \(k=1\) cases reduce exactly to the weak- and strong-kernel auxiliary systems analyzed in that paper.

On a Neumann mode with \(-\Delta\phi=\lambda\phi\), write the perturbation amplitudes as \(U,V_0,\ldots,V_k,A\). Linearization gives
\[
\dot U=-XU-d_2\lambda V_0,
\]
\[
\dot V_j=-BV_j+\tau^{-1}V_{j+1},\quad
\dot V_k=-BV_k+\tau^{-1}A,
\]
and
\[
\dot A=\rho U-MA.
\]
Eliminating the chain variables, or expanding the determinant of \(zI-J_\lambda\), gives
\[
P_k(z)=(z+X)(z+M)(z+B)^{k+1}+C.
\]

At \(z=i\omega\), the uncoupled product has modulus \(R_k(\omega)\) and phase \(\Phi_k(\omega)\). Since
\[
\Phi_k'(\omega)
=
\frac{X}{X^2+\omega^2}
+\frac{M}{M^2+\omega^2}
+(k+1)\frac{B}{B^2+\omega^2}>0,
\]
each admissible phase level is attained exactly once. If \(C>0\), the product must equal \(-C\), hence its phase is an odd multiple of \(\pi\). If \(C<0\), the product must equal \(-C>0\), hence its nonzero-frequency phase is a positive even multiple of \(\pi\). Counting the admissible phase levels below \((k+3)\pi/2\) yields \(N_+(k)\) and \(N_-(k)\).

For transversality, set
\[
L(z)=\frac1{z+X}+\frac1{z+M}+\frac{k+1}{z+B}.
\]
At an imaginary crossing, \(P_k(i\omega)=0\) implies
\[
\frac{dz}{dC}=\frac1{C\,L(i\omega)}.
\]
Writing \(L(i\omega)=A-iQ\),
\[
A=
\frac{X}{X^2+\omega^2}
+\frac{M}{M^2+\omega^2}
+(k+1)\frac{B}{B^2+\omega^2}>0,
\]
so
\[
\operatorname{Re}\frac{dz}{dC}
=
\frac{A}{C(A^2+Q^2)}\ne0.
\]
Every crossing is therefore simple and transversal. Moreover, as \(|C|\) is increased away from zero, each oscillatory crossing is destabilizing.

The stationary threshold has modulus
\[
|C_S|=XMB^{k+1}=R_k(0).
\]
Every negative-\(C\) oscillatory threshold has \(|C|=R_k(\omega)>R_k(0)\), so it lies strictly beyond the stationary loss of stability. On the positive side, the strictly increasing phase and modulus order the Hopf thresholds by \(j\). This proves the exact primary stability interval.

## New higher-order structure

The two kernel orders treated in the source paper do not display the full phase ladder. The first few counts are
\[
\begin{array}{c|ccccccc}
k&0&1&2&3&4&5&6\\ \hline
N_+(k)&1&1&1&1&2&2&2\\
N_-(k)&0&0&1&1&1&1&2.
\end{array}
\]
Thus \(k=2\) is the first Gamma order with a secondary oscillatory crossing on the same signed side as the stationary threshold, and \(k=4\) is the first with two positive-\(C\) Hopf thresholds. In general
\[
N_+(k)+N_-(k)=\left\lfloor\frac{k+2}2\right\rfloor.
\]
These additional crossings occur only after the corresponding modal equilibrium has already lost stability; they do not change the first-instability interval, but they change the unstable spectral dimension and create additional possibilities for higher-codimension interactions.

## Fixed-mean limit: convergence to a discrete delay

The higher-order formula also gives an explicit bridge from Gamma memory to a fixed discrete delay. Let
\[
r=k+1,\qquad \tau=\frac{T}{r},
\]
so that the Gamma kernel has fixed mean \(T\) while its variance tends to zero. Put
\[
K=d_2\rho\lambda.
\]
After division by \((r/T)^r\), the characteristic equation becomes
\[
(z+X)(z+M)
\left(1+\frac{T}{r}(z+d_1\lambda)\right)^r+K=0.
\]
As \(r\to\infty\), this converges locally uniformly in \(z\) to
\[
\boxed{
(z+X)(z+M)e^{T(z+d_1\lambda)}+K=0,
}
\]
which is the characteristic equation obtained from a discrete temporal delay \(T\) together with spatial heat propagation over that delay.

Consequently, each fixed-index phase threshold converges to the corresponding discrete-delay threshold. The limiting phase law is
\[
\arctan\frac{\omega}{X}
+\arctan\frac{\omega}{M}
+T\omega
=
\begin{cases}
(2j+1)\pi,&K>0,\\
2j\pi,&K<0,
\end{cases}
\]
with limiting threshold magnitude
\[
|K|=
e^{Td_1\lambda}
\sqrt{X^2+\omega^2}\sqrt{M^2+\omega^2}.
\]
The finite phase ladder for every Erlang order therefore converges, branch by branch, to the infinite phase ladder of the discrete-delay problem.

## Relation to prior literature and originality

Liang, Wang and Zhang introduce the Gamma family
\[
g_k(t)=t^k e^{-t/\tau}/(\tau^{k+1}k!)
\]
but their abstract and indexed mathematical summaries describe bifurcation analyses for the weak kernel \(k=0\) and strong kernel \(k=1\). Those two cases lead respectively to cubic and quartic characteristic equations. The result above extends the same cognitive-map PDE to every integer Gamma order and replaces order-by-order Routh-Hurwitz calculations by one exact factorization and a monotone phase law.

The linear-chain trick for Erlang distributions and its convergence toward fixed delays are established techniques; they are not claimed as new. The originality claim is restricted to the source-specific all-order characteristic factorization, exact crossing counts, primary stability interval, transversality formula, and the resulting fixed-mean spectral bridge for this cognitive-map reaction-diffusion model.

Searches by the source title and arXiv identifier, together with combinations of cognitive map, Gamma/Erlang memory, higher-order kernel, reaction-diffusion bifurcation, phase condition, and linear-chain terminology, did not identify a prior source stating these results for this model. To the best of our knowledge, this is new.

## Limitations

- The theorem is a local spectral result at the normalized positive homogeneous equilibrium. It does not establish global nonlinear dynamics.
- Calling a modal imaginary-axis crossing a full PDE Hopf bifurcation additionally requires the usual simple-mode and nonlinear nondegeneracy hypotheses; simultaneous crossings are excluded from that statement.
- The exact source article's abstract and detailed indexed mathematical summaries were inspected, but the full article text was not independently inspected. This leaves a residual originality risk that an unindexed appendix or remark contains a higher-order statement.
- Only integer Gamma orders are covered by the finite chain. Noninteger Gamma shapes require a different representation or approximation.
- The fixed-mean discrete-delay limit is a spectral convergence statement. It is not, by itself, a nonlinear convergence theorem for complete PDE trajectories.

## References

1. J. Liang, X. Wang, G. Zhang, *Bifurcation Analysis of a Reaction-Diffusion System with a Cognitive Map Memory Kernel*, arXiv:2606.02250 (2026). https://arxiv.org/abs/2606.02250
2. P. J. Hurtado, A. S. Kirosingh, *Generalizations of the 'Linear Chain Trick': incorporating more flexible dwell time distributions into mean field ODE models*, Journal of Mathematical Biology 79 (2019), 1831–1883. https://doi.org/10.1007/s00285-019-01412-w
3. M. C. Câmara De Souza, R. G. Plaza, *How fast is the linear chain trick? A rigorous analysis in the context of behavioral epidemiology*, Mathematical Biosciences and Engineering 17 (2020), 6075–6098. https://doi.org/10.3934/mbe.2020273
