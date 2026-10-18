# Exact Rips persistence and unit-cube homology bases of three-dimensional Manhattan boxes

## Finding
For any three nonnegative integers \(a,b,c\), let
\[
 B_{a,b,c}=\{0,\ldots,a\}\times\{0,\ldots,b\}\times\{0,\ldots,c\}\subset\mathbb Z^3,
 \qquad d(x,y)=\sum_{i=1}^{3}|x_i-y_i|.
\]
Write \(X_r=\operatorname{VR}_{\le r}(B_{a,b,c})\), the abstract simplicial complex of all finite nonempty subsets of diameter at most \(r\). Put
\[
 N=(a+1)(b+1)(c+1),\qquad
 E=a(b+1)(c+1)+b(a+1)(c+1)+c(a+1)(b+1),\quad R=E-N+1.
\]
For every real \(r\ge0\), its homotopy type is
\[
 X_r\simeq\begin{cases}
 \coprod^{N}\{\mathrm{pt}\},&0\le r<1,\\
 \bigvee^{R}S^1,&1\le r<2,\\
 \bigvee^{abc}S^3,&2\le r<3,\\
 \{\mathrm{pt}\},&r\ge3.
 \end{cases}
\]
A zero-fold wedge means a point. In degree three at scale two, the fundamental classes of the scale-two Rips complexes on the \(abc\) unit coordinate cubes form an **integral basis** of \(\widetilde H_3(X_2;\mathbb Z)\). Inclusions of one coordinate-aligned integer box into a larger one preserve this cube-indexed basis and induce injections in degree three at scale two.

Over every field, the finite persistence barcode consists precisely of one degree-zero interval \([0,\infty)\), \(N-1\) degree-zero intervals \([0,1)\), \(R\) degree-one intervals \([1,2)\), and \(abc\) degree-three intervals \([2,3)\). There are no other bars.

## Assumptions and scope
All three side lengths \(a,b,c\) are integers \(\ge0\). The metric is **Manhattan distance on vertices**, not Euclidean distance, ternary Hamming distance, toroidal distance, or the metric of a graph with extra wraparound edges. Thresholds are **inclusive**. In this convex grid box, Manhattan distance equals the ordinary shortest-path distance in the Cartesian product of three paths. The result concerns the full simplicial complexes and integral homotopy types, not just mod-two ranks.

## Proof
**1. Previously established topological baseline, with parameters checked.** Gupta, Sarkar and Shukla, *On the Vietoris-Rips Complexes of Integer Lattices* (arXiv:2511.04238v1, November 6, 2025), define \(\Delta_m^{n,2}=\operatorname{VR}_{\le2}(\{0,\ldots,m\}^n)\). Their Theorem 4.13 states that for \(m\ge3\) and \(n\ge3\), \(\Delta_m^{n,2}\) is homotopy equivalent to a finite wedge of three-spheres (with sphere multiplicity left implicit and a lower bound in the three-dimensional case). In the proof of Theorem 3.15 they establish contractibility of each finite \(\operatorname{VR}_{\le r}(\{0,\ldots,m\}^n)\) for \(2\le n\le5\) and \(r\ge n\). We apply both results only at \(n=3\).

Choose \(M\ge\max\{3,a,b,c\}\). The coordinatewise clamping map
\[
 q(x_1,x_2,x_3)=(\min\{a,x_1\},\min\{b,x_2\},\min\{c,x_3\})
\]
from \(\{0,\ldots,M\}^3\) to \(B_{a,b,c}\) is \(1\)-Lipschitz for \(d\) and fixes \(B_{a,b,c}\). Therefore it induces a simplicial retraction at every threshold. Since the larger scale-two complex is a wedge of three-spheres, the smaller one, as its retract, is simply connected, has no reduced integral homology except a finitely generated free group in degree three, and has trivial \(\pi_2\). A wedge of degree-three maps representing an integral basis (using the Hurewicz isomorphism in degree three) is a homology equivalence and hence a homotopy equivalence by the homology Whitehead theorem. Thus \(X_2\) is itself a wedge of three-spheres, with multiplicity to be calculated. Likewise \(X_r\) is a retract of a contractible space for \(r\ge3\), so it is contractible.

