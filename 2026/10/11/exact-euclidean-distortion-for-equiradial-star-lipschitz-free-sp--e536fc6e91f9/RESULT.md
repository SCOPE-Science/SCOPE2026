# Exact Euclidean distortion for equiradial star Lipschitz-free spaces

## Finding

Let \(m\ge2\) and \(t\in[1/2,1]\). On the metric space \(M=\{o,v_1,\ldots,v_m\}\), let \(d(o,v_i)=t\) and \(d(v_i,v_j)=1\) whenever \(i\ne j\). The real Lipschitz-free space \(\mathcal F(M)\) has dimension \(m\). This note determines **its exact Euclidean Banach--Mazur distance**, allowing arbitrary invertible linear changes of coordinates, by a finite list of explicit algebraic candidates.

Put \(\alpha=2t-1\), \(S_m=\{-m,-m+2,\ldots,m\}\), and for \(c>-1/m\) set
\[
R(c)=\max_{s\in S_m}\left(m(1+\alpha^2)+2\alpha s-\frac{c(s+\alpha m)^2}{1+mc}\right),\qquad
D(c)=\max\left\{\frac{1+c}{(1+\alpha)^2},\frac12\right\}.
\]
Let \(c_0=(1+\alpha)^2/2-1\) and \(L=\max\{-1/m,c_0\}\). Define the finite candidate set \(\mathcal C\) by the following three rules: include \(c_0\) when \(c_0>-1/m\); for each \(s\in S_m\) with \(|s|<m\), include
\[
c_s=\frac{|s+\alpha m|\sqrt{(m-1)/(m^2-s^2)}-1}{m}
\]
when \(c_s>-1/m\) and \(c_s\ge L\); and for each distinct \(s,u\in S_m\) with \(s+u\ne0\), include \(c_{s,u}=2\alpha/(s+u)\) when \(c_{s,u}>-1/m\) and \(c_{s,u}\ge L\). Equal numerical candidates are included only once. The candidate set is nonempty, and
\[
\boxed{\displaystyle
 d_{\mathrm{BM}}\!\left(\mathcal F(M),\ell_2^m\right)^2
 =\min_{c\in\mathcal C}R(c)D(c).}
\]
If \(c_*\) realizes the minimum, the Euclidean pullback \(Q_{c_*}(y)=\sum_i y_i^2+c_*(\sum_i y_i)^2\) is an optimal quadratic form up to normalization. Consequently a quadratic form with only two symmetric coordinate orbits already solves the unrestricted Hilbert-distance problem. The finite calculation uses at most quadratically many real candidates.

In particular, the endpoint values are
\[
d_{\mathrm{BM}}\!\left(\mathcal F(M),\ell_2^m\right)^2
=\begin{cases}
 m,&t=\frac12,\\[2mm]
 \displaystyle\frac{2\lfloor(m+1)/2\rfloor\lceil(m+1)/2\rceil}{m+1},&t=1.
\end{cases}
\]
These endpoint identities are included as consistency checks and not asserted to be new by themselves. For example, three leaves with \(t=3/4\) have squared distance \(15/7\), attained at \(c_*=1/4\). Four leaves with \(t=7/10\) have squared distance \(144/49\), attained at \(c_*=1/5\).

## Assumptions and scope

All Banach spaces and linear maps are real. The star has finitely many \(m\ge2\) leaves, positive hub radius \(t\in[1/2,1]\), and leaf-to-leaf distance exactly one. The inequalities on \(t\) are the triangle inequality and the convenient normalization: other radii can be reduced to this interval by a common rescaling only when the relative distances match. The Banach--Mazur distance is \(d_{\mathrm{BM}}(X,Y)=\inf_T\|T\|\,\|T^{-1}\|\), where \(T\) ranges over all invertible real linear maps.

Write each molecule as a signed zero-mass measure \(\mu_y=\sum_i y_i(\delta_{v_i}-\delta_o)\). The free-space norm equals the optimal transport cost. Put \(\alpha=2t-1\). Then
\[
\|\mu_y\|=\frac12\left(\sum_i|y_i|+\alpha\left|\sum_i y_i\right|\right).
\]
The common factor \(1/2\) does not change the Banach--Mazur distance; in the proof \(N_\alpha(y)=\sum_i|y_i|+\alpha|\sum_i y_i|\) denotes twice the free-space norm.

## Proof

