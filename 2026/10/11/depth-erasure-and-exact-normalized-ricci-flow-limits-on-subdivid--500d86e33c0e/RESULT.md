# Depth erasure and exact normalized Ricci-flow limits on subdivided spiders

## Finding

Let
\[
T=\operatorname{Sp}(\ell_1,\ldots,\ell_d)
\]
be a finite spider tree with center \(o\) of degree \(d\ge3\). Arm \(i\) is a path of \(\ell_i\ge1\) edges from \(o\) to a leaf. Put
\[
r=\#\{i:\ell_i\ge2\},
\]
and assume
\[
r\ge3.
\]

Run the normalized inverse-weight Lin--Lu--Yau Ricci flow of Bai--Hua from any positive initial edge metric of total weight \(1\). Then the normalized metric converges for every such initial condition.

Let \(C\) be the set of the \(d\) edges incident to the center. The limiting positive support is exactly
\[
E_*=C,
\]
and the common limiting curvature on \(C\) is
\[
c_*=\frac{2-r}{d}<0.
\]
Every edge of a subdivided arm lying in \(C\) has limiting weight
\[
p_L=\frac{d+r-2}{2d(r-1)},
\]
whereas every unsubdivided arm edge has limiting weight
\[
p_U=\frac{r-2}{2d(r-1)}.
\]
All remaining edges satisfy
\[
w_e(t)\longrightarrow0.
\]

Consequently the normalized limit forgets every subdivision depth beyond the binary information of whether an arm has length \(1\) or at least \(2\). In particular, changing any \(\ell_i\ge2\) to an arbitrarily larger value leaves both the positive limiting metric and its common curvature unchanged.

When all arms are subdivided, so \(r=d\), the limit is the uniform metric on the center star:
\[
p_L=\frac1d,
\qquad
c_*=\frac{2-d}{d}.
\]
When \(3\le r<d\), the surviving center edges of long arms are heavier than the unsubdivided leaf arms by the exact ratio
\[
\frac{p_L}{p_U}=\frac{d+r-2}{r-2}.
\]

## Assumptions and scope

The curvature convention is the inverse-weight metric-dependent Lin--Lu--Yau curvature used in arXiv:2609.04671. The result is about the normalized flow
\[
\dot w_e=-w_e\bigl(\kappa_e-K\bigr),
\qquad
K=\sum_f w_f\kappa_f,
\qquad
\sum_e w_e=1.
\]

The hypothesis \(r\ge3\) is essential for the argument because it makes the minimizing curvature level negative. No assertion is made here for spiders with at most two subdivided arms.

The theorem identifies the normalized limit only. It does not claim that the unnormalized edge weights converge to finite nonzero values, nor does it give a convergence rate.

## Proof

Bai--Hua associate to every edge set \(A\subseteq E(T)\) the quantity
\[
\beta(A)=\sum_{x:E(x)\subseteq A}(2-d_x),
\qquad
\lambda(A)=\frac{\beta(A)}{|A|},
\]
and define
\[
c_*=\min_{\varnothing\ne A\subseteq E(T)}\lambda(A).
\]
Their theorem gives a unique largest minimizing edge set \(E_*\), and their convergence criterion reduces normalized metric convergence to existence of a supported Einstein metric on \(E_*\).

For a spider, degree-two vertices contribute \(0\) to \(\beta(A)\). A leaf contributes \(1\) exactly when its terminal edge belongs to \(A\). The center contributes \(2-d\) exactly when all \(d\) center edges belong to \(A\). If \(L(A)\) denotes the number of terminal leaf edges contained in \(A\), then
\[
\beta(A)=L(A)+(2-d)\mathbf 1_{\{C\subseteq A\}}.
\]

The set \(C\) contains all \(d-r\) terminal edges coming from unsubdivided arms and no terminal edge from a subdivided arm. Hence
\[
\beta(C)=(d-r)+(2-d)=2-r,
\]
so
\[
\lambda(C)=\frac{2-r}{d}<0.
\]

If \(C\nsubseteq A\), then
\[
\beta(A)=L(A)\ge0,
\]
and therefore
\[
\lambda(A)\ge0>\lambda(C).
\]
If \(C\subsetneq A\), write
\[
k=|A|-d>0
\]
and
\[
\ell=L(A)-(d-r)\ge0.
\]
Then
\[
\lambda(A)=\frac{2-r+\ell}{d+k}.
\]
A direct comparison gives
\[
d(2-r+\ell)-(d+k)(2-r)
=
d\ell+k(r-2)>0.
\]
Thus
\[
\lambda(A)>\frac{2-r}{d}.
\]
Therefore \(C\) is the unique minimizer:
\[
E_*=C,
\qquad
c_*=\frac{2-r}{d}.
\]

