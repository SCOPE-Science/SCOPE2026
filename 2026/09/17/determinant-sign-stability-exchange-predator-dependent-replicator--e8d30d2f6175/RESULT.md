# A determinant-sign proof of stability exchange in the predator-dependent replicator model

## Result

Consider the Cruz--Neves system in variables \((x,P,Y)\):
\[
\dot x=x(1-x)(f_A(x,Y)-f_B(x,Y)),
\]
\[
\dot P=(r(x)-P/K-\delta(x)Y)P,
\qquad
\dot Y=(-\beta+\beta\delta(x)P)Y.
\]
Define
\[
g(x)=f_A(x,0)-f_B(x,0)=(a-c)x+(b-d)(1-x),
\]
\[
h(x)=(a'-c')x+(b'-d')(1-x),
\qquad m(x)=g(x)/h(x),
\]
and
\[
F(x)=r(x)-\delta(x)m(x),
\qquad
\kappa(x)=1/(\delta(x)F(x)).
\]
A positive three-species equilibrium (ABY equilibrium) has
\[
Y=m(x),\qquad P=1/\delta(x),\qquad K=\kappa(x).
\]

Suppose a positive ABY branch meets a positive AY equilibrium at \(x=1\), a positive BY equilibrium at \(x=0\), or an AB equilibrium at the reproduction-balance point \(x=x_R\). Assume the collision is nondegenerate in the source paper's generic sense: the relevant \(\kappa'\) is nonzero, the colliding zero eigenvalue is simple, and at \(x_R\) one has \(h(x_R)\ne0\). Then all three numbered stability assertions in Conjecture 6.2 of Cruz--Neves hold.

At AY and BY collisions, the nearby positive ABY equilibrium has the opposite local stability status from the corresponding boundary equilibrium. Hence stable-to-unstable boundary transitions are accompanied by either annihilation of an unstable ABY equilibrium or creation of a stable one; unstable-to-stable boundary transitions have the reverse alternatives. At an AB collision in the reproduction-coexistence case \(a<c,d<b\), the same exchange holds. In the reproduction-codominance case \(a>c,d>b\), every sufficiently nearby positive ABY equilibrium is unstable.

The result is a stability-exchange theorem. It does **not** assert that these collisions satisfy the standard Sotomayor transcritical nondegeneracy conditions; Cruz--Neves explicitly show that one of those conditions fails.

## Proof

