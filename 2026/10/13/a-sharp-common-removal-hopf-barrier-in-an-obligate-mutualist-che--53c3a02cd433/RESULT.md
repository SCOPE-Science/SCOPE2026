# A sharp common-removal Hopf barrier in an obligate-mutualist chemostat

## Finding

For identical obligate mutualists sharing one nutrient, equality of the two biomass removal rates does **not** exclude oscillatory coexistence when removal exceeds hydraulic dilution. The sharp universal boundary for a *local Hopf crossing at a positive equilibrium* is \(d>2D\), where \(D\) is the nutrient dilution and \(d\) is the common biomass removal. The boundary is sharp: every ratio \(d/D>2\) permits a transversal imaginary pair for some positive Monod parameters, and one exact example gives a nondegenerate, supercritical Hopf bifurcation with stable positive cycles. For \(d\le D\), periodic coexistence is globally excluded. These different thresholds distinguish a global non-oscillation theorem from local Hopf feasibility; no assertion about large-amplitude cycles in the intermediate range \(D<d\le2D\) is made.

More precisely, for the system in the next section, the following assertions hold.

1. Every positive periodic orbit has \(x_1(t)=x_2(t)\) at all times. Every positive equilibrium is likewise symmetric. The only boundary equilibrium is washout, which is always exponentially stable.
2. If \(m\le d\), there is no positive equilibrium. If \(m>d\), put \(q=\sqrt{KmLD/2}\) and
   \[
   S_{\mathrm{in},*}=\frac{d}{m-d}\left(K+\frac{2dL+4q}{D}\right).
   \]
   Exactly zero, one, or two coexistence equilibria occur as \(S_{\mathrm{in}}\) lies below, at, or above this explicit threshold. At equality the scalar equilibrium equation has a nondegenerate quadratic fold; above it the lower-biomass equilibrium is a saddle. This does not exclude additional dynamical degeneracies at a fold parameter.
3. If \(d\le D\), the system has no nonconstant positive periodic orbit. Every initially positive solution converges either to washout or to a coexistence equilibrium.
4. If \(d\le2D\), the upper-biomass coexistence equilibrium (when distinct) is locally asymptotically stable. No positive equilibrium can undergo a spectral Hopf crossing at or below this boundary. For each \(d>2D\) a smooth positive-parameter family with a fixed positive equilibrium and a transversal imaginary pair exists.
5. In particular, at
   \[
   (D,d,S_{\mathrm{in}},K,L,m)=(1,5,11,3/5,19,160),\qquad (S,x_1,x_2)=(1,1,1),
   \]
   the nontrivial spectral pair is \(\pm i\sqrt{14}\), the transverse exponent is \(-19/4\), and the canonical planar first Lyapunov coefficient, defined below, is exactly \(-40879/532480<0\). Along the family \(m=100(1+K)\), with all other parameters fixed, a branch of **orbitally asymptotically stable, strictly positive periodic orbits** exists for \(K<3/5\) sufficiently close to \(3/5\).

## Assumptions and scope

Let \(D,d,S_{\mathrm{in}},m,K,L\) all be strictly positive real numbers. For nutrient concentration \(S\ge0\) and biomasses \(x_1,x_2\ge0\), define the cross-growth function
\[
 f(S,z)=\frac{mS}{K+S}\frac{z}{L+z},\qquad
 \begin{aligned}
 \dot S&=D(S_{\mathrm{in}}-S)-x_1f(S,x_2)-x_2f(S,x_1),\\
 \dot x_1&=x_1[f(S,x_2)-d],\\
 \dot x_2&=x_2[f(S,x_1)-d].
 \end{aligned}
\]
This is the exchange-symmetric, equal-yield rescaling of the obligate-mutualism model of Mtar and Fekih-Salem (2026), equations (2) and (21), with \(D_1=D_2=d\) but **not** an assumption \(d=D\). Values \(d>D\) and \(d<D\) are admissible because biomass removal may contain an additional mortality component or have a different retention time. For statements about periodic orbits and convergence the orbit starts with \(x_1,x_2>0\) and \(S\ge0\). Equilibrium counts concern states with all three components positive. 'Hopf crossing' means a simple imaginary eigenvalue pair with nonzero speed through the imaginary axis, and is distinguished from existence of cycles; the final exact example supplies the latter by a nonzero first Lyapunov coefficient.

