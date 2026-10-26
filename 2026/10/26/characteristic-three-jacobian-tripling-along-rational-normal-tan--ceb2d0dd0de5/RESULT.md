# Characteristic-three Jacobian tripling along rational-normal tangential surfaces

## Finding
Let \(k\) be algebraically closed and \(d\geq3\). Write \(C_d\subset\mathbb P^d_k\) for the rational normal curve with coordinates \([S^d:S^{d-1}T:\cdots:T^d]\), and \(T_d\) for the **reduced** union of its projective tangent lines. Let \(Y_d\subset T_d\) be its intrinsic singular scheme, defined by \(\operatorname{Fitt}_2\Omega_{T_d/k}\).

In characteristic three, \(Y_d\) is a multiplicity-three, locally curvilinear thickening of \(C_d\). If \(\mathcal I\subset\mathcal O_{Y_d}\) is the ideal of its reduction, then \(\mathcal I^3=0\), and
\[
\mathcal I^j/\mathcal I^{j+1}\cong\mathcal O_{\mathbb P^1}(-4j)\quad(j=0,1,2),
\]
where \(j=0\) denotes \(\mathcal O_{Y_d}/\mathcal I\). Consequently
\[
\deg Y_d=3d,\qquad P_{Y_d}(n)=3dn-9.
\]
By contrast, in characteristic zero or characteristic \(p\geq5\), the same construction gives a multiplicity-two thickening with graded pieces \(\mathcal O_{\mathbb P^1}\) and \(\mathcal O_{\mathbb P^1}(-4)\), hence \(\deg Y_d=2d\) and \(P_{Y_d}(n)=2dn-2\). In characteristic two the tangential surface is smooth and \(Y_d\) is empty; this last fact is already known from the scroll description.

For \(d=3\) in characteristic three, the tangential quartic is
\[
X_0^2X_3^2+X_1^3X_3+X_0X_2^3=0;
\]
its singular scheme is the complete intersection of the two cubics \(2X_0X_3^2+X_2^3\) and \(2X_0^2X_3+X_1^3\), of degree nine and arithmetic genus ten.

## Assumptions and scope
All schemes are over an algebraically closed field. The tangential variety is taken with its **reduced image scheme**, not as the possibly inseparable scheme-theoretic image with multiplicity. The singular scheme is intrinsic to that reduced surface. The degree is the geometric projective degree of the one-dimensional singular scheme, not the degree of the two-dimensional tangential surface. The Hilbert polynomial is with respect to \(\mathcal O_{\mathbb P^d}(1)\), and is asserted for all \(d\ge3\) and precisely the characteristics stated.

## Proof
On the chart \(X_0=1\), the tangent-line parametrization is
\[
X_i=t^i+i s t^{i-1},\qquad0\le i\le d.
\]
Put \(u=t+s\). Expanding \((u-s)^i+i s(u-s)^{i-1}\) shows that the coefficient of \(s\) vanishes for every \(i\). In odd characteristic,
\[
X_1=u,\quad X_2=u^2-s^2,\quad X_3=u^3-3us^2+2s^3.
\]
Because \(2\) is invertible, the three indicated coordinates recover \(u\), \(y=s^2\), and \(z=s^3\). Every later coordinate is a polynomial in these three generators: its expansion has no term of degree one in \(s\), and every \(s^r\) with \(r\ge2\) belongs to \(k[s^2,s^3]\). Hence the reduced affine coordinate ring on this chart is **exactly**
\[
k[u,s^2,s^3]\simeq k[u,y,z]/(z^2-y^3).
\]
This is an equality of coordinate rings, not merely an equality of tangent cones or of completed germs.

The presentation of relative differentials has one row, the gradient of \(z^2-y^3\), so the intrinsic singular subscheme has ideal \((3y^2,2z)\). In characteristic three its coordinate ring is \(k[u,y]/(y^3)\); in characteristic zero or \(p\ge5\) it is \(k[u,y]/(y^2)\). Its reduced support is \(y=z=0\), the rational normal curve on this chart.

