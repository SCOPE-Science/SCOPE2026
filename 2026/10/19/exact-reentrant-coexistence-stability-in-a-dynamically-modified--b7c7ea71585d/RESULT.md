# Exact reentrant coexistence stability in a dynamically modified three-species food web

## Finding
Consider the cyclic, symmetric higher-order interaction model of Van Giel, Daly, Baetens and De Baets, with fixed pairwise magnitude \(\alpha=2\), negative modifier strength \(\beta<0\), and modifier speed \(\omega>0\). The model has exactly one strictly positive coexistence equilibrium. An explicit cubic in \(\omega\), given below, decides its complete **linear** stability: positive values mean local asymptotic stability, negative values mean two eigenvalues in the right half-plane, and zeros mean one simple imaginary conjugate pair with all other eigenvalues in the open left half-plane.

At the natural interaction-nullification strength \(\beta=-9\), the unique coexistence state is \((u,v,z,h)=(7/9,11/9,1/9,0)\). It is locally asymptotically stable precisely when
\[
0<\omega<\omega_-\quad\text{or}\quad\omega>\omega_+,
\qquad
\omega_\pm=\frac{43}{15}\pm\frac{2\sqrt{3679}}{45}.
\]
For \(\omega_-<\omega<\omega_+\), the equilibrium has exactly two unstable eigenvalues. At either endpoint, it has one simple purely imaginary conjugate pair and two eigenvalues with negative real parts. This stable–unstable–stable sequence persists for every modifier strength in some open interval containing \(\beta=-9\).

## Assumptions and scope
The four-dimensional autonomous ODE is
\[
\begin{aligned}
\dot u&=u(1-u+2hv-2z),\\
\dot v&=v(1-v-2hu+2z),\\
\dot z&=z(1-z+2u-2v),\\
\dot h&=\omega(1-h+\beta z).
\end{aligned}
\]
The species abundances \(u,v,z\) are strictly positive; the interaction modifier \(h\) is real-valued, as it may reverse the sign of a pairwise interaction. The parameters satisfy \(\beta<0\) and \(\omega>0\). This is the intransitive, symmetric modification of both directed interactions between the first two species in equations (3)–(5) and Supplement S1 of [1], with all nonzero base pairwise magnitudes equal to two.

For an arbitrary \(\beta<0\), let \(m\) be the unique number in
\[
-1+\frac{\sqrt3}{2}<m<1
\]
satisfying
\[
\beta=\frac{(m-1)(4m^2+9)}{4m^2+8m+1}.
\]
The unique positive equilibrium, independently of \(\omega\), has
\[
u=\frac{6m+7}{4m^2+9},\qquad
v=\frac{2m+11}{4m^2+9},\qquad
z=\frac{4m^2+8m+1}{4m^2+9},\qquad h=m.
\]
Here and below the unadorned \(u,v,z\) in coefficient definitions denote these equilibrium values. Define
\[
\begin{aligned}
S&=u+v+z,\\
Q&=uv+uz+vz+4m^2uv+4(u+v)z,\\
R&=(9+4m^2)uvz,\\
C_1&=Q-8\beta uvz,\\
D_1&=R+4\beta uvz\,[2m(u-v)-u-v],\\
A&=S+\omega,\quad B=Q+S\omega,\\
C&=R+C_1\omega,\quad D=D_1\omega,\\
\Delta_\beta(\omega)&=ABC-C^2-A^2D.
\end{aligned}
\]
For each fixed \(\beta<0\), this last expression is a real polynomial of degree at most three in \(\omega\), whose coefficients can be determined from the unique \(m\). No claim concerns boundary equilibria, attraction basins, periodic-orbit existence, or global asymptotics.

## Proof
**1. Exactly one positive coexistence state.** At a strictly positive equilibrium the three per-capita growth factors vanish. With \(h=m\), these are three linear equations in \(u,v,z\). Solving gives the rational expressions above, whose common denominator is positive. Positivity of \(u\) requires \(m>-7/6\); positivity of \(z\) requires either \(m<-1-\sqrt3/2\) or \(m>-1+\sqrt3/2\). Therefore simultaneous positivity requires the latter range. The modifier equilibrium then gives \(\beta=(m-1)/z\); since \(\beta<0\) and \(z>0\), necessarily \(m<1\).

Write \(P(m)=16m^4+64m^3-56m^2+64m+81\). Direct differentiation yields
\[
\frac{d\beta}{dm}=\frac{P(m)}{(4m^2+8m+1)^2}.
\]
On \(-1/4\le m\le0\), \(P(m)\ge81-1-7/2-16>0\). On \(0\le m\le1\), \(64m-56m^2\ge8m\), so again \(P(m)>0\). The admissible interval lies in \((-1/4,1)\). Moreover \(\beta(m)\) increases continuously from \(-\infty\) as \(m\) approaches its lower endpoint, to \(0\) as \(m\uparrow1\). Hence every negative \(\beta\) selects exactly one positive state.

**2. Characteristic polynomial and coefficient signs.** Linearization at that state gives
\[
J=\begin{pmatrix}
-u&2mu&-2u&2uv\\
-2mv&-v&2v&-2uv\\
2z&-2z&-z&0\\
0&0&\omega\beta&-\omega
\end{pmatrix}.
\]
Direct determinant expansion, or elimination of the modifier block, gives
\[
\det(\lambda I-J)=\lambda^4+A\lambda^3+B\lambda^2+C\lambda+D.
\]
The coefficients \(A,B,C,D\) are all strictly positive. Indeed \(S,Q,R>0\) immediately. The two non-obvious quantities simplify to
\[
C_1=\frac{3(4m^2+32m+29)}{4m^2+9}>0,
\]
\[
D_1=\frac{(2m+11)(6m+7)P(m)}{(4m^2+9)^3}>0.
\]
For the first inequality, \(m>-1/4\) implies \(4m^2+32m+29>21\); for the second, Step 1 proves positivity of all factors. This establishes the signs for the *entire* admissible negative-modification family, not just one sample parameter.

