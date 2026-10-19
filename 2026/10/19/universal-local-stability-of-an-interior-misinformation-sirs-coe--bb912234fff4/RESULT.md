# Universal local stability of an interior misinformation–SIRS coexistence equilibrium

## Finding

Consider the six-compartment information–epidemic model of Bulai, Sensi and Sottile [1], with strictly positive rate parameters, nondegenerate infection feedback \(0<K<1\), \(b_1>b_2\), and an information-to-epidemic time-scale factor \(\varepsilon>0\). Whenever a strictly interior equilibrium with positive misinformed, skeptical and infected fractions exists, **that equilibrium is unique and locally exponentially stable for every \(\varepsilon>0\)**. In particular, the fully mixed coexistence equilibrium cannot undergo a local Hopf or zero-eigenvalue instability merely by varying the time-scale ratio while it remains interior.

There is also an exact feasibility criterion. Put
\[
 u=\frac{\mu_1}{b_1},\qquad q=1-u,\qquad
 i=\frac{b_1-b_2}{Kb_1},\qquad
 t=\eta+\mu_2,\qquad g=\gamma+\mu_2,
\]
\[
 s=1-i\left(1+\frac{\gamma}{t}\right),\qquad p=\frac{\beta s}{g}.
\]
Under the stipulated \(0<K<1\) and \(b_1>b_2>0\), a strictly interior coexistence equilibrium exists if and only if
\[
 0<u<1,\quad 0<i<\frac{t}{t+\gamma},
 \quad \frac1{1+q}<p<1+q.
\]
In that case its coordinates are
\[
 U_*=u,\quad I_*=i,\quad S_*=s,\quad R_*=\frac{\gamma i}{t},
 \quad M_*=\frac{1+q-p}{1+p},\quad
 Z_*=\frac{p(1+q)-1}{1+p}.
\]
All six coordinates are strictly positive, and the first and last three respectively sum to one. No restriction of the form \(\varepsilon\ll1\) is needed for the mathematical stability assertion.

## Assumptions and scope

The model evolves on the product of the two population simplices \(U+M+Z=1\) and \(S+I+R=1\), with fast time variable and equations
\[
\begin{aligned}
 \dot U&=\mu_1-b_1UM-\frac{b_2}{1-KI}UZ-\mu_1U,\\
 \dot M&=b_1UM-\mu_1M,\\
 \dot Z&=\frac{b_2}{1-KI}UZ-\mu_1Z,\\
 \dot S&=\varepsilon\left(\mu_2-\beta\frac{1+M}{1+Z}SI+\eta R-\mu_2S\right),\\
 \dot I&=\varepsilon\left(\beta\frac{1+M}{1+Z}SI-(\gamma+\mu_2)I\right),\\
 \dot R&=\varepsilon\left(\gamma I-(\eta+\mu_2)R\right).
\end{aligned}
\]
Here \(b_1,b_2,\mu_1,\mu_2,\gamma,\eta,\beta,\varepsilon\) are strictly positive, \(0<K<1\), and \(b_1>b_2\). The degenerate case \(K=0\) is excluded: when also \(b_1=b_2\), the two positive information classes can form a neutral continuum rather than a unique asymptotically stable equilibrium. The theorem is about the exact finite-dimensional ODE and local stability of its interior equilibrium. It does not make any global attraction claim.

## Proof

**Existence and uniqueness.** At an equilibrium with \(M,Z>0\), the \(M\)- and \(Z\)-equations give
\[
 U=\frac{\mu_1}{b_1}=u,\qquad
 \frac{b_2}{1-KI}=b_1.
\]
Therefore \(I=i\) and \(M+Z=q\). At a positive endemic equilibrium the \(R\)-equation gives \(R=\gamma i/t\), while \(S=s\) follows from the epidemiological total. Finally, the \(I\)-equation gives
\[
 \beta s\frac{1+M}{1+Z}=g.
\]
Solving this identity and \(M+Z=q\) produces the stated expressions for \(M,Z\). Their strict positivity is exactly \(1/(1+q)<p<1+q\). The remaining feasibility inequalities are precisely those needed for positive \(u,i,s\), including \(S+I+R=1\). Conversely, substitution verifies every equilibrium equation. Since all coordinates are forced, this interior equilibrium is unique.

