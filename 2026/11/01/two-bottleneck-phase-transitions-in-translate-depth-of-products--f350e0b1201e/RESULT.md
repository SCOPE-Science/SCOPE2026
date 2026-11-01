# Two-bottleneck phase transitions in translate depth of products of simplices

## Finding

Let \(r\ge2\), let \(d_1,\ldots,d_r\) be positive integers, and let \(S_i\) be any full-dimensional Euclidean \(d_i\)-simplex. Put \(P=S_1\times\cdots\times S_r\), \(N=\sum_i d_i\), and let \(\mu\) be normalized volume on \(P\). For each \(t>0\), define the translate depth
\[
\mathsf d_t(y)=1-\sup\{\mu(tP+z):z\in\mathbb R^N,\ y\notin tP+z\}.
\]
Every homothety center gives the same family of translates. For the barycentric coordinate functions \(\lambda_{ij}\) of \(S_i\), let \(m_i(y_i)=\max\{0,\min_{0\le j\le d_i}\lambda_{ij}(y_i)\}\) and \(\theta=\min\{t,1\}\). The exact all-point formula is
\[
\boxed{\mathsf d_t(y)=1-\max_{1\le i\le r}\theta^{N-d_i}\min\{\theta,1-m_i(y_i)\}^{d_i}.}\tag{1}
\]
In particular, the depth is constant outside \(P\), at the baseline \(1-\theta^N\), and for every \(t\ge1\) the entire depth function is independent of \(t\).

Write \(p=\min_i d_i\), \(q=\max_i d_i\), and \(T_k=k/(k+1)\). The exact maximal depth \(M(t)=\sup_y\mathsf d_t(y)\) is attained at the product of the simplex centroids. If \(p<q\), define
\[
\boxed{t_*=\left(\frac{T_q^q}{T_p^p}\right)^{1/(q-p)},\qquad T_q<t_*<1.}\tag{2}
\]
Then the exact *three moving phases and final plateau* are
\[
\boxed{M(t)=\begin{cases}
1-t^N,&0<t\le T_q,\\
1-T_q^q t^{N-q},&T_q\le t\le t_*,\\
1-T_p^p t^{N-p},&t_*\le t\le1,\\
1-T_p^p,&t\ge1.
\end{cases}}\tag{3}
\]
The first phase has no depth discrimination: every ambient point maximizes \(\mathsf d_t\). For \(t>T_q\) the entire median set is the product of inner homothetic simplices
\[
\boxed{\operatorname*{argmax}_y\mathsf d_t(y)=\prod_{i=1}^r
\left\{y_i\in S_i:\min_j\lambda_{ij}(y_i)\ge c_i(t)\right\},\quad
c_i(t)=1-\left(\frac{1-M(t)}{\theta^{N-d_i}}\right)^{1/d_i}.}\tag{4}
\]
The factors with dimension \(q\) are forced to their centroids for \(T_q<t<t_*\); those with dimension \(p\) are forced to their centroids for \(t>t_*\). Both extreme dimensions are simultaneously forced at \(t=t_*\); all strictly intermediate factor dimensions have nondegenerate allowable simplices. If all factor dimensions equal \(p=q\), the threshold is \(T_p\), the first branch is \(1-t^N\), the next is \(1-T_p^p t^{N-p}\) until \(t=1\), and the median is uniquely the product centroid whenever \(t>T_p\).

For the **three-dimensional triangular prism** \(P=\Delta_1\times\Delta_2\), the exact transition scales are \(2/3\), \(8/9\), and \(1\):
\[
M(t)=\begin{cases}
1-t^3,&0<t\le2/3,\\
1-4t/9,&2/3\le t\le8/9,\\
1-t^2/2,&8/9\le t\le1,\\
1/2,&t\ge1.
\end{cases}\tag{5}
\]
Its median set jumps from the entire ambient space to a line segment with the triangle factor fixed at its centroid, shrinks to a **single point exactly at \(t=8/9\)**, and then expands into an inner triangle with the segment factor fixed at its midpoint. The terminal triangle has barycentric lower bound \(1-1/\sqrt2\). Thus uniqueness occurs precisely at one isolated dilation scale after the discrimination threshold, despite a uniquely defined testing body and distribution.

