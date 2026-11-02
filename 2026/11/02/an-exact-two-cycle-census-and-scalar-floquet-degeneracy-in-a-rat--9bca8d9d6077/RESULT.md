# An exact two-cycle census and scalar Floquet degeneracy in a rational plane map

## Finding

For every \(a,c\in\mathbb R\setminus\{0\}\), consider
\[
F_{a,c}(x,y)=\left(\left(1+\frac{a}{1+y^2}\right)x,\ y+cx\right).
\]
The complete set of *primitive* period-two orbits (geometrically distinct orbits, rather than counted points) is empty when \(a\ge-2\), and contains exactly one orbit when \(a<-2\). In the latter case, write \(t=\sqrt{-a/2-1}>0\). The unique cycle is
\[
\left(-\frac{2t}{c},t\right)\longleftrightarrow
\left(\frac{2t}{c},-t\right).
\]
The return derivative at either point is a *scalar matrix*,
\[
D F_{a,c}^{2}=\left(-7-\frac{16}{a}\right)I_2.
\]
Consequently the cycle is locally exponentially attracting exactly for \(-8/3<a<-2\), a hyperbolic repeller for \(a<-8/3\), and linearly neutral with two multipliers equal to \(-1\) at \(a=-8/3\). At the unique parameter \(a=-16/7\), the first return derivative is the zero matrix; its second derivative is nonzero, giving genuine quadratic superattraction. No nonlinear stability assertion is made at the neutral point \(a=-8/3\).

## Assumptions and scope

The state space is the entire real plane. The parameters \(a\) and \(c\) are real and nonzero, with no sign restriction on \(c\). The map is defined everywhere because \(1+y^2>0\). The assumption of zero constant drives is the line-of-fixed-points case \(b=d=0\) of the rational map introduced in Zhang et al. [1], rather than an arbitrary parameter restriction. Every \((0,y)\) is a fixed point. A primitive period-two orbit is a two-element orbit under iteration, excluding all fixed points. No statements concern other periodic orbits or global basins.

## Proof

**1. Normalize the coupling.** The invertible linear coordinate change \(u=cx\), \(v=y\) conjugates the map to
\[
G_a(u,v)=\bigl(u g_a(v),\ v+u\bigr),\qquad
 g_a(v)=1+\frac{a}{1+v^2}.
\]
Let \((u_0,v_0)\mapsto(u_1,v_1)\mapsto(u_0,v_0)\) be a primitive two-cycle. Its second component gives \(u_0+u_1=0\). If \(u_0=0\), both first components vanish and the point is fixed, contrary to primitivity. Thus \(u_0\ne0\), and the first-component identities force \(g_a(v_0)=g_a(v_1)=-1\). Equivalently,
\[
v_0^2=v_1^2=-\frac a2-1.
\]
The two \(v\)-coordinates differ because \(v_1=v_0+u_0\ne v_0\). Therefore \(v_1=-v_0\), forcing \(a<-2\), \(v_0=\pm t\), and \(u_0=-2v_0\). These two ordered points belong to the same orbit. Conversely, direct substitution verifies the orbit for every \(a<-2\), proving the global census without a bounded numerical search. At \(a=-2\) the would-be cycle collapses to the fixed point \((0,0)\).

**2. Compute the exact return derivative.** Differentiate:
\[
D G_a(u,v)=
\begin{pmatrix}
 g_a(v)&u g_a'(v)\\
1&1
\end{pmatrix},\qquad
 g_a'(v)=-\frac{2av}{(1+v^2)^2}.
\]
At both cycle points \((\mp2t,\pm t)\), the derivative is the same matrix
\[
J_t=\begin{pmatrix}-1&-8t^2/(1+t^2)\\1&1\end{pmatrix}.
\]
It has trace zero, so multiplication (or Cayley–Hamilton) yields
\[
J_t^2=\frac{1-7t^2}{1+t^2}I_2
=\left(-7-\frac{16}{a}\right)I_2.
\]
Linear conjugacy preserves the scalar derivative, so the same formula holds for \(F_{a,c}^{2}\) at either original cycle point.

