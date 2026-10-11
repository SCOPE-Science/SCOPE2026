# Sharp transverse derivative and optimality of the harmonic Landau shear

## Finding

Let
\[
u:\mathbb D\to(-1,1)
\]
be real harmonic and satisfy
\[
u(0)=0,
\qquad
\nabla u(0)=0.
\]
Then, for every
\[
0<r<1,
\]
the transverse derivative on the positive real axis satisfies the sharp inequality
\[
|u_y(r,0)|
\le
\frac{8r}{\pi(1-r^4)}.
\]

Equality is attained, up to sign, by
\[
u_*(z)
=
\frac{2}{\pi}
\operatorname{Arg}
\left(
\frac{1-z^2}{1+z^2}
\right).
\]
This is exactly the bounded real harmonic perturbation used in the 2026 counterexample to the Liu--Luo--Luo harmonic Landau conjecture.

For
\[
F_{M,u}(z)
=
z+i(M-1)u(z),
\qquad
M>1,
\]
the earliest possible Jacobian zero on the positive real axis is therefore the unique radius
\[
r_M\in(0,1)
\]
satisfying
\[
8(M-1)r_M
=
\pi(1-r_M^4).
\]
The source perturbation \(u_*\) attains this lower bound on the fold radius.

The exact threshold for this optimal shear fold to occur strictly inside the classical holomorphic Landau disk is
\[
M_{\mathrm{shear}}
=
4.4487630197851664455692236305\ldots.
\]
Equivalently,
\[
r_M<r_0(M)
\quad\Longleftrightarrow\quad
M>M_{\mathrm{shear}},
\]
where
\[
r_0(M)
=
\frac{1}{M+\sqrt{M^2-1}}.
\]

If \(\rho_*\) denotes the unique zero in \((0,1)\) of
\[
\pi\rho^3+\pi\rho^2+(\pi+4)\rho+\pi-4=0,
\]
then
\[
\rho_*
=
0.1138475181625531267398612878\ldots
\]
and
\[
M_{\mathrm{shear}}
=
\frac{1+\rho_*^2}{2\rho_*}.
\]

## Assumptions and scope

The class considered in the sharpness statement consists of vertical harmonic shears
\[
F_{M,u}(x+iy)
=
x+i\bigl(y+(M-1)u(x,y)\bigr)
\]
with
\[
|u|<1,
\qquad
u(0)=0,
\qquad
\nabla u(0)=0.
\]
These conditions imply
\[
F_{M,u}(0)=0,
\qquad
\lambda_{F_{M,u}}(0)=1,
\qquad
|F_{M,u}(z)|<M.
\]

The claim is an optimality theorem for the positive-real-axis fold mechanism in this vertical-shear class. It does not assert that every harmonic Landau counterexample must be a vertical shear, nor does it rule out an earlier nonreal Jacobian zero for some other perturbation.

The derivative inequality itself is a sharp statement about real bounded harmonic functions with a vanishing first jet at the origin.

## Proof

Fix
\[
0<r<1.
\]
A bounded real harmonic function has an essentially bounded boundary trace
\[
\varphi
\]
with
\[
|\varphi|\le1
\]
and Poisson representation. Write its boundary Fourier coefficients as
\[
\varphi(t)
=
\frac{a_0}{2}
+
\sum_{n\ge1}
\bigl(
a_n\cos nt+b_n\sin nt
\bigr).
\]
The conditions
\[
u(0)=0,
\qquad
\nabla u(0)=0
\]
give
\[
a_0=a_1=b_1=0.
\]

On the positive real axis,
\[
u_y(r,0)
=
\sum_{n\ge2}
n b_n r^{n-1}.
\]
Since \(b_1=0\), the missing first harmonic can be restored inside the integral:
\[
u_y(r,0)
=
\frac1\pi
\int_{-\pi}^{\pi}
\varphi(t)
K_r(t)\,dt,
\]
where
\[
K_r(t)
=
\sum_{n\ge1}
n r^{n-1}\sin(nt)
=
\frac{
(1-r^2)\sin t
}{
(1-2r\cos t+r^2)^2
}.
\]

