# Linearized localization rigidity for the hyperbolic–hyperbolic transverse Poisson structure in dimension four

## Context and motivation

Let $(M^4,\pi_0)$ be a Poisson $4$-manifold with a nondegenerate rank-zero point
$p$ of Williamson type $(0,2,0)$ (hyperbolic–hyperbolic). The admitted SCOPE
target asked whether $p$ is universally leafwise unstable under general
($C^\infty$-small, not necessarily integrable) Poisson deformations: either an
arbitrarily small Poisson deformation erases the zero in a fixed ball, leaving
only rank-$2$ leaves, or some such $p$ persists. Eliasson theory settles only
integrable perturbations (which preserve the Casimir fibration), and
Dufour–Molino-type results treat $3$D nonzero $1$-jet cases, so the general
Poisson deformation question was open.

The natural attack is to take the explicit global rank-jump direction and
localize it into a compactly supported deformation. This record decides the
entire linearized localization problem for that jump direction: it gives the
mechanism, two certified dead ends, and an essentiality certificate.

## Definitions and setup

Work in Weinstein coordinates $x=(x_0,x_1,x_2,x_3)$ at $p$ with Casimirs
$C_1=x_0x_1$, $C_2=x_2x_3$ and Nambu form
$\Pi^{ij}=\varepsilon^{ijkl}\,\partial_k C_1\,\partial_l C_2$. Explicitly

$$\Pi_{02}=-x_0x_2,\quad \Pi_{03}=x_0x_3,\quad
  \Pi_{12}=x_1x_2,\quad \Pi_{13}=-x_1x_3,\quad
  \Pi_{01}=\Pi_{23}=0,$$

skew-symmetric. Then $\Pi=A\wedge B$ with $A=(-x_0,x_1,0,0)$,
$B=(0,0,x_2,-x_3)$, so $\mathrm{Pf}(\Pi)\equiv 0$ and
$\mathrm{rank}\,\Pi\le 2$ everywhere. The zero set is the union of two planes
$\{x_0=x_1=0\}\cup\{x_2=x_3=0\}$. Write $d_{ij}=dx_i\wedge dx_j$ for constant
bivectors. The Lichnerowicz differential is the Schouten bracket
$[\Pi,\,\cdot\,]$; an infinitesimal deformation $\nu$ is a cocycle if
$[\Pi,\nu]=0$.

## Result (headline claim)

For the hyperbolic–hyperbolic germ $\Pi$ above:

- **(A) Constant infinitesimal classification.** For constant
  $\nu=\sum n_{ij}d_{ij}$, $[\Pi,\nu]=0$ iff
  $n_{02}=n_{03}=n_{12}=n_{13}=0$. Hence the constant-cocycle space is exactly
  $\mathrm{span}\{d_{01},d_{23}\}$, of dimension $2$.
- **(B) Global rank-jump family.** $\Pi_t=\Pi+t\,d_{01}$ with $t\ne 0$ is
  Poisson, has no zeros anywhere on $\mathbb{R}^4$, and has rank exactly $2$ at
  every point.
- **(C) Single-component localization no-go.** No nonzero compactly supported
  $C^1$ function $\varphi$ makes $\varphi\,d_{01}$ a Poisson cocycle:
  $[\Pi,\varphi\,d_{01}]\ne 0$.
- **(D) Radial localization impossible at linear order.** Let
  $\nu^{ij}(x)=f_{ij}(s)$ with $s=|x|^2$, $C^1$. If $[\Pi,\nu]\equiv 0$ then all
  $f_{ij}$ are constant, off-span components vanish, and $f'\equiv 0$; the
  admissible space on every sphere $s>0$ is exactly
  $\mathrm{span}\{e_{f_{01}},e_{f_{23}}\}$. In particular no $C^1$ radial
  transition $f_{01}:1\to 0$ exists. Certified by an exact minor determinant
  $D(s)=-36\,s^6\ne 0$ for all $s>0$.
- **(E) Degree-$\le 2$ cohomology slice.** Quadratic-polynomial bivector
  cocycles ($90$ unknowns, $96$ equations over $\mathbb{Q}$) form a
  $34$-dimensional space. The coboundary image of affine vector fields ($20$
  parameters) has rank $16$. Hence the essential quotient has dimension
  $34-16=18$, and $d_{01}$ represents a nonzero essential class (not a
  coordinate artifact).

## Proof / evidence

**(A)** Machine-expanded (sympy, exact):
$[\Pi,\nu]^{012}=-n_{02}x_1-n_{12}x_0$,
$[\Pi,\nu]^{013}=n_{03}x_1+n_{13}x_0$,
$[\Pi,\nu]^{023}=-n_{02}x_3-n_{03}x_2$,
$[\Pi,\nu]^{123}=n_{12}x_3+n_{13}x_2$.
Each must vanish as a polynomial; linear independence of the $x_i$ forces the
four coefficients to zero.

