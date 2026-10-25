# Critical transversality moments for crossings of regular-polygon diagonals

## Finding

Choose four distinct vertices uniformly from a regular \(n\)-gon, \(n\ge4\), and join the first and third, and the second and fourth, in cyclic order. The two diagonals cross in their interiors. Let \(\Theta_n\in(0,\pi/2]\) be their smaller, unoriented intersection angle and define the **transversality amplification** \(K_n=1/\sin\Theta_n\). All crossing pairs are counted with multiplicity, even when several pairs intersect at the same point.

For every integer \(2\le k\le\lfloor n/2\rfloor\), the **complete exact angle law** is
\[
\Pr\!\left(\Theta_n=\frac{k\pi}{n}\right)
=\frac{12(k-1)(n-k-1)}{(n-1)(n-2)(n-3)}
\begin{cases}
1,&2k<n,\\
\frac12,&2k=n.
\end{cases}
\]
No other angles occur. As \(n\to\infty\), \(\Theta_n\) converges in distribution to \(\Theta\) supported on \([0,\pi/2]\), with
\[
F_\Theta(t)=6(t/\pi)^2-4(t/\pi)^3,
\qquad 0\le t\le\pi/2,
\]
\[
f_\Theta(t)=\frac{12t(\pi-t)}{\pi^3},
\qquad 0<t<\pi/2.
\]
Consequently, \(K=1/\sin\Theta\) has a heavy tail
\[
\Pr(K>z)\sim\frac6{\pi^2z^2}\quad(z\to\infty).
\]

The **critical inverse-sine moment spectrum** is, for each fixed real \(q\ge0\),
\[
\mathbb E K_n^q\longrightarrow
\int_0^{\pi/2}\frac{12t(\pi-t)}{\pi^3\sin^q t}\,dt,
\qquad 0\le q<2,
\]
\[
\mathbb E K_n^2=\frac{12}{\pi^2}\log n+O(1),
\]
\[
\lim_{n\to\infty}\frac{\mathbb E K_n^q}{n^{q-2}}
=\frac{12}{\pi^q}\bigl(\zeta(q-1)-\zeta(q)\bigr),
\qquad q>2.
\]
Here \(\zeta\) is the Riemann zeta function in its convergent-series domain \(q>2\). The critical exponent \(2\) separates bounded moments from logarithmic and power-law divergence. The factor \(1/\sin\Theta_n\) is the reciprocal determinant of the two unit direction vectors, relevant to conditioning of intersecting-line geometry; it is not asserted to equal every matrix-norm condition number.

## Assumptions and scope

The vertices are the \(n\) points \(v_j=(\cos(2\pi j/n),\sin(2\pi j/n))\), indexed by integers \(0\le j<n\). Sample uniformly one of the \(\binom n4\) four-element vertex subsets, then draw the unique crossing pairing of its elements. Equivalently, sample uniformly one unordered crossing pair of diagonals, counting distinct pairs even if their intersection points coincide. There is no randomness in the polygon orientation. The continuum limit uses four independent arclength-uniform circle points connected by the alternate crossing pairing.

## Proof

**Angle identity.** Fix cyclically ordered indices \(A<B<C<D\) and positive integer cyclic gaps \(a=B-A\), \(b=C-B\), \(c=D-C\), and \(d=n-(D-A)\), so \(a+b+c+d=n\). For distinct circle points at arguments \(\alpha,\beta\), the unoriented direction of their chord is \((\alpha+\beta)/2+\pi/2\pmod\pi\). Hence the difference of the chord directions of \(AC\) and \(BD\) is \(\pi(a+c)/n\pmod\pi\). The acute angle is therefore \(\pi k/n\), where \(k=\min(a+c,b+d)\). Both opposite gap sums are at least \(2\), so the stated support is exact.

**Exact counting, including the even midpoint.** Mark one of the four cyclic vertices as the start. There are \(n\) possible marked starting vertices. For a fixed positive opposite-gap sum \(s=a+c\), the gap pairs \((a,c)\) and \((b,d)\) have respectively \(s-1\) and \(n-s-1\) choices. Thus there are \(n(s-1)(n-s-1)\) marked quadruples with this specified sum. If \(s=k<n/2\), every unmarked four-subset with acute angle \(k\pi/n\) has exactly **two** marked starts with sum \(k\) and two with sum \(n-k\). Its total count is therefore \(n(k-1)(n-k-1)/2\). If \(n\) is even and \(k=n/2\), all four starts have the same opposite-gap sum and the count is \(n(k-1)^2/4\). Dividing by \(\binom n4=n(n-1)(n-2)(n-3)/24\) gives the exact mass function, whose total is one because every sampled quartet has one acute angle.

**Continuum distribution and tail.** Write \(u=k/n\). For \(0<u<1/2\), the mass function gives \(n\Pr(\Theta_n=k\pi/n)\to12u(1-u)\). The exceptional midpoint atom for even \(n\) has vanishing mass. Riemann sums give the limit density \(12u(1-u)\) on \([0,1/2]\) for \(\Theta/\pi\). Integrating yields \(6u^2-4u^3\). Since \(K>z\) is equivalent to \(\Theta<\arcsin(1/z)\) for \(z>1\), the limiting CDF implies \(\Pr(K>z)=6/(\pi^2z^2)+O(z^{-3})\).

