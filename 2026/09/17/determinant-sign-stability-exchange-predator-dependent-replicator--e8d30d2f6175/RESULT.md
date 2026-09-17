# A determinant-sign proof of stability exchange in the predator-dependent replicator model

## Result

Consider the three-dimensional reformulation of the Cruz--Neves predator-dependent replicator model
\[
\begin{aligned}
\dot x&=x(1-x)\bigl(f_A(x,Y)-f_B(x,Y)\bigr),\\
\dot P&=\left(r(x)-\frac{P}{K}-\delta(x)Y\right)P,\\
\dot Y&=\bigl(-\beta+\beta\delta(x)P\bigr)Y,
\end{aligned}
\]
with all source-model parameters positive. Write
\[
g(x)=f_A(x,0)-f_B(x,0)
=(a-c)x+(b-d)(1-x),
\]
\[
h(x)=(a'-c')x+(b'-d')(1-x),
\qquad m(x)=\frac{g(x)}{h(x)},
\]
and, where defined,
\[
F(x)=r(x)-\delta(x)m(x),
\qquad
\kappa(x)=\frac{1}{\delta(x)F(x)}.
\]
A positive three-species equilibrium (ABY equilibrium) has
\[
Y=m(x),\qquad P=\frac1{\delta(x)},\qquad K=\kappa(x).
\]

Suppose a positive ABY branch meets a positive AY equilibrium at \(x=1\), a positive BY equilibrium at \(x=0\), or an AB equilibrium at the reproduction-balance point \(x=x_R\). Assume the collision is nondegenerate in the source paper's generic sense: the relevant \(\kappa'\) is nonzero, the colliding zero eigenvalue is simple, and at \(x_R\) one has \(h(x_R)\ne0\). Then the stability conclusions of Conjecture 6.2 of Cruz--Neves hold.

More explicitly:

1. At an AY or BY collision, the nearby positive ABY equilibrium has the opposite local stability status from the nearby boundary equilibrium on the side where both are compared. Consequently, if the boundary equilibrium changes stable-to-unstable as \(K\) increases, an ABY equilibrium annihilated there is unstable whereas one created there is stable. If the boundary equilibrium changes unstable-to-stable, an ABY equilibrium annihilated there is stable whereas one created there is unstable.
2. At an AB collision in the reproduction-coexistence case \(a<c\), \(d<b\), the same exchange holds: the AB equilibrium is stable for \(K<\kappa(x_R)\) and unstable for larger \(K\), while a nearby positive ABY equilibrium has the opposite stability on its side of the collision.
3. In the reproduction-codominance case \(a>c\), \(d>b\), the AB equilibrium already has an unstable prey-plane direction. That unstable eigenvalue persists on every sufficiently nearby positive ABY branch, so the nearby ABY equilibrium is unstable. This proves the third numbered assertion of Conjecture 6.2.

The conclusion is a stability-exchange theorem; it does **not** assert that the collisions satisfy the standard Sotomayor transcritical nondegeneracy conditions. Cruz--Neves explicitly observe that one of those conditions fails.

## Proof

