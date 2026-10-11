# Two-contact screening under a minimal orientation swap of balanced cycle root polytopes

## Finding
For every integer \(k\ge3\), put \(L=k-1\) and \(n=2k\). Let \(e_0,\ldots,e_{n-1}\) be the standard orthonormal basis of \(\mathbb R^n\), with indices read cyclically. Define the sign word
\[
(s_0,\ldots,s_{n-1})=(\underbrace{+1,\ldots,+1}_{L},-1,+1,\underbrace{-1,\ldots,-1}_{L})
\]
and the directed-cycle root polytope
\[
P_k=\operatorname{conv}\{v_i=s_i(e_i-e_{i+1}):0\le i<n\}.
\]
This orientation is obtained from the two-block balanced orientation (\(k\) successive positive arcs followed by \(k\) negative arcs) by interchanging its two adjacent boundary signs. Thus it is a nearest nontrivial balanced orientation perturbation of the two-block configuration.

The **unique minimum-enclosing Euclidean ball** of \(P_k\) has squared radius
\[
\boxed{R_k^2=\begin{cases}
\dfrac{28}{17},&k=3,\\[3pt]
2-\dfrac{3(2k-1)}{(k-1)k(k^2-k+1)},&k\ge4.
\end{cases}}
\]
There is a sharp **two-contact phase transition**: for \(k=3\), all six vertices lie on this ball; for every \(k\ge4\), the only vertices strictly inside the ball are \(v_{k-1}\) and \(v_k\). Hence exactly \(2k-2\) vertices touch the ball in every dimension \(k\ge4\). The two screened vertices have the same strictly positive squared-distance clearance:
\[
\boxed{R_k^2-\|v_{k-1}-c_k\|^2
=R_k^2-\|v_k-c_k\|^2
=\frac{6(k^2-4k+2)}{(k-1)k(k^2-k+1)}\quad(k\ge4).}
\]

The center is explicit. For \(k=3\), set
\[
(w_0,\ldots,w_5)=\frac1{34}(7,9,1,1,9,7),
\qquad c_3=\sum_{i=0}^{5}w_iv_i.
\]
For \(k\ge4\), write
\[
\alpha=\frac{3(2L+1)}{L(L+1)(L^2+L+1)},\qquad
 a=\frac{2L^2+2L+1}{2L+1},\qquad
 w_j=\frac{\alpha}{2}(L+1-j)(a-L-1+j)\quad(1\le j\le L).
\]
Then
\[
\boxed{c_k=\sum_{j=1}^{L}w_jv_{j-1}
+\sum_{j=1}^{L}w_jv_{n-j};}
\]
all \(w_j>0\), their sum on each branch is \(1/2\), and the two coefficients of \(v_L\) and \(v_{L+1}\) are zero. This is a complete positive-weight contact certificate.

For comparison, the minimum sphere of the unperturbed two-block orientation has squared radius \(2-6/[k(k^2+2)]\). For \(k\ge4\), the exact squared-radius decrease caused by the adjacent sign exchange is
\[
\boxed{\frac{9k}{(k-1)(k^2+2)(k^2-k+1)}.}
\]
The unperturbed and perturbed directed-edge polytopes have the same face lattice, so the transition is not a combinatorial-type change.

## Assumptions and scope
All distances are the ordinary Euclidean distances inherited from \(\mathbb R^{2k}\), equivalently the intrinsic Euclidean metric on the affine hull of \(P_k\). The sign convention for an arrow \(i\to i+1\) is \(e_i-e_{i+1}\); reversing all arrows negates the polytope and preserves every metric conclusion. The stated family includes all rotations and global sign reversals of the displayed sign word by Euclidean symmetry. Its cyclic sign sequence has \(k\) positive and \(k\) negative entries, and therefore defines a semi-balanced orientation with \(2k\) distinct polytope vertices and affine dimension \(2k-2\).

The theorem classifies this minimally perturbed family for all \(k\ge3\); it makes no claim about other balanced orientation words.

