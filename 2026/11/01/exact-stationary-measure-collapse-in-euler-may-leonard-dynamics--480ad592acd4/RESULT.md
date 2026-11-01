# Exact stationary-measure collapse in Euler–May–Leonard dynamics

## Finding
For the three-species **forward-Euler May–Leonard map**, the critical interaction balance \(\alpha+\beta=2\) does not preserve the neutral interior cycles of its underlying differential equation. Instead, for every admissible positive step size and every unequal strictly positive initial composition, one species approaches zero along a subsequence; and the complete invariant-probability simplex is finite-dimensional.

**Theorem.** Fix real parameters \(0<R\le1\), \(0<\alpha<2\), and \(\beta=2-\alpha\). On the closed population simplex
\[
\Delta=\{(x,y,z)\in[0,\infty)^3:x+y+z\le1\},
\]
let \(F:\Delta\to\Delta\) be
\[
\begin{aligned}
x'&=x+Rx(1-x-\alpha y-\beta z),\\
y'&=y+Ry(1-\beta x-y-\alpha z),\\
z'&=z+Rz(1-\alpha x-\beta y-z).
\end{aligned}
\]
Write \(O=(0,0,0)\), \(C=(1/3,1/3,1/3)\), and \(E_1=(1,0,0)\), \(E_2=(0,1,0)\), \(E_3=(0,0,1)\). Then:

1. If \(\alpha\ne1\), the **entire set of invariant Borel probability measures** of \(F\) on \(\Delta\) is
\[
\left\{w_O\delta_O+w_C\delta_C+\sum_{j=1}^3w_j\delta_{E_j}:w_O,w_C,w_1,w_2,w_3\ge0,\ w_O+w_C+w_1+w_2+w_3=1\right\}.
\]
In particular, no invariant probability assigns positive mass to a non-equilibrium interior or boundary cycle.
2. If \(\alpha=\beta=1\), the invariant probabilities are **exactly** \(t\delta_O+(1-t)\eta\), where \(0\le t\le1\) and \(\eta\) is *any* Borel probability on \(\Sigma=\{x+y+z=1\}\). Every point of \(\Sigma\) is fixed.
3. For every initial state with \(s_0=x_0+y_0+z_0>0\), one has \(s_n\to1\) and the quantitative bound
\[
0\le 1-s_n\le(1-s_0)(1-Rs_0)^n.
\]
If also \(\alpha\ne1\) and \(x_0y_0z_0>0\), then either \(x_0=y_0=z_0\), in which case the orbit converges to \(C\), or
\[
\lim_{n\to\infty}\min\{x_n,y_n,z_n\}=0.
\]
The latter conclusion says approach to the **boundary as a set**, not convergence of one permanently identified species to zero.

## Assumptions and scope
The theorem concerns the polynomial map restricted to \(\Delta\). The hypotheses \(0<R\le1\), \(0<\alpha<2\), \(\beta=2-\alpha\) ensure all three coordinate multipliers are strictly positive on \(\Delta\); no claim is made for larger steps, negative interactions, or initial points outside this simplex. For invariant measures, *invariant* means \(F_*\mu=\mu\) for a Borel probability measure \(\mu\). The term *interior* in the trajectory statement means all three coordinates are positive, not necessarily \(x+y+z<1\).

The balance \(\alpha+\beta=2\) is the familiar neutral-cycle locus of the **continuous** May–Leonard flow: on \(x+y+z=1\), its species product is conserved, and every regular positive product level is a closed periodic orbit when \(\alpha\ne1\). This contrast motivates studying the discrete map rather than an arbitrary parameter slice.