Cruz--Neves calculate the determinant of the Jacobian at a positive ABY equilibrium as
\[
\det J
=
\beta\,\delta(x)F(x)^2x(1-x)g(x)\kappa'(x).
\tag{1}
\]
Along a positive ABY branch all factors in (1), except \(g(x)\kappa'(x)\), are positive. Hence
\[
\operatorname{sgn}(\det J)=\operatorname{sgn}\bigl(g(x)\kappa'(x)\bigr).
\tag{2}
\]

At a boundary collision relevant below, the two eigenvalues tangent to the corresponding positive two-species subsystem have negative real parts whenever that subsystem is asymptotically stable. The remaining eigenvalue is zero at the collision and is simple under the stated genericity assumptions. Therefore, for nearby ABY equilibria, two eigenvalues remain in the open left half-plane and there is a unique real eigenvalue \(\lambda_*\) near zero. The product of the two stable eigenvalues is positive (either two negative real numbers or a complex-conjugate pair), so
\[
\operatorname{sgn}\lambda_*=\operatorname{sgn}(\det J).
\tag{3}
\]
Thus the sign of (1) determines stability of the nearby ABY branch.

### Collision with AY at \(x=1\)

Let
\[
K_c=K_C^A=\kappa(1),
\qquad
g_1=g(1)=a-c,
\qquad h_1=h(1)=a'-c'.
\]
The colliding AY equilibrium is positive, so \(m(1)=g_1/h_1>0\); hence
\[
\operatorname{sgn}g_1=\operatorname{sgn}h_1.
\tag{4}
\]
A positive interior branch has \(x<1\). Since \(\kappa'(1)\ne0\),
\[
\operatorname{sgn}(K-K_c)
=-\operatorname{sgn}\kappa'(1)
\tag{5}
\]
for \(x\) sufficiently close to 1 on that branch. Equation (2) gives
\[
\operatorname{sgn}\lambda_*
=\operatorname{sgn}\bigl(h_1\kappa'(1)\bigr).
\tag{6}
\]

The eigenvalue of the AY equilibrium corresponding to invasion by rare B prey is its B per-capita growth rate,
\[
\lambda_B(K)=c-\frac{1}{Ka'}-c'Y_A(K),
\qquad
Y_A(K)=\frac1{a'}\left(a-\frac1{Ka'}\right).
\]
At \(K=K_c\), \(\lambda_B=0\), and
\[
\lambda_B'(K_c)=\frac{a'-c'}{a'^2K_c^2}=rac{h_1}{a'^2K_c^2}.
\]
Combining this with (5),
\[
\operatorname{sgn}\lambda_B
=-\operatorname{sgn}\bigl(h_1\kappa'(1)\bigr)
=-\operatorname{sgn}\lambda_*.
\tag{7}
\]
Hence the AY and nearby ABY equilibria have opposite stability status. The creation/annihilation alternatives in Conjecture 6.2 follow directly from the sign of \(\kappa'(1)\).

### Collision with BY at \(x=0\)

Let
\[
K_c=K_C^B=\kappa(0),
\qquad g_0=b-d,
\qquad h_0=b'-d'.
\]
Again positivity of the collision gives \(g_0/h_0>0\), hence \(\operatorname{sgn}g_0=\operatorname{sgn}h_0\). The positive interior branch has \(x>0\), so
\[
\operatorname{sgn}(K-K_c)=\operatorname{sgn}\kappa'(0).
\tag{8}
\]
Equation (2) therefore gives
\[
\operatorname{sgn}\lambda_*
=\operatorname{sgn}\bigl(h_0\kappa'(0)\bigr).
\tag{9}
\]

The A-invasion eigenvalue at the BY equilibrium is
\[
\lambda_A(K)=b-\frac{1}{Kd'}-b'Y_B(K),
\qquad
Y_B(K)=\frac1{d'}\left(d-\frac1{Kd'}\right),
\]
so at the collision
\[
\lambda_A'(K_c)
=-\frac{b'-d'}{d'^2K_c^2}
=-\frac{h_0}{d'^2K_c^2}.
\]
Using (8),
\[
\operatorname{sgn}\lambda_A
=-\operatorname{sgn}\bigl(h_0\kappa'(0)\bigr)
=-\operatorname{sgn}\lambda_*.
\tag{10}
\]
Thus the BY and nearby ABY equilibria also have opposite stability status, proving both BY alternatives in the conjecture.

### Collision with AB at \(x=x_R\)

At the reproduction-balance point \(x_R\), one has \(g(x_R)=0\) and therefore \(m(x_R)=0\). The boundary equilibrium is predator-free. Its predator-invasion eigenvalue is
\[
\lambda_Y(K)
=
\beta\bigl(-1+\delta(x_R)K r(x_R)\bigr)
=
\beta\left(\frac{K}{K_c}-1\right),
\qquad
K_c=\kappa(x_R),
\tag{11}
\]
because \(F(x_R)=r(x_R)\). Hence
\[
\operatorname{sgn}\lambda_Y=\operatorname{sgn}(K-K_c).
\tag{12}
\]

First consider reproduction coexistence, \(a<c\) and \(d<b\). Then
\[
g(0)=b-d>0,\qquad g(1)=a-c<0,
\]
so the affine function \(g\) has \(g'(x)<0\). Put \(h_R=h(x_R)\ne0\). On a positive ABY branch, \(m=g/h>0\); close to \(x_R\), this forces
\[
\operatorname{sgn}g(x)=\operatorname{sgn}h_R,
\qquad
\operatorname{sgn}(x-x_R)=-\operatorname{sgn}h_R.
\tag{13}
\]
Therefore
\[
\operatorname{sgn}(K-K_c)
=-\operatorname{sgn}\bigl(h_R\kappa'(x_R)\bigr),
\tag{14}
\]
whereas (2) gives
\[
\operatorname{sgn}\lambda_*
=\operatorname{sgn}\bigl(h_R\kappa'(x_R)\bigr)
=-\operatorname{sgn}(K-K_c)
=-\operatorname{sgn}\lambda_Y.
\tag{15}
\]
The AB equilibrium is asymptotically stable in the prey plane in this reproduction regime, so the other two eigenvalues remain in the left half-plane. Equations (12)--(15) prove the claimed stability exchange.

Finally consider reproduction codominance, \(a>c\), \(d>b\). Cruz--Neves show that the AB equilibrium is unstable already in the predator-free prey plane. At the collision this gives a strictly positive prey-plane eigenvalue. Eigenvalues depend continuously on the equilibrium and parameters, so this positive eigenvalue persists on every sufficiently nearby positive ABY branch. Hence such ABY equilibria are unstable, proving the third assertion of Conjecture 6.2.

This proves all three numbered statements of the conjecture under the explicit generic nondegeneracy assumptions above. \(\square\)

## Interpretation

The failed Sotomayor condition does not prevent stability exchange here because the needed information is already encoded in two simpler structures: the sign of the exact ABY determinant formula and the one-dimensional invasion eigenvalue of the boundary equilibrium. Near each collision, the other spectral directions are separated from the imaginary axis. The sign comparison therefore replaces a full transcritical normal-form calculation.

This also explains why stability conclusions are only local in \(K\). Farther along an ABY branch, the separated pair can itself reach the imaginary axis; Cruz--Neves report numerical evidence of precisely such Hopf-type losses of stability in some examples.

## Limitations

- The theorem is local near nondegenerate boundary collisions. It does not classify ABY stability far from the collision.
- It does not prove that the collision is a standard transcritical bifurcation; the source paper's observation that a standard Sotomayor condition fails is left intact.
- Degenerate cases such as \(\kappa'=0\) at the collision, \(h(x_R)=0\) (coincident zeros of numerator and denominator of \(m\)), or additional zero eigenvalues require separate analysis.
- The result concerns local equilibrium stability. It does not establish global convergence or exclude periodic or more complicated invariant sets.

## Relation to the literature and originality scope

Cruz and Neves explicitly formulate the above stability-exchange behavior as Conjecture 6.2 and state in their conclusions that proving it is a future-work problem. Their determinant identity (43), their stability theorems for AY/BY/AB equilibria, and the positivity structure of the ABY branch are the inputs to the proof above. Searches by exact title, arXiv identifier, conjecture number, stability-exchange terminology, transcritical/Sotomayor terminology, and author names did not locate a later proof or correction covering the conjecture.

The generic facts used here---continuity of eigenvalues, determinant as the eigenvalue product, and invasion-eigenvalue stability tests---are standard and are not claimed as new. The originality claim is the source-specific determinant-sign proof and the resulting proof of the numbered assertions of Conjecture 6.2, to the best of our knowledge.

## References

1. H. M. Cruz and A. G. M. Neves, *Predator-dependent replicator dynamics or a predator-prey model with two prey types and frequency dependence*, arXiv:2607.13281 (2026). https://arxiv.org/abs/2607.13281
2. J. Sotomayor, *Generic bifurcations of dynamical systems*, in M. M. Peixoto (ed.), *Dynamical Systems*, Academic Press (1973), 549--560.

**Same-model review: passed. Cross-model review: not yet performed.**