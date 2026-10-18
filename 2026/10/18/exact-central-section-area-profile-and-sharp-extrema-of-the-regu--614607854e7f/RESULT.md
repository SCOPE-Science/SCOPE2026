# Exact central-section area profile and sharp extrema of the regular rhombic dodecahedron

## Finding

For the three-dimensional rhombic dodecahedron
\[
K=\{x\in\mathbb R^3:|x_i|+|x_j|\le2\text{ for all }1\le i<j\le3\},
\]
let \(A(n)\) denote the intrinsic Euclidean area of \(K\cap n^\perp\) for every nonzero normal \(n\). Write \(a\ge b\ge c\ge0\) for the decreasing rearrangement of \((|n_1|,|n_2|,|n_3|)\), and \(\rho=\sqrt{a^2+b^2+c^2}\). Then
\[
A(n)=\begin{cases}
\dfrac{12\rho}{a+b+c},&a\le b+c,\\[5pt]
\dfrac{8\rho\bigl(a^2+a(b+c)-2(b^2+c^2)+2bc\bigr)}
{(a+b-c)(a-b+c)(a+b+c)},&a>b+c.
\end{cases}
\]
The formulas extend continuously across equality cases. In the generic interior of the first chamber the section has six sides; in the generic interior of the second it has eight sides. All nonzero normals satisfy the sharp bounds
\[
\boxed{4\sqrt3\le A(n)\le6\sqrt2}.
\]
The lower equality directions are **exactly** the eight signed body diagonals \(n/\|n\|=(\pm1,\pm1,\pm1)/\sqrt3\). The upper equality directions are **exactly** the twelve signed face diagonals, the signed permutations of \((1,1,0)/\sqrt2\). Antipodal normals determine the same section.

## Assumptions and scope

The scale and normalization are fixed by the inequalities defining \(K\), which has eight vertices \((\pm1,\pm1,\pm1)\), six vertices \(\pm2e_i\), and twenty-four edges. Its regular faces are rhombi. Every section is a plane through the origin. The normal need not be of unit length. The result concerns intrinsic sectional area, not the area of an orthogonal projection. Symmetry permits replacing each normal by \((a,b,c)\). All claims include coordinate-zero and chamber-wall normals by continuity.

## Proof

**1. Complete chamber decomposition.** Each of the twelve supporting inequalities of the form \(\pm x_i\pm x_j\le2\) defines a rhombus with axial endpoints and two cube-vertex endpoints; these are all facets and prove the 14-vertex description. Each of the 24 edges joins a cube vertex \(v\in\{\pm1\}^3\) to an axial vertex \(w=2v_ie_i\). For a generic normal \(n=(a,b,c)\) with \(a>b>c>0\) and \(a\ne b+c\), a section vertex lies on an edge if and only if \((n\cdot v)(n\cdot w)<0\). Its exact position is
\[
p(v,w)=\frac{(n\cdot v)w-(n\cdot w)v}{n\cdot v-n\cdot w}.
\]
The inequalities \(a>b>c>0\) leave just two sign patterns, separated by \(a=b+c\). A complete cyclic edge listing is given here; each pair is \((v,w)\). For \(a>b+c\), the eight pairs in order are

```
(-1, 1, 1):( 0, 2, 0)
(-1, 1, 1):( 0, 0, 2)
(-1,-1, 1):( 0, 0, 2)
( 1,-1, 1):( 0,-2, 0)
( 1,-1,-1):( 0,-2, 0)
( 1,-1,-1):( 0, 0,-2)
( 1, 1,-1):( 0, 0,-2)
(-1, 1,-1):( 0, 2, 0)
```

For \(a<b+c\), the six pairs in order are

```
(-1, 1, 1):(-2, 0, 0)
(-1,-1, 1):( 0, 0, 2)
( 1,-1, 1):( 0,-2, 0)
( 1,-1,-1):( 2, 0, 0)
( 1, 1,-1):( 0, 0,-2)
(-1, 1,-1):( 0, 2, 0)
```

Substituting their section vertices \(p_j\) into the oriented polygon-area identity
\[
A(n)=\frac1{2\rho}\left|\sum_j n\cdot(p_j\times p_{j+1})\right|
\]
yields the two displayed rational-radical formulas exactly. The exhaustive edge construction and symbolic cancellation are independently reproducible in `check_section.py`. Central sections depend continuously on the normal (for example, by bounded convex radial functions and dominated convergence), so the formulas cover all chamber boundaries and coordinate coincidences by limits.

**2. Bounds in the hexagonal chamber.** Cauchy–Schwarz gives \(a+b+c\le\sqrt3\rho\), whence \(A(n)\ge4\sqrt3\), with equality only at \(a=b=c>0\). For the other inequality, the chamber condition \(a\le b+c\) and the ordering imply \(0\le a-b\le c\), and
\[
(a+b+c)^2-2\rho^2=4bc-(a-b-c)^2\ge0.
\]
Thus \(A(n)\le6\sqrt2\). Equality requires \(c=0\) and \(a=b>0\), precisely a face-diagonal normal.