**3. Classify stability and the singular parameter.** As \(a\) runs from \(-2\) down to \(-\infty\), the scalar \(\lambda(a)=-7-16/a\) strictly decreases from \(1\) toward \(-7\). Its crossings of \(0\) and \(-1\) occur uniquely at \(a=-16/7\) and \(a=-8/3\), respectively. Thus \(|\lambda(a)|<1\) exactly for \(-8/3<a<-2\); contraction of a sufficiently small neighborhood under the smooth two-step return yields local exponential attraction, including the case \(\lambda=0\). For \(a<-8/3\), \(|\lambda|>1\) gives a hyperbolic repeller. At \(a=-8/3\) both return multipliers are \(-1\), so linearization alone does not settle nonlinear behavior.

At \(a=-16/7\), the normalized point \(p=(-2/\sqrt7,1/\sqrt7)\) has \(D G_a^2(p)=0\). Direct differentiation of its first return component gives the nonzero Hessian
\[
D^2(G_a^2)_1(p)=\sqrt7
\begin{pmatrix}3/2&1\\1&2\end{pmatrix}.
\]
Hence the Taylor expansion begins at (nonvanishing) quadratic order. This proves quadratic superattraction, not merely a vanishing numerical multiplier.

## Verification

Run `python verify.py` with SymPy 1.14 or a compatible recent version. The supplied program reconstructs both coordinates of the two-step return symbolically, checks the general Jacobian identity and its equality to the scalar-matrix formula, and verifies the quadratic Hessian at the superattracting parameter. It also tests 15 exact parameter/coupling choices on both sides of the stability thresholds. The exhaustiveness and infinite parameter conclusions are proved in the preceding algebra, not inferred from tests.

## Relationship to prior work

Zhang et al. [1, Secs. 2–3, Case I] introduce exactly this zero-drive, nonzero-coupling slice and report numerical period-two behavior at \(a=-2.1\) and higher-period behavior near \(a=-2.667\) for \(c=0.1\). Their accessible full article provides stability calculations for the *line of fixed points* and numerical bifurcation diagrams; it does not give this all-real-parameter primitive-period-two census, scalar double-multiplier identity, or unique quadratic superattractor. The exact boundaries here explain those numerical observations without asserting which higher-period attractors occur.

Tikjha and Muni [2] study another rational planar map, \(T(x,y)=(-\alpha x/(1+y^2),\ x+\beta y)\), and discuss explicit two-cycles. Its first component lacks the additive \(x\) term and its second component is structurally different; no general conjugacy or implication covering the present theorem is established by the accessed material. Complete text of [2] was not available for detailed comparison. Literature-index searches did not identify an exact covering result, but nonretrieval is not a proof of novelty.

## Limitations

The classification concerns only least period two in the zero-drive subfamily and gives only local stability; it does not classify period four or higher, global basins, the nonlinear behavior at the neutral multiplier \(-1\), or all driven versions of the map. Other general results about symmetric rational plane maps might subsume parts of the theorem. Source-publication dating is not uniform across publisher portals: the legacy publisher metadata reports accepted-manuscript online 2021-12-05, while the newer portal reports 2022-03-19. The earlier public date is used here; neither the manuscript's acceptance date alone nor the 2022 journal issue date is treated as its first public date.

## References

1. L.-P. Zhang, Y. Liu, Z.-C. Wei, H.-B. Jiang and Q.-S. Bi, “A class of two-dimensional rational maps with self-excited and hidden attractors,” *Chinese Physics B* **31** (2022), 030503. DOI: https://doi.org/10.1088/1674-1056/ac4025. Accessible full text: https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2022/1674-1056/cpb_31_3_030503.shtml. Earliest publisher date evidence: https://cpb.cpsjournals.org/EN/10.1088/1674-1056/ac4025.
2. W. Tikjha and S. S. Muni, “Explicit 2-cycle solutions and bifurcation structures in a non-invertible planar rational map,” *International Journal of Dynamics and Control* **13** (2025), article 184. DOI: https://doi.org/10.1007/s40435-025-01673-y. Accessible abstract and defining-map excerpt: https://www.researchgate.net/publication/391281660_Explicit_2-cycle_solutions_and_bifurcation_structures_in_a_non-invertible_planar_rational_map.
