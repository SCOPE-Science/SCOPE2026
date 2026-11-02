# Two-scale corner-collision laws for long distances in disk-clipped squares

## Finding

For \(1\le r\le\sqrt2\), define the convex disk-clipped square
\[
K_r=[-1,1]^2\cap\{(x,y)\in\mathbb R^2:x^2+y^2\le r^2\}.
\]
Let \(X_r,Y_r\) be independent uniform-area points in \(K_r\), let \(D_r=\|X_r-Y_r\|_2\), and write \(T_r(\varepsilon)=\Pr\{D_r>2r-\varepsilon\}\). Its diameter is exactly \(2r\). Define the area and the total angular extent of its circular boundary arcs by
\[
A(r)=\pi r^2-4\bigl(r^2\arccos(1/r)-\sqrt{r^2-1}\bigr),\qquad
\Theta(r)=2\pi-8\arccos(1/r).
\]
The following four assertions jointly describe the near-diameter tail and the collapse of its maximizing circular arcs into the square's four corners.

**Fixed rounded shape.** For each fixed \(1\le r<\sqrt2\),
\[
T_r(\varepsilon)\sim C(r)\varepsilon^{5/2},\qquad
C(r)=\frac{16r^{3/2}\Theta(r)}{15A(r)^2}
\quad(\varepsilon\downarrow0).
\]
In particular, \(C(1)=32/(15\pi)\), and the coefficient vanishes at the polygonal limit:
\[
C(r)\sim\frac{4\,2^{5/4}}{15}(\sqrt2-r)
\quad(r\uparrow\sqrt2).
\]

**Square endpoint.** At \(r=\sqrt2\),
\[
T_{\sqrt2}(\varepsilon)\sim\frac{\varepsilon^4}{24}.
\]

**Curvature-scale crossover.** Fix \(z>0\), put \(r_\lambda=\sqrt2-\lambda\), and let \(\lambda\downarrow0\). Then
\[
\frac{T_{r_\lambda}(z\lambda^2)}{\lambda^6}\longrightarrow
H(z)=
\begin{cases}
\displaystyle \frac{8\,2^{1/4}}{15}z^{5/2}-\frac{\sqrt2}{6}z^3,
&0<z\le1/\sqrt2,\\[4pt]
\displaystyle\frac{30z^2-5\sqrt2z+1}{60},
&z\ge1/\sqrt2.
\end{cases}
\]
The two branches agree at the transition \(z=1/\sqrt2\).

**Corner-scale crossover.** Fix \(t\ge0\), put \(r_\varepsilon=\sqrt2-t\varepsilon\), and let \(\varepsilon\downarrow0\). Then
\[
\frac{T_{r_\varepsilon}(\varepsilon)}{\varepsilon^4}
\longrightarrow J(t)=\frac1{24}+\frac t3+\frac{t^2}{2}.
\]
The two crossovers occur at different joint scales and cannot be inferred from the two fixed-shape endpoint tails by interchanging limits.

## Assumptions and scope

All distances are ordinary Euclidean distances between two **interior area-uniform** points, not invariant random-line chords or distances along the boundary. The set \(K_r\) is full-dimensional throughout the stated interval. Limits in the first and square assertions fix \(r\) before letting \(\varepsilon\) vanish. In the two joint limits, \(z\) and \(t\) are fixed finite constants, not functions of the vanishing parameter. The symbols \(\sim\) and \(\longrightarrow\) denote respectively a positive-ratio limit of one and an ordinary limit. No uniformity over unbounded \(z\) or \(t\) is asserted.

## Proof

**1. Diameter and area.** Since \(K_r\subseteq\overline B(0,r)\), its diameter is at most \(2r\). The points \(\pm(r/\sqrt2,r/\sqrt2)\) belong to \(K_r\), so equality holds. For \(1\le r\le\sqrt2\), the four disk caps cut off by \(|x|>1\) or \(|y|>1\) have pairwise disjoint interiors. Each cap has area \(r^2\arccos(1/r)-\sqrt{r^2-1}\); subtraction proves \(A(r)\). A point on the circle of radius \(r\) survives the square constraint exactly when both absolute coordinate values do not exceed \(1\). Four angular arcs remain, with total angular measure \(\Theta(r)\).

