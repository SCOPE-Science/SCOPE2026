# Uniform length-four singular-scheme thickening in the even-characteristic plane-filling family

## Finding

Let \(q=2^m\), with \(m\ge1\), let \(k\in\mathbb F_q\), and put \(K=\overline{\mathbb F}_q\). For the plane curve \(C_k\) defined by
\[
F=x^2(x^qy-xy^q)+y^2(y^qz-yz^q)+(z^2+kx^2)(z^qx-zx^q)=0,
\]
write \(J_k\) for its Jacobian singular subscheme over \(K\). Then \(J_k\) is finite, has exactly \(1+q(q+2)/4\) geometric support points, and has completed local algebra \(K[[U,V]]/(U^2,V^2)\) at every one of them. In particular, \(\operatorname{length}(J_k)=q(q+2)+4\). This holds for all \(k\), without an irreducibility assumption.

## Assumptions and scope

The singular scheme is defined by \(F\) and its three homogeneous partials. This is the Jacobian/Fitting singular subscheme, not the reduced support or the conductor. The curve is the original Asgarli–Ghioca family \(C_k\), not their distinct even-characteristic replacement family \(D_k\). The geometric count includes points not rational over \(\mathbb F_q\). The cases \(q=2\) and \(k=0\) are included.

## Proof

On \(x=0\) we have \(F_z=y^{q+2}\), so any singular point there must be \([0:0:1]\); at that point \(F_x=1\). Thus the entire singular scheme is on the chart \(x=1\).

On that chart let \(t=y/x\), \(s=z/x\), \(f(t,s)=F(1,t,s)\), and let \(\kappa^2=k\). Direct differentiation in characteristic two gives
\[
f_t=1+t^2s^q=A^2,\qquad f_s=t^{q+2}+s^2+k=B^2,\qquad
A=1+ts^{q/2},\qquad B=t^{(q+2)/2}+s+\kappa.
\]
The odd degree \(q+3\) gives the Euler identity \(F=xF_x+yF_y+zF_z\), so the projective Jacobian ideal on the chart is \((f,f_t,f_s)\). To remove \(f\), one needs an additional polynomial identity. Indeed, expanding the original equation gives
\[
f=(t+t^q)(1+t^2s^q)+(s+s^q)(t^{q+2}+s^2+k)=(t+t^q)f_t+(s+s^q)f_s.
\]
Consequently the ideal is \((A^2,B^2)\), and its support is cut out by \(A=B=0\).

At a support point \(s\ne0\) and \(t=s^{-q/2}\). Substitution in \(B=0\) reduces it to
\[
H(s)=s^{r+1}+\kappa s^r+1=0,\qquad r=\frac{q(q+2)}4=2^{m-1}(2^{m-1}+1).
\]
The integer \(r\) is even, so \(H'(s)=s^r\); since \(H(0)=1\), all its \(r+1\) roots in \(K\) are simple and nonzero. Each gives exactly one support point. The Jacobian determinant of \((A,B)\) in coordinates \((t,s)\) is \(s^{q/2}\): the product of the two off-diagonal entries vanishes because the integers \(q/2\) and \((q+2)/2\) are consecutive. At any support point this determinant is nonzero, so \(A,B\) are formal local parameters. The completed singular algebra is therefore \(K[[A,B]]/(A^2,B^2)\), with basis \(1,A,B,AB\). Summing the local lengths gives \(4(r+1)=q(q+2)+4\).

## Verification

The identities and separability check apply symbolically to all \(m\ge1\). As a check on the total length, in the derivative quotient \(s\) is invertible and \(t^2=s^{-q}\). After substituting this relation into \(B^2\), the resulting relation on \(s\) is \(H(s)^2=0\), up to the unit \(s^{-2r}\). Thus the quotient is free of rank two with basis \(1,t\) over \(K[s,s^{-1}]/(H^2)\); its dimension is \(4(r+1)\), in agreement with the completed local calculation.

## Relationship to prior work

Asgarli and Ghioca define this family in equation (1); Theorem 1.2 concerns smoothness at rational points, and the remark after Conjecture 1.5 states that all members in even characteristic are singular. The distinct family \(D_k\), introduced there, uses \(z^2+kxy\) instead of \(z^2+kx^2\). A later result on Frobenius valuations classifies singularities at \(\mathbb F_q\)-rational points of a family including this one, but does not count its geometric support or compute the Jacobian scheme at all geometric points. The new calculation concerns the geometric count and the uniform completed Jacobian algebra, not the qualitative singularity obstruction.

## Limitations

This does not classify analytic branches, conductor or delta invariants, the normalization, or support locations over specified finite extensions.

## References

1. Shamil Asgarli and Dragos Ghioca, *Plane-filling curves of small degree over finite fields*, [arXiv:2307.03072v1](https://arxiv.org/html/2307.03072v1), equation (1), Theorem 1.2, and the discussion following Conjecture 1.5.
2. *Frobenius-valuation trichotomy for rational singularities of plane-filling curves*, [published finding](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-frobenius-valuation-trichotomy-for-rational-singularities-of-pla--07ef9547766e/RESULT.md), Finding and Assumptions and scope.
