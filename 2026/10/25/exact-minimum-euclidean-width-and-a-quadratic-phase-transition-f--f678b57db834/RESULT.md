# Exact minimum Euclidean width and a quadratic phase transition for hypersimplices

## Finding

For integers \(n\ge5\) and \(2\le k\le n-2\), let \(\Delta_{n,k}\) be the standard \((n-1)\)-dimensional hypersimplex, let \(r=\min\{k,n-k\}\), \(h=\lfloor n/2\rfloor\), and \(H=\lceil n/2\rceil\). Its **intrinsic Euclidean minimum width** is exactly

\[
W(\Delta_{n,k})=\min\left\{\sqrt{\frac{n}{n-1}},\;r\sqrt{\frac{n}{hH}}\right\}.
\]

Every unit minimizing normal, and no others, is proportional to a two-level vector whose coordinate blocks have either sizes \(1,n-1\) or sizes \(h,H\). Precisely, if \(n<4r^2-1\) the only possibilities are the singleton-versus-remainder partitions; if \(n>4r^2-1\) the only possibilities are balanced partitions; at the sharp odd integer \(n=4r^2-1\), both families minimize and no additional ones do. Coordinate permutations and sign reversal are understood. In particular, \(W(\Delta_{4r^2,r})=1\), and at fixed \(r\ge2\) the minimum width satisfies \(W(\Delta_{n,r})\sim 2r/\sqrt n\) as \(n\to\infty\).

## Assumptions and scope

The ambient Euclidean space is \(\mathbb R^n\) with its ordinary inner product and its affine hyperplane \(A_k=\{x:\sum_{i=1}^n x_i=k\}\). Set

\[
\Delta_{n,k}=\operatorname{conv}\{\mathbf1_S:S\subseteq\{1,\ldots,n\},\ |S|=k\}
=\{x\in[0,1]^n:\sum x_i=k\}.
\]

The intrinsic normal space is \(V=\{u\in\mathbb R^n:\sum_i u_i=0\}\). For nonzero \(u\in V\), define the projected width

\[
w_{n,k}(u)=\max_{x\in\Delta_{n,k}}\langle x,u\rangle-\min_{x\in\Delta_{n,k}}\langle x,u\rangle.
\]

Then \(W(\Delta_{n,k})=\min_{u\in V,\ \|u\|_2=1}w_{n,k}(u)\). Taking all unit vectors in \(\mathbb R^n\) instead would give the vacuous value zero, since the polytope is contained in a proper affine hyperplane. The theorem covers exactly the genuine non-simplex range \(2\le k\le n-2\). No assertion is made for other types of matroid polytopes or for other norms.

## Proof

**1. Ordered-support formula.** Sort any vector \(u\in V\) so that \(u_1\le\cdots\le u_n\). The maximum of \(\sum_{i\in S}u_i\) over all size-\(k\) subsets is the sum of its largest \(k\) entries, and the minimum is the sum of its smallest \(k\) entries. Since \(\sum_i u_i=0\), replacing \(k\) by \(n-k\) does not change the width. Consequently, with \(r=\min\{k,n-k\}\),

\[
w_{n,k}(u)=\sum_{i=n-r+1}^n u_i-\sum_{i=1}^r u_i.
\tag{1}
\]

**2. Gap generators of the sorted chamber.** For each \(j=1,\ldots,n-1\), define \(v^{(j)}\in V\) by setting its first \(j\) entries equal to \(-(n-j)/n\) and its remaining \(n-j\) entries equal to \(j/n\). It has precisely one nonzero successive-coordinate gap, equal to one, and

\[
\|v^{(j)}\|_2^2=\frac{j(n-j)}n,\qquad
w_{n,k}(v^{(j)})=\min\{r,j,n-j\}.
\tag{2}
\]

Indeed, the second identity counts how many of the \(r\) largest versus \(r\) smallest coordinates differ; it is valid also when \(2r=n\), because both groups then partition the coordinates. For any sorted mean-zero \(u\), set \(\delta_j=u_{j+1}-u_j\ge0\). Its gaps and mean determine it uniquely, so

\[
u=\sum_{j=1}^{n-1}\delta_j v^{(j)}.
\tag{3}
\]

The ordered-support functional (1) is linear throughout this chamber. Put

\[
\gamma_j=\frac{w_{n,k}(v^{(j)})}{\|v^{(j)}\|_2}
=\min\{r,j,n-j\}\sqrt{\frac n{j(n-j)}}
\quad\text{and}\quad M=\min_{1\le j<n}\gamma_j.
\tag{4}
\]

Equations (1)–(4), followed by the Euclidean triangle inequality, give

\[
w_{n,k}(u)=\sum_j\delta_j\gamma_j\|v^{(j)}\|_2
\ge M\sum_j\delta_j\|v^{(j)}\|_2
\ge M\left\|\sum_j\delta_jv^{(j)}\right\|_2=M\|u\|_2.
\tag{5}
\]

