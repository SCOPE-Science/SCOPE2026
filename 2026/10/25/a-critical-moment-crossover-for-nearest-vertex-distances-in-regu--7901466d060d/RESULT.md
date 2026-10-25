# A critical-moment crossover for nearest-vertex distances in regular polygons

## Finding
Let \(P_n\subset\mathbb R^2\) be the regular \(n\)-gon with circumradius \(1\), let \(X_n\) be uniformly distributed in its interior, and let \(D_n\) be the Euclidean distance from \(X_n\) to its closest polygon vertex. For every integer \(n\ge3\) and real \(p>0\), put \(a=\pi/n\) and \(M_n(p)=\mathbb E[D_n^p]\). Then
\[
\boxed{M_n(p)=\frac{2}{(p+1)(p+2)}\left[1+\frac{p\sin^{p+1}a}{\cos a}\int_a^{\pi/2}\sin^{-p}t\,dt\right].}
\]
Define the excess \(\Delta_n(p)=M_n(p)-2/((p+1)(p+2))\). It is strictly positive for finite \(n\). The following three asymptotic regimes hold for each *fixed* positive exponent:
\[
\begin{aligned}
0<p<1:\quad&\lim_{n\to\infty}\frac{\Delta_n(p)}{(\pi/n)^{p+1}}=\frac{p\sqrt\pi\,\Gamma((1-p)/2)}{(p+1)(p+2)\Gamma(1-p/2)},\\[4pt]
p=1:\quad&\lim_{n\to\infty}\frac{\Delta_n(1)}{(\pi/n)^2\log(n/\pi)}=\frac13,\\[4pt]
p>1:\quad&\lim_{n\to\infty}\frac{\Delta_n(p)}{(\pi/n)^2}=\frac{2p}{(p+2)(p^2-1)}.
\end{aligned}
\]
There is a nontrivial *critical window*. With \(L_n=\log(n/\pi)\), set \(p_n=1+\lambda/L_n\) for each fixed \(\lambda\in\mathbb R\) and sufficiently large \(n\). Then
\[
\boxed{\lim_{n\to\infty}\frac{\Delta_n(p_n)}{(\pi/n)^2L_n}=\frac{1-e^{-\lambda}}{3\lambda},}
\]
where the value at \(\lambda=0\) is defined continuously as \(1/3\). The convergence is uniform for \(\lambda\) in any fixed compact interval. These varying-exponent asymptotics, together with the three fixed-exponent regimes, form the principal result.

## Assumptions and scope
All distances are ordinary Euclidean distances in the plane. The point is *area-uniform* on the filled polygon, and the sites are exactly the \(n\) polygon vertices; distance to the boundary, to the polygon center, and distances between two independent random points are different observables. The circumradius normalization is \(1\); radius \(R\) multiplies the \(p\)-th moment by \(R^p\). There is no restriction to even \(n\). The exponent \(p\) is positive, and statements with fixed \(p\) are not asserted uniformly as \(p\to0\) or \(p\to\infty\).

## Proof
**1. Exact nearest-site cell.** Write \(O=(0,0)\), \(V=(1,0)\), and \(a=\pi/n\). Since all sites lie on the unit circle, minimizing \(\|x-v\|^2=\|x\|^2+1-2x\cdot v\) is equivalent to maximizing the angular cosine. Up to measure-zero ties, the Voronoi cell of \(V\) inside \(P_n\) occupies polar angles \([-a,a]\). Its upper half is the right triangle with corners \(V\), \(O\), and
\[
M=(\cos^2a,\sin a\cos a),
\]
the midpoint of the side joining \(V\) to \((\cos2a,\sin2a)\). The lower half is its reflection. All \(2n\) such triangles have equal area, so the distribution of \(D_n\) equals the distribution of distance to \(V\) from an area-uniform point in triangle \(VOM\).

**2. Polar integration from the vertex.** Measure a polar angle \(\phi\) at \(V\) from the inward ray \(VO\) toward \(VM\). It ranges over \([0,\pi/2-a]\); the endpoint of the ray on \(OM\) is at radius
\[
\rho_{\max}(\phi)=\frac{\sin a}{\sin(a+\phi)}.
\]
The triangle has area \(\sin a\cos a/2\). Radial integration of \(\rho^p\) against area measure \(\rho\,d\rho\,d\phi\) yields
\[
M_n(p)=\frac{2\sin^{p+1}a}{(p+2)\cos a}\int_a^{\pi/2}\sin^{-p-2}t\,dt.
\]
For \(p>0\), differentiating \(\cos t/\sin^{p+1}t\) gives
\[
\frac{d}{dt}\frac{\cos t}{\sin^{p+1}t}=-(p+1)\sin^{-p-2}t+p\sin^{-p}t.
\]
Integrating this identity gives the boxed exact formula. The integral term is positive because \(0<a\le\pi/3\).

