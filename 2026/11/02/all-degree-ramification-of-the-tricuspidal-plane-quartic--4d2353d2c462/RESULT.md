# All-degree ramification of the tricuspidal plane quartic

## Finding
Let \(C\subset\mathbb P^2_{\mathbb C}\) be the integral three-cusped quartic
\[
X^2Y^2+X^2Z^2+Y^2Z^2-2XYZ(X+Y+Z)=0,
\]
with normalization \(\nu:\mathbb P^1\to C\) given by
\[
\nu([s:t])=[s^2t^2:t^2(s-t)^2:s^2(s-t)^2].
\]
For every integer \(m\ge2\), let \(V_m\subset H^0(\mathbb P^1,\mathcal O(4m))\) be the pullback of all degree-\(m\) plane forms, modulo forms vanishing identically on \(C\). It is a base-point-free linear series of dimension \(4m-2\). Its **complete ramification divisor** is
\[
\boxed{\mathcal R(V_m)=(4m-3)\bigl([0:1]+[1:1]+[1:0]\bigr)+[-1:1]+[2:1]+[1:2].}
\]
Equivalently, its homogeneous Wronskian is, up to a nonzero scalar,
\[
\boxed{\operatorname{Wr}(V_m)\doteq s^{4m-3}t^{4m-3}(s-t)^{4m-3}(s+t)(s-2t)(2s-t).}
\]
Thus **exactly three smooth points** are ramification points of the degree-\(m\) plane linear system, **each with weight one for every \(m\ge2\)**. Their images on \(C\) are \([1:4:4]\), \([4:1:4]\), and \([4:4:1]\). All other ramification is concentrated at the three cusps, each of weight \(4m-3\). The case \(m=2\) has a previously known unrefined count of three sextactic points; the contribution here is the all-degree exact divisor, locations, multiplicities, and persistence.

## Assumptions and scope
The ground field is \(\mathbb C\); \(m\) is an arbitrary integer at least two. The divisor is computed **on the normalization** \(\mathbb P^1\), using the possibly incomplete linear system \(V_m=\nu^*H^0(C,\mathcal O_C(m))\subset H^0(\mathbb P^1,\mathcal O(4m))\). It is not a canonical pluricanonical Weierstrass divisor of the singular plane curve. Ramification weight is the sum of deviations of the vanishing sequence from \(0,1,\ldots,\dim V_m-1\). A smooth point is ramified iff a degree-\(m\) plane curve has local intersection multiplicity at least \(4m-2\). For \(m=1\) the separate ramification divisor consists only of the three cusp preimages, each with weight two.

## Proof
**1. The normalization and the three cusps.** In the chart \(t=1\), write \(u=s/t\); the coordinate functions become \(X(u)=u^2\), \(Y(u)=(u-1)^2\), \(Z(u)=u^2(u-1)^2\). Substitution verifies the defining quartic equation. Since \(Z/X=(u-1)^2\) and \(Z/Y=u^2\), equality of two generic image points forces \(u=v\) in characteristic zero: the simultaneous equations \(u^2=v^2\) and \((u-1)^2=(v-1)^2\) have only \(u=v\). The morphism is consequently birational and, being finite, is the normalization. At \(u=0\), in a local affine chart one has the generators \(u^2\) and \(u^2/(1-u)^2\); their difference has order three with nonzero leading coefficient. This gives the completed local ring \(\mathbb C[[u^2,u^3]]\) and an ordinary \(A_2\) cusp. Coordinate permutations show the same at \(u=1\) and \(u=\infty\). The plane-quartic arithmetic genus is three; these three cusps contribute total delta invariant three, so the curve has no further singularities.

**2. Three exact first-jet conditions.** Put \(D=4m\). The exact sequence for the degree-four plane equation gives
\[
\dim V_m=\binom{m+2}{2}-\binom{m-2}{2}=4m-2\quad(m\ge4),
\]
with the same equality for \(m=2,3\) using the first binomial term alone. Pullback to the normalization is injective. Let \(F(u)=\sum_{j=0}^{D}a_ju^j\) represent a section in the \(t=1\) trivialization. The ordinary-cusp condition says that a regular function in the local ring of \(C\) has no first-order term when lifted to its normalization. Applying this at the three preimages, respectively using \(Y^m\), \(X^m\), and \(Z^m\) as nonvanishing local trivializations, yields
\[
F'(0)+2mF(0)=0,\qquad F'(1)-2mF(1)=0,\qquad a_{D-1}+2ma_D=0.\tag{1}
\]
For the third equation use \(w=1/u\) and divide \(w^DF(1/w)\) by \((1-w)^{2m}\). The three derivative conditions on \(H^0(\mathbb P^1,\mathcal O(D))\) are independent for \(D\ge8\): first jets at the three distinct points can be prescribed independently. Their common kernel has dimension \(D-2\), exactly \(\dim V_m\). Therefore (1) characterizes the **entire** series, not just a containing space.

