# Uniform length-four singular-scheme thickening in the even-characteristic plane-filling family

## Finding

Let \(q=2^m\), where \(m\ge1\), let \(k\in\mathbb F_q\), and set \(K=\overline{\mathbb F}_q\). The projective curve \(C_k\subset\mathbb P^2_{\mathbb F_q}\) has equation
\[
F=x^2(x^qy-xy^q)+y^2(y^qz-yz^q)+(z^2+kx^2)(z^qx-zx^q)=0.
\]
Write \(J_k\) for the scheme-theoretic singular locus, defined by the homogeneous Jacobian ideal and viewed over \(K\). Then \(J_k\) is finite, with precisely
\[
1+\frac{q(q+2)}4
\]
geometric support points. Each point has the same completed local singular-scheme algebra, namely \(K[[U,V]]/(U^2,V^2)\), and consequently
\[
\operatorname{length}(J_k)=q(q+2)+4.
\]
These conclusions hold for **every** parameter \(k\in\mathbb F_q\), without assuming that \(C_k\) is irreducible.

## Assumptions and scope

All schemes are base changed to the algebraic closure \(K\) of the field of characteristic two. The singular scheme is the Jacobian/Fitting singular subscheme of the plane hypersurface, not the reduced support and not its conductor. The curve is the *original* Asgarli–Ghioca family \(C_k\), not their distinct even-characteristic replacement family \(D_k\). The point count is a geometric, not necessarily an \(\mathbb F_q\)-rational, count. The equation and the invariant include \(q=2\) and \(k=0\).

## Proof

**No singular points occur on \(x=0\).** The degree is \(q+3\), an odd integer in characteristic two. On the line \(x=0\), direct differentiation of the homogeneous equation gives \(F_z=y^{q+2}\). Hence a singular point there would have \(y=0\). But at \([0:0:1]\) one has \(F_x=1\), a contradiction.

**Jacobian ideal on \(x=1\).** Use coordinates \(t=y/x\) and \(s=z/x\), and choose the unique \(\kappa\in\mathbb F_q\) with \(\kappa^2=k\). Define
\[
A=1+t s^{q/2},\qquad B=t^{(q+2)/2}+s+\kappa.
\]
The affine derivatives of \(f(t,s)=F(1,t,s)\), computed in characteristic two, are
\[
f_t=1+t^2s^q=A^2,\qquad f_s=t^{q+2}+s^2+k=B^2.
\]
Since the projective degree \(q+3\) is odd, Euler's identity reads \(F=xF_x+yF_y+zF_z\). Thus, on this chart, the scheme-theoretic projective singular locus has ideal exactly \((f_t,f_s)=(A^2,B^2)\). In particular, the singular support is cut out by \(A=B=0\).

**Counting the geometric points.** The equation \(A=0\) forces \(s\ne0\) and \(t=s^{-q/2}\). Substituting into \(B=0\) gives
\[
s^{r+1}+\kappa s^r+1=0,\qquad r=\frac{q(q+2)}4=2^{m-1}(2^{m-1}+1).
\]
The integer \(r\) is even for every \(m\ge1\), and the derivative of the displayed polynomial is \(s^r\). Since its constant term is one, all roots are nonzero, and all \(r+1\) roots are simple. Each root determines a unique \(t\). This proves the claimed exact number of geometric support points; it is independent of \(k\).

**Scheme structure at each support point.** For \(A\) and \(B\) the Jacobian determinant in local coordinates \((t,s)\) is
\[
\det\!\left(\frac{\partial(A,B)}{\partial(t,s)}\right)
=s^{q/2}+\bigl(q/2\bmod2\bigr)\bigl((q+2)/2\bmod2\bigr)t^{q/2+1}s^{q/2-1}=s^{q/2}.
\]
Here one of the two consecutive integer factors is always even. At any point of the singular support \(s\ne0\), so \(A,B\) are regular formal local parameters. Passing to the completed local ring, the singular subscheme becomes \(K[[A,B]]/(A^2,B^2)\), whose basis is \(1,A,B,AB\), of length four. The total length is therefore \(4(r+1)=q(q+2)+4\).

## Verification

Every step above is symbolic for all \(m\ge1\); no finite enumeration is used to infer the general theorem. As spot checks, polynomial differentiation over the prime field confirms the displayed derivative identities for \(q=2,4,8,16\), with predicted support-point counts \(3,7,21,73\) and lengths \(12,28,84,292\), respectively. The independent variables \(A,B\) give a direct complete local-ring computation, rather than an inferred multiplicity from a point count.

## Relationship to prior work

Asgarli and Ghioca construct the plane-filling \(C_k\) in their equation (1), Theorem 1.2, and explicitly remark after Conjecture 1.5 that **for every even** \(q\) **all** such curves are singular. They then turn to a different family \(D_k\). Their discussion proves the motivating qualitative singularity obstruction, but the inspected material does not give the complete geometric point count or the uniform length-four local structure of the Jacobian singular scheme. The present result quantifies precisely how the even-characteristic degeneration is distributed, without claiming the known singularity observation as new.

## Limitations

The theorem concerns the Jacobian singular subscheme, not the analytic classification of curve branches, delta invariants, the normalization, or singularity locations over a specified proper finite extension. It makes no irreducibility assertion, and the support points need not be \(\mathbb F_q\)-rational. The published literature search cannot rule out equivalent computations elsewhere, particularly in general work on Frobenius plane curves or Jacobian ideals.

## References

Shamil Asgarli and Dragos Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1, first publicly submitted 6 July 2023 (primary MSC 14G15, 14H50), especially equation (1), Theorem 1.2, Conjectures 1.5–1.6 and the even-characteristic discussion, and Section 4. https://arxiv.org/html/2307.03072v1