For every nonempty proper \(A\subset C\), the center does not contribute, so
\[
\lambda(A)\ge0>c_*.
\]
The subgraph carried by \(C\) is a connected star. Bai--Hua's supported-Einstein criterion therefore gives a unique positive supported metric on \(C\) with curvature \(c_*\), and their convergence theorem implies that every positive normalized initial metric converges to it. In particular, every edge outside \(C\) has limiting normalized weight \(0\).

It remains to compute the unique supported metric. Denote the limiting weight of the \(i\)-th center edge by \(p_i\), and put
\[
D=\sum_{j=1}^d\frac1{p_j},
\qquad
q_i=\frac1{p_iD}.
\]
Then
\[
\sum_{i=1}^d q_i=1.
\]

For a center edge leading into a subdivided arm, the next edge has limiting weight \(0\). In the inverse-weight degree at that degree-two endpoint, the reciprocal of that vanishing edge diverges, so the endpoint contribution to the limiting curvature vanishes. The tree curvature formula therefore gives
\[
c_*=(2-d)q_i.
\]
Hence every subdivided arm has
\[
q_L=\frac{r-2}{d(d-2)}.
\]

For an unsubdivided arm, the far endpoint is a leaf. Its endpoint contribution to the curvature is exactly \(1\), so
\[
c_*=1+(2-d)q_i,
\]
and therefore
\[
q_U=\frac{d+r-2}{d(d-2)}.
\]

Because \(q_i=(p_iD)^{-1}\), the weights \(p_i\) are proportional to \(q_i^{-1}\). Normalizing their sum to \(1\) yields
\[
p_L=\frac{d+r-2}{2d(r-1)},
\qquad
p_U=\frac{r-2}{2d(r-1)}.
\]
Indeed,
\[
r p_L+(d-r)p_U=1.
\]
This proves the claimed limit and its independence from the actual values of the subdivision depths.

## Verification

The proof is analytic. The bundled checker independently verifies the minimizer formula by exhaustive subset enumeration for a representative collection of spiders, then checks the closed limiting weights and their curvature equations exactly with rational arithmetic.

The exhaustive finite computations are stress tests only. The general result follows from the displayed formula for \(\beta(A)\), the strict comparison with every other edge set, and the Bai--Hua supported-Einstein and convergence theorems.

## Relationship to prior work

Bai and Hua prove a general curvature-diffusion theorem for the inverse-weight normalized Ricci flow on finite trees. They characterize the limiting curvature by the minimum of \(\lambda(A)\), identify a unique largest minimizing support \(E_*\), and prove convergence when the corresponding supported Einstein set is nonempty. They explicitly leave general normalized metric convergence on arbitrary finite trees as an open problem. The present result solves their criterion completely on a natural infinite family of non-caterpillar trees and gives the exact limiting metric.

The earlier paper by Bai, Hua, Yong Lin, and Shuang Liu studies the same inverse-weight Ricci flow and proves detailed long-time statements, including a caterpillar characterization for flat supported limits. It does not give the negative-curvature spider limit above.

A recent spider-tree result for the curvature-distortion invariant studies a different Lin--Lu--Yau convention in which the transport distance is fixed by the combinatorial graph metric. Its canonical static weights vary geometrically with arm length. It therefore neither implies nor contains the present metric-dependent Ricci-flow limit; in fact, the present limit has the opposite structural feature that all depths beyond the first edge are erased.

## Limitations

The result covers spiders with at least three subdivided arms. It does not settle the cases \(r\le2\), arbitrary finite trees, convergence rates, or the asymptotic scale of the unnormalized metric.

The originality comparison includes the focal full text, the earlier inverse-weight tree-flow paper, targeted statement-level searches, and the closest published spider-tree curvature result. An equivalent specialization could still exist in very recent or unindexed work.

## References

1. S. Bai and B. Hua, *Curvature Diffusion of Inverse-weight Lin--Lu--Yau Ricci Flow on Finite Trees*, arXiv:2609.04671v3, first public 4 September 2026. Primary MSC 53C21.
2. S. Bai, B. Hua, Y. Lin, and S. Liu, *On the Ricci flow on Trees*, arXiv:2509.22140v3, first public 26 September 2025.
3. Q. Xia, *Curvature-Distortion Numbers of Graphs: Nonnegative Lin--Lu--Yau Curvature*, arXiv:2609.12125v2, first public 10 September 2026.
