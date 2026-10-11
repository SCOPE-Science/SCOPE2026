# Weighted terminal simplices have a sorted active-set formula for their minimum enclosing sphere
## Finding
Let
\[
d\ge2,
\qquad
a>0,
\qquad
b_1,\ldots,b_d>0.
\]
After relabeling, assume
\[
0<b_1\le\cdots\le b_d.
\tag{1}
\]
Consider
\[
S
=
\operatorname{conv}\{-a\mathbf1,\ b_1e_1,\ldots,b_de_d\}
\subset\mathbb R^d.
\tag{2}
\]
This is the source family \(S(\omega)\) with
\[
\omega_0=a,
\qquad
\omega_i=b_i.
\]

The unique minimum enclosing Euclidean ball of \(S\) is determined by one sort and a scan over tails of the ordered base weights.

For
\[
p\in\{2,\ldots,d\},
\qquad
m=d-p+1,
\]
define
\[
\mu_p
=
\frac{p-2}{\displaystyle\sum_{i=m}^d b_i^{-2}}.
\tag{3}
\]
There is a unique \(p_B\) such that
\[
b_{m-1}^2\le\mu_{p_B}<b_m^2,
\tag{4}
\]
where the lower inequality is omitted when \(m=1\). Put
\[
c_i^B=
\begin{cases}
0,&i<m,\\[2mm]
\dfrac{b_i^2-\mu_{p_B}}{2b_i},&i\ge m,
\end{cases}
\tag{5}
\]
and
\[
\kappa_B
=
2a\sum_{i=1}^d c_i^B+da^2.
\tag{6}
\]

If
\[
\kappa_B\le\mu_{p_B},
\tag{7}
\]
then
\[
\boxed{
c_{\min}=c^B,
\qquad
R_{\min}^2=\|c^B\|^2+\mu_{p_B}.
}
\tag{8}
\]
The positive contact certificate uses precisely the tail base vertices
\[
b_me_m,\ldots,b_de_d.
\]
The apex is also a contact exactly when equality holds in (7). An earlier base vertex is a zero-weight contact exactly when its squared weight equals \(\mu_{p_B}\).

Suppose instead that
\[
\kappa_B>\mu_{p_B}.
\tag{9}
\]
Then the apex is necessarily a positive-weight contact. For each
\[
p\in\{1,\ldots,d\},
\qquad
m=d-p+1,
\]
put
\[
S_1=\sum_{i=m}^d b_i^{-1},
\qquad
S_2=\sum_{i=m}^d b_i^{-2},
\qquad
B_1=\sum_{i=m}^d b_i,
\tag{10}
\]
\[
A=1+aS_1,
\qquad
D=A^2+a^2(d-p)S_2,
\tag{11}
\]
and
\[
K_p
=
\frac{
A(aB_1+da^2)-a^2(d-p)(2-p)
}{
D
},
\tag{12}
\]
\[
t_p
=
\frac{2-p+S_2K_p}{2A}.
\tag{13}
\]

There is a unique \(p\) with
\[
t_p>0
\tag{14}
\]
and
\[
b_{m-1}^2+2at_pb_{m-1}
\le
K_p
<
b_m^2+2at_pb_m,
\tag{15}
\]
again omitting the left inequality when \(m=1\).

For this \(p\),
\[
\boxed{
c_{\min,i}
=
\begin{cases}
-at_p,&i<m,\\[2mm]
\dfrac{b_i^2-K_p}{2b_i},&i\ge m,
\end{cases}
}
\tag{16}
\]
and
\[
\boxed{
R_{\min}^2
=
\|c_{\min}\|^2+K_p.
}
\tag{17}
\]

The apex and all tail vertices
\[
b_me_m,\ldots,b_de_d
\]
are contacts. An earlier base vertex \(b_je_j\) is an additional, zero-weight contact exactly when
\[
b_j^2+2at_pb_j=K_p.
\tag{18}
\]

Thus the minimum enclosing ball of the entire weighted family \(S(\omega)\) is not a generic high-dimensional optimization problem: after sorting \(b_1,\ldots,b_d\), its positive contact set is always either a tail of the base vertices or the apex together with a tail.

For the standard terminal simplex
\[
S_d
=
\operatorname{conv}\{-\mathbf1,e_1,\ldots,e_d\},
\tag{19}
\]
the apex branch applies with every vertex in contact, and
\[
\boxed{
c_{\min}
=
-\frac{d-1}{2(d+1)}\mathbf1,
\qquad
R_{\min}
=
\frac{\sqrt d\,(d+3)}{2(d+1)}.
}
\tag{20}
\]

## Assumptions and scope
The metric is the standard Euclidean metric in the coordinate realization (2).

The weights are arbitrary positive real numbers. Relabeling the base coordinates to enforce (1) is an orthogonal coordinate permutation and therefore does not change the minimum enclosing ball.

