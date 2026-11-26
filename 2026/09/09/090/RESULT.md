# Exact squeezing at the origin of the type-4 Thullen ellipsoid

Let \(E=\{(z_1,z_2)\in\mathbb C^2:|z_1|^2+|z_2|^4<1\}\), and let \(B^2\) denote the Euclidean unit ball. The squeezing function at the origin is the supremum of the radii \(r>0\) such that an injective holomorphic \(f:E\to B^2\) satisfies \(f(0)=0\) and \(B(0,r)\subset f(E)\). Then

\[
s_E(0)=\frac{2}{\sqrt5}>\frac1{\sqrt2}.
\]

The supremum is attained by the scalar map \(f(z)=2z/\sqrt5\).

## Proof

The domain is bounded, balanced and convex, with Minkowski norm \(m\). The infinitesimal Kobayashi metric of \(E\) at 0 is \(K_E(0,v)=m(v)\): the upper bound comes from the linear disc in direction \(v\), and the lower bound from applying Schwarz's lemma to a complex Hahn–Banach functional \(\ell\) with \(\ell(v)=m(v)\) and \(|\ell|\le m\). (The zero vector is immediate.)

For an admissible \(f\), set \(A=df_0\). Biholomorphic invariance on \(f(E)\) and monotonicity for \(B(0,r)\subset f(E)\subset B^2\) give
\[
   |Av|\le m(v)\le |Av|/r.
\]
In particular, \(|Ae_i|\ge r\) for both coordinate unit vectors. The boundary points \(v_\pm=(\sqrt3/2,\pm1/\sqrt2)\) satisfy \(m(v_\pm)=1\), so averaging their image squared norms cancels the cross terms and gives
\[
1\ge\tfrac34 |Ae_1|^2+\tfrac12 |Ae_2|^2\ge\tfrac54 r^2.
\]
Thus every admissible radius is at most \(2/\sqrt5\), without restricting the original embeddings to be linear.

For the lower bound, \(B^2\subset E\), since \(|z_2|^4\le |z_2|^2\) in the unit ball. On \(E\), with \(x=|z_1|^2\) and \(y=|z_2|^2\), we have \(x+y=(x+y^2)+(y-y^2)<1+1/4=5/4\). Hence \((2/\sqrt5)E\subset B^2\) and contains \(B(0,2/\sqrt5)\).

## Boundary type and scope

The smooth defining function \(\rho=|z_1|^2+|z_2|^4-1\) has Levi form \(|v_1|^2+4|z_2|^2|v_2|^2\). The boundary is strongly pseudoconvex away from \(\{z_2=0\}\). At a weak point we can rotate to \((1,0)\). Write a nonconstant holomorphic curve there as \((1+u,v)\). With \(a=\operatorname{ord}u\), \(b=\operatorname{ord}v\) and order of the identically zero function taken as infinity, the vanishing order of \(2\Re u+|u|^2+|v|^4\) is \(\min(a,4b)\): even at a tie the pure and mixed lowest monomials cannot cancel. Dividing by \(\min(a,b)\) gives at most 4, attained by \((1,\zeta)\). Thus the weak points have D'Angelo type 4, including singular-curve tests.

This result concerns ordinary squeezing at the interior origin, not a boundary limit, a formula on all of \(E\), or a uniform lower bound for a class of type-4 domains. It rules out \(1/\sqrt2\) as the exact value at this point. The analytic proof does not depend on the finite sample checks in `artifacts/scaling_check.py`.

## Related extremal problems

Deng–Guan–Zhang (arXiv:1109.3920, Remark 7.2) compare squeezing with maximizing the modulus of the complex Jacobian at the origin and mention Ma's solution for generalized ellipsoids. The two optimizations differ here. In Ma's notation the two blocks have dimensions \(1,1\) and powers \(m=(1,2)\). Proposition 3.4 and Theorem 3.11 give squared diagonal coefficients \(3/4,\sqrt3/2\) for a Jacobian extremal map into \(B^2\). Its image misses points on the first axis at radius \(\sqrt3/2\), strictly below \(2/\sqrt5\). See D. W. Ma, *Carathéodory extremal maps of ellipsoids*, J. Math. Soc. Japan 49 (1997), 723–739, DOI: 10.2969/jmsj/04940723.