## Proof

### Positivity, boundedness, and synchronization

The nonnegative octant is forward invariant: the nutrient derivative is \(D S_{\mathrm{in}}>0\) at \(S=0\), and each biomass equation is proportional to its biomass. With \(T=S+x_1+x_2\), cancellation of consumption and growth terms gives
\[
 \dot T=DS_{\mathrm{in}}-DS-d(x_1+x_2)
 \le DS_{\mathrm{in}}-\min(D,d)T.
\]
Thus all solutions are global and bounded. At a positive equilibrium, \(f(S,x_2)=f(S,x_1)=d\); the strict monotonicity of \(f\) in its second argument implies \(x_1=x_2\). On either one-species face, obligate mutualism makes the remaining population decay, so the only boundary equilibrium is \((S_{\mathrm{in}},0,0)\). Its eigenvalues are \(-D,-d,-d\).

For positive populations, define \(R=\log(x_1/x_2)\). Direct subtraction gives the exact identity
\[
 \dot R=f(S,x_2)-f(S,x_1)
 =-\frac{mSL(x_1-x_2)}{(K+S)(L+x_1)(L+x_2)}.
\]
Hence \(R\) is strictly decreasing when positive and strictly increasing when negative; \(|R|\) cannot increase. A periodic \(R\) must be constant, and strict positivity of the nutrient along such an orbit forces \(x_1=x_2\). This argument does not require \(d\le D\).

### Coexistence census and the fold

On the symmetric plane put \(x_1=x_2=x>0\). The equations reduce to
\[
 \dot S=D(S_{\mathrm{in}}-S)-2xf(S,x),\qquad
 \dot x=x[f(S,x)-d].
\]
If \(m\le d\), strict saturation gives \(f(S,x)<m\le d\), so no coexistence equilibrium exists. If \(m>d\), the equation \(f(S,x)=d\) is equivalent to
\[
 x>\frac{dL}{m-d},\quad
 S=\frac{dK(L+x)}{(m-d)x-dL}=:s(x),\quad
 S_{\mathrm{in}}=H(x):=s(x)+\frac{2d}{D}x.
\]
Writing \(a=m-d>0\), a derivative calculation yields
\[
 H'(x)=-\frac{dKmL}{(ax-dL)^2}+\frac{2d}{D},\qquad
 H''(x)=\frac{2adKmL}{(ax-dL)^3}>0.
\]
As \(x\downarrow dL/a\) and as \(x\to\infty\), \(H(x)\to\infty\). Its unique minimizer is \(x_*=(dL+q)/a\), with \(q=\sqrt{KmLD/2}\), and substitution gives the stated exact \(S_{\mathrm{in},*}=H(x_*)\). Strict convexity and \(\partial_{S_{\mathrm{in}}}[H(x)-S_{\mathrm{in}}]=-1\) show a nondegenerate **scalar equilibrium fold** at equality (not necessarily an isolated one-dimensional center manifold for every parameter choice).

### Spectral splitting and the sharp Hopf barrier

