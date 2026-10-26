# Environmental response speed switches the criticality of a logit game–environment Hopf bifurcation

## Finding

For the two-strategy logit game–environment feedback system described below, the Hopf bifurcation at the positive interior equilibrium has the **explicit first Lyapunov coefficient**
\[
\boxed{\ell_1=-\frac{(2+\chi)+(2-\chi)\omega^2}{16q}},\qquad
\chi=\frac{(1-\theta)a}{D},\quad
\omega^2=\varepsilon\beta_h qD\,n_h(1-n_h).
\]
The normalization of \(\ell_1\) is specified below: the linearized canonical coordinates satisfy \(\dot u=-\omega v\), \(\dot v=\omega u\) in original physical time. In particular, \(\chi>-2\). When \(\chi\leq2\), all such Hopf bifurcations are supercritical. When \(\chi>2\), the criticality is supercritical for \(0<\varepsilon<\varepsilon_*\), subcritical for \(\varepsilon>\varepsilon_*\), where
\[
\boxed{\varepsilon_* = \frac{2+\chi}{(\chi-2)\beta_hqD\,n_h(1-n_h)}.}
\]
At equality, \(\ell_1=0\), and no assertion of a nondegenerate Hopf or generalized-Hopf bifurcation is made. Thus varying only the *environmental response speed*, without moving the rationality threshold, can reverse the stability and side of the small cycles. For \(\ell_1<0\), locally attracting small cycles occur for \(\beta>\beta_h\) close enough to the crossing; for \(\ell_1>0\), locally repelling small cycles occur for \(\beta<\beta_h\) close enough to the crossing.

The admissible game \(\theta=1/10\), \((r,s,p,t)=(2,1,31,1)\) has \(\chi=81/20\), \(\beta_h=(22+9\log 10)/21\), and \(\varepsilon_*\approx30.0811031274\). Thus its Hopf bifurcation is supercritical at \(\varepsilon=1\) and subcritical at \(\varepsilon=40\). The exact rational inequalities in the verification program certify both signs, independently of numerical integration.

## Assumptions and scope

Fix \(0<\theta<1\), \(\varepsilon>0\), and strictly positive payoff constants \(r,s,p,t\), with \(r>s\). These correspond to the original payoff differences \(\delta_{RT0}=r\), \(\delta_{SP0}=-s\), \(\delta_{PS1}=p\), and \(\delta_{TR1}=t\). Put
\[
\begin{split}
a&=p-s-r-t,\quad b=r+s,\quad c=s-p,\quad d=-s,\\
D&=r+t+\theta(p-s)>0,\quad m=1+\theta,\\
g(x,n)&=a x n+b x+c n+d,\quad S(z)=\frac{1}{1+e^{-z}}.
\end{split}
\]
The state \((x,n)\) lies in \([0,1]^2\), with \(x\) the fraction choosing cooperation and \(n\) the environmental state. The physical-time dynamics studied here are
\[
\boxed{\dot x=S(\beta g(x,n))-x,\qquad
\dot n=\varepsilon n(1-n)(mx-1),\qquad \beta>0.}
\]
The explicit environmental speed \(\varepsilon\) is the timescale parameter used in the Jacobian and examples of the initiating paper; this theorem concerns the above displayed system with its speed included. Define
\[
\begin{split}
x_*&=1/m,\quad q=x_*(1-x_*)=\theta/m^2,\quad k=1-2x_*,\quad L=\log(1/\theta),\\
n_0&=(r-\theta s)/D,\quad H=a n_0+b=m(rp+st)/D,\\
\beta_{\rm int}&=mL/(r-\theta s),\quad
\beta_h=\frac{1+qa mL/D}{qH},\\
n_h&=n_0-\frac{mL}{\beta_hD}.
\end{split}
\]
All denominators are positive, and \(0<n_h<1\) under these assumptions. The Hopf equilibrium is \((x_*,n_h)\) at \(\beta=\beta_h\), while away from the crossing the interior equilibrium has environmental component \(n_\beta=n_0-mL/(\beta D)\). Stability and cycles asserted here are **local**, within the open state square. The logarithm is natural. The first Lyapunov coefficient is the coefficient of radial cubic drift in the canonical \((u,v)\) coordinates and original time; its *sign* is coordinate-independent.

## Proof

