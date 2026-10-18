# Singular-fiber and genus trichotomy in a Kummer smoothing of the Ceva arrangement

## Finding

Let \(k\) be an algebraically closed field of characteristic zero, let \(m\ge2\) be an integer, and, for every finite parameter \(\lambda\in k\), set
\[
C_{m,\lambda}=V\!\left((x^m-y^m)(y^m-z^m)(z^m-x^m)-\lambda(xyz)^m\right)\subset\mathbb P_k^2.
\]

These degree-\(3m\) curves form a natural one-term smoothing of the \(3m\)-line Fermat–Ceva arrangement. Their complete **reduced singular-support and geometric-genus trichotomy** is:

1. At \(\lambda=0\), the curve is the union of \(3m\) distinct lines, with exactly \(m^2\) ordinary triple points off the coordinate triangle and three ordinary \(m\)-fold points at its vertices; there are no other singularities.
2. For \(\lambda\ne0\) and \(\lambda^2+27\ne0\), the curve is geometrically integral, its only singularities are the three ordinary \(m\)-fold coordinate vertices, and the genus of its normalization is \(3m^2-3m+1\).
3. At each of the two parameters \(\lambda\) satisfying \(\lambda^2+27=0\), the curve is geometrically integral. Besides the same three ordinary \(m\)-fold vertices, it has exactly \(m^2\) ordinary nodes off the coordinate triangle, and its normalization has genus \(2m^2-3m+1\).

The two node-producing parameters arise from the two cyclic orderings of the nontrivial cube roots of unity. The genus loss at each is exactly \(m^2\). The parameter \(\lambda=\infty\), in the projective completion of the pencil, instead gives the nonreduced divisor \(m\{xyz=0\}\) and is excluded from the finite-parameter trichotomy.

## Assumptions and scope

All assertions concern geometric points over an algebraically closed characteristic-zero field, and \(m\) is any integer at least two. An *ordinary \(r\)-fold point* is a reduced plane-curve singularity with \(r\) smooth branches having pairwise distinct tangent lines; it has delta-invariant \(\binom r2\). A node is an ordinary twofold point. Genus means the genus of the smooth normalization of an integral projective curve. The singularity assertions describe reduced support and analytic branch types, not the entire Jacobian scheme. No assertion is made in positive characteristic or about \(\lambda=\infty\) beyond its displayed equation.

## Proof

**Step 1: the cubic quotient and its singular parameters.** Write \(X=x^m\), \(Y=y^m\), \(Z=z^m\). The coordinatewise power map \(\pi_m:\mathbb P^2\to\mathbb P^2\) is finite of degree \(m^2\), and our curve is the inverse image of
\[
D_\lambda: (X-Y)(Y-Z)(Z-X)-\lambda XYZ=0.
\]
On the dense torus, put \(Z=1\) and \(a=X/Z\), \(b=Y/Z\). A singular point of \(D_\lambda\) is a critical point of the rational function
\[
h(a,b)=\frac{(a-b)(b-1)(1-a)}{ab}
\]
with critical value \(\lambda\). Direct differentiation gives
\[
\frac{\partial h}{\partial a}=-\frac{(a^2-b)(b-1)}{a^2b},\qquad
\frac{\partial h}{\partial b}=-\frac{(a-1)(a-b^2)}{ab^2}.
\]
Hence \((a,b)=(1,1)\), or \(a^3=1\) and \(b=a^2\). The point \((1,1)\) has value \(0\). If \(a\) is either primitive cube root \(\omega\), then \(b=a^2\) and \(ab=1\). The Vandermonde identity for the roots \(1,\omega,\omega^2\) gives \(h(a,b)^2=-27\), with distinct opposite values. At either nonzero critical value the affine cubic \(f(a,b)=(a-b)(b-1)(1-a)-\lambda ab\) has nonsingular quadratic tangent cone: its Hessian determinant at the critical point is \(-9\). More explicitly its critical coordinates are
\[
a=-\frac{\lambda+3}{6},\qquad b=\frac{\lambda-3}{6},
\]
when \(\lambda^2=-27\). On every coordinate line \(D_\lambda\) meets the line in its two coordinate vertices and the third point with the other two coordinates equal; direct differentiation shows all these boundary points are smooth on \(D_\lambda\), for every finite \(\lambda\). Thus the cubic is smooth for \(\lambda\notin\{0,\lambda:\lambda^2=-27\}\), nodal with one node for the two nonzero exceptional values, and the three concurrent lines at \(\lambda=0\). For \(\lambda\ne0\) it is irreducible: a reducible reduced cubic cannot have precisely one ordinary node or be smooth; nonreduced reducibility would give a positive-dimensional singular set.

**Step 2: pulling back the torus.** The power map is finite étale on the dense torus, with geometric fibers of cardinality \(m^2\). Therefore every singular point of \(D_\lambda\) on the torus lifts to \(m^2\) singularities with the same completed local analytic type. This gives \(m^2\) triple points above \([1:1:1]\) for \(\lambda=0\), and \(m^2\) nodes over the unique node for each nonzero exceptional parameter. There are no others on the torus.

