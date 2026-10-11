# Sharp isotropic-constant range of all Hanner polytopes
## Finding
Let \(H\subset\mathbb R^d\) be a \(d\)-dimensional Hanner polytope. Then
\[
\boxed{
\frac{(d!)^{1/d}}{\sqrt{2(d+1)(d+2)}}
\le L_H\le
\frac1{\sqrt{12}}
}.
\tag{1}
\]
For \(d\ge3\), equality on the left holds exactly for linear images of the cross-polytope
\[
B_1^d=\left\{x:\sum_i|x_i|\le1\right\},
\]
and equality on the right holds exactly for parallelotopes, equivalently linear images of
\[
B_\infty^d=[-1,1]^d.
\]
In dimensions \(1\) and \(2\), the endpoint values coincide up to affine equivalence.

The mechanism is an exact recursion. If \(P\subset\mathbb R^p\) and \(Q\subset\mathbb R^q\) are centrally symmetric convex bodies and \(d=p+q\), then
\[
L_{P\times Q}^{2d}
=
L_P^{2p}L_Q^{2q}.
\tag{2}
\]
For the \(\ell_1\)-sum
\[
P\oplus_1Q
=
\{(x,y):\|x\|_P+\|y\|_Q\le1\},
\]
one has
\[
L_{P\oplus_1Q}^{2d}
=
C_{p,q}L_P^{2p}L_Q^{2q},
\tag{3}
\]
where
\[
C_{p,q}
=
\binom{d}{p}^{2}
\left(\frac{(p+1)(p+2)}{(d+1)(d+2)}\right)^p
\left(\frac{(q+1)(q+2)}{(d+1)(d+2)}\right)^q.
\tag{4}
\]
Moreover,
\[
0<C_{p,q}\le1,
\tag{5}
\]
and equality in (5) occurs only when
\[
p=q=1.
\]

Thus Cartesian-product nodes preserve the weighted geometric mean of squared isotropic constants, while every genuine higher-dimensional \(\ell_1\)-sum node incurs a strict loss.

## Assumptions and scope
For a full-dimensional convex body \(K\subset\mathbb R^m\), let \(A(K)\) be the covariance matrix of the uniform distribution on \(K\). The isotropic constant is normalized by
\[
L_K^{2m}
=
\frac{\det A(K)}{\operatorname{vol}(K)^2}.
\tag{6}
\]
This quantity is affine invariant.

A Hanner polytope is obtained recursively from one-dimensional symmetric segments by repeated \(\ell_\infty\)-sums and \(\ell_1\)-sums. In orthogonal coordinate decompositions, the \(\ell_\infty\)-sum is the Cartesian product.

Every Hanner polytope is centrally symmetric, so its centroid is at the origin and no translation term enters the covariance computations.

## Proof
For the Cartesian product
\[
K=P\times Q,
\]
the volume factors:
\[
\operatorname{vol}(K)
=
\operatorname{vol}(P)\operatorname{vol}(Q).
\]
Its covariance matrix is block diagonal:
\[
A(K)
=
A(P)\oplus A(Q).
\]
Taking determinants in (6) proves (2).

Now let
\[
K=P\oplus_1Q.
\]
Write
\[
r=\|x\|_P.
\]
The \(Q\)-fiber over \(x\in P\) is
\[
(1-r)Q.
\]
Using the radial integration identity
\[
\int_P\phi(\|x\|_P)\,dx
=
p\,\operatorname{vol}(P)
\int_0^1 r^{p-1}\phi(r)\,dr,
\]
one gets
\[
\operatorname{vol}(K)
=
\frac{p!\,q!}{d!}
\operatorname{vol}(P)\operatorname{vol}(Q).
\tag{7}
\]

For a homogeneous quadratic form \(f\),
\[
\int_P f(x)\phi(\|x\|_P)\,dx
=
(p+2)\left(\int_P f(x)\,dx\right)
\int_0^1 r^{p+1}\phi(r)\,dr.
\]
Applying this to the matrix-valued function \(xx^{\mathsf T}\) gives
\[
A(K)|_{\mathbb R^p}
=
\frac{(p+1)(p+2)}{(d+1)(d+2)}A(P),
\tag{8}
\]
and similarly
\[
A(K)|_{\mathbb R^q}
=
\frac{(q+1)(q+2)}{(d+1)(d+2)}A(Q).
\tag{9}
\]
The off-diagonal covariance blocks vanish by central symmetry. Substitution of (7)--(9) into (6) gives (3)--(4).

