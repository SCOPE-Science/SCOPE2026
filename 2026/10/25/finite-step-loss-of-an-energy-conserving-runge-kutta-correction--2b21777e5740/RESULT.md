# Finite-step loss of an energy-conserving Runge–Kutta correction on skew oscillators

## Finding

Consider the fixed-step, two-stage relaxation-free Runge–Kutta (RF-RK) modification of SSPRK(2,2), with the stage-weight perturbation vector \((1,-1)\) prescribed in [1]. For any finite collection of nonzero, uncoupled planar rotations, define the **active** frequencies to be those with positive initial squared norm. The following complete feasibility classification holds in exact arithmetic:

**Theorem.** Let \(m\ge1\), \(h>0\), \(\omega_j>0\), and \(u_{j,0}\in\mathbb R^2\), with at least one \(u_{j,0}\ne0\). Put \(r_j=(h\omega_j)^2\) and \(r_*=\max_{\|u_{j,0}\|>0}r_j\). Starting at this initial condition, there exists a real energy-conserving correction at **every** step of the RF-SSPRK(2,2) iteration if and only if

\[
r_*\le1.
\]

If \(r_*>1\), every possible sequence of real correction roots (including arbitrary switching between the two roots) must terminate after finitely many successfully energy-conserving steps: at the next state the scalar energy equation has **no real root**. This can happen even if the initial correction exists and all completed steps conserve the total quadratic norm exactly.

More precisely, with \(E_{j,n}=\|u_{j,n}\|_2^2\), define

\[
U_n=\sum_j r_jE_{j,n},\qquad V_n=\sum_j r_j^2E_{j,n},\qquad \mu_n=V_n/U_n.
\]

An energy-conserving real correction exists at step \(n\) **exactly when** \(\mu_n\le1\). Whenever it exists, every resulting correction satisfies

\[
E_{j,n+1}=\left[1+b_n^2r_j(r_j-\mu_n)\right]E_{j,n},\qquad b_n\ge\tfrac12.
\]

If \(r_*>1\) and \(E_{*,0}\) denotes the sum of the initial squared norms in the largest-frequency group, then each feasible step multiplies that group's energy by at least \(1+\delta\), where \(\delta=r_*(r_*-1)/4>0\). If \(N\) consecutive steps can be completed, necessarily

\[
N\le\left\lfloor\frac{\log(E_{\mathrm{tot}}/E_{*,0})}{\log(1+\delta)}\right\rfloor,
\quad E_{\mathrm{tot}}=\sum_jE_{j,0}.
\]

For **two active modes** with \(0<a=r_1<1<c=r_2\) and high-frequency share \(p=E_{2,0}/(E_{1,0}+E_{2,0})\), the sharp initial-feasibility frontier is

\[
0<p\le p_*:=\frac{a(1-a)}{a(1-a)+c(c-1)}.
\]

Every such initially feasible state still suffers finite-step failure. In the exact rational example \(h=1\), \(\omega_1=1/2\), \(\omega_2=3/2\), \(E_{1,0}=27\), and \(E_{2,0}=1\), the first near-predictor correction is \(\epsilon_0=-1/6\), and the energies become \((51/2,5/2)\). The next correction equation has discriminant \(-108\), so no second energy-conserving RF-RK step is possible.

## Assumptions and scope

The ODE is the autonomous linear system

\[
\dot u_j=\omega_jJu_j,\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad j=1,\dots,m.
\]

Its exact flow preserves every squared norm \(E_j=\|u_j\|_2^2\), and hence their sum. Only the **sum** is imposed as a numerical invariant. The SSPRK(2,2) stages are \(f_1=Ku_n\) and \(f_2=K(u_n+hf_1)\), where \(K\) is block diagonal with blocks \(\omega_jJ\). The modified update is

\[
u_{n+1}=u_n+h\big[(\tfrac12+\epsilon_n)f_1+(\tfrac12-\epsilon_n)f_2\big].
\]

