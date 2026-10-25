# Exact disappearing central-hole law for regular-polygon vertex sums

## Finding
Let \(n\ge3\) be odd, let \(P_n\) be the regular Euclidean \(n\)-gon of circumradius one centered at the origin, and let \(V_n\) denote its vertex set. Write \(h_n=\cos(\pi/n)\), \(1\le\lambda\le h_n^{-1}\), and
\[
U_{n,\lambda}=V_n+\lambda P_n,\qquad Q_{n,\lambda}=(1+\lambda)P_n.
\]
The **entire uncovered set**, not just its area, is exactly a reversed regular polygon:
\[
\boxed{Q_{n,\lambda}\setminus U_{n,\lambda}
=\operatorname{int}\!\left[(h_n^{-1}-\lambda)(-P_n)\right].}
\]
Here the right-hand side is empty at the endpoint \(\lambda=h_n^{-1}\), and \(\operatorname{int}\) means ordinary Euclidean interior. Consequently the exact missing area and Euclidean Hausdorff distance are
\[
\boxed{\Delta_n(\lambda)=\frac n2\sin\left(\frac{2\pi}{n}\right)(h_n^{-1}-\lambda)^2
=n\tan\left(\frac\pi n\right)(1-\lambda h_n)^2,}
\]
\[
\boxed{d_H(U_{n,\lambda},Q_{n,\lambda})=1-\lambda h_n.}
\]
Thus the exact area-to-squared-Hausdorff ratio is \(n\tan(\pi/n)\). For every \(\lambda\ge h_n^{-1}\), the uncovered set is empty. For \(\lambda=1\) and odd \(n\to\infty\),
\[
\boxed{\Delta_n(1)=\frac{\pi^5}{4n^4}+O(n^{-6}).}
\]
For even \(n\), the known vertex-generated identity gives \(V_n+\lambda P_n=(1+\lambda)P_n\) for all \(\lambda\ge1\); this even-order threshold and the odd-order threshold themselves are background, not a separate novelty claim.

## Assumptions and scope
All sums are Minkowski sums in the Euclidean plane. The polygon has unit circumradius; scaling it by a positive factor scales the missing area quadratically and the Hausdorff distance linearly. The exact set and area identities are asserted for every odd integer \(n\ge3\) and every real \(\lambda\in[1,\sec(\pi/n)]\); the convexification assertion extends to larger \(\lambda\). The regime \(0\le\lambda<1\), which can feature disconnected edge gaps, is not classified here. The Euclidean Hausdorff metric is used, not an arbitrary Minkowski gauge.

## Proof
Write \(\theta=\pi/n\), \(h=\cos\theta\), \(\varepsilon=1-\lambda h\), and \(v_j=(\cos(2\pi j/n),\sin(2\pi j/n))\). First suppose \(1\le\lambda<h^{-1}\), so \(\varepsilon>0\). Since \(n\) is odd, the edge of \(P_n\) opposite \(v_0=(1,0)\) is the segment from \((-h,-\sin\theta)\) to \((-h,\sin\theta)\). Hence the translate \(S_j=v_j+\lambda P_n\) satisfies the necessary support inequality
\[
\langle x,v_j\rangle\ge1-\lambda h=\varepsilon\quad(x\in S_j).
\]
It follows that every point covered by any translate satisfies \(\max_j\langle x,v_j\rangle\ge\varepsilon\).

We prove the converse **inside the outer polygon** by an exact sector argument. Partition \(Q=(1+\lambda)P_n\) into the closed sectors \(C_j\) in which \(\langle x,v_j\rangle=\max_i\langle x,v_i\rangle\). Rotate to \(j=0\). In this sector, \(x=(x_1,x_2)\) obeys \(|x_2|\le x_1\tan\theta\), and the quadrilateral \(Q\cap C_0\) has vertices
\[
0,\quad(1+\lambda)v_0,\quad(1+\lambda)m_+,\quad(1+\lambda)m_-,
\qquad m_\pm=(v_0+v_{\pm1})/2.
\]
Because \(h\ge1/2\) and \(\lambda\ge1\),
\[
0<\varepsilon\le(1+\lambda)h^2,
\]
so the subregion \(B=Q\cap C_0\cap\{x_1\ge\varepsilon\}\) is the convex hull of the three nonzero outer quadrilateral vertices and the two points \(z_\pm=(\varepsilon,\pm\varepsilon\tan\theta)\). All five belong to \(S_0=v_0+\lambda P_n\): the apex \((1+\lambda)v_0\) is immediate; and
\[
(1+\lambda)m_\pm-v_0
=\tfrac{\lambda-1}{2}v_0+\tfrac{\lambda+1}{2}v_{\pm1}
\in\lambda P_n
\]
since the coefficients are nonnegative and sum to \(\lambda\). Finally
\[
z_\pm-v_0=(-\lambda h,\ \pm\varepsilon\tan\theta)
\]
belongs to the opposite edge of \(\lambda P_n\), because \(\varepsilon\tan\theta\le\lambda\sin\theta\) follows from \(\varepsilon\le\lambda h\), itself equivalent to \(1\le2\lambda h\). Convexity yields \(B\subset S_0\). Thus, on every sector, points of \(Q\) satisfying \(\max_j\langle x,v_j\rangle\ge\varepsilon\) are covered, and no others are.

