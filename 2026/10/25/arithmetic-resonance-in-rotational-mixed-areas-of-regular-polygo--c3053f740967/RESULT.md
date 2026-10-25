# Arithmetic resonance in rotational mixed areas of regular polygons

## Finding

For integers \(m,n\ge3\), let \(P_m(r)\) and \(P_n(s)\) be centered regular polygons of circumradii \(r,s>0\), with a vertex on the positive horizontal axis. Let \(R_\phi\) denote counterclockwise rotation through any real angle \(\phi\). Define
\[
g=\gcd(m,n),\quad L=\operatorname{lcm}(m,n)=mn/g,\quad M=m/g,\quad N=n/g,
\]
\[
\phi_0=\begin{cases}\pi/L,&M,N\text{ are both odd},\\0,&\text{otherwise},\end{cases}\quad
 d(\phi)=\min_{j\in\mathbb Z}|\phi-\phi_0-2\pi j/L|,
\]
\[
 A_0=\frac{m r^2}{2}\sin\frac{2\pi}{m}
 +\frac{n s^2}{2}\sin\frac{2\pi}{n},\qquad
 B=\frac{2grs\sin(\pi/m)\sin(\pi/n)}{\sin(\pi/L)}.
\]
The exact area of the Minkowski sum, for **every** \(\phi\in\mathbb R\), is
\[
\boxed{\operatorname{Area}(P_m(r)+R_\phi P_n(s))=A_0+B\cos d(\phi).}
\]
Here \(0\le d(\phi)\le\pi/L\). Consequently, every global maximum occurs precisely at \(\phi\equiv\phi_0\pmod{2\pi/L}\), and every global minimum occurs precisely at \(\phi\equiv\phi_0+\pi/L\pmod{2\pi/L}\). The exact range is
\[
[A_0+B\cos(\pi/L),\ A_0+B],
\]
and its width is \(B(1-\cos(\pi/L))>0\).

The Minkowski sum has exactly \(m+n-g\) sides **at every minimizing orientation** and exactly \(m+n\) sides at every other orientation. Its area response has a strict angular cusp at each minimum: if \(\phi_*\) minimizes the area, then as \(\eta\to0\),
\[
\operatorname{Area}(P_m(r)+R_{\phi_*+\eta}P_n(s))
 = A_0+B\cos(\pi/L)+B\sin(\pi/L)|\eta|+O(\eta^2).
\]
Thus the jump between one-sided slopes there is \(2B\sin(\pi/L)\), while the maxima are locally smooth.

For a uniformly random relative orientation, the complete area distribution is that of \(A_0+B\cos U\) with \(U\) uniform on \([0,\pi/L]\). In particular, its expectation is
\[
\mathbb E\operatorname{Area}(P_m(r)+R_\Phi P_n(s))
=A_0+\frac{2mnrs}{\pi}\sin\frac\pi m\sin\frac\pi n
=A_0+\frac{\operatorname{per}(P_m(r))\operatorname{per}(P_n(s))}{2\pi}.
\]
For fixed positive radii and both side counts tending to infinity, the angular range is asymptotic to \(\pi^3rs/L^2\). The \(\gcd\)-dependent value of \(L\), not simply the smaller side count, therefore determines the orientation sensitivity.

## Assumptions and scope

Both objects are ordinary planar filled convex polygons in the Euclidean metric. The two circumradii are strictly positive, and each first vertex lies at angular coordinate zero before the stated rotation. The Minkowski sum means the set of all pointwise sums. The uniform-orientation statement uses Lebesgue-uniform angle on one full period of length \(2\pi/L\), equivalently uniform on a full turn. Assertions about polygon side counts refer to nonzero straight boundary edges, not merely to the number of pairwise vertex sums. No assumption of equal sizes, coprimality, or generic position is made.

## Proof

**1. Mixed-area reduction.** Let \(h_Q(u)=\max_{x\in Q}\langle x,u\rangle\) be the support function. The planar mixed-area formula for polygons gives
\[
\operatorname{Area}(P+Q)=\operatorname{Area}(P)+\operatorname{Area}(Q)
+\sum_{e\in E(P)}|e|h_Q(u_e),
\]
where \(u_e\) is the outward unit normal to edge \(e\). This follows, for example, by differentiating the area of \(P+tQ\) at \(t=0^+\) and using the quadratic Minkowski-area polynomial; the cross coefficient is symmetric in the summands. For \(P=P_m(r)\), each edge has length \(2r\sin(\pi/m)\), and its outward normal has angle \((2j+1)\pi/m\), for \(j=0,\ldots,m-1\). For \(Q=R_\phi P_n(s)\), the support function is the largest scalar product with one of the vertices of angular coordinates \(\phi+2\pi k/n\). Therefore the cross term is
\[
2rs\sin(\pi/m)\sum_{j=0}^{m-1}
\max_{0\le k<n}\cos\left(\frac{(2j+1)\pi}{m}-\phi-\frac{2\pi k}{n}\right).
\tag{1}
\]

