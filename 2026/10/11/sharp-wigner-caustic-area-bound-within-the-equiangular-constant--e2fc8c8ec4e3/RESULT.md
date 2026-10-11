# Sharp Wigner-caustic area bound within the equiangular constant-width octagon family

## Finding

**Theorem.** Let \(P=(P_0,\ldots,P_7)\) be a strictly convex counterclockwise equiangular octagon with parallel opposite sides. Suppose the four distances between the corresponding pairs of opposite supporting sides are equal; this is the discrete constant-width condition for polygons with parallel opposite sides. Define its Wigner caustic \(W\) as the (possibly nonconvex) closed polygonal chain through
\[
W_j=\frac{P_j+P_{j+4}}2,\qquad j=0,1,2,3,
\]
with consecutive indices read cyclically, and its oriented area by the shoelace formula \(A^*(W)=\frac12\sum_{j=0}^3\det(W_j,W_{j+1})\). Then
\[
0\le \frac{|A^*(W)|}{A(P)}<\frac{\sqrt2-1}{6}.
\]
The constant is the exact supremum, but no strictly convex octagon attains it. Its limiting maximizers are classified by the eight parameter vertices described below.

## Assumptions and scope

For the class in the theorem, the 2026 Konicer--Murawski--Rogala--Wieczorek--Zwierzyński theorem identifies the central symmetral \(Q=(P-P)/2\) as a regular octagon. Rotate and translate, and let its edge length be \(s>0\). Let
\[
v_j=(\cos(j\pi/4),\sin(j\pi/4)),\qquad j=0,\ldots,7.
\]
All edge directions are fixed by these vectors. Write opposite edge lengths uniquely as
\[
\ell_j=s+d_j,\quad \ell_{j+4}=s-d_j,\qquad j=0,1,2,3.
\]
Closure is equivalent to \(\sum_{j=0}^3d_jv_j=0\), and hence, on setting \(a=d_1\) and \(b=d_3\),
\[
(d_0,d_1,d_2,d_3)=\left(-\frac{a-b}{\sqrt2},\ a,\ -\frac{a+b}{\sqrt2},\ b\right).
\]
All eight edges are positive exactly when
\[
s>0,\qquad |a|<s,\quad |b|<s,\quad |a|+|b|<\sqrt2s.
\]
Thus these inequalities parametrize every octagon in the stated equality class, up to rigid motions and translation. No equal-area or central-symmetry assumption is imposed.

## Proof

**1. Complete parameterization.** Since opposite edges are antiparallel, the edges of the central symmetral are their half-differences. Regularity of \(Q\) forces their lengths to be \(s\), giving the stated opposite-pair representation. Summing the eight oriented edges gives twice \(\sum_{j=0}^3 d_j v_j\). Resolving its two coordinate equations produces \(d_0=-(a-b)/\sqrt2\), \(d_2=-(a+b)/\sqrt2\). Conversely these values guarantee closure. Strict positivity of all \(\ell_j\) guarantees eight nondegenerate edges with successive exterior turn \(\pi/4\), hence a strictly convex octagon. Finally \(\max\{|a+b|,|a-b|\}=|a|+|b|\), so the stated three strict inequalities describe the full feasible parameter set.

**2. Exact oriented Wigner area.** The midpoint edges are
\[
W_{j+1}-W_j=\frac{(P_{j+1}-P_j)+(P_{j+5}-P_{j+4})}{2}=d_jv_j,
\]
for \(j=0,1,2,3\), with cyclic indices. Their sum vanishes by closure. The shoelace formula for the resulting four-edge closed chain, or direct expansion of
\[
\frac12\sum_{0\le i<j\le3}d_id_j\det(v_i,v_j),
\]
yields exactly
\[
A^*(W)=-\frac{a^2+b^2}{4}\le0.
\]
This identity includes self-intersecting Wigner chains, since oriented area is used.

