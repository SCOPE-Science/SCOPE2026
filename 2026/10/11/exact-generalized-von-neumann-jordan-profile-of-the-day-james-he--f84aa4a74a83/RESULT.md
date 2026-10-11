# Exact generalized von Neumann--Jordan profile of the Day--James hexagon
## Finding
Let \(X=(\mathbb R^2,N)\), where
\[
N(s,t)=\max\{|s|,|t|,|s-t|\},
\]
the affine-regular hexagonal realization of the real Day--James plane \(\ell_\infty-\ell_1\). For \(1\le p<\infty\), let
\[
C_{\mathrm{NJ}}^{(p)}(X)
=
\sup_{(x,y)\ne(0,0)}
\frac{N(x+y)^p+N(x-y)^p}{2^{p-1}\bigl(N(x)^p+N(y)^p\bigr)}.
\]
Then \(C_{\mathrm{NJ}}^{(1)}(X)=2\). For every \(p>1\), there is a unique \(\tau_p\in(0,1)\) satisfying
\[
\tau_p^{1-p}-(1+\tau_p)^{1-p}=1,
\]
and
\[
C_{\mathrm{NJ}}^{(p)}(X)
=
\frac{1+(1+\tau_p)^p}{2^{p-1}(1+\tau_p^p)}
=
\left(\frac{1+\tau_p}{2\tau_p}\right)^{p-1}.
\]
In the standard unit-sphere parametrization, an extremizer is \(x=(0,1)\), \(y=(1,0)\), with scale parameter \(t=\tau_p\).

At \(p=2\), the critical point is
\[
\tau_2=\frac{\sqrt5-1}{2},
\]
and the formula reduces to
\[
C_{\mathrm{NJ}}^{(2)}(X)=\frac{3+\sqrt5}{4},
\]
recovering the classical Day--James endpoint value.

## Assumptions and scope
The scalar field is real and the dimension is exactly two. The generalized von Neumann--Jordan constant is the exponent-\(p\) constant defined for \(1\le p<\infty\). No assertion is made for other Day--James norms or higher-dimensional analogues.

## Proof
For arbitrary nonzero \(x,y\), swap them if necessary so \(N(x)\ge N(y)\). Put
\[
a=N(x),\qquad b=N(y),\qquad t=\frac ba\in[0,1].
\]
If \(b>0\), set \(u=x/a\) and \(v=y/b\). Homogeneity gives
\[
\frac{N(x+y)^p+N(x-y)^p}{2^{p-1}(N(x)^p+N(y)^p)}
=
\frac{N(u+tv)^p+N(u-tv)^p}{2^{p-1}(1+t^p)}.
\]
The case \(b=0\) is \(t=0\). Thus it suffices to maximize over \(u,v\in S_X\) and \(0\le t\le1\).

The unit ball has cyclic vertices
\[
v_0=(1,1),\ v_1=(1,0),\ v_2=(0,-1),\
v_3=(-1,-1),\ v_4=(-1,0),\ v_5=(0,1).
\]
For fixed \(t\),
\[
\Phi_t(u,v)=N(u+tv)^p+N(u-tv)^p
\]
is jointly convex on \(B_X\times B_X\). Hence its maximum is attained at a vertex pair. Dihedral symmetry fixes the first vertex, and the six relative positions of the second give only
\[
(1+t,1-t),\quad(1+t,1),\quad(1,1+t),\quad(1-t,1+t)
\]
for
\[
\bigl(N(u+tv),N(u-tv)\bigr).
\]
Therefore
\[
\max_{u,v\in S_X}\Phi_t(u,v)=1+(1+t)^p,
\]
because \((1-t)^p\le1\). The pair \(u=(0,1)\), \(v=(1,0)\) attains this value.

Consequently
\[
C_{\mathrm{NJ}}^{(p)}(X)=\max_{0\le t\le1}
f_p(t),\qquad
f_p(t)=\frac{1+(1+t)^p}{2^{p-1}(1+t^p)}.
\]
For \(p=1\),
\[
f_1(t)=\frac{2+t}{1+t},
\]
so the maximum is \(2\) at \(t=0\).

