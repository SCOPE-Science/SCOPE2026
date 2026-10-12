# The infection-free state remains globally stable at the critical threshold in a recruited-immune delay virus model

## Finding

Consider the delayed within-host virus model of Jiang, Wang, and Song,
\[
\begin{aligned}
\dot T(t)&=\lambda-d_1T(t)-\beta T(t)V(t),\\
\dot I(t)&=\beta T(t-\tau)V(t-\tau)e^{-s\tau}-d_2I(t)-pI(t)C(t),\\
\dot V(t)&=r d_2I(t)-d_3V(t)-qA(t)V(t),\\
\dot C(t)&=\lambda_1+\frac{k_1I(t)C(t)}{h_1+C(t)}-d_4C(t),\\
\dot A(t)&=\lambda_2+\frac{k_2A(t)V(t)}{h_2+A(t)}-d_5A(t).
\end{aligned}
\]
Its infection-free equilibrium is
\[
E_0=(T_0,0,0,C_0,A_0),
\]
where
\[
T_0=\frac{\lambda}{d_1},\qquad
C_0=\frac{\lambda_1}{d_4},\qquad
A_0=\frac{\lambda_2}{d_5}.
\]
The source defines
\[
\mathcal R_0
=
\frac{\beta T_0 r d_2e^{-s\tau}}
{(d_2+pC_0)(d_3+qA_0)}.
\]

The source proves global asymptotic stability of \(E_0\) for \(\mathcal R_0<1\). The same Lyapunov functional proves the stronger closed-threshold statement:

\[
\boxed{\mathcal R_0\le1\quad\Longrightarrow\quad E_0\text{ is globally asymptotically stable}.}
\]

The equality case is not hyperbolic. At \(\mathcal R_0=1\), the infected linearization has a simple zero characteristic root. Thus the endpoint is a genuine critical case closed by the nonlinear Lyapunov-LaSalle argument, not by continuity of a strict linear-stability inequality.

## Assumptions and scope

All model parameters are positive, the delay satisfies \(\tau\ge0\), and the initial history is nonnegative and belongs to the same positively invariant bounded state region used in the source. The variables \(T,I,V,C,A\) denote target cells, infected cells, virus, cellular immune response, and antibody response, respectively.

The claim concerns only the infection-free equilibrium and the critical value \(\mathcal R_0=1\). It does not alter the source's supercritical persistence analysis, does not assert global stability of an endemic equilibrium, and does not claim exponential convergence at the nonhyperbolic endpoint.

## Proof

The source constructs a Lyapunov functional \(L_0\) for \(E_0\). After differentiation along solutions, its derivative has the form
\[
\begin{aligned}
\dot L_0={}&d_1T_0\left(2-\frac{T}{T_0}-\frac{T_0}{T}\right)\\
&+\frac{(d_2+pC_0)(d_3+qA_0)e^{s\tau}}{r d_2}(\mathcal R_0-1)V\\
&-\frac{p d_4e^{s\tau}}{k_1}(C-C_0)^2
+\frac{p\lambda_1h_1e^{s\tau}}{k_1}
\left(2-\frac{C_0}{C}-\frac{C}{C_0}\right)\\
&-\frac{(d_2+pC_0)q d_5e^{s\tau}}{r d_2k_2}(A-A_0)^2\\
&+\frac{(d_2+pC_0)q\lambda_2h_2e^{s\tau}}{r d_2k_2}
\left(2-\frac{A_0}{A}-\frac{A}{A_0}\right).
\end{aligned}
\]
For every positive \(x\),
\[
2-x-\frac1x\le0,
\]
with equality only at \(x=1\). Therefore, when \(\mathcal R_0=1\), every term in \(\dot L_0\) is nonpositive and
\[
\dot L_0=0
\]
can hold only if
\[
T=T_0,\qquad C=C_0,\qquad A=A_0.
\]
The variables \(I\) and \(V\) do not have to vanish merely from this algebraic equality, so the invariant-set step is essential.

