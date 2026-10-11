# Exact \(\Delta\)-constants of finite-dimensional real cubes and sharp extremizers

## Finding
Let \(n\ge1\) be an integer, let \(X_n=\ell_\infty^n(\mathbb R)\), and let \(x=(x_1,\ldots,x_n)\in B_{X_n}\). Put
\[
a_i=|x_i|,\qquad b_i=1-a_i,\qquad b_*=\max_{1\le i\le n}b_i.
\]
For \(0<r\le2\), define the opposite-face capacity
\[
\Phi_x(r)=\sum_{\{i:\ r\le1+a_i\}}\frac{1-a_i}{r+1-a_i}.
\]
An empty sum is zero, and a term with \(a_i=1\) is zero. Then the pointwise Choi--Jung \(\Delta\)-constant has the **exact full-ball formula**
\[
\boxed{\displaystyle
\delta c_{X_n}(x)=\max\left\{b_*,\ \sup\{r\in(b_*,2]:\Phi_x(r)\ge1\}\right\},}
\]
where the supremum of an empty set is taken to be zero. In particular, for every \(r>b_*\), the exact convexification criterion is
\[
\boxed{\displaystyle
x\in\operatorname{conv}\{y\in B_{X_n}:\|y-x\|_\infty\ge r\}
\quad\Longleftrightarrow\quad \Phi_x(r)\ge1.}
\]
The capacity is a finite, piecewise rational and nonincreasing function of the radius. Thus the formula gives a finite exact procedure: inspect the thresholds \(1+a_i\) and the roots of a rational equation between successive thresholds.

For equal absolute coordinates \(a\in[0,1]\), it simplifies to
\[
\boxed{\displaystyle
\delta c_{X_n}(a,\ldots,a)=
\begin{cases}1-a,&n=1,\\
\min\{1+a,(n-1)(1-a)\},&n\ge2.
\end{cases}}
\]
In particular, the previously plotted three-dimensional line has the **exact radical profile**
\[
\boxed{\displaystyle
\delta c_{X_3}\left(\frac23,\frac23,t\right)
=\frac{1+\sqrt{25-24t}}6\qquad(0\le t\le1).}
\]

The optimal \(\Delta\)-constant among **unit vectors** is also exact:
\[
\boxed{\displaystyle
\max_{x\in S_{X_n}}\delta c_{X_n}(x)=
\begin{cases}0,&n=1,\\1,&n=2,\\2-\dfrac2{n-1},&n\ge3.\end{cases}}
\]
For \(n=2\), the maximizers are the centers of the cube's edges. For \(n=3\), they are precisely the unit vectors with at least one zero coordinate. For every \(n\ge4\), there is one maximizing orbit under signed coordinate permutations, represented by
\[
\left(1,1-\frac2{n-1},\ldots,1-\frac2{n-1}\right).
\]
Therefore the best finite-dimensional value rises to \(2\) as the dimension tends to infinity, although no finite cube contains a \(\Delta\)-point.

## Assumptions and scope
The scalar field is real and all dimensions are finite. The pointwise constant is defined for **every** \(x\in B_{X_n}\), including the interior, by
\[
\delta c_X(x)=\inf_{\substack{S\text{ a slice of }B_X\\x\in S}}
\sup_{y\in S}\|y-x\|,
\quad
S=S(f,\alpha)=\{y\in B_X:f(y)>1-\alpha\},
\quad f\in S_{X^*},\quad\alpha>0.
\]
Coordinate sign changes and permutations preserve this constant. Neither infinite-dimensional \(c_0\) nor infinite compact \(C(K)\) is used as a substitute for the finite cube; those settings have an additional unavoidable radius floor at one.

## Proof
**1. Compact convex-hull reduction.** For a finite-dimensional Banach space \(X\), \(x\in B_X\), and \(0\le r\le2\), put
\[
E_r(x)=\{y\in B_X:\|y-x\|\ge r\}.
\]
Then
\[
\delta c_X(x)\ge r\quad\Longleftrightarrow\quad x\in\operatorname{conv}E_r(x).
\]
For the forward implication, suppose that \(x\notin\operatorname{conv}E_r(x)\). Compactness of \(E_r(x)\) (including the trivial empty case) and strict separation give a nonzero linear functional \(f\) and a number \(s\) with
\[
\sup_{y\in E_r(x)}f(y)<s<f(x)\le\sup_{y\in B_X}f(y).
\]
Normalize \(f\) and \(s\) by the same positive dual norm. The slice \(S=\{y\in B_X:f(y)>s\}\) contains \(x\), and its compact closure in \(B_X\) misses \(E_r(x)\). Hence \(\sup_{y\in S}\|y-x\|<r\), giving \(\delta c_X(x)<r\). Conversely, if \(x\) is a convex combination of points of \(E_r(x)\), every slice containing \(x\) contains at least one of the contributing points; its radius is at least \(r\). The case \(r=0\) follows directly.