## Proof
**1. A self-contained certificate for minimum balls.** Suppose a finite point set \(\{z_i\}\) has common squared norm \(q\), and suppose \(w_i\ge0\), \(\sum_iw_i=1\), and \(c=\sum_iw_iz_i\) satisfy
\[
\langle c,z_i\rangle\ge\|c\|^2\quad\text{for all }i,
\qquad
\langle c,z_i\rangle=\|c\|^2\quad\text{if }w_i>0.
\tag{1}
\]
Every point lies in the ball with center \(c\) and squared radius \(q-\|c\|^2\). For any other center \(y\), the exact weighted identity
\[
\sum_iw_i\|z_i-y\|^2=q-\|c\|^2+\|y-c\|^2
\tag{2}
\]
shows that the largest vertex-distance squared is at least \(q-\|c\|^2+\|y-c\|^2\). Thus \(c\) is the **unique** minimum-ball center. Moreover \(z_i\) is tangent exactly when equality holds in its instance of (1).

**2. Two equal arms after omitting the exchanged arcs.** For \(k\ge4\), put \(L=k-1\). The \(2L\) vectors \(v_i\) with \(i\notin\{L,L+1\}\) represent two length-\(L\) paths, both directed from vertex \(0\) toward their respective terminal vertices \(L\) and \(L+2\). The two paths have no other common graph vertices. Index the oriented arcs along either path by \(j=1,\ldots,L\) outward from their common source. Their Euclidean Gram matrix has diagonal \(2\), adjacent entries \(-1\) within each path, and one cross-entry \(+1\) between the first arcs of the two paths; all other cross-entries vanish.

Choose \(\alpha,a,w_j\) as in the finding and assign \(w_j\) to the \(j\)-th arc on **each** path. Elementary finite sums give
\[
\sum_{j=1}^Lw_j=\frac12,\qquad w_j>0.
\tag{3}
\]
For a branch's interior arcs, the quadratic formula has constant second difference
\[
2w_j-w_{j-1}-w_{j+1}=\alpha\quad(1<j<L).
\tag{4}
\]
At the terminal arc \(j=L\), the formula gives \(2w_L-w_{L-1}=\alpha\). At the common source, where the first arcs have positive mutual Gram product, the chosen value of \(a\) gives
\[
3w_1-w_2=\alpha.
\tag{5}
\]
The same equations hold on the reflected branch. Consequently every supported vertex satisfies
\[
\langle c_k,v_i\rangle=\alpha\qquad(i\notin\{L,L+1\}).
\tag{6}
\]
Multiplying (6) by its coefficient and summing, using (3), proves \(\|c_k\|^2=\alpha\).

**3. The two omitted arcs.** The intermediate graph vertex \(L+1\) is isolated in the supported two-path subgraph, so its coordinate in \(c_k\) vanishes. Both terminal vertices \(L\) and \(L+2\) have center coordinate \(-w_L\). The omitted arcs are directed outward from vertex \(L+1\) to those two terminals; therefore
\[
\langle c_k,v_L\rangle=\langle c_k,v_{L+1}\rangle=w_L.
\tag{7}
\]
Direct algebra yields
\[
w_L-\alpha=\frac{3(L^2-2L-1)}{L(L+1)(L^2+L+1)}.
\tag{8}
\]
Since \(L\ge3\), expression (8) is strictly positive. Thus (1) holds at **every** original root vertex, equality holds precisely for the \(2L\) supported arcs, and the two omitted arcs are strictly inside. Each root vector has squared norm \(2\), so the unique minimum enclosing radius squared is \(2-\alpha\). Equation (8) multiplied by \(2\) gives the stated clearance. Substituting \(L=k-1\) gives all displayed formulas.

**4. The exceptional six-cycle.** For \(k=3\), the six coefficient values \((7,9,1,1,9,7)/34\) are positive and sum to \(1\). Direct incidence-vector multiplication shows
\[
\left\|\sum_{i=0}^5w_iv_i\right\|^2=\frac6{17},
\qquad \langle v_i,\sum_{j=0}^5w_jv_j\rangle=\frac6{17}
\quad(0\le i\le5).
\tag{9}
\]
Applying (1)--(2) proves the exceptional squared radius \(2-6/17=28/17\) and contact of all six vertices. In fact the two-path certificate from Step 3 fails here because its proposed weights violate the omitted-arc inequality; hence this case cannot be silently absorbed into the larger-dimensional formula.

**5. Comparison with the two-block orientation.** For the sign word with \(k\) consecutive positive signs followed by \(k\) negative signs, the arc graph is two directed length-\(k\) paths with a common source and common sink. The positive normalized weights along either path can be taken as
\[
\frac{3(2j(k+1-j)-k)}{2k(k^2+2)}\qquad(1\le j\le k).
\]
Their Gram products with the associated barycenter all equal \(6/[k(k^2+2)]\), and the coefficients on both paths add to \(1\). Applying (1)--(2) proves its minimum squared radius \(2-6/[k(k^2+2)]\). Subtracting the perturbed squared radius for \(k\ge4\) simplifies exactly to the stated positive rational decrease.