There are no additional singular points away from the curve. The analogous chart near the point of the curve at infinity is obtained by reversing the projective coordinates. At other points with \(X_0=0\), the tangent parametrization near a finite tangent direction can be written \([v\nu(t)+\nu'(t)]\) where \(v=1/s\). On \(X_1\ne0\), the first two affine functions are \(A=v/(1+vt)\) and \(B=(vt^2+2t)/(1+vt)\). At \(v=0\) the Jacobian of \((A,B)\) in \((v,t)\) has determinant \(2\ne0\). The formal inverse-function theorem thus identifies the completed image germ there with a smooth two-variable power-series ring: the remaining projective coordinates are regular series in \(A,B\). The tangent-line parametrization is geometrically one-to-one outside the curve, as follows both from the cusp coordinates above and from \(B=2t\) on \(A=0\); the tangent line at infinity is handled by reversal. This proves global support and local structure in odd characteristic.

To calculate the nilpotent line bundles, compare the two standard charts of \(C_d\). If \(t\ne0\), the reversed tangent parameters are \(q=1/t\) and
\[
r=-\frac{s}{t(t+d s)}.
\]
Thus \(r^2\equiv t^{-4}s^2\) modulo the square of the nilradical (and modulo the local singular ideal). The associated graded of the nilradical has transition \(t^{-4j}\) in grade \(j\), giving \(\mathcal O_{\mathbb P^1}(-4j)\). The same calculation holds in characteristic three through grade two; terms involving \(s^3=z\) are zero on its singular scheme. Additivity of Euler characteristic for the filtration, using \(\mathcal O_{\mathbb P^d}(1)|_{C_d}=\mathcal O_{\mathbb P^1}(d)\), gives
\[
P_{Y_d}(n)=\sum_{j=0}^{m-1}(dn-4j+1)
=m dn+m-2m(m-1),
\]
where \(m=3\) in characteristic three and \(m=2\) otherwise in odd characteristic. The leading coefficient gives the stated degrees.

In characteristic two the first coordinates instead generate \(k[u,s^2]\), and every other \(X_i\) belongs to this polynomial ring. Together with the reversed and tangent-direction charts this is the known smooth rational-scroll description; see Raicu's account below. Finally, for \(d=3\) and characteristic three, direct substitution establishes the displayed quartic; its only nonzero partial derivatives are precisely the two displayed cubics. They form a height-two regular sequence, so the complete-intersection Hilbert polynomial is \(9n-9\), as predicted.

## Verification
Run the standalone \(\texttt{check_tangent.py}\) with Python and SymPy. It checks the cancellation of the linear tangent parameter term for degrees three through eleven in characteristics two, three, five, seven; the identities recovering the cusp parameters; the characteristic-three quartic and its Jacobian derivatives; and the \((3,3)\) complete-intersection Hilbert polynomial. The arbitrary-degree theorem follows from the symbolic binomial cancellation and the geometric chart and gluing arguments above, not from bounded experiments.

## Relationship to prior work
The local tangent parametrization, the characteristic-two scroll identification, and characteristic-sensitive equations and Betti numbers of \(T_d\) occur in Claudiu Raicu's *Syzygies of the tangential variety to a rational normal curve*. Oeding and Raicu's *Tangential varieties of Segre–Veronese varieties* (arXiv:1111.6202, originally submitted 2011-11-26) determines ideal generators and representation-theoretic coordinate rings, with characteristic-zero theorems. The present statement concerns a **different invariant**: the intrinsic Jacobian singular subscheme in characteristic three, its nilpotent filtration, and its Hilbert polynomial. The cuspidal transverse type is classical; its local Jacobian length alone does not give the global nilpotent twisting or Hilbert polynomial without gluing.

## Limitations
The assertion makes no claim of independent peer certification, or of describing the entire deformation family of tangential surfaces over a mixed-characteristic base. Possible equivalent treatments under other terminology in classical modular geometry or singular-scheme literature remain a literature risk. The characteristic-two smooth-scroll fact is established prior art, used only for comparison. This result concerns scheme-theoretic singular loci, not homogeneous ideal resolutions.

## References
- Luke Oeding and Claudiu Raicu, *Tangential varieties of Segre–Veronese varieties*, arXiv:1111.6202v1 (first public 2011-11-26), https://arxiv.org/abs/1111.6202.
- Claudiu Raicu, *Syzygies of the tangential variety to a rational normal curve*, notes, https://www.math.utah.edu/ca/Raicu_1.pdf (publication date not asserted).
- Marian Aprodu, Gavril Farkas, Stefan Papadima, Claudiu Raicu and Jerzy Weyman, *Koszul modules and Green's conjecture*, arXiv:1810.11635 (later supporting literature).
