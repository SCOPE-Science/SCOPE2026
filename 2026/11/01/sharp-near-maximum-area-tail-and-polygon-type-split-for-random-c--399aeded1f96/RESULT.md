# Sharp near-maximum area tail and polygon-type split for random central cube sections

## Finding

Let \(Q=[-1,1]^3\), and let \(U\) be Haar-uniform on the unit sphere \(S^2\). Write \(A(U)=\mathcal H^2(Q\cap U^\perp)\) and \(N(U)\) for the number of sides of this section. The latter is almost surely either four or six. The classical sharp maximum is \(4\sqrt2\). The new **joint sharp near-maximum law** is
\[
\boxed{\begin{aligned}
\Pr\big\{A(U)>4\sqrt2-\varepsilon,\ N(U)=4\big\}
 &=\frac3{8\pi\sqrt2}\varepsilon^2+O(\varepsilon^3),\\
\Pr\big\{A(U)>4\sqrt2-\varepsilon,\ N(U)=6\big\}
 &=\frac{3(\pi+2)}{16\pi\sqrt2}\varepsilon^2+O(\varepsilon^3).
\end{aligned}}
\]
Consequently,
\[
\boxed{\Pr\big\{A(U)>4\sqrt2-\varepsilon\big\}
=\frac{3(\pi+4)}{16\pi\sqrt2}\varepsilon^2+O(\varepsilon^3)}
\]
and, conditional on such near-maximal area,
\[
\boxed{\Pr\{N(U)=4\mid A(U)>4\sqrt2-\varepsilon\}
\longrightarrow\frac2{\pi+4},\quad
\Pr\{N(U)=6\mid A(U)>4\sqrt2-\varepsilon\}
\longrightarrow\frac{\pi+2}{\pi+4}.}
\]
These are respectively about \(0.28004958\) and \(0.71995042\).

There is also a **complete local angular limit law**. In any signed-coordinate, ordered-absolute-value chamber adjacent to one of the twelve maximizing normals, write \(a\ge b\ge c\ge0\) for the ordered absolute coordinates of \(U\), and put \(x=a-b\) and \(y=c\). Conditional on that chamber and the near-maximal event, \((x/\varepsilon,y/\varepsilon)\) converges weakly to a uniform point in
\[
\Omega=\left\{(s,t)\in[0,\infty)^2:g(s,t)\le1\right\},\qquad
 g(s,t)=\begin{cases}4s,&t\le s,\\2(t+s^2/t),&t>s.\end{cases}
\]
The limiting region has area \((\pi+4)/64\). Its intersection with \(t\le s\) has area \(1/32\), explaining the two asymptotic polygon probabilities.

## Assumptions and scope

All areas are intrinsic Euclidean areas of central **sections**, not orthogonal projection areas. The cube has side length two; the numerical constants change with scale. A Haar-uniform unoriented plane is represented by a uniformly sampled unit normal, with \(U\) and \(-U\) representing the same plane. The event is a strict upper-tail threshold; replacing strict by non-strict does not change the probabilities because the area level sets have zero spherical measure for sufficiently small positive thresholds. Generic normal directions avoid coordinate zeros and tangent-plane transition great circles; such exceptional normals have probability zero. The local angular coordinates use ordered absolute values, and the orientation chamber is one of the 48 signed-permutation cells on the sphere.

## Proof

**1. Exact section-area and polygon formulas.** Fix a unit normal and order its absolute coordinates as \(a\ge b\ge c\ge0\). Let \(X_1,X_2,X_3\) be independent, uniform on \([-1,1]\). The coarea identity for the linear map \(X\mapsto U\cdot X\) gives \(A(U)=8f_{aX_1+bX_2+cX_3}(0)\), where \(f\) is the density. Conditioning on \(bX_2+cX_3\), the density is \(1/(2a)\) times the probability that its absolute value is at most \(a\). Because \(a\ge b\ge c\), the excluded upper and lower triangular tails of this sum have combined probability \((b+c-a)_+^2/(4bc)\), for \(b,c>0\). Hence
\[
\boxed{A(U)=\frac4a-\frac{(b+c-a)_+^2}{abc}.}\tag{1}
\]
When \(c=0\), interpret the correction continuously as zero. Intersecting the plane with all six open faces of the cube shows that all six contribute polygon sides if and only if \(a<b+c\). Otherwise the section is a quadrilateral. Thus, setting \(x=a-b\), \(y=c\), its type is four when \(y<x\), and six when \(y>x\), apart from null transitions. This face criterion also follows from the requirement that each signed face constraint \(\pm a,\pm b,\pm c\) be balanced by the other two contributions.