Cruz--Neves calculate, at a positive ABY equilibrium,
\[
\det J=\beta\,\delta(x)F(x)^2x(1-x)g(x)\kappa'(x).
\tag{1}
\]
All factors in (1), except \(g(x)\kappa'(x)\), are positive. Thus
\[
\operatorname{sgn}(\det J)=\operatorname{sgn}(g(x)\kappa'(x)).
\tag{2}
\]

At each collision considered below, the two eigenvalues tangent to the relevant stable two-species subsystem have negative real parts, while the remaining eigenvalue is a simple zero. Therefore, on a nearby ABY branch, two eigenvalues stay in the open left half-plane and there is a unique real eigenvalue \(\lambda_*\) near zero. The product of the two stable eigenvalues is positive, so
\[
\operatorname{sgn}\lambda_* = \operatorname{sgn}(\det J).
\tag{3}
\]

### AY collision

Let \(K_c=K_C^A=\kappa(1)\), \(g_1=a-c\), and \(h_1=a'-c'\). Positivity of the colliding AY equilibrium gives \(m(1)=g_1/h_1>0\), so \(g_1\) and \(h_1\) have the same sign. A positive interior branch has \(x<1\), hence
\[
\operatorname{sgn}(K-K_c)=-\operatorname{sgn}\kappa'(1).
\tag{4}
\]
By (2)--(3),
\[
\operatorname{sgn}\lambda_* = \operatorname{sgn}(h_1\kappa'(1)).
\tag{5}
\]

The B-invasion eigenvalue of the AY equilibrium is
\[
\lambda_B(K)=c-1/(Ka')-c'Y_A(K),
\qquad
Y_A(K)=\bigl(a-1/(Ka')\bigr)/a'.
\]
At \(K=K_c\), \(\lambda_B=0\), and
\[
\lambda_B'(K_c)=(a'-c')/(a'^2K_c^2)=h_1/(a'^2K_c^2).
\]
Using (4), for the side containing the positive ABY branch,
\[
\operatorname{sgn}\lambda_B
=-\operatorname{sgn}(h_1\kappa'(1))
=-\operatorname{sgn}\lambda_*.
\tag{6}
\]
Thus AY and nearby ABY equilibria have opposite stability. The creation/annihilation alternatives are determined by the sign of \(\kappa'(1)\), giving precisely the AY assertions of Conjecture 6.2.

### BY collision

Let \(K_c=K_C^B=\kappa(0)\), \(g_0=b-d\), and \(h_0=b'-d'\). Positivity gives \(g_0/h_0>0\). The positive interior branch has \(x>0\), so
\[
\operatorname{sgn}(K-K_c)=\operatorname{sgn}\kappa'(0),
\qquad
\operatorname{sgn}\lambda_* = \operatorname{sgn}(h_0\kappa'(0)).
\tag{7}
\]
The A-invasion eigenvalue of BY is
\[
\lambda_A(K)=b-1/(Kd')-b'Y_B(K),
\qquad
Y_B(K)=\bigl(d-1/(Kd')\bigr)/d',
\]
and
\[
\lambda_A'(K_c)=-(b'-d')/(d'^2K_c^2)=-h_0/(d'^2K_c^2).
\]
Consequently,
\[
\operatorname{sgn}\lambda_A=-\operatorname{sgn}\lambda_*.
\tag{8}
\]
This proves the two BY alternatives of the conjecture.

### AB collision

At \(x=x_R\), one has \(g(x_R)=0\), hence \(m(x_R)=0\), and the boundary equilibrium is predator-free. Since \(F(x_R)=r(x_R)\), its predator-invasion eigenvalue is
\[
\lambda_Y(K)=\beta\bigl(K/K_c-1\bigr),
\qquad K_c=\kappa(x_R),
\tag{9}
\]
so \(\operatorname{sgn}\lambda_Y=\operatorname{sgn}(K-K_c)\).

First assume reproduction coexistence: \(a<c,d<b\). Then \(g(0)=b-d>0\), \(g(1)=a-c<0\), so the affine function \(g\) has negative slope. Put \(h_R=h(x_R)\ne0\). On a positive ABY branch, \(m=g/h>0\), hence close to \(x_R\)
\[
\operatorname{sgn}g(x)=\operatorname{sgn}h_R,
\qquad
\operatorname{sgn}(x-x_R)=-\operatorname{sgn}h_R.
\tag{10}
\]
Therefore
\[
\operatorname{sgn}(K-K_c)
=-\operatorname{sgn}(h_R\kappa'(x_R)),
\]
whereas (2)--(3) give
\[
\operatorname{sgn}\lambda_*
=\operatorname{sgn}(h_R\kappa'(x_R))
=-\operatorname{sgn}\lambda_Y.
\tag{11}
\]
The AB equilibrium is asymptotically stable in the prey plane in this regime, so its other two eigenvalues remain in the left half-plane. This proves the AB stability exchange in the coexistence case.

Now assume reproduction codominance: \(a>c,d>b\). Cruz--Neves show that the AB equilibrium is already unstable in the predator-free prey plane. At the collision it therefore has a strictly positive prey-plane eigenvalue. Spectral continuity preserves that positive eigenvalue on every sufficiently nearby positive ABY branch, so the ABY equilibrium is unstable. This proves the third numbered assertion of Conjecture 6.2.

Thus the conjectured local stability conclusions follow without a standard transcritical normal-form argument. \(\square\)

## Interpretation

The source paper's failed Sotomayor condition does not obstruct stability exchange because the required local information is already contained in the exact ABY determinant and the one-dimensional invasion eigenvalue of the boundary equilibrium. The two remaining spectral directions are separated from the imaginary axis, so a sign comparison replaces the missing normal-form calculation.

The result is deliberately local. Farther along an ABY branch, the separated spectral pair can itself reach the imaginary axis; Cruz--Neves report numerical evidence of such Hopf-type losses of stability in some examples.

## Limitations

- The theorem is local near nondegenerate boundary collisions and does not classify ABY stability far from the collision.
- It does not prove that the collision is a standard transcritical bifurcation.
- Cases with \(\kappa'=0\) at the collision, \(h(x_R)=0\), or additional zero eigenvalues require separate analysis.
- The result concerns local equilibrium stability; it does not establish global convergence or exclude periodic or more complicated invariant sets.

## Relation to the literature and originality scope

Cruz and Neves explicitly formulate this stability behavior as Conjecture 6.2 and state that proving it is a future-work problem. Their determinant identity (43), their AY/BY/AB stability theorems, and the positivity structure of the ABY branch are inputs to the proof above. Searches by exact title, arXiv identifier, conjecture number, author names, stability-exchange terminology, and transcritical/Sotomayor terminology did not locate a later proof or correction covering the conjecture.

Continuity of eigenvalues, determinant-as-product, and invasion-eigenvalue stability tests are standard and are not claimed as new. The originality claim is the source-specific determinant-sign argument proving the numbered assertions of Conjecture 6.2, to the best of our knowledge.

## References

1. H. M. Cruz and A. G. M. Neves, *Predator-dependent replicator dynamics or a predator-prey model with two prey types and frequency dependence*, arXiv:2607.13281 (2026). https://arxiv.org/abs/2607.13281
2. J. Sotomayor, *Generic bifurcations of dynamical systems*, in M. M. Peixoto (ed.), *Dynamical Systems*, Academic Press (1973), 549--560.
