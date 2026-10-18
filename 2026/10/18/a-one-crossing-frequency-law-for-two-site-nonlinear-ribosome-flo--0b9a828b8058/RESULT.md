# A one-crossing frequency law for two-site nonlinear ribosome flow

## Finding

For any two-site ribosome flow model (RFM) with an increasing smooth nonlinear steric-hindrance law, positive constant mean rates, and **one** rate modulated by a small zero-mean sinusoid of angular frequency \(\omega>0\), the quadratic coefficient of the gain of entrainment (GOE) can change sign **at most once** as frequency varies. More precisely, with the definitions below, it is

\[
Q(\omega)=-\frac{R_C}{2}\,\frac{U+V\omega^2}{(\det B-\omega^2)^2+(\operatorname{tr}B)^2\omega^2},\qquad U=u^{\mathsf T}Hu,\quad V=v^{\mathsf T}Hv.
\]

If \(UV<0\), the one possible crossover lies at the explicit frequency \(\omega_c=\sqrt{-U/V}\), and the sign changes there. If \(UV\geq0\), there is no sign crossover for positive frequencies (including zero coefficients). The sign of the actual GOE agrees with that of \(Q(\omega)\) at every fixed frequency with \(Q(\omega)\ne0\), for all sufficiently small nonzero forcing amplitudes. The theorem does **not** assign a sign at a zero of the quadratic coefficient.

This bound is attained by a fully explicit **real-analytic, strictly increasing** hindrance function and one-site initiation modulation. Let

\[
g(x)=x+\frac{8x-5}{8\pi^2}\sin^2(4\pi x),\qquad h(x)=1-g(x),\qquad 0\leq x\leq1,
\]

and consider

\[
\dot x=\frac43(1+\varepsilon\cos(\omega t))h(x)-16x h(y),\qquad
\dot y=16x h(y)-\frac43y.
\]

The comparison equilibrium is \((x,y)=(1/4,3/4)\), with steady production \(R_C=1\). The unique attracting periodic solution satisfies, for every fixed \(\omega>0\),

\[
\operatorname{GOE}(\varepsilon,\omega)=\varepsilon^2\,\frac{12(9\omega^2-176)}{7(9\omega^2+16)(9\omega^2+784)}+O_\omega(\varepsilon^4).
\]

Hence the actual GOE is negative for \(0<\omega<4\sqrt{11}/3\), and positive for \(\omega>4\sqrt{11}/3\), at all sufficiently small nonzero amplitudes (with an amplitude bound allowed to depend on frequency). The positive quadratic gain has its **unique global frequency maximum** at

\[
\omega_* =\frac43\sqrt{11+12\sqrt5},\qquad
Q(\omega_*)=\frac{3-\sqrt5}{896}.
\]

This is a sharp realization of the universal one-crossing limitation: a fixed mean-rate system and the same single sinusoidal input can switch from an average production loss to an average production gain simply by changing frequency.

## Assumptions and scope

