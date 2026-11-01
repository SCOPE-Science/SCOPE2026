# Sharp zonoid-test Bézout coefficients for every planar trapezoid

## Finding
Let \(K\) be a nondegenerate planar trapezoid whose two parallel sides have lengths \(a\le b\), and set \(\tau=a/b\in(0,1]\). The sharp constant in the two-test planar mixed-area Bézout inequality restricted to zonoid auxiliary bodies is exactly
\[
\boxed{C_{\mathrm{zon}}(K)=1+\tau.}
\]
Specifically, for **every pair** \(L,M\) of planar zonoids (possibly degenerate segments),
\[
\operatorname{area}(K)V_2(L,M)\le(1+\tau)V_2(K,L)V_2(K,M).
\]
This is optimal: a pair of explicit nonparallel segments realizes equality. If the auxiliary sets must have interior, the same value is approached by arbitrarily thin parallelograms. Consequently the optimal inverse ratio is \(1/(1+\tau)\), whose reciprocal coefficient varies exactly linearly in the affine trapezoid parameter. The triangle limit has coefficient \(1\), while parallelograms have coefficient \(2\). In particular, within the trapezoid family, a near-unit coefficient provides the exact affine control \(\tau=C_{\mathrm{zon}}-1\).

## Assumptions and scope
A *trapezoid* here is a convex quadrilateral with at least one pair of parallel opposite sides; a parallelogram is included, and the chosen parallel sides have lengths \(0<a\le b\). A *zonoid* is a Hausdorff limit of finite Minkowski sums of line segments, up to translation. This includes all centrally symmetric planar convex bodies and degenerate segments. Write \(V_2\) for planar mixed area, determined by
\[
\operatorname{area}(X+tY)=\operatorname{area}(X)+2tV_2(X,Y)+t^2\operatorname{area}(Y),\qquad t\ge0.
\]
The optimal coefficient is the least real \(C\) for which the inequality holds for all zonoids \(L,M\), allowing translated and degenerate bodies. The claim does **not** replace zonoid test bodies by arbitrary non-centrally-symmetric bodies.

## Proof
**Affine normalization.** By translating, rescaling, and shearing, put
\[
K=K_\tau=\operatorname{conv}\{(0,0),(1,0),(\tau,1),(0,1)\},\qquad 0<\tau\le1.
\]
The affine-invariant mixed-area ratio and the relative parallel-base length are unchanged. The area is \(A=(1+\tau)/2\).

**Segment mixed volumes.** For a vector \(u\), write \(S_u=[0,u]\), let \(Ju=(-u_2,u_1)\), and let \(D=K-K\). The planar extrusion formula gives
\[
V_2(K,S_u)=\frac12w_K(Ju)=\frac12h_D(Ju),\qquad
V_2(S_u,S_v)=\frac12|\det(u,v)|,
\]
where \(w_K(n)=\max_{x\in K}\langle n,x\rangle-\min_{x\in K}\langle n,x\rangle\). The six extreme points of \(D\) (with harmless collinear redundancies at \(\tau=1\)) are
\[
(1,0),\ (1,-1),\ (-\tau,-1),\ (-1,0),\ (-1,1),\ (\tau,1).
\]
Its polar is the intersection
\[
D^\circ=\{(x,y):|x|\le1,\ |x-y|\le1,\ |\tau x+y|\le1\}.
\]
For \(0<\tau<1\), its six vertices in cyclic order are
\[
(1,0),\ (1,1-\tau),\ (0,1),\ (-1,0),\ (-1,\tau-1),\ (0,-1).
\]
The same formula works at \(\tau=1\) after suppressing duplicates.

**Exact extremal determinant.** Since determinant is bilinear, its maximum absolute value on \(D^\circ\times D^\circ\) occurs at a pair of vertices. The fifteen unordered vertex-pair determinants from the displayed list have absolute values exclusively among \(0,1-\tau,1\). In particular,
\[
\max_{p,q\in D^\circ}|\det(p,q)|=1
\]
for all \(0<\tau\le1\), and equality is realized by \((1,0)\) and \((0,1)\). For nonzero \(u,v\), the normalized perpendicular vectors \(Ju/h_D(Ju)\) and \(Jv/h_D(Jv)\) lie on \(D^\circ\). Therefore
\[
|\det(u,v)|\le h_D(Ju)h_D(Jv),
\]
so
\[
V_2(S_u,S_v)\le 2V_2(K,S_u)V_2(K,S_v).
\]
Multiplying by \(A=(1+\tau)/2\) proves the desired inequality for two segments with coefficient \(1+\tau\).

