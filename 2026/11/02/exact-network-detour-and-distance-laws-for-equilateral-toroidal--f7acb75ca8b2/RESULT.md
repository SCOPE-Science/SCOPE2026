# Exact network-detour and distance laws for equilateral toroidal grids

## Finding

Let \(m,n\geq3\) be integers. Replace each edge of the Cartesian product \(C_m\square C_n\) by a unit interval and equip the resulting network \(G_{m,n}\) with its intrinsic path metric. Draw \(X,Y\) independently from normalized total edge arclength; set \(D=d_{G_{m,n}}(X,Y)\). The canonical coordinate embedding identifies the network with the horizontal and vertical unit grid lines of the flat torus \(\mathbb T_m\times\mathbb T_n\), where \(\mathbb T_k=\mathbb R/k\mathbb Z\). Equip this ambient torus with its taxicab quotient metric \(d_1\), and write \(L=d_1(X,Y)\), \(\Delta=D-L\).

**Exact network detour.** Set
\[
p_{m,n}=\frac{m+n-2}{4mn}.
\]
Then \(\Delta\geq0\) for every sampled pair; furthermore,
\[
\mathbb P(\Delta>z)=p_{m,n}(1-z)^2\quad(0\leq z\leq1),
\]
and \(\Delta\leq1\) surely. Thus \(\Delta\) has mass \(1-p_{m,n}\) at zero and, conditional on being positive, has the \(\mathrm{Beta}(1,2)\) law. In particular, \(\mathbb E\Delta=p_{m,n}/3\).

**Complete distance distribution.** Put \(a=m/2\), \(b=n/2\), \(v_k(j)=\min(j,k-j)\) for \(j=0,\ldots,k-1\), and \(u_+=\max(u,0)\). Define the following cumulative distribution functions for real \(t\):
\[
H_a(t)=\min\{1,\max\{0,t/a\}\},\qquad
B_{a,b}(t)=\frac{t_+^2-(t-a)_+^2-(t-b)_+^2+(t-a-b)_+^2}{2ab},
\]
\[
h(t)=\min\{1,\max\{0,t\}\},\qquad P(t)=h(t)^2,\qquad Q(t)=2h(t)-h(t)^2.
\]
For every real \(t\), the exact cumulative distribution is
\[
\begin{aligned}
\mathbb P(D\leq t)={}&\tfrac12 B_{a,b}(t)
+\tfrac1{4n}\sum_{j=0}^{n-1} H_a(t-v_n(j))
+\tfrac1{4m}\sum_{i=0}^{m-1} H_b(t-v_m(i))\\
&+\tfrac1{4mn}\left[\sum_{j=1}^{n-1}\big(P(t-v_n(j))-Q(t-v_n(j))\big)
+\sum_{i=1}^{m-1}\big(P(t-v_m(i))-Q(t-v_m(i))\big)\right].
\end{aligned}
\]
This is a finite, completely explicit, piecewise-quadratic formula, including all parity cases and all endpoint values. Its signed correction terms arise from the specific parallel-edge configurations responsible for nonzero detour.

**Mean and sharp sign change.** Let \(\epsilon_k\) be one if \(k\) is odd and zero if \(k\) is even. Then
\[
\boxed{\mathbb ED=\frac{m+n}{4}-\frac{\epsilon_m}{16m}-\frac{\epsilon_n}{16n}+\frac{m+n-2}{12mn}.}
\]
The mean Manhattan distance between two independent *area-uniform* points on the ambient flat torus is \((m+n)/4\). The difference between the network mean and this ambient-area mean is negative exactly for \((m,n)=(3,3)\), zero exactly for \((3,5)\) and \((5,3)\), and strictly positive for every other integer pair \(m,n\geq3\). In particular, the respective means of \(G_{3,3}\), \(G_{3,5}\) and \(G_{4,4}\) are \(323/216\), \(2\), and \(65/32\).

## Assumptions and scope

