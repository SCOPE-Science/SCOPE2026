# A universal self-Cheeger threshold and angular curvature jump for outer-parallel polygons

## Finding
Let \(P\subset\mathbb R^2\) be a compact convex polygon of positive area, with at least three genuine vertices and no consecutive collinear edges. Write \(A=|P|\), \(L=\operatorname{per}(P)\), \(\alpha_i\in(0,\pi)\) for its interior angles, and
\[
T=\sqrt{A/\pi},\qquad C=\sum_i\cot(\alpha_i/2),\qquad D=L+2\pi T.
\]
For \(t\ge0\) put \(\Omega_t=P+tB\), where \(B\) is the closed unit Euclidean disk, and let \(h(t)=\inf\{\operatorname{per}(E)/|E|:E\subseteq\Omega_t,\ |E|>0\}\), with the infimum over finite-perimeter sets.

**Theorem (sharp self-Cheeger transition and angle signature).** The unique Cheeger set of \(\Omega_t\) is the whole of \(\Omega_t\) exactly when \(t\ge T\). Throughout this regime,
\[
h(t)=\frac{L+2\pi t}{A+Lt+\pi t^2}.
\]
For \(0\le t<T\), if \(s(t)=1/h(t)\) and \(\delta(t)=s(t)-t\), then \(\delta(t)>0\) is the unique root of
\[
|P\ominus\delta B|=\pi(t+\delta)^2,
\]
and the proper Cheeger set is \((P\ominus\delta(t)B)+(t+\delta(t))B\). Near the transition the function \(h\) is analytic on each side and globally \(C^1\), but not \(C^2\):
\[
\boxed{\quad h''(T^-)-h''(T^+)=-\frac{8\pi^2(C-\pi)}{D^3}<0.\quad}
\]
Thus the normalized one-sided curvature jump determines the exact angular invariant \(C\) from \(A,L\) and the offset Cheeger profile. Both the threshold and jump are sharp equalities for every such polygon, not merely bounds.

The local rounding scale has the more precise expansion, as \(\varepsilon\downarrow0\),
\[
\delta(T-\varepsilon)=\frac{2\pi T}{D}\varepsilon+\frac{\pi(4\pi CT^2-L^2)}{D^3}\varepsilon^2+O_P(\varepsilon^3).
\]
Here \(C>\pi\) for every polygon in the stated class.

## Assumptions and scope
A convex polygon is the closed convex hull of finitely many points with nonempty interior; redundant collinear vertices are discarded. No regularity or rotational symmetry is required. Erosion is the Minkowski difference \(P\ominus uB=\{x:x+uB\subseteq P\}\). The statements at \(t=T\) mean ordinary two-sided derivatives on the specified open half-neighborhoods, not a classical second derivative at the joining point. The theorem does not assert global analyticity below \(T\), because inward-offset edges can disappear at further parameter thresholds.

## Proof
**1. Transfer of inward offsets.** For an arbitrary compact convex \(K\) and \(u\ge0\), its erosion by \(uB\) is the intersection of all halfplanes \(\langle x,v\rangle\le h_K(v)-u\), over unit vectors \(v\), where \(h_K\) is the support function. Since \(h_{P+tB}(v)=h_P(v)+t\), it follows exactly that
\[
(\Omega_t\ominus sB)=
\begin{cases}
 P+(t-s)B,&0\le s\le t,\\
 P\ominus(s-t)B,&s\ge t.
\end{cases}
\]
In the first case, the displayed body is a Minkowski sum because the shifted support function is \(h_P+t-s\); in the second it is the intersection of the contracted support halfplanes.

**2. Identify the unique transition.** The established planar convex Cheeger characterization says that the positive Cheeger radius \(s(t)=1/h(t)\) is the unique solution of \(|\Omega_t\ominus sB|=\pi s^2\), and the unique Cheeger set is \((\Omega_t\ominus sB)+sB\). Evaluate the difference of the two sides at \(s=t\): it is \(A-\pi t^2\), since \(\Omega_t\ominus tB=P\). The left side of this root equation is nonincreasing in \(s\), whereas \(\pi s^2\) is strictly increasing. Thus \(s(t)\le t\) exactly for \(t\ge T\), with equality at \(T\). For \(s\le t\), planar Steiner's identity \(|P+uB|=A+Lu+\pi u^2\) yields
\[
A+L(t-s)+\pi(t-s)^2=\pi s^2.
\]
Cancelling \(\pi s^2\) gives \(s=(A+Lt+\pi t^2)/(L+2\pi t)\). Its Cheeger set is \((P+(t-s)B)+sB=\Omega_t\). For \(s>t\), writing \(\delta=s-t>0\) gives the stated erosion equation and Cheeger set; it is proper because \((P\ominus\delta B)+\delta B\) is strictly smaller than the genuine polygon \(P\) (a positive-radius disk opening cannot reconstruct any genuine corner wedge), and adding \(tB\) preserves this strict inclusion by support functions. This proves the exact transition and global formulas.