**Step 3: the ramification boundary.** On \(z=0\) the equation becomes, up to a nonzero factor, \(x^m y^m(x^m-y^m)=0\); cyclic permutations give the other coordinate lines. The three coordinate vertices are therefore singular. In the chart \(x=1\) at \([1:0:0]\), the lowest homogeneous part is \(-(y^m-z^m)\). Since \(k\) has characteristic zero, its \(m\) linear factors are distinct. Thus the vertex is an ordinary \(m\)-fold point; the other two vertices are symmetric. At the remaining boundary points (for example \([0:\zeta:1]\) with \(\zeta^m=1\)), a partial derivative in the nonzero coordinate direction is nonzero, so they are smooth. This proves that the singular lists are exhaustive.

**Step 4: irreducibility for nonzero parameters.** Put \(K=k(D_\lambda)\), where \(\lambda\ne0\); Step 1 gives an integral cubic. On its normalization the two smooth points \(P=[0:1:1]\), \(Q=[1:0:1]\) satisfy
\[
(v_P(X/Z),v_P(Y/Z))=(1,0),\qquad
(v_Q(X/Z),v_Q(Y/Z))=(0,1).
\]
Indeed, at \(P\), \(X/Z\) is a local parameter and \(Y/Z\) a unit; the converse holds at \(Q\). These two valuation vectors show that the classes of \(X/Z\) and \(Y/Z\) are independent modulo \(m\)-th powers: a relation \((X/Z)^a(Y/Z)^b\in K^{*m}\) forces \(a\equiv b\equiv0\pmod m\). Since \(k\) contains all \(m\)-th roots of unity, elementary Kummer theory then gives an extension of degree \(m^2\) on adjoining their \(m\)-th roots. Thus the inverse image is connected and integral on the dense torus; its closure is the full plane curve, since no coordinate line is a component. This proves geometric integrality of all nonzero fibers.

**Step 5: normalization genera.** The arithmetic genus of a degree-\(3m\) integral plane curve is \((3m-1)(3m-2)/2\). Each of the three ordinary \(m\)-fold points contributes \(m(m-1)/2\) to the genus defect. A nodal exceptional fiber has the additional \(m^2\) nodes, each contributing one. Consequently
\[
 g(\widetilde C_{m,\lambda})=
 \begin{cases}
 3m^2-3m+1,&\lambda\ne0,\quad\lambda^2+27\ne0,\\
 2m^2-3m+1,&\lambda^2+27=0.
 \end{cases}
\]
For \(\lambda=0\), factorization over \(k\) gives three pencils of \(m\) distinct lines, with pairwise intersections within each pencil at one coordinate vertex and intersections between pencils exactly when \(x^m=y^m=z^m\); this proves the claimed arrangement incidence.

## Verification

The accompanying `verify_ceva_pencil.py` uses exact SymPy rational identities to check the two critical-point derivative factorizations, the exceptional node coordinates and Hessian determinant, and a characteristic-zero Gröbner elimination giving the parameter factor \(\lambda(\lambda^2+27)\). It also enumerates all \(183\) points of \(\mathbb P^2(\mathbb F_{13})\) for \(m\in\{2,3\}\) and \(\lambda\in\{0,1,5,8\}\), comparing gradient-zero loci with independently predicted coordinate vertices and torus lifts. Run `python3 verify_ceva_pencil.py`; the success marker is `VERIFY_OK`. The finite-field tests are corroboration only, not proofs for all \(m\), and the characteristic-zero theorem does not claim the same classification over finite fields.

## Relationship to prior work

The Fermat–Ceva line arrangement and its net structure are classical; Falk and Yuzvinsky (arXiv:math/0603166, first public 2006-03-07) study the associated **different** degree-\(m\) Fermat pencil and its multinet geometry. Dimca (arXiv:math/0606442, first public 2006-06-19) treats characteristic varieties and the geometry of arrangement-associated pencils. Neither inspected work gives the singular-parameter, node, and genus trichotomy for the particular degree-\(3m\) smoothing \(C_{m,\lambda}\). The result uses elementary Kummer covering geometry and standard plane-curve genus and singularity formulas; it does not claim those general tools as new.

## Limitations

The classification applies only in characteristic zero and to finite values of \(\lambda\). It does not determine the full nonreduced Jacobian schemes, the arithmetic of fields of definition of the nodes, stable reduction of the total pencil, or the moduli of the normalizations. Earlier published equivalent computations under another description of this special pencil cannot be excluded solely by the accessible literature searches.

## References

- Michael Falk and Sergey Yuzvinsky, *Multinets, resonance varieties, and pencils of plane curves*, arXiv:math/0603166 (first version 2006-03-07), Compositio Mathematica 143 (2007), 1069–1088. https://arxiv.org/abs/math/0603166
- Alexandru Dimca, *Pencils of plane curves and characteristic varieties*, arXiv:math/0606442 (first version 2006-06-19). https://arxiv.org/abs/math/0606442
- The classical arithmetic-genus and delta-invariant formulas for reduced plane curve singularities, and Kummer theory for function fields containing roots of unity, are used in their standard forms.