Therefore
\[
Q\setminus U=Q\cap\{x:\langle x,v_j\rangle<\varepsilon\ \text{for every }j\}.
\]
The closed polygon \(H=\bigcap_j\{x:\langle x,v_j\rangle\le\varepsilon\}\) is a regular \(n\)-gon of inradius \(\varepsilon\), circumradius \(\varepsilon/h\), and vertex angles \(\theta+2\pi j/n\). For odd \(n\), these angles are precisely the vertex angles of \(-P_n\). Hence \(H=(\varepsilon/h)(-P_n)=(h^{-1}-\lambda)(-P_n)\). Moreover, \(H\subset Q\): in sector \(C_0\), its farthest point is one of \(z_\pm\), and \(\varepsilon\le(1+\lambda)h^2\) puts both on or inside the outer sector rays; rotation treats all sectors. The boundary \(\partial H\) is covered because equality in a support inequality and the preceding sector argument imply membership in a translate. This proves \(Q\setminus U=\operatorname{int}H\).

Since \(\operatorname{Area}(P_n)=\frac n2\sin(2\theta)\), area scaling gives the stated missing-area formula. The distance from \(0\) to the covered complement is exactly \(\varepsilon\), the inradius of \(H\). For every \(x\in H\), distance to \(U\) equals distance to \(\partial H\), which is
\[
\min_j(\varepsilon-\langle x,v_j\rangle)
=\varepsilon-\max_j\langle x,v_j\rangle\le\varepsilon.
\]
(The maximum is nonnegative because the vertex vectors sum to zero.) Therefore \(d_H(U,Q)=\varepsilon\).

At \(\lambda=h^{-1}\), the same five-vertex argument, with \(\varepsilon=0\), shows all sectors of \(Q\) are covered, including the origin. For larger \(\lambda\), Minkowski addition of \((\lambda-h^{-1})P_n\) to the resulting equality gives \(U=Q\). The asymptotic follows from \(1-\cos\theta=\theta^2/2+O(\theta^4)\) and \(n\tan\theta=\pi+O(n^{-2})\).

## Verification
The proof is exact and applies to the full infinite parameter family. The standalone \(\texttt{verify.py}\) script constructs each translated polygon and its geometric union independently using robust planar polygon operations, then compares the predicted removed regular polygon and area at 49 parameter combinations covering odd orders \(3\) through \(19\). The maximum observed symmetric-difference or area discrepancy was below \(8\times10^{-15}\) in unit-circumradius coordinates. These finite checks test the construction but do not replace the analytic proof.

## Relationship to prior work
Artstein-Avidan, Falah and Slomka introduced the \(\lambda\)-vertex-generated parameter and characterized vertex-generated polytopes in the setting \(P+V(P)=2P\). The sharp regular-polygon threshold (one in even order and \(\sec(\pi/n)\) in odd order) has also been established and is not asserted here as a new theorem. What is resolved is the **entire shape of the uncovered complement for every intermediate scaling**, along with its exact area and Euclidean Hausdorff coupling. Van Hintum's 2026 Hausdorff-convexification theorem addresses Minkowski averages of a compact set rather than this vertex-plus-polytope family. Meyer develops general finite-convexification criteria; the relevant planar criteria test finiteness of the threshold, not the intermediate uncovered geometry.

## Limitations
The uniform regularity and odd number of vertices are essential to the stated description of the hole. General polygons may have multiple hole components. No assertion is made about the regime \(\lambda<1\), about higher-dimensional polytopes, or about priority against unindexed geometric covering calculations. Independent mathematical review has not been performed.

## References
1. Peter van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition*, arXiv:2606.10815v1, first public 2026-06-09. https://arxiv.org/abs/2606.10815
2. Shiri Artstein-Avidan, Tomer Falah and Boaz A. Slomka, *Vertex generated polytopes*, arXiv:2407.20604v1, 2024-07-30. https://arxiv.org/html/2407.20604v1
3. Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1, 2026-10-19. https://arxiv.org/html/2610.26744v1
4. Matthieu Fradelizi, Mokshay Madiman, Arnaud Marsiglietti and Artem Zvavitch, *The convexification effect of Minkowski summation*, EMS Surveys in Mathematical Sciences 5 (2018), 1–64, https://doi.org/10.4171/EMSS/26