**3. Polygonal inward area.** For all sufficiently small \(u\ge0\), each polygon edge survives its inward translation by distance \(u\). At vertex \(i\), its two neighboring side lengths each lose \(u\cot(\alpha_i/2)\). Therefore the perimeter of the eroded polygon is \(L-2Cu\). Integrating the standard inner-area variation \(\frac{d}{du}|P\ominus uB|=-\operatorname{per}(P\ominus uB)\), or equivalently summing its corner triangles, gives the exact polynomial
\[
|P\ominus uB|=A-Lu+Cu^2
\]
in a nonempty interval \(0\le u<u_0(P)\).

**4. Expansion and derivative jump.** Put \(t=T-\varepsilon\) and \(u=\delta(t)\). Continuity of the unique root from step 2 gives \(u\to0\). The exact local root equation becomes
\[
A-Lu+Cu^2=\pi(T-\varepsilon+u)^2.
\]
Its partial derivative with respect to \(u\) at \((\varepsilon,u)=(0,0)\) equals \(-D<0\), so the implicit function theorem yields a real-analytic branch. Equating coefficients of \(\varepsilon\) and \(\varepsilon^2\) gives
\[
u=b_1\varepsilon+b_2\varepsilon^2+O(\varepsilon^3),\quad
b_1=\frac{2\pi T}{D},\quad
b_2=\frac{\pi(4\pi CT^2-L^2)}{D^3}.
\]
Since \(s(T-\varepsilon)=T-\varepsilon+u\), its one-sided first derivative is \(L/D\) and second derivative is \(2b_2\). On the self-Cheeger side, \(s(t)=(A+Lt+\pi t^2)/(L+2\pi t)\), so \(s(T)=T\), \(s'(T^+)=L/D\), and \(s''(T^+)=-2\pi(L-2\pi T)/D^2\). Subtraction yields
\[
s''(T^-)-s''(T^+)=\frac{8\pi^2T^2(C-\pi)}{D^3}.
\]
For \(h=1/s\), the first derivatives agree and the jump in second derivatives is precisely \(-[s''(T^-)-s''(T^+)]/T^2\), proving the boxed identity.

**5. Strictness.** Let \(\beta_i=\pi-\alpha_i\) be exterior angles. Their sum is \(2\pi\), with every \(\beta_i\in(0,\pi)\). Strict convexity of tangent on \((0,\pi/2)\) and Jensen give
\[
C=\sum_i\tan(\beta_i/2)\ge n\tan(\pi/n)>\pi,
\]
where the last inequality is \(\tan z>z\) for positive \(z<\pi/2\). Hence the second-derivative jump is genuinely nonzero at every polygonal threshold.

## Verification
The accompanying dependency-free program `verify.py` computes inner offsets independently by successive halfplane clipping, checks the polygonal area expansion and the near-threshold Cheeger-root expansion on squares, triangles, regular polygons, and an asymmetric pentagon, and checks the predicted sign of the jump. All tested numerical assertions passed when the program was executed from the package. These finite checks do not establish the theorem for arbitrary polygons; the proof above does.

## Relationship to prior work
Kawohl and Lachand-Robert (2006) proved the general planar convex Cheeger-radius equation and self-Cheeger curvature criterion; these foundational theorems are used, not claimed new. Cañete (first publicly published November 2021) studied Cheeger regularity and inherited symmetry for rotationally symmetric planar convex bodies, but did not formulate the outer-parallel polygonal transition or angular second-derivative formula. Ftouhi (first publicly available December 2024 and published 2025) proved general monotonicity and first differentiability for Cheeger constants of parallel bodies, without the universal polygonal threshold or explicit nonzero second-derivative jump. The present theorem adds a closed, all-polygon, parameter-sharp transition and a one-sided second-order corner signature, rather than a second proof of the established convex Cheeger characterization.

## Limitations
The result is planar and Euclidean, and the exact polynomial for the inner erosion is local to the threshold; no global closed formula for all \(t<T\) is claimed. The analytical result is checked internally but not independently validated. Scholarly priority outside inspected full texts and indexed records is not exhaustively established; a hidden earlier computation of the same derivative jump remains possible. The standalone checker uses floating-point arithmetic and only finite examples, separate from the general proof.

## References
1. A. Cañete, *Cheeger Sets for Rotationally Symmetric Planar Convex Bodies*, Results in Mathematics 77, article 9 (first public 6 November 2021). DOI: 10.1007/s00025-021-01539-7.
2. B. Kawohl and T. Lachand-Robert, *Characterization of Cheeger sets for convex subsets of the plane*, Pacific Journal of Mathematics 225 (2006), 103–118. DOI: 10.2140/pjm.2006.225.103.
3. I. Ftouhi, *The Monotonicity of the Cheeger constant for Parallel Bodies*, arXiv:2412.20917 (first public 30 December 2024); Journal of Optimization Theory and Applications 206, article 44 (2025). DOI: 10.1007/s10957-025-02727-z.
4. G. Saracco, *A Sufficient Criterion to Determine Planar Self-Cheeger Sets*, arXiv:1906.12101 (2019); Journal of Convex Analysis 28 (2021), 951–958. DOI: 10.68381/jca28055.
