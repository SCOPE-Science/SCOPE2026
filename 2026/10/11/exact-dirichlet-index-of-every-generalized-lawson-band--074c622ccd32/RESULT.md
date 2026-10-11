# Exact Dirichlet index of every generalized Lawson band

## Finding

For every integer \(k\ge1\), let \(\bar\tau_{1,2k}\subset S^3\) be the generalized Lawson band whose oriented double cover is parameterized by
\[
F_k(x,y)=
\bigl(
\cos y\cos x,\,
\sin y\cos x,\,
\cos(2ky)\sin x,\,
\sin(2ky)\sin x
\bigr),
\]
with
\[
0\le x\le\pi,
\qquad
y\in\mathbb R/(2\pi\mathbb Z).
\]
Then
\[
\boxed{
\operatorname{ind}_D(\bar\tau_{1,2k})=2k,
\qquad
\operatorname{null}_D(\bar\tau_{1,2k})=1.
}
\]

More precisely, in the separated odd Fourier sectors, the radial ground state is negative exactly for
\[
n=1,3,\ldots,2k-1,
\]
and is strictly positive for every odd
\[
n\ge2k+1.
\]
Each negative odd frequency contributes two independent eigenfunctions, through the cosine and sine angular factors. Even Fourier sectors contribute no negative eigenfunctions, and the sole zero mode is the known \(n=0\) rotational Jacobi field.

This extends the previously explicit cases
\[
k=1
\quad\text{and}\quad
k=2
\]
to the full generalized Lawson-band family.

## Assumptions and scope

The Dirichlet Morse index and nullity are those of the stability operator on the nonorientable band, equivalently of the odd sector on its oriented double cover with Dirichlet boundary condition at
\[
x=0,\pi.
\]

Following the source, define
\[
H_k(x)=1+(4k^2-1)\sin^2x.
\]
The separated radial stability operator in Fourier frequency \(n\) is
\[
\mathcal L_{k,n}u
=
u''
+
\frac{(4k^2-1)\sin x\cos x}{H_k(x)}u'
-
\frac{n^2}{H_k(x)}u
+
\left(
2+\frac{8k^2}{H_k(x)^2}
\right)u.
\]
Its Dirichlet quadratic form is
\[
E_n^k[u]
=
\int_0^\pi
\left(
|u'|^2+
\left(
\frac{n^2}{H_k(x)}
-
2-
\frac{8k^2}{H_k(x)^2}
\right)u^2
\right)
\sqrt{2H_k(x)}\,dx.
\]

The source proves two structural facts that are used here. First, all admissible even Fourier sectors are nonnegative, with equality only for the \(n=0\) rotational Jacobi field. Second, for each admissible odd Fourier frequency, only its lowest radial eigenfunction can contribute to index or nullity. The new argument determines the sign of that lowest eigenvalue for every odd frequency.

## Proof

Write
\[
H=H_k(x)=1+(4k^2-1)\sin^2x.
\]

Consider first the odd frequency
\[
n_-=2k-1.
\]
A direct calculation gives
\[
\frac{\mathcal L_{k,n_-}(\sin x)}{\sin x}
=
\frac{
(2k-1)(2k+1)(4k-1)\sin^2x
+
8k^2+4k-1
}{
H^2
}.
\]
For every integer \(k\ge1\), the numerator is strictly positive on the entire interval. Since \(\sin x\) is positive in \((0,\pi)\) and vanishes at the two endpoints,
\[
E_{2k-1}^k[\sin x]
=
-\int_0^\pi
\sin x\,
\mathcal L_{k,2k-1}(\sin x)\,
\sqrt{2H}\,dx
<0.
\]
Hence the lowest Dirichlet eigenvalue in frequency \(2k-1\) is negative.

If \(n\) is any positive odd integer with
\[
n\le2k-1,
\]
then
\[
\mathcal L_{k,n}
=
\mathcal L_{k,2k-1}
+
\frac{(2k-1)^2-n^2}{H}.
\]
Thus the same test function gives
\[
E_n^k[\sin x]<0.
\]
Therefore every odd frequency
\[
1,3,\ldots,2k-1
\]
has a negative radial ground state.

Now set
\[
n_+=2k+1
\]
and define
\[
u_+(x)
=
\frac{1+(2k-1)\sin^2x}{\sqrt{H}}.
\]
The function \(u_+\) is strictly positive on the closed interval and satisfies the exact identity
\[
\mathcal L_{k,2k+1}u_+=0.
\]

There is also a geometric origin for this function. A unit normal to the oriented double cover may be chosen as
\[
\nu=
\left(
-\frac{2k\sin x\sin y}{\sqrt H},
\frac{2k\sin x\cos y}{\sqrt H},
\frac{\cos x\sin(2ky)}{\sqrt H},
-\frac{\cos x\cos(2ky)}{\sqrt H}
\right).
\]
The rotational Jacobi field
\[
R_{13}=x_1\nu_3-x_3\nu_1
\]
splits into frequencies \(2k-1\) and \(2k+1\). Up to a harmless factor, the coefficient of
\[
\sin((2k+1)y)
\]
is precisely \(u_+\). Hence the zero-mode identity is also forced by ambient rotational symmetry.