Only the odd part
\[
\psi(t)
=
\frac{\varphi(t)-\varphi(-t)}2
\]
contributes to this integral. It still satisfies
\[
|\psi|\le1
\]
and, because \(b_1=0\),
\[
\int_0^\pi
\psi(t)\sin t\,dt
=
0.
\]
Define
\[
H_r(x)
=
\frac{1-r^2}{(1-2rx+r^2)^2}.
\]
This is strictly increasing in \(x\in[-1,1]\). Hence, for
\[
\lambda_r=H_r(0),
\]
\[
\begin{aligned}
u_y(r,0)
&=
\frac2\pi
\int_0^\pi
\psi(t)\sin t
\bigl(
H_r(\cos t)-\lambda_r
\bigr)\,dt\\
&\le
\frac2\pi
\int_0^\pi
\sin t
\left|
H_r(\cos t)-H_r(0)
\right|\,dt.
\end{aligned}
\]
The same estimate applied to \(-u\) controls the absolute value.

Since \(H_r\) is increasing, the absolute value changes sign exactly at
\[
t=\frac{\pi}{2}.
\]
With
\[
x=\cos t,
\]
the last integral equals
\[
\frac2\pi
\left(
\int_0^1H_r(x)\,dx
-
\int_{-1}^0H_r(x)\,dx
\right).
\]
Using
\[
\int
H_r(x)\,dx
=
\frac{1-r^2}{2r}
\frac1{1-2rx+r^2},
\]
one obtains
\[
|u_y(r,0)|
\le
\frac{8r}{\pi(1-r^4)}.
\]

Equality requires the odd boundary trace to agree almost everywhere with the sign of
\[
H_r(\cos t)-H_r(0).
\]
Because the threshold is always \(t=\pi/2\), one common extremal for every radius is
\[
\varphi_*(t)
=
-\operatorname{sgn}(\sin2t).
\]
Its Poisson integral is
\[
u_*(z)
=
\frac{2}{\pi}
\operatorname{Arg}
\left(
\frac{1-z^2}{1+z^2}
\right),
\]
and direct differentiation gives
\[
(u_*)_y(r,0)
=
-\frac{8r}{\pi(1-r^4)}.
\]
Thus the derivative constant is sharp simultaneously for all \(r\).

For the vertical shear
\[
F_{M,u}(x+iy)
=
x+i\bigl(y+(M-1)u(x,y)\bigr),
\]
the Jacobian is
\[
J_{F_{M,u}}(x,y)
=
1+(M-1)u_y(x,y).
\]
If a positive-real-axis fold occurs at \(r\), then
\[
-u_y(r,0)
=
\frac1{M-1}.
\]
The sharp derivative estimate forces
\[
\frac1{M-1}
\le
\frac{8r}{\pi(1-r^4)}.
\]
The right-hand side is strictly increasing in \(r\). Hence
\[
r\ge r_M,
\]
where \(r_M\) is the unique solution of
\[
8(M-1)r_M
=
\pi(1-r_M^4).
\]
For \(u=u_*\), equality holds and the fold occurs exactly at \(r_M\). This proves optimality within the stated shear class.

It remains to locate exactly when this optimal fold lies inside the holomorphic Landau disk. The inverse relation for
\[
r_0(M)
=
M-\sqrt{M^2-1}
\]
is
\[
M
=
\frac{1+r_0^2}{2r_0}.
\]
At equality
\[
r_M=r_0(M)=\rho,
\]
the two expressions for \(M\) give
\[
1+\frac{\pi(1-\rho^4)}{8\rho}
=
\frac{1+\rho^2}{2\rho}.
\]
Equivalently,
\[
(\rho-1)
\left(
\pi\rho^3+\pi\rho^2+(\pi+4)\rho+\pi-4
\right)
=
0.
\]
On \((0,1)\), the cubic factor is strictly increasing, negative at \(0\), and positive at \(1\). Hence it has a unique root
\[
\rho_*.
\]
Since the shear parameter
\[
1+\frac{\pi(1-\rho^4)}{8\rho}
\]
strictly decreases with \(\rho\), the comparison is
\[
r_M<r_0(M)
\quad\Longleftrightarrow\quad
M>
\frac{1+\rho_*^2}{2\rho_*}.
\]
This is the stated \(M_{\mathrm{shear}}\).

