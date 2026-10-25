# Exact maximal-shadow law and unique optimum for odd regular bipyramids

## Finding
For every odd integer \(n\ge3\), write \(B_{n,h}\) for the solid regular bipyramid with equatorial circumradius \(1\) and apices \((0,0,\pm h)\). Under a uniformly random orthogonal planar projection, the probability that **all** \(n+2\) vertices belong to the projected convex hull is
\[
 P_n(h)=\frac2a\left[2\arcsin(q\sin a)-\arcsin(q\sin(a/2))-\arcsin(q\sin(3a/2))\right],
 \qquad a=\pi/n,\quad q=h/\sqrt{h^2+\cos^2a}.
\]
For every odd \(n\), this probability has a **unique** global maximizing height \(h_n>0\), determined by the unique solution \(q_n\in(0,1)\) of
\[
 \frac{2\sin a}{\sqrt{1-q_n^2\sin^2a}}
 =\frac{\sin(a/2)}{\sqrt{1-q_n^2\sin^2(a/2)}}
 +\frac{\sin(3a/2)}{\sqrt{1-q_n^2\sin^2(3a/2)}},
 \qquad h_n=\frac{q_n\cos a}{\sqrt{1-q_n^2}}.
\]
Along odd integers tending to infinity,
\[
 q_n\longrightarrow1/\sqrt3,\qquad h_n\longrightarrow1/\sqrt2,\qquad
 n^2P_n(h_n)\longrightarrow\pi^2/(3\sqrt3).
\]
The leading constant is half of the analogous even-sided maximal silhouette constant.

## Assumptions and scope
The base consists of the \(n\) planar points \((\cos(2\pi j/n),\sin(2\pi j/n),0)\), for integer \(0\le j<n\); the two apices are \((0,0,h)\) and \((0,0,-h)\), with \(h>0\). A viewing direction is Haar uniform on the unit sphere modulo sign. The projected convex hull is formed from all \(n+2\) projected points. Degenerate orientations, forming a zero-probability set, are excluded when counting vertices. This is a statement for **odd** \(n\), not a restatement of the even-polygon result.

## Proof
### 1. Projected polygon and the one-facet criterion
Fix a viewing direction whose absolute vertical coordinate is \(c\in(0,1)\) and whose azimuth is \(\phi\). Use orthonormal screen coordinates in which the equatorial vertices project to
\[
 E_j=(\sin(2\pi j/n+\phi),\;c\cos(2\pi j/n+\phi))
\]
and the apices project to \((0,\pm h\sqrt{1-c^2})\). Put \(C=\cos(\pi/n)\), \(a=\pi/n\), and \(k=h\sqrt{1-c^2}/c\). The projected equatorial polygon obeys the \(n\) supporting inequalities
\[
 (\sin\psi_j)X+(\cos\psi_j)Y/c\le C,\quad \psi_j=\phi+(2j+1)a.
\]
An added point on the vertical screen axis outside this polygon preserves all \(n\) equatorial vertices exactly when it violates precisely one side inequality: crossing two or more consecutive supporting sides removes an intervening vertex, whereas crossing one side inserts the point between that side's endpoints. The upper and lower added apices are on opposite sides of the polygon and their replacement chains are disjoint. Therefore all \(n+2\) vertices remain exposed exactly when the upper apex violates one *positive-cosine* side and the lower apex violates one *negative-cosine* side. This also follows directly by cyclic order of the convex-hull boundary; equality boundaries have measure zero.

### 2. The odd-angle gap
The \(n\) side-normal azimuths form a regular angular lattice. When \(n\) is odd, the distance from the positive vertical normal to the closest side normal and the corresponding distance at the opposite normal add to \(a\). Write these distances as \(x\) and \(a-x\), where \(x\) is uniform on \([0,a]\). Their maximum \(d=\max(x,a-x)\) is uniform on \([a/2,a]\) with density \(2/a\). The second-closest side normal to either vertical direction is at angular distance \(2a-d\), which belongs to \([a,3a/2]\subset(0,\pi/2]\). Consequently the one-facet criterion for **both** apices reduces to
\[
 \frac{C}{\cos d}<k<\frac{C}{\cos(2a-d)}.
\]
At the endpoint where the upper bound is infinite, the same inequality holds by continuity.

### 3. Integrating Haar directions
For a uniformly random unoriented spatial direction, \(c=|u_z|\) is uniform on \([0,1]\), independently of azimuth. For fixed \(d\), the probability of the previous inequality is
\[
 g(d)-g(2a-d),\qquad
 g(t)=\frac{h\cos t}{\sqrt{C^2+h^2\cos^2t}}.
\]
The antiderivative of \(g(t)\) is \(F(t)=\arcsin(q\sin t)\), where \(q=h/\sqrt{h^2+C^2}\). Integration against density \(2/a\) yields
\[
 \frac2a\left[\int_{a/2}^a g(t)\,dt-\int_a^{3a/2}g(t)\,dt\right]
 =\frac2a\bigl(2F(a)-F(a/2)-F(3a/2)\bigr).
\]
This is the asserted exact law.