**2. Fixed-radius law.** For \(r<\sqrt2\), every diameter pair is an antipodal pair on the surviving circular arcs (including their endpoints). Compactness localizes all pairs having distance \(2r-o(1)\) to this diametral set. Away from its finitely many arc endpoints, use polar coordinates
\[
X=(r-u)(\cos\theta,\sin\theta),\qquad
Y=(r-v)(\cos(\theta+\pi+\phi),\sin(\theta+\pi+\phi)),
\]
with \(u,v\ge0\). Uniformly on compact subarcs, as \((u,v,\phi)\to0\),
\[
2r-\|X-Y\|_2=u+v+\frac r4\phi^2+o(u+v+\phi^2),
\]
and the product area element is \((r-u)(r-v)\,du\,dv\,d\theta\,d\phi\). Setting \(u=\varepsilon U\), \(v=\varepsilon V\), and \(\phi=\sqrt\varepsilon\,W\), the limiting integral at any interior arc angle is
\[
r^2\int_{\mathbb R}\int_{U,V\ge0}
\mathbf1\{U+V+(r/4)W^2<1\}\,dU\,dV\,dW
=\frac{16r^{3/2}}{15}.
\]
Here the inner simplex area is \((1-rW^2/4)_+^2/2\). Arc endpoints contribute zero to this leading coefficient: remove angular intervals of arbitrarily small fixed total measure, use the uniform bound \(u+v\le\varepsilon\) and \(|\phi|=O(\sqrt\varepsilon)\), then restore those intervals. Dividing by \(A(r)^2\) and integrating over \(\Theta(r)\) establishes \(C(r)\), including \(r=1\) by the same full-circle calculation. Differentiation of \(\arccos(1/r)\) at \(r=\sqrt2\) shows \(\Theta(r)\sim4\sqrt2(\sqrt2-r)\); together with \(A(r)\to4\), this gives the stated decay of \(C(r)\).

**3. Corner localization.** When \(r\to\sqrt2\) and \(\varepsilon\to0\), any pair with \(D_r>2r-\varepsilon\) must approach one of the four **ordered** opposite-corner pairs of \([-1,1]^2\), by compactness and the fact that these are exactly the limiting square's diameter pairs. Near \((1,1)\) write \(X=(1-U,1-V)\) with \(U,V\ge0\), and use analogous positive inward coordinates near \((-1,-1)\) for \(Y\). Every opposite-corner pair has the same contribution by symmetry.

**4. Square and corner-scale crossover.** Put \(r=\sqrt2-t\varepsilon\) with fixed \(t\ge0\), and write \(U=\varepsilon a\), \(V=\varepsilon b\), and likewise \(U'=\varepsilon c\), \(V'=\varepsilon d\). The circle condition expands to
\[
a+b\ge\sqrt2t+O(\varepsilon),\qquad
c+d\ge\sqrt2t+O(\varepsilon).
\]
The distance condition expands to
\[
a+b+c+d<\sqrt2(2t+1)+O(\varepsilon).
\]
All four rescaled variables are bounded on the event. Boundary sets have zero four-dimensional volume, so dominated convergence applies. Set \(a+b=\sqrt2t+x\) and \(c+d=\sqrt2t+y\); the Jacobian of summing each pair of nonnegative coordinates contributes its sum. The limiting four-dimensional volume per ordered opposite-corner pair equals
\[
\int_{x,y\ge0,\ x+y<\sqrt2}
(x+\sqrt2t)(y+\sqrt2t)\,dx\,dy
=\frac16+\frac{4t}{3}+2t^2.
\]
There are four such ordered pairs, and \(A(r)^2\to16\). Multiplying by \(4/16\) gives \(J(t)\). In particular \(J(0)=1/24\), proving the square law.

