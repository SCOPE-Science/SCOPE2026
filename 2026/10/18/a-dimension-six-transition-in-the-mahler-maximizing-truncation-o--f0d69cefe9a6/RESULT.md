# A dimension-six transition in the Mahler-maximizing truncation of two antipodal cube corners

## Finding
For each integer \(d\geq3\) and each real \(0\leq t\leq2\), define the centrally symmetric cube truncation
\[
K_{d,t}=[-1,1]^d\cap\left\{x\in\mathbb R^d:\left|\sum_{i=1}^d x_i\right|\leq d-t\right\}.
\]
Let \(Q_d(t)\) denote its volume product divided by the cube's volume product \(4^d/d!\):
\[
Q_d(t)=\frac{d!}{4^d}\operatorname{vol}_d(K_{d,t})\operatorname{vol}_d(K_{d,t}^{\circ}).
\]
Then throughout the complete vertex-disjoint truncation range,
\[
\boxed{Q_d(t)=\left(1-\frac{t^d}{2^{d-1}d!}\right)\left(1+\frac{t}{2^{d-1}(d-t)}\right).}
\]
There is a sharp dimension-dependent change in the **global maximizing cut depth**. Set \(B_d=2^{d-1}\) and
\[
H_d(t)=t^{d-1}\left[(d-t)^2+\frac{t(d-t+1)}{B_d}\right].
\]
For \(d=3,4,5\), the unique maximizer \(t_d\) belongs to \((0,2)\) and is the unique root of \(H_d(t_d)=d!\). For **every \(d\geq6\)**, \(Q_d\) is strictly increasing on \([0,2]\); hence \(t_d=2\) is its unique maximizer. The first three interior maximizers are approximately
\[
t_3=1.22436654819266,\quad t_4=1.52257578574713,\quad t_5=1.84030857908916.
\]
The corresponding optimal normalized products are approximately \(1.08272561930926\), \(1.04668145701090\), and \(1.02500795600643\). In dimension six the maximum is exactly \(4667/4608\). These decimal values are illustrative, not part of the proof.

## Assumptions and scope
The integer dimension satisfies \(d\geq3\). The cut parameter is real and satisfies \(0\leq t\leq2\), precisely the range in which the removed neighborhoods of the two antipodal cube corners are disjoint simplices and no additional cube vertices are removed. The polar is taken about the origin: \(K^{\circ}=\{y:\langle x,y\rangle\leq1\text{ for all }x\in K\}\). Volumes are Euclidean Lebesgue volumes. Since the body is centrally symmetric and has nonempty interior, the origin is its Santaló point. “Maximizer” always refers only to this explicit one-parameter truncation family, not to arbitrary centrally symmetric convex bodies.

## Proof
**Primal volume.** Near \((1,\ldots,1)\), substitute \(s_i=1-x_i\). The deleted region is \(s_i\geq0\), \(\sum_i s_i<t\), of volume \(t^d/d!\). The opposite corner contributes the same amount. For \(t\leq2\) these are nonoverlapping cube-corner simplices, yielding
\[
\operatorname{vol}_d(K_{d,t})=2^d-\frac{2t^d}{d!}.
\]
This remains valid at the endpoint \(t=2\) by continuity.

**Polar volume.** By the elementary polar identity for intersections, the polar is
\[
K_{d,t}^{\circ}=\operatorname{conv}\left\{\pm e_1,\ldots,\pm e_d,\ \pm\frac{\mathbf1}{d-t}\right\}.
\]
The first \(2d\) vertices form the cross-polytope \(B_1^d\), of volume \(2^d/d!\). Put \(a=\mathbf1/(d-t)\). Every supporting facet of \(B_1^d\) is given by \(\sum_i\varepsilon_i y_i=1\), where \(\varepsilon_i\in\{-1,1\}\). For \(0<t<2\), only the all-positive facet has \(\langle\varepsilon,a\rangle>1\), because all other sign sums are at most \(d-2<d-t\). Correspondingly, \(-a\) sees only the all-negative facet. The two new hull pieces are therefore disjoint pyramids on these two facets. Each base has \((d-1)\)-volume \(\sqrt d/(d-1)!\), and each height is \(t/[\sqrt d(d-t)]\); its \(d\)-volume is \(t/[d!(d-t)]\). Consequently
\[
\operatorname{vol}_d(K_{d,t}^{\circ})=\frac{2^d}{d!}+\frac{2t}{d!(d-t)}.
\]
The same expression holds by continuity at \(t=0\) and \(t=2\). Multiplying the primal and polar expressions and dividing by \(4^d/d!\) proves the boxed formula.