**3. Every cusp has weight \(D-3\).** At \(u=0\), conditions (1) imply that a section vanishing there cannot have order one. For integers \(2\le k\le D-2\), write \(F=u^kG\) with \(\deg G\le e=D-k\). The two remaining conditions are
\[
G'(1)+(k-2m)G(1)=0,\qquad g_{e-1}+2mg_e=0,\tag{2}
\]
where \(g_i\) denotes a coefficient of \(G\). They are independent whenever \(e\ge2\). Indeed, the second functional is nonzero on the top two coefficients, while for \(e\ge3\) the first has a nonzero value on either \(1\) or \(u\), where the second vanishes. If \(e=2\), then \(k=D-2\) and the first functional takes the nonzero value \(2m-2\) on \(1\), whereas the second vanishes on \(1\). Thus \(\dim\{F\in V_m:u^k\mid F\}=e-1=D-k-1\) for \(2\le k\le D-2\). For \(k=D-1\), equation (2) with \(e=1\) implies that a linear \(G=au+b\) must obey \(b=-2ma\) and \(a[1-(2m-1)^2]=0\); since \(m\ge2\), only \(G=0\) works. Also a section of order zero exists (for example \(Y^m\)). It follows that the vanishing sequence at \(u=0\) is **exactly**
\[
0,2,3,\ldots,D-2,\qquad w_0=D-3=4m-3.
\]
The three cusp preimages are permuted by the automorphisms \(u\mapsto1-u\) and \(u\mapsto1/u\); the same calculation applies to each.

**4. The residual ramification is forced by symmetry.** The Plücker formula for a base-point-free \(N=D-2\) dimensional series of degree \(D\) on \(\mathbb P^1\) gives
\[
\deg\mathcal R(V_m)=N(D-N+1)=3(D-2)=3D-6.
\]
The cusps account for \(3(D-3)=3D-9\), leaving an effective divisor of degree three disjoint from the cusps. Permuting the homogeneous coordinates \(X,Y,Z\) induces the full anharmonic action of \(S_3\) on the normalization, generated by \(u\mapsto1-u\) and \(u\mapsto1/u\). Because all degree-\(m\) plane forms are preserved under these permutations, so is the residual divisor. In characteristic zero, the only orbit of size three on \(\mathbb P^1\) away from \(\{0,1,\infty\}\) is \(\{-1,1/2,2\}\); there is no orbit of size one. All other smooth orbits have size two or six. Hence an invariant effective divisor of degree three disjoint from the cusps must be the stated three-point orbit, each with multiplicity one. This gives the complete ramification divisor and, because a binary Wronskian is a section of \(\mathcal O(3D-6)\), its displayed factorization. Each smooth point has simple ramification and vanishing sequence \(0,1,\ldots,N-2,N\). No other ramification is possible.

## Verification
The standalone script `verify.py` uses exact rational symbolic arithmetic (SymPy). It substitutes the parametrization into the plane equation, checks the three independent derivative constraints against all plane monomials of degrees two through five, checks all cusp-subspace dimensions for \(2\le m\le10\), and calculates full Wronskian determinants in degrees \(m=2,3\). Its successful output is `VERIFY_OK`. Those experiments verify identities and sample instances, not infinitely many degrees; the all-degree conclusion is supplied by Steps 2–4 above. The six-by-six and ten-by-ten Wronskian matrices correspond, respectively, to conics and cubics.

## Relationship to prior work
Nawara, *Third-Order Weierstrass Points on Plane Quartics* (arXiv:2610.30992v1, public on 2026-10-22), develops the Wronskian language for rational parametrizations in Theorem 3.2 and studies specific **smooth** quartics; its formula for rational cubics does not evaluate the tricuspidal quartic, and it does not provide the all-degree divisor here. Maugesten–Moe, *The 2-Hessian and sextactic points on plane algebraic curves* (arXiv:1709.01698), provides the second-Veronese method and examples on a different singular quartic. The classical Coolidge count (quoted by Dimca–Ilardi–Malara–Pokora in arXiv:2311.08913, Theorem 3.1) already yields the **unrefined** three-sextactic-point count in this genus-zero three-cusp case when the dual has only ordinary singularities; that isolated count is not claimed as new. The original aspect is the exact three-jet characterization, complete weights and locations for **every** higher plane degree \(m\ge2\), including the persistence of the same smooth three-point orbit. A differently formulated classical all-degree statement has not been ruled out absolutely.

## Limitations
The theorem is over \(\mathbb C\), not in positive characteristic; positive-characteristic Wronskians require separate treatment. It concerns normalization ramification of the plane-form series, not intrinsic pluricanonical Weierstrass theory of a singular curve. The isolated previously known \(m=2\) count is expressly excluded from the novelty claim. Related classical all-degree osculation literature and inaccessible historical sources leave residual priority uncertainty.

## References
1. E. Nawara, *Third-Order Weierstrass Points on Plane Quartics*, arXiv:2610.30992v1 (first publicly submitted 2026-10-22), https://arxiv.org/html/2610.30992v1 . Sections 2–3.1 and 5–9 were read.
2. M. Maugesten and T. K. Moe, *The 2-Hessian and sextactic points on plane algebraic curves*, arXiv:1709.01698, https://arxiv.org/abs/1709.01698 . The methodological and singular-curve example sections were inspected.
3. A. Dimca, G. Ilardi, G. Malara, and P. Pokora, *Construction of free curves by adding osculating conics to a given cubic curve*, arXiv:2311.08913, https://arxiv.org/abs/2311.08913 . The quoted classical Coolidge sextactic-count formula was compared.
4. Classical Plücker–Brill–Segre formula for ramification of a base-point-free linear series on \(\mathbb P^1\), recalled in Reference 1, Section 2.1.