**Extension to zonoids.** If \(L=\sum_i S_{u_i}\) and \(M=\sum_j S_{v_j}\), mixed-area bilinearity gives
\[
AV_2(L,M)=A\sum_{i,j}V_2(S_{u_i},S_{v_j})
\le(1+\tau)\sum_{i,j}V_2(K,S_{u_i})V_2(K,S_{v_j})
=(1+\tau)V_2(K,L)V_2(K,M).
\]
Translation does not affect mixed area. Every zonoid is a Hausdorff limit of zonotopes, and mixed volume is continuous, so the inequality holds for all stated \(L,M\).

**Sharpness.** Take \(u=(1,0)\), \(v=(0,1)\). The two directional widths are both \(1\), so \(V_2(K,S_u)=V_2(K,S_v)=1/2\), while \(V_2(S_u,S_v)=1/2\). The resulting ratio \(AV_2(S_u,S_v)/(V_2(K,S_u)V_2(K,S_v))=1+\tau\). Thus no smaller coefficient works. Thickening either segment by arbitrarily small positive-width cross-segments proves the same optimal value when tests are required to have interior. The limit \(\tau\downarrow0\) gives the triangular coefficient \(1\).

## Verification
The standalone `verify.py` recomputes the polar-vertex pair determinants and membership inequalities with exact rational arithmetic for all reduced rational parameters in a prescribed finite grid, checks the equality witnesses, and tests the extension to randomly generated zonotopes. On replay from its package path, it printed `VERIFY_OK trapezoid zonoid Bezout: exact rational checks 21282`. These checks test the computations; the displayed vertex argument and bilinearity establish the universal claim for all real \(0<\tau\le1\) and all zonoid test bodies.

## Relationship to prior work
The classical Bézout inequality holds for simplices with coefficient \(1\). Saroglou, Soprunov, and Zvavitch (2015) characterized simplices among polytopes using the unrestricted auxiliary-body inequality. Langharst and Wang (September 17, 2026) extended simplex characterization to all full-dimensional convex bodies. Averkov and Soprunov (2025) studied a related three-dimensional zonoid inequality, and classical Fenchel theory supplies the universal coefficient \(2\). Those are **prior** results, not contributions here. The present, narrower quantitative statement evaluates the exact *zonoid-test* coefficient continuously across all affine trapezoid classes, rather than characterizing the coefficient-one equality class or asserting the unrestricted all-test constant. It is not implied numerically by the qualitative simplex characterization or the general universal bound \(2\).

## Limitations
Only planar trapezoids and zonoid (equivalently centrally symmetric planar convex) auxiliary bodies are covered. No formula for the unrestricted coefficient over all arbitrary non-centrally-symmetric test bodies is claimed. The argument does not settle coefficients for generic quadrilaterals without parallel sides or higher-dimensional polytopes. Historical priority is provisional: the primary full text of the 2026 simplex-characterization preprint could not be retrieved, so possible equivalent calculations in its appendices or older sources are a residual risk. No independent mathematical audit has been performed.

## References
- D. Langharst and S. Wang, *The Bézout inequality for mixed volumes characterizes simplices*, arXiv:2609.20380, first public September 17, 2026. https://arxiv.org/abs/2609.20380
- C. Saroglou, I. Soprunov, and A. Zvavitch, *Characterization of Simplices via the Bezout Inequality for Mixed Volumes*, arXiv:1512.05442 (2015); *Proc. Amer. Math. Soc.* 144 (2016), 5333–5340. https://arxiv.org/abs/1512.05442
- G. Averkov and I. Soprunov, *An Algebraic-Combinatorial Proof of a Bézout-Type Inequality for Mixed Volumes of Three-Dimensional Zonoids*, *Discrete Comput. Geom.*, published May 23, 2025. https://doi.org/10.1007/s00454-025-00745-2
