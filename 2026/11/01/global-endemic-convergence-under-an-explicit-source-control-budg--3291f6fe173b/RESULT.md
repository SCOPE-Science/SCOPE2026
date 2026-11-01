# Global endemic convergence under an explicit source-control budget

## Finding
Consider the three-dimensional susceptible–infected–adherence system
\[
\begin{aligned}
\dot S&=\mu(1-S)-T(x)SI,\\
\dot I&=T(x)SI-qI,\\
\dot x&=\varepsilon x(1-x)(A(x)I-c),
\end{aligned}\qquad
q=\mu+\gamma,\quad
T(x)=\beta(1-ax)(1-ex),\quad
A(x)=a\xi\beta(1-ex).
\]
Here \(\mu,\gamma,\beta,\xi,c,\varepsilon\) are positive and \(0<a,e<1\). This is the permanent-immunity, no-conformity specialization of the SIRS–behavioral model of Kumata, Ito, and Yamamichi (2026): the immunity-waning and conformity parameters are both zero.

**Theorem.** Assume some \(x_*\in(0,1)\) satisfies
\[
T_*:=T(x_*)>q,\qquad S_*:=\frac{q}{T_*},\qquad I_*:=\frac{\mu}{q}(1-S_*),\qquad c=A(x_*)I_*.
\]
If
\[
\boxed{\quad \frac{e}{\beta(a+e)}>\frac{I_*}{4\mu}=\frac{1-S_*}{4q},\quad}
\]
then \((S_*,I_*,x_*)\) is the unique equilibrium in \(S>0,I>0,S+I<1,0<x<1\), and every solution with initial state in that region converges to it. The conclusion is valid for **every** behavioral speed \(\varepsilon>0\). Consequently, this region contains no nonconstant periodic orbit and no other compact invariant set supporting a complete trajectory. The strict criterion holds on a nonempty open set of parameters.

## Assumptions and scope
The variables \(S,I,R=1-S-I\) are susceptible, infectious, and recovered population fractions; \(x\) is intervention adherence. The state domain is the *strict epidemiological interior* \(\mathcal D=\{S>0,I>0,S+I<1,0<x<1\}\). Recovery is permanent on the modeled time scale; births and deaths balance at rate \(\mu\). We neither assume nor conclude anything about waning immunity, social conformity, epidemic states with initially zero infection, or adherence frozen at a boundary.

The source-control parameter \(e\) modifies both the transmission factor and the private adherence incentive. The theorem's criterion is sufficient for global attraction and is not claimed to be necessary or an optimal parameter boundary. The existence assumption is readily checked from the scalar equation \(c=A(x_*)\mu(1-q/T(x_*))/q\); it is not a hidden numerical fit.

## Proof
**1. Positive invariance and uniqueness.** On the biological closure, \(\dot R=\gamma I-\mu R\); hence the population simplex is invariant. Strictly positive \(I\) and \(x\) remain positive, and \(x<1\) is preserved because of the factors \(I\) and \(x(1-x)\). The susceptible boundary satisfies \(\dot S=\mu>0\), and the recovered boundary satisfies \(\dot R=\gamma I>0\). Smoothness and boundedness on the compact biological closure give global solutions.

Any interior equilibrium must satisfy \(S=q/T(x)\) and \(I=\mu(1-q/T(x))/q\). Since \(T\) and \(A\) strictly decrease with \(x\), the positive product \(A(x)I(x)\) also strictly decreases wherever \(T(x)>q\). Thus \(c=A(x)I(x)\) has at most one interior solution; the assumed \(x_*\) furnishes it.

**2. Exact entropy identity.** Let \(s=S/S_*\), \(i=I/I_*\), and
\[
H= S-S_*-S_*\log(S/S_*)+I-I_*-I_*\log(I/I_*).
\]
Define the behavioral potential
\[
U(x)=-\frac{q}{\varepsilon T_*}\int_{x_*}^x
\frac{T(z)-T_*}{z(1-z)A(z)}\,dz,\qquad V=H+U.
\]
Because \(T\) decreases, \(U\ge0\), with equality only at \(x=x_*\). Each relative entropy is nonnegative and vanishes only at its starred variable. Direct differentiation, using \(T_*S_*=q\) and \(A(x_*)I_*=c\), gives the *exact* identity
\[
\boxed{\dot V=-\mu\frac{(s-1)^2}{s}
-\frac{qI_*}{T_*}(T(x)-T_*)(s-1)
-\frac{qI_*}{T_*}\frac{(T(x)-T_*)(A(x)-A(x_*))}{A(x)}.}
\]
The last summand is nonpositive because \(T\) and \(A\) are decreasing.

