# An arithmetic node dichotomy on the characteristic-two symmetric Burkhardt quartic

## Finding
Consider the symmetric quartic threefold \(X/\mathbb F_2\) cut out in \(\mathbb P^5\) by \(e_1=e_4=0\), where \(e_i\) is the elementary symmetric polynomial in six homogeneous coordinates. Its 45 geometric singularities are ordinary double points, but its arithmetic is sharply asymmetric: 15 nodes are rational over \(\mathbb F_2\), and the remaining 30 form 15 degree-two Frobenius orbits. There are no smooth \(\mathbb F_2\)-points.

Let \(\widetilde X\to X\) be the blowup of the reduced singular locus. This is a smooth threefold, and
\[
\#X(\mathbb F_2)=15,\quad \#\widetilde X(\mathbb F_2)=75,\quad
\#X(\mathbb F_4)=205,\quad \#\widetilde X(\mathbb F_4)=1285.
\]
For every integer \(n\ge1\), putting \(q=2^n\),
\[
\#\widetilde X(\mathbb F_q)-\#X(\mathbb F_q)=
\begin{cases}15q^2,&n\text{ odd},\\45q^2+90q,&n\text{ even}.\end{cases}
\]
Consequently the rational zeta-factor correction is
\[
\frac{Z(\widetilde X/\mathbb F_2,T)}{Z(X/\mathbb F_2,T)}=
\frac{1}{(1-4T)^{30}(1+4T)^{15}(1-2T)^{45}(1+2T)^{45}}.
\]
These statements concern the *symmetric six-coordinate form*, not every arithmetic form of the Burkhardt quartic.

## Assumptions and scope
Work over fields of characteristic two and their algebraic closures. For six coordinates \(x_0,\ldots,x_5\), let \(e_i\) be their \(i\)-th elementary symmetric polynomial, and eliminate one coordinate using \(e_1=0\). Thus \(X\) is a quartic hypersurface in \(\mathbb P^4\). All rational-point counts refer to this specified \(\mathbb F_2\)-model, not to an unspecified twist. “Ordinary double point” means an isolated hypersurface singularity with nondegenerate quadratic tangent cone (nondegenerate polar bilinear form in characteristic two).

## Proof
**1. Complete geometric singular classification.** On \(e_1=0\), the partial derivatives of \(e_4\) satisfy
\[
\partial_{x_i}e_4=e_3+x_i e_2+x_i^3.
\]
The gradient of \(e_4\) is proportional to the nonzero gradient of \(e_1\) exactly when the six coordinates satisfy one equation \(x_i^3+e_2x_i=c\), with a common \(c\). Hence there are at most three distinct coordinate values. If just one value occurs, then \(e_1=0\) automatically, but \(e_4=\binom64 a^4=a^4\), so the only solution is the forbidden all-zero vector. If there are two distinct values \(a,b\) with multiplicities \(r,6-r\), the equality \(e_1=0\) forces \(r\) even. For the possibilities \((2,4)\) and \((4,2)\), the coefficient \(e_4\) equals the fourth power of the value of multiplicity four; it therefore vanishes only if that value is zero. These are exactly the 15 projective points with two coordinates equal to 1 and four equal to 0.

If three distinct values \(a,b,c\) occur, they are the distinct roots of a monic cubic with zero quadratic coefficient, so \(a+b+c=0\). Since \(e_1=0\), their multiplicities are all even: a common odd parity would make their total number odd. Thus all multiplicities equal two. Here \(e_4=(ab+ac+bc)^2\), so \(ab+ac+bc=0\). The three values are, up to common scalar, \(1,\omega,\omega^2\), where \(\omega^2+\omega+1=0\) over \(\mathbb F_4\). Conversely direct substitution verifies the gradient condition for these values. The 90 coordinate reorderings, modulo the three projective scalar multiplications by \(1,\omega,\omega^2\), produce precisely 30 distinct geometric points. This proves that the geometric singular set has exactly \(15+30=45\) points, all defined over \(\mathbb F_4\).

**2. Nondegenerate quadratic cones.** For a rational node \((1,1,0,0,0,0)\), choose the affine chart with the first coordinate 1 and take the four formerly zero coordinates as local parameters \(u_1,\ldots,u_4\). The remaining coordinate is \(1+u_1+u_2+u_3+u_4\). The quadratic term of \(e_4\) is
\[
Q_1(u)=\sum_{1\le i<j\le4}u_i u_j.
\]
Its polar matrix has zeros on the diagonal and ones off-diagonal; it is invertible over \(\mathbb F_2\). At a node of the 30-point orbit represented by \((1,1,\omega,\omega,\omega^2,\omega^2)\), chart coordinates \(x_0=1\), \(x_j=x_j(P)+u_j\) for \(1\le j\le4\), and \(x_5=\sum_{j=0}^4 x_j\) give quadratic term
\[
Q_2(u)=\omega^2u_2u_3+\omega u_4(u_1+u_2+u_3+u_4).
\]
Its polar form has rank four: \(u_1\) is paired with \(u_4\) and \(u_2\) with \(u_3\). Permutation invariance covers every node. Thus all 45 are ordinary nodes, and the Jacobian singular scheme is reduced on the geometric fiber.