## Assumptions and scope

All simplices are nondegenerate, their product decomposition is fixed, and the measure is the uniform product probability measure. The dilated testing body \(tP\) has the same orientation and one common positive scaling factor in every component; arbitrary rotations, different factor scales, nonproduct measures, and a priori constrained query locations are not asserted. Depth uses translates missing the query point, and the supremum need not be attained because exclusion is strict. The formulas use suprema, with limiting translations where needed. The claim applies to all \(y\in\mathbb R^N\), including points on or outside the support.

## Proof

**1. Exact volume of translated homothetic simplices.** Represent \(S_i\) by barycentric coordinates \(\lambda_{ij}(x)\ge0\) with \(\sum_j\lambda_{ij}(x)=1\). Every translate of \(tS_i\) is uniquely described by inequalities \(\lambda_{ij}(x)\ge a_{ij}\), where \(\sum_j a_{ij}=1-t\). Its intersection with \(S_i\) consists of the points whose barycentric coordinates exceed \(\max\{0,a_{ij}\}\). This is either empty or a simplex of volume fraction
\[
\left(1-\sum_j(a_{ij})_+\right)_+^{d_i}.\tag{6}
\]
In particular, maximizing overlap over all translations gives \(\theta^{d_i}\), with \(\theta=\min\{1,t\}\).

**2. Optimize subject to exclusion.** A translate from step 1 misses \(y_i\) exactly when some \(a_{ij}>\lambda_{ij}(y_i)\). If \(m=\min_j\lambda_{ij}(y_i)\), the infimum of \(\sum_j(a_{ij})_+\) under this condition and the fixed-sum condition is
\[
\max\{0,1-t,m\}.\tag{7}
\]
The lower bound follows from the positive-part sum and the excluded barycentric coordinate. To attain it as a limit, choose an index with barycentric value \(m\), set its threshold to \(\max\{0,m+\varepsilon\}\) (or to a negative number just above \(m\) if desired), and distribute the remaining threshold sum equally among the other \(d_i\) coordinates. For \(m\ge0\) and \(\varepsilon>0\), this produces an admissible excluded translate; if \(m<0\), threshold zero already excludes \(y_i\). Taking \(\varepsilon\downarrow0\) proves the infimum, including equality boundaries. Therefore the maximal overlap fraction among the translates excluding \(y_i\) is exactly
\[
q_i(y_i)=\min\{\theta,1-m_i(y_i)\}^{d_i}.\tag{8}
\]

**3. Product factorization.** For the product distribution, the mass of a product translate is the product of factor overlap fractions. The product translate misses \(y\) if and only if some factor misses \(y_i\). Optimizing the disjunction, with all other factors placed at their unconstrained maximum \(\theta^{d_k}\), gives \(\sup\mu(tP+z)=\max_i\theta^{N-d_i}q_i(y_i)\) over excluding translates. This proves (1), including the outside-support baseline and stabilization for \(t\ge1\).

