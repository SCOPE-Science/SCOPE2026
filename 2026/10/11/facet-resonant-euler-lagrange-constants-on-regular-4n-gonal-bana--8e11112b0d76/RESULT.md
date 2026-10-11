# Facet-resonant Euler--Lagrange constants on regular \(4n\)-gonal Banach planes
## Finding
For every integer \(n\ge1\), let \(X_{4n}\) be the real two-dimensional Banach space whose unit ball is a Euclidean regular \(4n\)-gon circumscribed about the Euclidean unit disk. Put
\[
\alpha=\frac{\pi}{4n}.
\]
For the Liu--Li Euler--Lagrange geometric constant
\[
L_{\mathrm{YJ}}(\lambda,\mu,X)
=
\sup_{(x,y)\ne(0,0)}
\frac{\|\lambda x+\mu y\|^2+\|\mu x-\lambda y\|^2}
{(\lambda^2+\mu^2)(\|x\|^2+\|y\|^2)},
\qquad
\lambda,\mu>0,
\]
one has the parameter-independent upper bound
\[
L_{\mathrm{YJ}}(\lambda,\mu,X_{4n})
\le
\sec^2\alpha.
\]

The bound is attained at the balanced parameter ratio
\[
\frac{\mu}{\lambda}=1.
\]
It is also attained at every facet-resonant ratio
\[
\frac{\mu}{\lambda}
=
\tan((2k+1)\alpha),
\qquad
k=0,1,\ldots,n-1.
\]
Consequently, at each of those ratios,
\[
L_{\mathrm{YJ}}(\lambda,\mu,X_{4n})
=
\sec^2\!\left(\frac{\pi}{4n}\right).
\]

For example, on the regular octagonal plane the three displayed saturation ratios include
\[
\sqrt2-1,\qquad 1,\qquad \sqrt2+1,
\]
and the common value is
\[
4-2\sqrt2.
\]
On the regular dodecagonal plane the facet-resonant ratios are
\[
2-\sqrt3,\qquad 1,\qquad 2+\sqrt3,
\]
and the common value is
\[
8-4\sqrt3.
\]

## Assumptions and scope
All spaces and scalars are real. Let
\[
N=4n.
\]
Normalize the regular \(N\)-gon to have Euclidean inradius \(1\). Its outward unit facet normals have directions
\[
2j\alpha,
\qquad
j\in\mathbb Z,
\]
and its vertices have Euclidean radius
\[
R=\sec\alpha
\]
and directions
\[
(2j+1)\alpha.
\]

If \(\|\cdot\|_N\) denotes the polygonal norm, then for every vector \(z\),
\[
\|z\|_N\le\|z\|_2
\le
R\|z\|_N.
\tag{1}
\]
The first inequality follows because the norm is the maximum of Euclidean inner products with unit facet normals. The second follows because the farthest points of the inradius-one polygon are its vertices, all at Euclidean distance \(R\).

The claim identifies a natural finite family of parameter ratios at which the sharp Euclidean-comparison ceiling is attained. It does not classify all parameter ratios at which equality may occur.

## Proof
Let
\[
S=\lambda^2+\mu^2.
\]
For arbitrary \(x,y\in X_N\), the first half of (1) gives
\[
\|\lambda x+\mu y\|_N^2
+
\|\mu x-\lambda y\|_N^2
\le
\|\lambda x+\mu y\|_2^2
+
\|\mu x-\lambda y\|_2^2.
\]
The two-by-two coefficient matrix
\[
\begin{pmatrix}
\lambda&\mu\\
\mu&-\lambda
\end{pmatrix}
\]
is Euclidean orthogonal up to the scale \(\sqrt S\). Therefore
\[
\|\lambda x+\mu y\|_2^2
+
\|\mu x-\lambda y\|_2^2
=
S\bigl(\|x\|_2^2+\|y\|_2^2\bigr).
\]
Using the second half of (1),
\[
S\bigl(\|x\|_2^2+\|y\|_2^2\bigr)
\le
SR^2\bigl(\|x\|_N^2+\|y\|_N^2\bigr).
\]
After division by the denominator in the definition of \(L_{\mathrm{YJ}}\),
\[
L_{\mathrm{YJ}}(\lambda,\mu,X_N)\le R^2=\sec^2\alpha.
\tag{2}
\]

We first attain (2) at the balanced ratio. Since \(N\) is divisible by \(4\), the coordinate axes are facet-normal directions. Take the adjacent unit-ball vertices
\[
x=R(\cos\alpha,\sin\alpha),
\qquad
y=R(\cos\alpha,-\sin\alpha).
\]
Then
\[
x+y=(2,0)
\]
and
\[
x-y=(0,2\tan\alpha).
\]
Both output directions are facet-normal directions, so polygonal and Euclidean norms agree on these rays. At \(\lambda=\mu\), common parameter scaling cancels from the quotient, and hence
\[
L_{\mathrm{YJ}}(\lambda,\lambda,X_N)
\ge
\frac{4+4\tan^2\alpha}{4}
=
\sec^2\alpha.
\]
Together with (2), this is equality.

