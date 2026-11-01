# A sharp two-cycle fold and a three-halves onset law for a fixed-point-free memristor map

## Finding

Let \(F_{\alpha,\beta}:\mathbb R^2\to\mathbb R^2\) be the real discrete map
\[
F_{\alpha,\beta}(x,y)=\bigl(\alpha\cos x+\beta(y^2-1)x,\ y+x\bigr),
\qquad \alpha>0,\quad 0<\beta\le2.
\]
For \(1<\beta\le2\), define
\[
R_\beta=\sqrt{1-1/\beta},\qquad
Q_\beta(u)=\frac{\beta u^2\sqrt{R_\beta^2-u^2/4}}{\cos u}
\quad (0<u<2R_\beta).
\]
The function \(Q_\beta\) has a *unique*, strictly nondegenerate maximum at a point \(u_\beta\), and we write \(\alpha_*(\beta)=Q_\beta(u_\beta)>0\). The complete number of geometrically distinct prime-period-two orbits of \(F_{\alpha,\beta}\) is
\[
\begin{array}{c|c}
\text{parameter regime}&\text{number of distinct prime-two orbits}\\ \hline
0<\beta\le1&0\\
1<\beta\le2,\ \alpha>\alpha_*(\beta)&0\\
1<\beta\le2,\ \alpha=\alpha_*(\beta)&1\\
1<\beta\le2,\ 0<\alpha<\alpha_*(\beta)&2.
\end{array}
\]
There are no fixed points for \(\alpha>0\). The threshold \(\alpha_*(\beta)\) is continuous and strictly increasing on \((1,2]\), and it has the sharp singular onset
\[
\alpha_*(\beta)=\frac8{3\sqrt3}(\beta-1)^{3/2}
+O\bigl((\beta-1)^{5/2}\bigr)\qquad(\beta\downarrow1).
\]
At each fixed \(1<\beta\le2\), the two period-two orbits coalesce in a nondegenerate *scalar root fold* when \(\alpha\uparrow\alpha_*(\beta)\): their positive first coordinates satisfy
\[
u_\pm(\alpha)=u_\beta\pm
\sqrt{\frac{2[\alpha_*(\beta)-\alpha]}{-Q_\beta''(u_\beta)}}
+O\bigl(\alpha_*(\beta)-\alpha\bigr).
\]
This refers to a fold in the period-two solution set, not to a claim about attraction, global basins, or the second eigenvalue of the return map.

## Assumptions and scope

The domain is the full real plane, not a preselected trapping region. Parameters satisfy \(\alpha>0\) and \(0<\beta\le2\). The limit \(\alpha=0\) is excluded because the map then has fixed points; the regime \(\beta>2\) is excluded from the census. The interval \(1.35\le\beta\le1.85\), used in the numerical parameter study of the original publication, lies entirely in the covered range. A prime-period-two orbit consists of two distinct points exchanged by \(F_{\alpha,\beta}\), counted once up to swapping their order.

## Proof

**1. Exact elimination of the second iterate.** Let \((x,y)\) lie on a prime-two orbit, and write its successor \((x',y')\). Since \(y'=y+x\) and \(y=y'+x'\), one has \(x'=-x\). Also \(x\ne0\), since \(F_{\alpha,\beta}(0,y)=(\alpha,y)\). By exchanging the two orbit points, take \(x>0\), and set \(z=y+x/2\). The orbit points are exactly \((x,z-x/2)\) and \((-x,z+x/2)\). The two first-coordinate equations become
\[
\alpha\cos x=\bigl[\beta(1-(z-x/2)^2)-1\bigr]x,
\quad
\alpha\cos x=\bigl[1-\beta(1-(z+x/2)^2)\bigr]x.
\]
Equating them gives
\[
z^2+x^2/4=1-1/\beta.
\]
Substituting this identity into either equation gives
\[
\alpha\cos x=\beta z x^2.
\]
The converse follows by reversing these algebraic steps, so this reduction is necessary and sufficient, without discarding branch or boundary solutions. If \(\beta\le1\), its nonnegative left side contradicts \(x>0\), hence no prime-two orbit exists. If \(1<\beta\le2\), then \(0<x<2R_\beta\le\sqrt2<\pi/2\), so \(\cos x>0\) and necessarily \(z>0\). Thus every prime-two orbit corresponds bijectively to one positive solution of \(Q_\beta(x)=\alpha\), with the orbit points above and \(z=\sqrt{R_\beta^2-x^2/4}\).

**2. Strict log concavity of the scalar fold curve.** Put \(A=4R_\beta^2\in(0,2]\). On \((0,\sqrt A)\),
\[
\frac{d^2}{dx^2}\log Q_\beta(x)
=\sec^2x-\frac2{x^2}-\frac{A+x^2}{(A-x^2)^2}.
\]
For fixed \(x\), \((A+x^2)/(A-x^2)^2\) is strictly decreasing in \(A>x^2\). Therefore its value at \(A\le2\) is at least \((2+x^2)/(2-x^2)^2\). To prove that the displayed second derivative is negative, set \(v=x^2\in(0,2)\). The alternating Taylor estimate for cosine gives
\[
\cos x>c(v):=1-\frac v2+\frac{v^2}{24}-\frac{v^3}{720}>0.
\]
Direct exact polynomial arithmetic yields
\[
\left(\frac2v+\frac{2+v}{(2-v)^2}-\frac1{c(v)^2}\right)
 v(2-v)^2c(v)^2=P(v),
\]
where
\[
P(v)=\frac{3v^8-186v^7+5228v^6-79320v^5+669600v^4
-3294720v^3+8121600v^2-9331200v+4147200}{518400}.
\]
For \(v=2t\), \(0\le t\le1\), its degree-eight Bernstein expansion has the positive coefficients (listed for indices \(0,\ldots,8\))
\[
\left(8,\frac72,\frac{26}{21},\frac{193}{630},\frac{29}{315},
\frac{1439}{7560},\frac{9631}{28350},\frac{1519}{4050},\frac{392}{2025}\right).
\]
That is, \(P(2t)=\sum_{j=0}^8 b_j\binom8j t^j(1-t)^{8-j}>0\). Consequently \(\sec^2x<2/x^2+(2+x^2)/(2-x^2)^2\), and \((\log Q_\beta)''<0\). As \(Q_\beta\) tends to zero at both ends and is positive inside, strict logarithmic concavity gives exactly one maximizer \(u_\beta\), with \(Q_\beta''(u_\beta)<0\), and exactly the root counts asserted.