**2. The elementary floor.** Apply coordinate sign changes to assume \(x_i=a_i\ge0\), and choose \(j\) with \(b_j=b_*\). Two points obtained by replacing the \(j\)-th coordinate of \(x\) by \(1\) and \(2a_j-1\), respectively, are in the cube, are both at distance \(b_*\) from \(x\), and have midpoint \(x\). Therefore \(\delta c_X(x)\ge b_*\).

**3. All far faces above the floor.** Fix \(r>b_*\). No coordinate can move upward from \(a_i\) through a distance \(r\), because \(1-a_i=b_i\le b_*\). Consequently
\[
E_r(x)=\bigcup_{\{i:\ r\le1+a_i\}} C_i(r),\qquad
C_i(r)=\{y\in[-1,1]^n:y_i\le a_i-r\}.
\]
Each \(C_i(r)\) is a (possibly degenerate) closed face cap, nonempty exactly for the indices displayed. Put \(c_i=b_i/(r+b_i)\) on these active indices and \(c_i=0\) elsewhere, and write \(C=\sum_i c_i=\Phi_x(r)\).

If \(x\) belongs to the convex hull of the caps, group a finite convex decomposition by one cap containing each point, and denote the total group weights by \(\lambda_i\ge0\), with \(\sum_i\lambda_i=1\). In coordinate \(i\), the contribution of its own cap is at most \(\lambda_i(a_i-r)\), while all other groups contribute at most \(1-\lambda_i\). Therefore
\[
a_i\le1-\lambda_i(r+b_i),\qquad
\lambda_i\le\frac{b_i}{r+b_i}=c_i.
\]
Summing gives \(C\ge1\).

Conversely, suppose \(C\ge1\), and put \(\lambda_i=c_i/C\). Then \(\sum_i\lambda_i=1\), \(0\le\lambda_i\le c_i<1\) and \(\lambda_i=0\) at inactive coordinates. For each \(j\) with \(\lambda_j>0\), define a point \(y^{(j)}\) coordinatewise by
\[
y_i^{(j)}=
\begin{cases}
a_i-r,&i=j,\\
a_i+\dfrac{\lambda_i r}{1-\lambda_i},&i\ne j.
\end{cases}
\]
The first branch lies in \([-1,1]\) by activity of \(j\). On the second branch, \(\lambda_i\le b_i/(r+b_i)\) implies \(\lambda_i r/(1-\lambda_i)\le b_i\), so that coordinate also lies in \([-1,1]\). Thus \(y^{(j)}\in B_{X_n}\), and its \(j\)-th coordinate differs from \(a_j\) by exactly \(r\). Finally, for every \(i\),
\[
\sum_j\lambda_j y_i^{(j)}
=\lambda_i(a_i-r)+(1-\lambda_i)
\left(a_i+\frac{\lambda_i r}{1-\lambda_i}\right)=a_i.
\]
Therefore \(x=\sum_j\lambda_j y^{(j)}\in\operatorname{conv}E_r(x)\). Combining this equivalence with steps 1 and 2 proves the full-ball formula.

For an independent separating certificate when \(C<1\), define
\[
f(y)=\sum_{\{i:r\le1+a_i\}}\frac{y_i}{r+b_i}.
\]
Each \(y\in C_i(r)\) satisfies \(f(y)\le\sum_i(r+b_i)^{-1}-1\), whereas \(f(x)=\sum_i(r+b_i)^{-1}-C\). The strict gap is \(1-C>0\). This independently confirms the excluded side of the exact capacity criterion.

**4. Uniform-coordinate and three-dimensional profiles.** If every \(a_i=a\) and \(b=1-a\), then above the floor \(b\), the capacity is \(nb/(r+b)\) for \(r\le1+a\) and zero after this threshold. For \(n\ge2\), its last feasible radius is the lesser of \(1+a\) and \((n-1)b\), both at least \(b\). For \(n=1\), no radius above \(b\) is feasible. This proves the stated equal-coordinate formulas.

For \(x=(2/3,2/3,t)\), put \(b=1-t\). Whenever all three opposite caps are active, the capacity equation reads
\[
\frac{2/3}{r+1/3}+\frac{b}{r+b}=1
\quad\Longleftrightarrow\quad 3r^2-r-2b=0.
\]
Its positive root is \(r_t=(1+\sqrt{25-24t})/6\). Directly for \(0\le t\le1\), one checks
\[
\max\{1/3,1-t\}\le r_t\le\min\{5/3,1+t\}.
\]
Hence the active-set assumptions hold, the root is not lost at a cap cutoff, and monotonicity of the capacity gives \(\delta c_{X_3}(x)=r_t\) exactly, including both endpoints.

