# Integral ring nonisomorphism for every positive-dimensional odd biisotropic three-plane Grassmannian

## Finding

For each integer \(n\ge3\), let \(V\cong\mathbb C^{2n+1}\) carry a general pencil of skew-symmetric bilinear forms, and let \(X_n=\operatorname{S_2Gr}(3,2n+1)\) be the smooth projective locus of three-planes isotropic for both forms. Put \(Y_n=\operatorname{Gr}(3,2n-1)\). By Fonarev--Kuznetsov, their integral cohomology **groups**, degree by degree, are isomorphic. Their graded integral cohomology **rings** and graded integral Chow rings are **not** isomorphic, for every \(n\ge3\).

More precisely, write \(R=2n-2\), \(d=6(n-2)\), and let \(H_X,H_Y\) be the Plücker hyperplane classes. Their top intersection degrees satisfy the closed formula
\[
\frac{\int_{X_n}H_X^d}{\int_{Y_n}H_Y^d}
=\frac{8(8R^3-24R^2+10R+15)}{R(R+1)(R+2)},
\qquad
1<\frac{\int_{X_n}H_X^d}{\int_{Y_n}H_Y^d}<64\le 2^d.
\]
For the first member, \(X_3\subset\operatorname{Gr}(3,7)\) and \(Y_3=\operatorname{Gr}(3,5)\) have dimension six and Plücker degrees \(61\) and \(5\), respectively. The ratio tends to \(64\) as \(n\) tends to infinity. The cutoff is sharp: at the remaining admissible three-plane boundary \(n=2\), both \(\operatorname{S_2Gr}(3,5)\) and \(\operatorname{Gr}(3,3)\) are points, so their rings agree.

## Assumptions and scope

Work over \(\mathbb C\), in ordinary integral singular cohomology and integral Chow groups. A general pencil has the standard regular orbit; the associated biisotropic variety is smooth and has the dimensions quoted above, as in Fonarev--Kuznetsov, arXiv:2610.03309v1. There is no assertion about exceptional nongeneral pencils, arbitrary \(k\)-planes for \(k\ne3\), or rational-coefficient ring isomorphisms. The nontrivial theorem ranges over all integers \(n\ge3\); the dimension-zero boundary \(n=2\) is addressed separately.

Let \(S\) denote the tautological rank-three bundle on \(G_n=\operatorname{Gr}(3,2n+1)\). Since the two forms restrict to global sections of \(\bigwedge^2S^\vee\), the smooth common zero locus \(X_n\) has expected codimension \(6\). Its fundamental Chow class is
\[
[X_n]=c_3(\bigwedge^2S^\vee)^2
\quad\text{in }A^6(G_n).
\]
Write \(a,b,c\) for the formal Chern roots of \(S^\vee\) and \(H=a+b+c=c_1(\det S^\vee)\). The degree computation below uses the usual integral Schur-class normalization \(s_\lambda(S^\vee)\) and integration against the fundamental class of an ordinary Grassmannian.

## Proof

**1. Exact Schubert-degree formula.** Since \(\bigwedge^2 S^\vee\) has Chern roots \(a+b\), \(a+c\), \(b+c\), regular-section intersection theory gives
\[
D_n:=\int_{X_n}H_X^d
=\int_{G_n}H^d(a+b)^2(a+c)^2(b+c)^2.
\]
The elementary symmetric polynomial has the exact Schur expansion in three variables
\[
\bigl((a+b)(a+c)(b+c)\bigr)^2
=s_{(4,2)}+s_{(4,1,1)}+s_{(3,3)}+2s_{(3,2,1)}+s_{(2,2,2)}.
\tag{1}
\]
Here omitted trailing zero parts are understood. To see why this determines \(D_n\), the top Schubert class of \(G_n\) has rectangular partition \((R,R,R)\). Repeated Pieri multiplication by \(H=s_{(1)}\) shows that for any partition \(\lambda\) of \(6\) contained in that rectangle,
\[
\int_{G_n}H^d s_\lambda(S^\vee)
=f^{(R-\lambda_3,R-\lambda_2,R-\lambda_1)},
\tag{2}
\]
where \(f^\mu\) is the number of standard Young tableaux of shape \(\mu\). The complement and reversal in (2) are essential. The hook-length formula, equivalently the three-row determinant formula,
\[
f^{(u,v,w)}
=\frac{(u+v+w)!(u-v+1)(u-w+2)(v-w+1)}{(u+2)!(v+1)!w!},
\tag{3}
\]
applies to the weakly decreasing nonnegative triple \((u,v,w)\).

For \(Y_n=\operatorname{Gr}(3,2n-1)\), the top rectangular partition is \((R-2,R-2,R-2)\). Therefore
\[
B_n:=\int_{Y_n}H_Y^d=f^{(R-2,R-2,R-2)}>0.
\]
Substituting (3) into the five summands in (1)--(2), and dividing by \(B_n\), yields the five respective contributions
\[
\begin{aligned}
\lambda=(4,2):&\quad\frac{27(R-3)(R-2)}{(R+1)(R+2)},\\
(4,1,1):&\quad\frac{10(R-3)(R-2)}{R(R+1)},\\
(3,3):&\quad\frac{10(R-2)(R-1)}{(R+1)(R+2)},\\
2(3,2,1):&\quad\frac{16(R-2)}{R+1},\\
(2,2,2):&\quad 1.
\end{aligned}
\]
Their sum simplifies **identically in \(R\)** to
\[
\frac{D_n}{B_n}
=\frac{8(8R^3-24R^2+10R+15)}{R(R+1)(R+2)}.
\tag{4}
\]
As \(R=2n-2\ge4\), we have the exact factorizations
\[
\frac{D_n}{B_n}-1
=\frac{3(R-2)(3R-5)(7R+4)}{R(R+1)(R+2)}>0
\tag{5}
\]
and
\[
64-\frac{D_n}{B_n}
=\frac{24(2R-1)(8R+5)}{R(R+1)(R+2)}>0.
\tag{6}
\]
Because \(d\ge6\), equations (5)--(6) imply \(1<D_n/B_n<64\le2^d\). Equations (4)--(6) prove the asserted ratio, inequalities, and limit. At \(R=4\), the hook-length calculation gives \(D_3=61\), \(B_3=5\).