**5. Curvature-scale crossover.** Set \(r=\sqrt2-\lambda\), \(\varepsilon=z\lambda^2\) for fixed \(z>0\). In the same corner coordinates define \(S=U+V\), \(T=U-V\). The square constraints are \(S\ge|T|\); the circular boundary is
\[
S\ge 2-\sqrt{2r^2-T^2}.
\]
For pairs within \(O(\lambda^2)\) of the diameter, the triangle inequality and the near-antipodality of their radius vectors imply \(T=O(\lambda)\) and \(S=\sqrt2\lambda+O(\lambda^2)\). Thus introduce bounded variables \(w,q\) by
\[
T=\lambda w,\qquad
S=\sqrt2\lambda+\lambda^2\bigl(w^2/4+q\bigr).
\]
The circular constraint becomes \(q\ge o(1)\), and the square constraint becomes \(|w|\le\sqrt2+o(1)\). The area Jacobian for one point tends to \(\lambda^3\,dq\,dw/2\). For a second point at the opposite corner with variables \(w',q'\), direct expansion of the Euclidean distance gives
\[
2r-\|X-Y\|_2
=\frac{\lambda^2}{\sqrt2}
\left(q+q'+\frac{(w-w')^2}{8}\right)+o(\lambda^2).
\]
All relevant scaled variables lie in a fixed bounded region, so dominated convergence applies. Integrating over \(q,q'\ge0\), summing the four ordered opposite-corner pairs and dividing by \(A(r)^2\to16\), gives
\[
H(z)=\frac1{32}\int_{-\sqrt2}^{\sqrt2}
\int_{-\sqrt2}^{\sqrt2}
\left(\sqrt2z-\frac{(w-w')^2}{8}\right)_+^2\,dw\,dw'
=\frac1{16}\int_0^{2\sqrt2}
(2\sqrt2-v)\left(\sqrt2z-v^2/8\right)_+^2\,dv.
\]
For \(z\le1/\sqrt2\), the upper endpoint of the positive integrand is \(\sqrt{8\sqrt2z}\); for larger \(z\), it is \(2\sqrt2\). Elementary polynomial integration on these two intervals yields exactly the two displayed branches of \(H\). The threshold therefore has geometric content: it is the point where all tangential differences between the two shrinking circular arcs become admissible. This finishes all four assertions.

## Verification

Run `python CHECK.py` with Python 3, NumPy, SciPy, and SymPy installed. The script verifies both closed-form branches of \(H\) and the polynomial \(J\) by symbolic integration. It also numerically integrates an independently written exact opposite-corner distance inequality in \((S,T)\) coordinates, using Gaussian quadrature, and compares the resulting finite-parameter tails with three asymptotic regimes. The checked program outputs 25 passing assertions. These tests are not a substitute for the limiting and localization arguments above.

## Relationship to prior work

Classical geometric-probability results compute distance distributions for disks, rectangles and other standard regions, often by the overlap/covariogram method. In particular, Alagar (1976) gives uniform-point distance laws in balls and adjacent squares; Sheng (1985) develops general distance integrals in planar regions; Kumar and collaborators (2014, Appendix C) record the square's distance density. Those formulas provide background but do not themselves state the two specific joint square–disk crossover limits proved here. A separate recent result studies extreme **sample diameters** in a shrinking two-disk lens; its observation variable and degeneration differ from the two-point area-uniform distance in the present clipped-square family. The present square-only and disk-only leading coefficients are consistent with existing distribution formulas and are not individually presented as new discoveries. Historical priority of the combined two-scale law has not been independently established.

## Limitations

The result concerns precisely the concentric intersection of an axis-aligned square and a centered Euclidean disk; no classification for arbitrary rounded polygons, nonsymmetric clipping, or higher-dimensional boxes is asserted. The asymptotic statements do not give finite-parameter error bounds uniform over all scaling variables. The relevance of general prior distance-integral literature was checked, but the complete text of Sheng's historical paper was not available; it may contain unlocated specialized consequences. The proof relies on ordinary Euclidean area sampling, not line-invariant chord sampling.

## References

1. V. S. Alagar, “The distribution of the distance between random points,” *Journal of Applied Probability* **13** (1976), 558–566. DOI: 10.2307/3212475.
2. T. K. Sheng, “The distance between two random points in plane regions,” *Advances in Applied Probability* **17** (1985), 748–773. DOI: 10.2307/1427086.
3. P. F. Ehlers and E. G. Enns, “Random secants of a convex body generated by surface randomness,” *Journal of Applied Probability* **18** (1981), 157–166. DOI: 10.2307/3213176.
4. A. Kumar, V. Grupcev, Y. Yuan, J. Huang, Y.-C. Tu, and G. Shen, “Computing Spatial Distance Histograms for Large Scientific Datasets On-the-Fly,” *IEEE Transactions on Knowledge and Data Engineering* **26** (2014), 2410–2424, Appendix C. DOI: 10.1109/TKDE.2014.2298015. Public manuscript: https://pmc.ncbi.nlm.nih.gov/articles/PMC4172330/.
5. S. Lellouche and M. Souris, “Distribution of Distances between Elements in a Compact Set,” *Stats* **3** (2020), 1–15, published online 2019-12-26. DOI: 10.3390/stats3010001.
6. T. Koshizuka, “On the Random Distance Within an Area,” *Journal of the Operations Research Society of Japan* **21** (1978), 302–319, especially Section 2 (disk and square distance densities). DOI: 10.15807/jorsj.21.302. Open PDF: https://www.jstage.jst.go.jp/article/jorsj/21/2/21_KJ00002432743/_pdf/-char/en.