**Subcritical moments.** For \(2\le k\le n/2\) and \(n\) sufficiently large, the exact mass is at most \(Ck/n^2\), and \(\sin(\pi k/n)\ge2k/n\). For each \(0\le q<2\), the contribution of \(2\le k\le\delta n\) to \(\mathbb E K_n^q\) is bounded by \(C_q\delta^{2-q}\), uniformly as \(n\to\infty\). Away from zero the inverse-sine function is bounded and Riemann sums converge. Letting \(\delta\downarrow0\) proves the stated integral convergence; its integrand is integrable precisely for \(q<2\).

**Critical second moment.** Uniformly for \(2\le k\le n/2\), apart from the final half-weight atom in the even case, the exact formula and \(\sin x=x(1+O(x^2))\) imply
\[
\Pr\!\left(\Theta_n=\frac{k\pi}{n}\right)
\sin^{-2}\!\left(\frac{k\pi}{n}\right)
=\frac{12}{\pi^2}\frac{k-1}{k^2}+O(n^{-1}).
\]
The expansion is uniform because \((x/\sin x)^2=1+O(x^2)\) on \([0,\pi/2]\); the geometric-weight error is \(O(k/n+1/n)\), which becomes \(O(1/n)\) after multiplying \((k-1)/k^2\). The even endpoint contributes at most \(O(n^{-1})\). Finally \(\sum_{k=2}^{\lfloor n/2\rfloor}(k-1)/k^2=\log n+O(1)\), giving the logarithmic law.

**Supercritical moments.** For fixed \(k\ge2\), as \(n\to\infty\),
\[
n^{2-q}\Pr\!\left(\Theta_n=\frac{k\pi}{n}\right)
\sin^{-q}\!\left(\frac{k\pi}{n}\right)
\longrightarrow \frac{12}{\pi^q}\frac{k-1}{k^q}.
\]
For every \(q>2\), the same two bounds used above dominate the left-hand summands by \(C_q k^{1-q}\), an absolutely summable sequence. Dominated convergence for series therefore gives \(12\pi^{-q}\sum_{k=2}^\infty(k-1)k^{-q}=12\pi^{-q}[\zeta(q-1)-\zeta(q)]\). This completes all quantifiers and parity cases.

## Verification

The standalone `diagonal_transversality_verify.py` uses only the Python standard library. It independently reconstructs **actual Euclidean angles** from the Cartesian coordinates of both diagonals for every four-subset for \(4\le n\le24\), then compares integer frequency counts to the exact formula. Additional checks normalize both parity classes, compare exact discrete and limiting CDFs, independently integrate subcritical moments, and numerically examine the logarithmic and zeta-normalized moments over increasing polygon sizes. Run `python diagonal_transversality_verify.py`. These finite computations check implementations and representative parameters; the displayed infinite-\(n\) assertions follow from the proof, not from numerical extrapolation.

## Relationship to prior work

Poonen and Rubinstein study **distinct spatial intersection points and concurrency** of all diagonals, not the pair-multiplicity-weighted angle distribution. Arikushi and Tóth's Observation 2 establishes the **available angular support** for crossing edges of a regular-polygon drawing of the complete graph; that support is credited here, while its multiplicities and inverse-sine moment phase transition are separate. Bortolotto and Souza determine the **radial location** distribution of intersections of randomly sampled circle chords, including the regular-polygon limiting model; their radial marginal does not determine crossing-angle moments. Barahona Torres, Manrique-Mirón and Treviño-Aguilar obtain a sine law under a **different chord sampling model** (interior endpoints for one chord and a uniform-height horizontal chord); it cannot be substituted for the uniformly selected four boundary vertices. The fourfold counting and inverse-sine spectral claims were not found in the inspected sources or the compared published mathematical index results. This is a provisional originality assessment, not a proof of historical priority.

## Limitations

The finite exact law requires vertices in exact regular position, a **uniformly selected crossing pair** (equivalently a uniform quartet), and multiplicity-counting of crossing pairs rather than distinct intersection locations. The asymptotics are for fixed moment order \(q\) as \(n\to\infty\); no uniform transition theorem when \(q\) depends on \(n\), no result for perturbed polygons, and no finite-\(n\) operator-norm condition-number identity is claimed. The proof establishes the full moment asymptotics but not a closed elementary formula for every finite-\(n\) moment. The source comparison does not establish absolute historical novelty.

## References

1. B. Poonen and M. Rubinstein, *The Number of Intersection Points Made by the Diagonals of a Regular Polygon*, arXiv:math/9508209, first public version 2 August 1995; SIAM J. Discrete Math. 11 (1998), 135–156. Primary classification 51M04.
2. K. Arikushi and C. D. Tóth, *Crossing Angles of Geometric Graphs*, J. Graph Algorithms Appl. 18 (2014), 401–420, DOI:10.7155/jgaa.00329, especially Observation 2.
3. J. I. H. Barahona Torres, P. C. Manrique-Mirón, and E. Treviño-Aguilar, *Angle distribution of two random chords in the disc: A sine law*, arXiv:1911.05576 (2019), Theorem 2.1.
4. C. Bortolotto and V. Souza, *Intersections of random chords of a circle*, arXiv:2504.12866 (2025), Theorem 1 and its regular-polygon interpretation.