## Proof
**Step 1: invariant simplex and scalar mass.** Put \(s=x+y+z\) and \(\kappa=R(1-\alpha)\). Using \(\alpha+\beta=2\), the map has the exact form
\[
\begin{aligned}
x'&=x\{1+R(1-s)+\kappa(y-z)\},\\
y'&=y\{1+R(1-s)+\kappa(z-x)\},\\
z'&=z\{1+R(1-s)+\kappa(x-y)\},\\
s'&=s+Rs(1-s).
\end{aligned}
\]
Since \(|\kappa|=R|1-\alpha|<1\) and \(|x-y|,|y-z|,|z-x|\le1\), each coordinate multiplier is \(\ge1-|\kappa|>0\). Also \(1-s'=(1-s)(1-Rs)\ge0\) on \(0\le s\le1\). Thus \(F(\Delta)\subseteq\Delta\), and every exact zero-coordinate pattern is preserved under iteration. For \(s_0>0\), \(s_n\) increases to one because its only scalar fixed values are zero and one. The displayed quantitative bound follows by multiplying \(1-s_{n+1}=(1-s_n)(1-Rs_n)\) and using \(s_n\ge s_0\).

**Step 2: localization of stationary measures.** For any invariant Borel probability \(\mu\), stationarity of the bounded observable \(s\) yields
\[
0=\int_\Delta(s'-s)\,d\mu=R\int_\Delta s(1-s)\,d\mu.
\]
Hence \(\mu\) is supported on \(\{O\}\cup\Sigma\), where \(\Sigma=\{s=1\}\). The two sets are invariant, so restriction to either component (when it has positive mass) is invariant.

**Step 3: strict product contraction on the face.** On \(\Sigma\), put \(V(x,y,z)=xyz\). The three factors of \(V'/V\), when \(V>0\), are
\[
1+\kappa(y-z),\quad1+\kappa(z-x),\quad1+\kappa(x-y).
\]
All are strictly positive and their sum is three. Arithmetic–geometric mean therefore gives \(V'\le V\), with equality for \(V>0\) precisely when all factors agree. If \(\kappa\ne0\), this requires \(x=y=z=1/3\), i.e. \(C\). When \(V=0\), the same inequality holds by coordinate-face invariance. Thus \(V-V'\ge0\) everywhere on \(\Sigma\), and its zeros are the three closed edges \(\{V=0\}\) together with \(C\). For a stationary probability on \(\Sigma\), integrating \(V-V'\) shows all its mass is on that zero set.

**Step 4: no stationary mass on open edges.** Each relative open edge is invariant and is never entered from a different coordinate-zero pattern, because each coordinate multiplier is positive. Consider \(z=0\), \(x+y=1\), and \(0<x<1\). Its scalar map is
\[
x'=x+\kappa x(1-x).
\]
For \(\kappa\ne0\), the bounded increment \(x'-x\) has one strict sign throughout the open edge. If an invariant probability charged this edge, the normalized restricted probability would itself be invariant; integrating this increment would give zero, a contradiction. The other two edges follow by cyclic symmetry. Hence any invariant probability is supported on the five listed points. All five are fixed, so *every* convex combination is invariant. This proves item 1.

**Step 5: degeneracy at \(\kappa=0\).** If \(\alpha=1\), the face map is the identity, while Step 2 still forces all invariant probabilities onto \(\{O\}\cup\Sigma\). Any measure supported there is invariant. This gives item 2.

**Step 6: boundary approach from unequal positive compositions.** For \(s_n>0\), set \(p_{j,n}=x_{j,n}/s_n\), where \((x_1,x_2,x_3)=(x,y,z)\). Then \(\sum_jp_{j,n}=1\) and
\[
p_{j,n+1}=p_{j,n}\left[1+\theta_n(p_{j+1,n}-p_{j+2,n})\right],\qquad
\theta_n=\frac{\kappa s_n}{1+R(1-s_n)},
\]
with cyclic indices and \(\theta_n\to\kappa\ne0\). Again the three positive bracket factors have mean one. Consequently \(P_n=p_{1,n}p_{2,n}p_{3,n}\) is strictly decreasing unless \(p_{1,n}=p_{2,n}=p_{3,n}\). If the initial proportions are unequal, \(P_0<1/27\). Suppose \(P_n\to P_\infty>0\). Choose any convergent subsequence of compositions; it has a positive limiting composition because \(P_\infty>0\). Since \(P_{n+1}/P_n\to1\) and \(\theta_n\to\kappa\ne0\), equality in arithmetic–geometric mean at this limit forces all three proportions to equal \(1/3\), giving \(P_\infty=1/27>P_0\), a contradiction. Thus \(P_n\to0\). As \(\min_jp_{j,n}\le P_n^{1/3}\), and \(0<s_n\le1\), the asserted extinction-distance limit follows. Equal initial proportions remain equal by symmetry, and \(s_n\to1\), so their orbit tends to \(C\). This proves item 3.

**Continuous-time comparison.** For \(\dot x=x(1-x-\alpha y-\beta z)\) and cyclic companions, \(\dot s=s(1-s)\), and \(\frac{d}{dt}\log(xyz)=3(1-s)\) in the positive octant. Hence \(xyz\) is a first integral on \(\Sigma\). Its regular levels \(0<xyz<1/27\) there are simple compact closed curves, and the flow has no zero on them for \(\alpha\ne1\), so each is a periodic orbit. In the discrete system at every \(R>0\) under the theorem's hypotheses, Steps 3–6 instead rule out all nontrivial interior stationary orbits and show approach to the boundary from unequal compositions.

## Verification
The accompanying standalone `CHECK.py` uses exact symbolic algebra and rational arithmetic to confirm the reduction to cyclic multipliers, the total-mass identity, the product identity, strict normalized-product descent at representative admissible rational parameters, edge drift, and the neutral-face identity. Its finite tests do **not** prove the all-parameter theorem; the arguments above provide the proof.

Reproduce with `python CHECK.py` using Python 3 and the `sympy` package. An ordinary Python test exit status of zero indicates all implemented checks passed; no external certificate is claimed.

## Relationship to prior work
Joshi, Savescu, Syed, and Blackmore (2021) introduce the three-dimensional polynomial Lotka–Volterra model in equivalent logistic coordinates and analyze fixed points, invariant coordinate faces, and multidimensional bifurcations. The present family is conjugate to their equal-growth model: their variables are \(u=Rx/(1+R)\), \(v=Ry/(1+R)\), \(w=Rz/(1+R)\), with common birth rate \(\lambda=1+R\) and cyclic interaction coefficients \(\alpha,\beta\). Their statements do not give the stationary probability classification or critical-face product contraction presented here.

Muni (arXiv:2408.15054, first posted August 27, 2024), equation (2.1), uses precisely the unscaled Euler polynomial map and studies quasiperiodicity, bifurcations, and hyperchaos in other parameter ranges; the present parameter-restricted invariant-measure result is not among its stated results. Baigent (2019) studies the carrying simplex of a **different rational map** \(T_i=rx_i/(1+x_i+\alpha x_{i+1}+\beta x_{i+2})\); its geometric conclusions do not imply the Euler-product identity. Baigent and Ching (2020) study continuous-time May–Leonard balance simplices, where the same neutral locus has periodic trajectories rather than the Euler-collapse phenomenon. The discrete Ricker-type May–Leonard competition models studied by Roeger and others are not the forward-Euler polynomial model.

## Limitations
The measure classification is **only** for the stated compact invariant simplex and parameter range. It does not classify invariant measures elsewhere in the nonnegative octant or at larger positive step sizes. The boundary-approach conclusion does not establish convergence of a single fixed species to extinction or a unique limiting vertex. Stationary measures are all atomic except at the interaction-degenerate case \(\alpha=\beta=1\), where the whole face is fixed. The one-step decline of the product is an exact discrete statement; no claim is made that the continuous May–Leonard cycles are nonexistent. Mathematical priority remains contingent on any equivalent result in the broader literature. Finite checks are consistency evidence, not an infinite-dimensional proof.

## References
1. Y. Joshi, M. Savescu, M. Syed, and D. Blackmore, “Interesting Features of Three-Dimensional Discrete Lotka–Volterra Dynamics,” *Applied Mathematics* **12** (2021), 694–722, published August 26, 2021. DOI: 10.4236/am.2021.128049. Full text: https://www.scirp.org/journal/paperinformation?paperid=111500.
2. S. S. Muni, “Torus and hyperchaos in 3D Lotka-Volterra map,” arXiv:2408.15054, first submitted August 27, 2024. https://arxiv.org/abs/2408.15054.
3. S. Baigent, “Convex geometry of the carrying simplex for the May–Leonard map,” *Discrete and Continuous Dynamical Systems B* **24** (2019), 1697–1723. DOI: 10.3934/dcdsb.2018288. Open author version: https://www.ucl.ac.uk/~ucess29/resources/map2convexDCDS.pdf.
4. S. Baigent and A. Ching, “Balance simplices of 3-species May–Leonard systems,” *Journal of Biological Dynamics* **14** (2020), 187–199. DOI: 10.1080/17513758.2020.1736656. https://www.tandfonline.com/doi/full/10.1080/17513758.2020.1736656.
5. L.-I. W. Roeger, “Discrete May–Leonard competition models II,” *Discrete and Continuous Dynamical Systems B* **5** (2005), 841–860. DOI: 10.3934/dcdsb.2005.5.841 (Ricker, not the present polynomial map).
