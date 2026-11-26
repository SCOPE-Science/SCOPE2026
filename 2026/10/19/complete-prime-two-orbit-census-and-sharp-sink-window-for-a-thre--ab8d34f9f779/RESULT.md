# Floquet spectra of the asymmetric two-cycles of the three-dimensional parabolic map

## Finding

For the real map
\[
F(x,y,z)=(ay^2,\;by(1-z),\;c(1-x)),\qquad a,b,c>0,
\]
put \(B=b(c-1)\). For \(B>2\), each asymmetric primitive two-cycle (the two successive \(y\)-coordinates are neither equal nor negatives of each other) has two-step characteristic polynomial
\[
P_B(\lambda)=\lambda^3-\lambda^2+2(B^2-2)\lambda-4.
\]
The unique real multiplier \(\rho\) lies in \((0,1)\). The other two multipliers are nonreal conjugates of modulus \(2/\sqrt{\rho}>2\). In particular, each of these period-two orbits is a hyperbolic saddle with a one-dimensional local stable manifold and a two-dimensional local unstable manifold. The stable dimension and the complex expanding pair are not determined by the previously known determinant-four obstruction to attraction.

## Assumptions and scope

The dynamics is on all of \(\mathbb R^3\). Multipliers refer to the derivative of the two-step return at a cycle point. The earlier full period-two census and the symmetric sink boundary are not claimed here. No assertion is made about higher periods or global invariant manifolds.

## Proof

Set \(v=abc\). The invertible affine coordinate change \(X=bcx,\ U=\sqrt v\,y,\ Z=b(1-z)\) puts the map in the form
\[
G(X,U,Z)=(U^2,\ UZ,\ X-B).
\]
If \(U,V\) are successive values of the middle coordinate along a period-two orbit, its two points must be \((V^2,U,U^2-B)\) and \((U^2,V,V^2-B)\). Hence \(V=U(U^2-B)\), \(U=V(V^2-B)\), and both \(U,V\) are nonzero on a primitive orbit. For the asymmetric case \(U\ne V\) and \(U\ne -V\), subtraction and addition of the equations give
\[
U^2+UV+V^2=B-1,\qquad U^2-UV+V^2=B+1.
\]
In particular \(UV=-1\) and \(U^2+V^2=B\). For \(B>2\), choosing \(U+V=\pm\sqrt{B-2}\) and \(U-V=\sqrt{B+2}\) gives such pairs: the two quadratic equations imply the original scalar equations by multiplying them by \(U-V\) and \(U+V\) and reversing the sum and difference. These identities specify the orbits to which the calculation applies.

At the point with middle coordinate \(U\), the derivative is
\[
J_U=\begin{pmatrix}0&2U&0\\0&V/U&U\\1&0&0\end{pmatrix};
\]
the other derivative \(J_V\) is obtained by interchanging \(U,V\). Their product is
\[
J_VJ_U=\begin{pmatrix}0&2V^2/U&2UV\\V&1&U^2/V\\0&2U&0\end{pmatrix}.
\]
The trace is \(1\), the determinant is \(4U^2V^2=4\), and the sum of the principal two-by-two minors is
\[
-2(V^3/U+U^3/V)=2(U^4+V^4)=2(B^2-2),
\]
using \(UV=-1\). This gives \(P_B\), and the same polynomial applies at the other point since both derivatives are invertible there. For real \(\lambda\),
\[
P_B'(\lambda)=3(\lambda-1/3)^2+2(B^2-2)-1/3>0
\]
when \(B>2\). Also \(P_B(0)=-4<0\) and \(P_B(1)=2(B^2-4)>0\). Thus the only real root is in \((0,1)\), and the product of the conjugate pair is \(4/\rho\). The return is a smooth local diffeomorphism at the orbit points because the determinant is nonzero. The local stable-manifold theorem for a hyperbolic fixed point of this return gives the stated dimensions.

## Verification

Run `python3 verify.py` with SymPy installed. The companion script works in the normalized coordinates, checks the symbolic characteristic polynomial of the full return derivative under \(UV=-1\), and verifies both asymmetric cycles at \(B=3\) with exact radicals. The run printed `ASYMMETRIC_FLOQUET_CHECK_OK`. These checks supplement the proof; root locations for all \(B>2\) follow from the monotonicity and product argument above.

## Relationship to prior work

Wang, Tong, Li, Zhang, Iu and Li, *Symmetry* **15** (2023), 1879, [DOI 10.3390/sym15101879](https://doi.org/10.3390/sym15101879), §2.1 Eq. (3), give the map. Their fixed-point analysis and numerical bifurcation plots are distinct from a two-step multiplier calculation. [The earlier golden-ratio sink-boundary and primitive-two-cycle census](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-a-golden-ratio-sink-boundary-and-complete-primitive-two-cycle-ce--37fa6309f5c1/RESULT.md) gives the same asymmetric orbit equations and proves that their determinant is four, so the cycles are not sinks. The claim here is the exact asymmetric characteristic polynomial and the resulting hyperbolic type and multiplier gap, not the census or nonattraction alone. The statement-level comparison does not establish absolute historical priority.