Now let \(p>1\) and \(q=p-1\). Apart from a positive factor, the derivative of \(f_p\) has the sign of
\[
H_q(t)=t^{-q}-(1+t)^{-q}-1.
\]
Indeed,
\[
(1+t)^q(1+t^{q+1})-t^q(1+(1+t)^{q+1})
=
t^q(1+t)^qH_q(t).
\]
Moreover
\[
H_q'(t)=-q\,t^{-q-1}+q(1+t)^{-q-1}<0,
\]
while \(H_q(t)\to+\infty\) as \(t\downarrow0\) and \(H_q(1)=-2^{-q}<0\). Hence there is a unique \(\tau_p\in(0,1)\) with \(H_q(\tau_p)=0\), and it is the unique global maximizer.

Put
\[
a=\tau_p^q,\qquad b=(1+\tau_p)^q.
\]
The critical equation is \(1/a-1/b=1\), equivalently \(b-a=ab\). A direct cross multiplication then gives
\[
\frac{1+(1+\tau_p)^{q+1}}{1+\tau_p^{q+1}}=\frac ba.
\]
Therefore
\[
f_p(\tau_p)=\frac1{2^q}\frac ba
=
\left(\frac{1+\tau_p}{2\tau_p}\right)^q,
\]
as claimed.

## Verification
The continuum optimization is exhaustive. Homogeneity reduces arbitrary nonzero pairs to the scale interval \(0\le t\le1\). Joint convexity then reduces each fixed-\(t\) problem to all \(36\) hexagon vertex pairs, and symmetry reduces these to six relative positions. The remaining scalar derivative has exactly one zero.

For \(p=2\), the critical equation gives
\[
\tau_2=\frac{\sqrt5-1}{2},
\]
and the formula becomes
\[
C_{\mathrm{NJ}}^{(2)}(X)=\frac{3+\sqrt5}{4},
\]
matching the known classical value. No numerical sampling or external certificate is used in the proof.

## Relationship to prior work
Yang and Wang computed the classical von Neumann--Jordan constant of the identical \(\ell_\infty-\ell_1\) Day--James plane in 2006 and obtained \((3+\sqrt5)/4\); that is exactly the \(p=2\) specialization.

Cui, Huang, Hudzik, and Kaczmarek introduced \(C_{\mathrm{NJ}}^{(p)}\) in 2015, gave the unit-sphere scale parametrization, related it to uniform non-squareness and fixed-point geometry, and calculated it for Lebesgue spaces. Their inspected full text does not calculate the Day--James hexagonal endpoint.

A later Yang--Wang paper treats the classical quadratic von Neumann--Jordan constant on a broader class of Day--James \(\ell_p-\ell_1\) spaces. Targeted searches using the exact hexagonal norm, \(C_{\mathrm{NJ}}^{(p)}\), the critical equation, and the closed value did not locate an equivalent all-\(p\) endpoint formula.

## Limitations
The theorem treats one real two-dimensional Day--James endpoint. It does not determine the generalized exponent profile for the full Day--James family. A later equivalent computation under different notation remains a residual bibliographic risk.

## References
1. C. Yang and F. Wang, “On a new geometric constant related to the von Neumann--Jordan constant,” *Journal of Mathematical Analysis and Applications* 324 (2006), 555--565, DOI 10.1016/j.jmaa.2005.12.009; available online 2006-01-18.
2. Y. Cui, W. Huang, H. Hudzik, and R. Kaczmarek, “Generalized von Neumann--Jordan constant and its relationship to the fixed point property,” *Fixed Point Theory and Applications* 2015, Article 40, DOI 10.1186/s13663-015-0288-3; published 2015-03-18.
3. C. Yang and F. Wang, “The von Neumann--Jordan Constant for a Class of Day--James Spaces,” *Mediterranean Journal of Mathematics* 13 (2016), 1097--1108, DOI 10.1007/s00009-015-0539-x.
