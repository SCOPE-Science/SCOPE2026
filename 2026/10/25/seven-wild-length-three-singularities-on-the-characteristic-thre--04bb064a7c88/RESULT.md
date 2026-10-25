# Seven wild length-three singularities on the characteristic-three Klein cubic fourfold

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\). On \(\mathbb P^5_k\), with subscripts in \(\mathbb Z/6\mathbb Z\), consider the coefficientwise characteristic-three reduction of the classical Klein cubic fourfold
\[
X=V(F),\qquad F=\sum_{i=0}^{5}X_i^2X_{i+1}.
\]
The fourfold is geometrically integral and normal. Its full projective singular subscheme is the finite length-\(21\) scheme
\[
\operatorname{Sing}(X)\;\simeq\;\operatorname{Spec} k[t,t^{-1}]/(t^{21}-1)
=\operatorname{Spec}k[t]/(t^7-1)^3.
\]
Under this isomorphism, the closed embedding into the chart \(X_0=1\) is
\[
t\longmapsto[1:t:t^{-1}:t^3:t^{-5}:t^{11}].
\]
Thus its support consists precisely of the seven points \(P_\zeta=[1:\zeta:\zeta^{-1}:\zeta^3:\zeta^{-5}:\zeta^{11}]\) with \(\zeta^7=1\). The singular scheme at each point is curvilinear of length \(3\), not reduced. Every one of these singularities has completed local ring
\[
\widehat{\mathcal O}_{X,P_\zeta}\simeq
k[[u,v_1,v_2,v_3,v_4]]/(u^3+v_1^2+v_2^2+v_3^2+v_4^2).
\]
Over \(\mathbb F_3\), Frobenius has one rational fixed point and one six-cycle on the other singular points. In particular the six nonrational points are defined over \(\mathbb F_{3^6}\) and over no smaller finite extension.

## Assumptions and scope

All schemes are schemes over \(k\) unless an \(\mathbb F_3\)-structure is explicitly mentioned. The projective singular subscheme is cut out by \(F\) and all six ordinary projective partial derivatives, with its full (possibly nonreduced) scheme structure. Formal equivalence means an isomorphism of complete local \(k\)-algebras. The cubic is the coefficientwise reduction of the stated integral equation; the assertion does not address arbitrary integral models of isomorphic complex cubic fourfolds.

## Proof

**1. The singular scheme lives in one affine torus chart.** In characteristic \(3\), the projective partial derivatives are
\[
\frac{\partial F}{\partial X_i}=X_{i-1}^2-X_iX_{i+1}.
\]
If \(X_i=0\) at a singular point, then the \(i\)-th partial forces \(X_{i-1}=0\), and iteration forces all projective coordinates to vanish, impossible. Consequently every geometric singular point has all coordinates nonzero, and all of the finite singular subscheme is covered by \(X_0=1\).

**2. Elimination yields the exact scheme, not merely its points.** Set \(x_j=X_j/X_0\), for \(1\le j\le5\), and put \(t=x_1\). The affine equation is
\[
f=x_1+x_1^2x_2+x_2^2x_3+x_3^2x_4+x_4^2x_5+x_5^2.
\]
The five affine partial equations are
\[
1-x_1x_2,\quad x_1^2-x_2x_3,\quad x_2^2-x_3x_4,\quad
x_3^2-x_4x_5,\quad x_4^2-x_5.
\]
The first four successively force \(x_2=t^{-1}\), \(x_3=t^3\), \(x_4=t^{-5}\), and \(x_5=t^{11}\). They also imply that \(t\) is a unit, since \(x_1x_2=1\). The fifth becomes \(t^{-10}-t^{11}=t^{-10}(1-t^{21})\), hence the quotient of the affine polynomial ring by the partial ideal is exactly \(k[t,t^{-1}]/(t^{21}-1)\). Substituting into \(f\) gives \(5t+t^{22}=6t\equiv0\) modulo \(t^{21}-1\) in characteristic three; thus the hypersurface equation adds no relation. The remaining homogeneous partial also vanishes: it reduces to \(t^{22}-t=t(t^{21}-1)\). We have obtained the projective singular subscheme exactly. Since \(t^{21}-1=(t^7-1)^3\) and \(7\) is prime to \(3\), each of the seven roots of \(t^7-1\) has local length \(3\), with embedding dimension \(1\).

