# Reentrant Markov positivity and the sharp rate-imbalance threshold for two-stage Radau IIA

## Finding

Let two-stage Radau IIA (the order-three \([1/2]\) Padé approximation of the exponential) advance a two-state continuous-time Markov chain with strictly positive transition rates \(a,b\). Although its endpoint matrix always preserves row sums and strictly contracts deviations from equilibrium, its entrywise positivity can disappear over a bounded nonempty range of step lengths and then return for every sufficiently large step.

Write \(m=\min\{a,b\}/(a+b)\), \(s=h(a+b)\) for \(h\ge0\), and
\[
m_c=\frac{2-\sqrt3}{3},\qquad
\rho_c=5+3\sqrt3.
\]
The exact classification is:

1. If \(m\ge m_c\), **every** step \(h\ge0\) is endpoint-positive. When \(m=m_c\), one diagonal entry vanishes at the unique positive step \(s=3+3\sqrt3\); all other positive steps yield strictly positive entries.
2. If \(0<m<m_c\), define
\[
s_\pm(m)=\frac{1-3m\pm\sqrt{9m^2-12m+1}}{m}.
\]
Both endpoints are strictly positive, \(s_-<s_+\), and entrywise positivity holds **if and only if**
\[
s\in[0,s_-(m)]\cup[s_+(m),\infty).
\]
For \(s_-<s<s_+\), exactly the diagonal associated with the less probable stationary state is negative; every off-diagonal remains positive. Equivalently, all step sizes are endpoint-positive exactly when the rate imbalance satisfies
\[
\frac{\max\{a,b\}}{\min\{a,b\}}\le\rho_c.
\]
At \(m=m_c\) the two roots meet by a square-root transition; as \(m\uparrow m_c\) from below,
\[
s_+(m)-s_-(m)\sim\frac{2\sqrt{6\sqrt3}}{m_c}\sqrt{m_c-m}.
\]
In the nonpositive interval, the endpoint map remains strictly contractive toward equilibrium in the stationary weighted quadratic norm. Moreover **the square of every positive-step endpoint matrix is strictly positive and stochastic**, so two successive equal steps always preserve nonnegative data, even when one step does not.

For an exact witness take \(a=19\), \(b=1\). Then the positive step lengths are precisely
\[
h\in[0,1/5]\cup[3/2,\infty),
\]
while the first diagonal of the update at \(h=1\) is \(-4/243\). At the two distinct boundary steps the **same** stochastic matrix occurs:
\[
T_{1/5}=T_{3/2}=
\begin{pmatrix}0&1\\[1mm]1/19&18/19\end{pmatrix}.
\]

## Assumptions and scope