**2. Arithmetic collapse to one cosine.** Write \(m=gM\), \(n=gN\), where \(\gcd(M,N)=1\), and put \(a=2\pi/L\). For a fixed \(j\), the maximizing vertex in (1) is a nearest angular vertex; thus the chosen principal angle, modulo \(2\pi/n=Ma\), is
\[
a\left(Nj+\frac N2-\frac\phi a\right).
\]
As \(j\) runs through \(0,\ldots,m-1\), the residue classes \(Nj\pmod M\) run through each class \(0,\ldots,M-1\) exactly \(g\) times. Hence the maximizing principal angles form, with multiplicity \(g\), one consecutive grid of \(M\) angles with separation \(a\), selected in the arc \([-Ma/2,Ma/2]\). This grid has a center displacement \(\varepsilon\in[-a/2,a/2]\), whose congruence class modulo \(a\) is
\[
\varepsilon\equiv\frac{(M+N-1)\pi}{L}-\phi\pmod a.
\]
Because \(M,N\) are coprime, \(M+N-1\) is odd exactly when both are odd. Thus \(|\varepsilon|=d(\phi)\). The finite geometric-series identity, valid at a grid-selection tie by continuity, gives
\[
\begin{aligned}
\sum_{j=0}^{m-1}\max_k\cos(\cdots)
&=g\sum_{q=0}^{M-1}\cos\left(\varepsilon+(q-\tfrac{M-1}{2})a\right)\\
&=g\frac{\sin(Ma/2)}{\sin(a/2)}\cos\varepsilon\\
&=g\frac{\sin(\pi/n)}{\sin(\pi/L)}\cos d(\phi).
\end{aligned}
\]
Substitute this identity into (1) and add the two elementary regular-polygon areas. This proves the exact profile, for every angle including ties.

**3. Extremizers, side counts, and cusps.** Since \(L\ge3\), cosine is strictly decreasing on \([0,\pi/L]\), giving all and only the stated extremizers. The side normals of the two polygons can coincide precisely when
\[
\phi\equiv\frac\pi L(N-M)\pmod{2\pi/L}.
\]
This congruence is exactly \(\phi\equiv\phi_0+\pi/L\pmod{2\pi/L}\). When it holds, the two cyclic normal-angle sets intersect in exactly \(g\) directions: the intersection of their cyclic subgroups has order \(\gcd(m,n)\). Otherwise they have no shared normal angles. The normal fan of a planar polygon sum is the common refinement of the summands' fans, so its nonzero side-normal set is exactly the union of the two normal sets. The counts are therefore \(m+n-g\) and \(m+n\). Near any minimum, the distance to the nearest maximizing-phase grid is \(d(\phi_*+\eta)=\pi/L-|\eta|\) for sufficiently small \(|\eta|\); the displayed cusp expansion follows from a Taylor expansion of cosine.

**4. Distribution and asymptotic.** A uniform angle over one period has distance \(d\) from the nearest maximizing phase uniformly distributed on \([0,\pi/L]\). The distribution and expectation follow by direct one-variable integration. The standard perimeter formula is \(\operatorname{per}(P_m(r))=2mr\sin(\pi/m)\). Finally, if \(m,n\to\infty\) with \(r,s\) fixed, then \(\sin x\sim x\), giving \(B\to2\pi rs\); also \(1-\cos(\pi/L)\sim\pi^2/(2L^2)\). Multiplication yields \(\pi^3rs/L^2\), as claimed.

## Verification

The accompanying `verify.py` constructs the convex hull of **all** pairwise vertex sums independently of the mixed-area proof, computes its shoelace area, and compares it with the closed formula. With Python's standard library, it passed 3,696 checks across polygon side counts \(3\) through \(19\), with radius perturbations, orientation perturbations, both extremal side-count families, and finite-sample angular expectation checks. Its largest absolute area discrepancy was \(2.14\times10^{-14}\) (rounded upward). This numerical regression only tests finite inputs; the preceding arithmetic argument establishes the theorem for all allowed parameters.

## Relationship to prior work

The normal-fan face decomposition is classical; the presentation by Deza and Pournin (2018) supplies an accessible geometric reference. Geigenfeind and de las Heras (2019, Section III.1) studied angle-dependent excluded areas for identical regular polygons, presented numerical curves for three to six sides, and compared analytic formulas for equilateral triangles and squares. Their same-species orientation extremum counts, and those small-polygon expressions, are pre-existing special cases; they do not give the arbitrary two-side-count formula, the \(\gcd/\operatorname{lcm}\) phase and side-count transition, or the full distribution derived here. Abbasi Moud (2026, Section IV.1 and Table 2) gives special fixed-orientation Minkowski-sum excluded areas for regular-polygon mixtures, including an exact same-species parity law; these are single-angle values of the continuous profile here, not a complete relative-angle response. The classical rotational-average mixed-area identity agrees with the displayed expectation and is not claimed as new. Earlier general results on minimum excluded volume of congruent convex shapes also cover the congruent special case of the minimum-orientation assertion, but not the mixed-order profile.

## Limitations

This concerns planar Euclidean regular polygons, not arbitrary equiangular polygons or higher-dimensional polytopes. It is not a result about packing density or random sequential adsorption coverage; those models motivate why mixed excluded areas matter. The known same-order extremum statements and small-order exact curves are not new. The primary sources examined establish close contextual results, but literature priority cannot be certified exhaustively; an algebraically equivalent formula may appear in earlier polygon collision or kinematic literature. No independent mathematical audit has been performed. The standard-library numerical tests do not replace the general proof.

## References

1. A. Deza and L. Pournin, *Diameter, decomposability, and Minkowski sums of polytopes* (2018), arXiv:1806.07643v1, especially Section 2 on normal fans and face decompositions, https://arxiv.org/abs/1806.07643.
2. T. Geigenfeind and D. de las Heras, *The excluded area of two-dimensional hard particles* (2019), arXiv:1902.05961v1, Section III.1, https://arxiv.org/abs/1902.05961.
3. A. Abbasi Moud, *Saturation Coverage in Binary Mixtures of Oriented Regular Polygons via Random Sequential Adsorption* (2026), arXiv:2606.21812v1, Section IV.1, https://arxiv.org/abs/2606.21812.
4. P. Pálffy-Muhoray, E. G. Virga, and X. Zheng, *The minimum excluded volume of convex shapes* (2014), Journal of Physics A 47, 415205, DOI:10.1088/1751-8113/47/41/415205. This reference addresses a broader identical-shape minimization statement, not the mixed-order angular formula.