**2. Maximizing normals and coordinates.** The sharp cube-slicing theorem states \(A(U)\le4\sqrt2\), with equality precisely for the twelve signed two-coordinate diagonal normals \((\pm e_i\pm e_j)/\sqrt2\), with \(i<j\). This equality characterization is prior work [1], not a new conclusion. By continuity on the compact unit sphere, normals with area within \(\varepsilon\) of \(4\sqrt2\) must approach this finite set as \(\varepsilon\downarrow0\). Each maximum borders four signed-order chambers, so there are 48 congruent local chambers to integrate.

Within one chamber near a maximum, \(a-b=x\ge0\), \(c=y\ge0\), and normalization \(a^2+b^2+y^2=1\) gives
\[
a=\frac{x+\sqrt{2-x^2-2y^2}}2,\qquad b=a-x.
\tag{2}
\]
The spherical-area element in these coordinates is \(J(x,y)\,dx\,dy\), with
\[
J(0,0)=\left\|\frac{\partial(a,b,c)}{\partial x}\times
\frac{\partial(a,b,c)}{\partial y}\right\|_{(0,0)}
=\frac1{\sqrt2},\qquad J(x,y)=\frac1{\sqrt2}+O(x+y).
\tag{3}
\]
The functions are smooth in a fixed small closed quadrant.

**3. Two different first-order area losses.** Let \(\Delta(x,y)=4\sqrt2-A(U)\). Substitution of (2) into (1) gives, uniformly as \(x+y\to0\),
\[
\Delta(x,y)=g(x,y)+O((x+y)^2),
\quad g(x,y)=\begin{cases}
4x,&0\le y\le x,\\
2(y+x^2/y),&y>x\ge0.
\end{cases}\tag{4}
\]
Indeed, in the quadrilateral chamber \(y\le x\) the correction in (1) is zero and \(4/a=4\sqrt2-4x+O((x+y)^2)\). In the hexagon chamber \(y>x\), that correction is \((y-x)^2/(aby)=2(y-x)^2/y+O((x+y)^2)\), while \(4/a=4\sqrt2-4x+O((x+y)^2)\), giving \(4x+2(y-x)^2/y=2(y+x^2/y)\). The error is uniform even near the interface because \(0\le (y-x)^2/y\le y\) for \(y>x\).

The function \(g\) is continuous and positively homogeneous of degree one, and its value on the nonnegative unit quarter-circle is strictly positive. In polar coordinates \((x,y)=r(\cos\phi,\sin\phi)\), \(0\le\phi\le\pi/2\), (4) reads \(\Delta=rG(\phi)+O(r^2)\) uniformly, with \(\inf G>0\). The exact formulas show \(\partial_r\Delta=G(\phi)+O(r)\) uniformly. Hence the radial boundary of \(\{\Delta<\varepsilon\}\) is
\[
r_{\varepsilon}(\phi)=\frac{\varepsilon}{G(\phi)}+O(\varepsilon^2)
\tag{5}
\]
uniformly in \(\phi\). In particular this event lies in \(r=O(\varepsilon)\); the annular boundary error is \(O(\varepsilon^3)\) after area integration. The exact area element (3) contributes the same remainder order.

**4. Exact limiting cone areas.** The limiting scaled region is \(\Omega=\{g\le1\}\). In the quadrilateral sector \(0\le y\le x\), it is \(0\le x\le1/4\) and \(0\le y\le x\), of area
\[
|\Omega_4|=\int_0^{1/4}x\,dx=\frac1{32}.
\tag{6}
\]
For the hexagonal sector \(0\le x<y\), introduce \(t=x/y\in[0,1]\). There \(g=2y(1+t^2)\), and \(dx\,dy=y\,dt\,dy\). It follows that
\[
|\Omega_6|=\frac18\int_0^1\frac{dt}{(1+t^2)^2}
=\frac1{32}+\frac\pi{64}=\frac{\pi+2}{64}.
\tag{7}
\]
Thus \(|\Omega|=(\pi+4)/64\).