**1. Interior crossing is genuine.** Since the equilibrium condition gives \(S(\beta g(x_*,n_\beta))=x_*\), the logit equilibrium has \(n_\beta=n_0-mL/(\beta D)\). Its Jacobian is
\[
J_\beta=\begin{pmatrix}
q\beta(a n_\beta+b)-1 & q\beta G\\
\varepsilon m n_\beta(1-n_\beta)&0
\end{pmatrix},\qquad G=ax_*+c=-D/m<0.
\]
The trace is \(q\beta H-qamL/D-1\), so it vanishes exactly at \(\beta_h\), with strictly positive slope \(qH>0\). Its determinant is \(-q\beta G\,\varepsilon m n_\beta(1-n_\beta)>0\) for an interior equilibrium. The interior branch starts at \(\beta_{\rm int}\), and at that branch's lower endpoint its trace is \(q\beta_{\rm int}b-1<0\). Indeed,
\[
q\beta_{\rm int}b=\frac{\theta L(r+s)}{m(r-\theta s)}
<\frac{2\theta L}{1-\theta^2}<1.
\]
The first strict inequality uses \(r>s\), the second the elementary logarithm inequality \(2\theta\log(1/\theta)<1-\theta^2\) for \(0<\theta<1\). Therefore \(\beta_h>\beta_{\rm int}\), so \(n_h>0\); also \(n_h<n_0<1\). The pair of eigenvalues at the crossing is \(\pm i\omega\), with \(\omega^2=\varepsilon\beta_hqD n_h(1-n_h)\). The real-part crossing speed is \(qH/2>0\).

**2. Canonical cubic Taylor expansion.** Set
\[
P=\beta_hqG<0,\qquad Q=\varepsilon mn_h(1-n_h)>0,
\qquad\omega=\sqrt{-PQ},
\]
and translate and rescale by \(u=x-x_*\), \(v=-P(n-n_h)/\omega\). At the Hopf point the linearized system is exactly \(\dot u=-\omega v\), \(\dot v=\omega u\). Write \(\tau=-a\omega/G\) and \(h=-\omega/P>0\). The bilinearity of the payoff yields the **exact** sigmoid-argument increment
\[
\beta_h[g(x,n)-g(x_*,n_h)]=(u-\omega v+\tau uv)/q.
\]
The sigmoid derivatives at the equilibrium are \(S^{\prime}=q\), \(S^{\prime\prime}=qk\), and \(S^{(3)}=q(1-6q)\). Therefore, separating the linear rotation, the nonlinear components \(f,g_1\) of the transformed vector field satisfy
\[
\begin{split}
f(u,v)&=\tau uv+\frac{k}{2q}(u-\omega v)^2
+\frac{k\tau}{q}uv(u-\omega v)
+\frac{1-6q}{6q^2}(u-\omega v)^3+O(\|(u,v)\|^4),\\
g_1(u,v)&=\varepsilon m(1-2n_h)uv-\varepsilon m h\,uv^2.
\end{split}
\]
The second transformed equation is polynomial of degree at most three; in particular \((g_1)_{uu}=(g_1)_{vv}=(g_1)_{uuv}=(g_1)_{vvv}=0\) at the origin. Differentiating the first gives
\[
\begin{array}{ll}
f_{uu}=k/q,&f_{uv}=\tau-k\omega/q,\\
f_{vv}=k\omega^2/q,&f_{uuu}=(1-6q)/q^2,\\
f_{uvv}=(1-6q)\omega^2/q^2-2k\tau\omega/q.
\end{array}
\]
All derivatives in this paragraph are evaluated at \((0,0)\).

**3. Evaluate the Hopf coefficient.** The standard planar first-Lyapunov formula for \(\dot u=-\omega v+f(u,v)\), \(\dot v=\omega u+g_1(u,v)\), with \(f,g_1\) starting at degree two, reads
\[
\ell_1=\frac{f_{uuu}+f_{uvv}+(g_1)_{uuv}+(g_1)_{vvv}}{16}
+\frac{f_{uv}(f_{uu}+f_{vv})-(g_1)_{uv}((g_1)_{uu}+(g_1)_{vv})
-f_{uu}(g_1)_{uu}+f_{vv}(g_1)_{vv}}{16\omega}.
\]
Substitution and simplification, using \(k^2=1-4q\), gives
\[
\ell_1=-\frac{(2+\chi)+(2-\chi)\omega^2}{16q},\qquad
\chi=\frac{ka}{G}=\frac{(1-\theta)a}{D}.
\]
The result is an identity in the parameters, not a numerically fitted approximation. The included symbolic checker independently differentiates the displayed cubic expansion and simplifies the formula.