**3. Exact octagon area.** The central symmetral \(Q\) is the regular octagon with side length \(s\), so
\[
A(Q)=2(1+\sqrt2)s^2.
\]
The general oriented-area identity for polygons with parallel opposite sides, proved as Equation (4.8) in the initiating paper, is \(A(Q)=A(P)-2A^*(W)\). Substituting the preceding expression gives
\[
A(P)=2(1+\sqrt2)s^2-\frac{a^2+b^2}{2}.
\]
This identity can also be checked directly by the octagon shoelace formula, independently of the cited source.

**4. Exact optimization.** Put \(u=|a|/s\), \(v=|b|/s\). Then \(0\le u,v<1\), \(u+v<\sqrt2\). On the closure of this polygonal parameter region, the strictly convex function \(u^2+v^2\) has maximum
\[
M=1+(\sqrt2-1)^2=4-2\sqrt2,
\]
attained only at \((u,v)=(1,\sqrt2-1)\) or its coordinate swap. Indeed its maximum lies at a vertex, and the other vertices \((0,0),(1,0),(0,1)\) have smaller squared norms. Restoring independent signs gives exactly eight normalized parameter vertices. Since the area ratio
\[
\frac{|A^*(W)|}{A(P)}=\frac{a^2+b^2}{8(1+\sqrt2)s^2-2(a^2+b^2)}
\]
is strictly increasing in \((a^2+b^2)/s^2\), its strict upper bound is
\[
\frac{M}{8(1+\sqrt2)-2M}=\frac{\sqrt2-1}{6}.
\]
No parameter vertex is in the open feasible region, proving nonattainment. For every vertex, multiply its normalized parameter pair by \(t\in(0,1)\) and take \(t\uparrow1\); the resulting strictly convex octagons attain ratios approaching the bound. Conversely, every parameter sequence approaching the supremum must approach the finite set of maximizing vertices, by continuity and compactness. \(\square\)

## Verification

Run `python verify_octagon.py` with SymPy installed. It reconstructs all eight vertices in exact \(\mathbb Q(\sqrt2)\)-symbolic arithmetic, checks the closure, all three area identities, the maximizing parameter vertex values, and the sharp constant. The expected output is `OCTAGON_WIGNER_EXACT_SYMBOLIC_CHECKS_OK`. The finite symbolic assertions verify the stated algebraic steps; the global maximization over the continuum is the analytic vertex argument in the proof, not a finite sampling assertion.

## Relationship to prior work

Konicer et al. (arXiv:2606.22612v1, Theorem 4.4) characterized equality in their improved isoperimetric inequality precisely by equiangular constant-width CPPOSes; their proof's Equation (4.8) relates the symmetral area to Wigner caustic area. Their Theorem 4.7 supplies a sharp but much weaker \(1/4\) supremum for **all** CPPOSes with a fixed even number of vertices, with extremal sequences outside the restrictive equality family. It does not state the sharp octagonal equality-family bound. Craizer--Teixeira--da Silva introduced the polygonal area-evolute theory; Kwong treats discrete Fourier isoperimetric inequalities without this optimization.

## Limitations

The conclusion is specific to strictly convex **eight-sided** equiangular CPPOSes of equal opposite-side distances, not to all octagons or all CPPOSes. The constant is a supremum and is not attained by an eight-sided strictly convex polygon: at the limiting parameter vertices two side lengths vanish. The result neither estimates the area of the center symmetry set nor gives the optimal value for ten or more sides. No independent audit has been performed.

## References

1. I. Konicer, B. Murawski, B. Rogala, T. Wieczorek, and M. Zwierzyński, *Convex Polygons with Parallel Opposite Sides: Convergence, Reconstruction, and Isoperimetric Inequalities*, arXiv:2606.22612v1 (21 June 2026), Theorems 4.4 and 4.7, Equation (4.8). https://arxiv.org/abs/2606.22612
2. M. Craizer, R. C. Teixeira, and M. A. H. B. da Silva, *Polygons with Parallel Opposite Sides*, Discrete Comput. Geom. 50 (2013), 474--490; arXiv:1210.2442. https://arxiv.org/abs/1210.2442
3. K.-K. Kwong, *A Unified Approach to Higher Order Discrete and Smooth Isoperimetric Inequalities*, Mathematika (2024); arXiv:2111.13352. https://arxiv.org/abs/2111.13352
