# Relative edge-collision normal forms for tetrahedral quartics in characteristic two

## Finding

Let \(k\) be algebraically closed of characteristic two. Fix the coordinate tetrahedron of \(\mathbb P^3_k\), and put
\[
Q=\sum_{i=1}^4 b_i x_i^2+\sum_{i<j}a_{ij}x_ix_j,\qquad F=x_1x_2x_3x_4+Q^2,
\quad B=\operatorname{Spec}k[b_1^{\pm1},\ldots,b_4^{\pm1},a_{12},\ldots,a_{34}].
\]
Let \(\mathcal X=V(F)\subset\mathbb P^3_B\). On this entire marked base, including arbitrary simultaneous intersections of collision walls, the relative Jacobian scheme is the disjoint union of six finite locally free edge divisors of rank four, each cut out on its edge by \(Q^2\).

More precisely, fix a closed parameter point \(p\in B(k)\) with \(a_{ij}(p)=0\), and let \(t_0\in k^\times\) be the double root of \(Q|_{L_{ij}}(1,t)\) at \(p\). In \(A=\widehat{\mathcal O}_{B,p}\), set
\[
\lambda=a_{ij}/b_j,\qquad \mu=t_0^2+(a_{ij}/b_j)t_0+b_i/b_j.
\]
The completion of \(\mathcal X\) at this marked-edge singularity, as an \(A\)-algebra, is
\[
A[[U,V,s]]/\bigl(UV+(s^2+\lambda s+\mu)^2\bigr).
\]
Here \(\lambda,\mu\) can be included in a regular parameter system for this edge over \(A\), and the coordinates may be chosen with \(s=x_j/x_i-t_0\) and with the edge cut out by \(U=V=0\). The other transverse coefficients impose no additional terms in this completed equation. This is a local description at each colliding edge separately; it does not claim that twelve parameters from six different edges are simultaneously independent.