Conversely each normalized \(v^{(j)}\) attains ratio \(\gamma_j\), proving \(W=M\). Furthermore, any two distinct nonzero vectors \(v^{(j)}\) and \(v^{(\ell)}\) with \(j\ne\ell\) are not positive scalar multiples: their successive-coordinate gaps occur in different places. Therefore equality in the Euclidean triangle inequality (5) forces **exactly one** \(\delta_j>0\). All minimizing normals are thus exactly the two-level rays indexed by minimizing \(\gamma_j\), together with permutations and negatives. This strictness argument excludes hidden convex combinations of optimal rays.

**3. Determine the minimizing partition sizes.** The values in (4) are invariant under \(j\mapsto n-j\). Restrict to \(1\le j\le h\). If \(1\le j\le r\), then

\[
\gamma_j=\sqrt{\frac{nj}{n-j}},
\]

which increases strictly with \(j\). If \(r\le j\le h\), then

\[
\gamma_j=r\sqrt{\frac n{j(n-j)}},
\]

which decreases strictly with \(j\) except for the irrelevant reflection tie when \(n\) is odd. Hence precisely the endpoint partition sizes \(j=1\) and \(j=h\), and their reflections \(n-1,H\), can be optimal. This gives

\[
M=\min\left\{\gamma_1,\gamma_h\right\}
=\min\left\{\sqrt{\frac n{n-1}},\;r\sqrt{\frac n{hH}}\right\}.
\tag{6}
\]

The balanced partition wins if and only if \(hH>r^2(n-1)\). For odd \(n=2m+1\), the difference is exactly \(m(m+1-2r^2)\); it vanishes if and only if \(n=4r^2-1\), is negative below, and positive above. For even \(n=2m\), the difference is \(m^2-r^2(2m-1)\), a convex quadratic in \(m\). On the admissible interval \(r\le m\le2r^2-1\), both endpoint values are negative: at \(m=r\) it is \(2r^2(1-r)<0\), and at \(m=2r^2-1\) it is \(1-r^2<0\). Convexity makes it negative throughout. On \(m\ge2r^2\) it is positive, since at the left endpoint it is \(r^2>0\) and increases strictly thereafter. This proves the full sharp phase split and all equality cases.

**4. Boundary consequences.** When \(n=4r^2\) the balanced branch in (6) equals one, strictly beating the exceptional branch. For fixed \(r\) and increasing \(n\), the balanced branch is eventually active and equals \(2r/\sqrt n\) for even \(n\), and \(2r\sqrt{n/(n^2-1)}\) for odd \(n\); both give the asserted asymptotic. This concludes the proof.

## Verification

A standalone standard-library script, `verify_width.py`, recomputes the ray ratios and optimal phase with exact rational arithmetic for \(12{,}320\) finite integer pairs, explicitly checks \(25{,}540\) ray widths, and tests the proved norm inequality on \(65{,}800\) random vectors. Run from the directory containing this document using `python3 verify_width.py`. The analytic steps (1)–(6), including strict equality classification, are the proof for all admissible integers; finite tests are only regression checks. Cases at \((r,n)=(2,14),(2,15),(2,16)\) and \((3,34),(3,35),(3,36)\) check both sides and equality at the quadratic threshold.

## Relationship to prior work

Har-Peled and Robson (2023, arXiv:2301.02616) derive the Euclidean width of a regular simplex and give an elementary ordered-coordinate argument. The simplex is precisely the rank-one (or corank-one) hypersimplex, **excluded** from the novel range of this theorem. The full text was inspected, including proof; its width computation does not state the formula or rank-dependent phase for \(2\le k\le n-2\). Martínez-Sandoval and Padrol (2019, arXiv:1909.01189) study hypersimplex projections and skeleton preservation, not its Euclidean minimum width. The known Euclidean inradius of a connected matroid base polytope specializes to the hypersimplex. At the centrally symmetric case \(n=2k\), the identity \(W=2\,\mathrm{inradius}\) can independently recover the formula; **this special case is already implied** and is not advanced as a separate novelty claim. For the noncentrally symmetric family, inradius alone does not determine minimum width. The global formula, both sharp direction classes and the rank-dependent quadratic transition are the asserted contribution.

## Limitations

Absolute publication priority has not been independently certified. The relationship to possible older results under the names Ky Fan spread inequalities, ordered-coordinate norm inequalities, or hypersimplex thickness remains a search risk. This is the intrinsic Euclidean width only, not a result about width with arbitrary ambient-space normals. The statement neither establishes new inradius values nor extends to arbitrary matroid base polytopes. Independent mathematical review has not yet been performed.

## References

1. S. Har-Peled and E. W. Robson, *On the Width of the Regular n-Simplex*, arXiv:2301.02616 (first publicly posted January 6, 2023), https://arxiv.org/abs/2301.02616.
2. L. Martínez-Sandoval and A. Padrol, *The convex dimension of hypergraphs and the hypersimplicial Van Kampen-Flores Theorem*, arXiv:1909.01189 (first publicly posted September 3, 2019), https://arxiv.org/abs/1909.01189.