The source quantity called the covering radius is a lattice covering radius. The radius in this result is instead the ordinary Euclidean minimum-enclosing radius of the finite vertex set, equivalently of its convex hull.

The theorem gives the exact center, radius, positive contact support, and all possible extra zero-weight contacts. It does not compute the Euclidean inradius, John ellipsoid, or lattice covering minima.

## Proof
We use a standard finite-point optimality lemma in a self-contained form.

Let
\[
X=\{x_1,\ldots,x_N\}\subset\mathbb R^d.
\]
If a ball centered at \(c\) contains \(X\), and there are contact points with nonnegative weights
\[
\alpha_i\ge0,
\qquad
\sum_i\alpha_i=1,
\qquad
c=\sum_i\alpha_i x_i,
\tag{21}
\]
then the ball is minimum enclosing. Indeed, if all positively weighted points satisfy
\[
\|x_i-c\|=R,
\]
then for every \(y\),
\[
\sum_i\alpha_i\|x_i-y\|^2
=
R^2+\|y-c\|^2.
\tag{22}
\]
Hence some contact point lies at distance at least the square root of the right side, and equality in the enclosing radius forces
\[
y=c.
\]
Conversely, the center of a minimum enclosing ball lies in the convex hull of its contacts; otherwise strict separation permits a small displacement that decreases every active distance. Thus (21) characterizes minimum-enclosing certificates.

We first ignore the apex and solve the minimum enclosing ball of the base points
\[
b_1e_1,\ldots,b_de_d.
\tag{23}
\]
Suppose a positive contact set is \(J\). Since the center is their convex combination, coordinates outside \(J\) vanish. Equality of the contact distances implies that for one common scalar \(\mu\),
\[
b_i^2-2b_ic_i=\mu
\qquad
(i\in J),
\tag{24}
\]
so
\[
c_i=\frac{b_i^2-\mu}{2b_i}.
\tag{25}
\]
The convex weights are
\[
\alpha_i=\frac{c_i}{b_i}
=
\frac12\left(1-\frac{\mu}{b_i^2}\right).
\tag{26}
\]
Their sum is \(1\), hence
\[
\mu
=
\frac{|J|-2}{\sum_{i\in J}b_i^{-2}}.
\tag{27}
\]
Positive weight means
\[
b_i^2>\mu,
\]
while a noncontact base point must satisfy
\[
b_j^2\le\mu.
\tag{28}
\]
Because the \(b_i\) are ordered, every positive contact set is therefore a tail. Equations (27)--(28) are exactly (3)--(4), and they determine one tail. This proves (5) and the base minimum-enclosing radius
\[
R_B^2=\|c^B\|^2+\mu_{p_B}.
\tag{29}
\]

The squared apex distance minus (29) is
\[
\|-a\mathbf1-c^B\|^2-R_B^2
=
2a\sum_i c_i^B+da^2-\mu_{p_B}
=
\kappa_B-\mu_{p_B}.
\tag{30}
\]
Therefore (7) is exactly the condition that the base minimum ball already contains the apex. In that case (21)--(22) prove (8), including uniqueness.

Assume now (9). The minimum enclosing ball of all vertices cannot omit the apex from its positive contact certificate: otherwise it would be the minimum ball of the base set, which by (30) does not contain the apex.

Let the apex weight be
\[
t>0
\]
and let \(J\) be the positive base contact set. For an inactive base coordinate,
\[
c_j=-at.
\tag{31}
\]
For an active base contact \(i\), equality of its squared distance with the apex squared distance gives
\[
b_i^2-2b_ic_i
=
K,
\tag{32}
\]
where
\[
K
=
2a\sum_{j=1}^d c_j+da^2.
\tag{33}
\]
Hence
\[
c_i=\frac{b_i^2-K}{2b_i}.
\tag{34}
\]
The corresponding positive base weight is
\[
\alpha_i
=
\frac{c_i+at}{b_i}
=
\frac12
\left(
1-\frac{K}{b_i^2}+\frac{2at}{b_i}
\right).
\tag{35}
\]

Write \(p=|J|\). The equation
\[
t+\sum_{i\in J}\alpha_i=1
\]
becomes
\[
2(1+aS_1)t-S_2K=2-p.
\tag{36}
\]
Substituting (31) and (34) into (33) gives
\[
2a^2(d-p)t+(1+aS_1)K=aB_1+da^2.
\tag{37}
\]
Solving the two linear equations (36)--(37) yields exactly (12)--(13).

The positivity condition in (35) is
\[
b_i^2+2atb_i>K.
\tag{38}
\]
For an inactive base vertex, comparison with the apex contact distance gives the reverse weak inequality
\[
b_j^2+2atb_j\le K.
\tag{39}
\]
Since
\[
b\longmapsto b^2+2atb
\]
is strictly increasing on \(b>0\), the positive base contact set must again be a tail. Conditions (14)--(15) are exactly (38)--(39) at the tail boundary.