Geometrically, the collision walls are exactly \(a_{ij}=0\), independently specified for the six edges. All \(2^6\) strata occur. For \(r=\#\{(i,j):a_{ij}=0\}\), the fibre is normal and integral and has basket \(2(6-r)A_1+rA_3\). The relative Jacobian lengths are \(2+2\) on each uncollided edge and \(4\) on each collided edge.

## Proof

**The six marked divisors.** The four partial derivatives of \(F\) are the four triple products. A coordinate vertex does not lie on the surface, since the value of \(F\) there is a unit square. Where \(x_i,x_j\) are both units in a dehomogenized chart, the two complementary coordinates lie in the Jacobian ideal (each occurs as a triple product times a unit), and they generate its derivative part. The remaining equation is \(Q^2\) on that edge. No other support is possible because the triple products vanish only where at most two coordinates are nonzero. Thus the six components are disjoint, even scheme-theoretically. The component on \(L_{ij}\) is entirely in \(x_i\ne0\) and in that chart has equation
\[
\bigl(t^2+(a_{ij}/b_j)t+b_i/b_j\bigr)^2=0.
\]
The polynomial is monic of degree four, so the quotient is free with basis \(1,t,t^2,t^3\) over the base ring. This gives the rank-24 Jacobian family over all six walls. The quadratic has two distinct roots exactly when \(a_{ij}\ne0\); its square prescribes the local lengths on each edge.

**Completed collision equation.** Use \(x_i=1\), write \(x_j=t=t_0+s\), and denote the two transverse coordinates by \(u,v\). The ambient completed ring is \(A[[s]][[u,v]]\). The relative equation is \(tuv+Q(t,u,v)^2\). Put \(D=A[[s]]\), a complete local ring. The equation has no terms linear in \(u,v\), and its transverse quadratic part has polar coefficient \(t\in D^\times\) because the remaining terms come from squares. The quadratic form over the residue field has two distinct isotropic lines: it is binary over the algebraically closed field, and distinctness follows from the nonzero polar coefficient. Each line lifts by Hensel's lemma in its slope chart since the derivative of the slope equation is the polar coefficient times a unit. The two lifted lines give a basis of \(D^2\), and a unit rescaling identifies the quadratic form with \(UV\).

The coordinate changes so far preserve \((u,v)\). To remove any transverse homogeneous part of degree \(d\ge3\), write it as \(V\alpha+U\beta\) with \(\alpha,\beta\) homogeneous of degree \(d-1\). Substituting \(U+\alpha,V+\beta\) cancels it in degree \(d\) and introduces only terms of higher degree. The iterative substitutions stabilize modulo every transverse power and yield an invertible formal change; they fix \(D\) and preserve the edge ideal. Hence the completed equation is \(UV+Q(t,0,0)^2\). Expanding the edge quadratic about \(t_0\) gives \(Q(t,0,0)=b_j(s^2+\lambda s+\mu)\); scale one transverse variable and normalize the equation by the unit \(b_j^2\). The inverse substitutions \(a_{ij}=b_j\lambda\), \(b_i=b_j(\mu+t_0^2+\lambda t_0)\) prove the regular-parameter assertion while keeping all other base coordinates fixed.

**Fibres.** A nonzero mixed coefficient gives a simple edge root. In the fibre use \(Q\) as the third parameter along with \(u,v\), since the derivative in the edge direction is \(a_{ij}\ne0\); the factor \(t\) in \(tuv\) is a unit and can be absorbed into one transverse variable. The result is \(UV+W^2\), an \(A_1\). At a collision, \(\lambda=\mu=0\) in the closed fibre of the completed model, giving \(UV+s^4\), an \(A_3\). The six independently variable coefficients prescribe the walls (all zero/nonzero patterns are realized with \(b_i=1\)). There are no other singularities. A reducible or nonreduced projective hypersurface in \(\mathbb P^3_k\) would have a singular locus of positive dimension (two distinct hypersurface components meet in at least a curve; a repeated component is singular along a surface). Every fibre here is therefore reduced and integral, and Serre's criterion applies by the hypersurface Cohen–Macaulay property and regularity in codimension one. Over geometric fields the same argument applies directly.

## Established cases and scope of the extension

- Catanese–Schütt, [*Singularities of normal quartic surfaces III*, §3.8, Example 19](https://arxiv.org/html/2206.03295v1), introduce the product-plus-square family, give the general twelve-node statement, and give the six-\(A_3\) Dwork example. Dolgachev–Kondō, [*Desmic quartic surfaces in arbitrary characteristic*, §7](https://arxiv.org/html/2505.01033v1), also cover a six-\(A_3\) all-mixed-zero subfamily. Those endpoint cases are not new here.
- [*Exact 12-node chamber for the tetrahedral square-quartic family in characteristic two*](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-exact-12-node-chamber-for-the-tetrahedral-square-quartic-family--f0a07bc20820) gives the exact open chamber, the Jacobian ideal formula and the simple-root local model. The relative rank-four edge algebra is a direct consequence of that ideal calculation once the vertices are removed. It is included here to identify the scheme whose support collides, not as a separate novelty claim.
- [*The flat length-24 singular scheme and Cremona dual of primitive Heisenberg quartics in characteristic two*](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-the-flat-length-24-singular-scheme-and-cremona-dual-of-primitive--2253bd84ce62) proves the paired-edge specialization of the fibre classification, with the same formal splitting argument over a fixed fibre. Its equal-diagonal and paired mixed coefficients force the edges to collide in pairs. Here the completion is over the full marked coefficient base; the formula accounts for any subset of colliding edges and retains both deformation coordinates at each collision rather than specializing them to zero.
- [*Independent Frobenius splitting of twelve nodes on tetrahedral quartic K3 models*](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-independent-frobenius-splitting-of-twelve-nodes-on-tetrahedral-q--7913d261353b) already covers the all-nonzero finite-field trace criterion and all 64 labelled splitting profiles. Neither this arithmetic classification nor the generic splitting group is claimed as a finding here.

The walls classify collisions of geometric singular supports in the marked coefficient base; they do not classify the non-étale locus of an already nonreduced Jacobian scheme, projective-isomorphism classes, or singularities where some diagonal coefficient vanishes.

## Reproducibility

`verify_tetrahedral.py` checks all 64 binary mixed-coefficient patterns at \(b_i=1\) by exact point evaluation over \(\mathbb F_4\). Its trace tests are supplementary checks of the arithmetic context. The normal forms and the finite flat relative statement are proved above, not inferred from the finite tests.
