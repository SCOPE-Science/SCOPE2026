# Positive Neumann steady patterns at a degenerate porous-diffusion resonance

## Result

Consider the one-dimensional porous-diffusion system
\[
\begin{aligned}
U_t&=(U U_x)_x+U(a_1-bU)+h_1+c_1V,\\
V_t&=(V V_x)_x+V(a_2-bV)+h_2+c_2U,
\end{aligned}
\qquad b>0,
\]
on \(0<x<L\), with homogeneous Neumann conditions
\[
U_x(0)=U_x(L)=V_x(0)=V_x(L)=0.
\]

Suppose that, for some \(\alpha>0\),
\[
h_2=\alpha^2h_1,\qquad
\alpha a_2+c_2=\alpha^2(a_1+\alpha c_1),
\tag{1}
\]
and that
\[
bU^2-(a_1+\alpha c_1)U-h_1
=b(U-U_-)(U-U_+)
\tag{2}
\]
has two roots \(0<U_-<U_+\).

Then the stationary system has an exact proportional reduction
\[
V(x)=\alpha U(x),
\tag{3}
\]
under which both stationary equations reduce to
\[
(UU_x)_x-b(U-U_-)(U-U_+)=0.
\tag{4}
\]

If \(U_->U_+/2\), define
\[
L_c=\pi\sqrt{\frac{U_-}{b(U_+-U_-)}}.
\tag{5}
\]
For every \(L>L_c\), (4) has a positive nonconstant Neumann solution on \([0,L]\). More generally, for every integer \(m\ge1\) satisfying \(mL_c<L\), there is a positive proportional stationary profile with \(m\) half-oscillations on \([0,L]\). Hence there are at least
\[
\left\lceil \frac{L}{L_c}\right\rceil-1
\tag{6}
\]
distinct oscillation classes of such profiles.

For the concrete prey-predator example studied by Cherniha and Kriukova,
\[
\begin{aligned}
U_t&=(UU_x)_x+U(6.5-3U)-1-V,\\
V_t&=(VV_x)_x+V(1.5-3V)-9+27U,
\end{aligned}
\tag{7}
\]
one has
\[
\alpha=3,\qquad U_-=\frac12,\qquad U_+=\frac23,\qquad L_c=\pi.
\tag{8}
\]
Thus every pure-Neumann interval of length \(L>\pi\) supports a positive nonconstant steady state with \(V=3U\); if \(L=8\), for example, (6) gives at least two distinct half-wave classes.

The lower homogeneous equilibrium
\[
P_-=\left(\frac12,\frac32\right)
\]
does not lose stability through an ordinary Turing-unstable band. For a Neumann Laplacian eigenvalue \(\mu\ge0\), the linearized mode matrix at \(P_-\) has
\[
\operatorname{tr}A_-(\mu)=-2(\mu+2),\qquad
\det A_-(\mu)=\frac34(\mu-1)^2.
\tag{9}
\]
Hence all modal eigenvalues have negative real part except for a simple zero eigenvalue when \(\mu=1\). At the upper homogeneous equilibrium
\[
P_+=\left(\frac23,2\right),
\]
\[
\operatorname{tr}A_+(\mu)=-\frac83(\mu+3),\qquad
\det A_+(\mu)=\frac{(4\mu+3)^2}{12}>0.
\tag{10}
\]
The source example therefore exhibits a degenerate stationary-pattern resonance: the lower state has a double zero of the dispersion determinant at \(\mu=1\), but there is no open interval of Turing-unstable wavenumbers.

Moreover, the small-amplitude proportional branch opens toward \(L>\pi\). With
\[
q=\frac{U^2}{2},\qquad y=q-\frac18,
\]
the stationary scalar equation near \(P_-\) becomes
\[
y_{xx}+y-14y^2+56y^3+O(y^4)=0.
\tag{11}
\]
A Poincare-Lindstedt expansion with leading harmonic amplitude \(A\) gives the half-period
\[
\ell(A)=\pi\left(1+\frac{182}{3}A^2+O(A^3)\right).
\tag{12}
\]
Thus the nonconstant branch locally lies on the \(L>\pi\) side even though the homogeneous equilibrium is spectrally stable again when the Neumann eigenvalue moves away from the isolated resonance.

## Context