All graph edges have length one, all cycles are simple with at least three edges, and the sampling law is normalized **one-dimensional** arclength on the network, not two-dimensional ambient area. Points chosen at vertices have probability zero; the formulas nevertheless hold for all threshold values and for the intrinsic metric on the completed metric graph. The ambient metric is the quotient \(\ell_1\) metric, **not** the Euclidean flat-torus metric. A probability law stated conditionally on \(\Delta>0\) uses \(p_{m,n}>0\), which is automatic here.

## Proof

**1. Endpoint routes.** In coordinates modulo \(m\) and \(n\), horizontal edges have the form \((i+s,j)\), and vertical edges \((i,j+s)\), with \(s\in[0,1]\). Vertex-to-vertex path distance is the sum of the two cyclic distances. For distinct edges, any shortest network path enters and exits the two containing edges through endpoints; minimize the four endpoint routes. When the edges coincide, direct motion along that unit interval may be shorter and must be included. This exact route classification shows \(D=L\) except when the two containing edges are parallel, lie in distinct coordinate rows/columns, and have the same running-coordinate edge index. For two such horizontal edges, with cyclic row separation \(k\) and independent edge parameters \(S,T\in[0,1]\),
\[
D=k+\min\{S+T,2-S-T\},\qquad L=k+|S-T|.
\]
The vertical case is identical with coordinates interchanged. Therefore on an exceptional pair
\[
\Delta=2\min\{\min(S,T),1-\max(S,T)\}.
\]
This proves the nonnegative detour and the stated classification; no other path can improve on the four endpoint routes because any change of coordinate direction occurs at a network vertex.

**2. Exceptional-pair count and detour law.** Each orientation has sampling probability \(1/2\). Conditioned on two horizontal edges, the probability that their running indices coincide and their transverse row indices differ is \((n-1)/(mn)\). The vertical analogue has probability \((m-1)/(mn)\). The unconditional exceptional probability is therefore \(p_{m,n}\). Conditional on this event, the parameters \(S,T\) remain independent uniform random variables. For \(0\leq z\leq1\),
\[
\{\Delta>z\}=\{z/2<S<1-z/2,\ z/2<T<1-z/2\}
\]
up to null boundaries, so its conditional probability is \((1-z)^2\). Integration of this survival function yields \(\mathbb E\Delta=p_{m,n}/3\).

**3. Distribution by orientation.** In the horizontal–vertical and vertical–horizontal cases, the endpoint optimization separates into two independent circle-to-vertex distances. A uniform point on a length-\(k\) circle has distance uniformly distributed on \([0,k/2]\) from a fixed vertex. Thus mixed orientations give the sum of two independent uniforms, with CDF \(B_{a,b}\). For two horizontal edges, the ambient distance is the sum of an independent \(\mathrm{Unif}[0,a]\) variable and cyclic row distance \(v_n(J)\), where \(J\) is uniform on \(\{0,\ldots,n-1\}\). This gives \(n^{-1}\sum_jH_a(t-v_n(j))\). For two vertical edges interchange \(m,n\).

Exceptional horizontal pairs of row displacement \(j\in\{1,\ldots,n-1\}\) occur with unconditional probability \(1/(4mn)\) for each \(j\). On them replace the ambient horizontal-coordinate distance \(|S-T|\), whose CDF is \(Q\), by \(\min(S+T,2-S-T)\), whose CDF is \(P\). The same substitution applies to the exceptional vertical pairs. Weighting the four orientation cases and summing these corrections gives exactly the displayed CDF. In particular, because \(P(u)\leq Q(u)\), this independently confirms stochastic domination of \(L\) by \(D\) in the joint sampling law.

**4. Exact mean and sign classification.** For a cycle of length \(k\), the mean distance between two independent uniform vertices is
\[
\frac1k\sum_{j=0}^{k-1}v_k(j)=\frac{k}{4}-\frac{\epsilon_k}{4k}.
\]
Consequently, the ambient network-sampled mean is \((m+n)/4-\epsilon_m/(16m)-\epsilon_n/(16n)\). Add the detour mean from step 2. To classify its difference from \((m+n)/4\), if both side lengths are odd the numerator reduces to \((m+n-8)/(48mn)\); if \(m\) is even and \(n\) odd, it is \((m+4n-8)/(48mn)>0\); if both are even it is \((m+n-2)/(12mn)>0\). The remaining mixed-parity case follows by symmetry. Since odd side lengths are at least three, the only odd–odd negative pair is \((3,3)\), and the only zeros are the two permutations of \((3,5)\). This proves the full classification.