Here \(\epsilon_n\in\mathbb R\) must make \(\sum_j\|u_{j,n+1}\|^2=\sum_j\|u_{j,n}\|^2\). The near-predictor root is the one approaching \(\epsilon_n=0\) as \(h\to0\) for fixed data; the theorem in fact covers either real root. The method does not involve adaptive base step sizes, roundoff, or an additional projection. Zero modes stay zero; only initially active modes enter \(r_*\).

## Proof

**1. Exact scalar energy equation.** Set \(b=1/2-\epsilon\). Because \(J^2=-I\), one RF-RK update acts on mode \(j\) as

\[
u_j^+=(1-br_j)u_j+h\omega_jJu_j.
\]

The two summands are orthogonal, so the exact squared-norm multiplier is

\[
g(r_j,b)=\frac{\|u_j^+\|^2}{\|u_j\|^2}=(1-br_j)^2+r_j.
\]

Writing \(U=\sum_jr_jE_j>0\) and \(V=\sum_jr_j^2E_j>0\), conservation of the sum of squared norms is equivalent to

\[
Vb^2-2Ub+U=0.
\]

Its discriminant is \(4U(U-V)\). Thus a real correction exists exactly when \(\mu=V/U\le1\). For \(\mu\in(0,1]\), the two roots are

\[
b_{\mathrm{near}}=\frac1{1+\sqrt{1-\mu}},\qquad
b_{\mathrm{far}}=\frac1{1-\sqrt{1-\mu}},
\]

which coincide at \(\mu=1\). Both satisfy \(b\ge1/2\). In particular the near root corresponds to \(\epsilon=1/2-b_{\mathrm{near}}\), the correction used for the consistent branch in [1].

**2. Exact modal transfer.** Dividing the conservation equation by \(U\) gives \(1-2b=-b^2\mu\). Consequently

\[
g(r_j,b)-1=r_j(1-2b)+b^2r_j^2=b^2r_j(r_j-\mu).
\]

All \(g(r_j,b)=(1-br_j)^2+r_j>0\), so the set of active modes is unchanged whenever a real correction is performed. Moreover the total energy remains equal to the finite constant \(E_{\mathrm{tot}}\).

**3. Sufficient condition for indefinite solvability.** Since \(\mu\) is the weighted average of the active \(r_j\) with strictly positive weights \(r_jE_j\), one always has \(\mu\le r_*\). If \(r_*\le1\), the real-root condition holds at every subsequent state for every choice of real root. Thus arbitrarily many energy-conserving updates are possible.

**4. Necessary condition and finite termination.** Suppose \(r_*>1\). If no root exists initially, termination is immediate. Otherwise, at each feasible step \(\mu\le1\). For every mode with \(r_j=r_*\), step 2 and \(b\ge1/2\) imply

\[
g(r_*,b)\ge1+\tfrac14r_*(r_*-1)=1+\delta>1.
\]

Let \(E_{*,n}\) be the total squared norm in this maximal-frequency group. After \(N\) successive feasible updates it obeys \(E_{*,N}\ge(1+\delta)^NE_{*,0}\). But \(E_{*,N}\le E_{\mathrm{tot}}\) because all modal energies are nonnegative and their sum is conserved. The displayed bound on \(N\) follows. Consequently no infinite sequence of real roots exists, irrespective of which branch is selected. This proves the if-and-only-if claim.

**5. Sharp two-mode frontier.** For \(r_1=a\in(0,1)\), \(r_2=c>1\), and high-frequency share \(p\), the inequality \(V\le U\) becomes

\[
(1-p)a(a-1)+pc(c-1)\le0.
\]

Solving for \(p\) gives exactly \(p\le p_*\); equality yields a repeated real root. When \(p>p_*\), no real root exists; when \(0<p\le p_*\), the first root exists but the finite-termination theorem applies. This is an exact boundary, not a sufficient-only estimate.

