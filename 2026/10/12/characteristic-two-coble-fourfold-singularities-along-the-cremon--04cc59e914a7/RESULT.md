# Characteristic-two Coble fourfold singularities along the Cremona–Richmond configuration
## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). Dolgachev identifies the GIT quotient \(P_2^6=(\mathbb P^2)^6/\!/\operatorname{{PGL}}_3\) with the weighted hypersurface
\[
\mathcal V=V(G)\subset\mathbb P(1,1,1,1,1,2),
\qquad G=w^2+wq+b,
\]
where
\[
q=y_2y_3+y_1y_4+y_0(y_0+y_1+y_2+y_3+y_4)
\]
and
\[
b=y_0y_1y_4(y_0+y_1+y_2+y_3+y_4).
\]
The involution \(w\mapsto w+q\) has fixed locus an inseparable double cover of the smooth quadric \(Q=V(q)\). The source describes on this fixed locus the lifted Cremona–Richmond \((15_3)\) configuration: fifteen rational curves, with three distinguished incidence points on each curve and three curves through each incidence point.

Every one of these fifteen lifted curves is contained in \(\operatorname{{Sing}}(\mathcal V)\). Moreover, the ambient singularity changes type precisely at the three Cremona–Richmond incidence points on each curve. At a non-incidence point, a transverse slice has a nondegenerate quadratic tangent cone, hence an ordinary quadratic double point. At an incidence point, the quadratic tangent cone is instead the union of two distinct hyperplanes. The three lifted Cremona–Richmond curves through such a point have distinct tangent directions.

For a representative curve
\[
L=\{y_0=y_1=y_2=w=0\},
\]
work on the chart \(y_4=1\), put \(t=y_3\), and write \(x_i=y_i\) for \(i=0,1,2\). The quadratic part in the four normal variables \(w,x_0,x_1,x_2\) is
\[
Q_t=w^2+w((t+1)x_0+x_1+t x_2)+(t+1)x_0x_1.
\]
Its polar bilinear form has determinant
\[
t^2(t+1)^2.
\]
Thus it is nondegenerate for \(t\notin\{0,1,\infty\}\). At \(t=0\),
\[
Q_0=(w+x_0)(w+x_1),
\]
and the other two special points have the same local type by the symmetry of the Cremona–Richmond configuration. Consequently the ambient characteristic-two Coble fourfold has a sharp local singularity jump along this canonical fifteen-curve stratum exactly at its fifteen incidence points.

## Assumptions and scope
The ground field is algebraically closed of characteristic \(2\). The weighted coordinate \(w\) has weight \(2\), while the \(y_i\) have weight \(1\). The statement concerns the fifteen lifted curves identified by Dolgachev and the local analytic behavior of \(\mathcal V\) along them. It does not assert that these curves exhaust the complete reduced singular locus of \(\mathcal V\), nor does it determine the nonreduced Jacobian scheme or construct a resolution.

An ordinary quadratic double point here means that, after taking a transverse three-dimensional hypersurface slice to a smooth point of one of the singular curves, the degree-two tangent cone is a smooth quadric in \(\mathbb P^3\). In characteristic \(2\), this is detected by nondegeneracy of the polar alternating form.

## Proof
Differentiating \(G=w^2+wq+b\) in characteristic \(2\) gives
\[
G_w=q,
\qquad
G_{y_i}=wq_{y_i}+b_{y_i}.
\]
Hence any singular point of \(\mathcal V\) lies in the fixed locus \(q=0\). Consider the explicit lifted curve \(L\) above. Substituting \(y_0=y_1=y_2=w=0\) into \(G\) and all six partial derivatives gives zero identically, so \(L\subset\operatorname{{Sing}}(\mathcal V)\). Dolgachev's \(\mathfrak S_6\)-action on \(P_2^6\) preserves \(\mathcal V\) and is transitive on the fifteen lines of the Cremona–Richmond configuration; therefore all fifteen lifted curves lie in the ambient singular locus.

On \(y_4=1\), expansion around \(L\) gives the displayed normal quadratic form \(Q_t\). In the ordered normal variables \(w,x_0,x_1,x_2\), the polar matrix is
\[
\begin{{pmatrix}}
0&t+1&1&t\\
t+1&0&t+1&0\\
1&t+1&0&0\\
t&0&0&0
\end{{pmatrix}},
\]
whose determinant is \(t^2(t+1)^2\). Therefore the transverse tangent cone is a smooth quadric for finite \(t\neq0,1\). The source's \((15_3)\) incidence description identifies the third exceptional point on \(L\) as \(t=\infty\). At \(t=0\), direct factorization gives \(Q_0=(w+x_0)(w+x_1)\). Symmetry transfers this local model to every incidence point.

At the representative incidence point \(P=[0:0:0:0:1;0]\), three lifted singular curves are parametrized homogeneously by
\[
[0:0:0:u:v;0],
\qquad
[0:0:u:0:v;0],
\qquad
[u:u:0:0:v;uv].
\]
Direct substitution into \(G\) and its partial derivatives verifies that all three lie in \(\operatorname{{Sing}}(\mathcal V)\). On the chart \(v=1\), their tangent directions at \(P\) are distinct.

## Verification
The accompanying exact symbolic script works over \(\mathbb F_2\). It reconstructs \(G\), verifies that the three representative lifted curves annihilate \(G\) and every first derivative, extracts \(Q_t\), checks the determinant \(t^2(t+1)^2\), and verifies the factorization \(Q_0=(w+x_0)(w+x_1)\). It also enumerates the \(15\) rational points and \(15\) projective lines on \(Q(\mathbb F_2)\), checking the \((15_3)\) incidence counts. The finite-field enumeration is only a consistency check for the Cremona–Richmond combinatorics; the local singularity argument itself is symbolic in the parameter \(t\).

## Relationship to prior work
Dolgachev supplies the characteristic-two equation, the separable double-cover description, the association involution, the lifted fifteen-line singular configuration on the fixed locus, its \((15_3)\) incidence, and the \(\mathfrak S_6\)-action. The additional statement here concerns the ambient fourfold: the fifteen lifted curves themselves are singular curves of \(\mathcal V\), with generic transverse ordinary quadratic double points and a different reducible quadratic tangent cone at the fifteen incidence points.

In characteristic zero, Cheltsov--Kuznetsov--Shramov study the classical Coble fourfold, whose singular locus is the Cremona–Richmond configuration and which admits small resolutions. Their model is a double cover branched over the Igusa quartic. That result does not determine the local characteristic-two behavior of Dolgachev's Artin--Schreier-type equation, where the differential identities and quadratic forms change essentially because \(2=0\).

## Limitations
No claim is made that the fifteen curves exhaust all singular points of \(\mathcal V\). No primary decomposition of the Jacobian ideal, scheme-theoretic multiplicity along the curves, completed normal form at an incidence point beyond its quadratic tangent cone, or global resolution is asserted. The characteristic-two hypothesis is essential to the displayed equation and derivative computation.

A bibliographic residual risk remains that the same local calculation may occur in older invariant-theoretic or modular literature under a different presentation of \(P_2^6\). The full-text and targeted searches described in the review did not locate such a statement.

## References
I. V. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, arXiv:2302.13101v1; Bulletin of the London Mathematical Society 56 (2024), 1903–1919, DOI 10.1112/blms.13033.

I. Cheltsov, A. Kuznetsov and C. Shramov, *Coble fourfold, S6-invariant quartic threefolds, and Wiman–Edge sextics*, arXiv:1712.08906v1; Algebraic & Number Theory 14 (2020), 213–302, DOI 10.2140/ant.2020.14.213.