**3. Threshold monotonicity and onset.** For a fixed admissible positive \(x\),
\[
\beta\sqrt{1-1/\beta-x^2/4}
=\sqrt{\beta^2(1-x^2/4)-\beta}
\]
is strictly increasing in \(\beta\), because the derivative of its squared radicand is \(2\beta(1-x^2/4)-1>1\) on the allowed domain. The domain \((0,2R_\beta)\) itself grows with \(\beta\). Evaluating at the previous maximizer proves strict increase of \(\alpha_*(\beta)\). Continuity follows from the rescaling \(x=2R_\beta s\), \(0\le s\le1\), and continuous dependence of a maximum on a compact interval.

Writing \(\varepsilon=\beta-1\downarrow0\), the same rescaling gives uniformly in \(s\in[0,1]\)
\[
Q_\beta(2R_\beta s)
=4\beta R_\beta^3s^2\sqrt{1-s^2}
\bigl(1+O(R_\beta^2)\bigr).
\]
The function \(s^2\sqrt{1-s^2}\) has unique maximum \(2/(3\sqrt3)\) at \(s=\sqrt{2/3}\), giving the three-halves law. A second-order Taylor expansion of \(Q_\beta\) at its nondegenerate maximum gives the stated square-root splitting.

**4. Concrete parameter check.** At the source's illustrative parameters \(\alpha=1/10\), \(\beta=17/10\), \(R_\beta^2=7/17\) and \(1<2R_\beta\). The explicit value
\[
Q_{17/10}(1)=\frac{17}{10\cos1}\sqrt{\frac{11}{68}}>\frac1{10}
\]
proves \(\alpha<\alpha_*(\beta)\) without numerical root hunting, and hence exactly two distinct prime-two orbits. Their positive first coordinates are approximately \(0.300116255656\) and \(1.283217899437\).

## Verification

Run `python verify.py` with Python 3 and SymPy. The standalone checker reconstructs the eliminated two-cycle equations symbolically; differentiates the log-fold curve; verifies the polynomial and all nine exact rational Bernstein coefficients and the Bernstein reconstruction; checks the onset maximizer; and independently finds and iterates both period-two cycles at three representative parameter values. The program reports successful exact checks and three pairs of periodic-orbit coordinates. These finite numerical tests are supplementary: the infinite census, log concavity, and asymptotic laws are proved above.

## Relationship to prior work

Almatroud and Pham, *Building Fixed Point-Free Maps with Memristor*, Mathematics **11** (2023), 1319, introduce the precise map (their FPFM1, equation (5)), establish absence of fixed points, and study its bifurcation plots and Lyapunov exponents numerically. Their article does not state a full prime-period-two orbit count, a sharp scalar fold boundary, or its three-halves scaling. The present result does **not** claim the map itself is new, nor that absence of fixed points is new. Two earlier, superficially related models are distinct: Ramadoss et al. (2022) couple a serial nonlinear sine term to a cosine-of-\(y\) memristance, whereas Zhang et al. (2022) use an additive constant and a cosine-of-\(y\) multiplicative coefficient. Neither their reported numerical periodic behavior nor exact short-cycle results on other planar families imply this cosine–quadratic-memristance census.

## Limitations

The complete census is limited to \(0<\beta\le2\), including the original article's studied interval, with positive \(\alpha\). For sufficiently large \(\beta\), the cosine factor changes sign within the algebraic ellipse and additional branches may arise; the strict-concavity certificate here covers only \(\beta\le2\). The theorem neither determines the linear stability of the two-cycles nor asserts an attracting cycle, global boundedness, a trapping region, chaotic behavior, or cryptographic performance. The origin of the map and its no-fixed-point property are prior work. An unindexed analysis of the same FPFM1 short-period equations remains a publication-priority risk. There has been no independent mathematical validation.

## References

1. O. A. Almatroud and V.-T. Pham, *Building Fixed Point-Free Maps with Memristor*, Mathematics **11** (2023), 1319, doi:10.3390/math11061319, first publicly dated 2023-03-09.
2. J. Ramadoss, O. A. Almatroud, S. Momani, V.-T. Pham, and V. P. Thoai, *Discrete Memristance and Nonlinear Term for Designing Memristive Maps*, Symmetry **14** (2022), 2110, doi:10.3390/sym14102110 (a distinct serial architecture).
3. L.-P. Zhang et al., *Extremely hidden multi-stability in a class of two-dimensional maps with a cosine memristor*, Chinese Physics B **31** (2022), 100503, doi:10.1088/1674-1056/ac7294 (cosine-of-\(y\) rather than cosine-of-\(x\)).
4. Research-index comparison: *Exact prime-two orbit census and coexistence wedge for the rational Rulkov neuron map*, record `2026/10/11/SCOPE-exact-prime-two-orbit-census-and-coexistence-wedge-for-the-ratio--7ffcf1ae63a3` (a distinct rational slow–fast model).