**3. Sharp upper bound in the octagonal chamber.** By scale invariance put \(a=1\), \(s=b+c\in[0,1]\), \(q=b-c\in[0,s]\), and \(t=q^2\). Define
\[
P=1+\frac{s^2+t}{2},\qquad Q=1+s-\frac{s^2+3t}{2}.
\]
The octagonal area is \(8\sqrt P\,Q/((1-t)(1+s))\), so the inequality \(A\le6\sqrt2\) is equivalent, where denominators are positive, to
\[
F(s,z)=9(1-s^2z)^2(1+s)^2-8
\left(1+\frac{s^2(1+z)}2\right)
\left(1+s-\frac{s^2(1+3z)}2\right)^2\ge0,
\quad z=t/s^2\in[0,1].
\]
The case \(s=0\) is the axial section of area \(8\). An exact Bernstein certificate is
\[
F(s,z)=\sum_{i=0}^{6}\sum_{j=0}^{3}m_{ij}{6\choose i}s^i(1-s)^{6-i}{3\choose j}z^j(1-z)^{3-j},
\]
with the coefficient rows \((m_{i0},m_{i1},m_{i2},m_{i3})\) given by

```
(1,     1,     1,     1)
(4/3,   4/3,   4/3,   4/3)
(2,     92/45, 94/45, 32/15)
(3,     14/5,  13/5,  12/5)
(21/5,  41/15, 4/3,   0)
(6,     2,     0,     0)
(9,     0,     0,     0)
```

All are nonnegative, and the constant first row makes \(F>0\) for \(s<1\). The only boundary zero is at \(s=z=1\), the face-diagonal limit; the original area there is \(6\sqrt2\). The checker verifies this Bernstein identity as an exact polynomial identity, not by sampling.

**4. Lower bound in the octagonal chamber.** At fixed \(s\), the logarithmic derivative with respect to \(t\) is
\[
\frac{\partial\log A}{\partial t}=\frac1{4P}-\frac3{2Q}+\frac1{1-t}.
\]
After multiplication by the positive factor \(PQ(1-t)\), its numerator \(N\) satisfies
\[
\frac{\partial N}{\partial t}=-\frac{s^2-2s+7-6t}{8}\le0,
\]
because \(0\le t\le s^2\le1\) and \(7-2s-5s^2=(1-s)(5s+7)\ge0\). Thus any interior critical point as \(t\) varies can only be a maximum, and each fixed-\(s\) minimum occurs at \(t=0\) or \(t=s^2\). Their continuous endpoint area profiles are
\[
f_0(s)=8\sqrt{1+s^2/2}\frac{1+s-s^2/2}{1+s},
\quad f_1(s)=8\sqrt{1+s^2}\frac{1+2s}{(1+s)^2}.
\]
Direct differentiation shows \(f_0\) is decreasing on \([0,1]\), with \(f_0(1)=3\sqrt6\), while \(f_1\) decreases up to \(s=1/3\) and increases thereafter, with minimum \(f_1(1/3)=5\sqrt{10}/2\). Since both constants exceed \(4\sqrt3\), the octagonal chamber has strictly larger area than the claimed global minimum.

Combining the two chambers proves both sharp bounds and all equality cases. Continuity handles the nongeneric normals.

## Verification

Running `python check_section.py` with SymPy available checks the exact edge list (24 edges, cyclic six- and eight-vertex lists), both symbolic area identities, all 28 rational Bernstein coefficients and their full polynomial reconstruction, the octagonal derivative factorizations, and a separate 2000-direction edge-plane intersection reconstruction. The direct polygon test uses all intersected edges independently of the chamber formulas; its observed maximum absolute discrepancy was less than \(9\times10^{-15}\). The finite tests corroborate but do not substitute for the exact area identities and inequalities above.

## Relationship to prior work

The rhombic dodecahedron is a classical face-transitive polytope and the face-centered-cubic Voronoi cell. Hausel–Makai–Szűcs use it for a universal covering theorem; Živaljević analyzes it as a three-dimensional simplex-generated zonotope; and Koca and collaborators describe the cube-and-octahedron vertex structure via root-system geometry. Those constructions establish the object and its symmetries, not an all-normal intrinsic plane-section area formula or this sharp extrema-and-equality classification. General maximal-section theory concerns broader inequalities but does not directly calculate the two rational-radical branches. No claim of definitive historical priority is made.

## Limitations

The result covers sections through the center, not a full affine offset-area function. It does not determine the full distribution of central-section areas for randomly oriented normals. A comprehensive historical priority certification and independent mathematical validation have not been performed.

## References

1. T. Hausel, E. Makai Jr., and A. Szűcs, *Inscribing cubes and covering by rhombic dodecahedra via equivariant topology*, arXiv:math/9906066 (first submitted 10 June 1999), https://arxiv.org/abs/math/9906066.
2. R. T. Živaljević, *Illumination complexes, Δ-zonotopes, and the polyhedral curtain theorem*, arXiv:1307.5138 (first submitted 19 July 2013), https://arxiv.org/abs/1307.5138.
3. M. Koca and collaborators, *Group Theoretical Analysis of Quasicrystallography from Projections of Higher Dimensional Lattices Bn*, arXiv:1403.2847 (first submitted 12 March 2014), https://arxiv.org/abs/1403.2847.