**3. Uniform strict dissipation.** On the feasible simplex, \(S\le1\), hence \(1/s=S_*/S\ge S_*\). Set \(d=s-1\), \(z=T(x)-T_*\), \(B=qI_*/T_*>0\). Whenever \(x\ne x_*\),
\[
\frac{A(x)-A(x_*)}{A(x)[T(x)-T_*]}
=\frac{e}{\beta(1-ex)[a+e-ae(x+x_*)]}
\ge\frac{e}{\beta(a+e)}.
\]
The denominator is positive for \(0<a,e<1\) and \(x,x_*\in(0,1)\). It follows that
\[
\begin{aligned}
\dot V&\le -\mu S_*d^2-Bzd-B\frac{e}{\beta(a+e)}z^2\\
&=-\mu S_*\left(d+\frac{Bz}{2\mu S_*}\right)^2
-B\left(\frac{e}{\beta(a+e)}-\frac{I_*}{4\mu}\right)z^2.
\end{aligned}
\]
The same inequality holds continuously at \(x=x_*\), where \(z=0\). The stated strict inequality implies \(\dot V\le0\), with \(\dot V=0\) only if \(S=S_*\) and \(x=x_*\). Along that line, the adherence equation is
\(\dot x=\varepsilon x_*(1-x_*)A(x_*)(I-I_*)\), so the only trajectory that can remain in the zero-dissipation set is the claimed equilibrium.

**4. Global attraction.** As \(S\) or \(I\) tends to zero, the corresponding relative-entropy term diverges. As \(x\downarrow0\) or \(x\uparrow1\), \(U(x)\to+\infty\), because its integrand behaves as a nonzero constant times \(1/x\) or \(1/(1-x)\), respectively. Therefore each finite sublevel set of \(V\) in the closed biological simplex is compact, stays away from all these boundaries, and is positively invariant; approach to the recovered-free face does not obstruct compactness. LaSalle's invariance principle and the zero-dissipation characterization above yield convergence of every strictly interior trajectory. Any compact invariant set consisting of interior complete trajectories must therefore contain only the equilibrium.

**5. Exact nonempty instance.** Take
\[
\mu=\frac15,\quad\gamma=\frac45,\quad\beta=4,\quad
a=\frac3{10},\quad e=\frac9{10},\quad\xi=1,
\quad x_*=\frac3{10},\quad \varepsilon>0.
\]
The requisite values, all obtained by exact arithmetic, are
\[
T_*=\frac{6643}{2500},\quad S_*=\frac{2500}{6643},\quad
I_*=\frac{4143}{33215},\quad A(x_*)=\frac{219}{250},\quad
c=\frac{12429}{113750}.
\]
The damping gap is strictly positive:
\[
\frac{e}{\beta(a+e)}-\frac{I_*}{4\mu}
=\frac{3}{16}-\frac{4143}{26572}
=\frac{3357}{106288}>0.
\]
All hypotheses are strict, so a neighborhood of these parameters (with the corresponding nearby interior equilibrium) also satisfies the theorem.

## Verification
Execute the accompanying standalone \(\texttt{verify.py}\) using Python 3 with SymPy installed. It symbolically reconstructs the exact entropy derivative, verifies the cancellation and source-control quotient, checks the simplex mass balance and equilibrium identities, and recomputes the illustrative rational parameters and strict margin. All listed checks passed. These algebraic checks support the displayed analytical proof; no finite computation is used to infer a global statement.

## Relationship to prior work
Kumata, Ito, and Yamamichi, *Voluntary nonpharmaceutical intervention as a feedback-evolving game* (arXiv:2610.12519v1, October 7, 2026), introduce the private-protection/source-control transmission factor and payoff coupling, analyze boundary and interior equilibria locally, and display numerical behavioral–epidemic regimes; their Supplement S3–S4 uses characteristic-polynomial and Hopf calculations, not a global proper entropy certificate. The theorem here is deliberately confined to their permanent-immunity, zero-conformity specialization and derives a new sufficient *global* criterion uniform in adaptation speed.

Saad-Roy and Traulsen (2023) introduced an earlier behavioral–epidemiological model; their different intervention transmission structure does not state the present source-control condition. Martin, Castella, and Hamelin (2026) study a related *SIS* imitation model of masking. An endemic equilibrium classification or local-stability statement in those systems does not imply global attraction for the present three-dimensional *SIR* system. General epidemic Lyapunov methods are prior art and are not presented as novel; the potential and damping condition are tailored to the specific infection–adherence feedback.

## Limitations
The inequality is only sufficient and may be conservative. The proof does not cover positive immunity waning, social conformity, the boundary faces of state space, \(a=0\), \(e=0\), \(a=1\), or \(e=1\). It excludes nonconstant compact recurrent dynamics *only in the strictly interior feasible region*. It does not show that the original complete SIRS behavioral model is globally stable. The accessible historical search does not exclude a more general theorem elsewhere that implies this result; independent originality review remains necessary.

## References
1. R. Kumata, H. Ito, and M. Yamamichi, *Voluntary nonpharmaceutical intervention as a feedback-evolving game*, arXiv:2610.12519v1 (October 7, 2026). https://arxiv.org/abs/2610.12519 . Full text: https://arxiv.t3mt.com/html/2610.12519v1 .
2. C. M. Saad-Roy and A. Traulsen, *Dynamics in a behavioral–epidemiological model for individual adherence to a nonpharmaceutical intervention*, Proceedings of the National Academy of Sciences **120** (2023), e2311584120. https://doi.org/10.1073/pnas.2311584120 .
3. H. Martin, F. Castella, and F. Hamelin, *Wearing face masks to protect oneself and/or others: Counter-intuitive results from a simple epidemic model accounting for selfish and altruistic human behavior*, Journal of Theoretical Biology **624** (2026), 112395. https://doi.org/10.1016/j.jtbi.2026.112395 .
