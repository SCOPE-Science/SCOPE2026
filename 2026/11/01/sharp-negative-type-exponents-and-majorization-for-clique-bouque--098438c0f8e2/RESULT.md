# Sharp negative-type exponents and majorization for clique bouquets

## Finding
For integers \(r\ge 2\) and \(m_1,\ldots,m_r\ge1\), let \(G=K_1\vee\bigl(K_{m_1}\sqcup\cdots\sqcup K_{m_r}\bigr)\), with its ordinary shortest-path distance \(d\). Each \(K_{m_i}\) is a blade, and the extra vertex is the hub. For \(t>2\) define
\[
 F_{\mathbf m}(t)=(t-2)\sum_{i=1}^r\frac{m_i}{(t-1)m_i+1}.
\]
There is exactly one \(t_*(\mathbf m)>2\) satisfying \(F_{\mathbf m}(t_*)=1\). The **supremal negative-type exponent** is
\[
 \boxed{\wp(G)=\log_2 t_*(\mathbf m).}
\]
In particular, the kernel \(d(u,v)^p\) is conditionally negative semidefinite exactly for \(0\le p\le\wp(G)\), and strictly so for \(0\le p<\wp(G)\). At the endpoint its zero-sum nullspace is exactly one-dimensional. The metric \(d^{p/2}\) has a Euclidean realization of minimal affine dimension \(M=\sum_i m_i\) below the endpoint and \(M-1\) at the endpoint.

At fixed \(r\) and \(M\ge r\), \(\wp(G)\) is **minimized** precisely when the blade sizes are as equal as possible and **maximized** precisely when, up to permutation, the sizes are \((M-r+1,1,\ldots,1)\). Both equality classifications include the cases where the extremal partitions coincide. Moreover, for \(r\) equal blades of size \(m\),
\[
 \boxed{\wp(G)=\log_2\frac{2r-1+1/m}{r-1}.}
\]
This includes the classical star case \(m=1\); the unequal-blade exponent and fixed-size majorization law are the subject of the finding.

## Assumptions and scope
The assertion concerns every finite graph obtained from \(r\ge2\) nonempty, pairwise disjoint cliques by adjoining one vertex incident with all other vertices; there are no edges between distinct blades. The graph distance takes values \(0,1,2\). For \(p=0\), the convention is \(d(u,v)^0=1\) for distinct vertices and \(0\) on the diagonal. Negative type means
\[
 \sum_{u,v\in V(G)} c_uc_vd(u,v)^p\le0
 \quad\text{whenever}\quad\sum_u c_u=0,
\]
for **all real** coefficients \(c_u\), and strict negative type means strict inequality for each nonzero zero-sum coefficient vector. Complex coefficients give the equivalent Hermitian formulation. The empty-blade and single-blade cases are excluded; with one blade the graph is complete and has strict negative type for every finite exponent.

## Proof
Put \(t=2^p\). Given a real zero-sum vector, write \(x_{i,a}\) for its coefficients on blade \(i\), \(s_i=\sum_{a=1}^{m_i}x_{i,a}\), and \(x_0=-\sum_i s_i\) at the hub. Expanding the distance-power form, separating same-blade and cross-blade pairs, yields the **exact identity**
\[
 Q_p(x)=\sum_{u,v}c_uc_vd(u,v)^p
 =-\sum_{i,a}x_{i,a}^2+(1-t)\sum_i s_i^2+(t-2)\left(\sum_i s_i\right)^2.\tag{1}
\]
For fixed blade sums, the elementary inequality \(\sum_a x_{i,a}^2\ge s_i^2/m_i\) is sharp precisely when \(x_{i,a}=s_i/m_i\). Consequently,
\[
 \sup_{x:\,\sum_a x_{i,a}=s_i}Q_p(x)
 =-\sum_i a_i(t)s_i^2+(t-2)\Big(\sum_i s_i\Big)^2,
 \qquad a_i(t)=t-1+1/m_i.\tag{2}
\]
For \(1\le t\le2\), equation (1) is strictly negative for each nonzero \(x\). For \(t>2\), the diagonal entries \(a_i(t)\) are positive. Weighted Cauchy--Schwarz implies
\[
 \Big(\sum_i s_i\Big)^2\le
 \Big(\sum_i a_i(t)s_i^2\Big)\Big(\sum_i a_i(t)^{-1}\Big),\tag{3}
\]
with equality exactly for \(s_i\) proportional to \(a_i(t)^{-1}\). Thus (2) is nonpositive for all \(s\) precisely when \(F_{\mathbf m}(t)\le1\). If \(F_{\mathbf m}(t)>1\), taking \(s_i=a_i(t)^{-1}\) and uniform coefficients within each blade makes \(Q_p>0\), proving necessity rather than merely a sufficient bound.