Because \(u_+>0\), the standard ground-state transform yields, for every Dirichlet test function \(f\),
\[
E_{2k+1}^k[f]
=
\int_0^\pi
\sqrt{2H}\,
u_+^2
\left|
\left(\frac{f}{u_+}\right)'
\right|^2dx.
\]
This is nonnegative. It is in fact strictly positive for every nonzero Dirichlet \(f\): equality would force
\[
f=cu_+,
\]
but \(u_+\) does not vanish at the boundary.

Therefore the lowest Dirichlet eigenvalue in frequency \(2k+1\) is strictly positive. For every odd
\[
n>2k+1,
\]
one has
\[
E_n^k[f]
=
E_{2k+1}^k[f]
+
\bigl(n^2-(2k+1)^2\bigr)
\int_0^\pi
\frac{f^2}{H}\sqrt{2H}\,dx,
\]
so the quadratic form is again strictly positive.

Thus the sign pattern of all admissible odd ground states is exact:
\[
\lambda_{k,n}^{(1)}<0
\iff
n\in\{1,3,\ldots,2k-1\},
\]
while
\[
\lambda_{k,n}^{(1)}>0
\quad\text{for every odd }n\ge2k+1.
\]

The source's Sturm--Liouville and nodal-domain argument shows that no higher radial eigenfunction in an odd Fourier sector can contribute to the index or nullity. It also shows that all even sectors are nonnegative and that equality occurs only for the \(n=0\) function
\[
R_{12}
=
\frac{\sqrt2\,k\sin(2x)}
{\sqrt{4k^2+1-(4k^2-1)\cos(2x)}}.
\]

There are exactly \(k\) negative odd frequencies. Each supplies two linearly independent modes,
\[
f_n(x)\cos(ny),
\qquad
f_n(x)\sin(ny).
\]
Consequently
\[
\operatorname{ind}_D(\bar\tau_{1,2k})=2k.
\]
No odd sector is null, and the \(n=0\) rotational mode is the only even null mode, so
\[
\operatorname{null}_D(\bar\tau_{1,2k})=1.
\]

## Verification

The proof is symbolic and valid for every integer \(k\ge1\). No finite computation is used to infer the infinite family.

The bundled checker verifies algebraically that
\[
\mathcal L_{k,2k+1}u_+=0
\]
for symbolic \(k\), and that
\[
\frac{\mathcal L_{k,2k-1}(\sin x)}{\sin x}
\]
reduces to the displayed positive rational expression. It also verifies the normal field, the Fourier decomposition of \(R_{13}\), and the ground-state-transform identity symbolically.

As an implementation check only, it discretizes the radial Sturm--Liouville problem for several small values of \(k\) and confirms that the numerical sign transition occurs between \(2k-1\) and \(2k+1\). These numerical checks are not part of the proof.

The primary paper was inspected through its full text, especially Appendix B. There it derives the separated operator and quadratic form, proves that even sectors do not contribute except for the \(n=0\) null field, proves that only the lowest radial eigenfunction in an odd sector can contribute, gives a general upper bound, and computes only the cases \(k=1\) and \(k=2\) exactly.

## Relationship to prior work

Bernstein and Ketover derive the full separated Sturm--Liouville problem for \(\bar\tau_{1,2k}\). Their Proposition B.1 proves
\[
\operatorname{null}_D(\bar\tau_{1,2k})\in\{1,3\}
\]
and an upper bound on
\[
\operatorname{ind}_D+\operatorname{null}_D.
\]
They compute
\[
\operatorname{ind}_D(\bar\tau_{1,2})=2,
\qquad
\operatorname{null}_D(\bar\tau_{1,2})=1,
\]
and, with computer assistance,
\[
\operatorname{ind}_D(\bar\tau_{1,4})=4,
\qquad
\operatorname{null}_D(\bar\tau_{1,4})=1.
\]
The exact all-\(k\) formula above is not stated there.

Morozov and Penskoi compute the Morse index and nullity of the closed Lawson Klein bottle \(\tau_{2,1}\). Their problem is a periodic closed-surface spectrum, not the Dirichlet spectrum of the half-band family treated here.

Searches using the generalized-Lawson-band notation, the exact formula \(2k\), the Dirichlet-index formulation, and the separated-mode threshold did not locate a prior statement of the all-\(k\) band formula.

## Limitations

The result concerns the Dirichlet problem for the generalized Lawson bands \(\bar\tau_{1,2k}\). It does not compute the full closed-surface Morse index of every Lawson \(\tau\)-surface or the indices of the more general twisted Lawson surfaces mentioned in the source's open problems.

The proof uses the source's established mode-reduction fact that only the radial ground state of an admissible odd Fourier sector can contribute at nonpositive energy. The new contribution is the exact sign classification of those ground states.

The result does not address embeddedness. For \(k>1\), the generalized bands are immersed rather than the embedded Lawson band.

## References

1. Jacob Bernstein and Daniel Ketover, *Minimal equatorial fillings of low index*, arXiv:2610.00247v1, first submitted 23 September 2026.
2. E. A. Morozov and A. V. Penskoi, *Index of minimal surfaces in the 3-sphere*, Russian Mathematical Surveys 78 (2023), 396--398.