**5. Haar normalizing factor and limit law.** Each of the 48 chambers has, by (3)–(5), quad/hex near-maximum spherical areas
\[
\frac{\varepsilon^2}{\sqrt2}|\Omega_4|+O(\varepsilon^3),\qquad
\frac{\varepsilon^2}{\sqrt2}|\Omega_6|+O(\varepsilon^3).
\]
Multiplying by 48 and dividing by \(\operatorname{area}(S^2)=4\pi\) gives the two boxed coefficients and their sum. Dividing by the summed probability gives the conditional polygon probabilities.

For the stronger conditional angular statement, in a fixed chamber the change of variables \((x,y)=\varepsilon(s,t)\) turns the conditional law into normalized Lebesgue integration on \(\{\Delta(\varepsilon s,\varepsilon t)<\varepsilon\}\), weighted by \(J(\varepsilon s,\varepsilon t)\). By (3)–(5), these indicators converge almost everywhere to \(1_{\Omega}\), with uniformly bounded support and uniformly convergent Jacobian. Dominated convergence gives the uniform law on \(\Omega\). This completes the proof.

## Verification

Run `python3 verify_cube_tail.py` using Python 3 with NumPy and SciPy. The self-contained checker constructs the intersection polygon independently from twelve cube-edge intersections and a planar convex hull, rather than from the density formula. For 1,958 nondegenerate deterministic random normals, the polygon's directly calculated area agrees with (1) to maximum absolute discrepancy below \(5\times10^{-15}\), and the side-count classification agrees in all cases. It also integrates (6) and (7) numerically and checks exact limiting constants to machine precision. Finally, numerical quadrature of the **finite-\(\varepsilon\)** Haar event for six decreasing thresholds independently approaches all predicted constants and the conditional split; at \(\varepsilon=0.008\), the total probability divided by \(\varepsilon^2\) is about \(0.304230\), approaching the theorem's \(0.3013918308\). The analytic expansion and angular integration above, not these finite tests, prove the asymptotic law.

## Relationship to prior work

Ball's maximal cube-section theorem gives the maximum and its equality orientations [1], but no sharp Haar probability for nearly maximizing **random** directions. Melbourne–Roberto [2] show quantitative stability of these maximizing orientations, with bounds on their coordinate deviations, but do not compute the probability coefficient or the local angular limit. Ambrus [3] classifies the critical directions of the three-cube section-area function, not the probability of almost-maximum area. Fodor–González Merino [4] study high-dimensional Gaussian-weighted sections orthogonal to a main diagonal, without the present small-deficit random-orientation law. Lonke [5] studies face counts of random cube sections; its global three-dimensional polygon proportions, also established for all rectangular boxes by a separate exact Haar hexagon-law result [6], do not imply the area-conditioned quad/hex split. In particular, our conditioned hexagon probability is approximately \(0.72\), not the unconditioned value. The precise joint tail constant, piecewise limit region, and conditional split are the contributions asserted here; none of the named classical formulas or global probabilities is claimed as newly discovered.

## Limitations

The theorem applies to central hyperplanes through the origin of the **three-dimensional** Euclidean cube, with Haar-uniform normal directions and the specified side length. The explicit polynomial-order remainder is local in the small positive area deficit and is not asserted uniformly across other cube sizes or dimensions without rescaling. It gives a local asymptotic probability law, not the full finite-threshold distribution. No priority claim can exclude an unindexed equivalent stereological calculation. The computer checks cover finitely many samples and quadratures and do not constitute an independent scientific audit.

## References

[1] K. Ball, *Cube Slicing in \(\mathbb R^n\)*, *Proceedings of the American Mathematical Society* 97 (1986), 465–473; equality characterization recalled in [2].

[2] J. Melbourne and C. Roberto, *Quantitative Form of Ball's Cube Slicing in \(\mathbb R^n\) and Equality Cases in the Min-Entropy Power Inequality*, arXiv:2109.03946 (initial version 2021-09-08), https://arxiv.org/abs/2109.03946.

[3] G. Ambrus, *Critical Central Sections of the Cube*, arXiv:2107.14778, https://arxiv.org/abs/2107.14778.

[4] F. Fodor and B. González Merino, *Central Diagonal Sections of Gaussian Cubes*, arXiv:2511.01504 (first posted 2025-11-03), https://arxiv.org/abs/2511.01504.

[5] Y. Lonke, *On Random Sections of the Cube*, arXiv:math/9812123; *Discrete & Computational Geometry* 23 (2000), 157–169, https://arxiv.org/abs/math/9812123.

[6] *Exact Haar Hexagon Law and Cubic Rigidity for Central Sections of Rectangular Boxes*, publicly available mathematical result (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4.