**3. The local hypersurface normal form.** All singular points are projectively equivalent by the diagonal transformations
\[
(X_0,X_1,X_2,X_3,X_4,X_5)\mapsto
(X_0,\zeta X_1,\zeta^{-1}X_2,\zeta^3X_3,\zeta^{-5}X_4,\zeta^{11}X_5),
\quad\zeta^7=1.
\]
Indeed all six summands of \(F\) are multiplied by the common factor \(\zeta\). It suffices to study \(P_1=[1:1:1:1:1:1]\). Translate the affine variables by \(x_j=1+u_j\). The Hessian is twice the \(5\)-by-\(5\) tridiagonal matrix with diagonal and adjacent entries \(1\). In characteristic \(3\) it has rank \(4\), and its kernel is spanned by \((2,1,0,2,1)\). The homogeneous cubic part is \(\sum_{j=1}^{4}u_j^2u_{j+1}\); evaluated on this null direction it equals \(2\ne0\).

Since \(2\) is invertible, the formal splitting lemma for a nondegenerate quadratic summand applies to give a formal contact-equivalent equation \(Q(v_1,\ldots,v_4)+g(u)\) where \(Q\) is a nondegenerate quadratic form, \(g\) has no terms below degree \(3\), and its cubic coefficient is nonzero. In one formal variable, \(g(u)=c u^3(1+h(u))\), with \(c\ne0\), so multiplying the equation by the inverse unit makes the residual term \(u^3\). The altered nondegenerate quadratic coefficients are units in \(k[[u]]\) and have square roots since \(2\) is invertible, so a further invertible rescaling of the quadratic variables restores a constant diagonal form over \(k\). This gives the claimed completed local ring. The gradient of this normal form is \((0,2v_1,\ldots,2v_4)\), hence its singular subscheme is \(k[[u]]/(u^3)\), independently confirming local length \(3\).

**4. Arithmetic and normality.** On \(\zeta^7=1\), arithmetic Frobenius sends \(\zeta\mapsto\zeta^3\). Since the multiplicative order of \(3\) modulo \(7\) is \(6\), the six primitive seventh roots form one six-cycle, while \(1\) is fixed. Finally the geometric singular support is zero-dimensional; a reducible or nonreduced cubic hypersurface in projective five-space would have a positive-dimensional singular locus. Thus \(X\) is geometrically integral. A hypersurface is Cohen–Macaulay (\(S_2\)), and isolated singularities on a fourfold satisfy \(R_1\); Serre's criterion gives normality.

## Verification

The accompanying self-contained `VERIFY.py` reproduces the Laurent exponent relations and the reduction of \(F\) and its partial derivatives, checks that the affine Hessian has rank \(4\) and the displayed kernel has nonzero cubic coefficient, checks the Frobenius orbit length, and enumerates the \(\mathbb F_3\)-rational singular support. It uses only Python's standard library; execute `python3 VERIFY.py`. These exact checks supplement the universal algebraic proof; the finite-field enumeration alone is not a proof over \(k\).

## Relationship to prior work

González-Aguilera and Liendo, *Automorphisms of prime order of smooth cubic n-folds* (arXiv:1002.4136, first posted 22 February 2010), Definition 1.9, define the cyclic Klein cubic \(n\)-fold and study its smooth complex geometry. Their results do not give the characteristic-three singular scheme. He, Li, Wang and Zheng, *Cubic Fourfolds with an Order-7 Automorphism* (arXiv:2509.26359, 2025), Theorem 1.2(3), use exactly the cyclic six-variable Klein equation over \(\mathbb C\); their Section 3.3 and Proposition 3.12 classify certain singular *other members* of the characteristic-zero family. In particular, their special seven-\(A_2\) member has parameters \((a,b)=(1,1)\), whereas their smooth Klein member has \((a,b)=(0,0)\). Neither statement implies the present bad-reduction singular-scheme calculation. Searches for the reduction, its aliases, the exact equation and its length-three local scheme have not identified a previously published equivalent result. This lack of identification is not a uniqueness proof.

## Limitations

The result is for the specified coefficientwise integral model in characteristic \(3\), and for the scheme of vanishing ordinary partial derivatives; it does not establish a simultaneous resolution, stable or semistable reduction, or any Hodge or étale-cohomological invariant of the special fibre. Potential overlap with specialized positive-characteristic sources not identified by the literature searches remains. The verification script checks exact identities and small finite data but is not an independent certification of the formal splitting theorem.

## References

1. V. González-Aguilera and A. Liendo, *Automorphisms of prime order of smooth cubic n-folds*, arXiv:1002.4136 (first public version 2010-02-22), Definition 1.9 and Theorem 1.10. https://arxiv.org/abs/1002.4136
2. X. He, Y. Li, S. Wang and Z. Zheng, *Cubic Fourfolds with an Order-7 Automorphism*, arXiv:2509.26359 (2025), Theorem 1.2 and Propositions 3.11–3.12. https://arxiv.org/abs/2509.26359