Cherniha and Kriukova study (7) as a porous-Fisher prey-predator system with two stable positive homogeneous equilibria. Their stability analysis is explicitly spatially homogeneous, and they state that the search for nonconstant steady states satisfying zero Neumann conditions and their analysis is beyond the scope of their study. The proportionality identities used in their two-node construction, however, also imply the stationary reduction (3)-(4).

This fills that stated gap for the paper's main concrete example and, under (1)-(2), for a wider proportional family. It also identifies why the example is unusual from the viewpoint of standard Turing analysis: the relevant dispersion determinant touches zero quadratically rather than changing sign.

## Proof

### 1. Exact proportional stationary reduction

Set \(V=\alpha U\). For a stationary profile, the first equation becomes
\[
0=(UU_x)_x+(a_1+\alpha c_1)U-bU^2+h_1.
\tag{13}
\]
The second stationary residual is
\[
\alpha^2(UU_x)_x+(\alpha a_2+c_2)U-b\alpha^2U^2+h_2.
\]
Under (1) this is exactly \(\alpha^2\) times (13). Using (2), (13) is equivalent to (4). Therefore every positive solution of (4) yields a positive stationary solution \((U,\alpha U)\) of the full system.

### 2. Conservative spatial dynamics

Put
\[
p=UU_x.
\]
For \(U>0\), (4) is equivalent to
\[
U_x=\frac{p}{U},\qquad
p_x=b(U-U_-)(U-U_+).
\tag{14}
\]
Define
\[
F(U)=b\left[
\frac{U^4}{4}
-\frac{U_-+U_+}{3}U^3
+\frac{U_-U_+}{2}U^2
\right].
\tag{15}
\]
Since
\[
F'(U)=bU(U-U_-)(U-U_+),
\]
the quantity
\[
H(U,p)=\frac{p^2}{2}-F(U)
\tag{16}
\]
is constant along (14).

The point \((U_-,0)\) is a center of the spatial system and \((U_+,0)\) is a saddle. Linearization at the center gives
\[
u_{xx}+\omega_0^2u=0,\qquad
\omega_0^2=\frac{b(U_+-U_-)}{U_-},
\tag{17}
\]
so the small-amplitude half-period tends to \(L_c=\pi/\omega_0\).

If \(r=U_-/U_+>1/2\), then
\[
F(U_+)=\frac{bU_+^4}{12}(2r-1)>0.
\tag{18}
\]
At the saddle energy \(H_s=-F(U_+)<0\), the left turning point is therefore strictly positive. Indeed
\[
F(U)-F(U_+)
=\frac{bU_+^4}{12}(y-1)^2
\left(3y^2+(2-4r)y+1-2r\right),
\quad y=\frac{U}{U_+},
\tag{19}
\]
and the additional positive root lies in \((0,r)\). Consequently the center is surrounded, within \(U>0\), by a period annulus whose outer boundary is a positive homoclinic loop to \((U_+,0)\).

For an energy \(H\) in this annulus, let \(u_-(H)<U_-<u_+(H)\) be the two turning points. Its half-period is
\[
\ell(H)=
\int_{u_-(H)}^{u_+(H)}
\frac{U\,dU}{\sqrt{2(H+F(U))}}.
\tag{20}
\]
The period depends continuously on \(H\). By (17),
\[
\ell(H)\longrightarrow L_c
\]
as the orbit shrinks to the center. As \(H\) approaches the saddle energy, the orbit spends an unbounded spatial time near the hyperbolic saddle, so
\[
\ell(H)\longrightarrow+\infty.
\]
The intermediate value theorem therefore gives an orbit with \(\ell(H)=L\) for every \(L>L_c\). Starting at one turning point gives \(U_x=0\) at \(x=0\), and the opposite turning point is reached at \(x=L\), giving \(U_x=0\) there as well. Repeating \(m\) half-periods gives the stated profiles whenever \(L/m>L_c\), proving (6).

### 3. Specialization to the source example

For (7), setting \(V=3U\) makes the second stationary equation exactly nine times the first. Equation (4) becomes
\[
(UU_x)_x-3\left(U-\frac12\right)\left(U-\frac23\right)=0.
\tag{21}
\]
Here
\[
F(U)=\frac34U^4-\frac76U^3+\frac12U^2,
\tag{22}
\]
the center energy is \(-5/192\), and the saddle energy is \(-2/81\). At the homoclinic energy,
\[
F(U)-F(2/3)
=\frac{(3U-2)^2(27U^2-6U-2)}{324},
\tag{23}
\]
so the positive lower turning point is
\[
U_*=\frac{1+\sqrt7}{9}>0.
\tag{24}
\]
Equation (17) gives \(\omega_0=1\), hence \(L_c=\pi\).

