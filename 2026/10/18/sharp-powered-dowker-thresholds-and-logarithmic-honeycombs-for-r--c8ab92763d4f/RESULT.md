# Sharp powered-Dowker thresholds and logarithmic honeycombs for regular polygonal norms

## Finding
Let \(k\ge 2\) be an integer, and let \(P_k\) denote the regular Euclidean \(2k\)-gon circumscribed about the unit disk. For every integer \(n\ge3\), define \(A_k(n)\) to be the least area of a convex \(n\)-gon containing \(P_k\), allowing redundant vertices when \(n\ge2k\). For \(\alpha>0\), say that \(P_k\) is *weakly \(\alpha\)-Dowker* if, for all integers \(3\le m<6<n\),
\[
\frac{n-6}{n-m}A_k(m)^\alpha+\frac{6-m}{n-m}A_k(n)^\alpha\ge A_k(6)^\alpha.
\]
At \(\alpha=0\), replace each power by its logarithm (the weak log-Dowker property).

**Theorem.** The exact set of exponents \(\alpha\in[0,\infty)\) for which this property holds is
\[
\begin{cases}
[0,\infty),&k\notin\{4,5,7\},\\
[1,\infty),&k\in\{4,5,7\}.
\end{cases}
\]
In particular, for every regular \(2k\)-gonal normed plane with \(k\notin\{4,5,7\}\), a normal convex tiling by unit-area cells has lower average logarithmic norm-perimeter no smaller than that of a tiling by translates of a suitable centrally symmetric hexagon. This is a logarithmic, rather than merely ordinary-perimeter, honeycomb inequality. No assertion that hexagonal tilings fail to optimize in the three exceptional norms is made.

## Assumptions and scope
Area means two-dimensional Lebesgue area. The defining expression is unchanged under positive homotheties of \(P_k\), since the coefficients sum to one. The normed-plane corollary uses the lower average logarithmic norm-perimeter and normal convex unit-area tilings in the sense of Lángi and Wang (2024); the corresponding isoperimetrix of a regular even-gonal unit ball is itself a scaled and rotated regular even-gon. We use the proven formula of Lángi and Wang for least-area circumscribed polygons, the classical Dowker convexity theorem, and their sufficient condition connecting weak log-Dowker to the normed-plane log-honeycomb property.

## Proof
**1. Exact area formula.** Write \(N=2k\). For \(4\le n<N\), let \(N=nq+r\), where \(0\le r<n\). The minimum circumscribed area is [Lángi–Wang, Lemma 3.7]
\[
A_k(n)=(n-r)\tan\!\left(\frac{\pi q}{N}\right)+r\tan\!\left(\frac{\pi(q+1)}{N}\right).
\]
For \(n=3\), the same reference gives
\[
A_k(3)=\begin{cases}
3\tan(\pi/3),&r=0,\\
\frac{2}{\cos^2(\pi/N)}\left((3-r)\sin(q\pi/k)+r\sin((q+1)\pi/k)\right),&r=1,2,
\end{cases}
\]
where now \(N=3q+r\). For \(n\ge N\), \(A_k(n)=N\tan(\pi/N)\). These are the only nontrivial numerical premises in the finite certificate below.

**2. The three sharp obstructions.** Direct substitution gives the exact identity
\[
A_k(5)+A_k(7)=2A_k(6),\qquad A_k(5)>A_k(6)>A_k(7)
\]
for \(k=4,5,7\). Indeed, write \(t_j=\tan(j\pi/(2k))\). For \(k=4\), the triple \((A_k(5),A_k(6),A_k(7))\) is \((2t_1+3t_2,4t_1+2t_2,6t_1+t_2)\); for \(k=5\) it is \((5t_2,2t_1+4t_2,4t_1+3t_2)\); and for \(k=7\) it is \((t_2+4t_3,4t_2+2t_3,7t_2)\). The strict inequalities follow from these expressions (or from the rigorous intervals in the included checker). Strict concavity of \(x\mapsto x^\alpha\) when \(0<\alpha<1\), and of \(\log x\), defeats the weak inequality at \((m,n)=(5,7)\). For \(\alpha\ge1\), Dowker's theorem that \(A_k(n)\) is decreasing and convex, followed by composition with the increasing convex power, proves the weak property. Hence the second line of the classification is exact.

**3. Reduction for the other orders.** It suffices to prove the weak logarithmic property: weighted arithmetic–geometric mean, applied to the positive quantities \(A_k(m)^\alpha\) and \(A_k(n)^\alpha\), then proves the weak property for every \(\alpha>0\). The logarithmic inequality is equivalent to
\[
A_k(m)^{n-6}A_k(n)^{6-m}\ge A_k(6)^{n-m}.
\]
For \(k=2,3\), the body already has at most six sides, so \(A_k(n)=A_k(6)\) for \(n\ge6\) and monotonicity gives the inequality. For \(4\le k\le15\) excluding \(4,5,7\), it is enough to check \(n=7,\ldots,2k\), since \(A_k(n)\) is constant for larger \(n\) and the right secant \((\log A_k(6)-\log A_k(n))/(n-6)\) then decreases. The included `check.py` verifies **all 426** of these comparisons strictly using rational outward intervals, not floating-point comparisons. Its exact arithmetic uses Machin's identity for \(\pi\), explicit Taylor remainders for sine and cosine, and integer powers of outward-rounded rational endpoints; it also certifies the small numerical inequalities used in Step 4. This is finite verification of a finite reduction, not extrapolation from enumeration.