## Verification

The full 2026 primary manuscript was checked at the definition of
\[
u_*,
\]
the vertical shear \(F_M\), the Jacobian identity, the equation defining \(r_M\), and the source's sufficient comparison with the holomorphic Landau radius.

The derivative theorem above is independently reconstructed from the Poisson/Fourier representation. The optimization uses the vanishing first sine moment, not a numerical search. The extremal trace
\[
-\operatorname{sgn}(\sin2t)
\]
is exactly the boundary trace of the source's \(u_*\).

The packaged checker verifies symbolically the kernel sum, the integral giving
\[
\frac{8r}{\pi(1-r^4)},
\]
the source derivative formula, and the factorization of the exact threshold equation. It numerically evaluates the uniquely characterized cubic root and threshold only after the analytic uniqueness proof.

## Relationship to prior work

Borovikov's 2026 paper constructs \(u_*\) and proves that its fold radius \(r_M\) lies inside the classical holomorphic Landau disk for the sufficient range
\[
M>M^*
=
\frac{
16-2\pi+\pi^{3/2}
}{
4(4-\pi)
}
=
4.4515994514\ldots.
\]
The proof replaces the exact fold radius by the simpler upper bound
\[
r_M
<
\frac{\pi}{8(M-1)}.
\]
The present result does two different things: it proves that \(u_*\) is extremal for transverse derivative among all bounded real harmonic perturbations with zero first jet, and it computes the exact threshold of the resulting shear mechanism.

Classical harmonic Schwarz--Pick estimates give sharp bounds such as
\[
|\nabla u(z)|
\le
\frac4\pi
\frac{1-|u(z)|^2}{1-|z|^2},
\]
but do not incorporate the extra condition
\[
\nabla u(0)=0
\]
or identify the sharper transverse constant above.

Work on harmonic mappings having a zero of higher order studies sense-preserving disk self-mappings and value or boundary-derivative estimates. Those hypotheses do not cover a real-valued harmonic perturbation into an interval, which is rank one rather than sense-preserving.

Targeted searches for the source, the exact threshold, bounded-harmonic zero-first-jet derivative estimates, and vertical-shear optimality did not locate a published statement implying this result.

## Limitations

The optimality is restricted to vertical shears with a bounded real perturbation and vanishing first jet.

The theorem controls the first positive-real-axis fold. A different harmonic construction could fail local univalence at a nonreal point or outside this shear architecture for a smaller value of \(M\).

The numerical decimal for \(M_{\mathrm{shear}}\) is only a display value; the exact definition is the unique cubic-root formula above.

## References

1. M. Borovikov, *A Counterexample to the Liu--Luo--Luo Conjecture on the Harmonic Landau Radius*, arXiv:2609.39676v1, 2026.
2. R. Kargar, *On Harnack inequality and harmonic Schwarz lemma*, Canadian Mathematical Bulletin 67 (2024), 1084--1098. DOI: 10.4153/S0008439524000298.
3. X.-J. Bai, J. Huang and J.-F. Zhu, *Boundary Schwarz lemma for harmonic mappings having zero of order \(p\)*, Bulletin of the Malaysian Mathematical Sciences Society 44 (2021), 2331--2340. DOI: 10.1007/s40840-020-00980-1.
4. F. Colonna, *The Bloch constant of bounded harmonic mappings*, Indiana University Mathematics Journal 38 (1989), 829--840.
5. D. Kalaj and M. Vuorinen, *On harmonic functions and the Schwarz lemma*, Proceedings of the American Mathematical Society 140 (2012), 161--165.
