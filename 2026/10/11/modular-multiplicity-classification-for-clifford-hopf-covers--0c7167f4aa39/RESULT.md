# Modular multiplicity classification for Clifford Hopf covers

## Finding

For every integer
\[
m\ge1,
\]
let \(\gamma_m\) be an oriented unit-sphere great circle traversed exactly \(m\) times, and let
\[
X_m:M_{\gamma_m}\to S^3
\]
be the standard Hopf immersion associated with that parametrized profile.

Choose the oriented-area representative
\[
A_m=
\begin{cases}
0,&m\ \text{even},\\
2\pi,&m\ \text{odd}.
\end{cases}
\]
Then
\[
L_m=2\pi m
\]
and Pinkall's marked lattice is
\[
\boxed{
\Gamma_m
=
\operatorname{span}_{\mathbb Z}
\left\{
(2\pi,0),
\left(\frac{A_m}{2},\pi m\right)
\right\}.
}
\]
Its marked modulus is therefore
\[
\boxed{
z_m=\frac{A_m+iL_m}{4\pi}
=
\begin{cases}
\dfrac{im}{2},&m\ \text{even},\\[5pt]
\dfrac{1+im}{2},&m\ \text{odd}.
\end{cases}
}
\]

The scale-sensitive invariants agree exactly:
\[
\boxed{
\operatorname{covol}(\Gamma_m)
=
\mathcal W(X_m)
=
\|\mathbf V_{X_m}\|(S^3)
=
2\pi^2m.
}
\]

Finally, the conformal modular classes have exactly one collision:
\[
\boxed{
[z_m]=[z_n]
\quad\Longleftrightarrow\quad
m=n
\ \text{or}\
\{m,n\}=\{1,2\}.
}
\]
Thus the conformal modulus fails to determine Clifford covering multiplicity only for the once-covered versus twice-covered pair. For every
\[
m\ge3,
\]
the modular class determines \(m\) exactly.

Consequently, if a Hopf--Willmore flow has limiting profile equal to an \(m\)-fold great circle, its limiting conformal class has the value above; except for the unique \(m=1,2\) ambiguity, that class alone resolves the endpoint multiplicity.

## Assumptions and scope

The sphere \(S^3\) and base sphere \(S^2\) use the normalizations of Ahmedou--Jakob. In particular, for a profile \(\gamma\),
\[
\mathcal W(X_\gamma)=\pi\mathcal E(\gamma),
\qquad
\mathcal E(\gamma)=\int(1+|\kappa_\gamma|^2)\,ds.
\]

The modular class is the oriented class in
\[
\mathrm{PSL}(2,\mathbb Z)\backslash\mathbb H.
\]
Reversing the orientation of an odd-fold great circle changes the representative from
\[
\frac{1+im}{2}
\]
to
\[
\frac{-1+im}{2},
\]
which differs by an integer translation and hence gives the same modular class.

The theorem is a classification of the standard Hopf immersions over multiply traversed great circles. It does not assert that, for every \(m\ge3\), there exists a simple initial Willmore-flow datum converging to that \(m\)-fold endpoint.

## Proof

A unit-sphere great circle has length
\[
2\pi
\]
and geodesic curvature zero. Hence its \(m\)-fold traversal has
\[
L_m=2\pi m,
\qquad
\mathcal E(\gamma_m)=2\pi m.
\]

Its oriented area is \(m\) times the hemisphere area,
\[
2\pi m
\quad\text{modulo }4\pi.
\]
Thus one may take
\[
A_m=0
\]
for even \(m\), and
\[
A_m=2\pi
\]
for odd \(m\).

The Pinkall lattice formula gives
\[
\Gamma_m
=
\operatorname{span}_{\mathbb Z}
\left\{
(2\pi,0),
\left(\frac{A_m}{2},\frac{L_m}{2}\right)
\right\},
\]
which is exactly the displayed lattice. Its covolume is
\[
\left|
\det
\begin{pmatrix}
2\pi&A_m/2\\
0&\pi m
\end{pmatrix}
\right|
=
2\pi^2m.
\]

The Hopf--elastic energy identity and \(\kappa_{\gamma_m}=0\) give
\[
\mathcal W(X_m)
=
\pi\mathcal E(\gamma_m)
=
2\pi^2m.
\]
The multiplicity formula for a profile that is an \(m\)-fold cover of an embedded curve gives
\[
\mathbf V_{X_m}
=
m\,|T_{\mathrm{Cl}}|.
\]
Since a once-covered Clifford torus has area \(2\pi^2\),
\[
\|\mathbf V_{X_m}\|(S^3)=2\pi^2m.
\]

