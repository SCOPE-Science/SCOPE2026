# Sharp spectral energy cascade and finite-step breakdown of relaxation-free SSPRK(2,2)

## Finding
Consider the relaxation-free Runge--Kutta modification of the two-stage, second-order SSPRK method, with the fixed coefficient direction \(k=(1,-1)\), applied to a direct sum of planar linear harmonic oscillators. Whenever the real near-consistent correction exists, the method conserves the *total* squared Euclidean norm exactly. Nevertheless, it has the following exact and global behavior.

Let \(h>0\) be fixed, let \(m\ge1\), and let the angular frequencies \(\omega_i>0\) be fixed. At a nonzero state with modal energies \(E_i=\|z_i\|_2^2\), define \(v_i=(h\omega_i)^2\), \(M_1=\sum_i E_i v_i\), and \(M_2=\sum_i E_i v_i^2\). The published real correction exists **if and only if**
\[
M_2\le M_1.
\]
On this domain, its small-step-consistent branch is explicitly
\[
c=\frac{1}{1+\sqrt{1-M_2/M_1}},\qquad \epsilon=\frac12-c,
\]
and the exact modal-energy update is
\[
E_i^+=E_iF_i,\qquad F_i=(1-cv_i)^2+v_i=1+c^2v_i\left(v_i-\frac{M_2}{M_1}\right).
\]

If every initially excited mode satisfies \(v_i\le1\), a real correction exists at every step. The total energy is constant, yet energy in every frequency strictly below the highest *initially excited* frequency vanishes exponentially; the full conserved energy concentrates in the highest-frequency eigenspace. If there is more than one excited frequency, its energy increases strictly at every step. In particular, numerical total-energy preservation does not imply preservation of the individual exact modal invariants.

If the largest initially excited squared step frequency is \(v_*>1\), then either the real correction is already impossible at the first attempted step, or, after a finite positive number of successful energy-conserving steps, the correction necessarily becomes nonreal. This is forced even though the computed total energy remains exactly constant at all successful steps. For initial energy \(E_*>0\) in the highest-frequency group and total energy \(E_{\rm tot}\), write \(\alpha=v_*(v_*-1)/4\); no more than
\[
\left\lfloor\frac{\log(E_{\rm tot}/E_*)}{\log(1+\alpha)}\right\rfloor
\]
successful steps can precede the failed next-step request when the first step is feasible.

An exact, two-frequency witness has \(h=1\), \(\omega_1=1/2\), \(\omega_2=3/2\), and initial mode energies \(E_1=1\), \(E_2=1/16\). The first real energy correction exists, but the next one is impossible.

## Assumptions and scope
The ODE consists of \(m\) uncoupled real two-dimensional systems
\[
\dot z_i=\omega_i Jz_i,\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad z_i\in\mathbb R^2,
\]
with exact invariant \(\sum_i\|z_i\|_2^2\) and individually conserved modal energies. The fixed step is \(h>0\). The method uses the *published* SSPRK(2,2) tableau \(a_{21}=1\), \(b_1=b_2=1/2\), and output-weight perturbation \(\widehat b_1=1/2+\epsilon\), \(\widehat b_2=1/2-\epsilon\). Stages are evaluated with the original fixed \(h\), and the branch is the source's \((-B^*+\sqrt{(B^*)^2-4A^*C^*})/(2A^*)\) when real. No adaptive time-step change, projection onto an arbitrary direction, nonlinear force, or floating-point rounding is included. Initially zero modes remain zero and are excluded from the active-frequency maximum. Frequencies in the highest active group may coincide.

## Proof
**1. Exact reduction and discriminant.** The two stage derivatives in mode \(i\) are
\[
f_{1,i}=\omega_i Jz_i,\qquad f_{2,i}=\omega_i J(z_i+hf_{1,i})=\omega_i Jz_i-h\omega_i^2z_i.
\]
Writing \(c=1/2-\epsilon\), the modified fixed-step update is
\[
z_i^+=(1-cv_i)z_i+h\omega_iJz_i.
\]
Orthogonality of \(z_i\) and \(Jz_i\) gives \(E_i^+=E_i((1-cv_i)^2+v_i)\). Therefore the exact total-energy increment is \(M_1-2cM_1+c^2M_2\). As \(M_1,M_2>0\), the quadratic has real roots precisely when \(M_2\le M_1\).

For comparison with the actual source equations (2.12), direct substitution of the stage derivatives yields
\[
A^*=M_2/h^2,\qquad B^*=(2M_1-M_2)/h^2,\qquad C^*=M_2/(4h^2).
\]
Its discriminant is \(4M_1(M_1-M_2)/h^4\). Inserting the source's *plus-square-root* root gives exactly \(c=1/(1+\sqrt{1-M_2/M_1})\), the branch with \(c\to1/2\) as all \(h\omega_i\to0\). For every feasible step, \(1/2\le c\le1\), and total energy is unchanged.