### 4. Uniqueness of the optimal aspect ratio
Set \(A=\sin a\), \(B=\sin(a/2)\), \(D=\sin(3a/2)\), and \(f(q)=2\arcsin(Aq)-\arcsin(Bq)-\arcsin(Dq)\). Here \(0<B<A<D\le1\). We have \(f(0)=f(1)=0\), and \(f(q)>0\) for interior \(q\) by the positive interval integral above. Its derivative on \((0,1)\) has the absolutely convergent power series
\[
 f'(q)=\sum_{m\ge0}\frac{\binom{2m}{m}}{4^m}
 \left(2A^{2m+1}-B^{2m+1}-D^{2m+1}\right)q^{2m}.
\]
For \(v>0\) put \(H(v)=(B/A)^v+(D/A)^v\). Strict logarithmic concavity of sine on \((0,\pi)\) implies \(BD<A^2\), hence \(H'(0)<0\). Also \(H(0)=2\), \(H(1)=2\cos(a/2)<2\), \(H''(v)>0\), and \(H(v)\to\infty\). Thus there is exactly one \(v_*>1\) with \(H(v_*)=2\); the coefficients in the series for \(f'\) change sign **at most once**, from positive to negative. Some coefficients are positive, since \(f'(0)=2A-B-D>0\), and some are negative, since \(H(v)\to\infty\). If \(m_0\) denotes the last index of a positive coefficient, the positive terms of \(f'(q)/q^{2m_0}\) are nonincreasing and the negative terms strictly decreasing for \(q\in(0,1)\). So this quotient is strictly decreasing, and \(f'\) has at most one zero. It has at least one zero because \(f'(0)>0\) and \(f'(1)<0\): for \(n\ge5\), the latter follows from strict convexity of tangent,
\[
 f'(1)=2\tan a-\tan(a/2)-\tan(3a/2)<0;
\]
for \(n=3\), the final tangent term diverges and \(f'(q)\to-\infty\) as \(q\uparrow1\). Hence the unique interior zero is the unique global maximizer. The change of variables \(h\leftrightarrow q\) is bijective and increasing.

### 5. Large-order asymptotics
Uniformly for \(0\le q\le1\) and small \(t\),
\[
 \arcsin(q\sin t)=qt-\frac{q(1-q^2)}6t^3+O(t^5).
\]
Substituting \(t=a/2,a,3a/2\) cancels all linear terms and gives
\[
 f(q)=\frac{a^3}{4}q(1-q^2)+O(a^5),\quad
 P_n(h(q))=\frac{a^2}{2}q(1-q^2)+O(a^4),
\]
uniformly on the closed \(q\)-interval. The unique maximizer of \(q(1-q^2)\) on \([0,1]\) is \(q=1/\sqrt3\), so every unique \(q_n\) tends to that number. Using \(\cos a\to1\), the height limit follows. Evaluating the maximum gives \(n^2P_n(h_n)\to\pi^2/(3\sqrt3)\).

## Verification
Execute `python3 verify_odd_bipyramid.py` using the Python standard library. It independently constructs two-dimensional convex hulls with the monotone-chain algorithm, compares all-vertex survival to the facet criterion on \(40{,}000\) random orientations, checks probabilities against random proportions, tests the unique critical height for multiple odd orders, and checks the exact large-order constants. The script is a *finite corroboration*, not a proof of uniqueness or the asymptotic theorem.

## Relationship to prior work
Glisse and Lazard's work on average silhouette complexity addresses global complexity estimates for broad classes of surface-approximating polyhedra; it does not state this shape-specific probability. Glisse, Lazard, Michel and Pouget examine maximal silhouette complexity for Poisson random polytopes, not fixed regular odd bipyramids. Black and Criado provide general expected-shadow-vertex bounds for fixed polytopes rather than an exact probability for the all-vertex event. The known even-sided regular-prism maximal central-section law, related through polarity, has a different parity arrangement of opposite facet normals; its large-order optimized coefficient is twice the value here. These statements are distinct by their objects, quantifiers and claimed implications, though comprehensive historical priority has not been independently certified.

## Limitations
The theorem applies only to regular *odd*-sided right bipyramids with equal apical heights, Haar-uniform orthogonal views, and almost-sure vertex counts. It does not give all silhouette-size probabilities or treat irregular/oblique bipyramids. The proof does not imply that the odd-versus-even constant gap holds under arbitrary deformations. The originality comparison is limited to the identified and inspected sources; inaccessible or unindexed literature could contain equivalent formulas. No independent mathematical audit has been performed.

## References
- M. Glisse and S. Lazard, *An Upper Bound on the Average Size of Silhouettes*, arXiv:cs/0702087, submitted February 14, 2007, https://arxiv.org/abs/cs/0702087. The work also has an earlier 2006 conference version.
- M. Glisse, S. Lazard, J. Michel, and M. Pouget, *Silhouette of a Random Polytope*, *Journal of Computational Geometry* 7(1), 86–99 (2016), DOI:10.20382/jocg.v7i1a5, https://jocg.org/index.php/jocg/article/view/3009.
- A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936v1, submitted June 11, 2024, https://arxiv.org/html/2406.06936v1.