### 4. Dispersion factorization

At \(P_-=(1/2,3/2)\), the reaction Jacobian and diffusion matrix are
\[
J_-=
\begin{pmatrix}
7/2&-1\\
27&-15/2
\end{pmatrix},
\qquad
D_-=\operatorname{diag}(1/2,3/2).
\]
A Laplacian mode \(-\phi_{xx}=\mu\phi\) is governed by \(A_-(\mu)=J_--\mu D_-\), and direct calculation gives (9).

At \(P_+=(2/3,2)\),
\[
J_+=
\begin{pmatrix}
5/2&-1\\
27&-21/2
\end{pmatrix},
\qquad
D_+=\operatorname{diag}(2/3,2),
\]
which gives (10). Thus \(P_-\) has only an isolated neutral mode at \(\mu=1\), while \(P_+\) is strictly stable for every \(\mu\ge0\).

The double root in (9) is not accidental. In the proportional family, the additional balance
\[
c_2=-c_1\alpha^3
\tag{25}
\]
implies, at the lower proportional equilibrium,
\[
\det(J_--\mu D_-)
=\alpha U_-^2(\mu-\mu_0)^2,
\qquad
\mu_0=\frac{b(U_+-U_-)}{U_-}.
\tag{26}
\]
The source example satisfies (25), and \(\mu_0=1\).

### 5. Direction of the small-amplitude branch

For (21), let \(q=U^2/2\). Since \(q_{xx}=(UU_x)_x\), expansion about \(U=1/2\), equivalently \(q=1/8\), yields (11). For
\[
y_{xx}+y+a y^2+b_3 y^3+O(y^4)=0,
\]
the standard Poincare-Lindstedt calculation gives
\[
\ell(A)=\pi\left[
1+\left(\frac{5a^2}{12}-\frac{3b_3}{8}\right)A^2
+O(A^3)
\right].
\]
With \(a=-14\) and \(b_3=56\), the coefficient is \(182/3>0\), proving (12).

## Scientific significance

The source paper's main example was designed to exhibit two stable positive homogeneous prey-predator states. The same parameter identities contain a hidden stationary reduction that produces positive spatial patterns under pure Neumann confinement. In the concrete example, these patterns are not explained by a conventional diffusion-driven instability interval: the lower homogeneous state has a dispersion determinant that only touches zero at one wavenumber and is stable again on either side. The result therefore supplies an explicit nonlinear steady-pattern mechanism at a degenerate Turing resonance.

## Limitations

- The existence theorem concerns one-dimensional **stationary** profiles and does not establish their temporal stability.
- The \(L>\pi\) statement for (7) uses homogeneous Neumann conditions at both endpoints. It is not a claim about the mixed, time-dependent boundary-value problem used for the source paper's numerical illustrations.
- The proportional reduction gives a distinguished family of steady states; it does not classify every nonconstant steady state of the two-component PDE.
- The general all-\(L>L_c\) conclusion uses \(U_->U_+/2\), which guarantees that the relevant homoclinic loop remains strictly positive.
- No claim is made that nonconstant steady states or Turing bifurcation methods are new in general predator-prey reaction-diffusion theory. The originality claim is limited to the exact proportional reduction, domain-length existence consequence, and degenerate-dispersion mechanism for this model family and the cited concrete example.

## References

1. R. Cherniha and G. Kriukova, *A Reaction-Diffusion System with Nonconstant Diffusion Coefficients: Exact and Numerical Solutions*, Axioms 14 (2025), 655. DOI: 10.3390/axioms14090655. arXiv:2608.11172.
2. Y. Yang and M. Fan, *Bifurcation Analysis of a Predator-Prey Model With Degenerate Diffusion and Multiple Allee Effects in Predators*, Mathematical Methods in the Applied Sciences (2026). DOI: 10.1002/mma.70728.
3. Literature on nonconstant steady states and Turing patterns in other reaction-diffusion predator-prey models was checked as prior art; those results concern different reaction terms and do not supply the proportional reduction or the perfect-square dispersion law above.