**4. Sign and bifurcation direction.** With \(R=r+t\), \(H_0=p-s\), the relations \(D=R+\theta H_0\) and \(a=H_0-R\) imply
\[
\chi+2=\frac{(1+\theta)(R+H_0)}{D}
=\frac{(1+\theta)(r+t+p-s)}D>0.
\]
If \(\chi\le2\), both terms in the Lyapunov numerator are nonnegative and the first strictly positive. If \(\chi>2\), then \(\ell_1\) vanishes precisely when \(\omega^2=(2+\chi)/(\chi-2)\), equivalently \(\varepsilon=\varepsilon_*\). Because the real-part crossing speed is positive, the nondegenerate planar Hopf theorem gives the claimed attracting-versus-repelling small cycles on their respective parameter sides. The equality case is degenerate and is excluded from both conclusions. A useful restriction is \(\chi<(1-\theta)/\theta\), so subcriticality is impossible when \(\theta\ge1/3\).

**5. Strict exact witness.** At \(\theta=1/10\), \((r,s,p,t)=(2,1,31,1)\), direct substitution gives \(D=6\), \(a=27\), \(\chi=81/20\), \(q=10/121\),
\[
\beta_h=\frac{22+9\log10}{21},\quad
n_h=\frac{209-30\log10}{30(22+9\log10)}.
\]
The threshold for the squared frequency is \((2+\chi)/(\chi-2)=121/41\). An exact rational series for \(\log10\),
\[
\log10=2\sum_{j=0}^{\infty}\frac{(9/11)^{2j+1}}{2j+1},
\]
has a computable positive geometric upper bound on its tail; fifteen terms certify \(23/10<\log10<231/100\). These imply \(108/1000<n_h<110/1000\) and, by rational inequalities, \(K<121/41<40K\), where \(K=\beta_hqD n_h(1-n_h)\). Thus \(\varepsilon=1\) and \(\varepsilon=40\) lie rigorously on opposite sides. This completes the proof.

## Verification

Execute `python verification/verify_hopf_criticality.py` in an environment satisfying `verification/requirements.txt`. The program (i) symbolically reconstructs \(\ell_1\) from the exact cubic Taylor coefficients, (ii) uses exact rational arithmetic and an explicit tail bound to establish the two opposite signs, and (iii) checks local return-map drifts by high-accuracy ODE integration at two perturbation radii for each environmental speed. On execution, all checks pass. The exact symbolic identity and rational inequalities are certificates for their algebraic assertions; ODE calculations are corroborative, not an infinite-system proof.

## Relationship to prior work

Paarporn, *The madness of people: rational learning in feedback-evolving games* (2023), introduces this logit game–environment mechanism, derives its interior equilibrium and Hopf threshold, and explicitly leaves stability conditions via the first Lyapunov coefficient for further work (Section IV-A). Those prior equilibrium and threshold results are not claimed as new. The new content here is the exact coefficient in the environmental-speed parameter, the complete nondegenerate sign boundary, and one rigorous game at which varying only that speed switches the local Hopf criticality.

Gong, Yao, Gao, and Cao (2022) study environmental feedback with **replicator–mutator**, not logit, learning, so their Hopf/cycle results do not imply this sigmoid-based coefficient. Gavin, Cao, and Paarporn (2024) analyze equilibria of static two-strategy logit games, without this feedback-dynamic Hopf coefficient. The classical planar Hopf formula used here is standard mathematical machinery, not itself a novel statement.

## Limitations

The small periodic cycles are local and no global attractor or global cycle uniqueness is claimed. At \(\varepsilon=\varepsilon_*\), the cubic coefficient vanishes but no second Lyapunov coefficient is computed: in particular the result does **not** establish a Bautin or generalized-Hopf point. The environmental-speed convention is explicitly given in the governing ODE. Higher-order nonlinear changes to the feedback law need not obey this boundary. Exhaustive bibliographic originality beyond the inspected relevant literature has not been independently certified.

## References

1. Keith Paarporn, *The madness of people: rational learning in feedback-evolving games*, arXiv:2311.02745v1 (submitted 2023-11-05), https://arxiv.org/html/2311.02745v1, especially Sections III–IV.
2. Lulu Gong, Weijia Yao, Jian Gao, Ming Cao, *Limit Cycles Analysis and Control of Evolutionary Game Dynamics with Environmental Feedback*, arXiv:2205.10734v1 (2022), https://arxiv.org/abs/2205.10734.
3. Rory Gavin, Ming Cao, Keith Paarporn, *An Analysis of Logit Learning with the r-Lambert Function*, arXiv:2409.05044v1 (2024), https://arxiv.org/abs/2409.05044.