**Four-dimensional linearization.** Use independent coordinates \(q_1=M+Z\), \(z=Z\), \(I\) and \(R\), with \(U=1-q_1\) and \(S=1-I-R\). For this paragraph only write \(m=M_*>0\), \(z_*=Z_*>0\), \(q=m+z_*\), \(u=1-q\), and \(i=I_*\). Set
\[
\begin{gathered}
 a=b_1q,\qquad c=b_1z_*,\qquad
 d=\frac{ub_1Kz_*}{1-Ki},\\
 f=\frac{gi}{s},\qquad A=\frac{gi}{1+m},\qquad
 h=\frac{gi}{1+z_*},\qquad B=A+h,\qquad t=\eta+\mu_2.
\end{gathered}
\]
All quantities are positive and \(a-c=b_1m>0\). Direct differentiation gives the reduced Jacobian
\[
 J=\begin{pmatrix}
 -a&0&d&0\\
 -c&0&d&0\\
 \varepsilon A&-\varepsilon B&-\varepsilon f&-\varepsilon f\\
 0&0&\varepsilon\gamma&-\varepsilon t
 \end{pmatrix}.
\]
For \(\operatorname{Re}\lambda\ge0\) with \(\lambda\ne0\), elimination of the first, second and fourth eigenvector coordinates gives the necessary eigenvalue equation
\[
 \lambda+\varepsilon f+
 \frac{\varepsilon^2 f\gamma}{\lambda+\varepsilon t}
 +\frac{\varepsilon dB(a-c)}{a\lambda}
 +\frac{\varepsilon d(cB-aA)}{a(\lambda+a)}=0.
 \tag{1}
\]
The elimination is legitimate in this closed half-plane, since \(a,t>0\). Also
\[
 \det J=\varepsilon^2dBt(a-c)>0,
\]
so zero is not an eigenvalue.

**Strict right-half-plane obstruction.** For \(\operatorname{Re}\lambda\ge0\), \(\lambda\ne0\), the real parts of \(1/\lambda\) and \(1/(\lambda+\varepsilon t)\) are nonnegative, and
\[
 0\le\operatorname{Re}\frac1{\lambda+a}\le\frac1a.
\]
The only potentially negative term in the real part of (1) is the last one when \(cB-aA<0\). It is enough to establish
\[
 f+\frac{d(cB-aA)}{a^2}>0. \tag{2}
\]
Indeed, when \(cB-aA\ge0\) the claim is immediate. Otherwise, direct substitution yields
\[
 cB-aA=\frac{b_1gi(z_*-m)}{(1+z_*)(1+m)}
\]
and hence
\[
 f+\frac{d(cB-aA)}{a^2}
 =gi\left[\frac1s+
 \frac{uKz_*(z_*-m)}{(1-Ki)q^2(1+z_*)(1+m)}\right].
\]
If \(z_*<m\), use the two strict bounds
\[
 \frac{Ks}{1-Ki}<1,
 \qquad
 \frac{uz_*(m-z_*)}{q^2(1+z_*)(1+m)}<1.
\]
The first follows from \(K<1\) and \(s<1-i\); the second from \(u<1\), \(z_*(m-z_*)<q^2\) and the strictly positive denominators. Their product proves the bracket is positive. Thus (2) holds in every case.

Taking real parts of (1) now gives a strictly positive left-hand side: if \(cB-aA<0\), it is bounded below by \(\varepsilon[f+d(cB-aA)/a^2]>0\); otherwise it is at least \(\varepsilon f>0\). This contradicts (1). Consequently no eigenvalue of \(J\) lies in the closed right half-plane, for **any** \(\varepsilon>0\). Its eigenvalues all have negative real parts. The two normal total-population directions, in the natural normalized off-simplex extension, have eigenvalues \(-\mu_1\) and \(-\varepsilon\mu_2\). Local exponential stability follows.