The actual minimum enclosing ball supplies one such tail by the contact-convex-hull lemma. Conversely, any tail satisfying (14)--(15) has positive weights from (35), those weights together with \(t_p\) sum to \(1\), all vertices satisfy the radius bound, and the center is their convex combination. Therefore (21)--(22) certify it as the unique minimum enclosing ball. Uniqueness of the minimum enclosing center makes the valid tail unique.

For this certified center, (32)--(33) show
\[
R_{\min}^2
=
\|c_{\min}\|^2+K_p,
\]
which proves (17). Equation (39) is an equality exactly for the extra contacts in (18).

For the standard terminal simplex, all
\[
b_i=a=1.
\]
Permutation symmetry forces the center onto the diagonal. Equating the apex and base-vertex squared distances gives
\[
c_{\min}
=
-\frac{d-1}{2(d+1)}\mathbf1.
\]
Substitution gives
\[
R_{\min}^2
=
\frac{d(d+3)^2}{4(d+1)^2}.
\]
The center is a strict convex combination of all \(d+1\) vertices, so all are contacts and (20) follows.

## Verification
The proof is symbolic for every positive weight vector.

The source-dependent premise was checked directly in the primary full text: the family
\[
S(\omega)
=
\operatorname{conv}\{-\omega_0\mathbf1,\omega_1e_1,\ldots,\omega_de_d\}
\]
is defined there, and the paper computes its lattice covering radius rather than its Euclidean minimum enclosing ball. The publication lists \(52B20\) first among its Mathematics Subject Classifications.

A later full paper by Codenotti and Freyer was also inspected because it returns to the standard terminal simplex
\[
S_d=\operatorname{conv}\{-\mathbf1,e_1,\ldots,e_d\}
\]
as a principal lattice-reduced and lattice-complete example. That paper computes lattice width and lattice diameter, but contains no inradius, circumradius, or minimum-enclosing-sphere statement.

The accompanying `verify.py` uses exact rational arithmetic. For deterministic integer weight families in dimensions \(2\) through \(7\), it computes the formula above and independently enumerates every possible contact subset of the \(d+1\) vertices. For each subset it solves the generic minimum-ball contact equations, checks nonnegative barycentric weights and containment of all vertices, and compares the resulting exact center and squared radius with the sorted-tail formula. The enumeration is finite corroboration; the arbitrary-weight proof is the argument above.

## Relationship to prior work
Codenotti, Santos, and Schymura introduced the weighted simplices \(S(\omega)\) in their study of lattice covering radii and discrete surface area. Their Theorem 1.4 gives an exact lattice covering radius for every positive \(\omega\). That quantity is invariant under the lattice setting considered there and is different from the ordinary Euclidean minimum enclosing radius studied here.

The same paper singles out
\[
S_d=S(\mathbf1_{d+1})
\]
as the standard terminal simplex and a central conjectural extremizer for lattice covering radius.

Codenotti and Freyer later prove that \(S_d\) is simultaneously lattice reduced and lattice complete, and compute its lattice width and lattice diameter. These discrete notions again do not imply the Euclidean minimum-enclosing sphere.

Generic minimum-enclosing-ball theory supplies the contact-convex-hull optimality criterion used in the proof, but it does not by itself give the tail structure or the closed formulas (3)--(18). The special coordinate form of \(S(\omega)\) makes every positive base contact set a sorted tail and reduces the full Euclidean problem to a one-dimensional scan after sorting.

Targeted searches under “weighted terminal simplex”, “standard terminal simplex”, “\(S(\omega)\)”, “minimum enclosing ball”, “smallest enclosing sphere”, “axis simplex”, and “orthant simplex” did not locate a statement implying the sorted active-set formula.

## Limitations
The theorem concerns the specific weighted terminal coordinate realization (2). Euclidean minimum-enclosing balls are not invariant under arbitrary unimodular transformations.

The result determines the minimum enclosing sphere, not the Euclidean inball, John ellipsoid, lattice covering radius, or higher covering minima.

The proof uses standard minimum-enclosing-ball optimality. The new structural content is the explicit solution for the entire source family: contact supports are sorted tails and both the base-only and apex-active regimes have closed formulas.

A general source on diagonally structured simplices or orthogonal-axis point sets could contain an equivalent active-set formula under different terminology. The literature searches did not locate such a result, so this remains the principal residual originality risk.

## References
1. Giulia Codenotti, Francisco Santos, and Matthias Schymura, *The Covering Radius and a Discrete Surface Area for Non-Hollow Simplices*, arXiv:1903.02866, first public version 2019-03-07; *Discrete & Computational Geometry* 67 (2022), 65--111, DOI 10.1007/s00454-021-00330-3.
2. Giulia Codenotti and Ansgar Freyer, *Lattice reduced and complete convex bodies*, *Journal of the London Mathematical Society* 110 (2024), e12982, DOI 10.1112/jlms.12982.