**3. Quadrics and Galois action.** The projective \(\mathbb F_2\)-solutions of \(Q_1=0\) are exactly the weight-one vectors and the all-one vector, giving five points. A smooth projective quadric surface over \(\mathbb F_2\) with five rational points is the nonsplit form, so over \(\mathbb F_{2^n}\) it has \(q^2+1\) points for odd \(n\) and \((q+1)^2\) points for even \(n\). Every 30-orbit node is defined over \(\mathbb F_4\), and its quadric is split there: the displayed \(Q_2\) contains the two-dimensional totally singular subspace \(u_2=u_4=0\), and its polar form is nondegenerate. Its exceptional quadric therefore has \((q+1)^2\) points over all even-degree extensions \(\mathbb F_q/\mathbb F_2\). None of the 30-orbit nodes is fixed by Frobenius: any point fixed as a projective point over \(\mathbb F_2\) has a representative in \(\mathbb F_2^6\), but the three distinct coordinate values cannot then occur. Hence the Frobenius orbit profile is \(1^{15}2^{15}\).

**4. Rational-point and zeta correction.** Over \(\mathbb F_2\), a projective point has binary coordinates of even positive weight because \(e_1=0\). The only possible weights are 2, 4, and 6, and \(e_4=\binom w4\bmod2\) vanishes only at weight 2. This gives 15 points, all among the above nodes. A node with smooth projectivized tangent quadric is resolved by blowing up once; its exceptional surface is exactly that quadric. Therefore the 15 rational points are each replaced by five points over \(\mathbb F_2\), giving 75. More generally, subtract one for every rational node and add the point count of its exceptional quadric. For odd \(n\) only the 15 nonsplit rational nodes appear, giving \(15[(q^2+1)-1]=15q^2\). For even \(n\), all 45 nodes appear and all their quadrics are split, giving \(45[(q+1)^2-1]=45q^2+90q\). Finally, applying \(Z(Y,T)=\exp(\sum_{n\ge1}\#Y(\mathbb F_{2^n})T^n/n)\) to these differences yields the displayed product of four linear Euler factors.

## Verification
The accompanying self-contained `verify_burkhardt_twist.py` uses exact arithmetic in \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). It exhaustively enumerates the \(\mathbb F_2\)- and \(\mathbb F_4\)-points, confirms \(15\) and \(205\) points respectively, verifies \(45\) singular points over \(\mathbb F_4\), computes both representative local quadratic tangent cones and their rank-four polar forms, and counts five points on the first exceptional quadric over \(\mathbb F_2\) and 25 points on both types over \(\mathbb F_4\). It prints `VERIFY_OK`, `NODE_QUADRATICS_OK`, and `QUADRIC_FIELD_COUNTS_OK`. The general geometric classification and all-degree point corrections follow from the symbolic argument, not from finite enumeration alone.

## Relationship to prior work
Cheltsov--Przyjalkowski--Shramov (first made public June 14, 2016) describe the symmetric six-coordinate Burkhardt quartic and its 15-plus-30 complex node configuration; the modular geometry is an essential starting point. Their characteristic-zero statements alone do not prove that the characteristic-two reduction has precisely 45 ordinary nodes with the specified Frobenius and tangent-quadric forms. Bruin--Nasserden describe arithmetic of a distinct five-coordinate quartic form and warn that the symmetric form is a nontrivial arithmetic twist when cube roots of unity are absent; their characteristic-two singular-node arithmetic is not the same as the displayed model. Bruin--Filatov's later study of twists explicitly excludes characteristic two. The present result supplies a direct exceptional-divisor point-count and zeta-factor correction for the symmetric characteristic-two special fiber. No claim is made to compute the entire zeta function of \(X\).

## Limitations
The statement is specific to the symmetric six-coordinate \(\mathbb F_2\)-model; it does not classify all twists, nor does it calculate the full zeta function of \(X\) or \(\widetilde X\). A broader historical source covering precisely this characteristic-two special fiber could contain an equivalent exceptional-divisor correction; no exhaustive archival search has been achieved. Independent mathematical review is not represented by the accompanying finite-field script.

## References
1. I. Cheltsov, V. Przyjalkowski, C. Shramov, *Burkhardt quartic, Barth sextic, and the icosahedron*, arXiv:1606.04372v1 (June 14, 2016), https://arxiv.org/abs/1606.04372.
2. N. Bruin, B. Nasserden, *Arithmetic aspects of the Burkhardt quartic threefold*, arXiv:1705.09006 (May 25, 2017), https://arxiv.org/abs/1705.09006.
3. N. Bruin, E. Filatov, *Twists of the Burkhardt quartic threefold*, arXiv:2207.04393 (July 2022), https://arxiv.org/abs/2207.04393.