**5. Sharp unit-sphere extremum.** For \(n\ge3\) and \(x\in S_{X_n}\), at least one \(b_i=0\). For \(r>1\), each other active coordinate has \(b_i\le2-r\). Because \(b/(r+b)\) increases with \(b\ge0\),
\[
\Phi_x(r)\le(n-1)\frac{2-r}{2}.
\]
If \(r>2-2/(n-1)\), the right side is less than one; the floor \(b_*\le1\) cannot help at such a radius. Thus \(\delta c_{X_n}(x)\le2-2/(n-1)\). Equality is attained at \(x=(1,a,\ldots,a)\) with \(a=1-2/(n-1)\): at \(r=2-2/(n-1)\), its other \(n-1\) capacities are each \(1/(n-1)\), so their sum is one. For \(n\ge4\), the bound is strictly above one. Equality forces exactly one zero \(b_i\), and all other \(b_i=2/(n-1)\), proving uniqueness up to signed coordinate permutations. When \(n=3\), the upper bound is one; equality holds whenever some coordinate vanishes, by the floor. If no coordinate vanishes then \(b_*<1\), while at \(r=1\) the at most two nonsaturated coordinate capacities are each strictly below \(1/2\), so the capacity stays below one for all radii sufficiently close to one and the constant is strictly below one. The cases \(n=1,2\) follow directly from the full formula, completing the classification.

## Verification
The proof is analytic and applies to every real point of the finite cube, in every positive integer dimension. The bundled standard-library checker `verify_cube_delta.py` uses exact rational arithmetic for 31,294 tests of signed-cap capacities, explicit far-point barycentric witnesses, and strict separating-functional gaps; it also checks the sharp equal-coordinate boundaries and unit-sphere extremizers in dimensions through twelve. A separate exploratory linear-programming cross-check compared the full signed-cap criterion with explicit convex hulls of far-face vertices in 1,960 rational cases with dimensions at most four. All tests passed. The experiments verify examples and boundary handling, not the universal quantifiers of the proof.

## Relationship to prior work
Choi and Jung introduced the quantitative constant in arXiv:2307.10647 (first public version 2023-07-20; primary MSC 46B04, 46B20). Their Proposition 3.1 determines its Daugavet analogue on finite cubes and identifies the \(\Delta\)-constant only in dimension two. Remark 3.4(1) gives a lower bound in dimension three and plots the family \((2/3,2/3,t)\), without its exact values; the text explicitly notes the difficulty of exact \(\Delta\)-constants already in dimension three. The present formula fills that specific quantitative gap, and its sharp sphere extremizers are a separate global consequence.

The qualitative \(\Delta\)-point and stronger diametral variants studied by Abrahamsen--Haller--Lima--Pirk and Martín--Perreau--Rueda Zoca do not specify pointwise finite-radius constants. Recently published formulas titled *Exact \(\Delta\)-constants for every point of \(c_0\)* and *Exact \(\Delta\)-constants on every real \(C(K)\) space* treat, respectively, infinite sequences and **infinite** compact Hausdorff \(K\). Their unavoidable lower radius one is not available in a finite cube: for instance, \(\delta c_{\ell_\infty^3}(4/5,4/5,4/5)=2/5\), whereas the corresponding zero-extended vector in \(c_0\) has constant one. Accordingly, neither published infinite-dimensional formula specializes to the subunit finite-dimensional regime. The published finite-cube classification of *positive square points* concerns a different norming-functional condition and does not imply quantitative \(\Delta\)-constants.

## Limitations
All statements concern real scalar \(\ell_\infty^n\) with finite \(n\). The formula is not asserted for general finite-dimensional absolute norms, complex cubes, or arbitrary \(C(K)\). The exact profile may require solving a one-variable polynomial of degree up to \(n\); a uniform radicals-only expression is neither needed nor claimed. While source and published-result comparisons found no equivalent all-point finite-cube theorem, unindexed or differently formulated work remains a bibliographic risk. No independent external audit has been performed.

## References
1. G. Choi and M. Jung, *The Daugavet and Delta-constants of points in Banach spaces*, arXiv:2307.10647v1, 2023-07-20; current public arXiv HTML v3, https://arxiv.org/html/2307.10647v3 (Definition 2.1, Proposition 2.3, Proposition 3.1, Remark 3.4, and Section 4.2).
2. T. A. Abrahamsen, R. Haller, V. Lima and K. Pirk, *Delta- and Daugavet-points in Banach spaces*, arXiv:1812.02450v1, 2018-12-06, and Proc. Edinburgh Math. Soc. 63 (2020), 475–496.
3. M. Martín, Y. Perreau and A. Rueda Zoca, *Diametral notions for elements of the unit ball of a Banach space*, arXiv:2301.04433v1, 2023-01-11; https://arxiv.org/html/2301.04433v1.
4. *Exact \(\Delta\)-constants for every point of \(c_0\)*, publicly indexed mathematical result, 2026 (infinite-sequence all-point formula).
5. *Exact \(\Delta\)-constants on every real \(C(K)\) space*, publicly indexed mathematical result, 2026 (theorem explicitly assumes infinite compact Hausdorff \(K\)).
6. *Positive square points of \(\ell_\infty^n\) are exactly cube-face centers*, publicly indexed mathematical result, 2026 (a distinct positive-square invariant).