**3. Exact local stability test.** The quartic Routh–Hurwitz criterion for strictly positive coefficients reads
\[
AB>C\quad\text{and}\quad ABC>C^2+A^2D.
\]
Because \(C,D,A>0\), the second strict inequality automatically implies the first. Thus the equilibrium is locally asymptotically stable exactly when \(\Delta_\beta(\omega)>0\). When \(\Delta_\beta(\omega)<0\), the first Routh-column entries are \(1,A,(AB-C)/A,\Delta_\beta/(AB-C),D\) if \(AB\ne C\), producing exactly two sign changes for either sign of \(AB-C\). At \(AB=C\) the determinant equals \(-A^2D<0\), so the same count follows by continuity (no imaginary root can occur unless the determinant vanishes). When \(\Delta_\beta(\omega)=0\), the identity
\[
\det(\lambda I-J)
=\left(\lambda^2+\frac CA\right)
\left(\lambda^2+A\lambda+\frac{AD}{C}\right)
\]
holds: the first factor has a simple imaginary pair, and the second is Hurwitz because its two non-leading coefficients are positive. These conclusions classify the full linear spectrum, including the two endpoint cases. The imaginary-pair case does not, by itself, determine nonlinear stability.

**4. Exact reentrant interval.** The paper's interaction-nullification condition is \(h=m=0\), which gives \(\beta=-9\) and the coexistence state stated above. Then
\[
S=\frac{19}{9},\quad Q=\frac{167}{81},\quad R=\frac{77}{81},
\quad C_1=\frac{29}{3},\quad D_1=\frac{77}{9}.
\]
Consequently
\[
\Delta_{-9}(\omega)
=\frac{16}{59049}(108\omega+31)
(405\omega^2-2322\omega+385).
\]
Its quadratic factor has exactly the two distinct positive zeros \(\omega_\pm\) in the Finding. The linear factor is positive for \(\omega>0\), so the stability and instability intervals follow from Step 3. Both positive roots are simple. Coefficients of \(\Delta_\beta\) depend smoothly on \(m\), and the third root at \(m=0\) is the strictly negative value \(-31/108\). By continuity and the implicit-function theorem, for every \(m\) in a sufficiently small open neighborhood of zero there remain exactly two positive simple roots and one negative root. Step 1 gives a smooth monotone change of parameter from \(m\) to \(\beta\), proving persistence on an open interval of modification strengths.

## Verification
Run `python verify.py` in the same directory. The standalone SymPy script checks all three equilibrium identities and the modifier identity, computes the characteristic determinant independently from the explicit Jacobian, verifies the simplified coefficient formulas, proves the exact symbolic factorization at \(\beta=-9\), checks the two imaginary-threshold factors, and compares the Routh sign with explicit quartic root counts at 24 additional rational parameter-speed pairs. It also checks stable/unstable/stable spectra at \(\omega=1/10,1,10\). The displayed proof, not the finite eigenvalue checks, establishes the infinite-parameter conclusions.

## Relationship to prior work
Van Giel, Daly, Baetens and De Baets [1] introduced this continuously evolving modifier and numerically mapped the coexistence and oscillation regions in its three-species intransitive model. Supplement S1 explicitly solves the special nullification equilibrium \((7/9,11/9,1/9)\) and obtains \(\beta=-9\), but does not classify its modifier-speed spectrum or derive exact stability thresholds. The present result gives an explicit necessary-and-sufficient spectral criterion across all \(\beta<0\), and two algebraic crossing speeds with robust reentrance at that biologically distinguished nullification strength. It does **not** treat the visually observed cycles as proved to exist or to be attracting. The later agent-based study [2] uses discrete stochastic grid competition and a spatially localized modifier, not the continuous four-state ODE or its Jacobian spectrum.

The quartic Hurwitz test itself is classical. The contribution is the model-specific global positivity reduction, the exact polynomial stability law, and its two explicit reentrant crossings at a source-motivated parameter, rather than a new general criterion for fourth-degree polynomials.

## Limitations
Only local linear stability of the positive coexistence equilibrium is classified. At \(\omega=\omega_\pm\), one conjugate pair is imaginary; nonlinear center/focus behavior, Lyapunov coefficients, and existence or stability of nearby periodic orbits remain unproved. In a regime with an unstable positive equilibrium, the eventual population outcome is not inferred. The ecological interpretation presumes the source's sign-reversible interaction modifier and equal base pairwise magnitude two. The formula for general negative \(\beta\) requires solving a unique scalar monotone equation; it is an exact criterion but not a closed radical expression for all \(\beta\). Coverage by unindexed specialist literature remains a possible originality risk; this manuscript has not undergone independent validation.

## References
[1] T. Van Giel, A. J. Daly, J. M. Baetens, and B. De Baets, *Modification speed alters stability of ecological higher-order interaction networks*, arXiv:2408.14209v1, first public 26 August 2024; later Physical Review E 111, 014309 (2025). Main text equations (3)–(5), Figure 3, supplementary sections S1–S4. https://arxiv.org/abs/2408.14209 ; https://arxiv.org/pdf/2408.14209

[2] T. Van Giel, H. Jaspaert, A. J. Daly, B. De Baets, and J. M. Baetens, *Modification speed and radius of higher-order interactions alter the oscillatory dynamics in an agent-based model*, arXiv:2601.15144v1 (2026), especially sections 2 and 3. https://arxiv.org/html/2601.15144v1

[3] Routh–Hurwitz stability criterion for fourth-degree real polynomials (standard classical theorem).