**2. Modal comparison.** Set \(z=M_2/M_1\). The equation \(1-2c+c^2z=0\) implies
\[
F_i=1+c^2v_i(v_i-z).
\]
The number \(z\) is a positive \(E_iv_i\)-weighted average of the active \(v_i\), so it lies between the least and greatest active squared step frequencies. If \(v>u>0\) are two active frequencies, their factors obey
\[
F_v-F_u=c^2(v-u)(v+u-z).
\]
In particular, for \(v=v_*\) maximal, \(F_{v_*}-F_u\ge(v_*-u)u/4>0\). Further, if \(v_*\le1\), then \(F_{v_*}=(1-cv_*)^2+v_*\le2\), hence
\[
\frac{F_u}{F_{v_*}}\le1-\frac{u(v_*-u)}8<1.
\]
The same factor applies to all tied top-frequency modes. Consequently, each lower-to-top modal-energy ratio contracts at a uniform geometric rate. Since the total energy is constant, all lower-modal energies tend to zero geometrically and top-group energy tends to the full initial energy. With lower modes present, \(z<v_*\), so \(F_{v_*}>1\): the top group grows strictly at each step. If \(v_*\le1\), feasibility is automatic forever because \(M_2\le v_*M_1\le M_1\).

**3. Forced failure beyond the unit-frequency boundary.** Suppose instead that \(v_*>1\) and a step is feasible. Then \(z\le1\) and \(c\ge1/2\), so
\[
F_{v_*}=1+c^2v_*(v_*-z)\ge1+\frac14v_*(v_*-1)=1+\alpha>1.
\]
Every successful step multiplies top-group energy by at least \(1+\alpha\), yet each successful step also preserves the finite total energy \(E_{\rm tot}\). After more than \(\log(E_{\rm tot}/E_*)/\log(1+\alpha)\) successful updates these two facts contradict each other. Therefore a real correction fails in finitely many attempts, with the stated explicit maximum number of successful updates. The proof covers all finite \(m\), multiplicities, and nonzero active-mode amplitudes; it does not infer impossibility from a finite simulation.

**4. Exact next-step failure.** For the stated example \(v_1=1/4\), \(v_2=9/4\), \(E_1=1\), \(E_2=1/16\), one has
\[
M_1=25/64,\qquad M_2=97/256,\qquad M_1-M_2=3/256>0,
\]
so the first step has \(c=10/(10+\sqrt3)\in(1/2,1)\). The feasibility inequality in the next state is equivalent to \(E_2^+/E_1^+\le1/15\). But since \(F_2\ge v_2=9/4\) and \(F_1\le1+v_1=5/4\),
\[
\frac{E_2^+}{E_1^+}=\frac1{16}\frac{F_2}{F_1}\ge\frac9{80}>\frac1{15}.
\]
Thus the second quadratic has strictly negative discriminant. The strict rational comparison proves the example without reliance on rounded calculations.

## Verification
Run `python3 verify.py` in the same directory. Its deterministic standard-library tests independently reconstruct the published SSPRK(2,2) stage inner products and \(A^*,B^*,C^*\), check the energy-quadratic identity for rational data, verify the exact two-mode witness, and check modal amplification and energy conservation in representative finite runs. These finite computations are independent corroboration; all quantified infinite-time and finite-failure assertions rest on the preceding algebraic proof.

## Relationship to prior work
Najafian and Vermeire (arXiv:2401.14508v1, equations (2.7)--(2.15), section 4) introduced the relaxation-free output-weight modification, its small-step real-solvability result, and numerical examples exhibiting redistribution of energy between Fourier modes. Their reported larger-step failures and modal plots motivate this question. The present finding is not the method, the quadratic correction formula in general form, or the qualitative existence of modal redistribution: it is the sharp oscillator-specific *all-step spectral cascade*, the necessity of *finite-step eventual loss of real solvability* above the modal boundary, and an exact initially-solvable one-step-to-failure witness.

Ketcheson's earlier relaxation Runge--Kutta method (arXiv:1905.09847v1, especially sections 2 and 4.1) scales the complete output direction by a relaxation parameter and interprets the result at a modified time. It likewise exhibits mode redistribution for a fourth-order method, but does not implement the fixed-time two-weight perturbation analyzed here. General invariant-preserving integrator and modal-filtering principles are acknowledged rather than claimed as new.

## Limitations
The conclusions apply exactly to the original two-stage SSPRK tableau with this coefficient direction, finite direct sums of Euclidean harmonic oscillators, one fixed positive step and the stated near-consistent real root. They do **not** apply automatically to fourth-order Runge--Kutta, to other choices of coefficient direction, to nonlinear or dissipative problems, to floating-point implementations, to implicit energy projection, or to general PDE semidiscretizations without orthogonal modal decomposition. The singular case of a zero initial state is excluded. In the strictly subcritical case, the numerical state remains energy bounded but does not converge to the true multimode trajectory in general. This is a mathematical claim subject to independent validation; no independent scientific audit has been carried out.

## References
1. M. R. Najafian and B. C. Vermeire, *Energy Conservative Relaxation-Free Runge-Kutta Schemes*, arXiv:2401.14508v1, first publicly submitted 2024-01-25, especially sections 2.3, 3 and 4.
2. D. I. Ketcheson, *Relaxation Runge-Kutta Methods: Conservation and Stability for Inner-Product Norms*, arXiv:1905.09847v1 (2019), especially sections 2 and 4.1; SIAM Journal on Numerical Analysis 57 (2019), 2850--2870.
3. D. I. Ketcheson, *Highly Efficient Strong Stability-Preserving Runge-Kutta Methods with Low-Storage Implementations*, SIAM Journal on Scientific Computing 30 (2008), 2113--2136 (SSPRK tableau background).