## Verification

A reproducible exact-rational example is
\[
 (b_1,b_2,\mu_1,K)=(2,3/2,1,1/2),\qquad
 (\beta,\gamma,\mu_2,\eta)=(4/3,1/4,1/4,3/4).
\]
The unique interior equilibrium is
\[
 (U_*,M_*,Z_*,S_*,I_*,R_*)=(1/2,1/4,1/4,3/8,1/2,1/8).
\]
Its four-dimensional tangent characteristic polynomial is exactly
\[
\begin{aligned}
 P(\lambda)={}&\lambda^4+
 \left(1+\frac{5\varepsilon}{3}\right)\lambda^3
 +\left(\frac{17\varepsilon}{10}+\frac{5\varepsilon^2}{6}\right)\lambda^2\\
 &+\left(\frac\varepsilon{30}+\frac{13\varepsilon^2}{15}\right)\lambda
 +\frac{\varepsilon^2}{30}.
\end{aligned}
\]
The accompanying `verify.py` checks the six vector-field equations, reduced and full Jacobians, characteristic-polynomial identities, partial-fraction transfer identity, and exact rational Routh–Hurwitz inequalities for several admissible parameter sets. These computations check the algebra; the proof for **all** permitted parameters is the real-part argument above, not an extrapolation from test cases.

## Relationship to prior work

Bulai, Sensi and Sottile [1] introduced this precise coupled information–SIRS model, characterized the fast and reduced slow subsystems, and gave the coexistence equilibrium in their Appendix A. In Appendix A(vii) they report a quartic characteristic factor without a general stability classification, referring to an example where coexistence is stable. The present contribution establishes the general strict local stability of **every** feasible interior coexistence point for **every positive** time-scale factor, and a compact necessary-and-sufficient interior feasibility interval. The model and the equilibrium concept are therefore not claimed as new.

Opoku-Sarkodie, Bartha, Polner and Röst [2] study endemic stability switches in an SIRWS immunity-boosting system, not this information-driven UMZ–SIRS coupling. Their existence of Hopf bifurcations does not imply an instability, or a stability theorem, for the present equilibrium. Generic slow–fast or characteristic-polynomial results are methodological background and do not automatically establish the biological inequality (2) needed here.

## Limitations

This is strictly **local** exponential stability. It neither proves convergence from arbitrary positive initial conditions nor excludes non-equilibrium attractors elsewhere in phase space. At feasibility boundaries, some compartments vanish and the strict inequalities used in the proof fail; no boundary bifurcation classification is asserted. The degenerate \(K=0\), \(b_1=b_2\) case is excluded and can have nonisolated coexistence equilibria; no strict stability conclusion extends to that case. The epidemic and information populations are separately normalized, homogeneous and deterministic, with the paper's specific rational feedback \(b_2/(1-KI)\) and infection multiplier \((1+M)/(1+Z)\). Different couplings, extra delays, or time-varying parameters may invalidate the positive-real obstruction. Priority over all possible broader spectral or monotone-feedback theories has not been independently established.

## References

[1] I. M. Bulai, M. Sensi and S. Sottile, “A geometric analysis of the SIRS compartmental model with fast information and misinformation spreading,” arXiv:2311.06351 (first public version 2023-11-10), later *Chaos, Solitons & Fractals* 185 (2024), 115104. DOI: 10.1016/j.chaos.2024.115104. Full preprint: https://arxiv.org/html/2311.06351.

[2] R. Opoku-Sarkodie, F. A. Bartha, M. Polner and G. Röst, “Dynamics of an SIRWS model with waning of immunity and varying immune boosting period,” *Journal of Biological Dynamics* 16 (2022), 596–618. DOI: 10.1080/17513758.2022.2109766.
