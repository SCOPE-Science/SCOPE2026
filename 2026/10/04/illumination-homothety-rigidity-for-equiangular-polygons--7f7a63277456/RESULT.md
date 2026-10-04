# Illumination-homothety rigidity for equiangular polygons

## Finding

Let \(P\subset\mathbb R^2\) be a convex equiangular \(m\)-gon. If one illumination body of \(P\) is a positive homothetic copy of \(P\), then \(P\) is a regular polygon.

Equivalently, let
\[
G_{P,\lambda}(t)
=
A\!\left(\operatorname{conv}\bigl(P\cup(\lambda P+t)\bigr)\right),
\qquad 0\le\lambda<1.
\]
If one sublevel set of \(G_{P,\lambda}\) is a positive homothetic copy of \(P\), then \(P\) is regular.

This proves the polygonal illumination-homothety conjecture of Horváth and Lángi on the full class of equiangular convex polygons. Their theorem settles only the special \((1,1)\)-extension by proving affine regularity; the argument here treats every extension allowed by their general polygonal characterization.

## Assumptions and scope

An equiangular convex \(m\)-gon has exterior angle \(2\pi/m\), so its outward side normals occur at equally spaced angles. “Positive homothetic copy” allows an arbitrary homothety center and a positive scale factor.

Horváth and Lángi prove that the existence of a homothetic illumination body is equivalent to the existence of a \((k,l)\)-extension whose sides correspond homothetically to the sides of \(P\). Their Theorem 8 further forces
\[
k+l=2q,
\qquad
2q+1<\frac m2,
\]
for some integer \(q\ge1\), and the side corresponding to the \(i\)-th side of \(P\) has endpoints
\[
p_{i-q-1,i+q}
\quad\text{and}\quad
p_{i-q,i+q+1},
\]
where \(p_{a,b}\) is the intersection of the sidelines \(L_a\) and \(L_b\).

The same paper proves that the homothetic-convex-hull formulation for any \(0\le\lambda<1\) is equivalent, after rescaling the sublevel set, to the illumination-body formulation. Thus it suffices to prove the illumination statement.

## Proof

Translate the homothety center to the origin. The homothetic illumination body contains \(P\) in its interior, so the center belongs to the interior of \(P\). Let
\[
\phi=\frac{2\pi}{m}
\]
and write the outward unit normals as
\[
u_i=(\cos(\theta_0+i\phi),\sin(\theta_0+i\phi)).
\]
Write the sideline \(L_i\) in support form
\[
L_i=\{x:\langle u_i,x\rangle=h_i\},
\]
where every \(h_i>0\).

Apply the cited polygonal characterization. Put \(k+l=2q\). Since the homothetic image of the \(i\)-th side lies on the image of \(L_i\), there is one scale factor \(\mu>1\) such that
\[
\langle u_i,p_{i-q-1,i+q}\rangle=\mu h_i
\]
for every \(i\).

For two nonparallel support lines
\[
\langle u_a,x\rangle=h_a,
\qquad
\langle u_b,x\rangle=h_b,
\]
a direct two-by-two determinant calculation gives
\[
\langle u_i,p_{a,b}\rangle
=
\frac{h_a\sin(\theta_b-\theta_i)+h_b\sin(\theta_i-\theta_a)}{\sin(\theta_b-\theta_a)}.
\]
Use
\[
a=i-q-1,
\qquad
b=i+q.
\]
Because \(2q+1<m/2\), all sines below are positive. With
\[
A=\sin(q\phi),
\qquad
B=\sin((q+1)\phi),
\qquad
D=\sin((2q+1)\phi),
\]
we obtain the circulant recurrence
\[
A h_{i-q-1}+B h_{i+q}=\mu D h_i.
\tag{1}
\]

Sum (1) over all cyclic indices. Since \(\sum_i h_i>0\),
\[
\mu D=A+B.
\]
Thus
\[
A h_{i-q-1}+B h_{i+q}=(A+B)h_i.
\tag{2}
\]

Take the discrete Fourier transform of the real cyclic sequence \((h_i)\). If a Fourier mode with root of unity \(z\) has nonzero coefficient, (2) requires
\[
A z^{-(q+1)}+Bz^q=A+B.
\tag{3}
\]
Since \(A,B>0\) and both powers of \(z\) have modulus one, the left side of (3) is a positive weighted sum of two points of the unit circle whose modulus is at most \(A+B\). Equality with the positive real number \(A+B\) forces equality in the triangle inequality and zero argument. Hence
\[
z^{-(q+1)}=1
\qquad\text{and}\qquad
z^q=1.
\]
Because consecutive integers \(q\) and \(q+1\) are coprime, this implies \(z=1\).

Therefore every nonconstant Fourier coefficient of \((h_i)\) vanishes. All supports are equal:
\[
h_0=h_1=\cdots=h_{m-1}.
\]
A convex polygon whose outward normals are equally spaced and whose corresponding supports from one center are all equal is the intersection of equally spaced tangent half-planes to one circle. It is therefore a regular \(m\)-gon. This proves the claim.

## Verification

The proof is exact and uses only the published polygonal extension characterization, elementary line intersection, and the discrete Fourier transform of a circulant recurrence.

The accompanying `verify.py` performs two independent finite stress tests. First, for all admissible \((m,q)\) with \(q\le30\) and \(m\le250\), it checks that no nonconstant root-of-unity mode satisfies (3). Second, it reconstructs the relevant sideline intersections for regular support data and checks that both endpoints lie on the predicted homothetic side.

The replay prints:

`VERIFY_OK equiangular illumination-homothety rigidity`

These finite checks are not used to infer the theorem. The all-\(m\) rigidity follows from equality in the triangle inequality in (3).

## Relationship to prior work

Horváth and Lángi pose the problem of determining whether every polygon with a homothetic illumination body must be affinely regular. Their Theorem 8 gives an exact extension-theoretic characterization and proves affine regularity only when the relevant extension is the \((1,1)\)-extension. The accessible full text contains no occurrence of “equiangular.”

Lángi's earlier work characterizes many vertex recurrences that force affine regularity. That theory is related in spirit, but the illumination condition here first has to be converted into a recurrence for side support numbers. The resulting recurrence has positive coefficients tied to the equal angular spacing, and its Fourier spectrum collapses by a two-term triangle-equality argument.

Targeted searches for equiangular polygons, homothetic illumination bodies, generalized homothety, and \((k,l)\)-extensions located no statement covering this subclass rigidity result.

## Limitations

The argument uses equal angular spacing of the side normals. It does not settle the full polygonal problem for arbitrary convex polygons, nor does it classify non-equiangular solutions of higher \((k,l)\)-extension equations.

The conclusion is Euclidean regularity, which is stronger than the affine regularity requested by the general problem, but only on the equiangular subclass. The literature search was targeted and cannot exclude an older equivalent formulation under unrelated terminology.

## References

Á. G. Horváth and Z. Lángi, “On the convex hull and homothetic convex hull functions of a convex body,” arXiv:2012.08955, first submitted 2020-12-16; Geometriae Dedicata 216 (2022), article 10, DOI 10.1007/s10711-022-00673-y.

Z. Lángi, “A characterization of affinely regular polygons,” arXiv:1706.03036, first submitted 2017-06-09; Aequationes Mathematicae 92 (2018), 1037–1049, DOI 10.1007/s00010-018-0541-z.