**(B)** $[\Pi,\Pi]=0$ checked exactly componentwise; $[\Pi,d_{01}]=0$ is (A);
$[d_{01},d_{01}]=0$ since $d_{01}$ is constant. Bilinearity gives
$[\Pi_t,\Pi_t]=0$. Entry $(0,1)$ equals $t\ne 0$, so $\Pi_t(x)\ne 0$
everywhere. Exact Pfaffian
$\mathrm{Pf}(\Pi_t)=M_{01}M_{23}-M_{02}M_{13}+M_{03}M_{12}\equiv 0$ (sympy), so
rank $<4$; a nonzero skew-symmetric $4\times 4$ matrix has even rank $\ge 2$;
hence rank exactly $2$. Numeric eigen-checks at $4$ sample points confirm
spectrum $(0,0,\lambda,\lambda)$.

**(C)** $[\Pi,\varphi\,d_{01}]=X_\varphi\wedge d_{01}$ with
$X_\varphi=\Pi^\sharp(d\varphi)$. Vanishing holds iff
$X_\varphi\in\mathrm{span}(\partial_0,\partial_1)$, i.e. $X^2=X^3=0$. Exact
computation gives $X^2=x_2E$, $X^3=-x_3E$ with
$E:=x_0\varphi_{,0}-x_1\varphi_{,1}$. Hence $E=0$ off $\{x_2=x_3=0\}$ and by
continuity everywhere. So $\varphi$ is invariant under the hyperbolic flow
$(x_0,x_1)\mapsto(e^t x_0,e^{-t}x_1)$: $\varphi=F(x_0x_1,x_2,x_3)$. If
$F(s,a_2,a_3)\ne 0$, the points $(N,s/N,a_2,a_3)$ for $|N|\to\infty$ all carry
nonzero values, so the support is unbounded, contradicting compact support.
Hence $F\equiv 0$.

**(D)** Write $[\Pi,\nu]^{abc}=L^{abc}(x;f)+C^{abc}(x;g)$ with $g=f'$,
$L$ linear and $C$ cubic in $x$. On $|x|^2=s$ with direction
$v\in\mathbb{Q}^4\setminus 0$, $x=\rho v$: row$(v)/\rho=L(v;f)+(s/|v|^2)C(v;g)$.
Stacking $4$ equations over $21$ rational directions gives an $84\times 12$
system $M(s)=[A\mid sB]$ over $\mathbb{Q}[s]$. Exact rank computation shows
$\ker M=\mathrm{span}\{e_{f_{01}},e_{f_{23}}\}$ (nullity $2$ over
$\mathbb{Q}(s)$). A exhibited $10\times 10$ minor has exact determinant
$D(s)=-36s^6\ne 0$ for all $s>0$, so $\mathrm{rank}\,M(s)=10$ on every sphere
— no exceptional spheres — and $g\equiv 0$ is forced.

**(E)** Exact sympy rational nullspace/column-space computation over the
$90$-dimensional degree-$\le 2$ bivector coefficient space:
$\dim\ker=34$; coboundary rank from affine vector fields is $16$; quotient
dimension $34-16=18$; $\mathrm{rank}(B\mid d_{01})=17>16$, so $d_{01}$ is
essential. A smooth coboundary $[\Pi,X]$ vanishes at the origin (since $\Pi$
is quadratic), while $d_{01}(0)\ne 0$, giving an independent analytic reason
$d_{01}$ is not a coboundary.

Numeric spot-checks only: eigenvalue samples for (B); per-sphere SVD at
$s=0.25,1,4$ for (D), consistent with the exact certificates.

## Limitations

$\Pi_t$ is global on $\mathbb{R}^4$, not compactly supported. Theorems (C)–(D)
rule out the two most natural linear-order localization routes
(single-component cutoff; radial multi-component cutoff), and (E) quantifies
the finite polynomial slice, but the full nonlinear target — a compactly
supported $C^\infty$-small fixed-ball rank change, or a persistence proof —
remains open. Completing it needs a fully non-symmetric smooth cocycle,
higher-order/nonlinear analysis, or global gluing beyond this record.

## Reproducibility

Replay scripts (all green; exact parts over $\mathbb{Q}$):

- `output/artifacts/verify_target_routes.py` — (A), (B), (C) formulas,
  Pfaffian, decomposability, eigen spot-checks.
- `output/artifacts/verify_radial_exact.py` — exact (D) nullspace over
  $\mathbb{Q}(s)$.
- `output/artifacts/verify_loopholes.py` — $[\pi_0,\pi_0]=0$ and the
  $D(s)=-36s^6$ minor.
- `output/artifacts/verify_cohomology.py` — (E) $34/16/18$ decomposition and
  essentiality of $d_{01}$.

## References

- J.-P. Dufour and A. Haraki, Singularities and bifurcations of 3-dimensional
  Poisson structures.
- T. Zung, Structurally stable nondegenerate singularities of integrable
  systems.
- Perturbed rank 2 Poisson systems and periodic orbits on Casimir manifolds.
- J.-P. Dufour, Hyperbolic actions on Poisson manifolds.
- Dufour–Zung / Crainic–Fernandes normal-form and stability program
  (background).
- Monnier, Computations of Nambu-Poisson cohomologies (adjacent complex,
  contrasted in audit).