Finally, because the oriented cycle incidence vectors have one linear dependence \(\sum_i s_iv_i=0\) and the orientation is balanced \(\sum_i s_i=0\), this is their unique affine dependence. The two sign classes each contain \(k\) vertices, and the polytope is an affine free sum of two \((k-1)\)-simplices. The two-block and perturbed words have the same sign-class cardinalities and thus the same face lattice, as also follows from the source's oriented-cycle face classification.

## Verification
The independent `verify.py` included with this result constructs every incidence vector using exact integers, computes its prescribed barycenter with rational fractions, checks nonnegative weights and normalization, checks the exact center norm and all vertex inner-product optimality inequalities, and directly recomputes each squared Euclidean distance and the contact set. It checks every integer \(3\le k\le70\) with no floating-point arithmetic. The mathematical proof above, not the finite checker, establishes the theorem for all integers \(k\ge3\). Reproduce with `python3 verify.py` in the directory containing both this document and the checker.

## Relationship to prior work
Numata, Takahashi, and Tamaki classify faces of directed edge polytopes and, in their oriented-cycle example, describe the relevant balanced orientations and their combinatorial type. Kálmán and Tóthmérész establish the underlying semi-balanced directed-root-polytope and Ehrhart/dissection theory. Neither of those inspected primary texts determines the Euclidean minimum enclosing sphere for the present minimally perturbed orientation or its two-contact transition.

For an independent numerical comparison with the prior common-vertex-sphere construction, the directed cycle has cyclic height sequence \(0,1,\ldots,L,L-1,L,L-1,\ldots,1\) when \(L=k-1\). Its centered squared height norm is
\[
S_{\mathrm{height}}=\frac{L^4+4L^3-4L^2+8L+3}{6(L+1)}.
\]
The canonical sphere through all vertices has squared radius \(2-1/S_{\mathrm{height}}\), whereas the actual minimum sphere derived here has squared radius \(2-\alpha\). For every \(L\ge3\),
\[
\alpha-\frac1{S_{\mathrm{height}}}
=\frac{9(L^2-2L-1)^2}{L(L+1)(L^2+L+1)(L^4+4L^3-4L^2+8L+3)}>0.
\]
Thus the canonical sphere is **strictly nonminimal** in every genuinely screened dimension, an independently checkable distinction from the prior theory.

A general metric result on semi-balanced root polytopes gives an all-vertex sphere from the variance of a layer function and tests whether that sphere is minimum by a nonnegative-flow criterion. **That general formula is not a formula for the true minimum ball when the criterion fails.** In the present family it fails for every \(k\ge4\): two root vertices must be screened. The novel content is the complete correct replacement minimum sphere, exact weights, unique center, exceptional six-cycle, and both strict contact clearances. A separate directed-path one-reversal sphere calculation concerns a different incidence graph and cannot determine the two omitted-arc distances in this cyclic configuration.

Related orientation-dependent Ehrhart calculations for balanced cycle-root polytopes count lattice points rather than solve the Euclidean contact problem. In particular, combinatorial equivalence and equal numbers of positive and negative edges do not force equal Euclidean enclosing radii.

## Limitations
Only the single nearest adjacent sign exchange of the two-block balanced orientation is treated; this does not classify minimum spheres for arbitrary balanced oriented cycles. The Euclidean data depend on the standard orthonormal root-vector realization and are not invariant under arbitrary affine maps. The classical equal-norm ball-certificate identity is not claimed new. Independent external mathematical review has not been performed. Although relevant accessible primary full texts and targeted scientific comparisons were inspected, a differently named pre-existing minimum-ball calculation remains a residual literature-search risk.

## References
1. Yasuhide Numata, Yusuke Takahashi, and Dai Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521v1, first publicly posted 2022-03-28, primary MSC2020 52B05. See especially Example 5.3 and the face characterization, https://arxiv.org/html/2203.14521v1.
2. Tamás Kálmán and Lilla Tóthmérész, *Root polytopes and Jaeger-type dissections for directed graphs*, arXiv:2105.00960v3, https://arxiv.org/html/2105.00960v3, especially Sections 1--4 on semi-balanced root polytopes and Ehrhart theory.