It remains to classify the modular classes. The Pinkall modulus is
\[
z_m
=
\frac{A_m+iL_m}{4\pi},
\]
so
\[
z_m=
\begin{cases}
im/2,&m\text{ even},\\
(1+im)/2,&m\text{ odd}.
\end{cases}
\]

For \(m=1\),
\[
z_1=\frac{1+i}{2}.
\]
Applying the modular inversion
\[
S(z)=-\frac1z
\]
and then the translation
\[
T(z)=z+1
\]
gives
\[
T(S(z_1))=i=z_2.
\]
Hence
\[
[z_1]=[z_2].
\]

Now let \(m\ge2\). If \(m\) is even, then
\[
z_m=\frac{im}{2}
\]
lies in the standard closed fundamental domain
\[
\mathcal F
=
\left\{
z\in\mathbb H:
|\operatorname{Re}z|\le\frac12,\ |z|\ge1
\right\}.
\]
If \(m\ge3\) is odd, then
\[
z_m=\frac12+\frac{im}{2}
\]
lies on the right vertical boundary of \(\mathcal F\), with
\[
|z_m|>1.
\]

The standard fundamental-domain uniqueness theorem says that two points of \(\mathcal F\) can be modularly equivalent only if they are identical or are paired by the boundary identifications. On the vertical boundary, the only identification is translation between
\[
-\frac12+iy
\quad\text{and}\quad
\frac12+iy,
\]
which preserves the imaginary part. On the unit-circle boundary, the inversion identifies the corresponding paired points; among the displayed representatives only \(z_2=i\) lies there, and it is fixed by inversion.

Therefore, for \(m,n\ge2\),
\[
[z_m]=[z_n]
\quad\Longrightarrow\quad
m=n.
\]
Combining this with
\[
[z_1]=[z_2]
\]
proves the complete collision classification.

## Verification

The bundled checker verifies the lattice determinant, the Willmore-energy formula, and the explicit modular transformation
\[
T(S((1+i)/2))=i.
\]
It also verifies the algebraic fundamental-domain inequalities in the even and odd cases.

The proof of modular injectivity for \(m\ge2\) uses the standard global fundamental-domain theorem for \(\mathrm{PSL}(2,\mathbb Z)\), not a finite search over modular matrices.

## Relationship to prior work

Pinkall's classical Hopf-torus construction gives the marked lattice generated by
\[
(2\pi,0)
\quad\text{and}\quad
(A/2,L/2),
\]
and identifies the once-covered great-circle lift with a square Clifford torus.

Ahmedou and Jakob extend this marked-lattice framework to the full Hopf--Willmore flow and prove endpoint multiplicity and marked-lattice convergence. They explicitly analyze a twice-covered great-circle endpoint: its limiting marked lattice has covolume \(4\pi^2\) while its modular class is again the square class. Their Remark 10.2 emphasizes that conformal type and multiplicity therefore carry different information.

The result here determines the complete arithmetic boundary of that failure for all great-circle covers. It shows that the loss of multiplicity information is not persistent: among all \(m\)-fold Clifford Hopf covers, the only modular collision is the pair \(m=1\) and \(m=2\).

Targeted searches using Hopf-torus, great-circle-cover, Pinkall-lattice, modular-class, and multiplicity formulations did not locate this all-\(m\) classification.

## Limitations

The theorem classifies multiply covered Clifford Hopf immersions, not arbitrary Hopf tori or arbitrary multiply covered Willmore tori.

For \(m\ge3\), the statement is static unless a flow with such an endpoint is supplied independently. No existence theorem for simple initial data converging to every higher multiplicity is claimed.

The modular-class classification uses the oriented genus-one moduli space. The stated class is nevertheless unchanged by reversing the orientation of the great-circle profile because the two odd-case representatives differ by an integer translation.

## References

1. Mohameden Ahmedou and Ruben Jakob, *Hopf Reduction and Multiplicity-Resolved Endpoints for the Classical Willmore Flow of Hopf Tori*, arXiv:2609.26997v1, first submitted 22 September 2026.
2. Udo Pinkall, *Hopf tori in \(S^3\)*, Inventiones Mathematicae 81 (1985), 379--386.
3. Ruben Jakob, *Corrections to: "The Willmore flow of Hopf-tori in the \(3\)-sphere"*, arXiv:2602.13228v1, first submitted 27 January 2026.