**Critical equation.** Differentiate the exact rational function. With \(B_d=2^{d-1}\), a simplification gives
\[
Q_d'(t)=\frac{d}{B_d(d-t)^2}\left(1-\frac{H_d(t)}{d!}\right).
\]
Direct differentiation yields
\[
H_d'(t)=t^{d-2}(d-t)\left[d(d-1)-(d+1)\left(1-\frac1{B_d}\right)t\right].
\]
The bracket is positive on \(0<t<2\) for every \(d\geq3\). Indeed, at \(t=2\) its value is zero for \(d=3\) and strictly positive when \(d\geq4\). Since \(d-t>0\), \(H_d\) is strictly increasing on \((0,2)\), from \(H_d(0)=0\). Thus \(Q_d'\) changes sign at most once, necessarily from positive to negative.

**Sharp dimension threshold.** At the terminal depth,
\[
H_d(2)=2^{d-1}(d-2)^2+2(d-1).
\]
For dimensions \(3,4,5\), respectively, these values are \(8\), \(38\), and \(152\), strictly exceeding \(3!=6\), \(4!=24\), and \(5!=120\). Hence strict monotonicity of \(H_d\) guarantees one interior critical point; by the sign of \(Q_d'\), it is the unique global maximum.

At \(d=6\), the endpoint value is \(522<720=6!\). For every integer \(d\geq6\), if
\(2^{d-1}(d-2)^2+2(d-1)<d!\), then multiplying by \(d+1\) shows
\[
(d+1)!>2^d(d-1)^2+2d,
\]
because the difference between the two right-hand expressions is
\[
2^{d-1}\bigl(d^3-5d^2+4d+2\bigr)+2(d^2-d-1)>0
\]
for \(d\geq6\). Induction proves \(H_d(2)<d!\) for all \(d\geq6\). Since \(H_d\) is strictly increasing, \(Q_d'>0\) throughout the interior, and the unique maximum lies at \(t=2\). This completes the classification.

## Verification
The file `verify.py` performs exact rational checks of the two volume formulas, the normalized product, the derivative identity at many rational parameters, the endpoint threshold through dimension 29, and the cross-polytope facet-visibility criterion through dimension nine. Run `python3 verify.py` (standard library only). The expected final line begins with `VERIFY_OK`. Independent numerical convex-hull volumes of the stated polar vertices were also compared with the formula for dimensions three through five at four cut depths, agreeing to floating-point tolerance. These tests support but do not replace the preceding symbolic geometric proof.

## Relationship to prior work
The original 2026-10-07 cube-apex study of Shen and Dubovski concerns an optimization for adding apices to **cube facets** at fixed total height. Our bodies arise by truncating two opposite **vertices** of a cube, or equivalently adding opposite apices to facets of its *polar cross-polytope*. Thus these are not the same geometric parameter family; the original source's complete text could not be inspected, so unrecognized equivalent coverage remains a priority risk.

A published four-dimensional diagonal-corner calculation, *Exact linear Mahler-deficit rate on the 4D diagonal shadow path* (2026), already proves the volume product formula for \(d=4\) and \(0\leq t\leq1/2\). That special case is acknowledged as covered and **is not claimed as new**. It does not determine this family's dimension-dependent global maximizing depths across \(d\geq3\). The published all-dimensional cube–cross-polytope **intersection** volume product instead imposes \(\sum_i|x_i|\leq c\), simultaneously truncating all sign corners, and therefore has different products and different extrema. Classical cube-local Mahler lower bounds likewise do not imply the maximizing-cut classification.

## Limitations
The terminal depth \(t=2\) is a combinatorial threshold: the formulas need not extend beyond it. The theorem does not determine a global Mahler maximum across all convex bodies or across arbitrary vertex truncations. Its new claim is the strict dimension-six transition and exact global cut-depth classification, not the already known four-dimensional local formula. A fuller priority assessment would require access to the complete text of the October 2026 cube-apex preprint and potentially older unindexed studies of paired corner truncations. The findings have only self-review and no independent audit.

## References
1. H. Shen and P. B. Dubovski, *A sharp minimum for cube-apex bodies in every dimension*, arXiv:2610.11014, first submitted 2026-10-07, https://arxiv.org/abs/2610.11014.
2. *Exact linear Mahler-deficit rate on the 4D diagonal shadow path*, online mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/9/SCOPE101.
3. *Exact Mahler products for cube–cross-polytope intersections and their three-dimensional phase diagram*, online mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-mahler-products-for-cube-cross-polytope-intersections-and--afc1f44d4eb2.
4. F. Nazarov, F. Petrov, D. Ryabogin, and A. Zvavitch, *A remark on the Mahler conjecture: local minimality of the unit cube*, arXiv:0905.0867.
5. M. Fradelizi, M. Meyer, and A. Zvavitch, *Volume Product*, arXiv:2301.06131.