The generator is the irreducible two-state row generator
\[
Q=\begin{pmatrix}-a&a\\ b&-b\end{pmatrix},\qquad a,b>0.
\]
A row probability \(p\) evolves by \(p'=pQ\). The one-step map \(T_h\) is the rational function obtained from the two-stage Radau IIA Runge–Kutta stability function,
\[
R(z)=\frac{1+z/3}{1-2z/3+z^2/6},\qquad T_h=R(hQ).
\]
Endpoint positivity means all entries of \(T_h\) are nonnegative, which together with \(T_h\mathbf1=\mathbf1\) makes \(T_h\) a stochastic matrix. No claim of nonnegativity of internal stages is made. The step is any real \(h\ge0\), with \(T_0=I\). All quantities refer to exact real arithmetic.

## Proof

**Spectral projector reduction.** Put \(\lambda=a+b\) and
\[
\pi=(b/\lambda,a/\lambda),\qquad \Pi=\mathbf1\pi.
\]
The matrix \(\Pi\) is the rank-one stationary projection, \(\Pi^2=\Pi\), \(Q=-\lambda(I-\Pi)\), and \(Q\mathbf1=0\). The rational denominator has scalar values \(1\) and \(1+2s/3+s^2/6>0\) on the two eigenspaces, so \(T_h\) is well-defined for every \(s\ge0\). Functional calculus yields
\[
T_h=\Pi+r(s)(I-\Pi),\qquad
r(s)=R(-s)=\frac{6-2s}{s^2+4s+6}.
\]
Consequently \(T_h\mathbf1=\mathbf1\). For distinct \(i,j\), \((T_h)_{ij}=\pi_j(1-r(s))>0\) whenever \(h>0\), because
\[
1-r(s)=\frac{s(s+6)}{s^2+4s+6}>0.
\]
The diagonal entries are \(\pi_i+(1-\pi_i)r(s)\), and their smaller value occurs at the smaller stationary mass \(m\) because \(1-r(s)>0\). Multiplying that minimum by the positive denominator gives exactly
\[
(s^2+4s+6)\min_i(T_h)_{ii}
=m s^2+(6m-2)s+6=:F_m(s).
\]
Therefore positivity is equivalent to \(F_m(s)\ge0\).

**Exact threshold and sharpness.** The discriminant of \(F_m\) equals
\[
4(9m^2-12m+1).
\]
For \(0<m\le1/2\) it is positive precisely for \(m<m_c=(2-\sqrt3)/3\), vanishes at \(m=m_c\), and is negative for \(m>m_c\). If \(m<m_c\), the displayed two roots are strictly positive because \(1-3m>0\), the radicand is positive, and the product of the roots is \(6/m>0\). Since \(F_m\) is an upward-opening quadratic, its sign has exactly the asserted disconnected positivity set, with strict negativity between the roots. At equality its repeated root is \(s=(1-3m_c)/m_c=3+3\sqrt3\). Replacing \(m\) by \(1/(1+\rho)\), where \(\rho=\max\{a,b\}/\min\{a,b\}\), gives \(\rho_c=(1-m_c)/m_c=5+3\sqrt3\). Finally
\[
9m^2-12m+1=6\sqrt3(m_c-m)+O((m_c-m)^2),
\]
so subtracting the exact roots proves the stated square-root gap width. All inequalities include their exact boundary cases.

**Stability without positivity.** Direct arithmetic shows for every \(s>0\)
\[
1-r(s)=\frac{s(s+6)}{s^2+4s+6}>0,
\qquad
1+r(s)=\frac{s^2+2s+12}{s^2+4s+6}>0.
\]
Thus \(-1<r(s)<1\), even throughout the nonpositive interval. For any row vector \(v\) with \(v\mathbf1=1\), \(vT_h-\pi=r(s)(v-\pi)\), and hence
\[
\sum_{i=1}^2\frac{((vT_h)_i-\pi_i)^2}{\pi_i}
=r(s)^2\sum_{i=1}^2\frac{(v_i-\pi_i)^2}{\pi_i}.
\]
This identity remains algebraically true even if the intermediate row vector has a negative entry; it is **not** a claim of probabilistic interpretation in that case. Squaring the projector representation gives
\[
T_h^2=\Pi+r(s)^2(I-\Pi).
\]
Since \(0\le r(s)^2<1\), its off-diagonal entries \(\pi_j(1-r(s)^2)\) are positive and its diagonal entries \(\pi_i+(1-\pi_i)r(s)^2\) are positive. It is therefore strictly stochastic for every \(h>0\).

**Witness.** If \(a=19,b=1\), then \(m=1/20\), \(\lambda=20\), and the exact roots are \(s_-=4\), \(s_+=30\). Division by \(\lambda\) yields the claimed two intervals of \(h\). At \(s=20\), \(r(20)=-17/243\), giving the first diagonal \(-4/243\). At \(s=4\) and \(s=30\) the same value \(r=-1/19\) yields the displayed common endpoint matrix. This proves the claimed repeated transition and the strict failure inside the gap.

## Verification

Run `python3 verify.py` with the Python standard library. The reproducible checker independently forms the exact \(2\times2\) rational matrix \(N(hQ)D(hQ)^{-1}\) from the Padé numerator and denominator, and compares it with the spectral-projector formula at 3,360 rational configurations. It also checks exact row sums, the quadratic positivity criterion, the positivity of the squared map, the witness transition matrices and negative diagonal, and critical-parameter identities. All checks passed when run from the attached source file.

The universal quantifiers, discriminant classification, strict contraction, and asymptotic square-root coefficient are established in the analytic proof. The finite checker is a reproducibility check, not an infinite proof.

## Relationship to prior work

Jiao, Sun and Wu (2026) derive energy identities for the entire first-subdiagonal Padé family, including classical unconditional contractivity. The full source's statements on matrix denominators, discrete energy and numerical tests were examined. The present stationary-norm contraction is consistent with that framework, and is **not** claimed independently as a new general contractivity theorem. That source does not give the entrywise nonnegativity classification on two-state Markov generators, its exact rate-ratio threshold or the reentrant positivity gap.

Zappavigna, Colaneri, Kirkland and Shorten (2012) provide early examples of positivity failure of diagonal Padé approximations. Their discussion concerns different diagonal rational functions and does not imply the \([1/2]\) Radau IIA two-state phase boundary. General Runge–Kutta positivity/absolute-monotonicity results by Horváth and others concern worst-case steps over problem classes; a zero or finite uniform radius does not settle the full positivity set of this specific two-state conservative generator.

Three closely related published classifications apply respectively to the \([2/2]\) Padé map on an eight-state birth chain, the \([1/1]\) Crank–Nicolson map on reversible chains, and an SSP-SDIRK midpoint-square map on two- and three-state chains. Their rational maps differ from \(R(z)=(1+z/3)/(1-2z/3+z^2/6)\). In particular, Crank–Nicolson gives one initial positivity interval for unequal-rate two-state chains, while the squared-midpoint map is always positive on two states; neither implies the present disconnected interval.

Itkin and Kazbek's 2026 work on rational maps for Fokker–Planck generators provides related broader eventual-positivity context, but accessible source material did not establish a formula for this precise two-state family. Full theorem-level comparison to that paper remains an originality uncertainty.

## Limitations

The result is exact for the autonomous two-state Markov generator and the **endpoint** of the two-stage Radau IIA step, with shared constant rates and exact arithmetic. It does not classify internal stages, other rational approximants, time-dependent rates, nonlinear systems, floating-point implementation, or all larger Markov generators. The two-step positivity statement refers to repeating the same constant step and generator. It does not assert stochasticity at the intermediate endpoint when \(F_m(s)<0\).

Priority is not independently established: older specialized positivity theory and a related 2026 paper were not fully accessible in this search. Broad general energy-contractivity and eventual-positivity statements are acknowledged as prior context, not treated as novel. Independent mathematical audit and historical-priority review have not been performed.

## References

1. M. Jiao, Z. Sun, K. Wu, “On Energy Laws and Stability of First-Subdiagonal Padé Approximants for Linear Seminegative Problems,” *Journal of Information and Computing Science* 21 (2026), 151–178; first online 2026-06-30. DOI: https://doi.org/10.4208/jics-2026-008 ; arXiv:2608.09239v1, https://arxiv.org/abs/2608.09239.
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra Appl.* 436 (2012), 3425–3442. https://doi.org/10.1016/j.laa.2011.12.021.
3. Z. Horváth, “Positivity of Runge-Kutta and diagonally split Runge-Kutta methods,” *Appl. Numer. Math.* 28 (1998), 309–326. https://doi.org/10.1016/S0168-9274(98)00050-6.
4. Z. Horváth, “On the positivity step size threshold of Runge-Kutta methods,” *Appl. Numer. Math.* 53 (2005), 341–356. https://doi.org/10.1016/j.apnum.2004.08.026.
5. A. Itkin, R. Kazbek, “Diagonal Frog meets ADI: trading matrix exponentials for rational maps in the Fokker–Planck equation,” arXiv:2608.22703 (2026). https://arxiv.org/abs/2608.22703.
6. Published results: “Eight-state barrier for Markov positivity of the [2/2] Padé map,” https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab ; “A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains,” https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a ; “Two-state immunity and three-state sharpness for endpoint positivity of SSP-SDIRK2(2),” https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-two-state-immunity-and-three-state-sharpness-for-endpoint-positi--46bf11cc19c7.
