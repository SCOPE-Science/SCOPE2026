# Exact edge-length sensitivity and high-order saturation of complete-bipartite Lipschitz ball volumes

## Finding

Let \(p,q\ge2\) be integers, let \(d=p+q-1\), and let \(h\in[1,3]\) be real. On the complete bipartite graph \(K_{p,q}\), give exactly one distinguished cross edge length \(h\) and give all remaining edges length one. Let \(M_{p,q,h}\) carry the induced shortest-path metric. Choose its first-part endpoint \(a_1\) as the basepoint. Let \(V_{p,q}(h)\) be the ordinary \(d\)-dimensional Lebesgue volume of the real unit ball of \(\operatorname{Lip}_0(M_{p,q,h})\) in the anchored vertex-potential coordinates.

The exact formula, simultaneously for all such parameters, is
\[
V_{p,q}(h)=\frac{2^d(p-1)!(q-1)!}{d!}
\left[pq+2\left(1-\left(\frac{3-h}{2}\right)^d\right)\right].
\]
It gives an exact relative volume increase when the selected edge is removed:
\[
\frac{V_{p,q}(3)}{V_{p,q}(1)}=1+\frac{2}{pq},
\qquad
V_{p,q}(3)-V_{p,q}(h)
=\frac{2(p-1)!(q-1)!}{d!}(3-h)^d.
\]
Therefore its first \(d-1\) one-sided derivatives vanish at the redundant-edge endpoint \(h=3\), while its \(d\)-th derivative is nonzero. For any \(h<3\), the volume increases strictly with the selected edge length. At fixed \(p+q\), the relative full-deletion gain is largest when \(\min\{p,q\}=2\) and smallest when the two classes are as balanced as possible.

## Assumptions and scope

Write the vertex classes as \(A=\{a_1,\ldots,a_p\}\) and \(B=\{b_1,\ldots,b_q\}\). The exceptional edge is \(a_1b_1\). All other cross edges have length one. Since \(p,q\ge2\), a path of three ordinary edges joins \(a_1\) to \(b_1\). For \(1\le h\le3\), the graph's shortest-path metric has exactly the specified cross-edge distances; the other cross distances are one and all within-class distances are two. For \(h=3\) the exceptional edge constraint is redundant, which is the same metric as deletion of that edge.

The dual unit ball consists of potentials \(f:A\cup B\to\mathbb R\) with \(f(a_1)=0\) and \(\lvert f(u)-f(v)\rvert\le d_{M}(u,v)\) for all vertices. Equivalently it suffices to impose the weighted graph-edge inequalities. The measure is ordinary Lebesgue measure on the \(p+q-1\) free potential coordinates, **not** Euclidean Hausdorff volume in a zero-sum hyperplane. The formula has no assertion for \(h<1\), \(h>3\), \(p=1\), or \(q=1\).

## Proof

**Step 1: a determinant-one description.** Fix \(f(a_1)=0\), and make the linear change
\[
t=f(b_1),\qquad u_i=f(a_{i+1})-t\quad (1\le i<p),
\qquad v_j=f(b_{j+1})\quad(1\le j<q).
\]
It is triangular with determinant of absolute value one. Put \(a=p-1\) and \(b=q-1\). The edge inequalities become
\[
u_i,v_j\in[-1,1],\qquad
\lvert t+u_i-v_j\rvert\le1\quad\text{for all }i,j,
\qquad\lvert t\rvert\le h.
\]
These conditions describe the entire unit ball, so Fubini's theorem applies to this bounded polytope.

**Step 2: differentiate the moving cross-edge slab.** For \(1<h<3\), the derivative with respect to \(h\) is the sum of the sections at \(t=h\) and \(t=-h\). The involution \((t,u,v)\mapsto(-t,-u,-v)\) makes these two sections equal. At \(t=h\), since \(u_i,v_j\in[-1,1]\), the lower inequalities \(h+u_i-v_j\ge-1\) are automatic for \(h\ge1\). The upper inequalities are equivalent to
\[
\min_j v_j-\max_i u_i\ge h-1.
\]
Denote the common section measure by \(S(h)\). If \(x=\max_i u_i\), the (unnormalized) measure of the \(u\)-vectors with this maximum in \([x,x+dx]\) is \(a(x+1)^{a-1}\,dx\), for \(-1\le x\le1\). The possible \(v\)-vectors then form an interval product of volume \((2-h-x)^b\), provided \(x\le2-h\). Consequently
\[
S(h)=a\int_{-1}^{2-h}(x+1)^{a-1}(2-h-x)^b\,dx.
\]
Substitute \(x+1=(3-h)s\). Euler's beta integral gives
\[
S(h)=a(3-h)^{a+b}\int_0^1s^{a-1}(1-s)^b\,ds
=\frac{a!b!}{(a+b)!}(3-h)^{a+b}.
\]
Since \(a+b=d-1\),
\[
\frac{d}{dh}V_{p,q}(h)
=\frac{2(p-1)!(q-1)!}{(d-1)!}(3-h)^{d-1}
\qquad(1<h<3).
\]
This is strictly positive in the stated interval.