**2. Obstruction to integral ring isomorphism.** Fonarev--Kuznetsov, Theorem 1.1, gives graded integral cohomology-group isomorphisms \(H^*(X_n;\mathbb Z)\cong H^*(Y_n;\mathbb Z)\). In particular, \(H^2\cong\mathbb Z\) and \(H^{2d}\cong\mathbb Z\) for each variety. The Plücker hyperplane \(H_Y\) is a primitive positive generator of \(H^2(Y_n;\mathbb Z)\).

Suppose there were a graded integral unital ring isomorphism \(\phi:H^*(Y_n;\mathbb Z)\to H^*(X_n;\mathbb Z)\). Let \(x\) be a generator of \(H^2(X_n;\mathbb Z)\). Then \(\phi(H_Y)=\pm x\), whereas \(H_X=m x\) for a nonzero integer \(m\). Raising to the even power \(d\) and comparing the two positive fundamental-class intersection numbers forces
\[
D_n=|m|^d B_n.
\tag{7}
\]
If \(|m|=1\), the ratio is \(1\). If \(|m|\ge2\), the ratio is at least \(2^d\). Both contradict (5)--(6). Hence the integral cohomology rings are nonisomorphic. This argument deliberately **does not assume** that \(H_X\) is a primitive class.

Finally, the algebraic affine-cell filtrations of these smooth complex projective varieties identify their integral Chow groups with integral even-degree singular cohomology via the cycle-class maps, compatibly with products. Thus an integral Chow-ring isomorphism would induce the forbidden graded integral cohomology-ring isomorphism. This proves the Chow-ring statement. For \(n=2\), the general-pencil three-plane locus has dimension zero and exactly one torus fixed point by the originating cellular description, hence consists of one reduced point; the ordinary \(\operatorname{Gr}(3,3)\) is also a point. Thus the full admissible fixed-rank family has an exact ring-isomorphism boundary at \(n=2\).

## Verification

The accompanying standard-library-only script `verify.py` explicitly expands the degree-six Chern-root polynomial and the five Schur polynomials via semistandard tableaux, asserting identity (1) coefficientwise. For each \(3\le n\le12\), it independently obtains \(D_n\) by (i) the Schur/Pieri/hook formula and (ii) direct alternating-polynomial coefficient extraction from \(H^d(a+b)^2(a+c)^2(b+c)^2\). It checks both degree values and equation (4) exactly as rational numbers. Separately, it verifies the rational identity (4) and factorization identities (5)--(6) **symbolically as integer polynomial identities**, not merely at finitely many integer inputs.

Execution: `python3 verify.py` from the directory containing this result and the script; no external libraries or downloaded data are required. Successful execution ends with `PASS: exact rational identity and both strict bounds certified as polynomial identities`. The finite cases cross-check the nonstandard computations; the infinite result follows from the algebraic identities and the geometric intersection-theoretic argument above.

## Relationship to prior work

Fonarev and Kuznetsov, arXiv:2610.03309v1, Theorem 1.1, prove precisely the **additive** cohomology agreement used in this proof. Their Remark 1.2 explicitly identifies determining the multiplicative structure as a separate question. The present claim is the rank-three **nonisomorphism** theorem, derived by comparing integral top powers; it does not claim a full cohomology-ring presentation.

Benedetti's arXiv:1809.10902 develops equivariant cohomology and a Chevalley formula for two-planes in an **even-dimensional** bisymplectic ambient space, not this three-plane odd-dimensional family. Fatighenti and Mongardi's arXiv:1904.05679 studies Fano loci cut by homogeneous vector-bundle sections in Grassmannians, supplying related geometric context rather than an implication of (4) or the nonisomorphism theorem. Standard Schubert calculus and the hook-length formula are explicitly used as known inputs, not claimed as new.

## Limitations

Only the general-pencil three-plane family in odd ambient dimension is treated; no full multiplicative presentation, quantum cohomology description, or rational-coefficient ring nonisomorphism is asserted. The source bibliography mentions an in-preparation manuscript specifically on \(\operatorname{S_2Gr}(3,7)\); its full text was not publicly available for a content comparison. An earlier unpublished or unindexed computation of these exact Plücker degrees remains a concrete novelty risk. The finite verifier is not a formal proof of the geometric input; standard theorems and the accompanying written mathematical proof carry the infinite assertion.

## References

1. A. Fonarev and A. Kuznetsov, *Betti Numbers of Odd Biisotropic Symplectic Grassmannians*, arXiv:2610.03309v1 (first public version, 2 October 2026), Theorem 1.1, Remark 1.2, Definition 2.1. https://arxiv.org/html/2610.03309v1
2. V. Benedetti, *Bisymplectic Grassmannians of planes*, arXiv:1809.10902 (2018), especially the restriction to two-planes in even ambient dimension. https://arxiv.org/abs/1809.10902
3. E. Fatighenti and G. Mongardi, *Fano varieties of K3 type and IHS manifolds*, arXiv:1904.05679 (2019). https://arxiv.org/abs/1904.05679
4. W. Fulton, *Young Tableaux*, London Mathematical Society Student Texts 35, Cambridge University Press, 1997 (Pieri multiplication and hook-length formula).
