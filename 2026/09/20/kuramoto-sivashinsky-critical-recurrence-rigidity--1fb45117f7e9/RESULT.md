# Critical recurrence rigidity for periodic Kuramoto-Sivashinsky flows

Consider the conservative-flux Kuramoto-Sivashinsky family on the $2\pi$-periodic circle,
\[
 u_t+\nu u_{xxxx}+u_{xx}+\partial_x f(u)=0,\qquad \nu>0,
\]
with $f\in C^1(\mathbb R)$. Statements below concerning individual trajectories assume enough regularity for the displayed energy identity and Fourier equality case; for the global-attraction corollary, the positive orbit is also assumed precompact in $L^2$. These hypotheses hold for the classical one-dimensional periodic Kuramoto-Sivashinsky equation $f(u)=u^2/2$ by standard well-posedness and compactness results.

Let
\[
 m=\frac1{2\pi}\int_0^{2\pi}u(x,t)\,dx,
 \qquad
 E_m(u)=\frac12\int_0^{2\pi}(u-m)^2\,dx.
\]
The mean $m$ is conserved.

## Theorem 1: exact critical recurrent-orbit classification

At the critical value $\nu=1$, every recurrent trajectory is one of the following:

1. a constant equilibrium $u\equiv m$; or
2. a first-harmonic traveling wave
   \[
   u(x,t)=m+A\cos(x-ct-\theta_0),\qquad A>0,
   \]
   where $f$ is affine on the whole interval $[m-A,m+A]$ with slope $c$.

Conversely, whenever $f$ is affine on $[m-A,m+A]$ with slope $c$, the displayed first-harmonic traveling wave is an exact solution at $\nu=1$.

Hence a constant equilibrium of mean $m$ admits a nonconstant critical recurrent orbit arbitrarily close to it if and only if $f$ is affine on some nontrivial interval centered at $m$.

### Proof

The conservative flux drops out of the centered $L^2$ energy:
\[
 \frac{dE_m}{dt}
 =-\nu\|u_{xx}\|_2^2+\|u_x\|_2^2.
\]
Indeed, if $G_m'(r)=(r-m)f'(r)$, then
\[
 \int_0^{2\pi}(u-m)\partial_xf(u)\,dx
 =\int_0^{2\pi}\partial_xG_m(u)\,dx=0.
\]
At $\nu=1$,
\[
 -\frac{dE_m}{dt}
 =D(u):=\|u_{xx}\|_2^2-\|u_x\|_2^2
 =2\pi\sum_{|k|\ge2}k^2(k^2-1)|\widehat u_k|^2\ge0.
\]
Thus equality holds exactly when
\[
 u-m=a\cos x+b\sin x.
\]

If $u_0$ is recurrent, there are $t_j\to\infty$ with $u(t_j)\to u_0$ in $L^2$. Continuity of $E_m$ gives $E_m(u(t_j))\to E_m(u_0)$. Since $E_m$ is nonincreasing, it is constant along the entire forward trajectory, so $D(u(t))=0$ wherever the energy identity is classical. Therefore either $u\equiv m$, or
\[
 u(x,t)=m+A\cos(x-\theta(t))
\]
with a constant amplitude $A>0$.

For a first harmonic the critical linear terms cancel. Substitution gives, with $s=x-\theta(t)$,
\[
 A\bigl[\theta'(t)-f'(m+A\cos s)\bigr]\sin s=0.
\]
For $\sin s\ne0$, $f'(m+A\cos s)=\theta'(t)$. As $s$ varies, $m+A\cos s$ fills $(m-A,m+A)$; hence $f'$ is constant there. Continuity extends this to the endpoints, so $f$ is affine on $[m-A,m+A]$, and the common value is the constant wave speed $c=\theta'$. The converse follows by direct substitution. $\square$

## Theorem 2: invariant-measure rigidity at criticality

Let $\mu$ be a compactly supported invariant Borel probability measure for the critical flow on a regular phase space on which the energy identity is valid and $D$ is continuous. Then $\mu$ is supported on the union of the constant equilibria and the first-harmonic traveling waves identified in Theorem 1.

In particular, if $f$ is nowhere locally affine, every such invariant measure is supported on constants. On a fixed-mean phase space the only compactly supported invariant probability measure is then $\delta_m$.

### Proof

Invariance and the energy identity give, for each $T>0$,
\[
 0=\int\bigl(E_m(S_Tu)-E_m(u)\bigr)\,d\mu(u)
   =-\int\!\int_0^T D(S_tu)\,dt\,d\mu(u).
\]
The integrand is nonnegative, hence $D=0$ on the support by continuity and invariance of the support. Theorem 1 then classifies every orbit in that support. $\square$

## Corollary: the critical boundary closes for the classical KS equation

For
\[
 u_t+\nu u_{xxxx}+u_{xx}+u u_x=0,
\]
the set of constant equilibria is globally asymptotically stable in periodic $L^2$ if and only if
\[
 \boxed{\nu\ge1}.
\]
More precisely:

- If $\nu>1$, every solution converges exponentially to its conserved mean,
  \[
  \|u(t)-m\|_2\le e^{-(\nu-1)t}\|u(0)-m\|_2.
  \]
- If $\nu=1$, every solution converges to its conserved mean, although the linearization has neutral first harmonics and the energy estimate alone is only semidefinite.
- If $\nu<1$, every constant equilibrium is linearly and nonlinearly unstable: the $k=1$ linear mode has real growth rate $1-\nu>0$.

At $\nu=1$ there are no nonconstant periodic, quasiperiodic, or other recurrent trajectories. On each fixed-mean phase space the only compactly supported invariant probability measure is the Dirac mass at that mean.

### Proof of the critical attraction statement