Suppose a complete trajectory remains in the zero-derivative set. Then \(T(t)\equiv T_0\). Since \(\lambda=d_1T_0\), the target-cell equation becomes
\[
0=\dot T(t)=-\beta T_0V(t).
\]
Positivity of \(\beta\) and \(T_0\) implies
\[
V(t)\equiv0.
\]
Substitution into the virus equation gives
\[
0=\dot V(t)=r d_2I(t),
\]
and hence
\[
I(t)\equiv0.
\]
Thus the largest invariant subset of \(\{\dot L_0=0\}\) is exactly \(E_0\). LaSalle's invariance principle yields global attraction, while the Lyapunov functional gives stability. Hence \(E_0\) is globally asymptotically stable at \(\mathcal R_0=1\). Combined with the source's strict-subthreshold theorem, this gives the closed range \(\mathcal R_0\le1\).

To see why equality is a genuine critical endpoint, set
\[
a=d_2+pC_0,\qquad b=d_3+qA_0.
\]
The infected \((I,V)\) linearization at \(E_0\) is
\[
\dot I(t)=\beta T_0e^{-s\tau}V(t-\tau)-aI(t),
\qquad
\dot V(t)=r d_2I(t)-bV(t).
\]
Its characteristic equation is
\[
F(z)=(z+a)(z+b)-\beta T_0r d_2e^{-s\tau}e^{-z\tau}=0.
\]
At \(\mathcal R_0=1\), the coefficient identity
\[
\beta T_0r d_2e^{-s\tau}=ab
\]
gives
\[
F(0)=0.
\]
Moreover,
\[
F'(0)=a+b+ab\tau>0.
\]
Therefore zero is a simple characteristic root, so the disease-free equilibrium is nonhyperbolic at the endpoint.

## Verification

The bundled `verify.py` checks the reproduction-number coefficient identity, the zero characteristic root, and its positive derivative using exact rational arithmetic after replacing the infection coefficient by the threshold identity \(ab\). It also replays the invariant-set implication from \(T=T_0\) to \(V=0\) and then to \(I=0\) for a strictly positive rational parameter witness.

The checker is not used to infer the infinite-dimensional conclusion. Global asymptotic stability follows analytically from the Lyapunov derivative and LaSalle invariant-set argument above.

## Relationship to prior work

The motivating article states that the global dynamics are determined by the basic reproduction number, but its explicit infection-free theorem is written only for \(\mathcal R_0<1\). Its displayed Lyapunov derivative contains the factor \((\mathcal R_0-1)V\), making the omitted equality case directly testable from the same proof.

Ji and Liu study a different delayed viral-infection model with nonlinear immune response and use Lyapunov functionals and LaSalle's principle to obtain threshold stability results. Elaiw and Raezah likewise develop threshold-based global stability for general delayed virus models. These works establish that closed-threshold questions are mathematically natural, but they do not state or imply the source-specific invariant-set argument above for the recruited cellular-and-antibody model.

Targeted searches by exact title, DOI, critical-threshold terminology, and the phrase \(\mathcal R_0=1\) did not locate a published correction or a prior statement closing Theorem 3.1 at equality.

## Limitations

The theorem does not give an exponential decay rate at \(\mathcal R_0=1\); the simple zero characteristic root rules out treating the endpoint as an ordinary strictly stable linearization.

The result does not reanalyze every supercritical equilibrium or numerical experiment in the source. It only closes the infection-free threshold and leaves the source's \(\mathcal R_0>1\) persistence and endemic-equilibrium analysis outside the claim.

The earliest day-resolved public bibliographic record located for the article is 1 May 2017, while the publisher page lists formal publication on 1 October 2017. The earlier date is used only for source dating and does not affect the mathematics.

## References

1. C. Jiang, K. Wang, L. Song, “Global dynamics of a delay virus model with recruitment and saturation effects of immune responses,” Mathematical Biosciences and Engineering 14 (2017), 1233–1246. DOI: 10.3934/mbe.2017063.
2. Y. Ji, L. Liu, “Global stability of a delayed viral infection model with nonlinear immune response and general incidence rate,” Discrete and Continuous Dynamical Systems - B 21 (2016), 133–149. DOI: 10.3934/dcdsb.2016.21.133.
3. A. M. Elaiw, A. A. Raezah, “Stability of general virus dynamics models with both cellular and viral infections and delays,” Mathematical Methods in the Applied Sciences 40 (2017), 5863–5880. DOI: 10.1002/mma.4436.