Let \((S,x,x)\) be any positive equilibrium and set
\[
 u=xf_x(S,x)=\frac{dL}{L+x}\in(0,d),\qquad
 v=2xf_S(S,x)>0.
\]
Exchange symmetry splits the full Jacobian into an antisymmetric eigenvalue \(-u\) and the symmetric-plane matrix
\[
 A=\begin{pmatrix}-D-v&-2d-2u\\v/2&u\end{pmatrix},\quad
 \operatorname{tr}A=-D-v+u,\quad
 \det A=dv-Du.
\]
The determinant has the sign of \(H'(x)\), so it is negative at the lower positive equilibrium and positive at the upper one. The lower equilibrium is therefore a saddle in the full three-dimensional model. At an upper-branch point, suppose that the trace were nonnegative. Then \(v\le u-D\), while \(\det A>0\) requires \(dv>Du\). Combining them gives
\[
 (d-D)u>dD.
\]
Since \(u<d\), this is impossible whenever \(d\le2D\). Thus \(\operatorname{tr}A<0\) and \(\det A>0\) throughout the upper branch for \(d\le2D\); together with \(-u<0\), this proves local asymptotic stability. The strict inequality also excludes imaginary eigenvalue pairs at the fold or lower branch (where the determinant is nonpositive).

Conversely, fix any \(d>2D\). Choose \(\beta\) strictly between \(D/(d-D)\) and \(1\), and let
\[
 a=\frac{d\beta-D}{2d}\in(0,1),\quad
 K=\frac{a}{1-a},\quad L=\frac{\beta}{1-\beta},\quad
 m=d(1+K)(1+L),\quad S_{\mathrm{in}}=1+\frac{2d}{D}.
\]
The point \((S,x_1,x_2)=(1,1,1)\) is a positive equilibrium with \(u=d\beta\), \(v=d\beta-D\), hence \(\operatorname{tr}A=0\) and \(\det A=d((d-D)\beta-D)>0\). Varying \(K\) while setting \(m(K)=d(1+K)(1+L)\) keeps this equilibrium fixed and produces
\[
 \frac{d}{dK}\operatorname{tr}A=-\frac{2d}{(1+K)^2}\ne0.
\]
The simple imaginary pair therefore crosses transversally. The universal boundary \(d>2D\) is both necessary and sufficient for **some** symmetric positive-parameter model to have a spectral Hopf crossing.

### A nondegenerate supercritical Hopf instance

Set \(D=1\), \(d=5\), \(S_{\mathrm{in}}=11\), \(L=19\), and vary \(K>0\) with \(m=100(1+K)\). The positive equilibrium \((1,1,1)\) persists. At \(K_0=3/5\), the symmetric-plane matrix is
\[
 A_0=\begin{pmatrix}-19/4&-39/2\\15/8&19/4\end{pmatrix},
 \quad\operatorname{tr}A_0=0,\quad\det A_0=14,
\]
while the antisymmetric eigenvalue equals \(-19/4\). The real part of the imaginary pair varies with speed \(-125/64\) with respect to \(K\) at the crossing. Define local canonical coordinates
\[
 U=S-1,\qquad
 V=\frac{39}{2\sqrt{14}}\left(x-1+\frac{19}{78}(S-1)\right),
\]
so the planar vector field is \(\dot U=-\sqrt{14}V+F(U,V)\), \(\dot V=\sqrt{14}U+G(U,V)\), with \(F,G\) containing terms of order at least two. At the origin, the standard planar Hopf coefficient
\[
 \ell_1=\frac{F_{UUU}+F_{UVV}+G_{UUV}+G_{VVV}}{16}
 +\frac{F_{UV}(F_{UU}+F_{VV})-G_{UV}(G_{UU}+G_{VV})-F_{UU}G_{UU}+F_{VV}G_{VV}}{16\sqrt{14}}
 =-\frac{40879}{532480}<0
\]
was evaluated exactly from the rational vector field (the bundled symbolic verifier recomputes every derivative). Since the crossing speed is negative, the Hopf normal form has a small attracting periodic orbit when \(K<3/5\) is sufficiently close. Its transverse Floquet exponent tends to \(-19/4\), so the orbit also attracts in the full three-dimensional nonnegative system; its components remain strictly positive by continuity from the equilibrium.

### Global non-oscillation when removal does not exceed dilution

By the ratio identity, any interior periodic orbit must lie in the symmetric plane. On that plane every nonconstant periodic trajectory must satisfy \(0<S<S_{\mathrm{in}}\): the vector field points strictly toward decreasing \(S\) at \(S\ge S_{\mathrm{in}}\). Apply the Dulac multiplier \(B(S,x)=1/[xf(S,x)]\) on the simply connected rectangle \(0<S<S_{\mathrm{in}},\ x>0\). Its weighted divergence satisfies
\[
 xf(S,x)^2\,\operatorname{div}(B\dot S,B\dot x)
 =-Df-D(S_{\mathrm{in}}-S)f_S+dxf_x<0
\]
whenever \(d\le D\), because \(xf_x/f=L/(L+x)<1\). Thus the Bendixson–Dulac theorem excludes all nonconstant periodic coexistence orbits, including non-symmetric ones.

For convergence, the bounded monotone ratio \(R\) has a finite limit. If its limit is nonzero, invariance of the omega-limit set and the strict ratio sign force the omega-limit set onto the boundary, whose only compact invariant limiting state is washout. If its limit is zero, each non-washout omega-limit point lies on the symmetric plane. The planar omega-limit sets have finitely many equilibria (the census above), no closed orbit, and no connecting polycycle by the same strictly signed Dulac divergence; the planar Poincare–Bendixson alternatives therefore reduce every compact omega-limit set to one equilibrium. Consequently every interior trajectory converges to washout or to one of the positive equilibria for \(d\le D\). This does not assert which basin a given initial condition belongs to.

## Verification

The standalone `verify.py` script uses exact SymPy rational expressions, checks the two-dimensional symmetric Jacobian, the transverse eigenvalue and all displayed rational Hopf data, differentiates the complete planar vector field through cubic order, and independently recomputes \(\ell_1=-40879/532480\). Run `python verify.py` with SymPy installed as in `requirements.txt`. The output `VERIFY_OK` indicates that the finite algebraic checks passed; the global periodic-orbit exclusion and universal parameter inequalities are proved analytically above and are not consequences of finite symbolic tests alone.

## Relationship to prior work

Mtar and Fekih-Salem (arXiv:2603.11002v1, 2026) introduced the exact model family, treated generic distinct biomass-removal parameters, proved general equilibrium existence and local Routh–Hurwitz conditions, and exhibited complicated numerical Hopf and cycle scenarios. Those results and criteria are not claimed as new. Their mortality-free special case sets **both biomass rates equal to the hydraulic dilution**; they do not state the full exchange-symmetric, common-removal spectral Hopf feasibility boundary \(d>2D\), the global ratio obstruction to nonsymmetric periodic orbits, or the exact supercritical Hopf example above.

El Hajji, Harmand, Chaker, and Lobry (2009) established coexistence and global structural properties for models without species-specific mortality, effectively \(d=D\); their standard equilibrium and non-oscillation facts at that endpoint are acknowledged. The present theorem separates \(d\le D\) global non-oscillation, \(d\le2D\) local Hopf impossibility, and \(d>2D\) constructive possibility, including equal biomass rates. Work on mutualistic cross-feeding and Allee-effect bistability treats other nutrient systems and does not yield the displayed sharp common-removal threshold by direct specialization.

## Limitations

The sharp \(2D\) boundary is for **local Hopf feasibility in the class of positive symmetric Monod systems**, not a theorem that every particular model with \(d>2D\) oscillates. The existence proof for every \(d>2D\) gives a spectral crossing; only the separately specified rational example has its cubic Hopf nondegeneracy verified and a stable cycle proved. The global non-oscillation theorem covers \(d\le D\); large cycles in \(D<d\le2D\) are not excluded. No claim is made for asymmetric growth functions, unequal removal rates, stochastic systems, or experimentally measured microbial populations. Previously published generic local-stability criteria can imply the elementary Jacobian facts once symmetry is imposed; originality concerns their sharp global synthesis and the constructive exact Hopf boundary.

## References

1. T. Mtar and R. Fekih-Salem, *Global dynamics and bifurcation analysis of a chemostat model with obligate mutualism and mortality*, arXiv:2603.11002v1, first posted 11 March 2026. https://arxiv.org/html/2603.11002v1
2. M. El Hajji, J. Harmand, H. Chaker, and C. Lobry, *Association between competition and obligate mutualism in a chemostat*, Journal of Biological Dynamics 3 (2009), 635–647. doi:10.1080/17513750902915978. https://www.tandfonline.com/doi/full/10.1080/17513750902915978
3. S. Vet, L. Gelens, and D. Gonze, *Mutualistic cross-feeding in microbial systems generates bistability via an Allee effect*, Scientific Reports 10 (2020), 7763. doi:10.1038/s41598-020-63772-4. https://www.nature.com/articles/s41598-020-63772-4
