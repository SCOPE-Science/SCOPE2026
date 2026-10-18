# An exact supercritical Hopf point in the predator-dependent replicator model

## Finding

For the three-population frequency-dependent predator–prey model of Braga and Wardil, at the exact payoff matrices of Cruz and Neves's 2026 Scenario 8 and predator parameter \(\beta=2\), a strictly positive coexistence equilibrium undergoes a **nondegenerate supercritical Hopf bifurcation** at a uniquely specified local carrying-capacity parameter \(K_*\):

\[
1.6617073473536636108699702548448<K_*<1.6617073473536636108699702548511.
\]

At \(K=K_*\) the characteristic spectrum consists of one negative real eigenvalue and one simple purely imaginary conjugate pair; the conjugate pair crosses from stable to unstable as \(K\) increases. The first Lyapunov coefficient is strictly negative. Consequently, there exists \(\varepsilon>0\) such that for every \(K\in(K_*,K_*+\varepsilon)\), a nonconstant, **locally orbitally asymptotically stable, fully positive periodic solution** bifurcates from the equilibrium. The coexistence equilibrium is locally asymptotically stable for all \(K\in(K_*-\varepsilon,K_*)\) and unstable for all \(K\in(K_*,K_*+\varepsilon)\). The result proves the local Hopf mechanism and its supercritical direction that were proposed from numerical observations in the motivating paper.

## Assumptions and scope

The exact matrices, in the paper's ordering, are

\[
M_R=\begin{pmatrix}16/5&3/4\\3&4/5\end{pmatrix},\qquad
M_P=\begin{pmatrix}1/2&3/5\\7/20&3/10\end{pmatrix},\qquad \beta=2.
\]

Write \(x=A/(A+B)\) for the fraction of type-A prey, \(P=A+B\) for total prey, and \(Y\) for the rescaled predator population. Thus \(A=xP\), \(B=(1-x)P\). The exact differential equations are

\[
\begin{aligned}
\dot x&=x(1-x)\,[D_0(x)-D_1(x)Y],\\
\dot P&=P\,[r(x)-P/K-\delta(x)Y],\\
\dot Y&=2Y\,[\delta(x)P-1],
\end{aligned}
\]

where

\[
\begin{aligned}
D_0(x)&=(5x-1)/20, &D_1(x)&=3(2-x)/20,\\
r(x)&=(5x^2+43x+16)/20,&\delta(x)&=(3-x)(3x+2)/20.
\end{aligned}
\]

The biological interior is \(0<x<1\), \(P>0\), \(Y>0\), and \(K>0\). These are fixed, exact parameters and a local claim in \(K\); no statement is made about arbitrary payoff matrices, distant cycles, or global attractors.

## Proof

**1. Exact coexistence branch.** Solving the interior equilibrium equations gives

\[
Y=m(x)=\frac{5x-1}{3(2-x)},\qquad
P=\frac1{\delta(x)},\qquad
K=\kappa(x)=\frac1{\delta(x)F(x)},
\]

with

\[
F(x)=r(x)-\delta(x)m(x)
=\frac{137x^2-187x-102}{60(x-2)},\qquad
\kappa(x)=\frac{-1200(x-2)}{(x-3)(3x+2)(137x^2-187x-102)}.
\]