For each positive \(m\),
\[
 \frac{d}{dt}\frac{t-2}{t-1+1/m}
 =\frac{1+1/m}{(t-1+1/m)^2}>0.
\]
The function \(F_{\mathbf m}\) therefore increases strictly from \(0\) at \(t=2\) to \(r>1\) as \(t\to\infty\); there is exactly one crossing of \(1\). Below it, (1)--(3) give strict negative type. At equality, the only zero-sum equality vectors are scalar multiples of
\[
 x_{i,a}=\frac{1}{m_i(t_*-1+1/m_i)},\qquad
 x_0=-\sum_{i=1}^r\frac1{t_*-1+1/m_i}.\tag{4}
\]
Hence the kernel on the zero-sum space has dimension one. The basepoint Euclidean Gram matrix for \(d^{p/2}\), with the hub as basepoint, is \(\tfrac12(2-d(i,j)^p)\) on nonhub vertices; it equals minus one-half of the zero-sum distance form in the basis \(e_{i,a}-e_0\). Its rank is therefore \(M\) for \(p<\wp(G)\) and \(M-1\) at the endpoint. This establishes both minimal Euclidean affine dimensions.

For fixed \(t>2\), set \(g_t(x)=x/((t-1)x+1)\), which has
\[
 g_t''(x)=-\frac{2(t-1)}{((t-1)x+1)^3}<0\quad(x>0).
\]
Moving one unit from a larger blade to a smaller blade (when they differ by at least two) strictly increases \(\sum_i g_t(m_i)\). Repeating establishes that the balanced partition uniquely maximizes \(F_{\mathbf m}(t)\) up to permutation. Moving one unit from a smaller blade of size at least two to a larger blade strictly decreases the sum, leading uniquely to \((M-r+1,1,\ldots,1)\). Since every \(F_{\mathbf m}\) increases strictly with \(t\), these pointwise comparisons reverse for their unique roots, giving the announced minimizer, maximizer, and equality cases. If every \(m_i=m\), the equation \(r(t-2)/(t-1+1/m)=1\) gives the displayed closed formula.

## Verification
The included standalone `verify.py` constructs the zero-sum distance-power matrix exactly over rational parameters and independently verifies identity (1), sharp witnesses above the threshold, and rational principal-minor signs at/below the threshold. It also enumerates ordered integer blade compositions for small total sizes and checks both unique partition extremizers. Running `python verify.py` yielded `PASS: 2565 exact metric-signature or partition-majorization checks`. Those finite checks are supplementary; equations (1)--(4), monotonicity, and strict concavity prove the result for all permitted sizes and real exponents.

## Relationship to prior work
Doust and Weston, *Enhanced negative type for finite metric trees* (arXiv:0705.0411), Theorem 5.6, give the sharp exponent for stars, reproduced here when all blades have size one. Li and Weston, *Strict p-negative type of a metric space* (arXiv:0901.0695), give general strictness and endpoint principles without the unequal-clique-bouquet root or the fixed-cardinality majorization theorem. Abiad and collaborators, *Extending a conjecture of Graham and Lovász on the distance characteristic polynomial* (arXiv:2206.07561), study ordinary distance-matrix spectra and characteristic-polynomial coefficients for windmill/block graphs, including unequal clique sizes; their specified spectral polynomial concerns the ordinary distance matrix, not the continuum of power-distance negative-type forms or optimized partitions. These papers provide genuine foundational and object-level overlap, but the inspected claims do not state the present complete exponent and majorization classification.

## Limitations
The graph has exactly one common hub; the theorem does not classify arbitrary block graphs, edge-weighted graphs, or multiple cut vertices. The exponent is characterized by a strictly monotone scalar root, not generally a formula in radicals for unequal blades. The Hilbert representation concerns the snowflaked distance \(d^{p/2}\), not an isometric Euclidean realization of the original path metric for all parameters. The literature review is bounded and cannot exclude an earlier equivalent treatment under a different terminology.

## References
1. I. Doust and A. Weston, *Enhanced negative type for finite metric trees*, arXiv:0705.0411 (first public version 2007-05-03), especially Theorem 5.6. https://arxiv.org/abs/0705.0411
2. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695 (first public version 2009-01-06). https://arxiv.org/abs/0901.0695
3. A. Abiad, B. Brimkov, S. Hayat, A. P. Khramova and J. H. Koolen, *Extending a conjecture of Graham and Lovász on the distance characteristic polynomial*, arXiv:2206.07561 (first public version 2022-06-15), Section 4 and Remark 4.4. https://arxiv.org/abs/2206.07561