**4. Every order \(k\ge16\).** Put \(d(x)=x\tan(\pi/x)\) for \(x\ge3\). The function \(g(x)=\log d(x)\) is strictly convex. In fact, with \(y=2\pi/x\in(0,2\pi/3]\),
\[
x^2g''(x)=\frac{-\sin^2y+2y\sin y-y^2\cos y}{\sin^2y}>0,
\]
since the numerator vanishes at zero and has derivative \(\sin y\,[2(1-\cos y)+y^2]>0\) for \(0<y\le2\pi/3\). Consequently the Jensen gap at the integer mean \(6\), over all \(3\le m<6<n\), is smallest when \((m,n)=(5,7)\). The exact rational-interval checker establishes
\[
\frac{d(5)d(7)}{d(6)^2}>\frac{51}{50}>
\sec^4\!\left(\frac{\pi}{32}\right).
\]
The polygon \(P_k\) contains the unit disk and lies inside the concentric disk of radius \(R_k=\sec(\pi/(2k))\), so monotonicity and scaling of minimum enclosing area yield, for every \(n\),
\[
d(n)\le A_k(n)\le R_k^2d(n).
\]
For \(k\ge16\), \(R_k^4\le\sec^4(\pi/32)<d(5)d(7)/d(6)^2\). Therefore, for all \(m,n\) in the weak condition, the weighted mean of \(\log A_k(m)\) and \(\log A_k(n)\) exceeds \(\log A_k(6)\): its gap is at least
\[
\frac12\log\!\left(\frac{d(5)d(7)}{d(6)^2}\right)-\log R_k^2>0.
\]
This handles infinitely many orders analytically and completes the exact exponent classification.

**5. Tiling consequence.** A regular even-gonal unit ball has a regular even-gonal isoperimetrix up to a similarity; the weak log-Dowker property is scale invariant. Applying Lángi–Wang's implication from weak log-Dowker of the isoperimetrix to log-honeycomb of the norm proves the tiling assertion for every nonexceptional order.

## Verification
Run `python check.py` using Python's standard library only. The script proves the 426 strict finite inequalities for \(k\le15\) by exact rational enclosures; checks the exceptional order identities at the level of interval overlap and strict spacing (their equality is established symbolically in Step 2); and proves the rational cutoff sandwich used in Step 4. Taylor remainder bounds and all outward roundings are encoded in the checker. Its output includes the least relative integer-power margin and the number of comparisons. Replaying the script from this package is sufficient; no external data files or numerical libraries are needed. The analytic argument for all \(k\ge16\) and the external implications are essential and are not replaced by the finite check.

## Relationship to prior work
Lángi and Wang (first publicly available June 15, 2024) introduced the weak powered-Dowker mechanism for normed-plane honeycombs, proved its regular-polygon area formula, and classified the **weak \(1/2\)-Dowker** property: it holds exactly outside \(k=4,5,7\). Their work also establishes log-honeycomb for the Euclidean norm and sufficiently few-sided unit balls. The theorem here addresses a logically stronger endpoint—the weak **log**-Dowker property—for all regular even-gons, proves an exact no-intermediate-exponents dichotomy, and transfers the stronger endpoint to the logarithmic perimeter objective for nonexceptional polygonal norms. The previously known \(1/2\)-power conclusion alone does not entail logarithmic convexity.

## Limitations
The three exceptional cases are failures of the **sufficient weak-Dowker condition**, not counterexamples to the optimality of hexagonal tilings for any powered perimeter objective. The result concerns regular centrally symmetric polygonal norms and normal convex unit-area tilings; it does not classify arbitrary norms or irregular polygons. The literature comparison cannot exclude an unindexed equivalent derivation. Independent mathematical validation has not been performed.

## References
1. Z. Lángi and S. Wang, *The Honeycomb Conjecture in normed planes and an alpha-convex variant of a theorem of Dowker*, arXiv:2406.10622 (first posted 2024-06-15), especially definitions 1.7–1.8, Theorem 1.9, and Lemma 3.7; subsequent journal version, *International Mathematics Research Notices*, 2026, article rnaf372, DOI: 10.1093/imrn/rnaf372.
2. C. H. Dowker, *On minimum circumscribed polygons*, *Bulletin of the American Mathematical Society* **50** (1944), 120–122.
3. A. Aggarwal, J. S. Chang and C. K. Yap, *Minimum area circumscribing polygons*, *The Visual Computer* **1** (1985), 112–117.