For \(x\) in the rational interval \(I\) specified below, exact interval evaluation gives \(0<x<1\), \(m(x)>0\), \(F(x)>0\), \(\delta(x)>0\), \(\kappa(x)>0\), and \(\kappa'(x)<0\). Hence this describes a smooth positive equilibrium branch parametrized by \(K\) near the candidate threshold.

**2. Routh–Hurwitz equality and isolation of the crossing.** Let \(J(x)\) be the Jacobian of the three equations, evaluated at this equilibrium with \(K=\kappa(x)\), and set

\[
\det(\lambda I-J(x))=\lambda^3+a_1(x)\lambda^2+a_2(x)\lambda+a_3(x),
\quad H(x)=a_1(x)a_2(x)-a_3(x).
\]

Direct exact differentiation and polynomial simplification give

\[
H(x)=\frac{Q(x)}{36000(x-3)(x-2)^3(3x+2)},
\]

where the **integer** polynomial is

\[
\begin{aligned}
Q(x)={}&67455x^8-1105515x^7+5246054x^6-9041754x^5\\
&+3370659x^4+3356225x^3-826776x^2+296532x-146880.
\end{aligned}
\]

Set

\[
I=\big(0.338132677197410152848169921736,\ 
0.338132677197410152848169921738\big).
\]

Both endpoints are exact terminating rational decimals. Exact rational evaluation establishes \(Q(\inf I)<0<Q(\sup I)\); outward-rounded interval evaluation gives \(Q'(I)>0\). Thus \(Q\) has **exactly one zero in \(I\)**, denoted \(x_*\), with \(K_*=\kappa(x_*)\). Since the denominator above is positive on \(I\), \(H(x_*)=0\). The same interval arithmetic yields

\[
\begin{aligned}
1.43939&<a_1(x_*)<1.43940,\\
0.0298333&<a_2(x_*)<0.0298334,\\
0.0429417&<a_3(x_*)<0.0429419.
\end{aligned}
\]

The characteristic polynomial therefore factors as \((\lambda+a_1)(\lambda^2+a_2)\) at \(x_*\). Its roots are \(-a_1<0\) and \(\pm i\omega\), where \(\omega=\sqrt{a_2}\in(0.1727232,0.1727234)\).

**3. Transversal crossing and stability sides.** Exact derivative evaluation enclosed over \(I\) establishes

\[
0.71405<H'(x)<0.71407,
\qquad -3.07768<\kappa'(x)<-3.07765.
\]

Implicit differentiation of the characteristic polynomial at its imaginary root gives

\[
\left.\frac{d\operatorname{Re}\lambda}{dK}\right|_{K_*}
=-\frac{(dH/dK)(K_*)}{2\,[a_1(x_*)^2+a_2(x_*)]}>0.
\]

Consequently the conjugate pair crosses transversally from negative to positive real part as \(K\) increases. Routh–Hurwitz, using \(a_1,a_2,a_3>0\), proves local asymptotic stability on the lower-\(K\) side and instability on the higher-\(K\) side in a sufficiently small neighborhood.

**4. Nondegenerate supercritical direction.** Evaluate the Jacobian \(J\), symmetric second derivative tensor \(B\), and symmetric third derivative tensor \(C\) of the **unreduced, exact three-dimensional vector field** at the Hopf equilibrium. Let \(q\) satisfy \(Jq=i\omega q\) with its third coordinate normalized to \(q_3=1\); let \(p\) satisfy \(J^{\mathsf T}p=-i\omega p\), with the Hermitian pairing normalized by \(\langle p,q\rangle=1\). The standard first-Lyapunov-coefficient formula is

\[
\ell_1=\frac{1}{2\omega}\operatorname{Re}\left\langle p,
C(q,q,\overline q)
-2B\big(q,J^{-1}B(q,\overline q)\big)
+B\big(\overline q,(2i\omega I-J)^{-1}B(q,q)\big)
\right\rangle.
\]

The included standalone checker constructs \(J,B,C\) by symbolic differentiation with exact rational payoffs and evaluates every entry, eigenvector, linear solve, and contraction using outward-rounded 90-decimal complex interval arithmetic on \(I\). With the stated normalization it obtains the certified enclosure

\[
-0.545928<\ell_1<-0.545926<0.
\]

The checker additionally verifies that each eigenvector residual interval contains zero, that the Hermitian normalization contains one, and that the underlying polynomial relation is exact. The classical nondegenerate Hopf theorem now gives a small nonconstant periodic branch on the \(K>K_*\) side. Since \(\ell_1<0\), its radial Floquet exponent is negative; the third eigenvalue is also negative. Therefore these periodic orbits are locally orbitally asymptotically stable in the full three-dimensional biological system. Their positivity follows by continuity from the strictly positive equilibrium.

## Verification

Run `python verify_supercritical_hopf.py` after installing the packages listed in `requirements.txt`. No data files, private paths, third-party papers, or external network services are required. The script recomputes the exact symbolic equations, proves the Hurwitz polynomial identity with `sympy`, isolates a single real root by rational endpoint signs and monotonicity, certifies equilibrium positivity and transversal crossing, and bounds the first Lyapunov coefficient using `mpmath.iv` outward-rounded intervals. Its final assertion requires \(\ell_1<0\); a floating-point simulation is not substituted for these analytical and interval checks.

The root bound implies the displayed \(K_*\) interval by applying the strictly decreasing rational function \(\kappa\) to the two rational endpoints. The upper and lower decimal bounds in the finding are deliberately rounded outward.

## Relationship to prior work

Braga and Wardil introduced the frequency-dependent two-prey, one-predator model and established coexistence and persistence conditions; those underlying equations are prior work. Cruz and Neves (arXiv:2607.13281, version publicly posted July 14, 2026) supplied the exact Scenario 8 matrices and in Section 7 **explicitly conjectured**, from numerical eigenvalues and oscillations near \(K\approx1.66\), that the stable cycle emerges through a Hopf bifurcation. Their article did not prove either the crossing or the supercriticality and explicitly described such proofs as future work. The present result certifies that precise local phenomenon, including the critical parameter and Lyapunov sign.

A separate published mathematical result on a determinant-sign stability exchange in the same general model concerns collision with a two-species boundary equilibrium (the earlier Conjecture 6.2). It does not imply a nondegenerate interior Hopf point or the direction of its periodic branch. General Hopf theory is standard and supplies the abstract implication from the independently certified inequalities, but does not itself verify these specific payoffs.

## Limitations

This is a **local**, deterministic, mathematical-model result. It proves existence and orbital stability of small fully positive periodic orbits for sufficiently small positive \(K-K_*\), not that all initial states approach them. It neither certifies the finite-amplitude orbit shown in the source at \(K=1.7\), nor asserts uniqueness of all Hopf points or cycles at distant parameter values. Robustness for perturbations of the payoff matrices follows locally from nondegenerate Hopf theory but is not quantified here. The interval-computation certification relies on the ordinary correctness of the included open-source symbolic and outward-rounding libraries. Independent validation has not been performed.

## References

1. H. M. Cruz and A. G. M. Neves, *Predator-dependent replicator dynamics or a predator-prey model with two prey types and frequency dependence*, arXiv:2607.13281, publicly posted 2026-07-14, especially §3, §4.3, and §7. https://arxiv.org/abs/2607.13281
2. G. A. Braga and M. Wardil, *The predator-dependent replicator dynamics*, Journal of Physics A: Mathematical and Theoretical 55 (2022), 025601. Accessible author manuscript: https://www.researchgate.net/publication/356867039_The_predator-dependent_replicator_dynamics
3. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, Springer, Chapter 5 (standard Hopf normal-form and first Lyapunov coefficient framework).