For $f(u)=u^2/2$, the flux is not affine on any nontrivial interval, so Theorem 1 leaves only constants in the zero-dissipation invariant set. The periodic one-dimensional KS semigroup has precompact positive orbits by the standard compactness theory. LaSalle's invariance principle therefore yields $u(t)\to m$ in $L^2$. Stability of the set of constants follows directly from monotonicity of $E_m$, since $\|u-m\|_2$ is the $L^2$ distance to that set.

For $\nu>1$, Poincare's inequality gives
\[
 \frac{dE_m}{dt}
 \le-(\nu-1)\|u_x\|_2^2
 \le-(\nu-1)\|u-m\|_2^2
 =-2(\nu-1)E_m,
\]
which yields the exponential estimate. For $\nu<1$, linearization at a constant $m$ has Fourier eigenvalues
\[
 \lambda_k=k^2-\nu k^4-ikm,
\]
so $\Re\lambda_1=1-\nu>0$.

## Equivalent domain-length form

For the standard normalized equation
\[
 u_t+u_{xxxx}+u_{xx}+uu_x=0
\]
on a periodic interval of length $L$, rescaling shows that the constant equilibria are globally asymptotically stable exactly for
\[
 \boxed{L\le2\pi}.
\]
The equality $L=2\pi$ is nonhyperbolic but still globally attractive modulo the conserved mean.

## Literature context and originality boundary

Classical work of Nicolaenko, Scheurer and Temam (1985) developed nonlinear stability and attractor theory for the Kuramoto-Sivashinsky equation; Tadmor (1986) proved one-dimensional well-posedness; Il'yashenko (1992), Collet--Eckmann--Epstein--Stubbe (1993), and Goodman (1994) studied global dynamics, attracting sets, and stability. These are foundational sources for the compactness and long-time framework used here.

The most directly comparable accessible source is Al Jamal and Morris (2018). Their Theorem 3.3 proves global asymptotic stability of the set of constant equilibria for the strict regime $\nu>1$, and their linearized argument proves instability for $\nu<1$. Their discussion of $\nu=1$ does not give the zero-dissipation invariant-set calculation above; the final draft states both that the zero equilibrium is a global attractor in one passage and, later, that it is Lyapunov stable but not asymptotically stable. The latter statement is correct for an individual zero equilibrium in the unrestricted phase space because nonzero constants are nearby invariant equilibria, but it does not address asymptotic stability of the full constant-equilibrium set or attraction within a fixed-mean hyperplane.

Cui and Guo (2005) treat a generalized conservative flux $\partial_x f(u)$ with Dirichlet boundary conditions and prove exponential decay under a strict spectral inequality. Li and Chen (2001) and later bifurcation work analyze local branches near KS instabilities. None of the checked accessible sources states the critical recurrent-orbit classification in Theorem 1, the affine-flux obstruction, or the invariant-measure rigidity in Theorem 2.

The originality claim is therefore **to the best of our knowledge**. Important residual risks remain: the complete theorem-level texts of Nicolaenko--Scheurer--Temam (1985), Il'yashenko (1992), Goodman (1994), and Li--Chen (2001) were not fully accessible. They could contain an equivalent observation for the classical quadratic KS equation. The generalized affine-flux if-and-only-if classification was not found in exact, synonymous, or stronger-formulation searches.

## Scientific limitations

The recurrence classification is a critical-boundary statement; it does not describe the attractor after $\nu<1$ or prove existence of post-bifurcation patterns. For a general flux $f$, global convergence from the LaSalle argument requires global well-posedness and precompactness of the trajectory in the chosen phase space; these properties are not asserted here for arbitrary $C^1$ fluxes. The unconditional global-attraction corollary is stated only for the classical one-dimensional periodic KS equation, where the needed semigroup theory is established. No quantitative decay rate is claimed at the nonhyperbolic value $\nu=1$.

## References

1. B. Nicolaenko, B. Scheurer, R. Temam, *Some global dynamical properties of the Kuramoto-Sivashinsky equations: Nonlinear stability and attractors*, Physica D 16 (1985), 155--183. https://doi.org/10.1016/0167-2789(85)90056-9
2. E. Tadmor, *The Well-Posedness of the Kuramoto-Sivashinsky Equation*, SIAM J. Math. Anal. 17 (1986), 884--893. https://doi.org/10.1137/0517063
3. Ju. S. Il'yashenko, *Global analysis of the phase portrait for the Kuramoto-Sivashinsky equation*, J. Dynam. Differential Equations 4 (1992), 585--615. https://doi.org/10.1007/BF01048261
4. P. Collet, J.-P. Eckmann, H. Epstein, J. Stubbe, *A global attracting set for the Kuramoto-Sivashinsky equation*, Commun. Math. Phys. 152 (1993), 203--214. https://doi.org/10.1007/BF02097064
5. J. Goodman, *Stability of the Kuramoto-Sivashinsky and related systems*, Commun. Pure Appl. Math. 47 (1994), 293--306. https://doi.org/10.1002/cpa.3160470304
6. C. Li, G. Chen, *Bifurcation Analysis of the Kuramoto-Sivashinsky Equation in One Spatial Dimension*, Int. J. Bifurcation Chaos 11 (2001), 2493--2500. https://doi.org/10.1142/S021812740100353X
7. S. Cui, C. Guo, *Global Existence and Exponential Decay of Solutions of Generalized Kuramoto-Sivashinsky Equations*, J. Partial Differential Equations 18 (2005), 167--184. https://doi.org/10.4208/jpde.v18.n2.7
8. R. Al Jamal, K. Morris, *Linearized Stability of Partial Differential Equations with Application to Stabilization of the Kuramoto-Sivashinsky Equation*, SIAM J. Control Optim. 56 (2018), 120--147. https://doi.org/10.1137/140993417