Now fix
\[
k\in\{0,1,\ldots,n-1\},
\qquad
\phi=(2k+1)\alpha.
\]
The constant is unchanged when both parameters are multiplied by the same positive scalar, so take
\[
\lambda=\cos\phi,
\qquad
\mu=\sin\phi.
\]
Choose the quarter-turn pair of unit-ball vertices
\[
x=R(\cos\alpha,\sin\alpha),
\]
\[
y=R\left(\cos\left(\alpha+\frac{\pi}{2}\right),
\sin\left(\alpha+\frac{\pi}{2}\right)\right).
\]
The second vector is a vertex because
\[
\frac{\pi}{2}=2n\alpha.
\]
In complex notation, identifying the Euclidean plane with \(\mathbb C\),
\[
\lambda x+\mu y
=
Re^{i(\alpha+\phi)}
\]
and
\[
\mu x-\lambda y
=
Re^{i(\alpha+\phi-\pi/2)}.
\]
Their directions are
\[
\alpha+\phi
=
2(k+1)\alpha
\]
and
\[
\alpha+\phi-\frac{\pi}{2}
=
2(k+1-n)\alpha.
\]
Both are facet-normal directions. Therefore
\[
\|\lambda x+\mu y\|_N
=
\|\mu x-\lambda y\|_N
=
R.
\]
Because
\[
\lambda^2+\mu^2=1
\]
and
\[
\|x\|_N=\|y\|_N=1,
\]
the defining quotient at this pair equals
\[
\frac{R^2+R^2}{2}
=
R^2.
\]
Combining with (2) proves
\[
L_{\mathrm{YJ}}(\lambda,\mu,X_{4n})
=
\sec^2\!\left(\frac{\pi}{4n}\right)
\]
at every stated facet-resonant ratio.

## Verification
The proof is analytic. Its only geometric inputs are the exact inradius/circumradius comparison for a regular polygon and the fact that vertex directions and facet-normal directions alternate by the half-step \(\alpha\).

The bundled `verify.py` reconstructs the inradius-one polygon norm for representative regular \(4n\)-gons. It checks the global norm sandwich on deterministic test directions, verifies the balanced extremizer, and verifies every stated odd-half-step resonance for
\[
1\le n\le30.
\]
The script also checks the octagonal and dodecagonal closed forms.

These finite computations are reproducibility checks only. The universal quantifier over \(n\), the upper bound, and the resonance construction are proved symbolically above.

## Relationship to prior work
Liu and Li introduced \(L_{\mathrm{YJ}}(\lambda,\mu,X)\) from an Euler--Lagrange characterization of inner-product spaces. They proved the general range
\[
1\le L_{\mathrm{YJ}}(\lambda,\mu,X)\le2,
\]
showed that value \(1\) characterizes Hilbert spaces, and derived comparisons with the von Neumann--Jordan and James constants. The inspected full article contains no regular-polygon, octagonal, or dodecagonal computation.

A later public result gives the universal parameter envelope
\[
L_{\mathrm{YJ}}(\lambda,\mu,X)
\le
\frac{(\lambda+\mu)^2}{\lambda^2+\mu^2}.
\]
That statement applies to arbitrary Banach spaces but does not imply the present regular-polygon value. At the smallest facet resonance, for instance, its right-hand side is generally much larger than
\[
\sec^2\!\left(\frac{\pi}{4n}\right),
\]
and it supplies no matching lower construction.

The present result instead uses the Euclidean inradius/circumradius geometry of regular \(4n\)-gons. The parameter angle locks to the alternating vertex/facet-normal lattice, causing both transformed vectors to land exactly on facet-normal rays. This explains a discrete family of sharp non-Hilbert saturation points for the two-parameter invariant.

## Limitations
The theorem gives a sharp global ceiling and an explicit family of parameter ratios attaining it. It does not claim that the displayed ratios are the only saturation ratios.

The result is restricted to regular polygons with side count divisible by \(4\). The quarter-turn vertex construction is essential to the unbalanced resonance proof.

Bibliographic and semantic searches cannot establish absolute novelty. An equivalent result could exist under a different normalization of regular polygons or a reparameterization by the angle
\[
\phi=\arctan(\mu/\lambda).
\]

## References
1. Q. Liu and Y. Li, “On a New Geometric Constant Related to the Euler-Lagrange Type Identity in Banach Spaces,” Mathematics 9 (2021), 116, doi:10.3390/math9020116. Published 7 January 2021.