For a general model, let \(g\in C^3([0,1])\) satisfy \(g(0)=0\), \(g(1)=1\), and \(g'(x)>0\) for \(x\in(0,1)\). Set \(h=1-g\), \(z_0=1\), and \(z_3=0\). The state \(z=(z_1,z_2)\in[0,1]^2\) evolves under

\[
\dot z_1=\lambda_0(t)h(z_1)-\lambda_1(t)z_1h(z_2),\quad
\dot z_2=\lambda_1(t)z_1h(z_2)-\lambda_2(t)z_2.
\]

Choose positive constants \(\lambda_0,\lambda_1,\lambda_2\). For a fixed edge \(j\in\{0,1,2\}\), modulate only that rate as \(\lambda_j(t)=\lambda_j(1+\varepsilon\cos\omega t)\), keeping the other rates constant; \(|\varepsilon|<1\), \(\omega>0\). Let \(e=(e_1,e_2)\) denote the unique interior equilibrium under mean rates, and \(R_C=\lambda_2e_2\) its production flux. Let \(\gamma_{\varepsilon,\omega}(t)\) denote the unique attracting periodic state and set

\[
\operatorname{GOE}(\varepsilon,\omega)
=\frac{\lambda_2\omega}{2\pi}\int_0^{2\pi/\omega}\gamma_{\varepsilon,\omega,2}(t)\,dt-R_C.
\]

Write \(E=\operatorname{diag}(e_1,e_2)\), \(J=D_zf(e,\lambda)\), \(B=E^{-1}JE\), and \(v=E^{-1}\lambda_j\partial_{\lambda_j}f(e,\lambda)\), the normalized first-order forcing direction. The stable matrix \(B\) is real \(2\times2\), with \(\operatorname{tr}B<0\) and \(\det B>0\). Define \(u=\operatorname{adj}(-B)v\).

The symmetric \(2\times2\) Jacobi matrix \(H\) is the **previously established** GOE second-variation matrix of Zhou (2026, Theorem 5.3). For completeness, set

\[
\theta_j=\frac{e_j g'(e_j)}{h(e_j)},\quad
\chi_j=1+\theta_j+\frac{e_jg''(e_j)}{2g'(e_j)},\quad
p_0=(1+\theta_1+\theta_1\theta_2)^{-1},\quad
p_1=p_0\theta_1,\quad p_2=p_1\theta_2,
\]

\[
H=\begin{pmatrix}p_1\chi_1&-p_2/2\\-p_2/2&p_2\chi_2\end{pmatrix}.
\]

All frequency statements concern only the leading \(\varepsilon^2\) contribution. At a root of that coefficient, higher orders can determine the sign, and no finite-amplitude uniform-in-frequency statement is made.

## Proof

**1. Frequency rigidity in two dimensions.** The equilibrium is hyperbolically attracting and the first variation \(w=E^{-1}\partial_{\varepsilon}\gamma|_{\varepsilon=0}\) satisfies

\[
\dot w=Bw+v\cos(\omega t),\qquad
w(t)=\operatorname{Re}\left((i\omega I-B)^{-1}v\,e^{i\omega t}\right).
\]

The previously established nonlinear-RFM Jacobi second-variation identity gives

\[
\operatorname{GOE}(\varepsilon,\omega)
=-\varepsilon^2R_C\left\langle w^{\mathsf T}Hw\right\rangle+O_\omega(|\varepsilon|^3).
\]

For **any** real \(2\times2\) matrix, the adjugate identity

\[
\operatorname{adj}(i\omega I-B)=\operatorname{adj}(-B)+i\omega I
\]

implies

\[
(i\omega I-B)^{-1}v=\frac{u+i\omega v}{\det(i\omega I-B)}.
\]

As \(H\) is real symmetric, the cross term in its Hermitian quadratic form cancels. Averaging the square of the real harmonic gives

\[
\left\langle w^{\mathsf T}Hw\right\rangle
=\frac{u^{\mathsf T}Hu+\omega^2v^{\mathsf T}Hv}{2|\det(i\omega I-B)|^2},
\]

and

\[
|\det(i\omega I-B)|^2=(\det B-\omega^2)^2+(\operatorname{tr}B)^2\omega^2>0.
\]

The numerator is affine in the strictly positive variable \(\omega^2\). It has at most one positive zero; its zero is simple exactly when \(UV<0\). This proves the general theorem, including all degenerate cases \(U=0\) and/or \(V=0\).

**2. Admissibility of the example.** Since \(\lvert8x-5\rvert\leq5\), differentiating the explicit function yields

\[
|g'(x)-1|\leq \pi^{-2}+\frac5{2\pi}<\frac19+\frac56=\frac{17}{18}<1.
\]

Therefore \(g'>0\) on the entire unit interval. It has \(g(0)=0\), \(g(1)=1\), and at \(e_1=1/4\), \(e_2=3/4\),

\[
g(e_1)=\frac14,\quad g(e_2)=\frac34,\quad
(g'(e_1),g'(e_2))=(1,1),\quad
(g''(e_1),g''(e_2))=(-12,4).
\]

All three equilibrium edge fluxes equal one under the prescribed rates: \((4/3)(3/4)=16(1/4)(1/4)=(4/3)(3/4)=1\). Thus \(R_C=1\), \(e=(1/4,3/4)\), and direct differentiation gives

\[
B=\begin{pmatrix}-16/3&12\\4/3&-16/3\end{pmatrix},\qquad
v=\begin{pmatrix}4\\0\end{pmatrix},\qquad
H=\begin{pmatrix}-1/42&-3/14\\-3/14&33/14\end{pmatrix},
\]

\[
u=\operatorname{adj}(-B)v=\begin{pmatrix}64/3\\16/3\end{pmatrix},\qquad
u^{\mathsf T}Hu=\frac{1408}{189},\quad
v^{\mathsf T}Hv=-\frac8{21}.
\]

Substitution in the universal formula yields the announced rational function \(Q\). The signs change exactly at \(9\omega^2=176\).

**3. Unique optimal frequency and error parity.** Put \(z=9\omega^2\). Then

\[
Q=\frac{12(z-176)}{7(z+16)(z+784)},\quad
\frac{dQ}{dz}=\frac{12(-z^2+352z+153344)}{7(z+16)^2(z+784)^2}.
\]

The derivative numerator has just one positive root, \(z_*=176+192\sqrt5\). Its sign changes from positive to negative there; \(Q\) is negative at zero and tends to zero through positive values at infinity, proving the claimed unique positive maximum and its exact value.

The example's vector field is real analytic in state and amplitude. The periodic fixed-point equation has invertible derivative \(e^{JT}-I\) at zero amplitude because both eigenvalues of \(J\) are strictly negative. The periodic solution and its mean output therefore depend analytically on \(\varepsilon\). Replacing \(\varepsilon\) by \(-\varepsilon\) merely shifts forcing time by half a period, so the mean output is an **even** analytic function of amplitude. This eliminates every odd power, giving the claimed \(O_\omega(\varepsilon^4)\) remainder. For each fixed frequency away from the transition, the sign of the actual GOE equals the sign of the nonzero quadratic coefficient at sufficiently small amplitude.

## Verification

A standalone Python 3 verifier, `verify.py`, uses exact rational arithmetic to check the equilibrium, linearization, Jacobi matrix, adjugate response, numerator and denominator coefficients, threshold, polynomial derivative and the exact maximizing value through its defining quadratic identity. It verifies sampled frequency signs and performs a strict positivity test for the analytical derivative bound. The proof of the universal one-zero property uses the adjugate identity and is not inferred from numerical samples.

Independent numerical ODE integrations of the actual nonlinear periodically forced model at \(\omega=3,6,8.2,12\) and small amplitudes confirmed the predicted low/high-frequency signs and the response scale. Those computations are corroboration only, not the proof.

## Relationship to prior work

Zhou, arXiv:2610.10602v1 (2026), proves existence and attraction of periodic RFM responses and derives the general Jacobi quadratic-form identity (Theorem 5.3), as well as curvature and chain-length criteria. **Those identities and dynamical existence results are prior work and are explicitly used here**. The present finding concerns a different, input-restricted question: the number of possible changes of **sign as frequency alone varies**, uniformly over all two-site admissible models, with an analytic realization that attains the one-crossing limit and has an exactly optimized frequency. Zhou does not state a frequency-crossing classification or this realization.

Massas and Margaliot, arXiv:2607.25435v1 (2026), establish no positive GOE for classical *linear* hindrance, which does not include the analytic nonlinear example. Their separate arXiv:2606.23149 studies stable **linear state dynamics** with nonlinear static outputs, whereas here the state transport law is nonlinear. The abstract of their arXiv:2608.15214v1 concerns feedforward nonlinear cascades, not the two-site, bidirectionally coupled Jacobian here; its full text was not available during the comparison. An equivalent spectral-crossover lemma in broader control-theory literature remains an originality risk, as this two-dimensional adjugate calculation is elementary even though its transport consequence is specific.

## Limitations

The theorem classifies **second-order weak-forcing signs** for one **single harmonic input on one edge**. It does not classify general multi-harmonic or multi-edge forcing, higher-order terms at the critical frequency, nonperturbative amplitudes, or chains of at least three sites. The response is smooth separately for each fixed positive frequency; no uniform-in-frequency amplitude threshold is asserted. The worked example is an analytically admissible nonlinear steric-hindrance law, not an empirically calibrated biochemical response. Self-review does not constitute independent validation or a priority certificate.

## References

1. H. Zhou, *Gain of Entrainment in Ribosome Flow Models with Nonlinear Steric Hindrance: Global Rigidity and Dimension-Induced Gain*, arXiv:2610.10602v1, first public 2026-10-07, especially Sections 2 and 5, Theorem 5.3. https://arxiv.org/html/2610.10602v1
2. R. Massas and M. Margaliot, *On the Cost of Entrainment in Protein Translation*, arXiv:2607.25435v1, 2026. https://arxiv.org/abs/2607.25435
3. R. Massas and M. Margaliot, *On the gain of entrainment in stable linear control systems with a nonlinear output*, arXiv:2606.23149, 2026. https://arxiv.org/abs/2606.23149
4. R. Massas and M. Margaliot, *Gain of Entrainment in Nonlinear Cascades*, arXiv:2608.15214v1, 2026; abstract consulted. https://arxiv.org/abs/2608.15214