**4. Exact maximal depth.** Each \(m_i(y_i)\) is at most \(1/(d_i+1)\), with equality only at the centroid of \(S_i\). Each term in the maximum from (1) is therefore minimized at its factor centroid, and the whole maximum is minimized simultaneously at the product centroid. Hence, writing \(T_d=d/(d+1)\),
\[
1-M(t)=B(t)=\max_i\theta^{N-d_i}\min\{\theta,T_{d_i}\}^{d_i}.\tag{9}
\]
If \(t\le T_q\), a factor of maximal dimension \(q\) has full overlap \(t^{d_i}\) while every other factor term is at most \(t^N\). Therefore \(B(t)=t^N\); since every point's missing-translate mass is bounded by the same unconstrained maximum, the depth is then constant over the entire ambient space. For \(T_q<t<1\), all \(T_{d_i}<t\), so 
\[
B(t)=t^N\max_i\exp\{b(d_i)-d_i\log t\},\qquad
b(x)=x\log\frac{x}{x+1}.\tag{10}
\]
A direct differentiation gives \(b''(x)=1/[x(x+1)^2]>0\), while \(b'(x)<0\). Thus the expression maximized in (10) is **strictly convex as a function of the factor dimension**; over the finite set \(\{d_i\}\), its maximum is attained at \(p\) or \(q\), and strictly intermediate dimensions are below the upper envelope. At \(t=T_q\) the \(q\)-term strictly dominates the \(p\)-term, while at \(t=1\) the \(p\)-term strictly dominates the \(q\)-term. Their unique crossing is (2), and \(T_q<t_*<1\) follows from \(T_p<T_q\) and \(b(p)>b(q)\). This proves all branches in (3). When \(p=q\), (9) gives the stated two moving pieces and plateau directly.

**5. Median-set classification.** For \(t>T_q\), (9) satisfies \(B(t)<\theta^N\). A point attains maximal depth precisely when, for every factor, \(\theta^{N-d_i}\min\{\theta,1-m_i(y_i)\}^{d_i}\le B(t)\). Since \(B(t)/\theta^{N-d_i}<\theta^{d_i}\), this is equivalent to \(m_i(y_i)\ge c_i(t)\) with the positive threshold (4). Each threshold is at most \(1/(d_i+1)\) by (9), proving that (4) is nonempty and is exactly a product of homothetic inner simplices. A factor collapses to its centroid if and only if its term attains \(B(t)\). The strict convexity above gives precisely the forced factors asserted. In the triangular-prism case \((p,q,N)=(1,2,3)\), (2) yields \(t_*=8/9\); the median set changes from segment to point to triangle by the factor-collapse criterion. The terminal triangle threshold is \(1-(T_1)^{1/2}=1-1/\sqrt2\). For \(t\le T_q\), all ambient points are medians, as shown in step 4.

## Verification

The accompanying standard-library Python program `verify_product_depth.py` passed 434 exact assertions. It independently constructs intersection polygons for translated homothetic triangles using rational Sutherland–Hodgman clipping and shoelace area, and it computes translated interval intersections directly. It compares these geometric volumes to (6), constructs exclusion witnesses approaching the supremum, and checks the triangular-prism phase pieces and endpoint-dimension envelope over specified finite examples. The complete range of dimensions and real scales follows from the analytic argument in steps 1–5; the finite calculations alone are not a substitute for that proof.

## Relationship to prior work

Molchanov and Nagy (arXiv:2610.26108v1, October 19, 2026) define depth by translates and prove broad geometric, probabilistic and asymptotic results, including the general depth-region erosion identity and tangent-cone limit. Their Sections 5 and 6 address dilation and covariograms, but do not give the two-bottleneck phase law, the universal extreme-dimension reduction for arbitrary products of simplices, or the dimension-changing median-set transition of the triangular prism. An earlier exact single-simplex depth computation already treats the case of one simplex: neither that special case nor the bare product factorization is claimed as new here. The new contribution is the complete coupled-dilation maximum and median-set classification for genuine products, especially the strictly convex dimension envelope and isolated crossing phenomenon. Classical homothetic-intersection work of Soltan and earlier Rogers–Shephard results supply geometric background but no such translate-depth phase diagram in the material inspected.

## Limitations

The phase law is exact for a common scalar dilation of a fixed Cartesian product of simplices, uniform product measure, and the stated exclusion-based depth. Unequal component scales can have more complicated envelopes. The source comparison does not establish exhaustive historical priority: older or unindexed results about product covariograms or depth tensorization may exist. The theorem has not undergone independent mathematical audit.

## References

- I. Molchanov and S. Nagy, *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*, arXiv:2610.26108v1, first posted October 19, 2026. https://arxiv.org/html/2610.26108v1
- V. Soltan, *A Characterization of Homothetic Simplices*, Discrete & Computational Geometry 22 (1999), 193–200. https://doi.org/10.1007/PL00009454