**3. Three fixed-exponent regimes.** Let \(J_p(a)=\int_a^{\pi/2}\sin^{-p}t\,dt\). For \(0<p<1\), dominated convergence and the beta integral show
\[
J_p(a)\longrightarrow \int_0^{\pi/2}\sin^{-p}t\,dt=\frac{\sqrt\pi\,\Gamma((1-p)/2)}{2\Gamma(1-p/2)}.
\]
For \(p=1\), direct integration gives \(J_1(a)=\log\cot(a/2)\). For \(p>1\), \(\sin t/t\to1\) at the origin implies \(J_p(a)\sim a^{1-p}/(p-1)\). Substitution into the exact formula, with \(\sin a\sim a\) and \(\cos a\to1\), proves the stated limits. In particular,
\[
\Delta_n(1)=\frac{\sin^2a}{3\cos a}\log\cot(a/2)
=\frac{a^2}{3}\log\frac2a+O\!\left(a^4\log\frac1a\right).
\]
The exactly computable second moment provides a separate check:
\[
M_n(2)=\frac16+\frac{\sin^2(\pi/n)}3.
\]

**4. Uniform critical window.** Let \(L=\log(1/a)\), \(p=1+\lambda/L\), and fix \(|\lambda|\le B\). Uniformly for these exponents, the difference \(\sin^{-p}t-t^{-p}\) is integrable on \((0,\pi/2]\), with its integral bounded independently of \(a\) and \(\lambda\): near zero it is \(O(t^{2-p})\). Consequently
\[
J_p(a)=\int_a^{\pi/2}t^{-p}\,dt+O_B(1)
=L\frac{e^\lambda-1}{\lambda}+O_B(1),
\]
where the quotient at zero means \(1\). Also \(\sin^{p+1}a/\cos a=a^2e^{-\lambda}(1+O_B(a^2))\) and \(2p/((p+1)(p+2))=1/3+O_B(1/L)\). Therefore
\[
\frac{\Delta_n(p)}{a^2L}=\frac{1-e^{-\lambda}}{3\lambda}+O_B(1/L).
\]
This proves the compact-uniform crossover, including its continuous value at zero. It uses no interchange of nonuniform fixed-\(p\) limits.

## Verification
The accompanying standalone script `check_nearest_polygon.py` uses only the Python standard library. Run it with `python3 check_nearest_polygon.py`. It independently samples \(210{,}000\) area-uniform triangle points, computes the minimum of distances to *all* polygon vertices, compares four moments against numerical quadrature of the exact formula, checks both low-order identities, and tests all three asymptotic regimes and the finite-size critical crossover. Checks at finitely many orders and exponents are corroborative; the proof above supplies the infinite quantifiers.

## Relationship to prior work
Bäsel's 2012 preprint (later published in 2014) concerns chords and the distance between **two independent random points** in regular polygons, not distance to the nearest polygon vertex. Khalid–Durrani (2012/2013) studies distances to an **arbitrary fixed reference point**, again a distinct statistic. Li–Qiu (2016) gives general \(p\)-th moments of distance from a fixed triangle vertex to a uniform triangle point and explicitly motivates Voronoi decompositions. Consequently the finite-\(n\) integration formula here is **not claimed as a fundamentally new moment-integration method**: it can also be obtained by specializing that broad framework to the Voronoi triangles. The specific three-regime moment *asymptotics* and the \(p=1\) moving-exponent crossover with its compact-uniform scaling function are not stated in the inspected primary works and are the originality claim. Pan (2025) studies one probability threshold for points avoiding vertex disks; it does not compute the all-order moment crossover. A complete priority determination beyond the inspected literature is not asserted.

## Limitations
This result does not optimize the placement of sites, treat independently sampled sites, or establish any universal law for irregular polygons. The finite-\(n\) moment identity can be derived from existing general triangle-moment theory; originality is specifically claimed for the asymptotic transition and its uniform critical window. An unlocated equivalent asymptotic analysis remains a historical-priority risk. The estimates are for fixed \(p>0\) or \(p=1+\lambda/\log(n/\pi)\) with bounded \(\lambda\), not arbitrary joint scaling of \(p\) and \(n\).

## References
1. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first posted 2012-04-12; Acta Math. Univ. Comenianae 83 (2014), 1–18. https://arxiv.org/abs/1204.2707
2. Z. Khalid and S. Durrani, *Distance Distributions in Regular Polygons*, arXiv:1207.5857, first posted 2012-07-25; IEEE Trans. Veh. Technol. 62 (2013), 2363–2368. https://arxiv.org/abs/1207.5857
3. H. Li and X. Qiu, *Moments of Distance from a Vertex to a Uniformly Distributed Random Point within Arbitrary Triangles*, Math. Problems in Engineering (2016), Article 8371750. https://doi.org/10.1155/2016/8371750
4. W. Pan, *A Closed-Form Probability Formula for Random Points Avoiding Vertex Neighborhoods in Regular Polygons*, preprint posted 2025-05-16. https://www.preprints.org/manuscript/202505.1270
