# Exact P-angle constant of the regular octagonal plane
## Finding
For the real Banach plane \(X_8=(\mathbb R^2,N)\) with
\[
N(s,t)=\max\!\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\},
\]
the P-angle constant introduced by Yang and Li is
\[
S_P(X_8)=\frac{\sqrt2-1}{2}.
\]
The value is attained by the adjacent vertices
\[
x=(1,\sqrt2-1),\qquad y=(\sqrt2-1,1).
\]

## Assumptions and scope
All scalars are real. The P-angle of nonzero vectors \(u,v\) is defined by
\[
\cos\operatorname{ang}_P(u,v)=\frac{\|u\|^2+\|v\|^2-\|u-v\|^2}{2\|u\|\,\|v\|}.
\]
Hence, for \(x,y\in S_X\) with \(x\ne\pm y\), writing \(a=\|x+y\|\) and \(b=\|x-y\|\),
\[
\cos\operatorname{ang}_P(x+y,x-y)=\frac{a^2+b^2-4}{2ab}.
\]
The claim concerns only the displayed regular-octagonal norm and this Yang--Li constant.

## Proof
Put \(r=\sqrt2-1\). The unit sphere of \(X_8\) is the regular octagon with vertices
\[
(1,r),(r,1),(-r,1),(-1,r),(-1,-r),(-r,-1),(r,-1),(1,-r).
\]
Its norm is the maximum of the eight support functionals
\[
\pm s,\quad \pm t,\quad \frac{\pm s\pm t}{\sqrt2}.
\]
By the dihedral symmetries of the octagon, it is enough to let \(x\) run on the edge from \((1,r)\) to \((r,1)\), while \(y\) runs on any of the eight edges. Parameterize the two edges affinely by \(s,t\in[0,1]\). On each region where one support functional realizes \(N(x+y)\) and one realizes \(N(x-y)\), the two quantities
\[
a=N(x+y),\qquad b=N(x-y)
\]
are affine functions of \((s,t)\).

To prove the claimed upper bound it is enough to show
\[
a^2+b^2-rab-4\le0,
\]
because for \(a,b>0\) this is equivalent to
\[
\frac{a^2+b^2-4}{2ab}\le\frac r2.
\]
The quadratic form \(a^2+b^2-rab\) is positive definite because \(0<r<2\). Therefore, on every active-support region the left-hand side is a convex quadratic function of \((s,t)\). A convex function on a compact polygon reaches its maximum at a vertex. The exact checker `verify.py` constructs every nonempty active-support polygon over \(\mathbb Q(\sqrt2)\), enumerates all of its vertices, and verifies the inequality there. It finds 126 feasible active-support cells after the dihedral reduction and checks 176 cell vertices; the largest value of \(a^2+b^2-rab-4\) is exactly \(0\).

For the displayed adjacent vertices,
\[
N(x+y)=2,\qquad N(x-y)=2(\sqrt2-1)=2r.
\]
Thus
\[
\frac{N(x+y)^2+N(x-y)^2-4}{2N(x+y)N(x-y)}
=\frac r2=\frac{\sqrt2-1}{2},
\]
so the upper bound is attained.

## Verification
Run `python verify.py` with a standard Python 3 interpreter. The script uses exact rational arithmetic in \(\mathbb Q(\sqrt2)\); it does not use floating-point inequalities. A successful run prints `VERIFY_OK`, reports 126 feasible active-support cells and 176 checked cell vertices, and verifies the adjacent-vertex witness exactly.

## Relationship to prior work
Yang and Li introduced \(S_P(X)\), proved the universal bound \(0\le S_P(X)\le1/2\), characterized Hilbert spaces by \(S_P(X)=0\), and related \(S_P\) to uniform non-squareness and other classical geometric constants. Their concrete examples concern classical sequence/function spaces; the inspected full text contains no regular-octagon computation. Earlier regular-octagon work computes generalized or modified von Neumann--Jordan constants, and later work computes other constants such as \(L_{YJ}\); these are different functionals and do not determine the P-angle supremum above.

## Limitations
The proof is specific to the two-dimensional regular octagonal norm. It does not claim a formula for arbitrary regular polygons or for general polyhedral Banach planes. The exact checker certifies the finite polyhedral reduction used in the proof; it is not a substitute for the reduction argument itself.

## References
1. Zhijian Yang and Yongjin Li, “New Geometric Constant Related to the P-angle Function in Banach Spaces,” arXiv:2208.11239, first posted 24 August 2022. Mathematics Subject Classification: 46B20.
2. J. Alonso, P. Martin, and P. L. Papini, “Wheeling around von Neumann--Jordan constant in Banach spaces,” Studia Mathematica 188 (2008), 135--150.
3. Changsen Yang and Tianyu Wang, “Generalized von Neumann--Jordan constant \(C_{NJ}^{(p)}(X)\) for the regular octagon space,” Mathematical Inequalities & Applications 20 (2017), 483--490.