**Step 3: compute the undeformed volume.** When \(h=1\), the constraints are those of the unit-edge complete bipartite graph. For an anchored \(A\)-potential vector, write \(r\) for the range of its \(p\) vertex values. The \(B\) coordinates are independent in a common allowable interval of length \(2-r\), provided \(0\le r\le2\). The measure of anchored \(A\)-vectors with range in \([r,r+dr]\) is \(p(p-1)r^{p-2}\,dr\). To see this, for \(p-1\) free coordinates relative to the anchor, either the anchor is an extremum (two choices of sign, each with \((p-1)r^{p-2}\) boundary density) or both a negative and a positive extremum occur (the remaining \((p-1)(p-2)r^{p-2}\) density from two ordered extremes); the total is \(p(p-1)r^{p-2}\). Thus
\[
V_{p,q}(1)
=p(p-1)\int_0^2r^{p-2}(2-r)^q\,dr
=\frac{2^d p!q!}{d!}.
\]
This established complete-bipartite baseline is included for normalization and is not separately asserted as new.

**Step 4: integrate and close the endpoints.** Integration of Step 2 from \(1\) to \(h\), together with Step 3, gives
\[
V_{p,q}(h)=\frac{2^dp!q!}{d!}
+\frac{2(p-1)!(q-1)!}{d!}\left(2^d-(3-h)^d\right).
\]
Algebraic rearrangement yields the formula in the Finding. The cross-sectional integral is continuous for all \(h\in[1,3]\), hence the endpoint assertions follow. Subtracting the expression at \(h=3\) proves exact order-\(d\) flatness. Because \(pq\) is minimal at \(\min\{p,q\}=2\) and maximal for a balanced split at fixed \(p+q\), the fixed-order extremal statement also follows.

## Verification

The executable standalone file `verify.py` enumerates integer lattice points of every dilated anchored polytope by grouping the \(u\) and \(v\) integer-coordinate vectors according to their minima and maxima. For integral edge lengths it takes the \(d\)-th forward difference of Ehrhart counts at dilations \(0,1,\ldots,d\); the matrix of integer difference constraints is totally unimodular, so Ehrhart's theorem applies and the leading coefficient is the volume. For rational heights \(h=r/s\), clearing denominators gives a lattice polytope, whose leading coefficient divided by \(s^d\) gives the original volume. These counts are independent of the beta-integral derivation and are not used to justify the infinite-dimensional-parameter statement.

The checker passed 33 integer-height cases and six rational-height cases, including \(h=3/2\) and \(h=5/2\). Selected exact volumes: \(V_{2,2}(1)=16/3\), \(V_{2,2}(2)=23/3\), \(V_{2,2}(3)=8\); \(V_{3,4}(1)=64/5\), \(V_{3,4}(2)=149/10\), and \(V_{3,4}(3)=224/15\). Run `python3 verify.py` with Python 3 standard library.

## Relationship to prior work

Alexander, Fradelizi, García-Lirola, and Zvavitch (arXiv:1911.10642) establish the finite-metric Lipschitz-free/polar convex-body framework and study volume products and undeformed metrics. Their Section 5 treats volume products and the equilateral complete-graph case; their complete-bipartite discussion in Section 3 is an isometric-decomposition characterization, not the varying single-cross-edge polar volume here. Aliaga (arXiv:2102.01219, 2020 MSC primary 46B20) develops the extreme-point theory for Lipschitz-free Banach balls, rather than the specified continuous volume profile. Higashitani, Jochemko, and Michałek (arXiv:1807.07678) compute combinatorial invariants of primal symmetric-edge polytopes for undeformed graphs. A known exact undeformed complete-bipartite dual-volume formula supplies Step 3, but does not by itself imply the positive \(h\)-dependence or order-\(d\) saturation at edge redundancy.

Related geometric computations for a complete bipartite graph with one missing edge may give different invariants (facet counts, geodesic numbers, ellipsoids, distortion); none of the checked accessible primary statements determines the all-real-weight anchored polar-volume law above. The comparison is by mathematical object and implication, not solely by paper title.

## Limitations

This result concerns only one changed cross edge and only the interval \(1\le h\le3\) with both classes of size at least two. No formula is asserted for simultaneous deformation of multiple cross edges. The metric family becomes stationary for \(h>3\) under shortest-path closure, but that region is not included in the theorem. Exact volume depends on anchored-coordinate normalization; conversion to intrinsic Euclidean volume requires a separate Jacobian. Independent scientific audit has not been performed, and unindexed equivalent literature remains a residual bibliographic risk.

## References

1. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (public version 2019-11-24), especially Sections 3 and 5.
2. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (public version 2021-02-01), 2020 MSC Primary 46B20.
3. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (public version 2018-07-20), Section 4.