**1. Exact transport norm and the vertices.** Let \(P\) and \(Q\) denote respectively the total positive and negative leaf masses. Shipping \(\min(P,Q)\) units between opposite-sign leaves, at unit cost, and the remaining \(|P-Q|\) units between leaves and the hub, at cost \(t\), yields
\[
\|\mu_y\|\le\min(P,Q)+t|P-Q|=\tfrac12(P+Q+\alpha|P-Q|).
\]
The reverse inequality follows by considering any transport plan: direct opposite-sign leaf movements cost one, and each unmatched leaf unit must pass between a leaf and the hub at cost \(t\). An indirect leaf-to-leaf route through the hub costs \(2t\ge1\) and cannot improve the price. Equivalently, the Kantorovich dual potentials that assign optimally chosen constant values to the positive and negative leaf groups and a hub value zero attain the displayed bound. Therefore \(\|\mu_y\|=N_\alpha(y)/2\).

In the coordinates \(y\), the unit ball of \(N_\alpha\) is exactly
\[
K_\alpha=\operatorname{conv}\left\{\pm\frac{e_i}{1+\alpha},\ \pm\frac{e_i-e_j}{2}:i\ne j\right\}.
\]
Each displayed generator has \(N_\alpha\)-norm one. Conversely, decompose every \(y\) into transfers from negative to positive coordinates and any unmatched mass on single coordinate vectors; the total coefficient cost in the generator gauge is precisely \(N_\alpha(y)\). Hence the stated convex hull is the whole unit ball (some listed points need not be extreme at the endpoints).

**2. Reduce unrestricted ellipsoids to permutation-invariant ones.** For any positive-definite quadratic form \(Q\), the square of the distortion of its Euclidean norm relative to \(N_\alpha\) is
\[
\frac{\sup_{y\ne0}N_\alpha(y)^2/Q(y)}{\inf_{y\ne0}N_\alpha(y)^2/Q(y)}.
\]
Let the optimum distortion of \(Q\) be \(d\). Rescale \(Q\) so \(Q(y)\le N_\alpha(y)^2\le d^2Q(y)\) for all \(y\). Both inequalities are preserved when \(Q\) is replaced by the average of its conjugates under every permutation of the leaves, since \(N_\alpha\) is permutation-invariant. The averaged form is positive definite and has no larger distortion. The commutant of the permutation representation consists of \(Q_c(y)=\sum_i y_i^2+c(\sum_i y_i)^2\), up to a positive scalar, where \(c>-1/m\). Therefore optimizing over the single parameter \(c\) solves the unrestricted Banach--Mazur problem.

**3. Two exact extremal ratios.** Since
\[
N_\alpha(y)=\max_{\varepsilon\in\{-1,1\}^m,\,\eta\in\{-1,1\}}
 \left(\sum_i\varepsilon_i y_i+\alpha\eta\sum_i y_i\right),
\]
its squared supremum on \(Q_c(y)=1\) is the largest squared dual norm of these functionals. The inverse Gram matrix is
\[
(I+c\mathbf1\mathbf1^{\mathsf T})^{-1}=
 I-\frac{c}{1+mc}\mathbf1\mathbf1^{\mathsf T}.
\]
For \(s=\eta\sum_i\varepsilon_i\in S_m\), this gives exactly
\[
\sup_{y\ne0}\frac{N_\alpha(y)^2}{Q_c(y)}=R(c).
\]
By the vertex list from Step 1 and convexity of \(Q_c\),
\[
\sup_{N_\alpha(y)\le1}Q_c(y)=
\max\left\{\frac{1+c}{(1+\alpha)^2},\frac12\right\}=D(c).
\]
The latter supremum is the reciprocal of \(\inf_{y\ne0}N_\alpha(y)^2/Q_c(y)\). Consequently the exact squared distortion associated with \(Q_c\) is \(F(c)=R(c)D(c)\).

**4. Exhaustive finite candidate reduction.** The function \(R(c)\) is a maximum of functions \(r_s(c)=m(1+\alpha^2)+2\alpha s-c(s+\alpha m)^2/(1+mc)\), all nonincreasing for \(c>-1/m\). On \(c\le c_0\) one has \(D(c)=1/2\), so moving toward \(c_0\) cannot increase \(F(c)\). Every global minimizer may thus be chosen with \(c\ge L\), with the strict domain condition \(c>-1/m\).

On \(c\ge L\), \(D(c)=(1+c)/(1+\alpha)^2\), so \(F(c)=\max_{s\in S_m}f_s(c)\) where
\[
f_s(c)=\frac{1+c}{m(1+\alpha)^2}
\left(m^2-s^2+\frac{(s+\alpha m)^2}{1+mc}\right).
\]
Each \(f_s\) is convex, because the second derivative of the only nonlinear summand has the sign of \((m-1)(s+\alpha m)^2\), which is nonnegative. If \(|s|<m\), its interior critical point satisfies
\[
1+mc=|s+\alpha m|\sqrt{\frac{m-1}{m^2-s^2}},
\]
and hence equals \(c_s\). For \(|s|=m\), the branch has no interior stationary minimum unless it is constant, in which case another active branch or a boundary also determines the minimum. Whenever two *nonidentical* branches \(f_s\) and \(f_u\) cross, subtraction of their expressions yields
\[
(s-u)\left(2\alpha-\frac{c(s+u+2\alpha m)}{1+mc}\right)=0,
\]
so \(c=2\alpha/(s+u)\), provided \(s+u\ne0\). If \(s+u=0\) and \(\alpha=0\), their branches coincide identically; if \(s+u=0\) and \(\alpha>0\), they never cross inside the domain. Thus every interior minimizer of the finite maximum \(F=\max_s f_s\) is either a smooth stationary point \(c_s\) or a crossing \(c_{s,u}\); a boundary minimizer is \(c_0\) when admissible. Since \(F(c)\to\infty\) both as \(c\downarrow-1/m\) and as \(c\to+\infty\) for \(m\ge2\), a minimum exists in the domain. The same argument proves \(\mathcal C\ne\varnothing\) and the boxed formula.