It remains to prove (5). Fix \(d\) and write
\[
C_p=C_{p,d-p}.
\]
By symmetry it is enough to consider
\[
1\le p\le d-p.
\]
A direct quotient calculation gives
\[
\frac{C_{p+1}}{C_p}
=
\frac{h(p+1)}{h(d-p)},
\qquad
h(x)=
\left(1+\frac1x\right)
\left(1+\frac2x\right)^x.
\tag{10}
\]
For \(x>0\),
\[
\frac{d}{dx}\log h(x)
=
\log\left(1+\frac2x\right)
-\frac2{x+2}
+\frac1{x+1}
-\frac1x.
\]
Using
\[
\log(1+t)>\frac{2t}{2+t}
\qquad(t>0),
\]
with \(t=2/x\), gives
\[
\frac{d}{dx}\log h(x)
>
\frac{x-2}{x(x+1)(x+2)}.
\tag{11}
\]
Also
\[
h(1)=h(2)=6.
\]
Thus \(h\) is strictly increasing on \([2,\infty)\), and (10) shows that \(C_p\) decreases from the boundary toward the midpoint. Hence
\[
C_{p,q}\le C_{1,d-1}
=
\frac{6d^{d+1}}{(d+1)(d+2)^d}.
\tag{12}
\]
The logarithm of the reciprocal of the last expression is
\[
g(d)
=
d\log\left(1+\frac2d\right)
+
\log\frac{d+1}{6d}.
\]
One has
\[
g(2)=0,
\]
and the same computation as (11) gives
\[
g'(d)>0
\qquad(d\ge2).
\]
Therefore
\[
C_{p,q}\le1,
\]
with equality only at
\[
d=2,\qquad p=q=1.
\]

For the cube,
\[
L_{B_\infty^d}=\frac1{\sqrt{12}}.
\tag{13}
\]
For the cross-polytope,
\[
\operatorname{vol}(B_1^d)=\frac{2^d}{d!},
\qquad
A(B_1^d)=
\frac{2}{(d+1)(d+2)}I_d.
\]
Hence
\[
L_{B_1^d}
=
\frac{(d!)^{1/d}}{\sqrt{2(d+1)(d+2)}}.
\tag{14}
\]

Induct on the Hanner construction tree. Formula (2) takes weighted geometric means and (3) multiplies by a factor at most \(1\). Therefore the cube endpoint is maximal, and equality for \(d\ge3\) forces every nontrivial node to be a Cartesian-product node after the harmless two-dimensional affine equivalence; this yields a parallelotope.

For the lower endpoint, let
\[
S_d=L_{B_1^d}^{2d}.
\]
Because
\[
B_1^d=B_1^p\oplus_1B_1^q,
\]
formula (3) gives
\[
S_d=C_{p,q}S_pS_q.
\tag{15}
\]
If the root of a Hanner construction is an \(\ell_1\)-sum, the inductive lower bounds on its children and (15) give the cross-polytope bound. If the root is a Cartesian product and \(d\ge3\), then \(C_{p,q}<1\), so
\[
S_pS_q>S_d,
\]
and equality is impossible. Thus equality forces an all-\(\ell_1\) construction, up to the two-dimensional affine coincidence, and therefore gives a cross-polytope.

This proves (1) and both equality classifications.

## Verification
The supplied `verify.py` works with the exact rational quantity
\[
S(H)=L_H^{2\dim H}.
\]
It checks the coefficient (4), verifies
\[
C_{p,q}<1
\]
for all integer pairs with \(p+q\le40\) except \(p=q=1\), recursively enumerates all attainable Hanner values through dimension \(9\), and confirms that their exact minimum and maximum are respectively the cross-polytope and cube formulas.

It also independently recomputes the cube and cross-polytope covariance values.

The finite enumeration is only a regression test. The theorem in arbitrary dimension follows from the exact covariance recursion and the analytic proof of (5).

## Relationship to prior work
Kim's work on Hanner polytopes uses their standard recursive construction by \(\ell_1\)- and \(\ell_\infty\)-sums and emphasizes their distinguished role in the symmetric Mahler problem.

Rademacher gives the affine-invariant covariance definition (6) and studies extremizers of the isotropic constant among polytopes.

Kipp's later work states the centrally symmetric strong isotropic conjecture
\[
L_K\le\frac1{\sqrt{12}},
\]
identifies the cross-polytope isotropic constant explicitly, and proves structural results for local maximizers and for certain zonotope classes. In particular, it does not derive an upper bound from its local-maximizer theorem alone, and it treats zonotopes with at most \(d+1\) generators separately.

The result here proves the centrally symmetric strong upper bound on the entire Hanner class and, simultaneously, supplies the sharp lower endpoint and equality classifications within that class. Its proof is recursive and depends on the exact isotropic-constant transformation law under the two Hanner operations.

## Limitations
The upper bound is proved only for Hanner polytopes; it does not settle the centrally symmetric strong isotropic conjecture for arbitrary convex bodies.

The lower bound is an extremum within the Hanner class, not among all centrally symmetric convex bodies.

The exact recursion for Cartesian products and \(\ell_1\)-sums is elementary enough that an equivalent calculation may exist in older Banach-space or convex-geometry notes that are not well indexed.

No claim is made that the set of intermediate isotropic constants is an interval.

## References
1. J. Kim, *Minimal volume product near Hanner polytopes*, arXiv:1212.2544v1, 11 December 2012; *Journal of Functional Analysis* 266 (2014), 2360--2402.
2. L. Rademacher, *A simplicial polytope that maximizes the isotropic constant must be a simplex*, arXiv:1404.5662v1, 22 April 2014; *Mathematika* 62 (2016), 307--320. DOI: 10.1112/S0025579315000133.
3. C. Kipp, *Isotropic constants and regular polytopes*, *Advances in Mathematics* 476 (2025), 110361. DOI: 10.1016/j.aim.2025.110361.