**2. Exact Euler characteristic by a local sign-reversing involution.** Every nonempty simplex \(\sigma\in X_2\) has coordinatewise span \(w_i=\max_{x\in\sigma}x_i-\min_{x\in\sigma}x_i\le2\). Translate each simplex so that its three coordinate minima are zero. For \(w\in\{0,1,2\}^3\) let \(\gamma_w\) be the signed sum \(\sum_{\sigma}(-1)^{|\sigma|-1}\) over these **normalized** cliques with exact span vector \(w\). This is a finite local enumeration, independent of the box dimensions.

If some coordinate span equals two, say the first, every such simplex contains an extreme pair \(u=(0,p,q)\) and \(v=(2,p,q)\): the other coordinates must agree because \(d(u,v)\le2\). All other vertices are within Manhattan distance at most one from the midpoint \(h=(1,p,q)\). Inserting or deleting \(h\) consequently preserves the clique condition and exact span vector. The extreme pair is unaffected; the midpoint is uniquely determined; and the operation is an involution reversing \((-1)^{|\sigma|-1}\). Hence \(\gamma_w=0\) whenever any \(w_i=2\).

For span vectors in \(\{0,1\}^3\), symmetry shows that \(\gamma_w\) depends only on the number \(k\) of unit spans. The values are
\[
 \gamma_0=1,\qquad \gamma_1=-1,\qquad \gamma_2=1,\qquad \gamma_3=-2.
\]
Indeed, a point contributes one and an adjacent pair contributes minus one. On a unit square all four vertices are mutually at distance at most two, so its Rips complex is a simplex with Euler characteristic one; subtracting its four point contributions and four edge-span contributions gives \(\gamma_2=1\). On a unit three-cube exactly the four antipodal vertex pairs have distance three. Its Rips complex is the boundary of the four-dimensional cross-polytope, hence is \(S^3\) with Euler characteristic zero. Removing the contributions from proper spans gives \(0=8-12+6+\gamma_3\), so \(\gamma_3=-2\).

A normalized simplex with width vector \(w\) has exactly \(\prod_i(s_i-w_i+1)\) placements in the box with \((s_1,s_2,s_3)=(a,b,c)\), when each \(s_i\ge w_i\). After the vanishing of all width-two contributions and the four displayed weights, the Euler characteristic is exactly
\[
 \begin{aligned}
 \chi(X_2)={}&(a+1)(b+1)(c+1)
 -a(b+1)(c+1)-b(a+1)(c+1)-c(a+1)(b+1)\\
 &+ab(c+1)+ac(b+1)+bc(a+1)-2abc
 =1-abc.
 \end{aligned}
\]
The formula also holds when some side length is zero, because the corresponding nonzero-span placement counts vanish. Since \(X_2\) is a wedge of three-spheres, \(\chi(X_2)=1-\operatorname{rank}\widetilde H_3(X_2;\mathbb Z)\), giving the exact multiplicity \(abc\).

**3. Natural integral basis and its independence.** For each \(u=(i,j,k)\) with \(0\le i<a\), \(0\le j<b\), \(0\le k<c\), write \(Q_u=\{i,i+1\}\times\{j,j+1\}\times\{k,k+1\}\). As above, \(\operatorname{VR}_{\le2}(Q_u)\) is the boundary of a four-dimensional cross-polytope, so any choice of orientation gives a fundamental integral three-cycle \(z_u\). Its inclusion in \(X_2\) defines an integral class.