**5. Endpoints.** At \(t=1/2\), \(N_0\) is the \(\ell_1^m\)-norm, so the classical signed-permutation symmetry yields squared distance \(m\) (alternatively, evaluate the candidate formula). At \(t=1\), \(M\) is equilateral with \(m+1\) points, and its free-space norm is half the \(\ell_1\)-norm on the zero-sum hyperplane of \(\mathbb R^{m+1}\). Averaging over the full point-permutation group reduces the optimal quadratic form to the ambient Euclidean square norm on that hyperplane. The minimum squared quotient \(\|z\|_1^2/\|z\|_2^2\) for nonzero zero-sum \(z\) equals \(2\), realized by a positive and negative coordinate. The maximum is \(4\lfloor(m+1)/2\rfloor\lceil(m+1)/2\rceil/(m+1)\), realized by balanced opposite-sign constant blocks, using Cauchy--Schwarz separately on the two blocks and optimizing their sizes. Taking the ratio proves the endpoint formula.

## Verification

The embedded standalone script `CHECK.py` evaluates the finite candidate set without external numerical libraries and checks boundary cases and sample values. Independently, a dense numerical minimization of the one-variable distortion against the finite candidate minimum on \(19\times101=1919\) combinations of \(m\in\{2,\ldots,20\}\) and \(\alpha\in\{0,0.01,\ldots,1\}\) agreed within \(1.5\times10^{-8}\) in squared distortion. These computations test the algebraic reduction only; the proof is the five analytic steps above. The comparisons do not constitute exhaustive tests of infinitely many parameters.

## Relationship to prior work

Cúth, Doucha and Titkos [1] classify surjective linear isometries on broad families of Lipschitz-free spaces, explicitly including graph metrics, and motivate systematic quantitative study of their geometry; their inspected results do not determine Euclidean distortion for the present metric family. Ehrenborg, Hetyei and Readdy [2] study the full type-\(A\) root polytope, which captures the equilateral endpoint and its combinatorial structure; a triangulation/face classification does not imply the interior metric-interpolation distance profile. Alexander, Fradelizi, García-Lirola and Zvavitch [4] identify the canonical molecule polytope and develop its graph, Hanner-polytope and volume-product geometry; their detailed full-text results do not compute the Euclidean Banach--Mazur distance of these star interpolations. Grundbacher and Kobos [3] determine Euclidean Banach--Mazur distances for actual \(\ell_p\)-direct sums and related cone distances. The present additive correlation norm \(N_\alpha(y)=\|y\|_1+\alpha|\sum_i y_i|\) is neither their direct-sum hypothesis nor their cone setting; their general Euclidean-ellipsoid methodology is complementary. These comparisons do not establish global absence of an equivalent result.

## Limitations

Only real finite-dimensional Lipschitz-free spaces with **equal hub distances and equal leaf distances** are covered. The method does not classify unequal-edge stars, infinite stars, arbitrary finite metrics, or complex scalarizations. No uniqueness assertion is made for optimal quadratic forms; the result produces at least one symmetric optimum. The finite candidate algorithm can have duplicate values or algebraic ties. The endpoint cases are known classical norm geometries; novelty is sought in the full interpolating family and exhaustive sharp quantitative formula. Independent validation has not been performed.

## References

[1] M. Cúth, M. Doucha and T. Titkos, *Isometries of Lipschitz-free Banach spaces*, arXiv:2402.08266, first public version 13 February 2024 (2020 primary MSC 46B04).

[2] R. Ehrenborg, G. Hetyei and M. Readdy, *Classification of uniform flag triangulations of the boundary of the full root polytope of type A*, arXiv:1901.07113, 2019; especially Section 2.1.

[3] F. Grundbacher and T. Kobos, *Exact Banach–Mazur distances of certain \(\ell_p\)-sums and cones*, arXiv:2603.18268, first version 18 March 2026; especially Theorems 1.1--1.7 and Sections 2--4.

[4] M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, first public version 24 November 2019; Sections 1--5.