**6. Exact one-step breakdown witness.** Take \(r_1=1/4\), \(r_2=9/4\), \((E_{1,0},E_{2,0})=(27,1)\). Then \(U_0=9\), \(V_0=27/4\), and \(\mu_0=3/4\); the near root is \(b_0=2/3\), or \(\epsilon_0=-1/6\). The squared-norm multipliers are \(g(1/4,2/3)=17/18\) and \(g(9/4,2/3)=5/2\). Therefore the next state has energies \((51/2,5/2)\), still summing to \(28\). Here \(U_1=12\) and \(V_1=57/4\), giving discriminant

\[
4U_1(U_1-V_1)=4(12)(12-57/4)=-108<0.
\]

The second correction does not exist over the reals, completing the proof.

## Verification

The accompanying standalone Python 3 program `verify.py` uses exact rational arithmetic to verify the source-stage specialization, both modal multipliers, the conservation of \(28\), the sharp share threshold \(p_*=1/16\), and the negative second-step discriminant. It additionally checks modal transfer and total-energy identities on a rational lattice, then independently tests the near-root conservation identity on 20,000 seeded random finite-mode examples. Run using `python verify.py`; the expected final output begins `VERIFY_OK`. These tests are consistency checks; the quantifiers over arbitrary finite mode counts, positive frequencies, and all step numbers are proven in the preceding argument.

## Relationship to prior work

Najafian and Vermeire [1, §2.3 and §4] introduce the fixed-step relaxation-free RK correction, specify \((1,-1)\) for SSPRK(2,2), and give its quadratic discriminant criterion. They prove local real solvability for sufficiently small steps and note that larger steps can have no real correction. The present result does **not** claim those general facts as new. It establishes a distinct infinite-iteration question: a sharp characterization of which active spectra admit a real correction at **all** steps, a quantitative finite-failure bound otherwise, and an exact two-frequency initial-energy threshold and one-successful-step obstruction. Those conclusions are not consequences of one-step existence alone.

Ketcheson [2] studies the different relaxation RK update that scales the whole increment and reinterprets the attained physical time; it does not impose the fixed-time, zero-sum stage-weight modification used here. Najafian and Vermeire [3] develop a different quasi-orthogonal projection search direction, which may have different feasibility properties. The findings here concern only the particular fixed stage-weight direction in [1], not the broader class of projections.

## Limitations

The theorem applies only to exact-arithmetic SSPRK(2,2) with correction coefficients \((1,-1)\), autonomous finite-dimensional block-diagonal planar rotations, one common real scalar correction, and a constant positive base step. It does not assert breakdown for arbitrary RF-RK stage perturbations, for different time integrators, for rank-changing or adaptive-step solvers, or for independent mode-dependent corrections. The conserved quantity is the Euclidean quadratic norm sum, not necessarily a separately weighted physical Hamiltonian energy. A conditional method could handle a failed discriminant by changing its time step or algorithm; this is outside the theorem. A real root at any one step is not itself evidence of long-term solvability.

## References

[1] M. R. Najafian and B. C. Vermeire, *Energy Conservative Relaxation-Free Runge-Kutta Schemes*, arXiv:2401.14508v1 (first posted 2024-01-25), especially §§2.3, 3.1, and 4; https://arxiv.org/html/2401.14508v1 .

[2] D. I. Ketcheson, *Relaxation Runge–Kutta Methods: Conservation and Stability for Inner-Product Norms*, arXiv:1905.09847 (first posted 2019-05-23), especially §§1.1, 2, and 4.1; https://arxiv.org/abs/1905.09847 .

[3] M. R. Najafian and B. C. Vermeire, *Quasi-Orthogonal Runge-Kutta Projection Methods*, arXiv:2409.18328v1 (first posted 2024-09-26), especially §§1.1 and 2; https://arxiv.org/html/2409.18328v1 .