For each target cube \(Q_t\), clamp each coordinate of the **whole box** to the corresponding interval of \(Q_t\). This is again a \(1\)-Lipschitz simplicial retraction onto \(\operatorname{VR}_{\le2}(Q_t)\). It takes \(z_t\) to a generator. When \(u\ne t\), one coordinate interval of \(Q_u\) is different from that of \(Q_t\), so its image under that clamp is a single coordinate level of \(Q_t\); all resulting vertices lie in a four-vertex face whose Rips complex is a full simplex. Thus the induced homology map sends \(z_u\) to zero. The resulting evaluation matrix on the \(abc\) classes is diagonal with \(\pm1\) entries. Consequently their span is a **split direct summand** of \(\widetilde H_3(X_2;\mathbb Z)\), not merely a full-rank subgroup: the product of the clamping retractions is an integral left inverse. Since this ambient homology group is free of rank \(abc\), its complementary free summand has rank zero. Thus the classes form an **integral basis**. Their same-chain representatives under inclusion of nested boxes give the stated naturality and injectivity.

**4. Remaining filtration stages.** If \(0\le r<1\), only singleton simplices occur. If \(1\le r<2\), the complex is exactly the connected Cartesian grid graph: it has \(N\) vertices, \(E\) edges, and no triangles, so it is \(\bigvee^{E-N+1}S^1\). For \(2\le r<3\), the preceding proof applies unchanged. For \(r\ge3\), contractibility was shown in Step 1. The barcode follows because only one reduced homology degree occurs at each noncontractible positive-integer stage; in particular, all cross-stage homomorphisms in positive degrees are zero.

## Verification
`VERIFY.py` is a standalone standard-library checker. It enumerates all local scale-two cliques in the \(3\times3\times3\) point grid, checks the 27 signed span coefficients and their cancellations, checks distinct cube retractions, and independently computes complete mod-two simplicial boundary ranks for eight boxes through \(4\times4\times4\) vertices. Its recorded output is `VERIFY_OUTPUT.txt`. This is finite corroboration, **not** a substitute for the general proof in Steps 1–4. In particular, finite mod-two calculations alone would not show torsion-freeness or the infinite family of homotopy types.

## Relationship to prior work
Gupta–Sarkar–Shukla (arXiv:2511.04238, Theorem 4.13) already prove a three-sphere-wedge homotopy type for **equal-sided finite integer lattice cubes** at scale two; they leave its multiplicity as an unspecified \(\nu_m\), giving only \(\nu_m\ge(m-2)^3\) in dimension three. Their finite-box proof of contractibility at scales at least three underlies the terminal stage. The exact formula \(abc\) for all rectangular boxes, the local midpoint-cancellation calculation, and the explicit unit-cube integral basis and inclusion functoriality are the additions here. For an equal-sided box \(\{0,\ldots,m\}^3\), the new formula specializes to the **exact** value \(m^3\).

Adamaszek–Adams (arXiv:2103.01040, Theorem 1) classify scale-two Rips complexes of **binary** Hamming cubes; their three-cube case is the local sphere used here, not a classification of longer Manhattan grid boxes. Adams–Adetowubo–Barriga-Acosta–Feng–Sterling (arXiv:2502.07134) consider **periodically identified two-dimensional torus grids**, whose metric and boundary conditions differ. The published ternary Hamming-cube calculation on 27 points likewise uses Hamming distance, whereas the present \(\{0,1,2\}^3\) carries Manhattan distance; the resulting scale-two third Betti numbers are respectively 46 and 8 and cannot be substituted for one another.

## Limitations
The homotopy classification uses the previously published finite equal-cube wedge and contractibility theorems as its topological baseline; it independently derives the exact multiplicities, basis and persistence consequences. The theorem is limited to three coordinate directions and the integer Manhattan metric; it does not provide exact multiplicity formulas for higher-dimensional boxes, other metrics or scales beyond this particular three-dimensional filtration in other spaces. Publicly unindexed equivalent work remains a possible originality risk.

## References
1. R. K. Gupta, S. Sarkar and S. Shukla, *On the Vietoris-Rips Complexes of Integer Lattices*, arXiv:2511.04238v1 (first posted 2025-11-06), Theorems 3.15 and 4.13, Lemma 4.11. https://arxiv.org/pdf/2511.04238
2. M. Adamaszek and H. Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040, Theorem 1 and the three-cube example. https://arxiv.org/pdf/2103.01040
3. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng and J. Sterling, *Vietoris-Rips complexes of torus grids*, arXiv:2502.07134. https://arxiv.org/pdf/2502.07134
