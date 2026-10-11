# Exact Liu–Yang parameter profile of the affine-regular hexagonal plane
## Finding
Let \(X_H=(\mathbb R^2,N)\), where
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
For \(\lambda\in[0,1]\), define
\[
L'_Y(\lambda,X)
=
\sup_{x,y\in S_X}
\left(
\|\lambda x+(1-\lambda)y\|^2
+
\lambda(1-\lambda)\|x-y\|^2
\right).
\]
This is the notation of the first public version of arXiv:2110.15741; the current revision denotes the same displayed invariant by \(C'_{\mathrm{NJ}}(\lambda,X)\).

Writing
\[
m=\min\{\lambda,1-\lambda\},
\]
the exact profile is
\[
L'_Y(\lambda,X_H)=1+2m-3m^2.
\]
Hence
\[
\max_{\lambda\in[0,1]}L'_Y(\lambda,X_H)=\frac43,
\]
with equality exactly at \(\lambda=1/3\) and \(\lambda=2/3\). At the balanced parameter,
\[
L'_Y(1/2,X_H)=\frac54.
\]

## Assumptions and scope
All scalars are real. The unit ball of \(X_H\) is the affine-regular hexagon with vertices
\[
(1,1),\ (1,0),\ (0,-1),\ (-1,-1),\ (-1,0),\ (0,1).
\]
The defining source proves
\[
L'_Y(\lambda,X)=L'_Y(1-\lambda,X),
\]
which also follows directly by interchanging \(x\) and \(y\). It is therefore enough to treat
\[
0\le m\le\frac12.
\]

## Proof
Fix \(m\in[0,1/2]\) and put
\[
F_m(x,y)
=
N(mx+(1-m)y)^2+m(1-m)N(x-y)^2.
\]
The boundary of the hexagonal unit ball is the union of six line segments. For any fixed pair of such edges, \(F_m\) is convex jointly in \((x,y)\): a squared norm is convex, affine composition preserves convexity, and the sum has nonnegative coefficients. Therefore the maximum of \(F_m\) on the product of two fixed edges occurs at one of its four vertex pairs. Consequently the global supremum over \(S_{X_H}\times S_{X_H}\) is attained among the \(36\) ordered pairs of hexagon vertices.

An exact facet calculation for these \(36\) pairs partitions \(0\le m\le1/2\) at all possible facet-switch parameters. On every open subinterval the active objective is one of
\[
1,\qquad
1+m-m^2,\qquad
1+2m-3m^2.
\]
Boundary ties take the same values by continuity. The last polynomial dominates the other two throughout the interval because
\[
(1+2m-3m^2)-(1+m-m^2)=m(1-2m)\ge0
\]
and
\[
(1+2m-3m^2)-1=m(2-3m)\ge0.
\]

Sharpness is uniform in \(m\). Take
\[
x=(1,1),\qquad y=(0,-1).
\]
Both are unit vectors. For \(0\le m\le1/2\),
\[
mx+(1-m)y=(m,2m-1),
\]
so
\[
N(mx+(1-m)y)=1-m,
\qquad
N(x-y)=2.
\]
Thus
\[
F_m(x,y)
=
(1-m)^2+4m(1-m)
=
1+2m-3m^2.
\]
This proves the formula for \(0\le\lambda\le1/2\), and symmetry gives the full interval.

Finally, the quadratic \(1+2m-3m^2\) has its unique maximum on \([0,1/2]\) at \(m=1/3\), where it equals \(4/3\). Symmetry gives exactly the two maximizing parameters \(\lambda=1/3\) and \(\lambda=2/3\).

## Verification
The bundled `verify.py` uses exact rational arithmetic. It reconstructs every parameter breakpoint at which two hexagonal facet functionals can exchange dominance for each ordered pair of the six vertices. On each resulting open interval it derives the active quadratic exactly, verifies that the complete set is the three-polynomial list displayed in the proof, proves the candidate branch dominates the others on \([0,1/2]\), and checks the uniform attaining pair.

The finite computation is not used as a substitute for the infinite reduction: the reduction from the whole unit sphere to vertex pairs is the analytic convexity argument above.

## Relationship to prior work
The first public version of Liu, Yang, Sarfraz and Li introduces \(L'_Y(\lambda,X)\), proves the universal estimate
\[
1\le L'_Y(\lambda,X)\le1+4\lambda(1-\lambda),
\]
establishes parameter symmetry, and notes
\[
L'_Y(1/2,X)=C'_{\mathrm{NJ}}(X).
\]
Its concrete non-Hilbert example concerns \(\ell_3^2\), not the affine-regular hexagonal plane.

The current revision renames the same unrestricted invariant \(C'_{\mathrm{NJ}}(\lambda,X)\). It also studies an isosceles-orthogonality-restricted constant \(C''_{\mathrm{NJ}}(\lambda,X)\) and treats the same \(\ell_\infty-\ell_1\) hexagonal norm for that restricted invariant. Since the admissible pairs differ, that computation does not determine the unrestricted profile proved here.

A separate public research record gives the parameterized isosceles von Neumann–Jordan profile of this hexagonal plane, and another gives a parameterized von Neumann–Jordan profile for the regular octagonal plane. Their definitions or spaces differ, so neither statement implies the present formula.

Literature on modified von Neumann–Jordan constants for extreme absolute normalized norms may cover the single balanced value after an affine identification, but it does not by itself imply the full \(\lambda\)-profile or the off-center maximizers established here.

## Limitations
The result concerns one canonical two-dimensional polyhedral norm. It does not classify \(L'_Y(\lambda,X)\) for arbitrary hexagonal norms, and no monotonicity under Banach–Mazur distance, subspaces, or quotients is asserted. The literature search cannot prove absolute novelty. A 2023 bulletin paper on modified von Neumann–Jordan constants of extreme absolute normalized norms was located, but its repository full text was not accessible in the inspected channel; accordingly, no novelty is claimed here for the isolated balanced value \(5/4\) alone. The accepted claim is the complete parameter profile and its exact maximizing parameters.

## References
1. Q. Liu, Z. Yang, M. Sarfraz and Y. Li, “On new parameters concerning a generalization of the parallelogram law in Banach spaces,” arXiv:2110.15741v1, first public version 29 October 2021. MSC 46B20.
2. Y. Wang, Q. Liu, Q. Li, Q. Ni, Z. Yang, M. Sarfraz and Y. Li, “Novel constants based on the generalization of Von Neumann-Jordan constant,” arXiv:2110.15741v2, current revision inspected for the renamed notation and the restricted isosceles constant.
3. N. Komuro, K.-I. Mitani and T. Okazaki, “Geometrical constants of 2-dimensional spaces with extreme norms in \(\mathcal{AN}_2\),” RIMS Kokyuroku 2260 (2023), 129–136.