## Verification

Two dependency-free Python programs accompany this proof. `artifacts/verify_metric_routes.py` reconstructs vertex endpoint distances independently and checks exact rational shortest-path and coordinate-detour identities for all \((m,n)\) in \(\{3,4,5,6\}^2\) and nine rational parameter pairs per ordered edge pair: 266,256 exact checks. It also independently counts the exceptional edge pairs and verifies the sharp mean-sign boundary through cycle lengths 20.

`artifacts/verify_cdf_integrals.py` reconstructs, without invoking the conditional-distribution decomposition, the four affine endpoint routes for each ordered edge pair. It partitions the unit parameter square into exact rational polygons where each route is minimal, integrates each affine route there, and clips those polygons against twelve exact rational distance thresholds. All 91 independent mean/CDF comparisons passed for the seven grids \((3,3),(3,4),(3,5),(4,4),(4,5),(5,5),(6,4)\). The universal theorem is proved analytically above; these finite computations independently exercise critical geometry, indexing, normalization and endpoint boundaries.

Run either program with Python 3 and no optional packages. The verification is finite reproducibility evidence, not independent formal or external certification.

## Relationship to prior work

Doig (2004) defines Cartesian products of cycles as toroidal grid graphs and studies Hamiltonian run lengths, not arclength-pair distances. Cheng, Qiu and Shen (2011) derive surface-area generating functions and exact **vertex-to-vertex** mean distances for tori. In particular their odd/even correction in discrete cyclic distance is the vertex ingredient used in proof step 4, but their theorems do not establish continuous edge-pair distributions, the network–ambient detour law, or the area-uniform benchmark classification. Qiang and collaborators (2020) study vertex eccentricity, radius and diameter of products of two cycles, which are different functionals on the vertex set.

Garijo, Márquez and Silveira (2021) supply a general algorithm for continuous mean distance in weighted graphs; their method can compute a numerical instance of the mean in principle but does not directly state this toroidal-grid all-parameter law or full CDF. Baptista, Kennedy and Mugnolo (2024) develop general metric-graph mean-distance bounds rather than the exact pairwise distribution of this family. The present claim combines a complete distribution, a universal conditional detour shape, and a sharp parity-dependent sign classification; none of the inspected primary-source results states these conclusions or a stronger theorem immediately implying them.

## Limitations

The formula is specific to simple, unit-edge Cartesian products of two cycles. It does not assert the same correction for non-unit lengths, higher products, non-Cartesian torus quotients, or an ambient Euclidean flat-torus distance. The geometric comparison uses two *different* sampling measures when comparing the network mean with the area-uniform flat-torus mean; the equality/non-equality conclusion does not mean that their two probability distributions coincide. The 1982 Doyle–Graver publication on mean distance for shapes remains a historical-priority risk because its full text was not inspected; absence of a matching formula in searches is not proof of global novelty.

## References

- Margaret I. Doig, *Maximum Run Length in a Toroidal Grid Graph*, first posted 2004-12-29. https://arxiv.org/abs/math/0412530
- Eddie Cheng, Ke Qiu, Zhizhang Shen, *On the Surface Areas and Average Distances of Meshes and Tori*, *Parallel Processing Letters* 21 (2011), 61–75. https://doi.org/10.1142/S0129626411000072
- Xiaoli Qiang et al., *Distance Measurements Related to Cartesian Product of Cycles*, *Journal of Mathematics* (2020), article 6371694. https://doi.org/10.1155/2020/6371694
- Delia Garijo, Alberto Márquez, Rodrigo I. Silveira, *Continuous Mean Distance of a Weighted Graph*, first posted 2021-03-22. https://arxiv.org/abs/2103.11676
- Paulo Baptista, James B. Kennedy, Delio Mugnolo, *Mean Distance on Metric Graphs*, *Journal of Geometric Analysis* (2024). https://arxiv.org/abs/2312.04952
